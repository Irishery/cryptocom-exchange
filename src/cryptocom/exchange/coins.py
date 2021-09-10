from .structs import Coin

AAVE = Coin("AAVE")
ADA = Coin("ADA")
ALGO = Coin("ALGO")
ALICE = Coin("ALICE")
AMP = Coin("AMP")
ANKR = Coin("ANKR")
ATOM = Coin("ATOM")
AUDIO = Coin("AUDIO")
AVAX = Coin("AVAX")
AXS = Coin("AXS")
BAL = Coin("BAL")
BAND = Coin("BAND")
BAT = Coin("BAT")
BCH = Coin("BCH")
BNT = Coin("BNT")
BOSON = Coin("BOSON")
BTC = Coin("BTC")
CELR = Coin("CELR")
CHR = Coin("CHR")
CHZ = Coin("CHZ")
CKB = Coin("CKB")
COMP = Coin("COMP")
CQT = Coin("CQT")
CRO = Coin("CRO")
CRV = Coin("CRV")
CSPR = Coin("CSPR")
CTSI = Coin("CTSI")
DAI = Coin("DAI")
DERC = Coin("DERC")
DOGE = Coin("DOGE")
DOT = Coin("DOT")
DYDX = Coin("DYDX")
EFI = Coin("EFI")
EGLD = Coin("EGLD")
ENJ = Coin("ENJ")
EOS = Coin("EOS")
ETC = Coin("ETC")
ETH = Coin("ETH")
FARM = Coin("FARM")
FET = Coin("FET")
FIL = Coin("FIL")
FLOW = Coin("FLOW")
FORTH = Coin("FORTH")
FTM = Coin("FTM")
FXS = Coin("FXS")
GHST = Coin("GHST")
GRT = Coin("GRT")
GTC = Coin("GTC")
HNT = Coin("HNT")
HOT = Coin("HOT")
ICP = Coin("ICP")
ICX = Coin("ICX")
INJ = Coin("INJ")
IQ = Coin("IQ")
KAVA = Coin("KAVA")
KEEP = Coin("KEEP")
KNC = Coin("KNC")
KSM = Coin("KSM")
LINK = Coin("LINK")
LPT = Coin("LPT")
LRC = Coin("LRC")
LTC = Coin("LTC")
LUNA = Coin("LUNA")
MANA = Coin("MANA")
MASK = Coin("MASK")
MATIC = Coin("MATIC")
MCO = Coin("MCO")
MIR = Coin("MIR")
MKR = Coin("MKR")
MLN = Coin("MLN")
NANO = Coin("NANO")
NEAR = Coin("NEAR")
NEO = Coin("NEO")
NKN = Coin("NKN")
OCEAN = Coin("OCEAN")
OGN = Coin("OGN")
OMG = Coin("OMG")
ONE = Coin("ONE")
ONEINCH = Coin("1INCH")
ONT = Coin("ONT")
PAXG = Coin("PAXG")
PENDLE = Coin("PENDLE")
PLA = Coin("PLA")
POLY = Coin("POLY")
QNT = Coin("QNT")
QTUM = Coin("QTUM")
QUICK = Coin("QUICK")
RARI = Coin("RARI")
REN = Coin("REN")
RLC = Coin("RLC")
RLY = Coin("RLY")
RSR = Coin("RSR")
RUNE = Coin("RUNE")
RVN = Coin("RVN")
SAND = Coin("SAND")
SC = Coin("SC")
SHIB = Coin("SHIB")
SKL = Coin("SKL")
SLP = Coin("SLP")
SNX = Coin("SNX")
SOL = Coin("SOL")
STORJ = Coin("STORJ")
STX = Coin("STX")
SUSHI = Coin("SUSHI")
TFUEL = Coin("TFUEL")
THETA = Coin("THETA")
TRB = Coin("TRB")
UMA = Coin("UMA")
UNI = Coin("UNI")
USDC = Coin("USDC")
USDT = Coin("USDT")
VET = Coin("VET")
VTHO = Coin("VTHO")
WAVE = Coin("WAVE")
WAVES = Coin("WAVES")
WBTC = Coin("WBTC")
XLM = Coin("XLM")
XRP = Coin("XRP")
XTZ = Coin("XTZ")
YFI = Coin("YFI")
YGG = Coin("YGG")
ZIL = Coin("ZIL")
ZRX = Coin("ZRX")


def all():
    return [
        value for name, value in globals().items()
        if isinstance(value, Coin)
    ]
