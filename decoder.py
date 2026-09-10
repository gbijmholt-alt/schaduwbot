"""Decoder voor pump.fun Anchor-events uit 'Program data:'-logregels.
Discriminators worden berekend (sha256('event:<Naam>')[:8]) zodat er niets
hardcoded hoeft te worden. Layouts volgen de pump.fun IDL; velden achter de
kernvelden zijn optioneel (nieuwere programmaversies voegen velden toe)."""
import base64, hashlib, struct
from dataclasses import dataclass
from typing import Optional
import base58

def disc(name: str) -> bytes:
    return hashlib.sha256(f"event:{name}".encode()).digest()[:8]

D_TRADE = disc("TradeEvent")
D_CREATE = disc("CreateEvent")
D_COMPLETE = disc("CompleteEvent")

class _R:
    def __init__(self, b: bytes): self.b, self.i = b, 0
    def left(self): return len(self.b) - self.i
    def u64(self):
        v = struct.unpack_from("<Q", self.b, self.i)[0]; self.i += 8; return v
    def i64(self):
        v = struct.unpack_from("<q", self.b, self.i)[0]; self.i += 8; return v
    def boolean(self):
        v = self.b[self.i] != 0; self.i += 1; return v
    def pubkey(self):
        v = base58.b58encode(self.b[self.i:self.i+32]).decode(); self.i += 32; return v
    def string(self):
        n = struct.unpack_from("<I", self.b, self.i)[0]; self.i += 4
        v = self.b[self.i:self.i+n].decode("utf-8", "replace"); self.i += n; return v

@dataclass
class TradeEvent:
    mint: str; sol_amount: int; token_amount: int; is_buy: bool; user: str; timestamp: int
    v_sol: int; v_tok: int; r_sol: int; r_tok: int
    creator: Optional[str] = None

@dataclass
class CreateEvent:
    name: str; symbol: str; uri: str; mint: str; bonding_curve: str; user: str
    creator: Optional[str] = None; timestamp: Optional[int] = None
    v_tok: Optional[int] = None; v_sol: Optional[int] = None

@dataclass
class CompleteEvent:
    user: str; mint: str; bonding_curve: str; timestamp: int

def decode_program_data(line: str):
    """Geeft TradeEvent / CreateEvent / CompleteEvent of None."""
    if not line.startswith("Program data: "): return None
    try: raw = base64.b64decode(line[14:])
    except Exception: return None
    if len(raw) < 8: return None
    d, body = raw[:8], raw[8:]
    r = _R(body)
    try:
        if d == D_TRADE:
            ev = TradeEvent(r.pubkey(), r.u64(), r.u64(), r.boolean(), r.pubkey(), r.i64(), r.u64(), r.u64(), r.u64(), r.u64())
            # optionele staart: fee_recipient(32) fee_bps(8) fee(8) creator(32) ...
            if r.left() >= 32 + 8 + 8 + 32:
                r.pubkey(); r.u64(); r.u64(); ev.creator = r.pubkey()
            return ev
        if d == D_CREATE:
            ev = CreateEvent(r.string(), r.string(), r.string(), r.pubkey(), r.pubkey(), r.pubkey())
            if r.left() >= 32: ev.creator = r.pubkey()
            if r.left() >= 8: ev.timestamp = r.i64()
            if r.left() >= 16: ev.v_tok = r.u64(); ev.v_sol = r.u64()
            return ev
        if d == D_COMPLETE:
            return CompleteEvent(r.pubkey(), r.pubkey(), r.pubkey(), r.i64())
    except (struct.error, IndexError):
        return None
    return None

def decode_logs(logs):
    out = []
    for l in logs:
        ev = decode_program_data(l)
        if ev is not None: out.append(ev)
    return out
