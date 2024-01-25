from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence, Literal

Period = Literal[1, 5, 15, 30, 60, 120, 240, 360, 720, 1440, 4320, 10080]


@dataclass
class APIResponse:
    """A dataclass representing the response returned from Quidax servers.

    Every method on each client class provided by the pyquidax package returns
    an `APIResponse`
    """

    status_code: int
    status: Optional[str]
    message: Optional[str]
    data: Optional[dict]


class Currency(str, Enum):
    BITCOIN = "btc"
    LITECOIN = "ltc"
    DASH = "dash"
    TRON = "tron"
    QUIDAX_TOKEN = "qdx"
    ETHEREUM = "eth"
    RIPPLE = "xrp"
    BITCOIN_CASH = "bch"
    SOLANA = "sol"
    FLOKI_INU = "floki"
    WAKANDA_INU = "wkd"
    TEZOS = "xtz"
    HARMONY = "one"
    CARDANO = "ada"
    BABYDOGE = "babydoge"
    FILECOIN = "fil"
    AXIE_IFFINITY = "axa"
    STELLAR = "xlm"
    PANCAKE_SWAP = "cake"
    CHAINLINK = "link"
    POLKADOT = "dot"
    SHIBA_INU = "shib"
    AAVE = "aave"
    USD_COIN = "usdc"
    BINANCE_USD = "busd"
    POLYGON = "matic"
    BINANCE_COIN = "bnb"
    DOGECOIN = "doge"
    TETHER = "usdt"
    NAIRA = "ngn"


class Network(str, Enum):
    BTC = "btc"
    LTC = "ltc"
    DASH = "dash"
    TRC20 = "trc20"
    BEP20 = "bep20"
    ERC20 = "erc20"
    RIPPLE = "ripple"
    BHC = "bhc"
    CARDANO = "cardano"
    STELLAR = "stellar"
    DOGE = "doge"


class CurrencyPair(str, Enum):
    QDX_USDT = "qdxusdt"
    BTC_USDT = "btcusdt"
    BTC_NGN = "btcngn"
    ETH_NGN = "ethngn"
    QDX_NGN = "qdxngn"
    XRP_NGN = "xrpngn"
    DASH_NGN = "dashngn"
    LTC_NGN = "ltcngn"
    USDT_NGN = "usdtngn"
    BTC_GHS = "btcghs"
    USDT_GHS = "usdtghs"
    TRX_NGN = "trxngn"
    DOGE_USDT = "dogeusdt"
    BNB_USDT = "bnbusdt"
    MATIC_USDT = "maticusdt"
    SAFEMOOD_USDT = "safemoonusdt"
    AAVE_USDT = "aaveusdt"
    SHIB_USDT = "shibusdt"
    DOT_USDT = "dotusdt"
    LINK_USDT = "linkusdt"
    CAKE_USDT = "cakeusdt"
    XLM_USDT = "xlmusdt"
    XRP_USDT = "xrpusdt"
    LTC_USDT = "ltcusdt"
    ETH_USDT = "ethusdt"
    TRX_USDT = "trxusdt"
    AXS_USDT = "axsusdt"
    WSG_USDT = "wsgusdt"
    AFEN_USDT = "afenusdt"
    BLS_USDT = "blsusdt"
    DASH_USDT = "dashusdt"


class TransactionState(str, Enum):
    SUBMITTED = "submitted"
    PROCESSING = "processing"
    DONE = "done"
    REJECTED = "rejected"
    SUBMITTING = "submitting"
    CANCELED = "canceled"
    FAILED = "failed"
    ACCEPTED = "accepted"
    CHECKED = "checked"


class OrderState(str, Enum):
    DONE = "done"
    WAIT = "wait"
    CANCEL = "cancel"
    CONFIRM = "confirm"


class OrderType(str, Enum):
    BUY = "buy"
    SELL = "sell"


class Kind(str, Enum):
    ASK = "ask"
    BID = "bid"


class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


def append_query_parameters(url: str, query_params: Sequence) -> str:
    for key, value in query_params:
        if value:
            if "?" in url:
                url += f"&{key}={value}"
            else:
                url += f"?{key}={value}"
    return url
