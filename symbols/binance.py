from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ONEINCHBTC:
    name: str = "1INCHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "1INCHBTC"

    def __str__(self):
        return "1INCHBTC"

    def __call__(self):
        return "1INCHBTC"


ONEINCHBTC = ONEINCHBTC()


@dataclass(slots=True, frozen=True)
class ONEINCHBUSD:
    name: str = "1INCHBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "1INCHBUSD"

    def __str__(self):
        return "1INCHBUSD"

    def __call__(self):
        return "1INCHBUSD"


ONEINCHBUSD = ONEINCHBUSD()


@dataclass(slots=True, frozen=True)
class ONEINCHDOWNUSDT:
    name: str = "1INCHDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 2999958.00000000
    margin: bool = False

    def __repr__(self):
        return "1INCHDOWNUSDT"

    def __str__(self):
        return "1INCHDOWNUSDT"

    def __call__(self):
        return "1INCHDOWNUSDT"


ONEINCHDOWNUSDT = ONEINCHDOWNUSDT()


@dataclass(slots=True, frozen=True)
class ONEINCHUPUSDT:
    name: str = "1INCHUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 300000.00000000
    margin: bool = False

    def __repr__(self):
        return "1INCHUPUSDT"

    def __str__(self):
        return "1INCHUPUSDT"

    def __call__(self):
        return "1INCHUPUSDT"


ONEINCHUPUSDT = ONEINCHUPUSDT()


@dataclass(slots=True, frozen=True)
class ONEINCHUSDT:
    name: str = "1INCHUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "1INCHUSDT"

    def __str__(self):
        return "1INCHUSDT"

    def __call__(self):
        return "1INCHUSDT"


ONEINCHUSDT = ONEINCHUSDT()


@dataclass(slots=True, frozen=True)
class AAVEBKRW:
    name: str = "AAVEBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "AAVEBKRW"

    def __str__(self):
        return "AAVEBKRW"

    def __call__(self):
        return "AAVEBKRW"


AAVEBKRW = AAVEBKRW()


@dataclass(slots=True, frozen=True)
class AAVEBNB:
    name: str = "AAVEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "AAVEBNB"

    def __str__(self):
        return "AAVEBNB"

    def __call__(self):
        return "AAVEBNB"


AAVEBNB = AAVEBNB()


@dataclass(slots=True, frozen=True)
class AAVEBRL:
    name: str = "AAVEBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "AAVEBRL"

    def __str__(self):
        return "AAVEBRL"

    def __call__(self):
        return "AAVEBRL"


AAVEBRL = AAVEBRL()


@dataclass(slots=True, frozen=True)
class AAVEBTC:
    name: str = "AAVEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "AAVEBTC"

    def __str__(self):
        return "AAVEBTC"

    def __call__(self):
        return "AAVEBTC"


AAVEBTC = AAVEBTC()


@dataclass(slots=True, frozen=True)
class AAVEBUSD:
    name: str = "AAVEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "AAVEBUSD"

    def __str__(self):
        return "AAVEBUSD"

    def __call__(self):
        return "AAVEBUSD"


AAVEBUSD = AAVEBUSD()


@dataclass(slots=True, frozen=True)
class AAVEDOWNUSDT:
    name: str = "AAVEDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AAVEDOWNUSDT"

    def __str__(self):
        return "AAVEDOWNUSDT"

    def __call__(self):
        return "AAVEDOWNUSDT"


AAVEDOWNUSDT = AAVEDOWNUSDT()


@dataclass(slots=True, frozen=True)
class AAVEETH:
    name: str = "AAVEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AAVEETH"

    def __str__(self):
        return "AAVEETH"

    def __call__(self):
        return "AAVEETH"


AAVEETH = AAVEETH()


@dataclass(slots=True, frozen=True)
class AAVEUPUSDT:
    name: str = "AAVEUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "AAVEUPUSDT"

    def __str__(self):
        return "AAVEUPUSDT"

    def __call__(self):
        return "AAVEUPUSDT"


AAVEUPUSDT = AAVEUPUSDT()


@dataclass(slots=True, frozen=True)
class AAVEUSDT:
    name: str = "AAVEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "AAVEUSDT"

    def __str__(self):
        return "AAVEUSDT"

    def __call__(self):
        return "AAVEUSDT"


AAVEUSDT = AAVEUSDT()


@dataclass(slots=True, frozen=True)
class ACABTC:
    name: str = "ACABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ACABTC"

    def __str__(self):
        return "ACABTC"

    def __call__(self):
        return "ACABTC"


ACABTC = ACABTC()


@dataclass(slots=True, frozen=True)
class ACABUSD:
    name: str = "ACABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ACABUSD"

    def __str__(self):
        return "ACABUSD"

    def __call__(self):
        return "ACABUSD"


ACABUSD = ACABUSD()


@dataclass(slots=True, frozen=True)
class ACAUSDT:
    name: str = "ACAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ACAUSDT"

    def __str__(self):
        return "ACAUSDT"

    def __call__(self):
        return "ACAUSDT"


ACAUSDT = ACAUSDT()


@dataclass(slots=True, frozen=True)
class ACHBTC:
    name: str = "ACHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ACHBTC"

    def __str__(self):
        return "ACHBTC"

    def __call__(self):
        return "ACHBTC"


ACHBTC = ACHBTC()


@dataclass(slots=True, frozen=True)
class ACHBUSD:
    name: str = "ACHBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "ACHBUSD"

    def __str__(self):
        return "ACHBUSD"

    def __call__(self):
        return "ACHBUSD"


ACHBUSD = ACHBUSD()


@dataclass(slots=True, frozen=True)
class ACHUSDT:
    name: str = "ACHUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "ACHUSDT"

    def __str__(self):
        return "ACHUSDT"

    def __call__(self):
        return "ACHUSDT"


ACHUSDT = ACHUSDT()


@dataclass(slots=True, frozen=True)
class ACMBTC:
    name: str = "ACMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ACMBTC"

    def __str__(self):
        return "ACMBTC"

    def __call__(self):
        return "ACMBTC"


ACMBTC = ACMBTC()


@dataclass(slots=True, frozen=True)
class ACMBUSD:
    name: str = "ACMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ACMBUSD"

    def __str__(self):
        return "ACMBUSD"

    def __call__(self):
        return "ACMBUSD"


ACMBUSD = ACMBUSD()


@dataclass(slots=True, frozen=True)
class ACMUSDT:
    name: str = "ACMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ACMUSDT"

    def __str__(self):
        return "ACMUSDT"

    def __call__(self):
        return "ACMUSDT"


ACMUSDT = ACMUSDT()


@dataclass(slots=True, frozen=True)
class ADAAUD:
    name: str = "ADAAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ADAAUD"

    def __str__(self):
        return "ADAAUD"

    def __call__(self):
        return "ADAAUD"


ADAAUD = ADAAUD()


@dataclass(slots=True, frozen=True)
class ADABIDR:
    name: str = "ADABIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 184467.00000000
    margin: bool = False

    def __repr__(self):
        return "ADABIDR"

    def __str__(self):
        return "ADABIDR"

    def __call__(self):
        return "ADABIDR"


ADABIDR = ADABIDR()


@dataclass(slots=True, frozen=True)
class ADABKRW:
    name: str = "ADABKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ADABKRW"

    def __str__(self):
        return "ADABKRW"

    def __call__(self):
        return "ADABKRW"


ADABKRW = ADABKRW()


@dataclass(slots=True, frozen=True)
class ADABNB:
    name: str = "ADABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADABNB"

    def __str__(self):
        return "ADABNB"

    def __call__(self):
        return "ADABNB"


ADABNB = ADABNB()


@dataclass(slots=True, frozen=True)
class ADABRL:
    name: str = "ADABRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ADABRL"

    def __str__(self):
        return "ADABRL"

    def __call__(self):
        return "ADABRL"


ADABRL = ADABRL()


@dataclass(slots=True, frozen=True)
class ADABTC:
    name: str = "ADABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ADABTC"

    def __str__(self):
        return "ADABTC"

    def __call__(self):
        return "ADABTC"


ADABTC = ADABTC()


@dataclass(slots=True, frozen=True)
class ADABUSD:
    name: str = "ADABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ADABUSD"

    def __str__(self):
        return "ADABUSD"

    def __call__(self):
        return "ADABUSD"


ADABUSD = ADABUSD()


@dataclass(slots=True, frozen=True)
class ADADOWNUSDT:
    name: str = "ADADOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADADOWNUSDT"

    def __str__(self):
        return "ADADOWNUSDT"

    def __call__(self):
        return "ADADOWNUSDT"


ADADOWNUSDT = ADADOWNUSDT()


@dataclass(slots=True, frozen=True)
class ADAETH:
    name: str = "ADAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ADAETH"

    def __str__(self):
        return "ADAETH"

    def __call__(self):
        return "ADAETH"


ADAETH = ADAETH()


@dataclass(slots=True, frozen=True)
class ADAEUR:
    name: str = "ADAEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADAEUR"

    def __str__(self):
        return "ADAEUR"

    def __call__(self):
        return "ADAEUR"


ADAEUR = ADAEUR()


@dataclass(slots=True, frozen=True)
class ADAGBP:
    name: str = "ADAGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADAGBP"

    def __str__(self):
        return "ADAGBP"

    def __call__(self):
        return "ADAGBP"


ADAGBP = ADAGBP()


@dataclass(slots=True, frozen=True)
class ADAPAX:
    name: str = "ADAPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADAPAX"

    def __str__(self):
        return "ADAPAX"

    def __call__(self):
        return "ADAPAX"


ADAPAX = ADAPAX()


@dataclass(slots=True, frozen=True)
class ADARUB:
    name: str = "ADARUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ADARUB"

    def __str__(self):
        return "ADARUB"

    def __call__(self):
        return "ADARUB"


ADARUB = ADARUB()


@dataclass(slots=True, frozen=True)
class ADATRY:
    name: str = "ADATRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ADATRY"

    def __str__(self):
        return "ADATRY"

    def __call__(self):
        return "ADATRY"


ADATRY = ADATRY()


@dataclass(slots=True, frozen=True)
class ADATUSD:
    name: str = "ADATUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADATUSD"

    def __str__(self):
        return "ADATUSD"

    def __call__(self):
        return "ADATUSD"


ADATUSD = ADATUSD()


@dataclass(slots=True, frozen=True)
class ADAUPUSDT:
    name: str = "ADAUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADAUPUSDT"

    def __str__(self):
        return "ADAUPUSDT"

    def __call__(self):
        return "ADAUPUSDT"


ADAUPUSDT = ADAUPUSDT()


@dataclass(slots=True, frozen=True)
class ADAUSDC:
    name: str = "ADAUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADAUSDC"

    def __str__(self):
        return "ADAUSDC"

    def __call__(self):
        return "ADAUSDC"


ADAUSDC = ADAUSDC()


@dataclass(slots=True, frozen=True)
class ADAUSDT:
    name: str = "ADAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ADAUSDT"

    def __str__(self):
        return "ADAUSDT"

    def __call__(self):
        return "ADAUSDT"


ADAUSDT = ADAUSDT()


@dataclass(slots=True, frozen=True)
class ADXBNB:
    name: str = "ADXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADXBNB"

    def __str__(self):
        return "ADXBNB"

    def __call__(self):
        return "ADXBNB"


ADXBNB = ADXBNB()


@dataclass(slots=True, frozen=True)
class ADXBTC:
    name: str = "ADXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADXBTC"

    def __str__(self):
        return "ADXBTC"

    def __call__(self):
        return "ADXBTC"


ADXBTC = ADXBTC()


@dataclass(slots=True, frozen=True)
class ADXBUSD:
    name: str = "ADXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ADXBUSD"

    def __str__(self):
        return "ADXBUSD"

    def __call__(self):
        return "ADXBUSD"


ADXBUSD = ADXBUSD()


@dataclass(slots=True, frozen=True)
class ADXETH:
    name: str = "ADXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ADXETH"

    def __str__(self):
        return "ADXETH"

    def __call__(self):
        return "ADXETH"


ADXETH = ADXETH()


@dataclass(slots=True, frozen=True)
class ADXUSDT:
    name: str = "ADXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ADXUSDT"

    def __str__(self):
        return "ADXUSDT"

    def __call__(self):
        return "ADXUSDT"


ADXUSDT = ADXUSDT()


@dataclass(slots=True, frozen=True)
class AEBNB:
    name: str = "AEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AEBNB"

    def __str__(self):
        return "AEBNB"

    def __call__(self):
        return "AEBNB"


AEBNB = AEBNB()


@dataclass(slots=True, frozen=True)
class AEBTC:
    name: str = "AEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AEBTC"

    def __str__(self):
        return "AEBTC"

    def __call__(self):
        return "AEBTC"


AEBTC = AEBTC()


@dataclass(slots=True, frozen=True)
class AEETH:
    name: str = "AEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AEETH"

    def __str__(self):
        return "AEETH"

    def __call__(self):
        return "AEETH"


AEETH = AEETH()


@dataclass(slots=True, frozen=True)
class AERGOBTC:
    name: str = "AERGOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AERGOBTC"

    def __str__(self):
        return "AERGOBTC"

    def __call__(self):
        return "AERGOBTC"


AERGOBTC = AERGOBTC()


@dataclass(slots=True, frozen=True)
class AERGOBUSD:
    name: str = "AERGOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AERGOBUSD"

    def __str__(self):
        return "AERGOBUSD"

    def __call__(self):
        return "AERGOBUSD"


AERGOBUSD = AERGOBUSD()


@dataclass(slots=True, frozen=True)
class AGIBNB:
    name: str = "AGIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AGIBNB"

    def __str__(self):
        return "AGIBNB"

    def __call__(self):
        return "AGIBNB"


AGIBNB = AGIBNB()


@dataclass(slots=True, frozen=True)
class AGIBTC:
    name: str = "AGIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AGIBTC"

    def __str__(self):
        return "AGIBTC"

    def __call__(self):
        return "AGIBTC"


AGIBTC = AGIBTC()


@dataclass(slots=True, frozen=True)
class AGIETH:
    name: str = "AGIETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AGIETH"

    def __str__(self):
        return "AGIETH"

    def __call__(self):
        return "AGIETH"


AGIETH = AGIETH()


@dataclass(slots=True, frozen=True)
class AGIXBTC:
    name: str = "AGIXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AGIXBTC"

    def __str__(self):
        return "AGIXBTC"

    def __call__(self):
        return "AGIXBTC"


AGIXBTC = AGIXBTC()


@dataclass(slots=True, frozen=True)
class AGIXBUSD:
    name: str = "AGIXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AGIXBUSD"

    def __str__(self):
        return "AGIXBUSD"

    def __call__(self):
        return "AGIXBUSD"


AGIXBUSD = AGIXBUSD()


@dataclass(slots=True, frozen=True)
class AGLDBNB:
    name: str = "AGLDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AGLDBNB"

    def __str__(self):
        return "AGLDBNB"

    def __call__(self):
        return "AGLDBNB"


AGLDBNB = AGLDBNB()


@dataclass(slots=True, frozen=True)
class AGLDBTC:
    name: str = "AGLDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "AGLDBTC"

    def __str__(self):
        return "AGLDBTC"

    def __call__(self):
        return "AGLDBTC"


AGLDBTC = AGLDBTC()


@dataclass(slots=True, frozen=True)
class AGLDBUSD:
    name: str = "AGLDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "AGLDBUSD"

    def __str__(self):
        return "AGLDBUSD"

    def __call__(self):
        return "AGLDBUSD"


AGLDBUSD = AGLDBUSD()


@dataclass(slots=True, frozen=True)
class AGLDUSDT:
    name: str = "AGLDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "AGLDUSDT"

    def __str__(self):
        return "AGLDUSDT"

    def __call__(self):
        return "AGLDUSDT"


AGLDUSDT = AGLDUSDT()


@dataclass(slots=True, frozen=True)
class AIONBNB:
    name: str = "AIONBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AIONBNB"

    def __str__(self):
        return "AIONBNB"

    def __call__(self):
        return "AIONBNB"


AIONBNB = AIONBNB()


@dataclass(slots=True, frozen=True)
class AIONBTC:
    name: str = "AIONBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AIONBTC"

    def __str__(self):
        return "AIONBTC"

    def __call__(self):
        return "AIONBTC"


AIONBTC = AIONBTC()


@dataclass(slots=True, frozen=True)
class AIONBUSD:
    name: str = "AIONBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "AIONBUSD"

    def __str__(self):
        return "AIONBUSD"

    def __call__(self):
        return "AIONBUSD"


AIONBUSD = AIONBUSD()


@dataclass(slots=True, frozen=True)
class AIONETH:
    name: str = "AIONETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AIONETH"

    def __str__(self):
        return "AIONETH"

    def __call__(self):
        return "AIONETH"


AIONETH = AIONETH()


@dataclass(slots=True, frozen=True)
class AIONUSDT:
    name: str = "AIONUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "AIONUSDT"

    def __str__(self):
        return "AIONUSDT"

    def __call__(self):
        return "AIONUSDT"


AIONUSDT = AIONUSDT()


@dataclass(slots=True, frozen=True)
class AKROBTC:
    name: str = "AKROBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AKROBTC"

    def __str__(self):
        return "AKROBTC"

    def __call__(self):
        return "AKROBTC"


AKROBTC = AKROBTC()


@dataclass(slots=True, frozen=True)
class AKROBUSD:
    name: str = "AKROBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AKROBUSD"

    def __str__(self):
        return "AKROBUSD"

    def __call__(self):
        return "AKROBUSD"


AKROBUSD = AKROBUSD()


@dataclass(slots=True, frozen=True)
class AKROUSDT:
    name: str = "AKROUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "AKROUSDT"

    def __str__(self):
        return "AKROUSDT"

    def __call__(self):
        return "AKROUSDT"


AKROUSDT = AKROUSDT()


@dataclass(slots=True, frozen=True)
class ALCXBTC:
    name: str = "ALCXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALCXBTC"

    def __str__(self):
        return "ALCXBTC"

    def __call__(self):
        return "ALCXBTC"


ALCXBTC = ALCXBTC()


@dataclass(slots=True, frozen=True)
class ALCXBUSD:
    name: str = "ALCXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "ALCXBUSD"

    def __str__(self):
        return "ALCXBUSD"

    def __call__(self):
        return "ALCXBUSD"


ALCXBUSD = ALCXBUSD()


@dataclass(slots=True, frozen=True)
class ALCXUSDT:
    name: str = "ALCXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "ALCXUSDT"

    def __str__(self):
        return "ALCXUSDT"

    def __call__(self):
        return "ALCXUSDT"


ALCXUSDT = ALCXUSDT()


@dataclass(slots=True, frozen=True)
class ALGOBIDR:
    name: str = "ALGOBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9223371114.00000000
    margin: bool = False

    def __repr__(self):
        return "ALGOBIDR"

    def __str__(self):
        return "ALGOBIDR"

    def __call__(self):
        return "ALGOBIDR"


ALGOBIDR = ALGOBIDR()


@dataclass(slots=True, frozen=True)
class ALGOBNB:
    name: str = "ALGOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ALGOBNB"

    def __str__(self):
        return "ALGOBNB"

    def __call__(self):
        return "ALGOBNB"


ALGOBNB = ALGOBNB()


@dataclass(slots=True, frozen=True)
class ALGOBTC:
    name: str = "ALGOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ALGOBTC"

    def __str__(self):
        return "ALGOBTC"

    def __call__(self):
        return "ALGOBTC"


ALGOBTC = ALGOBTC()


@dataclass(slots=True, frozen=True)
class ALGOBUSD:
    name: str = "ALGOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ALGOBUSD"

    def __str__(self):
        return "ALGOBUSD"

    def __call__(self):
        return "ALGOBUSD"


ALGOBUSD = ALGOBUSD()


@dataclass(slots=True, frozen=True)
class ALGOETH:
    name: str = "ALGOETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALGOETH"

    def __str__(self):
        return "ALGOETH"

    def __call__(self):
        return "ALGOETH"


ALGOETH = ALGOETH()


@dataclass(slots=True, frozen=True)
class ALGOPAX:
    name: str = "ALGOPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ALGOPAX"

    def __str__(self):
        return "ALGOPAX"

    def __call__(self):
        return "ALGOPAX"


ALGOPAX = ALGOPAX()


@dataclass(slots=True, frozen=True)
class ALGORUB:
    name: str = "ALGORUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ALGORUB"

    def __str__(self):
        return "ALGORUB"

    def __call__(self):
        return "ALGORUB"


ALGORUB = ALGORUB()


@dataclass(slots=True, frozen=True)
class ALGOTRY:
    name: str = "ALGOTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALGOTRY"

    def __str__(self):
        return "ALGOTRY"

    def __call__(self):
        return "ALGOTRY"


ALGOTRY = ALGOTRY()


@dataclass(slots=True, frozen=True)
class ALGOTUSD:
    name: str = "ALGOTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ALGOTUSD"

    def __str__(self):
        return "ALGOTUSD"

    def __call__(self):
        return "ALGOTUSD"


ALGOTUSD = ALGOTUSD()


@dataclass(slots=True, frozen=True)
class ALGOUSDC:
    name: str = "ALGOUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ALGOUSDC"

    def __str__(self):
        return "ALGOUSDC"

    def __call__(self):
        return "ALGOUSDC"


ALGOUSDC = ALGOUSDC()


@dataclass(slots=True, frozen=True)
class ALGOUSDT:
    name: str = "ALGOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "ALGOUSDT"

    def __str__(self):
        return "ALGOUSDT"

    def __call__(self):
        return "ALGOUSDT"


ALGOUSDT = ALGOUSDT()


@dataclass(slots=True, frozen=True)
class ALICEBIDR:
    name: str = "ALICEBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922337194.00000000
    margin: bool = False

    def __repr__(self):
        return "ALICEBIDR"

    def __str__(self):
        return "ALICEBIDR"

    def __call__(self):
        return "ALICEBIDR"


ALICEBIDR = ALICEBIDR()


@dataclass(slots=True, frozen=True)
class ALICEBNB:
    name: str = "ALICEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALICEBNB"

    def __str__(self):
        return "ALICEBNB"

    def __call__(self):
        return "ALICEBNB"


ALICEBNB = ALICEBNB()


@dataclass(slots=True, frozen=True)
class ALICEBTC:
    name: str = "ALICEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ALICEBTC"

    def __str__(self):
        return "ALICEBTC"

    def __call__(self):
        return "ALICEBTC"


ALICEBTC = ALICEBTC()


@dataclass(slots=True, frozen=True)
class ALICEBUSD:
    name: str = "ALICEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ALICEBUSD"

    def __str__(self):
        return "ALICEBUSD"

    def __call__(self):
        return "ALICEBUSD"


ALICEBUSD = ALICEBUSD()


@dataclass(slots=True, frozen=True)
class ALICETRY:
    name: str = "ALICETRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ALICETRY"

    def __str__(self):
        return "ALICETRY"

    def __call__(self):
        return "ALICETRY"


ALICETRY = ALICETRY()


@dataclass(slots=True, frozen=True)
class ALICEUSDT:
    name: str = "ALICEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ALICEUSDT"

    def __str__(self):
        return "ALICEUSDT"

    def __call__(self):
        return "ALICEUSDT"


ALICEUSDT = ALICEUSDT()


@dataclass(slots=True, frozen=True)
class ALPACABNB:
    name: str = "ALPACABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPACABNB"

    def __str__(self):
        return "ALPACABNB"

    def __call__(self):
        return "ALPACABNB"


ALPACABNB = ALPACABNB()


@dataclass(slots=True, frozen=True)
class ALPACABTC:
    name: str = "ALPACABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPACABTC"

    def __str__(self):
        return "ALPACABTC"

    def __call__(self):
        return "ALPACABTC"


ALPACABTC = ALPACABTC()


@dataclass(slots=True, frozen=True)
class ALPACABUSD:
    name: str = "ALPACABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPACABUSD"

    def __str__(self):
        return "ALPACABUSD"

    def __call__(self):
        return "ALPACABUSD"


ALPACABUSD = ALPACABUSD()


@dataclass(slots=True, frozen=True)
class ALPACAUSDT:
    name: str = "ALPACAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPACAUSDT"

    def __str__(self):
        return "ALPACAUSDT"

    def __call__(self):
        return "ALPACAUSDT"


ALPACAUSDT = ALPACAUSDT()


@dataclass(slots=True, frozen=True)
class ALPHABNB:
    name: str = "ALPHABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPHABNB"

    def __str__(self):
        return "ALPHABNB"

    def __call__(self):
        return "ALPHABNB"


ALPHABNB = ALPHABNB()


@dataclass(slots=True, frozen=True)
class ALPHABTC:
    name: str = "ALPHABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ALPHABTC"

    def __str__(self):
        return "ALPHABTC"

    def __call__(self):
        return "ALPHABTC"


ALPHABTC = ALPHABTC()


@dataclass(slots=True, frozen=True)
class ALPHABUSD:
    name: str = "ALPHABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPHABUSD"

    def __str__(self):
        return "ALPHABUSD"

    def __call__(self):
        return "ALPHABUSD"


ALPHABUSD = ALPHABUSD()


@dataclass(slots=True, frozen=True)
class ALPHAUSDT:
    name: str = "ALPHAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ALPHAUSDT"

    def __str__(self):
        return "ALPHAUSDT"

    def __call__(self):
        return "ALPHAUSDT"


ALPHAUSDT = ALPHAUSDT()


@dataclass(slots=True, frozen=True)
class ALPINEBTC:
    name: str = "ALPINEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPINEBTC"

    def __str__(self):
        return "ALPINEBTC"

    def __call__(self):
        return "ALPINEBTC"


ALPINEBTC = ALPINEBTC()


@dataclass(slots=True, frozen=True)
class ALPINEBUSD:
    name: str = "ALPINEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPINEBUSD"

    def __str__(self):
        return "ALPINEBUSD"

    def __call__(self):
        return "ALPINEBUSD"


ALPINEBUSD = ALPINEBUSD()


@dataclass(slots=True, frozen=True)
class ALPINEEUR:
    name: str = "ALPINEEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPINEEUR"

    def __str__(self):
        return "ALPINEEUR"

    def __call__(self):
        return "ALPINEEUR"


ALPINEEUR = ALPINEEUR()


@dataclass(slots=True, frozen=True)
class ALPINETRY:
    name: str = "ALPINETRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPINETRY"

    def __str__(self):
        return "ALPINETRY"

    def __call__(self):
        return "ALPINETRY"


ALPINETRY = ALPINETRY()


@dataclass(slots=True, frozen=True)
class ALPINEUSDT:
    name: str = "ALPINEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ALPINEUSDT"

    def __str__(self):
        return "ALPINEUSDT"

    def __call__(self):
        return "ALPINEUSDT"


ALPINEUSDT = ALPINEUSDT()


@dataclass(slots=True, frozen=True)
class AMBBNB:
    name: str = "AMBBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AMBBNB"

    def __str__(self):
        return "AMBBNB"

    def __call__(self):
        return "AMBBNB"


AMBBNB = AMBBNB()


@dataclass(slots=True, frozen=True)
class AMBBTC:
    name: str = "AMBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AMBBTC"

    def __str__(self):
        return "AMBBTC"

    def __call__(self):
        return "AMBBTC"


AMBBTC = AMBBTC()


@dataclass(slots=True, frozen=True)
class AMBBUSD:
    name: str = "AMBBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = True

    def __repr__(self):
        return "AMBBUSD"

    def __str__(self):
        return "AMBBUSD"

    def __call__(self):
        return "AMBBUSD"


AMBBUSD = AMBBUSD()


@dataclass(slots=True, frozen=True)
class AMBETH:
    name: str = "AMBETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AMBETH"

    def __str__(self):
        return "AMBETH"

    def __call__(self):
        return "AMBETH"


AMBETH = AMBETH()


@dataclass(slots=True, frozen=True)
class AMPBNB:
    name: str = "AMPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AMPBNB"

    def __str__(self):
        return "AMPBNB"

    def __call__(self):
        return "AMPBNB"


AMPBNB = AMPBNB()


@dataclass(slots=True, frozen=True)
class AMPBTC:
    name: str = "AMPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AMPBTC"

    def __str__(self):
        return "AMPBTC"

    def __call__(self):
        return "AMPBTC"


AMPBTC = AMPBTC()


@dataclass(slots=True, frozen=True)
class AMPBUSD:
    name: str = "AMPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AMPBUSD"

    def __str__(self):
        return "AMPBUSD"

    def __call__(self):
        return "AMPBUSD"


AMPBUSD = AMPBUSD()


@dataclass(slots=True, frozen=True)
class AMPUSDT:
    name: str = "AMPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AMPUSDT"

    def __str__(self):
        return "AMPUSDT"

    def __call__(self):
        return "AMPUSDT"


AMPUSDT = AMPUSDT()


@dataclass(slots=True, frozen=True)
class ANCBNB:
    name: str = "ANCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ANCBNB"

    def __str__(self):
        return "ANCBNB"

    def __call__(self):
        return "ANCBNB"


ANCBNB = ANCBNB()


@dataclass(slots=True, frozen=True)
class ANCBTC:
    name: str = "ANCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ANCBTC"

    def __str__(self):
        return "ANCBTC"

    def __call__(self):
        return "ANCBTC"


ANCBTC = ANCBTC()


@dataclass(slots=True, frozen=True)
class ANCBUSD:
    name: str = "ANCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ANCBUSD"

    def __str__(self):
        return "ANCBUSD"

    def __call__(self):
        return "ANCBUSD"


ANCBUSD = ANCBUSD()


@dataclass(slots=True, frozen=True)
class ANCUSDT:
    name: str = "ANCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ANCUSDT"

    def __str__(self):
        return "ANCUSDT"

    def __call__(self):
        return "ANCUSDT"


ANCUSDT = ANCUSDT()


@dataclass(slots=True, frozen=True)
class ANKRBNB:
    name: str = "ANKRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ANKRBNB"

    def __str__(self):
        return "ANKRBNB"

    def __call__(self):
        return "ANKRBNB"


ANKRBNB = ANKRBNB()


@dataclass(slots=True, frozen=True)
class ANKRBTC:
    name: str = "ANKRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ANKRBTC"

    def __str__(self):
        return "ANKRBTC"

    def __call__(self):
        return "ANKRBTC"


ANKRBTC = ANKRBTC()


@dataclass(slots=True, frozen=True)
class ANKRBUSD:
    name: str = "ANKRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "ANKRBUSD"

    def __str__(self):
        return "ANKRBUSD"

    def __call__(self):
        return "ANKRBUSD"


ANKRBUSD = ANKRBUSD()


@dataclass(slots=True, frozen=True)
class ANKRPAX:
    name: str = "ANKRPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ANKRPAX"

    def __str__(self):
        return "ANKRPAX"

    def __call__(self):
        return "ANKRPAX"


ANKRPAX = ANKRPAX()


@dataclass(slots=True, frozen=True)
class ANKRTRY:
    name: str = "ANKRTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ANKRTRY"

    def __str__(self):
        return "ANKRTRY"

    def __call__(self):
        return "ANKRTRY"


ANKRTRY = ANKRTRY()


@dataclass(slots=True, frozen=True)
class ANKRTUSD:
    name: str = "ANKRTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ANKRTUSD"

    def __str__(self):
        return "ANKRTUSD"

    def __call__(self):
        return "ANKRTUSD"


ANKRTUSD = ANKRTUSD()


@dataclass(slots=True, frozen=True)
class ANKRUSDC:
    name: str = "ANKRUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ANKRUSDC"

    def __str__(self):
        return "ANKRUSDC"

    def __call__(self):
        return "ANKRUSDC"


ANKRUSDC = ANKRUSDC()


@dataclass(slots=True, frozen=True)
class ANKRUSDT:
    name: str = "ANKRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ANKRUSDT"

    def __str__(self):
        return "ANKRUSDT"

    def __call__(self):
        return "ANKRUSDT"


ANKRUSDT = ANKRUSDT()


@dataclass(slots=True, frozen=True)
class ANTBNB:
    name: str = "ANTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ANTBNB"

    def __str__(self):
        return "ANTBNB"

    def __call__(self):
        return "ANTBNB"


ANTBNB = ANTBNB()


@dataclass(slots=True, frozen=True)
class ANTBTC:
    name: str = "ANTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ANTBTC"

    def __str__(self):
        return "ANTBTC"

    def __call__(self):
        return "ANTBTC"


ANTBTC = ANTBTC()


@dataclass(slots=True, frozen=True)
class ANTBUSD:
    name: str = "ANTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ANTBUSD"

    def __str__(self):
        return "ANTBUSD"

    def __call__(self):
        return "ANTBUSD"


ANTBUSD = ANTBUSD()


@dataclass(slots=True, frozen=True)
class ANTUSDT:
    name: str = "ANTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ANTUSDT"

    def __str__(self):
        return "ANTUSDT"

    def __call__(self):
        return "ANTUSDT"


ANTUSDT = ANTUSDT()


@dataclass(slots=True, frozen=True)
class ANYBTC:
    name: str = "ANYBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ANYBTC"

    def __str__(self):
        return "ANYBTC"

    def __call__(self):
        return "ANYBTC"


ANYBTC = ANYBTC()


@dataclass(slots=True, frozen=True)
class ANYBUSD:
    name: str = "ANYBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ANYBUSD"

    def __str__(self):
        return "ANYBUSD"

    def __call__(self):
        return "ANYBUSD"


ANYBUSD = ANYBUSD()


@dataclass(slots=True, frozen=True)
class ANYUSDT:
    name: str = "ANYUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ANYUSDT"

    def __str__(self):
        return "ANYUSDT"

    def __call__(self):
        return "ANYUSDT"


ANYUSDT = ANYUSDT()


@dataclass(slots=True, frozen=True)
class APEAUD:
    name: str = "APEAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "APEAUD"

    def __str__(self):
        return "APEAUD"

    def __call__(self):
        return "APEAUD"


APEAUD = APEAUD()


@dataclass(slots=True, frozen=True)
class APEBNB:
    name: str = "APEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "APEBNB"

    def __str__(self):
        return "APEBNB"

    def __call__(self):
        return "APEBNB"


APEBNB = APEBNB()


@dataclass(slots=True, frozen=True)
class APEBRL:
    name: str = "APEBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "APEBRL"

    def __str__(self):
        return "APEBRL"

    def __call__(self):
        return "APEBRL"


APEBRL = APEBRL()


@dataclass(slots=True, frozen=True)
class APEBTC:
    name: str = "APEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "APEBTC"

    def __str__(self):
        return "APEBTC"

    def __call__(self):
        return "APEBTC"


APEBTC = APEBTC()


@dataclass(slots=True, frozen=True)
class APEBUSD:
    name: str = "APEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "APEBUSD"

    def __str__(self):
        return "APEBUSD"

    def __call__(self):
        return "APEBUSD"


APEBUSD = APEBUSD()


@dataclass(slots=True, frozen=True)
class APEETH:
    name: str = "APEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "APEETH"

    def __str__(self):
        return "APEETH"

    def __call__(self):
        return "APEETH"


APEETH = APEETH()


@dataclass(slots=True, frozen=True)
class APEEUR:
    name: str = "APEEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "APEEUR"

    def __str__(self):
        return "APEEUR"

    def __call__(self):
        return "APEEUR"


APEEUR = APEEUR()


@dataclass(slots=True, frozen=True)
class APEGBP:
    name: str = "APEGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "APEGBP"

    def __str__(self):
        return "APEGBP"

    def __call__(self):
        return "APEGBP"


APEGBP = APEGBP()


@dataclass(slots=True, frozen=True)
class APETRY:
    name: str = "APETRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "APETRY"

    def __str__(self):
        return "APETRY"

    def __call__(self):
        return "APETRY"


APETRY = APETRY()


@dataclass(slots=True, frozen=True)
class APEUSDT:
    name: str = "APEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "APEUSDT"

    def __str__(self):
        return "APEUSDT"

    def __call__(self):
        return "APEUSDT"


APEUSDT = APEUSDT()


@dataclass(slots=True, frozen=True)
class API3BNB:
    name: str = "API3BNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "API3BNB"

    def __str__(self):
        return "API3BNB"

    def __call__(self):
        return "API3BNB"


API3BNB = API3BNB()


@dataclass(slots=True, frozen=True)
class API3BTC:
    name: str = "API3BTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "API3BTC"

    def __str__(self):
        return "API3BTC"

    def __call__(self):
        return "API3BTC"


API3BTC = API3BTC()


@dataclass(slots=True, frozen=True)
class API3BUSD:
    name: str = "API3BUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "API3BUSD"

    def __str__(self):
        return "API3BUSD"

    def __call__(self):
        return "API3BUSD"


API3BUSD = API3BUSD()


@dataclass(slots=True, frozen=True)
class API3TRY:
    name: str = "API3TRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "API3TRY"

    def __str__(self):
        return "API3TRY"

    def __call__(self):
        return "API3TRY"


API3TRY = API3TRY()


@dataclass(slots=True, frozen=True)
class API3USDT:
    name: str = "API3USDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "API3USDT"

    def __str__(self):
        return "API3USDT"

    def __call__(self):
        return "API3USDT"


API3USDT = API3USDT()


@dataclass(slots=True, frozen=True)
class APPCBNB:
    name: str = "APPCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "APPCBNB"

    def __str__(self):
        return "APPCBNB"

    def __call__(self):
        return "APPCBNB"


APPCBNB = APPCBNB()


@dataclass(slots=True, frozen=True)
class APPCBTC:
    name: str = "APPCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "APPCBTC"

    def __str__(self):
        return "APPCBTC"

    def __call__(self):
        return "APPCBTC"


APPCBTC = APPCBTC()


@dataclass(slots=True, frozen=True)
class APPCETH:
    name: str = "APPCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "APPCETH"

    def __str__(self):
        return "APPCETH"

    def __call__(self):
        return "APPCETH"


APPCETH = APPCETH()


@dataclass(slots=True, frozen=True)
class APTBRL:
    name: str = "APTBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "APTBRL"

    def __str__(self):
        return "APTBRL"

    def __call__(self):
        return "APTBRL"


APTBRL = APTBRL()


@dataclass(slots=True, frozen=True)
class APTBTC:
    name: str = "APTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 8384883677.00000000
    margin: bool = False

    def __repr__(self):
        return "APTBTC"

    def __str__(self):
        return "APTBTC"

    def __call__(self):
        return "APTBTC"


APTBTC = APTBTC()


@dataclass(slots=True, frozen=True)
class APTBUSD:
    name: str = "APTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "APTBUSD"

    def __str__(self):
        return "APTBUSD"

    def __call__(self):
        return "APTBUSD"


APTBUSD = APTBUSD()


@dataclass(slots=True, frozen=True)
class APTEUR:
    name: str = "APTEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "APTEUR"

    def __str__(self):
        return "APTEUR"

    def __call__(self):
        return "APTEUR"


APTEUR = APTEUR()


@dataclass(slots=True, frozen=True)
class APTTRY:
    name: str = "APTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "APTTRY"

    def __str__(self):
        return "APTTRY"

    def __call__(self):
        return "APTTRY"


APTTRY = APTTRY()


@dataclass(slots=True, frozen=True)
class APTUSDT:
    name: str = "APTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "APTUSDT"

    def __str__(self):
        return "APTUSDT"

    def __call__(self):
        return "APTUSDT"


APTUSDT = APTUSDT()


@dataclass(slots=True, frozen=True)
class ARBNB:
    name: str = "ARBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARBNB"

    def __str__(self):
        return "ARBNB"

    def __call__(self):
        return "ARBNB"


ARBNB = ARBNB()


@dataclass(slots=True, frozen=True)
class ARBTC:
    name: str = "ARBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARBTC"

    def __str__(self):
        return "ARBTC"

    def __call__(self):
        return "ARBTC"


ARBTC = ARBTC()


@dataclass(slots=True, frozen=True)
class ARBUSD:
    name: str = "ARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARBUSD"

    def __str__(self):
        return "ARBUSD"

    def __call__(self):
        return "ARBUSD"


ARBUSD = ARBUSD()


@dataclass(slots=True, frozen=True)
class ARDRBNB:
    name: str = "ARDRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARDRBNB"

    def __str__(self):
        return "ARDRBNB"

    def __call__(self):
        return "ARDRBNB"


ARDRBNB = ARDRBNB()


@dataclass(slots=True, frozen=True)
class ARDRBTC:
    name: str = "ARDRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARDRBTC"

    def __str__(self):
        return "ARDRBTC"

    def __call__(self):
        return "ARDRBTC"


ARDRBTC = ARDRBTC()


@dataclass(slots=True, frozen=True)
class ARDRETH:
    name: str = "ARDRETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARDRETH"

    def __str__(self):
        return "ARDRETH"

    def __call__(self):
        return "ARDRETH"


ARDRETH = ARDRETH()


@dataclass(slots=True, frozen=True)
class ARDRUSDT:
    name: str = "ARDRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARDRUSDT"

    def __str__(self):
        return "ARDRUSDT"

    def __call__(self):
        return "ARDRUSDT"


ARDRUSDT = ARDRUSDT()


@dataclass(slots=True, frozen=True)
class ARKBTC:
    name: str = "ARKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARKBTC"

    def __str__(self):
        return "ARKBTC"

    def __call__(self):
        return "ARKBTC"


ARKBTC = ARKBTC()


@dataclass(slots=True, frozen=True)
class ARKBUSD:
    name: str = "ARKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ARKBUSD"

    def __str__(self):
        return "ARKBUSD"

    def __call__(self):
        return "ARKBUSD"


ARKBUSD = ARKBUSD()


@dataclass(slots=True, frozen=True)
class ARKETH:
    name: str = "ARKETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARKETH"

    def __str__(self):
        return "ARKETH"

    def __call__(self):
        return "ARKETH"


ARKETH = ARKETH()


@dataclass(slots=True, frozen=True)
class ARNBTC:
    name: str = "ARNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARNBTC"

    def __str__(self):
        return "ARNBTC"

    def __call__(self):
        return "ARNBTC"


ARNBTC = ARNBTC()


@dataclass(slots=True, frozen=True)
class ARNETH:
    name: str = "ARNETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARNETH"

    def __str__(self):
        return "ARNETH"

    def __call__(self):
        return "ARNETH"


ARNETH = ARNETH()


@dataclass(slots=True, frozen=True)
class ARPABNB:
    name: str = "ARPABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ARPABNB"

    def __str__(self):
        return "ARPABNB"

    def __call__(self):
        return "ARPABNB"


ARPABNB = ARPABNB()


@dataclass(slots=True, frozen=True)
class ARPABTC:
    name: str = "ARPABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ARPABTC"

    def __str__(self):
        return "ARPABTC"

    def __call__(self):
        return "ARPABTC"


ARPABTC = ARPABTC()


@dataclass(slots=True, frozen=True)
class ARPABUSD:
    name: str = "ARPABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "ARPABUSD"

    def __str__(self):
        return "ARPABUSD"

    def __call__(self):
        return "ARPABUSD"


ARPABUSD = ARPABUSD()


@dataclass(slots=True, frozen=True)
class ARPAETH:
    name: str = "ARPAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "ARPAETH"

    def __str__(self):
        return "ARPAETH"

    def __call__(self):
        return "ARPAETH"


ARPAETH = ARPAETH()


@dataclass(slots=True, frozen=True)
class ARPARUB:
    name: str = "ARPARUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ARPARUB"

    def __str__(self):
        return "ARPARUB"

    def __call__(self):
        return "ARPARUB"


ARPARUB = ARPARUB()


@dataclass(slots=True, frozen=True)
class ARPATRY:
    name: str = "ARPATRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ARPATRY"

    def __str__(self):
        return "ARPATRY"

    def __call__(self):
        return "ARPATRY"


ARPATRY = ARPATRY()


@dataclass(slots=True, frozen=True)
class ARPAUSDT:
    name: str = "ARPAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ARPAUSDT"

    def __str__(self):
        return "ARPAUSDT"

    def __call__(self):
        return "ARPAUSDT"


ARPAUSDT = ARPAUSDT()


@dataclass(slots=True, frozen=True)
class ARUSDT:
    name: str = "ARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000.00000000
    margin: bool = True

    def __repr__(self):
        return "ARUSDT"

    def __str__(self):
        return "ARUSDT"

    def __call__(self):
        return "ARUSDT"


ARUSDT = ARUSDT()


@dataclass(slots=True, frozen=True)
class ASRBTC:
    name: str = "ASRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ASRBTC"

    def __str__(self):
        return "ASRBTC"

    def __call__(self):
        return "ASRBTC"


ASRBTC = ASRBTC()


@dataclass(slots=True, frozen=True)
class ASRBUSD:
    name: str = "ASRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ASRBUSD"

    def __str__(self):
        return "ASRBUSD"

    def __call__(self):
        return "ASRBUSD"


ASRBUSD = ASRBUSD()


@dataclass(slots=True, frozen=True)
class ASRUSDT:
    name: str = "ASRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ASRUSDT"

    def __str__(self):
        return "ASRUSDT"

    def __call__(self):
        return "ASRUSDT"


ASRUSDT = ASRUSDT()


@dataclass(slots=True, frozen=True)
class ASTBTC:
    name: str = "ASTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ASTBTC"

    def __str__(self):
        return "ASTBTC"

    def __call__(self):
        return "ASTBTC"


ASTBTC = ASTBTC()


@dataclass(slots=True, frozen=True)
class ASTETH:
    name: str = "ASTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ASTETH"

    def __str__(self):
        return "ASTETH"

    def __call__(self):
        return "ASTETH"


ASTETH = ASTETH()


@dataclass(slots=True, frozen=True)
class ASTRBTC:
    name: str = "ASTRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ASTRBTC"

    def __str__(self):
        return "ASTRBTC"

    def __call__(self):
        return "ASTRBTC"


ASTRBTC = ASTRBTC()


@dataclass(slots=True, frozen=True)
class ASTRBUSD:
    name: str = "ASTRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "ASTRBUSD"

    def __str__(self):
        return "ASTRBUSD"

    def __call__(self):
        return "ASTRBUSD"


ASTRBUSD = ASTRBUSD()


@dataclass(slots=True, frozen=True)
class ASTRETH:
    name: str = "ASTRETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ASTRETH"

    def __str__(self):
        return "ASTRETH"

    def __call__(self):
        return "ASTRETH"


ASTRETH = ASTRETH()


@dataclass(slots=True, frozen=True)
class ASTRUSDT:
    name: str = "ASTRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "ASTRUSDT"

    def __str__(self):
        return "ASTRUSDT"

    def __call__(self):
        return "ASTRUSDT"


ASTRUSDT = ASTRUSDT()


@dataclass(slots=True, frozen=True)
class ATABNB:
    name: str = "ATABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ATABNB"

    def __str__(self):
        return "ATABNB"

    def __call__(self):
        return "ATABNB"


ATABNB = ATABNB()


@dataclass(slots=True, frozen=True)
class ATABTC:
    name: str = "ATABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ATABTC"

    def __str__(self):
        return "ATABTC"

    def __call__(self):
        return "ATABTC"


ATABTC = ATABTC()


@dataclass(slots=True, frozen=True)
class ATABUSD:
    name: str = "ATABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ATABUSD"

    def __str__(self):
        return "ATABUSD"

    def __call__(self):
        return "ATABUSD"


ATABUSD = ATABUSD()


@dataclass(slots=True, frozen=True)
class ATAUSDT:
    name: str = "ATAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ATAUSDT"

    def __str__(self):
        return "ATAUSDT"

    def __call__(self):
        return "ATAUSDT"


ATAUSDT = ATAUSDT()


@dataclass(slots=True, frozen=True)
class ATMBTC:
    name: str = "ATMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ATMBTC"

    def __str__(self):
        return "ATMBTC"

    def __call__(self):
        return "ATMBTC"


ATMBTC = ATMBTC()


@dataclass(slots=True, frozen=True)
class ATMBUSD:
    name: str = "ATMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ATMBUSD"

    def __str__(self):
        return "ATMBUSD"

    def __call__(self):
        return "ATMBUSD"


ATMBUSD = ATMBUSD()


@dataclass(slots=True, frozen=True)
class ATMUSDT:
    name: str = "ATMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ATMUSDT"

    def __str__(self):
        return "ATMUSDT"

    def __call__(self):
        return "ATMUSDT"


ATMUSDT = ATMUSDT()


@dataclass(slots=True, frozen=True)
class ATOMBIDR:
    name: str = "ATOMBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922337194.00000000
    margin: bool = False

    def __repr__(self):
        return "ATOMBIDR"

    def __str__(self):
        return "ATOMBIDR"

    def __call__(self):
        return "ATOMBIDR"


ATOMBIDR = ATOMBIDR()


@dataclass(slots=True, frozen=True)
class ATOMBNB:
    name: str = "ATOMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ATOMBNB"

    def __str__(self):
        return "ATOMBNB"

    def __call__(self):
        return "ATOMBNB"


ATOMBNB = ATOMBNB()


@dataclass(slots=True, frozen=True)
class ATOMBRL:
    name: str = "ATOMBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ATOMBRL"

    def __str__(self):
        return "ATOMBRL"

    def __call__(self):
        return "ATOMBRL"


ATOMBRL = ATOMBRL()


@dataclass(slots=True, frozen=True)
class ATOMBTC:
    name: str = "ATOMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ATOMBTC"

    def __str__(self):
        return "ATOMBTC"

    def __call__(self):
        return "ATOMBTC"


ATOMBTC = ATOMBTC()


@dataclass(slots=True, frozen=True)
class ATOMBUSD:
    name: str = "ATOMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "ATOMBUSD"

    def __str__(self):
        return "ATOMBUSD"

    def __call__(self):
        return "ATOMBUSD"


ATOMBUSD = ATOMBUSD()


@dataclass(slots=True, frozen=True)
class ATOMETH:
    name: str = "ATOMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ATOMETH"

    def __str__(self):
        return "ATOMETH"

    def __call__(self):
        return "ATOMETH"


ATOMETH = ATOMETH()


@dataclass(slots=True, frozen=True)
class ATOMEUR:
    name: str = "ATOMEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ATOMEUR"

    def __str__(self):
        return "ATOMEUR"

    def __call__(self):
        return "ATOMEUR"


ATOMEUR = ATOMEUR()


@dataclass(slots=True, frozen=True)
class ATOMPAX:
    name: str = "ATOMPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ATOMPAX"

    def __str__(self):
        return "ATOMPAX"

    def __call__(self):
        return "ATOMPAX"


ATOMPAX = ATOMPAX()


@dataclass(slots=True, frozen=True)
class ATOMTRY:
    name: str = "ATOMTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ATOMTRY"

    def __str__(self):
        return "ATOMTRY"

    def __call__(self):
        return "ATOMTRY"


ATOMTRY = ATOMTRY()


@dataclass(slots=True, frozen=True)
class ATOMTUSD:
    name: str = "ATOMTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ATOMTUSD"

    def __str__(self):
        return "ATOMTUSD"

    def __call__(self):
        return "ATOMTUSD"


ATOMTUSD = ATOMTUSD()


@dataclass(slots=True, frozen=True)
class ATOMUSDC:
    name: str = "ATOMUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ATOMUSDC"

    def __str__(self):
        return "ATOMUSDC"

    def __call__(self):
        return "ATOMUSDC"


ATOMUSDC = ATOMUSDC()


@dataclass(slots=True, frozen=True)
class ATOMUSDT:
    name: str = "ATOMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "ATOMUSDT"

    def __str__(self):
        return "ATOMUSDT"

    def __call__(self):
        return "ATOMUSDT"


ATOMUSDT = ATOMUSDT()


@dataclass(slots=True, frozen=True)
class AUCTIONBTC:
    name: str = "AUCTIONBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AUCTIONBTC"

    def __str__(self):
        return "AUCTIONBTC"

    def __call__(self):
        return "AUCTIONBTC"


AUCTIONBTC = AUCTIONBTC()


@dataclass(slots=True, frozen=True)
class AUCTIONBUSD:
    name: str = "AUCTIONBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "AUCTIONBUSD"

    def __str__(self):
        return "AUCTIONBUSD"

    def __call__(self):
        return "AUCTIONBUSD"


AUCTIONBUSD = AUCTIONBUSD()


@dataclass(slots=True, frozen=True)
class AUCTIONUSDT:
    name: str = "AUCTIONUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "AUCTIONUSDT"

    def __str__(self):
        return "AUCTIONUSDT"

    def __call__(self):
        return "AUCTIONUSDT"


AUCTIONUSDT = AUCTIONUSDT()


@dataclass(slots=True, frozen=True)
class AUDBUSD:
    name: str = "AUDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AUDBUSD"

    def __str__(self):
        return "AUDBUSD"

    def __call__(self):
        return "AUDBUSD"


AUDBUSD = AUDBUSD()


@dataclass(slots=True, frozen=True)
class AUDIOBTC:
    name: str = "AUDIOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "AUDIOBTC"

    def __str__(self):
        return "AUDIOBTC"

    def __call__(self):
        return "AUDIOBTC"


AUDIOBTC = AUDIOBTC()


@dataclass(slots=True, frozen=True)
class AUDIOBUSD:
    name: str = "AUDIOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "AUDIOBUSD"

    def __str__(self):
        return "AUDIOBUSD"

    def __call__(self):
        return "AUDIOBUSD"


AUDIOBUSD = AUDIOBUSD()


@dataclass(slots=True, frozen=True)
class AUDIOTRY:
    name: str = "AUDIOTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "AUDIOTRY"

    def __str__(self):
        return "AUDIOTRY"

    def __call__(self):
        return "AUDIOTRY"


AUDIOTRY = AUDIOTRY()


@dataclass(slots=True, frozen=True)
class AUDIOUSDT:
    name: str = "AUDIOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "AUDIOUSDT"

    def __str__(self):
        return "AUDIOUSDT"

    def __call__(self):
        return "AUDIOUSDT"


AUDIOUSDT = AUDIOUSDT()


@dataclass(slots=True, frozen=True)
class AUDUSDC:
    name: str = "AUDUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "AUDUSDC"

    def __str__(self):
        return "AUDUSDC"

    def __call__(self):
        return "AUDUSDC"


AUDUSDC = AUDUSDC()


@dataclass(slots=True, frozen=True)
class AUDUSDT:
    name: str = "AUDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AUDUSDT"

    def __str__(self):
        return "AUDUSDT"

    def __call__(self):
        return "AUDUSDT"


AUDUSDT = AUDUSDT()


@dataclass(slots=True, frozen=True)
class AUTOBTC:
    name: str = "AUTOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AUTOBTC"

    def __str__(self):
        return "AUTOBTC"

    def __call__(self):
        return "AUTOBTC"


AUTOBTC = AUTOBTC()


@dataclass(slots=True, frozen=True)
class AUTOBUSD:
    name: str = "AUTOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "AUTOBUSD"

    def __str__(self):
        return "AUTOBUSD"

    def __call__(self):
        return "AUTOBUSD"


AUTOBUSD = AUTOBUSD()


@dataclass(slots=True, frozen=True)
class AUTOUSDT:
    name: str = "AUTOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "AUTOUSDT"

    def __str__(self):
        return "AUTOUSDT"

    def __call__(self):
        return "AUTOUSDT"


AUTOUSDT = AUTOUSDT()


@dataclass(slots=True, frozen=True)
class AVABNB:
    name: str = "AVABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AVABNB"

    def __str__(self):
        return "AVABNB"

    def __call__(self):
        return "AVABNB"


AVABNB = AVABNB()


@dataclass(slots=True, frozen=True)
class AVABTC:
    name: str = "AVABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AVABTC"

    def __str__(self):
        return "AVABTC"

    def __call__(self):
        return "AVABTC"


AVABTC = AVABTC()


@dataclass(slots=True, frozen=True)
class AVABUSD:
    name: str = "AVABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "AVABUSD"

    def __str__(self):
        return "AVABUSD"

    def __call__(self):
        return "AVABUSD"


AVABUSD = AVABUSD()


@dataclass(slots=True, frozen=True)
class AVAUSDT:
    name: str = "AVAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "AVAUSDT"

    def __str__(self):
        return "AVAUSDT"

    def __call__(self):
        return "AVAUSDT"


AVAUSDT = AVAUSDT()


@dataclass(slots=True, frozen=True)
class AVAXAUD:
    name: str = "AVAXAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "AVAXAUD"

    def __str__(self):
        return "AVAXAUD"

    def __call__(self):
        return "AVAXAUD"


AVAXAUD = AVAXAUD()


@dataclass(slots=True, frozen=True)
class AVAXBIDR:
    name: str = "AVAXBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922337194.00000000
    margin: bool = False

    def __repr__(self):
        return "AVAXBIDR"

    def __str__(self):
        return "AVAXBIDR"

    def __call__(self):
        return "AVAXBIDR"


AVAXBIDR = AVAXBIDR()


@dataclass(slots=True, frozen=True)
class AVAXBNB:
    name: str = "AVAXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AVAXBNB"

    def __str__(self):
        return "AVAXBNB"

    def __call__(self):
        return "AVAXBNB"


AVAXBNB = AVAXBNB()


@dataclass(slots=True, frozen=True)
class AVAXBRL:
    name: str = "AVAXBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "AVAXBRL"

    def __str__(self):
        return "AVAXBRL"

    def __call__(self):
        return "AVAXBRL"


AVAXBRL = AVAXBRL()


@dataclass(slots=True, frozen=True)
class AVAXBTC:
    name: str = "AVAXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "AVAXBTC"

    def __str__(self):
        return "AVAXBTC"

    def __call__(self):
        return "AVAXBTC"


AVAXBTC = AVAXBTC()


@dataclass(slots=True, frozen=True)
class AVAXBUSD:
    name: str = "AVAXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "AVAXBUSD"

    def __str__(self):
        return "AVAXBUSD"

    def __call__(self):
        return "AVAXBUSD"


AVAXBUSD = AVAXBUSD()


@dataclass(slots=True, frozen=True)
class AVAXETH:
    name: str = "AVAXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AVAXETH"

    def __str__(self):
        return "AVAXETH"

    def __call__(self):
        return "AVAXETH"


AVAXETH = AVAXETH()


@dataclass(slots=True, frozen=True)
class AVAXEUR:
    name: str = "AVAXEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "AVAXEUR"

    def __str__(self):
        return "AVAXEUR"

    def __call__(self):
        return "AVAXEUR"


AVAXEUR = AVAXEUR()


@dataclass(slots=True, frozen=True)
class AVAXGBP:
    name: str = "AVAXGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "AVAXGBP"

    def __str__(self):
        return "AVAXGBP"

    def __call__(self):
        return "AVAXGBP"


AVAXGBP = AVAXGBP()


@dataclass(slots=True, frozen=True)
class AVAXTRY:
    name: str = "AVAXTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "AVAXTRY"

    def __str__(self):
        return "AVAXTRY"

    def __call__(self):
        return "AVAXTRY"


AVAXTRY = AVAXTRY()


@dataclass(slots=True, frozen=True)
class AVAXUSDT:
    name: str = "AVAXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "AVAXUSDT"

    def __str__(self):
        return "AVAXUSDT"

    def __call__(self):
        return "AVAXUSDT"


AVAXUSDT = AVAXUSDT()


@dataclass(slots=True, frozen=True)
class AXSAUD:
    name: str = "AXSAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "AXSAUD"

    def __str__(self):
        return "AXSAUD"

    def __call__(self):
        return "AXSAUD"


AXSAUD = AXSAUD()


@dataclass(slots=True, frozen=True)
class AXSBIDR:
    name: str = "AXSBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9223372.00000000
    margin: bool = False

    def __repr__(self):
        return "AXSBIDR"

    def __str__(self):
        return "AXSBIDR"

    def __call__(self):
        return "AXSBIDR"


AXSBIDR = AXSBIDR()


@dataclass(slots=True, frozen=True)
class AXSBNB:
    name: str = "AXSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "AXSBNB"

    def __str__(self):
        return "AXSBNB"

    def __call__(self):
        return "AXSBNB"


AXSBNB = AXSBNB()


@dataclass(slots=True, frozen=True)
class AXSBRL:
    name: str = "AXSBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "AXSBRL"

    def __str__(self):
        return "AXSBRL"

    def __call__(self):
        return "AXSBRL"


AXSBRL = AXSBRL()


@dataclass(slots=True, frozen=True)
class AXSBTC:
    name: str = "AXSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "AXSBTC"

    def __str__(self):
        return "AXSBTC"

    def __call__(self):
        return "AXSBTC"


AXSBTC = AXSBTC()


@dataclass(slots=True, frozen=True)
class AXSBUSD:
    name: str = "AXSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "AXSBUSD"

    def __str__(self):
        return "AXSBUSD"

    def __call__(self):
        return "AXSBUSD"


AXSBUSD = AXSBUSD()


@dataclass(slots=True, frozen=True)
class AXSETH:
    name: str = "AXSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "AXSETH"

    def __str__(self):
        return "AXSETH"

    def __call__(self):
        return "AXSETH"


AXSETH = AXSETH()


@dataclass(slots=True, frozen=True)
class AXSTRY:
    name: str = "AXSTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "AXSTRY"

    def __str__(self):
        return "AXSTRY"

    def __call__(self):
        return "AXSTRY"


AXSTRY = AXSTRY()


@dataclass(slots=True, frozen=True)
class AXSUSDT:
    name: str = "AXSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "AXSUSDT"

    def __str__(self):
        return "AXSUSDT"

    def __call__(self):
        return "AXSUSDT"


AXSUSDT = AXSUSDT()


@dataclass(slots=True, frozen=True)
class BADGERBTC:
    name: str = "BADGERBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BADGERBTC"

    def __str__(self):
        return "BADGERBTC"

    def __call__(self):
        return "BADGERBTC"


BADGERBTC = BADGERBTC()


@dataclass(slots=True, frozen=True)
class BADGERBUSD:
    name: str = "BADGERBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "BADGERBUSD"

    def __str__(self):
        return "BADGERBUSD"

    def __call__(self):
        return "BADGERBUSD"


BADGERBUSD = BADGERBUSD()


@dataclass(slots=True, frozen=True)
class BADGERUSDT:
    name: str = "BADGERUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "BADGERUSDT"

    def __str__(self):
        return "BADGERUSDT"

    def __call__(self):
        return "BADGERUSDT"


BADGERUSDT = BADGERUSDT()


@dataclass(slots=True, frozen=True)
class BAKEBNB:
    name: str = "BAKEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BAKEBNB"

    def __str__(self):
        return "BAKEBNB"

    def __call__(self):
        return "BAKEBNB"


BAKEBNB = BAKEBNB()


@dataclass(slots=True, frozen=True)
class BAKEBTC:
    name: str = "BAKEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "BAKEBTC"

    def __str__(self):
        return "BAKEBTC"

    def __call__(self):
        return "BAKEBTC"


BAKEBTC = BAKEBTC()


@dataclass(slots=True, frozen=True)
class BAKEBUSD:
    name: str = "BAKEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "BAKEBUSD"

    def __str__(self):
        return "BAKEBUSD"

    def __call__(self):
        return "BAKEBUSD"


BAKEBUSD = BAKEBUSD()


@dataclass(slots=True, frozen=True)
class BAKEUSDT:
    name: str = "BAKEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "BAKEUSDT"

    def __str__(self):
        return "BAKEUSDT"

    def __call__(self):
        return "BAKEUSDT"


BAKEUSDT = BAKEUSDT()


@dataclass(slots=True, frozen=True)
class BALBNB:
    name: str = "BALBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BALBNB"

    def __str__(self):
        return "BALBNB"

    def __call__(self):
        return "BALBNB"


BALBNB = BALBNB()


@dataclass(slots=True, frozen=True)
class BALBTC:
    name: str = "BALBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BALBTC"

    def __str__(self):
        return "BALBTC"

    def __call__(self):
        return "BALBTC"


BALBTC = BALBTC()


@dataclass(slots=True, frozen=True)
class BALBUSD:
    name: str = "BALBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BALBUSD"

    def __str__(self):
        return "BALBUSD"

    def __call__(self):
        return "BALBUSD"


BALBUSD = BALBUSD()


@dataclass(slots=True, frozen=True)
class BALUSDT:
    name: str = "BALUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "BALUSDT"

    def __str__(self):
        return "BALUSDT"

    def __call__(self):
        return "BALUSDT"


BALUSDT = BALUSDT()


@dataclass(slots=True, frozen=True)
class BANDBNB:
    name: str = "BANDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BANDBNB"

    def __str__(self):
        return "BANDBNB"

    def __call__(self):
        return "BANDBNB"


BANDBNB = BANDBNB()


@dataclass(slots=True, frozen=True)
class BANDBTC:
    name: str = "BANDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BANDBTC"

    def __str__(self):
        return "BANDBTC"

    def __call__(self):
        return "BANDBTC"


BANDBTC = BANDBTC()


@dataclass(slots=True, frozen=True)
class BANDBUSD:
    name: str = "BANDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BANDBUSD"

    def __str__(self):
        return "BANDBUSD"

    def __call__(self):
        return "BANDBUSD"


BANDBUSD = BANDBUSD()


@dataclass(slots=True, frozen=True)
class BANDUSDT:
    name: str = "BANDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "BANDUSDT"

    def __str__(self):
        return "BANDUSDT"

    def __call__(self):
        return "BANDUSDT"


BANDUSDT = BANDUSDT()


@dataclass(slots=True, frozen=True)
class BARBTC:
    name: str = "BARBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BARBTC"

    def __str__(self):
        return "BARBTC"

    def __call__(self):
        return "BARBTC"


BARBTC = BARBTC()


@dataclass(slots=True, frozen=True)
class BARBUSD:
    name: str = "BARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BARBUSD"

    def __str__(self):
        return "BARBUSD"

    def __call__(self):
        return "BARBUSD"


BARBUSD = BARBUSD()


@dataclass(slots=True, frozen=True)
class BARUSDT:
    name: str = "BARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BARUSDT"

    def __str__(self):
        return "BARUSDT"

    def __call__(self):
        return "BARUSDT"


BARUSDT = BARUSDT()


@dataclass(slots=True, frozen=True)
class BATBNB:
    name: str = "BATBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BATBNB"

    def __str__(self):
        return "BATBNB"

    def __call__(self):
        return "BATBNB"


BATBNB = BATBNB()


@dataclass(slots=True, frozen=True)
class BATBTC:
    name: str = "BATBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BATBTC"

    def __str__(self):
        return "BATBTC"

    def __call__(self):
        return "BATBTC"


BATBTC = BATBTC()


@dataclass(slots=True, frozen=True)
class BATBUSD:
    name: str = "BATBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "BATBUSD"

    def __str__(self):
        return "BATBUSD"

    def __call__(self):
        return "BATBUSD"


BATBUSD = BATBUSD()


@dataclass(slots=True, frozen=True)
class BATETH:
    name: str = "BATETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BATETH"

    def __str__(self):
        return "BATETH"

    def __call__(self):
        return "BATETH"


BATETH = BATETH()


@dataclass(slots=True, frozen=True)
class BATPAX:
    name: str = "BATPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BATPAX"

    def __str__(self):
        return "BATPAX"

    def __call__(self):
        return "BATPAX"


BATPAX = BATPAX()


@dataclass(slots=True, frozen=True)
class BATTUSD:
    name: str = "BATTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BATTUSD"

    def __str__(self):
        return "BATTUSD"

    def __call__(self):
        return "BATTUSD"


BATTUSD = BATTUSD()


@dataclass(slots=True, frozen=True)
class BATUSDC:
    name: str = "BATUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BATUSDC"

    def __str__(self):
        return "BATUSDC"

    def __call__(self):
        return "BATUSDC"


BATUSDC = BATUSDC()


@dataclass(slots=True, frozen=True)
class BATUSDT:
    name: str = "BATUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "BATUSDT"

    def __str__(self):
        return "BATUSDT"

    def __call__(self):
        return "BATUSDT"


BATUSDT = BATUSDT()


@dataclass(slots=True, frozen=True)
class BCCBNB:
    name: str = "BCCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCCBNB"

    def __str__(self):
        return "BCCBNB"

    def __call__(self):
        return "BCCBNB"


BCCBNB = BCCBNB()


@dataclass(slots=True, frozen=True)
class BCCBTC:
    name: str = "BCCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BCCBTC"

    def __str__(self):
        return "BCCBTC"

    def __call__(self):
        return "BCCBTC"


BCCBTC = BCCBTC()


@dataclass(slots=True, frozen=True)
class BCCETH:
    name: str = "BCCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCCETH"

    def __str__(self):
        return "BCCETH"

    def __call__(self):
        return "BCCETH"


BCCETH = BCCETH()


@dataclass(slots=True, frozen=True)
class BCCUSDT:
    name: str = "BCCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCCUSDT"

    def __str__(self):
        return "BCCUSDT"

    def __call__(self):
        return "BCCUSDT"


BCCUSDT = BCCUSDT()


@dataclass(slots=True, frozen=True)
class BCDBTC:
    name: str = "BCDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCDBTC"

    def __str__(self):
        return "BCDBTC"

    def __call__(self):
        return "BCDBTC"


BCDBTC = BCDBTC()


@dataclass(slots=True, frozen=True)
class BCDETH:
    name: str = "BCDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCDETH"

    def __str__(self):
        return "BCDETH"

    def __call__(self):
        return "BCDETH"


BCDETH = BCDETH()


@dataclass(slots=True, frozen=True)
class BCHABCBTC:
    name: str = "BCHABCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHABCBTC"

    def __str__(self):
        return "BCHABCBTC"

    def __call__(self):
        return "BCHABCBTC"


BCHABCBTC = BCHABCBTC()


@dataclass(slots=True, frozen=True)
class BCHABCBUSD:
    name: str = "BCHABCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHABCBUSD"

    def __str__(self):
        return "BCHABCBUSD"

    def __call__(self):
        return "BCHABCBUSD"


BCHABCBUSD = BCHABCBUSD()


@dataclass(slots=True, frozen=True)
class BCHABCPAX:
    name: str = "BCHABCPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHABCPAX"

    def __str__(self):
        return "BCHABCPAX"

    def __call__(self):
        return "BCHABCPAX"


BCHABCPAX = BCHABCPAX()


@dataclass(slots=True, frozen=True)
class BCHABCTUSD:
    name: str = "BCHABCTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHABCTUSD"

    def __str__(self):
        return "BCHABCTUSD"

    def __call__(self):
        return "BCHABCTUSD"


BCHABCTUSD = BCHABCTUSD()


@dataclass(slots=True, frozen=True)
class BCHABCUSDC:
    name: str = "BCHABCUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHABCUSDC"

    def __str__(self):
        return "BCHABCUSDC"

    def __call__(self):
        return "BCHABCUSDC"


BCHABCUSDC = BCHABCUSDC()


@dataclass(slots=True, frozen=True)
class BCHABCUSDT:
    name: str = "BCHABCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHABCUSDT"

    def __str__(self):
        return "BCHABCUSDT"

    def __call__(self):
        return "BCHABCUSDT"


BCHABCUSDT = BCHABCUSDT()


@dataclass(slots=True, frozen=True)
class BCHABUSD:
    name: str = "BCHABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHABUSD"

    def __str__(self):
        return "BCHABUSD"

    def __call__(self):
        return "BCHABUSD"


BCHABUSD = BCHABUSD()


@dataclass(slots=True, frozen=True)
class BCHBNB:
    name: str = "BCHBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHBNB"

    def __str__(self):
        return "BCHBNB"

    def __call__(self):
        return "BCHBNB"


BCHBNB = BCHBNB()


@dataclass(slots=True, frozen=True)
class BCHBTC:
    name: str = "BCHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BCHBTC"

    def __str__(self):
        return "BCHBTC"

    def __call__(self):
        return "BCHBTC"


BCHBTC = BCHBTC()


@dataclass(slots=True, frozen=True)
class BCHBUSD:
    name: str = "BCHBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "BCHBUSD"

    def __str__(self):
        return "BCHBUSD"

    def __call__(self):
        return "BCHBUSD"


BCHBUSD = BCHBUSD()


@dataclass(slots=True, frozen=True)
class BCHDOWNUSDT:
    name: str = "BCHDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHDOWNUSDT"

    def __str__(self):
        return "BCHDOWNUSDT"

    def __call__(self):
        return "BCHDOWNUSDT"


BCHDOWNUSDT = BCHDOWNUSDT()


@dataclass(slots=True, frozen=True)
class BCHEUR:
    name: str = "BCHEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHEUR"

    def __str__(self):
        return "BCHEUR"

    def __call__(self):
        return "BCHEUR"


BCHEUR = BCHEUR()


@dataclass(slots=True, frozen=True)
class BCHPAX:
    name: str = "BCHPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHPAX"

    def __str__(self):
        return "BCHPAX"

    def __call__(self):
        return "BCHPAX"


BCHPAX = BCHPAX()


@dataclass(slots=True, frozen=True)
class BCHSVBTC:
    name: str = "BCHSVBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHSVBTC"

    def __str__(self):
        return "BCHSVBTC"

    def __call__(self):
        return "BCHSVBTC"


BCHSVBTC = BCHSVBTC()


@dataclass(slots=True, frozen=True)
class BCHSVPAX:
    name: str = "BCHSVPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHSVPAX"

    def __str__(self):
        return "BCHSVPAX"

    def __call__(self):
        return "BCHSVPAX"


BCHSVPAX = BCHSVPAX()


@dataclass(slots=True, frozen=True)
class BCHSVTUSD:
    name: str = "BCHSVTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHSVTUSD"

    def __str__(self):
        return "BCHSVTUSD"

    def __call__(self):
        return "BCHSVTUSD"


BCHSVTUSD = BCHSVTUSD()


@dataclass(slots=True, frozen=True)
class BCHSVUSDC:
    name: str = "BCHSVUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHSVUSDC"

    def __str__(self):
        return "BCHSVUSDC"

    def __call__(self):
        return "BCHSVUSDC"


BCHSVUSDC = BCHSVUSDC()


@dataclass(slots=True, frozen=True)
class BCHSVUSDT:
    name: str = "BCHSVUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHSVUSDT"

    def __str__(self):
        return "BCHSVUSDT"

    def __call__(self):
        return "BCHSVUSDT"


BCHSVUSDT = BCHSVUSDT()


@dataclass(slots=True, frozen=True)
class BCHTUSD:
    name: str = "BCHTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHTUSD"

    def __str__(self):
        return "BCHTUSD"

    def __call__(self):
        return "BCHTUSD"


BCHTUSD = BCHTUSD()


@dataclass(slots=True, frozen=True)
class BCHUPUSDT:
    name: str = "BCHUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHUPUSDT"

    def __str__(self):
        return "BCHUPUSDT"

    def __call__(self):
        return "BCHUPUSDT"


BCHUPUSDT = BCHUPUSDT()


@dataclass(slots=True, frozen=True)
class BCHUSDC:
    name: str = "BCHUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCHUSDC"

    def __str__(self):
        return "BCHUSDC"

    def __call__(self):
        return "BCHUSDC"


BCHUSDC = BCHUSDC()


@dataclass(slots=True, frozen=True)
class BCHUSDT:
    name: str = "BCHUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "BCHUSDT"

    def __str__(self):
        return "BCHUSDT"

    def __call__(self):
        return "BCHUSDT"


BCHUSDT = BCHUSDT()


@dataclass(slots=True, frozen=True)
class BCNBNB:
    name: str = "BCNBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCNBNB"

    def __str__(self):
        return "BCNBNB"

    def __call__(self):
        return "BCNBNB"


BCNBNB = BCNBNB()


@dataclass(slots=True, frozen=True)
class BCNBTC:
    name: str = "BCNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCNBTC"

    def __str__(self):
        return "BCNBTC"

    def __call__(self):
        return "BCNBTC"


BCNBTC = BCNBTC()


@dataclass(slots=True, frozen=True)
class BCNETH:
    name: str = "BCNETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCNETH"

    def __str__(self):
        return "BCNETH"

    def __call__(self):
        return "BCNETH"


BCNETH = BCNETH()


@dataclass(slots=True, frozen=True)
class BCPTBNB:
    name: str = "BCPTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCPTBNB"

    def __str__(self):
        return "BCPTBNB"

    def __call__(self):
        return "BCPTBNB"


BCPTBNB = BCPTBNB()


@dataclass(slots=True, frozen=True)
class BCPTBTC:
    name: str = "BCPTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCPTBTC"

    def __str__(self):
        return "BCPTBTC"

    def __call__(self):
        return "BCPTBTC"


BCPTBTC = BCPTBTC()


@dataclass(slots=True, frozen=True)
class BCPTETH:
    name: str = "BCPTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCPTETH"

    def __str__(self):
        return "BCPTETH"

    def __call__(self):
        return "BCPTETH"


BCPTETH = BCPTETH()


@dataclass(slots=True, frozen=True)
class BCPTPAX:
    name: str = "BCPTPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCPTPAX"

    def __str__(self):
        return "BCPTPAX"

    def __call__(self):
        return "BCPTPAX"


BCPTPAX = BCPTPAX()


@dataclass(slots=True, frozen=True)
class BCPTTUSD:
    name: str = "BCPTTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCPTTUSD"

    def __str__(self):
        return "BCPTTUSD"

    def __call__(self):
        return "BCPTTUSD"


BCPTTUSD = BCPTTUSD()


@dataclass(slots=True, frozen=True)
class BCPTUSDC:
    name: str = "BCPTUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BCPTUSDC"

    def __str__(self):
        return "BCPTUSDC"

    def __call__(self):
        return "BCPTUSDC"


BCPTUSDC = BCPTUSDC()


@dataclass(slots=True, frozen=True)
class BDOTDOT:
    name: str = "BDOTDOT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BDOTDOT"

    def __str__(self):
        return "BDOTDOT"

    def __call__(self):
        return "BDOTDOT"


BDOTDOT = BDOTDOT()


@dataclass(slots=True, frozen=True)
class BEAMBNB:
    name: str = "BEAMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BEAMBNB"

    def __str__(self):
        return "BEAMBNB"

    def __call__(self):
        return "BEAMBNB"


BEAMBNB = BEAMBNB()


@dataclass(slots=True, frozen=True)
class BEAMBTC:
    name: str = "BEAMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BEAMBTC"

    def __str__(self):
        return "BEAMBTC"

    def __call__(self):
        return "BEAMBTC"


BEAMBTC = BEAMBTC()


@dataclass(slots=True, frozen=True)
class BEAMUSDT:
    name: str = "BEAMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BEAMUSDT"

    def __str__(self):
        return "BEAMUSDT"

    def __call__(self):
        return "BEAMUSDT"


BEAMUSDT = BEAMUSDT()


@dataclass(slots=True, frozen=True)
class BEARBUSD:
    name: str = "BEARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BEARBUSD"

    def __str__(self):
        return "BEARBUSD"

    def __call__(self):
        return "BEARBUSD"


BEARBUSD = BEARBUSD()


@dataclass(slots=True, frozen=True)
class BEARUSDT:
    name: str = "BEARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BEARUSDT"

    def __str__(self):
        return "BEARUSDT"

    def __call__(self):
        return "BEARUSDT"


BEARUSDT = BEARUSDT()


@dataclass(slots=True, frozen=True)
class BELBNB:
    name: str = "BELBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BELBNB"

    def __str__(self):
        return "BELBNB"

    def __call__(self):
        return "BELBNB"


BELBNB = BELBNB()


@dataclass(slots=True, frozen=True)
class BELBTC:
    name: str = "BELBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BELBTC"

    def __str__(self):
        return "BELBTC"

    def __call__(self):
        return "BELBTC"


BELBTC = BELBTC()


@dataclass(slots=True, frozen=True)
class BELBUSD:
    name: str = "BELBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "BELBUSD"

    def __str__(self):
        return "BELBUSD"

    def __call__(self):
        return "BELBUSD"


BELBUSD = BELBUSD()


@dataclass(slots=True, frozen=True)
class BELETH:
    name: str = "BELETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BELETH"

    def __str__(self):
        return "BELETH"

    def __call__(self):
        return "BELETH"


BELETH = BELETH()


@dataclass(slots=True, frozen=True)
class BELTRY:
    name: str = "BELTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "BELTRY"

    def __str__(self):
        return "BELTRY"

    def __call__(self):
        return "BELTRY"


BELTRY = BELTRY()


@dataclass(slots=True, frozen=True)
class BELUSDT:
    name: str = "BELUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "BELUSDT"

    def __str__(self):
        return "BELUSDT"

    def __call__(self):
        return "BELUSDT"


BELUSDT = BELUSDT()


@dataclass(slots=True, frozen=True)
class BETABNB:
    name: str = "BETABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BETABNB"

    def __str__(self):
        return "BETABNB"

    def __call__(self):
        return "BETABNB"


BETABNB = BETABNB()


@dataclass(slots=True, frozen=True)
class BETABTC:
    name: str = "BETABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BETABTC"

    def __str__(self):
        return "BETABTC"

    def __call__(self):
        return "BETABTC"


BETABTC = BETABTC()


@dataclass(slots=True, frozen=True)
class BETABUSD:
    name: str = "BETABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BETABUSD"

    def __str__(self):
        return "BETABUSD"

    def __call__(self):
        return "BETABUSD"


BETABUSD = BETABUSD()


@dataclass(slots=True, frozen=True)
class BETAETH:
    name: str = "BETAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BETAETH"

    def __str__(self):
        return "BETAETH"

    def __call__(self):
        return "BETAETH"


BETAETH = BETAETH()


@dataclass(slots=True, frozen=True)
class BETAUSDT:
    name: str = "BETAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "BETAUSDT"

    def __str__(self):
        return "BETAUSDT"

    def __call__(self):
        return "BETAUSDT"


BETAUSDT = BETAUSDT()


@dataclass(slots=True, frozen=True)
class BETHBUSD:
    name: str = "BETHBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BETHBUSD"

    def __str__(self):
        return "BETHBUSD"

    def __call__(self):
        return "BETHBUSD"


BETHBUSD = BETHBUSD()


@dataclass(slots=True, frozen=True)
class BETHETH:
    name: str = "BETHETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BETHETH"

    def __str__(self):
        return "BETHETH"

    def __call__(self):
        return "BETHETH"


BETHETH = BETHETH()


@dataclass(slots=True, frozen=True)
class BGBPUSDC:
    name: str = "BGBPUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BGBPUSDC"

    def __str__(self):
        return "BGBPUSDC"

    def __call__(self):
        return "BGBPUSDC"


BGBPUSDC = BGBPUSDC()


@dataclass(slots=True, frozen=True)
class BICOBTC:
    name: str = "BICOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "BICOBTC"

    def __str__(self):
        return "BICOBTC"

    def __call__(self):
        return "BICOBTC"


BICOBTC = BICOBTC()


@dataclass(slots=True, frozen=True)
class BICOBUSD:
    name: str = "BICOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "BICOBUSD"

    def __str__(self):
        return "BICOBUSD"

    def __call__(self):
        return "BICOBUSD"


BICOBUSD = BICOBUSD()


@dataclass(slots=True, frozen=True)
class BICOUSDT:
    name: str = "BICOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "BICOUSDT"

    def __str__(self):
        return "BICOUSDT"

    def __call__(self):
        return "BICOUSDT"


BICOUSDT = BICOUSDT()


@dataclass(slots=True, frozen=True)
class BIFIBNB:
    name: str = "BIFIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BIFIBNB"

    def __str__(self):
        return "BIFIBNB"

    def __call__(self):
        return "BIFIBNB"


BIFIBNB = BIFIBNB()


@dataclass(slots=True, frozen=True)
class BIFIBUSD:
    name: str = "BIFIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BIFIBUSD"

    def __str__(self):
        return "BIFIBUSD"

    def __call__(self):
        return "BIFIBUSD"


BIFIBUSD = BIFIBUSD()


@dataclass(slots=True, frozen=True)
class BIFIUSDT:
    name: str = "BIFIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BIFIUSDT"

    def __str__(self):
        return "BIFIUSDT"

    def __call__(self):
        return "BIFIUSDT"


BIFIUSDT = BIFIUSDT()


@dataclass(slots=True, frozen=True)
class BKRWBUSD:
    name: str = "BKRWBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BKRWBUSD"

    def __str__(self):
        return "BKRWBUSD"

    def __call__(self):
        return "BKRWBUSD"


BKRWBUSD = BKRWBUSD()


@dataclass(slots=True, frozen=True)
class BKRWUSDT:
    name: str = "BKRWUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BKRWUSDT"

    def __str__(self):
        return "BKRWUSDT"

    def __call__(self):
        return "BKRWUSDT"


BKRWUSDT = BKRWUSDT()


@dataclass(slots=True, frozen=True)
class BLZBNB:
    name: str = "BLZBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BLZBNB"

    def __str__(self):
        return "BLZBNB"

    def __call__(self):
        return "BLZBNB"


BLZBNB = BLZBNB()


@dataclass(slots=True, frozen=True)
class BLZBTC:
    name: str = "BLZBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BLZBTC"

    def __str__(self):
        return "BLZBTC"

    def __call__(self):
        return "BLZBTC"


BLZBTC = BLZBTC()


@dataclass(slots=True, frozen=True)
class BLZBUSD:
    name: str = "BLZBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BLZBUSD"

    def __str__(self):
        return "BLZBUSD"

    def __call__(self):
        return "BLZBUSD"


BLZBUSD = BLZBUSD()


@dataclass(slots=True, frozen=True)
class BLZETH:
    name: str = "BLZETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BLZETH"

    def __str__(self):
        return "BLZETH"

    def __call__(self):
        return "BLZETH"


BLZETH = BLZETH()


@dataclass(slots=True, frozen=True)
class BLZUSDT:
    name: str = "BLZUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BLZUSDT"

    def __str__(self):
        return "BLZUSDT"

    def __call__(self):
        return "BLZUSDT"


BLZUSDT = BLZUSDT()


@dataclass(slots=True, frozen=True)
class BNBAUD:
    name: str = "BNBAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBAUD"

    def __str__(self):
        return "BNBAUD"

    def __call__(self):
        return "BNBAUD"


BNBAUD = BNBAUD()


@dataclass(slots=True, frozen=True)
class BNBBEARBUSD:
    name: str = "BNBBEARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBBEARBUSD"

    def __str__(self):
        return "BNBBEARBUSD"

    def __call__(self):
        return "BNBBEARBUSD"


BNBBEARBUSD = BNBBEARBUSD()


@dataclass(slots=True, frozen=True)
class BNBBEARUSDT:
    name: str = "BNBBEARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBBEARUSDT"

    def __str__(self):
        return "BNBBEARUSDT"

    def __call__(self):
        return "BNBBEARUSDT"


BNBBEARUSDT = BNBBEARUSDT()


@dataclass(slots=True, frozen=True)
class BNBBIDR:
    name: str = "BNBBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBBIDR"

    def __str__(self):
        return "BNBBIDR"

    def __call__(self):
        return "BNBBIDR"


BNBBIDR = BNBBIDR()


@dataclass(slots=True, frozen=True)
class BNBBKRW:
    name: str = "BNBBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBBKRW"

    def __str__(self):
        return "BNBBKRW"

    def __call__(self):
        return "BNBBKRW"


BNBBKRW = BNBBKRW()


@dataclass(slots=True, frozen=True)
class BNBBRL:
    name: str = "BNBBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 45000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBBRL"

    def __str__(self):
        return "BNBBRL"

    def __call__(self):
        return "BNBBRL"


BNBBRL = BNBBRL()


@dataclass(slots=True, frozen=True)
class BNBBTC:
    name: str = "BNBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 100000.00000000
    margin: bool = True

    def __repr__(self):
        return "BNBBTC"

    def __str__(self):
        return "BNBBTC"

    def __call__(self):
        return "BNBBTC"


BNBBTC = BNBBTC()


@dataclass(slots=True, frozen=True)
class BNBBULLBUSD:
    name: str = "BNBBULLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBBULLBUSD"

    def __str__(self):
        return "BNBBULLBUSD"

    def __call__(self):
        return "BNBBULLBUSD"


BNBBULLBUSD = BNBBULLBUSD()


@dataclass(slots=True, frozen=True)
class BNBBULLUSDT:
    name: str = "BNBBULLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBBULLUSDT"

    def __str__(self):
        return "BNBBULLUSDT"

    def __call__(self):
        return "BNBBULLUSDT"


BNBBULLUSDT = BNBBULLUSDT()


@dataclass(slots=True, frozen=True)
class BNBBUSD:
    name: str = "BNBBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "BNBBUSD"

    def __str__(self):
        return "BNBBUSD"

    def __call__(self):
        return "BNBBUSD"


BNBBUSD = BNBBUSD()


@dataclass(slots=True, frozen=True)
class BNBDAI:
    name: str = "BNBDAI"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBDAI"

    def __str__(self):
        return "BNBDAI"

    def __call__(self):
        return "BNBDAI"


BNBDAI = BNBDAI()


@dataclass(slots=True, frozen=True)
class BNBDOWNUSDT:
    name: str = "BNBDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBDOWNUSDT"

    def __str__(self):
        return "BNBDOWNUSDT"

    def __call__(self):
        return "BNBDOWNUSDT"


BNBDOWNUSDT = BNBDOWNUSDT()


@dataclass(slots=True, frozen=True)
class BNBETH:
    name: str = "BNBETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BNBETH"

    def __str__(self):
        return "BNBETH"

    def __call__(self):
        return "BNBETH"


BNBETH = BNBETH()


@dataclass(slots=True, frozen=True)
class BNBEUR:
    name: str = "BNBEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBEUR"

    def __str__(self):
        return "BNBEUR"

    def __call__(self):
        return "BNBEUR"


BNBEUR = BNBEUR()


@dataclass(slots=True, frozen=True)
class BNBGBP:
    name: str = "BNBGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBGBP"

    def __str__(self):
        return "BNBGBP"

    def __call__(self):
        return "BNBGBP"


BNBGBP = BNBGBP()


@dataclass(slots=True, frozen=True)
class BNBIDRT:
    name: str = "BNBIDRT"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBIDRT"

    def __str__(self):
        return "BNBIDRT"

    def __call__(self):
        return "BNBIDRT"


BNBIDRT = BNBIDRT()


@dataclass(slots=True, frozen=True)
class BNBNGN:
    name: str = "BNBNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBNGN"

    def __str__(self):
        return "BNBNGN"

    def __call__(self):
        return "BNBNGN"


BNBNGN = BNBNGN()


@dataclass(slots=True, frozen=True)
class BNBPAX:
    name: str = "BNBPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBPAX"

    def __str__(self):
        return "BNBPAX"

    def __call__(self):
        return "BNBPAX"


BNBPAX = BNBPAX()


@dataclass(slots=True, frozen=True)
class BNBRUB:
    name: str = "BNBRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 184466.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBRUB"

    def __str__(self):
        return "BNBRUB"

    def __call__(self):
        return "BNBRUB"


BNBRUB = BNBRUB()


@dataclass(slots=True, frozen=True)
class BNBTRY:
    name: str = "BNBTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92232.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBTRY"

    def __str__(self):
        return "BNBTRY"

    def __call__(self):
        return "BNBTRY"


BNBTRY = BNBTRY()


@dataclass(slots=True, frozen=True)
class BNBTUSD:
    name: str = "BNBTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBTUSD"

    def __str__(self):
        return "BNBTUSD"

    def __call__(self):
        return "BNBTUSD"


BNBTUSD = BNBTUSD()


@dataclass(slots=True, frozen=True)
class BNBUAH:
    name: str = "BNBUAH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBUAH"

    def __str__(self):
        return "BNBUAH"

    def __call__(self):
        return "BNBUAH"


BNBUAH = BNBUAH()


@dataclass(slots=True, frozen=True)
class BNBUPUSDT:
    name: str = "BNBUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 500.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBUPUSDT"

    def __str__(self):
        return "BNBUPUSDT"

    def __call__(self):
        return "BNBUPUSDT"


BNBUPUSDT = BNBUPUSDT()


@dataclass(slots=True, frozen=True)
class BNBUSDC:
    name: str = "BNBUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBUSDC"

    def __str__(self):
        return "BNBUSDC"

    def __call__(self):
        return "BNBUSDC"


BNBUSDC = BNBUSDC()


@dataclass(slots=True, frozen=True)
class BNBUSDP:
    name: str = "BNBUSDP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBUSDP"

    def __str__(self):
        return "BNBUSDP"

    def __call__(self):
        return "BNBUSDP"


BNBUSDP = BNBUSDP()


@dataclass(slots=True, frozen=True)
class BNBUSDS:
    name: str = "BNBUSDS"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBUSDS"

    def __str__(self):
        return "BNBUSDS"

    def __call__(self):
        return "BNBUSDS"


BNBUSDS = BNBUSDS()


@dataclass(slots=True, frozen=True)
class BNBUSDT:
    name: str = "BNBUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "BNBUSDT"

    def __str__(self):
        return "BNBUSDT"

    def __call__(self):
        return "BNBUSDT"


BNBUSDT = BNBUSDT()


@dataclass(slots=True, frozen=True)
class BNBUST:
    name: str = "BNBUST"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBUST"

    def __str__(self):
        return "BNBUST"

    def __call__(self):
        return "BNBUST"


BNBUST = BNBUST()


@dataclass(slots=True, frozen=True)
class BNBZAR:
    name: str = "BNBZAR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNBZAR"

    def __str__(self):
        return "BNBZAR"

    def __call__(self):
        return "BNBZAR"


BNBZAR = BNBZAR()


@dataclass(slots=True, frozen=True)
class BNTBTC:
    name: str = "BNTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BNTBTC"

    def __str__(self):
        return "BNTBTC"

    def __call__(self):
        return "BNTBTC"


BNTBTC = BNTBTC()


@dataclass(slots=True, frozen=True)
class BNTBUSD:
    name: str = "BNTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BNTBUSD"

    def __str__(self):
        return "BNTBUSD"

    def __call__(self):
        return "BNTBUSD"


BNTBUSD = BNTBUSD()


@dataclass(slots=True, frozen=True)
class BNTETH:
    name: str = "BNTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BNTETH"

    def __str__(self):
        return "BNTETH"

    def __call__(self):
        return "BNTETH"


BNTETH = BNTETH()


@dataclass(slots=True, frozen=True)
class BNTUSDT:
    name: str = "BNTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "BNTUSDT"

    def __str__(self):
        return "BNTUSDT"

    def __call__(self):
        return "BNTUSDT"


BNTUSDT = BNTUSDT()


@dataclass(slots=True, frozen=True)
class BNXBNB:
    name: str = "BNXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BNXBNB"

    def __str__(self):
        return "BNXBNB"

    def __call__(self):
        return "BNXBNB"


BNXBNB = BNXBNB()


@dataclass(slots=True, frozen=True)
class BNXBTC:
    name: str = "BNXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BNXBTC"

    def __str__(self):
        return "BNXBTC"

    def __call__(self):
        return "BNXBTC"


BNXBTC = BNXBTC()


@dataclass(slots=True, frozen=True)
class BNXBUSD:
    name: str = "BNXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "BNXBUSD"

    def __str__(self):
        return "BNXBUSD"

    def __call__(self):
        return "BNXBUSD"


BNXBUSD = BNXBUSD()


@dataclass(slots=True, frozen=True)
class BNXUSDT:
    name: str = "BNXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "BNXUSDT"

    def __str__(self):
        return "BNXUSDT"

    def __call__(self):
        return "BNXUSDT"


BNXUSDT = BNXUSDT()


@dataclass(slots=True, frozen=True)
class BONDBNB:
    name: str = "BONDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BONDBNB"

    def __str__(self):
        return "BONDBNB"

    def __call__(self):
        return "BONDBNB"


BONDBNB = BONDBNB()


@dataclass(slots=True, frozen=True)
class BONDBTC:
    name: str = "BONDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "BONDBTC"

    def __str__(self):
        return "BONDBTC"

    def __call__(self):
        return "BONDBTC"


BONDBTC = BONDBTC()


@dataclass(slots=True, frozen=True)
class BONDBUSD:
    name: str = "BONDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "BONDBUSD"

    def __str__(self):
        return "BONDBUSD"

    def __call__(self):
        return "BONDBUSD"


BONDBUSD = BONDBUSD()


@dataclass(slots=True, frozen=True)
class BONDETH:
    name: str = "BONDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BONDETH"

    def __str__(self):
        return "BONDETH"

    def __call__(self):
        return "BONDETH"


BONDETH = BONDETH()


@dataclass(slots=True, frozen=True)
class BONDUSDT:
    name: str = "BONDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "BONDUSDT"

    def __str__(self):
        return "BONDUSDT"

    def __call__(self):
        return "BONDUSDT"


BONDUSDT = BONDUSDT()


@dataclass(slots=True, frozen=True)
class BOTBTC:
    name: str = "BOTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BOTBTC"

    def __str__(self):
        return "BOTBTC"

    def __call__(self):
        return "BOTBTC"


BOTBTC = BOTBTC()


@dataclass(slots=True, frozen=True)
class BOTBUSD:
    name: str = "BOTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BOTBUSD"

    def __str__(self):
        return "BOTBUSD"

    def __call__(self):
        return "BOTBUSD"


BOTBUSD = BOTBUSD()


@dataclass(slots=True, frozen=True)
class BQXBTC:
    name: str = "BQXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BQXBTC"

    def __str__(self):
        return "BQXBTC"

    def __call__(self):
        return "BQXBTC"


BQXBTC = BQXBTC()


@dataclass(slots=True, frozen=True)
class BQXETH:
    name: str = "BQXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 10.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BQXETH"

    def __str__(self):
        return "BQXETH"

    def __call__(self):
        return "BQXETH"


BQXETH = BQXETH()


@dataclass(slots=True, frozen=True)
class BRDBNB:
    name: str = "BRDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BRDBNB"

    def __str__(self):
        return "BRDBNB"

    def __call__(self):
        return "BRDBNB"


BRDBNB = BRDBNB()


@dataclass(slots=True, frozen=True)
class BRDBTC:
    name: str = "BRDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BRDBTC"

    def __str__(self):
        return "BRDBTC"

    def __call__(self):
        return "BRDBTC"


BRDBTC = BRDBTC()


@dataclass(slots=True, frozen=True)
class BRDETH:
    name: str = "BRDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BRDETH"

    def __str__(self):
        return "BRDETH"

    def __call__(self):
        return "BRDETH"


BRDETH = BRDETH()


@dataclass(slots=True, frozen=True)
class BSWBNB:
    name: str = "BSWBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BSWBNB"

    def __str__(self):
        return "BSWBNB"

    def __call__(self):
        return "BSWBNB"


BSWBNB = BSWBNB()


@dataclass(slots=True, frozen=True)
class BSWBUSD:
    name: str = "BSWBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "BSWBUSD"

    def __str__(self):
        return "BSWBUSD"

    def __call__(self):
        return "BSWBUSD"


BSWBUSD = BSWBUSD()


@dataclass(slots=True, frozen=True)
class BSWETH:
    name: str = "BSWETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BSWETH"

    def __str__(self):
        return "BSWETH"

    def __call__(self):
        return "BSWETH"


BSWETH = BSWETH()


@dataclass(slots=True, frozen=True)
class BSWTRY:
    name: str = "BSWTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "BSWTRY"

    def __str__(self):
        return "BSWTRY"

    def __call__(self):
        return "BSWTRY"


BSWTRY = BSWTRY()


@dataclass(slots=True, frozen=True)
class BSWUSDT:
    name: str = "BSWUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "BSWUSDT"

    def __str__(self):
        return "BSWUSDT"

    def __call__(self):
        return "BSWUSDT"


BSWUSDT = BSWUSDT()


@dataclass(slots=True, frozen=True)
class BTCAUD:
    name: str = "BTCAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCAUD"

    def __str__(self):
        return "BTCAUD"

    def __call__(self):
        return "BTCAUD"


BTCAUD = BTCAUD()


@dataclass(slots=True, frozen=True)
class BTCBBTC:
    name: str = "BTCBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCBBTC"

    def __str__(self):
        return "BTCBBTC"

    def __call__(self):
        return "BTCBBTC"


BTCBBTC = BTCBBTC()


@dataclass(slots=True, frozen=True)
class BTCBIDR:
    name: str = "BTCBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCBIDR"

    def __str__(self):
        return "BTCBIDR"

    def __call__(self):
        return "BTCBIDR"


BTCBIDR = BTCBIDR()


@dataclass(slots=True, frozen=True)
class BTCBKRW:
    name: str = "BTCBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00000100
    maximum_order_size: float = 100.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCBKRW"

    def __str__(self):
        return "BTCBKRW"

    def __call__(self):
        return "BTCBKRW"


BTCBKRW = BTCBKRW()


@dataclass(slots=True, frozen=True)
class BTCBRL:
    name: str = "BTCBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCBRL"

    def __str__(self):
        return "BTCBRL"

    def __call__(self):
        return "BTCBRL"


BTCBRL = BTCBRL()


@dataclass(slots=True, frozen=True)
class BTCBUSD:
    name: str = "BTCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = True

    def __repr__(self):
        return "BTCBUSD"

    def __str__(self):
        return "BTCBUSD"

    def __call__(self):
        return "BTCBUSD"


BTCBUSD = BTCBUSD()


@dataclass(slots=True, frozen=True)
class BTCDAI:
    name: str = "BTCDAI"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCDAI"

    def __str__(self):
        return "BTCDAI"

    def __call__(self):
        return "BTCDAI"


BTCDAI = BTCDAI()


@dataclass(slots=True, frozen=True)
class BTCDOWNUSDT:
    name: str = "BTCDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 921415.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCDOWNUSDT"

    def __str__(self):
        return "BTCDOWNUSDT"

    def __call__(self):
        return "BTCDOWNUSDT"


BTCDOWNUSDT = BTCDOWNUSDT()


@dataclass(slots=True, frozen=True)
class BTCEUR:
    name: str = "BTCEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCEUR"

    def __str__(self):
        return "BTCEUR"

    def __call__(self):
        return "BTCEUR"


BTCEUR = BTCEUR()


@dataclass(slots=True, frozen=True)
class BTCGBP:
    name: str = "BTCGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCGBP"

    def __str__(self):
        return "BTCGBP"

    def __call__(self):
        return "BTCGBP"


BTCGBP = BTCGBP()


@dataclass(slots=True, frozen=True)
class BTCIDRT:
    name: str = "BTCIDRT"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCIDRT"

    def __str__(self):
        return "BTCIDRT"

    def __call__(self):
        return "BTCIDRT"


BTCIDRT = BTCIDRT()


@dataclass(slots=True, frozen=True)
class BTCNGN:
    name: str = "BTCNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 305.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCNGN"

    def __str__(self):
        return "BTCNGN"

    def __call__(self):
        return "BTCNGN"


BTCNGN = BTCNGN()


@dataclass(slots=True, frozen=True)
class BTCPAX:
    name: str = "BTCPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCPAX"

    def __str__(self):
        return "BTCPAX"

    def __call__(self):
        return "BTCPAX"


BTCPAX = BTCPAX()


@dataclass(slots=True, frozen=True)
class BTCPLN:
    name: str = "BTCPLN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9223.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCPLN"

    def __str__(self):
        return "BTCPLN"

    def __call__(self):
        return "BTCPLN"


BTCPLN = BTCPLN()


@dataclass(slots=True, frozen=True)
class BTCRUB:
    name: str = "BTCRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 900.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCRUB"

    def __str__(self):
        return "BTCRUB"

    def __call__(self):
        return "BTCRUB"


BTCRUB = BTCRUB()


@dataclass(slots=True, frozen=True)
class BTCSTBTC:
    name: str = "BTCSTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCSTBTC"

    def __str__(self):
        return "BTCSTBTC"

    def __call__(self):
        return "BTCSTBTC"


BTCSTBTC = BTCSTBTC()


@dataclass(slots=True, frozen=True)
class BTCSTBUSD:
    name: str = "BTCSTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCSTBUSD"

    def __str__(self):
        return "BTCSTBUSD"

    def __call__(self):
        return "BTCSTBUSD"


BTCSTBUSD = BTCSTBUSD()


@dataclass(slots=True, frozen=True)
class BTCSTUSDT:
    name: str = "BTCSTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCSTUSDT"

    def __str__(self):
        return "BTCSTUSDT"

    def __call__(self):
        return "BTCSTUSDT"


BTCSTUSDT = BTCSTUSDT()


@dataclass(slots=True, frozen=True)
class BTCTRY:
    name: str = "BTCTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCTRY"

    def __str__(self):
        return "BTCTRY"

    def __call__(self):
        return "BTCTRY"


BTCTRY = BTCTRY()


@dataclass(slots=True, frozen=True)
class BTCTUSD:
    name: str = "BTCTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCTUSD"

    def __str__(self):
        return "BTCTUSD"

    def __call__(self):
        return "BTCTUSD"


BTCTUSD = BTCTUSD()


@dataclass(slots=True, frozen=True)
class BTCUAH:
    name: str = "BTCUAH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 1800.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCUAH"

    def __str__(self):
        return "BTCUAH"

    def __call__(self):
        return "BTCUAH"


BTCUAH = BTCUAH()


@dataclass(slots=True, frozen=True)
class BTCUPUSDT:
    name: str = "BTCUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 3000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCUPUSDT"

    def __str__(self):
        return "BTCUPUSDT"

    def __call__(self):
        return "BTCUPUSDT"


BTCUPUSDT = BTCUPUSDT()


@dataclass(slots=True, frozen=True)
class BTCUSDC:
    name: str = "BTCUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCUSDC"

    def __str__(self):
        return "BTCUSDC"

    def __call__(self):
        return "BTCUSDC"


BTCUSDC = BTCUSDC()


@dataclass(slots=True, frozen=True)
class BTCUSDP:
    name: str = "BTCUSDP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9223.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCUSDP"

    def __str__(self):
        return "BTCUSDP"

    def __call__(self):
        return "BTCUSDP"


BTCUSDP = BTCUSDP()


@dataclass(slots=True, frozen=True)
class BTCUSDS:
    name: str = "BTCUSDS"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00000100
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCUSDS"

    def __str__(self):
        return "BTCUSDS"

    def __call__(self):
        return "BTCUSDS"


BTCUSDS = BTCUSDS()


@dataclass(slots=True, frozen=True)
class BTCUSDT:
    name: str = "BTCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = True

    def __repr__(self):
        return "BTCUSDT"

    def __str__(self):
        return "BTCUSDT"

    def __call__(self):
        return "BTCUSDT"


BTCUSDT = BTCUSDT()


@dataclass(slots=True, frozen=True)
class BTCUST:
    name: str = "BTCUST"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCUST"

    def __str__(self):
        return "BTCUST"

    def __call__(self):
        return "BTCUST"


BTCUST = BTCUST()


@dataclass(slots=True, frozen=True)
class BTCVAI:
    name: str = "BTCVAI"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCVAI"

    def __str__(self):
        return "BTCVAI"

    def __call__(self):
        return "BTCVAI"


BTCVAI = BTCVAI()


@dataclass(slots=True, frozen=True)
class BTCZAR:
    name: str = "BTCZAR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 922.00000000
    margin: bool = False

    def __repr__(self):
        return "BTCZAR"

    def __str__(self):
        return "BTCZAR"

    def __call__(self):
        return "BTCZAR"


BTCZAR = BTCZAR()


@dataclass(slots=True, frozen=True)
class BTGBTC:
    name: str = "BTGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BTGBTC"

    def __str__(self):
        return "BTGBTC"

    def __call__(self):
        return "BTGBTC"


BTGBTC = BTGBTC()


@dataclass(slots=True, frozen=True)
class BTGBUSD:
    name: str = "BTGBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BTGBUSD"

    def __str__(self):
        return "BTGBUSD"

    def __call__(self):
        return "BTGBUSD"


BTGBUSD = BTGBUSD()


@dataclass(slots=True, frozen=True)
class BTGETH:
    name: str = "BTGETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTGETH"

    def __str__(self):
        return "BTGETH"

    def __call__(self):
        return "BTGETH"


BTGETH = BTGETH()


@dataclass(slots=True, frozen=True)
class BTGUSDT:
    name: str = "BTGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BTGUSDT"

    def __str__(self):
        return "BTGUSDT"

    def __call__(self):
        return "BTGUSDT"


BTGUSDT = BTGUSDT()


@dataclass(slots=True, frozen=True)
class BTSBNB:
    name: str = "BTSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTSBNB"

    def __str__(self):
        return "BTSBNB"

    def __call__(self):
        return "BTSBNB"


BTSBNB = BTSBNB()


@dataclass(slots=True, frozen=True)
class BTSBTC:
    name: str = "BTSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BTSBTC"

    def __str__(self):
        return "BTSBTC"

    def __call__(self):
        return "BTSBTC"


BTSBTC = BTSBTC()


@dataclass(slots=True, frozen=True)
class BTSBUSD:
    name: str = "BTSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTSBUSD"

    def __str__(self):
        return "BTSBUSD"

    def __call__(self):
        return "BTSBUSD"


BTSBUSD = BTSBUSD()


@dataclass(slots=True, frozen=True)
class BTSETH:
    name: str = "BTSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTSETH"

    def __str__(self):
        return "BTSETH"

    def __call__(self):
        return "BTSETH"


BTSETH = BTSETH()


@dataclass(slots=True, frozen=True)
class BTSUSDT:
    name: str = "BTSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BTSUSDT"

    def __str__(self):
        return "BTSUSDT"

    def __call__(self):
        return "BTSUSDT"


BTSUSDT = BTSUSDT()


@dataclass(slots=True, frozen=True)
class BTTBNB:
    name: str = "BTTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTBNB"

    def __str__(self):
        return "BTTBNB"

    def __call__(self):
        return "BTTBNB"


BTTBNB = BTTBNB()


@dataclass(slots=True, frozen=True)
class BTTBRL:
    name: str = "BTTBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTBRL"

    def __str__(self):
        return "BTTBRL"

    def __call__(self):
        return "BTTBRL"


BTTBRL = BTTBRL()


@dataclass(slots=True, frozen=True)
class BTTBTC:
    name: str = "BTTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTBTC"

    def __str__(self):
        return "BTTBTC"

    def __call__(self):
        return "BTTBTC"


BTTBTC = BTTBTC()


@dataclass(slots=True, frozen=True)
class BTTBUSD:
    name: str = "BTTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTBUSD"

    def __str__(self):
        return "BTTBUSD"

    def __call__(self):
        return "BTTBUSD"


BTTBUSD = BTTBUSD()


@dataclass(slots=True, frozen=True)
class BTTCBUSD:
    name: str = "BTTCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.0
    maximum_order_size: float = 92233720368.0
    margin: bool = False

    def __repr__(self):
        return "BTTCBUSD"

    def __str__(self):
        return "BTTCBUSD"

    def __call__(self):
        return "BTTCBUSD"


BTTCBUSD = BTTCBUSD()


@dataclass(slots=True, frozen=True)
class BTTCTRY:
    name: str = "BTTCTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.0
    maximum_order_size: float = 92233720368.0
    margin: bool = False

    def __repr__(self):
        return "BTTCTRY"

    def __str__(self):
        return "BTTCTRY"

    def __call__(self):
        return "BTTCTRY"


BTTCTRY = BTTCTRY()


@dataclass(slots=True, frozen=True)
class BTTCUSDC:
    name: str = "BTTCUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.0
    maximum_order_size: float = 92233720368.0
    margin: bool = False

    def __repr__(self):
        return "BTTCUSDC"

    def __str__(self):
        return "BTTCUSDC"

    def __call__(self):
        return "BTTCUSDC"


BTTCUSDC = BTTCUSDC()


@dataclass(slots=True, frozen=True)
class BTTCUSDT:
    name: str = "BTTCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.0
    maximum_order_size: float = 92233720368.0
    margin: bool = False

    def __repr__(self):
        return "BTTCUSDT"

    def __str__(self):
        return "BTTCUSDT"

    def __call__(self):
        return "BTTCUSDT"


BTTCUSDT = BTTCUSDT()


@dataclass(slots=True, frozen=True)
class BTTEUR:
    name: str = "BTTEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTEUR"

    def __str__(self):
        return "BTTEUR"

    def __call__(self):
        return "BTTEUR"


BTTEUR = BTTEUR()


@dataclass(slots=True, frozen=True)
class BTTPAX:
    name: str = "BTTPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTPAX"

    def __str__(self):
        return "BTTPAX"

    def __call__(self):
        return "BTTPAX"


BTTPAX = BTTPAX()


@dataclass(slots=True, frozen=True)
class BTTTRX:
    name: str = "BTTTRX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTTRX"

    def __str__(self):
        return "BTTTRX"

    def __call__(self):
        return "BTTTRX"


BTTTRX = BTTTRX()


@dataclass(slots=True, frozen=True)
class BTTTRY:
    name: str = "BTTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTTRY"

    def __str__(self):
        return "BTTTRY"

    def __call__(self):
        return "BTTTRY"


BTTTRY = BTTTRY()


@dataclass(slots=True, frozen=True)
class BTTTUSD:
    name: str = "BTTTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTTUSD"

    def __str__(self):
        return "BTTTUSD"

    def __call__(self):
        return "BTTTUSD"


BTTTUSD = BTTTUSD()


@dataclass(slots=True, frozen=True)
class BTTUSDC:
    name: str = "BTTUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTUSDC"

    def __str__(self):
        return "BTTUSDC"

    def __call__(self):
        return "BTTUSDC"


BTTUSDC = BTTUSDC()


@dataclass(slots=True, frozen=True)
class BTTUSDT:
    name: str = "BTTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BTTUSDT"

    def __str__(self):
        return "BTTUSDT"

    def __call__(self):
        return "BTTUSDT"


BTTUSDT = BTTUSDT()


@dataclass(slots=True, frozen=True)
class BULLBUSD:
    name: str = "BULLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00000100
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BULLBUSD"

    def __str__(self):
        return "BULLBUSD"

    def __call__(self):
        return "BULLBUSD"


BULLBUSD = BULLBUSD()


@dataclass(slots=True, frozen=True)
class BULLUSDT:
    name: str = "BULLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00000100
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "BULLUSDT"

    def __str__(self):
        return "BULLUSDT"

    def __call__(self):
        return "BULLUSDT"


BULLUSDT = BULLUSDT()


@dataclass(slots=True, frozen=True)
class BURGERBNB:
    name: str = "BURGERBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BURGERBNB"

    def __str__(self):
        return "BURGERBNB"

    def __call__(self):
        return "BURGERBNB"


BURGERBNB = BURGERBNB()


@dataclass(slots=True, frozen=True)
class BURGERBUSD:
    name: str = "BURGERBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "BURGERBUSD"

    def __str__(self):
        return "BURGERBUSD"

    def __call__(self):
        return "BURGERBUSD"


BURGERBUSD = BURGERBUSD()


@dataclass(slots=True, frozen=True)
class BURGERETH:
    name: str = "BURGERETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BURGERETH"

    def __str__(self):
        return "BURGERETH"

    def __call__(self):
        return "BURGERETH"


BURGERETH = BURGERETH()


@dataclass(slots=True, frozen=True)
class BURGERUSDT:
    name: str = "BURGERUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "BURGERUSDT"

    def __str__(self):
        return "BURGERUSDT"

    def __call__(self):
        return "BURGERUSDT"


BURGERUSDT = BURGERUSDT()


@dataclass(slots=True, frozen=True)
class BUSDBIDR:
    name: str = "BUSDBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 1000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDBIDR"

    def __str__(self):
        return "BUSDBIDR"

    def __call__(self):
        return "BUSDBIDR"


BUSDBIDR = BUSDBIDR()


@dataclass(slots=True, frozen=True)
class BUSDBKRW:
    name: str = "BUSDBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDBKRW"

    def __str__(self):
        return "BUSDBKRW"

    def __call__(self):
        return "BUSDBKRW"


BUSDBKRW = BUSDBKRW()


@dataclass(slots=True, frozen=True)
class BUSDBRL:
    name: str = "BUSDBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDBRL"

    def __str__(self):
        return "BUSDBRL"

    def __call__(self):
        return "BUSDBRL"


BUSDBRL = BUSDBRL()


@dataclass(slots=True, frozen=True)
class BUSDBVND:
    name: str = "BUSDBVND"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 1000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDBVND"

    def __str__(self):
        return "BUSDBVND"

    def __call__(self):
        return "BUSDBVND"


BUSDBVND = BUSDBVND()


@dataclass(slots=True, frozen=True)
class BUSDDAI:
    name: str = "BUSDDAI"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDDAI"

    def __str__(self):
        return "BUSDDAI"

    def __call__(self):
        return "BUSDDAI"


BUSDDAI = BUSDDAI()


@dataclass(slots=True, frozen=True)
class BUSDIDRT:
    name: str = "BUSDIDRT"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 1000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDIDRT"

    def __str__(self):
        return "BUSDIDRT"

    def __call__(self):
        return "BUSDIDRT"


BUSDIDRT = BUSDIDRT()


@dataclass(slots=True, frozen=True)
class BUSDNGN:
    name: str = "BUSDNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922320.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDNGN"

    def __str__(self):
        return "BUSDNGN"

    def __call__(self):
        return "BUSDNGN"


BUSDNGN = BUSDNGN()


@dataclass(slots=True, frozen=True)
class BUSDPLN:
    name: str = "BUSDPLN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDPLN"

    def __str__(self):
        return "BUSDPLN"

    def __call__(self):
        return "BUSDPLN"


BUSDPLN = BUSDPLN()


@dataclass(slots=True, frozen=True)
class BUSDRON:
    name: str = "BUSDRON"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDRON"

    def __str__(self):
        return "BUSDRON"

    def __call__(self):
        return "BUSDRON"


BUSDRON = BUSDRON()


@dataclass(slots=True, frozen=True)
class BUSDRUB:
    name: str = "BUSDRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDRUB"

    def __str__(self):
        return "BUSDRUB"

    def __call__(self):
        return "BUSDRUB"


BUSDRUB = BUSDRUB()


@dataclass(slots=True, frozen=True)
class BUSDTRY:
    name: str = "BUSDTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDTRY"

    def __str__(self):
        return "BUSDTRY"

    def __call__(self):
        return "BUSDTRY"


BUSDTRY = BUSDTRY()


@dataclass(slots=True, frozen=True)
class BUSDUAH:
    name: str = "BUSDUAH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDUAH"

    def __str__(self):
        return "BUSDUAH"

    def __call__(self):
        return "BUSDUAH"


BUSDUAH = BUSDUAH()


@dataclass(slots=True, frozen=True)
class BUSDUSDT:
    name: str = "BUSDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 15000000.00000000
    margin: bool = True

    def __repr__(self):
        return "BUSDUSDT"

    def __str__(self):
        return "BUSDUSDT"

    def __call__(self):
        return "BUSDUSDT"


BUSDUSDT = BUSDUSDT()


@dataclass(slots=True, frozen=True)
class BUSDVAI:
    name: str = "BUSDVAI"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDVAI"

    def __str__(self):
        return "BUSDVAI"

    def __call__(self):
        return "BUSDVAI"


BUSDVAI = BUSDVAI()


@dataclass(slots=True, frozen=True)
class BUSDZAR:
    name: str = "BUSDZAR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "BUSDZAR"

    def __str__(self):
        return "BUSDZAR"

    def __call__(self):
        return "BUSDZAR"


BUSDZAR = BUSDZAR()


@dataclass(slots=True, frozen=True)
class BZRXBNB:
    name: str = "BZRXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BZRXBNB"

    def __str__(self):
        return "BZRXBNB"

    def __call__(self):
        return "BZRXBNB"


BZRXBNB = BZRXBNB()


@dataclass(slots=True, frozen=True)
class BZRXBTC:
    name: str = "BZRXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "BZRXBTC"

    def __str__(self):
        return "BZRXBTC"

    def __call__(self):
        return "BZRXBTC"


BZRXBTC = BZRXBTC()


@dataclass(slots=True, frozen=True)
class BZRXBUSD:
    name: str = "BZRXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BZRXBUSD"

    def __str__(self):
        return "BZRXBUSD"

    def __call__(self):
        return "BZRXBUSD"


BZRXBUSD = BZRXBUSD()


@dataclass(slots=True, frozen=True)
class BZRXUSDT:
    name: str = "BZRXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "BZRXUSDT"

    def __str__(self):
        return "BZRXUSDT"

    def __call__(self):
        return "BZRXUSDT"


BZRXUSDT = BZRXUSDT()


@dataclass(slots=True, frozen=True)
class C98BNB:
    name: str = "C98BNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "C98BNB"

    def __str__(self):
        return "C98BNB"

    def __call__(self):
        return "C98BNB"


C98BNB = C98BNB()


@dataclass(slots=True, frozen=True)
class C98BRL:
    name: str = "C98BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "C98BRL"

    def __str__(self):
        return "C98BRL"

    def __call__(self):
        return "C98BRL"


C98BRL = C98BRL()


@dataclass(slots=True, frozen=True)
class C98BTC:
    name: str = "C98BTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "C98BTC"

    def __str__(self):
        return "C98BTC"

    def __call__(self):
        return "C98BTC"


C98BTC = C98BTC()


@dataclass(slots=True, frozen=True)
class C98BUSD:
    name: str = "C98BUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "C98BUSD"

    def __str__(self):
        return "C98BUSD"

    def __call__(self):
        return "C98BUSD"


C98BUSD = C98BUSD()


@dataclass(slots=True, frozen=True)
class C98USDT:
    name: str = "C98USDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "C98USDT"

    def __str__(self):
        return "C98USDT"

    def __call__(self):
        return "C98USDT"


C98USDT = C98USDT()


@dataclass(slots=True, frozen=True)
class CAKEAUD:
    name: str = "CAKEAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CAKEAUD"

    def __str__(self):
        return "CAKEAUD"

    def __call__(self):
        return "CAKEAUD"


CAKEAUD = CAKEAUD()


@dataclass(slots=True, frozen=True)
class CAKEBNB:
    name: str = "CAKEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CAKEBNB"

    def __str__(self):
        return "CAKEBNB"

    def __call__(self):
        return "CAKEBNB"


CAKEBNB = CAKEBNB()


@dataclass(slots=True, frozen=True)
class CAKEBRL:
    name: str = "CAKEBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CAKEBRL"

    def __str__(self):
        return "CAKEBRL"

    def __call__(self):
        return "CAKEBRL"


CAKEBRL = CAKEBRL()


@dataclass(slots=True, frozen=True)
class CAKEBTC:
    name: str = "CAKEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CAKEBTC"

    def __str__(self):
        return "CAKEBTC"

    def __call__(self):
        return "CAKEBTC"


CAKEBTC = CAKEBTC()


@dataclass(slots=True, frozen=True)
class CAKEBUSD:
    name: str = "CAKEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "CAKEBUSD"

    def __str__(self):
        return "CAKEBUSD"

    def __call__(self):
        return "CAKEBUSD"


CAKEBUSD = CAKEBUSD()


@dataclass(slots=True, frozen=True)
class CAKEGBP:
    name: str = "CAKEGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "CAKEGBP"

    def __str__(self):
        return "CAKEGBP"

    def __call__(self):
        return "CAKEGBP"


CAKEGBP = CAKEGBP()


@dataclass(slots=True, frozen=True)
class CAKEUSDT:
    name: str = "CAKEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "CAKEUSDT"

    def __str__(self):
        return "CAKEUSDT"

    def __call__(self):
        return "CAKEUSDT"


CAKEUSDT = CAKEUSDT()


@dataclass(slots=True, frozen=True)
class CDTBTC:
    name: str = "CDTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CDTBTC"

    def __str__(self):
        return "CDTBTC"

    def __call__(self):
        return "CDTBTC"


CDTBTC = CDTBTC()


@dataclass(slots=True, frozen=True)
class CDTETH:
    name: str = "CDTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CDTETH"

    def __str__(self):
        return "CDTETH"

    def __call__(self):
        return "CDTETH"


CDTETH = CDTETH()


@dataclass(slots=True, frozen=True)
class CELOBTC:
    name: str = "CELOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CELOBTC"

    def __str__(self):
        return "CELOBTC"

    def __call__(self):
        return "CELOBTC"


CELOBTC = CELOBTC()


@dataclass(slots=True, frozen=True)
class CELOBUSD:
    name: str = "CELOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "CELOBUSD"

    def __str__(self):
        return "CELOBUSD"

    def __call__(self):
        return "CELOBUSD"


CELOBUSD = CELOBUSD()


@dataclass(slots=True, frozen=True)
class CELOUSDT:
    name: str = "CELOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "CELOUSDT"

    def __str__(self):
        return "CELOUSDT"

    def __call__(self):
        return "CELOUSDT"


CELOUSDT = CELOUSDT()


@dataclass(slots=True, frozen=True)
class CELRBNB:
    name: str = "CELRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CELRBNB"

    def __str__(self):
        return "CELRBNB"

    def __call__(self):
        return "CELRBNB"


CELRBNB = CELRBNB()


@dataclass(slots=True, frozen=True)
class CELRBTC:
    name: str = "CELRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CELRBTC"

    def __str__(self):
        return "CELRBTC"

    def __call__(self):
        return "CELRBTC"


CELRBTC = CELRBTC()


@dataclass(slots=True, frozen=True)
class CELRBUSD:
    name: str = "CELRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CELRBUSD"

    def __str__(self):
        return "CELRBUSD"

    def __call__(self):
        return "CELRBUSD"


CELRBUSD = CELRBUSD()


@dataclass(slots=True, frozen=True)
class CELRETH:
    name: str = "CELRETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CELRETH"

    def __str__(self):
        return "CELRETH"

    def __call__(self):
        return "CELRETH"


CELRETH = CELRETH()


@dataclass(slots=True, frozen=True)
class CELRUSDT:
    name: str = "CELRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "CELRUSDT"

    def __str__(self):
        return "CELRUSDT"

    def __call__(self):
        return "CELRUSDT"


CELRUSDT = CELRUSDT()


@dataclass(slots=True, frozen=True)
class CFXBTC:
    name: str = "CFXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CFXBTC"

    def __str__(self):
        return "CFXBTC"

    def __call__(self):
        return "CFXBTC"


CFXBTC = CFXBTC()


@dataclass(slots=True, frozen=True)
class CFXBUSD:
    name: str = "CFXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CFXBUSD"

    def __str__(self):
        return "CFXBUSD"

    def __call__(self):
        return "CFXBUSD"


CFXBUSD = CFXBUSD()


@dataclass(slots=True, frozen=True)
class CFXUSDT:
    name: str = "CFXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CFXUSDT"

    def __str__(self):
        return "CFXUSDT"

    def __call__(self):
        return "CFXUSDT"


CFXUSDT = CFXUSDT()


@dataclass(slots=True, frozen=True)
class CHATBTC:
    name: str = "CHATBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CHATBTC"

    def __str__(self):
        return "CHATBTC"

    def __call__(self):
        return "CHATBTC"


CHATBTC = CHATBTC()


@dataclass(slots=True, frozen=True)
class CHATETH:
    name: str = "CHATETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CHATETH"

    def __str__(self):
        return "CHATETH"

    def __call__(self):
        return "CHATETH"


CHATETH = CHATETH()


@dataclass(slots=True, frozen=True)
class CHESSBNB:
    name: str = "CHESSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CHESSBNB"

    def __str__(self):
        return "CHESSBNB"

    def __call__(self):
        return "CHESSBNB"


CHESSBNB = CHESSBNB()


@dataclass(slots=True, frozen=True)
class CHESSBTC:
    name: str = "CHESSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CHESSBTC"

    def __str__(self):
        return "CHESSBTC"

    def __call__(self):
        return "CHESSBTC"


CHESSBTC = CHESSBTC()


@dataclass(slots=True, frozen=True)
class CHESSBUSD:
    name: str = "CHESSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CHESSBUSD"

    def __str__(self):
        return "CHESSBUSD"

    def __call__(self):
        return "CHESSBUSD"


CHESSBUSD = CHESSBUSD()


@dataclass(slots=True, frozen=True)
class CHESSUSDT:
    name: str = "CHESSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CHESSUSDT"

    def __str__(self):
        return "CHESSUSDT"

    def __call__(self):
        return "CHESSUSDT"


CHESSUSDT = CHESSUSDT()


@dataclass(slots=True, frozen=True)
class CHRBNB:
    name: str = "CHRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CHRBNB"

    def __str__(self):
        return "CHRBNB"

    def __call__(self):
        return "CHRBNB"


CHRBNB = CHRBNB()


@dataclass(slots=True, frozen=True)
class CHRBTC:
    name: str = "CHRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CHRBTC"

    def __str__(self):
        return "CHRBTC"

    def __call__(self):
        return "CHRBTC"


CHRBTC = CHRBTC()


@dataclass(slots=True, frozen=True)
class CHRBUSD:
    name: str = "CHRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "CHRBUSD"

    def __str__(self):
        return "CHRBUSD"

    def __call__(self):
        return "CHRBUSD"


CHRBUSD = CHRBUSD()


@dataclass(slots=True, frozen=True)
class CHRETH:
    name: str = "CHRETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CHRETH"

    def __str__(self):
        return "CHRETH"

    def __call__(self):
        return "CHRETH"


CHRETH = CHRETH()


@dataclass(slots=True, frozen=True)
class CHRUSDT:
    name: str = "CHRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CHRUSDT"

    def __str__(self):
        return "CHRUSDT"

    def __call__(self):
        return "CHRUSDT"


CHRUSDT = CHRUSDT()


@dataclass(slots=True, frozen=True)
class CHZBNB:
    name: str = "CHZBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CHZBNB"

    def __str__(self):
        return "CHZBNB"

    def __call__(self):
        return "CHZBNB"


CHZBNB = CHZBNB()


@dataclass(slots=True, frozen=True)
class CHZBRL:
    name: str = "CHZBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CHZBRL"

    def __str__(self):
        return "CHZBRL"

    def __call__(self):
        return "CHZBRL"


CHZBRL = CHZBRL()


@dataclass(slots=True, frozen=True)
class CHZBTC:
    name: str = "CHZBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CHZBTC"

    def __str__(self):
        return "CHZBTC"

    def __call__(self):
        return "CHZBTC"


CHZBTC = CHZBTC()


@dataclass(slots=True, frozen=True)
class CHZBUSD:
    name: str = "CHZBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "CHZBUSD"

    def __str__(self):
        return "CHZBUSD"

    def __call__(self):
        return "CHZBUSD"


CHZBUSD = CHZBUSD()


@dataclass(slots=True, frozen=True)
class CHZEUR:
    name: str = "CHZEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "CHZEUR"

    def __str__(self):
        return "CHZEUR"

    def __call__(self):
        return "CHZEUR"


CHZEUR = CHZEUR()


@dataclass(slots=True, frozen=True)
class CHZGBP:
    name: str = "CHZGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "CHZGBP"

    def __str__(self):
        return "CHZGBP"

    def __call__(self):
        return "CHZGBP"


CHZGBP = CHZGBP()


@dataclass(slots=True, frozen=True)
class CHZTRY:
    name: str = "CHZTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CHZTRY"

    def __str__(self):
        return "CHZTRY"

    def __call__(self):
        return "CHZTRY"


CHZTRY = CHZTRY()


@dataclass(slots=True, frozen=True)
class CHZUSDT:
    name: str = "CHZUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CHZUSDT"

    def __str__(self):
        return "CHZUSDT"

    def __call__(self):
        return "CHZUSDT"


CHZUSDT = CHZUSDT()


@dataclass(slots=True, frozen=True)
class CITYBNB:
    name: str = "CITYBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CITYBNB"

    def __str__(self):
        return "CITYBNB"

    def __call__(self):
        return "CITYBNB"


CITYBNB = CITYBNB()


@dataclass(slots=True, frozen=True)
class CITYBTC:
    name: str = "CITYBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CITYBTC"

    def __str__(self):
        return "CITYBTC"

    def __call__(self):
        return "CITYBTC"


CITYBTC = CITYBTC()


@dataclass(slots=True, frozen=True)
class CITYBUSD:
    name: str = "CITYBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CITYBUSD"

    def __str__(self):
        return "CITYBUSD"

    def __call__(self):
        return "CITYBUSD"


CITYBUSD = CITYBUSD()


@dataclass(slots=True, frozen=True)
class CITYUSDT:
    name: str = "CITYUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CITYUSDT"

    def __str__(self):
        return "CITYUSDT"

    def __call__(self):
        return "CITYUSDT"


CITYUSDT = CITYUSDT()


@dataclass(slots=True, frozen=True)
class CKBBTC:
    name: str = "CKBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CKBBTC"

    def __str__(self):
        return "CKBBTC"

    def __call__(self):
        return "CKBBTC"


CKBBTC = CKBBTC()


@dataclass(slots=True, frozen=True)
class CKBBUSD:
    name: str = "CKBBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CKBBUSD"

    def __str__(self):
        return "CKBBUSD"

    def __call__(self):
        return "CKBBUSD"


CKBBUSD = CKBBUSD()


@dataclass(slots=True, frozen=True)
class CKBUSDT:
    name: str = "CKBUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "CKBUSDT"

    def __str__(self):
        return "CKBUSDT"

    def __call__(self):
        return "CKBUSDT"


CKBUSDT = CKBUSDT()


@dataclass(slots=True, frozen=True)
class CLOAKBTC:
    name: str = "CLOAKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CLOAKBTC"

    def __str__(self):
        return "CLOAKBTC"

    def __call__(self):
        return "CLOAKBTC"


CLOAKBTC = CLOAKBTC()


@dataclass(slots=True, frozen=True)
class CLOAKETH:
    name: str = "CLOAKETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CLOAKETH"

    def __str__(self):
        return "CLOAKETH"

    def __call__(self):
        return "CLOAKETH"


CLOAKETH = CLOAKETH()


@dataclass(slots=True, frozen=True)
class CLVBNB:
    name: str = "CLVBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CLVBNB"

    def __str__(self):
        return "CLVBNB"

    def __call__(self):
        return "CLVBNB"


CLVBNB = CLVBNB()


@dataclass(slots=True, frozen=True)
class CLVBTC:
    name: str = "CLVBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "CLVBTC"

    def __str__(self):
        return "CLVBTC"

    def __call__(self):
        return "CLVBTC"


CLVBTC = CLVBTC()


@dataclass(slots=True, frozen=True)
class CLVBUSD:
    name: str = "CLVBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "CLVBUSD"

    def __str__(self):
        return "CLVBUSD"

    def __call__(self):
        return "CLVBUSD"


CLVBUSD = CLVBUSD()


@dataclass(slots=True, frozen=True)
class CLVUSDT:
    name: str = "CLVUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "CLVUSDT"

    def __str__(self):
        return "CLVUSDT"

    def __call__(self):
        return "CLVUSDT"


CLVUSDT = CLVUSDT()


@dataclass(slots=True, frozen=True)
class CMTBNB:
    name: str = "CMTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CMTBNB"

    def __str__(self):
        return "CMTBNB"

    def __call__(self):
        return "CMTBNB"


CMTBNB = CMTBNB()


@dataclass(slots=True, frozen=True)
class CMTBTC:
    name: str = "CMTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CMTBTC"

    def __str__(self):
        return "CMTBTC"

    def __call__(self):
        return "CMTBTC"


CMTBTC = CMTBTC()


@dataclass(slots=True, frozen=True)
class CMTETH:
    name: str = "CMTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CMTETH"

    def __str__(self):
        return "CMTETH"

    def __call__(self):
        return "CMTETH"


CMTETH = CMTETH()


@dataclass(slots=True, frozen=True)
class CNDBNB:
    name: str = "CNDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CNDBNB"

    def __str__(self):
        return "CNDBNB"

    def __call__(self):
        return "CNDBNB"


CNDBNB = CNDBNB()


@dataclass(slots=True, frozen=True)
class CNDBTC:
    name: str = "CNDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CNDBTC"

    def __str__(self):
        return "CNDBTC"

    def __call__(self):
        return "CNDBTC"


CNDBTC = CNDBTC()


@dataclass(slots=True, frozen=True)
class CNDETH:
    name: str = "CNDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CNDETH"

    def __str__(self):
        return "CNDETH"

    def __call__(self):
        return "CNDETH"


CNDETH = CNDETH()


@dataclass(slots=True, frozen=True)
class COCOSBNB:
    name: str = "COCOSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "COCOSBNB"

    def __str__(self):
        return "COCOSBNB"

    def __call__(self):
        return "COCOSBNB"


COCOSBNB = COCOSBNB()


@dataclass(slots=True, frozen=True)
class COCOSBTC:
    name: str = "COCOSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "COCOSBTC"

    def __str__(self):
        return "COCOSBTC"

    def __call__(self):
        return "COCOSBTC"


COCOSBTC = COCOSBTC()


@dataclass(slots=True, frozen=True)
class COCOSBUSD:
    name: str = "COCOSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "COCOSBUSD"

    def __str__(self):
        return "COCOSBUSD"

    def __call__(self):
        return "COCOSBUSD"


COCOSBUSD = COCOSBUSD()


@dataclass(slots=True, frozen=True)
class COCOSTRY:
    name: str = "COCOSTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "COCOSTRY"

    def __str__(self):
        return "COCOSTRY"

    def __call__(self):
        return "COCOSTRY"


COCOSTRY = COCOSTRY()


@dataclass(slots=True, frozen=True)
class COCOSUSDT:
    name: str = "COCOSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "COCOSUSDT"

    def __str__(self):
        return "COCOSUSDT"

    def __call__(self):
        return "COCOSUSDT"


COCOSUSDT = COCOSUSDT()


@dataclass(slots=True, frozen=True)
class COMPBNB:
    name: str = "COMPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "COMPBNB"

    def __str__(self):
        return "COMPBNB"

    def __call__(self):
        return "COMPBNB"


COMPBNB = COMPBNB()


@dataclass(slots=True, frozen=True)
class COMPBTC:
    name: str = "COMPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "COMPBTC"

    def __str__(self):
        return "COMPBTC"

    def __call__(self):
        return "COMPBTC"


COMPBTC = COMPBTC()


@dataclass(slots=True, frozen=True)
class COMPBUSD:
    name: str = "COMPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "COMPBUSD"

    def __str__(self):
        return "COMPBUSD"

    def __call__(self):
        return "COMPBUSD"


COMPBUSD = COMPBUSD()


@dataclass(slots=True, frozen=True)
class COMPUSDT:
    name: str = "COMPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "COMPUSDT"

    def __str__(self):
        return "COMPUSDT"

    def __call__(self):
        return "COMPUSDT"


COMPUSDT = COMPUSDT()


@dataclass(slots=True, frozen=True)
class COSBNB:
    name: str = "COSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "COSBNB"

    def __str__(self):
        return "COSBNB"

    def __call__(self):
        return "COSBNB"


COSBNB = COSBNB()


@dataclass(slots=True, frozen=True)
class COSBTC:
    name: str = "COSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "COSBTC"

    def __str__(self):
        return "COSBTC"

    def __call__(self):
        return "COSBTC"


COSBTC = COSBTC()


@dataclass(slots=True, frozen=True)
class COSBUSD:
    name: str = "COSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "COSBUSD"

    def __str__(self):
        return "COSBUSD"

    def __call__(self):
        return "COSBUSD"


COSBUSD = COSBUSD()


@dataclass(slots=True, frozen=True)
class COSTRY:
    name: str = "COSTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "COSTRY"

    def __str__(self):
        return "COSTRY"

    def __call__(self):
        return "COSTRY"


COSTRY = COSTRY()


@dataclass(slots=True, frozen=True)
class COSUSDT:
    name: str = "COSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 18443055.00000000
    margin: bool = True

    def __repr__(self):
        return "COSUSDT"

    def __str__(self):
        return "COSUSDT"

    def __call__(self):
        return "COSUSDT"


COSUSDT = COSUSDT()


@dataclass(slots=True, frozen=True)
class COTIBNB:
    name: str = "COTIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "COTIBNB"

    def __str__(self):
        return "COTIBNB"

    def __call__(self):
        return "COTIBNB"


COTIBNB = COTIBNB()


@dataclass(slots=True, frozen=True)
class COTIBTC:
    name: str = "COTIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "COTIBTC"

    def __str__(self):
        return "COTIBTC"

    def __call__(self):
        return "COTIBTC"


COTIBTC = COTIBTC()


@dataclass(slots=True, frozen=True)
class COTIBUSD:
    name: str = "COTIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "COTIBUSD"

    def __str__(self):
        return "COTIBUSD"

    def __call__(self):
        return "COTIBUSD"


COTIBUSD = COTIBUSD()


@dataclass(slots=True, frozen=True)
class COTIUSDT:
    name: str = "COTIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "COTIUSDT"

    def __str__(self):
        return "COTIUSDT"

    def __call__(self):
        return "COTIUSDT"


COTIUSDT = COTIUSDT()


@dataclass(slots=True, frozen=True)
class COVERBUSD:
    name: str = "COVERBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "COVERBUSD"

    def __str__(self):
        return "COVERBUSD"

    def __call__(self):
        return "COVERBUSD"


COVERBUSD = COVERBUSD()


@dataclass(slots=True, frozen=True)
class COVERETH:
    name: str = "COVERETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "COVERETH"

    def __str__(self):
        return "COVERETH"

    def __call__(self):
        return "COVERETH"


COVERETH = COVERETH()


@dataclass(slots=True, frozen=True)
class CREAMBNB:
    name: str = "CREAMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "CREAMBNB"

    def __str__(self):
        return "CREAMBNB"

    def __call__(self):
        return "CREAMBNB"


CREAMBNB = CREAMBNB()


@dataclass(slots=True, frozen=True)
class CREAMBUSD:
    name: str = "CREAMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "CREAMBUSD"

    def __str__(self):
        return "CREAMBUSD"

    def __call__(self):
        return "CREAMBUSD"


CREAMBUSD = CREAMBUSD()


@dataclass(slots=True, frozen=True)
class CRVBNB:
    name: str = "CRVBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CRVBNB"

    def __str__(self):
        return "CRVBNB"

    def __call__(self):
        return "CRVBNB"


CRVBNB = CRVBNB()


@dataclass(slots=True, frozen=True)
class CRVBTC:
    name: str = "CRVBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CRVBTC"

    def __str__(self):
        return "CRVBTC"

    def __call__(self):
        return "CRVBTC"


CRVBTC = CRVBTC()


@dataclass(slots=True, frozen=True)
class CRVBUSD:
    name: str = "CRVBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "CRVBUSD"

    def __str__(self):
        return "CRVBUSD"

    def __call__(self):
        return "CRVBUSD"


CRVBUSD = CRVBUSD()


@dataclass(slots=True, frozen=True)
class CRVETH:
    name: str = "CRVETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CRVETH"

    def __str__(self):
        return "CRVETH"

    def __call__(self):
        return "CRVETH"


CRVETH = CRVETH()


@dataclass(slots=True, frozen=True)
class CRVUSDT:
    name: str = "CRVUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "CRVUSDT"

    def __str__(self):
        return "CRVUSDT"

    def __call__(self):
        return "CRVUSDT"


CRVUSDT = CRVUSDT()


@dataclass(slots=True, frozen=True)
class CTKBNB:
    name: str = "CTKBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CTKBNB"

    def __str__(self):
        return "CTKBNB"

    def __call__(self):
        return "CTKBNB"


CTKBNB = CTKBNB()


@dataclass(slots=True, frozen=True)
class CTKBTC:
    name: str = "CTKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CTKBTC"

    def __str__(self):
        return "CTKBTC"

    def __call__(self):
        return "CTKBTC"


CTKBTC = CTKBTC()


@dataclass(slots=True, frozen=True)
class CTKBUSD:
    name: str = "CTKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "CTKBUSD"

    def __str__(self):
        return "CTKBUSD"

    def __call__(self):
        return "CTKBUSD"


CTKBUSD = CTKBUSD()


@dataclass(slots=True, frozen=True)
class CTKUSDT:
    name: str = "CTKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "CTKUSDT"

    def __str__(self):
        return "CTKUSDT"

    def __call__(self):
        return "CTKUSDT"


CTKUSDT = CTKUSDT()


@dataclass(slots=True, frozen=True)
class CTSIBNB:
    name: str = "CTSIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CTSIBNB"

    def __str__(self):
        return "CTSIBNB"

    def __call__(self):
        return "CTSIBNB"


CTSIBNB = CTSIBNB()


@dataclass(slots=True, frozen=True)
class CTSIBTC:
    name: str = "CTSIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CTSIBTC"

    def __str__(self):
        return "CTSIBTC"

    def __call__(self):
        return "CTSIBTC"


CTSIBTC = CTSIBTC()


@dataclass(slots=True, frozen=True)
class CTSIBUSD:
    name: str = "CTSIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CTSIBUSD"

    def __str__(self):
        return "CTSIBUSD"

    def __call__(self):
        return "CTSIBUSD"


CTSIBUSD = CTSIBUSD()


@dataclass(slots=True, frozen=True)
class CTSIUSDT:
    name: str = "CTSIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CTSIUSDT"

    def __str__(self):
        return "CTSIUSDT"

    def __call__(self):
        return "CTSIUSDT"


CTSIUSDT = CTSIUSDT()


@dataclass(slots=True, frozen=True)
class CTXCBNB:
    name: str = "CTXCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CTXCBNB"

    def __str__(self):
        return "CTXCBNB"

    def __call__(self):
        return "CTXCBNB"


CTXCBNB = CTXCBNB()


@dataclass(slots=True, frozen=True)
class CTXCBTC:
    name: str = "CTXCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "CTXCBTC"

    def __str__(self):
        return "CTXCBTC"

    def __call__(self):
        return "CTXCBTC"


CTXCBTC = CTXCBTC()


@dataclass(slots=True, frozen=True)
class CTXCBUSD:
    name: str = "CTXCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "CTXCBUSD"

    def __str__(self):
        return "CTXCBUSD"

    def __call__(self):
        return "CTXCBUSD"


CTXCBUSD = CTXCBUSD()


@dataclass(slots=True, frozen=True)
class CTXCUSDT:
    name: str = "CTXCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "CTXCUSDT"

    def __str__(self):
        return "CTXCUSDT"

    def __call__(self):
        return "CTXCUSDT"


CTXCUSDT = CTXCUSDT()


@dataclass(slots=True, frozen=True)
class CVCBNB:
    name: str = "CVCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CVCBNB"

    def __str__(self):
        return "CVCBNB"

    def __call__(self):
        return "CVCBNB"


CVCBNB = CVCBNB()


@dataclass(slots=True, frozen=True)
class CVCBTC:
    name: str = "CVCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CVCBTC"

    def __str__(self):
        return "CVCBTC"

    def __call__(self):
        return "CVCBTC"


CVCBTC = CVCBTC()


@dataclass(slots=True, frozen=True)
class CVCBUSD:
    name: str = "CVCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CVCBUSD"

    def __str__(self):
        return "CVCBUSD"

    def __call__(self):
        return "CVCBUSD"


CVCBUSD = CVCBUSD()


@dataclass(slots=True, frozen=True)
class CVCETH:
    name: str = "CVCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CVCETH"

    def __str__(self):
        return "CVCETH"

    def __call__(self):
        return "CVCETH"


CVCETH = CVCETH()


@dataclass(slots=True, frozen=True)
class CVCUSDT:
    name: str = "CVCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "CVCUSDT"

    def __str__(self):
        return "CVCUSDT"

    def __call__(self):
        return "CVCUSDT"


CVCUSDT = CVCUSDT()


@dataclass(slots=True, frozen=True)
class CVPBUSD:
    name: str = "CVPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "CVPBUSD"

    def __str__(self):
        return "CVPBUSD"

    def __call__(self):
        return "CVPBUSD"


CVPBUSD = CVPBUSD()


@dataclass(slots=True, frozen=True)
class CVPETH:
    name: str = "CVPETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CVPETH"

    def __str__(self):
        return "CVPETH"

    def __call__(self):
        return "CVPETH"


CVPETH = CVPETH()


@dataclass(slots=True, frozen=True)
class CVPUSDT:
    name: str = "CVPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CVPUSDT"

    def __str__(self):
        return "CVPUSDT"

    def __call__(self):
        return "CVPUSDT"


CVPUSDT = CVPUSDT()


@dataclass(slots=True, frozen=True)
class CVXBTC:
    name: str = "CVXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "CVXBTC"

    def __str__(self):
        return "CVXBTC"

    def __call__(self):
        return "CVXBTC"


CVXBTC = CVXBTC()


@dataclass(slots=True, frozen=True)
class CVXBUSD:
    name: str = "CVXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CVXBUSD"

    def __str__(self):
        return "CVXBUSD"

    def __call__(self):
        return "CVXBUSD"


CVXBUSD = CVXBUSD()


@dataclass(slots=True, frozen=True)
class CVXUSDT:
    name: str = "CVXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "CVXUSDT"

    def __str__(self):
        return "CVXUSDT"

    def __call__(self):
        return "CVXUSDT"


CVXUSDT = CVXUSDT()


@dataclass(slots=True, frozen=True)
class DAIBNB:
    name: str = "DAIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DAIBNB"

    def __str__(self):
        return "DAIBNB"

    def __call__(self):
        return "DAIBNB"


DAIBNB = DAIBNB()


@dataclass(slots=True, frozen=True)
class DAIBTC:
    name: str = "DAIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DAIBTC"

    def __str__(self):
        return "DAIBTC"

    def __call__(self):
        return "DAIBTC"


DAIBTC = DAIBTC()


@dataclass(slots=True, frozen=True)
class DAIBUSD:
    name: str = "DAIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "DAIBUSD"

    def __str__(self):
        return "DAIBUSD"

    def __call__(self):
        return "DAIBUSD"


DAIBUSD = DAIBUSD()


@dataclass(slots=True, frozen=True)
class DAIUSDT:
    name: str = "DAIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "DAIUSDT"

    def __str__(self):
        return "DAIUSDT"

    def __call__(self):
        return "DAIUSDT"


DAIUSDT = DAIUSDT()


@dataclass(slots=True, frozen=True)
class DARBNB:
    name: str = "DARBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DARBNB"

    def __str__(self):
        return "DARBNB"

    def __call__(self):
        return "DARBNB"


DARBNB = DARBNB()


@dataclass(slots=True, frozen=True)
class DARBTC:
    name: str = "DARBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "DARBTC"

    def __str__(self):
        return "DARBTC"

    def __call__(self):
        return "DARBTC"


DARBTC = DARBTC()


@dataclass(slots=True, frozen=True)
class DARBUSD:
    name: str = "DARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "DARBUSD"

    def __str__(self):
        return "DARBUSD"

    def __call__(self):
        return "DARBUSD"


DARBUSD = DARBUSD()


@dataclass(slots=True, frozen=True)
class DARETH:
    name: str = "DARETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DARETH"

    def __str__(self):
        return "DARETH"

    def __call__(self):
        return "DARETH"


DARETH = DARETH()


@dataclass(slots=True, frozen=True)
class DAREUR:
    name: str = "DAREUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DAREUR"

    def __str__(self):
        return "DAREUR"

    def __call__(self):
        return "DAREUR"


DAREUR = DAREUR()


@dataclass(slots=True, frozen=True)
class DARTRY:
    name: str = "DARTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "DARTRY"

    def __str__(self):
        return "DARTRY"

    def __call__(self):
        return "DARTRY"


DARTRY = DARTRY()


@dataclass(slots=True, frozen=True)
class DARUSDT:
    name: str = "DARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "DARUSDT"

    def __str__(self):
        return "DARUSDT"

    def __call__(self):
        return "DARUSDT"


DARUSDT = DARUSDT()


@dataclass(slots=True, frozen=True)
class DASHBNB:
    name: str = "DASHBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "DASHBNB"

    def __str__(self):
        return "DASHBNB"

    def __call__(self):
        return "DASHBNB"


DASHBNB = DASHBNB()


@dataclass(slots=True, frozen=True)
class DASHBTC:
    name: str = "DASHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DASHBTC"

    def __str__(self):
        return "DASHBTC"

    def __call__(self):
        return "DASHBTC"


DASHBTC = DASHBTC()


@dataclass(slots=True, frozen=True)
class DASHBUSD:
    name: str = "DASHBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "DASHBUSD"

    def __str__(self):
        return "DASHBUSD"

    def __call__(self):
        return "DASHBUSD"


DASHBUSD = DASHBUSD()


@dataclass(slots=True, frozen=True)
class DASHETH:
    name: str = "DASHETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DASHETH"

    def __str__(self):
        return "DASHETH"

    def __call__(self):
        return "DASHETH"


DASHETH = DASHETH()


@dataclass(slots=True, frozen=True)
class DASHUSDT:
    name: str = "DASHUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "DASHUSDT"

    def __str__(self):
        return "DASHUSDT"

    def __call__(self):
        return "DASHUSDT"


DASHUSDT = DASHUSDT()


@dataclass(slots=True, frozen=True)
class DATABTC:
    name: str = "DATABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DATABTC"

    def __str__(self):
        return "DATABTC"

    def __call__(self):
        return "DATABTC"


DATABTC = DATABTC()


@dataclass(slots=True, frozen=True)
class DATABUSD:
    name: str = "DATABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DATABUSD"

    def __str__(self):
        return "DATABUSD"

    def __call__(self):
        return "DATABUSD"


DATABUSD = DATABUSD()


@dataclass(slots=True, frozen=True)
class DATAETH:
    name: str = "DATAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DATAETH"

    def __str__(self):
        return "DATAETH"

    def __call__(self):
        return "DATAETH"


DATAETH = DATAETH()


@dataclass(slots=True, frozen=True)
class DATAUSDT:
    name: str = "DATAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DATAUSDT"

    def __str__(self):
        return "DATAUSDT"

    def __call__(self):
        return "DATAUSDT"


DATAUSDT = DATAUSDT()


@dataclass(slots=True, frozen=True)
class DCRBNB:
    name: str = "DCRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "DCRBNB"

    def __str__(self):
        return "DCRBNB"

    def __call__(self):
        return "DCRBNB"


DCRBNB = DCRBNB()


@dataclass(slots=True, frozen=True)
class DCRBTC:
    name: str = "DCRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DCRBTC"

    def __str__(self):
        return "DCRBTC"

    def __call__(self):
        return "DCRBTC"


DCRBTC = DCRBTC()


@dataclass(slots=True, frozen=True)
class DCRBUSD:
    name: str = "DCRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "DCRBUSD"

    def __str__(self):
        return "DCRBUSD"

    def __call__(self):
        return "DCRBUSD"


DCRBUSD = DCRBUSD()


@dataclass(slots=True, frozen=True)
class DCRUSDT:
    name: str = "DCRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "DCRUSDT"

    def __str__(self):
        return "DCRUSDT"

    def __call__(self):
        return "DCRUSDT"


DCRUSDT = DCRUSDT()


@dataclass(slots=True, frozen=True)
class DEGOBTC:
    name: str = "DEGOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DEGOBTC"

    def __str__(self):
        return "DEGOBTC"

    def __call__(self):
        return "DEGOBTC"


DEGOBTC = DEGOBTC()


@dataclass(slots=True, frozen=True)
class DEGOBUSD:
    name: str = "DEGOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "DEGOBUSD"

    def __str__(self):
        return "DEGOBUSD"

    def __call__(self):
        return "DEGOBUSD"


DEGOBUSD = DEGOBUSD()


@dataclass(slots=True, frozen=True)
class DEGOUSDT:
    name: str = "DEGOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "DEGOUSDT"

    def __str__(self):
        return "DEGOUSDT"

    def __call__(self):
        return "DEGOUSDT"


DEGOUSDT = DEGOUSDT()


@dataclass(slots=True, frozen=True)
class DENTBTC:
    name: str = "DENTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DENTBTC"

    def __str__(self):
        return "DENTBTC"

    def __call__(self):
        return "DENTBTC"


DENTBTC = DENTBTC()


@dataclass(slots=True, frozen=True)
class DENTBUSD:
    name: str = "DENTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DENTBUSD"

    def __str__(self):
        return "DENTBUSD"

    def __call__(self):
        return "DENTBUSD"


DENTBUSD = DENTBUSD()


@dataclass(slots=True, frozen=True)
class DENTETH:
    name: str = "DENTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "DENTETH"

    def __str__(self):
        return "DENTETH"

    def __call__(self):
        return "DENTETH"


DENTETH = DENTETH()


@dataclass(slots=True, frozen=True)
class DENTTRY:
    name: str = "DENTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DENTTRY"

    def __str__(self):
        return "DENTTRY"

    def __call__(self):
        return "DENTTRY"


DENTTRY = DENTTRY()


@dataclass(slots=True, frozen=True)
class DENTUSDT:
    name: str = "DENTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DENTUSDT"

    def __str__(self):
        return "DENTUSDT"

    def __call__(self):
        return "DENTUSDT"


DENTUSDT = DENTUSDT()


@dataclass(slots=True, frozen=True)
class DEXEBUSD:
    name: str = "DEXEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "DEXEBUSD"

    def __str__(self):
        return "DEXEBUSD"

    def __call__(self):
        return "DEXEBUSD"


DEXEBUSD = DEXEBUSD()


@dataclass(slots=True, frozen=True)
class DEXEETH:
    name: str = "DEXEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DEXEETH"

    def __str__(self):
        return "DEXEETH"

    def __call__(self):
        return "DEXEETH"


DEXEETH = DEXEETH()


@dataclass(slots=True, frozen=True)
class DEXEUSDT:
    name: str = "DEXEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DEXEUSDT"

    def __str__(self):
        return "DEXEUSDT"

    def __call__(self):
        return "DEXEUSDT"


DEXEUSDT = DEXEUSDT()


@dataclass(slots=True, frozen=True)
class DFBUSD:
    name: str = "DFBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "DFBUSD"

    def __str__(self):
        return "DFBUSD"

    def __call__(self):
        return "DFBUSD"


DFBUSD = DFBUSD()


@dataclass(slots=True, frozen=True)
class DFETH:
    name: str = "DFETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DFETH"

    def __str__(self):
        return "DFETH"

    def __call__(self):
        return "DFETH"


DFETH = DFETH()


@dataclass(slots=True, frozen=True)
class DFUSDT:
    name: str = "DFUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DFUSDT"

    def __str__(self):
        return "DFUSDT"

    def __call__(self):
        return "DFUSDT"


DFUSDT = DFUSDT()


@dataclass(slots=True, frozen=True)
class DGBBTC:
    name: str = "DGBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DGBBTC"

    def __str__(self):
        return "DGBBTC"

    def __call__(self):
        return "DGBBTC"


DGBBTC = DGBBTC()


@dataclass(slots=True, frozen=True)
class DGBBUSD:
    name: str = "DGBBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DGBBUSD"

    def __str__(self):
        return "DGBBUSD"

    def __call__(self):
        return "DGBBUSD"


DGBBUSD = DGBBUSD()


@dataclass(slots=True, frozen=True)
class DGBUSDT:
    name: str = "DGBUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DGBUSDT"

    def __str__(self):
        return "DGBUSDT"

    def __call__(self):
        return "DGBUSDT"


DGBUSDT = DGBUSDT()


@dataclass(slots=True, frozen=True)
class DGDBTC:
    name: str = "DGDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DGDBTC"

    def __str__(self):
        return "DGDBTC"

    def __call__(self):
        return "DGDBTC"


DGDBTC = DGDBTC()


@dataclass(slots=True, frozen=True)
class DGDETH:
    name: str = "DGDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DGDETH"

    def __str__(self):
        return "DGDETH"

    def __call__(self):
        return "DGDETH"


DGDETH = DGDETH()


@dataclass(slots=True, frozen=True)
class DIABNB:
    name: str = "DIABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DIABNB"

    def __str__(self):
        return "DIABNB"

    def __call__(self):
        return "DIABNB"


DIABNB = DIABNB()


@dataclass(slots=True, frozen=True)
class DIABTC:
    name: str = "DIABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DIABTC"

    def __str__(self):
        return "DIABTC"

    def __call__(self):
        return "DIABTC"


DIABTC = DIABTC()


@dataclass(slots=True, frozen=True)
class DIABUSD:
    name: str = "DIABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "DIABUSD"

    def __str__(self):
        return "DIABUSD"

    def __call__(self):
        return "DIABUSD"


DIABUSD = DIABUSD()


@dataclass(slots=True, frozen=True)
class DIAUSDT:
    name: str = "DIAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "DIAUSDT"

    def __str__(self):
        return "DIAUSDT"

    def __call__(self):
        return "DIAUSDT"


DIAUSDT = DIAUSDT()


@dataclass(slots=True, frozen=True)
class DLTBNB:
    name: str = "DLTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DLTBNB"

    def __str__(self):
        return "DLTBNB"

    def __call__(self):
        return "DLTBNB"


DLTBNB = DLTBNB()


@dataclass(slots=True, frozen=True)
class DLTBTC:
    name: str = "DLTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DLTBTC"

    def __str__(self):
        return "DLTBTC"

    def __call__(self):
        return "DLTBTC"


DLTBTC = DLTBTC()


@dataclass(slots=True, frozen=True)
class DLTETH:
    name: str = "DLTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DLTETH"

    def __str__(self):
        return "DLTETH"

    def __call__(self):
        return "DLTETH"


DLTETH = DLTETH()


@dataclass(slots=True, frozen=True)
class DNTBTC:
    name: str = "DNTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DNTBTC"

    def __str__(self):
        return "DNTBTC"

    def __call__(self):
        return "DNTBTC"


DNTBTC = DNTBTC()


@dataclass(slots=True, frozen=True)
class DNTBUSD:
    name: str = "DNTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DNTBUSD"

    def __str__(self):
        return "DNTBUSD"

    def __call__(self):
        return "DNTBUSD"


DNTBUSD = DNTBUSD()


@dataclass(slots=True, frozen=True)
class DNTETH:
    name: str = "DNTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DNTETH"

    def __str__(self):
        return "DNTETH"

    def __call__(self):
        return "DNTETH"


DNTETH = DNTETH()


@dataclass(slots=True, frozen=True)
class DNTUSDT:
    name: str = "DNTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DNTUSDT"

    def __str__(self):
        return "DNTUSDT"

    def __call__(self):
        return "DNTUSDT"


DNTUSDT = DNTUSDT()


@dataclass(slots=True, frozen=True)
class DOCKBTC:
    name: str = "DOCKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DOCKBTC"

    def __str__(self):
        return "DOCKBTC"

    def __call__(self):
        return "DOCKBTC"


DOCKBTC = DOCKBTC()


@dataclass(slots=True, frozen=True)
class DOCKBUSD:
    name: str = "DOCKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "DOCKBUSD"

    def __str__(self):
        return "DOCKBUSD"

    def __call__(self):
        return "DOCKBUSD"


DOCKBUSD = DOCKBUSD()


@dataclass(slots=True, frozen=True)
class DOCKETH:
    name: str = "DOCKETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOCKETH"

    def __str__(self):
        return "DOCKETH"

    def __call__(self):
        return "DOCKETH"


DOCKETH = DOCKETH()


@dataclass(slots=True, frozen=True)
class DOCKUSDT:
    name: str = "DOCKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DOCKUSDT"

    def __str__(self):
        return "DOCKUSDT"

    def __call__(self):
        return "DOCKUSDT"


DOCKUSDT = DOCKUSDT()


@dataclass(slots=True, frozen=True)
class DODOBTC:
    name: str = "DODOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DODOBTC"

    def __str__(self):
        return "DODOBTC"

    def __call__(self):
        return "DODOBTC"


DODOBTC = DODOBTC()


@dataclass(slots=True, frozen=True)
class DODOBUSD:
    name: str = "DODOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "DODOBUSD"

    def __str__(self):
        return "DODOBUSD"

    def __call__(self):
        return "DODOBUSD"


DODOBUSD = DODOBUSD()


@dataclass(slots=True, frozen=True)
class DODOUSDT:
    name: str = "DODOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "DODOUSDT"

    def __str__(self):
        return "DODOUSDT"

    def __call__(self):
        return "DODOUSDT"


DODOUSDT = DODOUSDT()


@dataclass(slots=True, frozen=True)
class DOGEAUD:
    name: str = "DOGEAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGEAUD"

    def __str__(self):
        return "DOGEAUD"

    def __call__(self):
        return "DOGEAUD"


DOGEAUD = DOGEAUD()


@dataclass(slots=True, frozen=True)
class DOGEBIDR:
    name: str = "DOGEBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGEBIDR"

    def __str__(self):
        return "DOGEBIDR"

    def __call__(self):
        return "DOGEBIDR"


DOGEBIDR = DOGEBIDR()


@dataclass(slots=True, frozen=True)
class DOGEBNB:
    name: str = "DOGEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGEBNB"

    def __str__(self):
        return "DOGEBNB"

    def __call__(self):
        return "DOGEBNB"


DOGEBNB = DOGEBNB()


@dataclass(slots=True, frozen=True)
class DOGEBRL:
    name: str = "DOGEBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGEBRL"

    def __str__(self):
        return "DOGEBRL"

    def __call__(self):
        return "DOGEBRL"


DOGEBRL = DOGEBRL()


@dataclass(slots=True, frozen=True)
class DOGEBTC:
    name: str = "DOGEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DOGEBTC"

    def __str__(self):
        return "DOGEBTC"

    def __call__(self):
        return "DOGEBTC"


DOGEBTC = DOGEBTC()


@dataclass(slots=True, frozen=True)
class DOGEBUSD:
    name: str = "DOGEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DOGEBUSD"

    def __str__(self):
        return "DOGEBUSD"

    def __call__(self):
        return "DOGEBUSD"


DOGEBUSD = DOGEBUSD()


@dataclass(slots=True, frozen=True)
class DOGEEUR:
    name: str = "DOGEEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGEEUR"

    def __str__(self):
        return "DOGEEUR"

    def __call__(self):
        return "DOGEEUR"


DOGEEUR = DOGEEUR()


@dataclass(slots=True, frozen=True)
class DOGEGBP:
    name: str = "DOGEGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGEGBP"

    def __str__(self):
        return "DOGEGBP"

    def __call__(self):
        return "DOGEGBP"


DOGEGBP = DOGEGBP()


@dataclass(slots=True, frozen=True)
class DOGEPAX:
    name: str = "DOGEPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGEPAX"

    def __str__(self):
        return "DOGEPAX"

    def __call__(self):
        return "DOGEPAX"


DOGEPAX = DOGEPAX()


@dataclass(slots=True, frozen=True)
class DOGERUB:
    name: str = "DOGERUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGERUB"

    def __str__(self):
        return "DOGERUB"

    def __call__(self):
        return "DOGERUB"


DOGERUB = DOGERUB()


@dataclass(slots=True, frozen=True)
class DOGETRY:
    name: str = "DOGETRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGETRY"

    def __str__(self):
        return "DOGETRY"

    def __call__(self):
        return "DOGETRY"


DOGETRY = DOGETRY()


@dataclass(slots=True, frozen=True)
class DOGEUSDC:
    name: str = "DOGEUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOGEUSDC"

    def __str__(self):
        return "DOGEUSDC"

    def __call__(self):
        return "DOGEUSDC"


DOGEUSDC = DOGEUSDC()


@dataclass(slots=True, frozen=True)
class DOGEUSDT:
    name: str = "DOGEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DOGEUSDT"

    def __str__(self):
        return "DOGEUSDT"

    def __call__(self):
        return "DOGEUSDT"


DOGEUSDT = DOGEUSDT()


@dataclass(slots=True, frozen=True)
class DOTAUD:
    name: str = "DOTAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTAUD"

    def __str__(self):
        return "DOTAUD"

    def __call__(self):
        return "DOTAUD"


DOTAUD = DOTAUD()


@dataclass(slots=True, frozen=True)
class DOTBIDR:
    name: str = "DOTBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTBIDR"

    def __str__(self):
        return "DOTBIDR"

    def __call__(self):
        return "DOTBIDR"


DOTBIDR = DOTBIDR()


@dataclass(slots=True, frozen=True)
class DOTBKRW:
    name: str = "DOTBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9200.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTBKRW"

    def __str__(self):
        return "DOTBKRW"

    def __call__(self):
        return "DOTBKRW"


DOTBKRW = DOTBKRW()


@dataclass(slots=True, frozen=True)
class DOTBNB:
    name: str = "DOTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTBNB"

    def __str__(self):
        return "DOTBNB"

    def __call__(self):
        return "DOTBNB"


DOTBNB = DOTBNB()


@dataclass(slots=True, frozen=True)
class DOTBRL:
    name: str = "DOTBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTBRL"

    def __str__(self):
        return "DOTBRL"

    def __call__(self):
        return "DOTBRL"


DOTBRL = DOTBRL()


@dataclass(slots=True, frozen=True)
class DOTBTC:
    name: str = "DOTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DOTBTC"

    def __str__(self):
        return "DOTBTC"

    def __call__(self):
        return "DOTBTC"


DOTBTC = DOTBTC()


@dataclass(slots=True, frozen=True)
class DOTBUSD:
    name: str = "DOTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "DOTBUSD"

    def __str__(self):
        return "DOTBUSD"

    def __call__(self):
        return "DOTBUSD"


DOTBUSD = DOTBUSD()


@dataclass(slots=True, frozen=True)
class DOTDOWNUSDT:
    name: str = "DOTDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTDOWNUSDT"

    def __str__(self):
        return "DOTDOWNUSDT"

    def __call__(self):
        return "DOTDOWNUSDT"


DOTDOWNUSDT = DOTDOWNUSDT()


@dataclass(slots=True, frozen=True)
class DOTETH:
    name: str = "DOTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTETH"

    def __str__(self):
        return "DOTETH"

    def __call__(self):
        return "DOTETH"


DOTETH = DOTETH()


@dataclass(slots=True, frozen=True)
class DOTEUR:
    name: str = "DOTEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTEUR"

    def __str__(self):
        return "DOTEUR"

    def __call__(self):
        return "DOTEUR"


DOTEUR = DOTEUR()


@dataclass(slots=True, frozen=True)
class DOTGBP:
    name: str = "DOTGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTGBP"

    def __str__(self):
        return "DOTGBP"

    def __call__(self):
        return "DOTGBP"


DOTGBP = DOTGBP()


@dataclass(slots=True, frozen=True)
class DOTNGN:
    name: str = "DOTNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 92232.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTNGN"

    def __str__(self):
        return "DOTNGN"

    def __call__(self):
        return "DOTNGN"


DOTNGN = DOTNGN()


@dataclass(slots=True, frozen=True)
class DOTRUB:
    name: str = "DOTRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTRUB"

    def __str__(self):
        return "DOTRUB"

    def __call__(self):
        return "DOTRUB"


DOTRUB = DOTRUB()


@dataclass(slots=True, frozen=True)
class DOTTRY:
    name: str = "DOTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTTRY"

    def __str__(self):
        return "DOTTRY"

    def __call__(self):
        return "DOTTRY"


DOTTRY = DOTTRY()


@dataclass(slots=True, frozen=True)
class DOTUPUSDT:
    name: str = "DOTUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "DOTUPUSDT"

    def __str__(self):
        return "DOTUPUSDT"

    def __call__(self):
        return "DOTUPUSDT"


DOTUPUSDT = DOTUPUSDT()


@dataclass(slots=True, frozen=True)
class DOTUSDT:
    name: str = "DOTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "DOTUSDT"

    def __str__(self):
        return "DOTUSDT"

    def __call__(self):
        return "DOTUSDT"


DOTUSDT = DOTUSDT()


@dataclass(slots=True, frozen=True)
class DREPBNB:
    name: str = "DREPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DREPBNB"

    def __str__(self):
        return "DREPBNB"

    def __call__(self):
        return "DREPBNB"


DREPBNB = DREPBNB()


@dataclass(slots=True, frozen=True)
class DREPBTC:
    name: str = "DREPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DREPBTC"

    def __str__(self):
        return "DREPBTC"

    def __call__(self):
        return "DREPBTC"


DREPBTC = DREPBTC()


@dataclass(slots=True, frozen=True)
class DREPBUSD:
    name: str = "DREPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DREPBUSD"

    def __str__(self):
        return "DREPBUSD"

    def __call__(self):
        return "DREPBUSD"


DREPBUSD = DREPBUSD()


@dataclass(slots=True, frozen=True)
class DREPUSDT:
    name: str = "DREPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DREPUSDT"

    def __str__(self):
        return "DREPUSDT"

    def __call__(self):
        return "DREPUSDT"


DREPUSDT = DREPUSDT()


@dataclass(slots=True, frozen=True)
class DUSKBNB:
    name: str = "DUSKBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "DUSKBNB"

    def __str__(self):
        return "DUSKBNB"

    def __call__(self):
        return "DUSKBNB"


DUSKBNB = DUSKBNB()


@dataclass(slots=True, frozen=True)
class DUSKBTC:
    name: str = "DUSKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "DUSKBTC"

    def __str__(self):
        return "DUSKBTC"

    def __call__(self):
        return "DUSKBTC"


DUSKBTC = DUSKBTC()


@dataclass(slots=True, frozen=True)
class DUSKBUSD:
    name: str = "DUSKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DUSKBUSD"

    def __str__(self):
        return "DUSKBUSD"

    def __call__(self):
        return "DUSKBUSD"


DUSKBUSD = DUSKBUSD()


@dataclass(slots=True, frozen=True)
class DUSKPAX:
    name: str = "DUSKPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "DUSKPAX"

    def __str__(self):
        return "DUSKPAX"

    def __call__(self):
        return "DUSKPAX"


DUSKPAX = DUSKPAX()


@dataclass(slots=True, frozen=True)
class DUSKUSDC:
    name: str = "DUSKUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "DUSKUSDC"

    def __str__(self):
        return "DUSKUSDC"

    def __call__(self):
        return "DUSKUSDC"


DUSKUSDC = DUSKUSDC()


@dataclass(slots=True, frozen=True)
class DUSKUSDT:
    name: str = "DUSKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "DUSKUSDT"

    def __str__(self):
        return "DUSKUSDT"

    def __call__(self):
        return "DUSKUSDT"


DUSKUSDT = DUSKUSDT()


@dataclass(slots=True, frozen=True)
class DYDXBNB:
    name: str = "DYDXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 8384883677.00000000
    margin: bool = False

    def __repr__(self):
        return "DYDXBNB"

    def __str__(self):
        return "DYDXBNB"

    def __call__(self):
        return "DYDXBNB"


DYDXBNB = DYDXBNB()


@dataclass(slots=True, frozen=True)
class DYDXBTC:
    name: str = "DYDXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 46116860414.00000000
    margin: bool = False

    def __repr__(self):
        return "DYDXBTC"

    def __str__(self):
        return "DYDXBTC"

    def __call__(self):
        return "DYDXBTC"


DYDXBTC = DYDXBTC()


@dataclass(slots=True, frozen=True)
class DYDXBUSD:
    name: str = "DYDXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "DYDXBUSD"

    def __str__(self):
        return "DYDXBUSD"

    def __call__(self):
        return "DYDXBUSD"


DYDXBUSD = DYDXBUSD()


@dataclass(slots=True, frozen=True)
class DYDXETH:
    name: str = "DYDXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "DYDXETH"

    def __str__(self):
        return "DYDXETH"

    def __call__(self):
        return "DYDXETH"


DYDXETH = DYDXETH()


@dataclass(slots=True, frozen=True)
class DYDXUSDT:
    name: str = "DYDXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "DYDXUSDT"

    def __str__(self):
        return "DYDXUSDT"

    def __call__(self):
        return "DYDXUSDT"


DYDXUSDT = DYDXUSDT()


@dataclass(slots=True, frozen=True)
class EASYBTC:
    name: str = "EASYBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EASYBTC"

    def __str__(self):
        return "EASYBTC"

    def __call__(self):
        return "EASYBTC"


EASYBTC = EASYBTC()


@dataclass(slots=True, frozen=True)
class EASYETH:
    name: str = "EASYETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EASYETH"

    def __str__(self):
        return "EASYETH"

    def __call__(self):
        return "EASYETH"


EASYETH = EASYETH()


@dataclass(slots=True, frozen=True)
class EDOBTC:
    name: str = "EDOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EDOBTC"

    def __str__(self):
        return "EDOBTC"

    def __call__(self):
        return "EDOBTC"


EDOBTC = EDOBTC()


@dataclass(slots=True, frozen=True)
class EDOETH:
    name: str = "EDOETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EDOETH"

    def __str__(self):
        return "EDOETH"

    def __call__(self):
        return "EDOETH"


EDOETH = EDOETH()


@dataclass(slots=True, frozen=True)
class EGLDBNB:
    name: str = "EGLDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "EGLDBNB"

    def __str__(self):
        return "EGLDBNB"

    def __call__(self):
        return "EGLDBNB"


EGLDBNB = EGLDBNB()


@dataclass(slots=True, frozen=True)
class EGLDBTC:
    name: str = "EGLDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "EGLDBTC"

    def __str__(self):
        return "EGLDBTC"

    def __call__(self):
        return "EGLDBTC"


EGLDBTC = EGLDBTC()


@dataclass(slots=True, frozen=True)
class EGLDBUSD:
    name: str = "EGLDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "EGLDBUSD"

    def __str__(self):
        return "EGLDBUSD"

    def __call__(self):
        return "EGLDBUSD"


EGLDBUSD = EGLDBUSD()


@dataclass(slots=True, frozen=True)
class EGLDETH:
    name: str = "EGLDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "EGLDETH"

    def __str__(self):
        return "EGLDETH"

    def __call__(self):
        return "EGLDETH"


EGLDETH = EGLDETH()


@dataclass(slots=True, frozen=True)
class EGLDEUR:
    name: str = "EGLDEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "EGLDEUR"

    def __str__(self):
        return "EGLDEUR"

    def __call__(self):
        return "EGLDEUR"


EGLDEUR = EGLDEUR()


@dataclass(slots=True, frozen=True)
class EGLDUSDT:
    name: str = "EGLDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "EGLDUSDT"

    def __str__(self):
        return "EGLDUSDT"

    def __call__(self):
        return "EGLDUSDT"


EGLDUSDT = EGLDUSDT()


@dataclass(slots=True, frozen=True)
class ELFBTC:
    name: str = "ELFBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ELFBTC"

    def __str__(self):
        return "ELFBTC"

    def __call__(self):
        return "ELFBTC"


ELFBTC = ELFBTC()


@dataclass(slots=True, frozen=True)
class ELFBUSD:
    name: str = "ELFBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "ELFBUSD"

    def __str__(self):
        return "ELFBUSD"

    def __call__(self):
        return "ELFBUSD"


ELFBUSD = ELFBUSD()


@dataclass(slots=True, frozen=True)
class ELFETH:
    name: str = "ELFETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ELFETH"

    def __str__(self):
        return "ELFETH"

    def __call__(self):
        return "ELFETH"


ELFETH = ELFETH()


@dataclass(slots=True, frozen=True)
class ELFUSDT:
    name: str = "ELFUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ELFUSDT"

    def __str__(self):
        return "ELFUSDT"

    def __call__(self):
        return "ELFUSDT"


ELFUSDT = ELFUSDT()


@dataclass(slots=True, frozen=True)
class ENGBTC:
    name: str = "ENGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ENGBTC"

    def __str__(self):
        return "ENGBTC"

    def __call__(self):
        return "ENGBTC"


ENGBTC = ENGBTC()


@dataclass(slots=True, frozen=True)
class ENGETH:
    name: str = "ENGETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ENGETH"

    def __str__(self):
        return "ENGETH"

    def __call__(self):
        return "ENGETH"


ENGETH = ENGETH()


@dataclass(slots=True, frozen=True)
class ENJBNB:
    name: str = "ENJBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ENJBNB"

    def __str__(self):
        return "ENJBNB"

    def __call__(self):
        return "ENJBNB"


ENJBNB = ENJBNB()


@dataclass(slots=True, frozen=True)
class ENJBRL:
    name: str = "ENJBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ENJBRL"

    def __str__(self):
        return "ENJBRL"

    def __call__(self):
        return "ENJBRL"


ENJBRL = ENJBRL()


@dataclass(slots=True, frozen=True)
class ENJBTC:
    name: str = "ENJBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ENJBTC"

    def __str__(self):
        return "ENJBTC"

    def __call__(self):
        return "ENJBTC"


ENJBTC = ENJBTC()


@dataclass(slots=True, frozen=True)
class ENJBUSD:
    name: str = "ENJBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ENJBUSD"

    def __str__(self):
        return "ENJBUSD"

    def __call__(self):
        return "ENJBUSD"


ENJBUSD = ENJBUSD()


@dataclass(slots=True, frozen=True)
class ENJETH:
    name: str = "ENJETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ENJETH"

    def __str__(self):
        return "ENJETH"

    def __call__(self):
        return "ENJETH"


ENJETH = ENJETH()


@dataclass(slots=True, frozen=True)
class ENJEUR:
    name: str = "ENJEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ENJEUR"

    def __str__(self):
        return "ENJEUR"

    def __call__(self):
        return "ENJEUR"


ENJEUR = ENJEUR()


@dataclass(slots=True, frozen=True)
class ENJGBP:
    name: str = "ENJGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ENJGBP"

    def __str__(self):
        return "ENJGBP"

    def __call__(self):
        return "ENJGBP"


ENJGBP = ENJGBP()


@dataclass(slots=True, frozen=True)
class ENJTRY:
    name: str = "ENJTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ENJTRY"

    def __str__(self):
        return "ENJTRY"

    def __call__(self):
        return "ENJTRY"


ENJTRY = ENJTRY()


@dataclass(slots=True, frozen=True)
class ENJUSDT:
    name: str = "ENJUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ENJUSDT"

    def __str__(self):
        return "ENJUSDT"

    def __call__(self):
        return "ENJUSDT"


ENJUSDT = ENJUSDT()


@dataclass(slots=True, frozen=True)
class ENSBNB:
    name: str = "ENSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ENSBNB"

    def __str__(self):
        return "ENSBNB"

    def __call__(self):
        return "ENSBNB"


ENSBNB = ENSBNB()


@dataclass(slots=True, frozen=True)
class ENSBTC:
    name: str = "ENSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "ENSBTC"

    def __str__(self):
        return "ENSBTC"

    def __call__(self):
        return "ENSBTC"


ENSBTC = ENSBTC()


@dataclass(slots=True, frozen=True)
class ENSBUSD:
    name: str = "ENSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "ENSBUSD"

    def __str__(self):
        return "ENSBUSD"

    def __call__(self):
        return "ENSBUSD"


ENSBUSD = ENSBUSD()


@dataclass(slots=True, frozen=True)
class ENSTRY:
    name: str = "ENSTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ENSTRY"

    def __str__(self):
        return "ENSTRY"

    def __call__(self):
        return "ENSTRY"


ENSTRY = ENSTRY()


@dataclass(slots=True, frozen=True)
class ENSUSDT:
    name: str = "ENSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "ENSUSDT"

    def __str__(self):
        return "ENSUSDT"

    def __call__(self):
        return "ENSUSDT"


ENSUSDT = ENSUSDT()


@dataclass(slots=True, frozen=True)
class EOSAUD:
    name: str = "EOSAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSAUD"

    def __str__(self):
        return "EOSAUD"

    def __call__(self):
        return "EOSAUD"


EOSAUD = EOSAUD()


@dataclass(slots=True, frozen=True)
class EOSBEARBUSD:
    name: str = "EOSBEARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSBEARBUSD"

    def __str__(self):
        return "EOSBEARBUSD"

    def __call__(self):
        return "EOSBEARBUSD"


EOSBEARBUSD = EOSBEARBUSD()


@dataclass(slots=True, frozen=True)
class EOSBEARUSDT:
    name: str = "EOSBEARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSBEARUSDT"

    def __str__(self):
        return "EOSBEARUSDT"

    def __call__(self):
        return "EOSBEARUSDT"


EOSBEARUSDT = EOSBEARUSDT()


@dataclass(slots=True, frozen=True)
class EOSBNB:
    name: str = "EOSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSBNB"

    def __str__(self):
        return "EOSBNB"

    def __call__(self):
        return "EOSBNB"


EOSBNB = EOSBNB()


@dataclass(slots=True, frozen=True)
class EOSBTC:
    name: str = "EOSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "EOSBTC"

    def __str__(self):
        return "EOSBTC"

    def __call__(self):
        return "EOSBTC"


EOSBTC = EOSBTC()


@dataclass(slots=True, frozen=True)
class EOSBULLBUSD:
    name: str = "EOSBULLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSBULLBUSD"

    def __str__(self):
        return "EOSBULLBUSD"

    def __call__(self):
        return "EOSBULLBUSD"


EOSBULLBUSD = EOSBULLBUSD()


@dataclass(slots=True, frozen=True)
class EOSBULLUSDT:
    name: str = "EOSBULLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 92232.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSBULLUSDT"

    def __str__(self):
        return "EOSBULLUSDT"

    def __call__(self):
        return "EOSBULLUSDT"


EOSBULLUSDT = EOSBULLUSDT()


@dataclass(slots=True, frozen=True)
class EOSBUSD:
    name: str = "EOSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "EOSBUSD"

    def __str__(self):
        return "EOSBUSD"

    def __call__(self):
        return "EOSBUSD"


EOSBUSD = EOSBUSD()


@dataclass(slots=True, frozen=True)
class EOSDOWNUSDT:
    name: str = "EOSDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 69980060.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSDOWNUSDT"

    def __str__(self):
        return "EOSDOWNUSDT"

    def __call__(self):
        return "EOSDOWNUSDT"


EOSDOWNUSDT = EOSDOWNUSDT()


@dataclass(slots=True, frozen=True)
class EOSETH:
    name: str = "EOSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "EOSETH"

    def __str__(self):
        return "EOSETH"

    def __call__(self):
        return "EOSETH"


EOSETH = EOSETH()


@dataclass(slots=True, frozen=True)
class EOSEUR:
    name: str = "EOSEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSEUR"

    def __str__(self):
        return "EOSEUR"

    def __call__(self):
        return "EOSEUR"


EOSEUR = EOSEUR()


@dataclass(slots=True, frozen=True)
class EOSPAX:
    name: str = "EOSPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSPAX"

    def __str__(self):
        return "EOSPAX"

    def __call__(self):
        return "EOSPAX"


EOSPAX = EOSPAX()


@dataclass(slots=True, frozen=True)
class EOSTRY:
    name: str = "EOSTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSTRY"

    def __str__(self):
        return "EOSTRY"

    def __call__(self):
        return "EOSTRY"


EOSTRY = EOSTRY()


@dataclass(slots=True, frozen=True)
class EOSTUSD:
    name: str = "EOSTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSTUSD"

    def __str__(self):
        return "EOSTUSD"

    def __call__(self):
        return "EOSTUSD"


EOSTUSD = EOSTUSD()


@dataclass(slots=True, frozen=True)
class EOSUPUSDT:
    name: str = "EOSUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSUPUSDT"

    def __str__(self):
        return "EOSUPUSDT"

    def __call__(self):
        return "EOSUPUSDT"


EOSUPUSDT = EOSUPUSDT()


@dataclass(slots=True, frozen=True)
class EOSUSDC:
    name: str = "EOSUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "EOSUSDC"

    def __str__(self):
        return "EOSUSDC"

    def __call__(self):
        return "EOSUSDC"


EOSUSDC = EOSUSDC()


@dataclass(slots=True, frozen=True)
class EOSUSDT:
    name: str = "EOSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "EOSUSDT"

    def __str__(self):
        return "EOSUSDT"

    def __call__(self):
        return "EOSUSDT"


EOSUSDT = EOSUSDT()


@dataclass(slots=True, frozen=True)
class EPSBTC:
    name: str = "EPSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EPSBTC"

    def __str__(self):
        return "EPSBTC"

    def __call__(self):
        return "EPSBTC"


EPSBTC = EPSBTC()


@dataclass(slots=True, frozen=True)
class EPSBUSD:
    name: str = "EPSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "EPSBUSD"

    def __str__(self):
        return "EPSBUSD"

    def __call__(self):
        return "EPSBUSD"


EPSBUSD = EPSBUSD()


@dataclass(slots=True, frozen=True)
class EPSUSDT:
    name: str = "EPSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "EPSUSDT"

    def __str__(self):
        return "EPSUSDT"

    def __call__(self):
        return "EPSUSDT"


EPSUSDT = EPSUSDT()


@dataclass(slots=True, frozen=True)
class EPXBUSD:
    name: str = "EPXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = True

    def __repr__(self):
        return "EPXBUSD"

    def __str__(self):
        return "EPXBUSD"

    def __call__(self):
        return "EPXBUSD"


EPXBUSD = EPXBUSD()


@dataclass(slots=True, frozen=True)
class EPXUSDT:
    name: str = "EPXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = True

    def __repr__(self):
        return "EPXUSDT"

    def __str__(self):
        return "EPXUSDT"

    def __call__(self):
        return "EPXUSDT"


EPXUSDT = EPXUSDT()


@dataclass(slots=True, frozen=True)
class ERDBNB:
    name: str = "ERDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ERDBNB"

    def __str__(self):
        return "ERDBNB"

    def __call__(self):
        return "ERDBNB"


ERDBNB = ERDBNB()


@dataclass(slots=True, frozen=True)
class ERDBTC:
    name: str = "ERDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ERDBTC"

    def __str__(self):
        return "ERDBTC"

    def __call__(self):
        return "ERDBTC"


ERDBTC = ERDBTC()


@dataclass(slots=True, frozen=True)
class ERDBUSD:
    name: str = "ERDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ERDBUSD"

    def __str__(self):
        return "ERDBUSD"

    def __call__(self):
        return "ERDBUSD"


ERDBUSD = ERDBUSD()


@dataclass(slots=True, frozen=True)
class ERDPAX:
    name: str = "ERDPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ERDPAX"

    def __str__(self):
        return "ERDPAX"

    def __call__(self):
        return "ERDPAX"


ERDPAX = ERDPAX()


@dataclass(slots=True, frozen=True)
class ERDUSDC:
    name: str = "ERDUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ERDUSDC"

    def __str__(self):
        return "ERDUSDC"

    def __call__(self):
        return "ERDUSDC"


ERDUSDC = ERDUSDC()


@dataclass(slots=True, frozen=True)
class ERDUSDT:
    name: str = "ERDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ERDUSDT"

    def __str__(self):
        return "ERDUSDT"

    def __call__(self):
        return "ERDUSDT"


ERDUSDT = ERDUSDT()


@dataclass(slots=True, frozen=True)
class ERNBNB:
    name: str = "ERNBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ERNBNB"

    def __str__(self):
        return "ERNBNB"

    def __call__(self):
        return "ERNBNB"


ERNBNB = ERNBNB()


@dataclass(slots=True, frozen=True)
class ERNBUSD:
    name: str = "ERNBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "ERNBUSD"

    def __str__(self):
        return "ERNBUSD"

    def __call__(self):
        return "ERNBUSD"


ERNBUSD = ERNBUSD()


@dataclass(slots=True, frozen=True)
class ERNUSDT:
    name: str = "ERNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "ERNUSDT"

    def __str__(self):
        return "ERNUSDT"

    def __call__(self):
        return "ERNUSDT"


ERNUSDT = ERNUSDT()


@dataclass(slots=True, frozen=True)
class ETCBNB:
    name: str = "ETCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETCBNB"

    def __str__(self):
        return "ETCBNB"

    def __call__(self):
        return "ETCBNB"


ETCBNB = ETCBNB()


@dataclass(slots=True, frozen=True)
class ETCBRL:
    name: str = "ETCBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ETCBRL"

    def __str__(self):
        return "ETCBRL"

    def __call__(self):
        return "ETCBRL"


ETCBRL = ETCBRL()


@dataclass(slots=True, frozen=True)
class ETCBTC:
    name: str = "ETCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ETCBTC"

    def __str__(self):
        return "ETCBTC"

    def __call__(self):
        return "ETCBTC"


ETCBTC = ETCBTC()


@dataclass(slots=True, frozen=True)
class ETCBUSD:
    name: str = "ETCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "ETCBUSD"

    def __str__(self):
        return "ETCBUSD"

    def __call__(self):
        return "ETCBUSD"


ETCBUSD = ETCBUSD()


@dataclass(slots=True, frozen=True)
class ETCETH:
    name: str = "ETCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ETCETH"

    def __str__(self):
        return "ETCETH"

    def __call__(self):
        return "ETCETH"


ETCETH = ETCETH()


@dataclass(slots=True, frozen=True)
class ETCEUR:
    name: str = "ETCEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ETCEUR"

    def __str__(self):
        return "ETCEUR"

    def __call__(self):
        return "ETCEUR"


ETCEUR = ETCEUR()


@dataclass(slots=True, frozen=True)
class ETCGBP:
    name: str = "ETCGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ETCGBP"

    def __str__(self):
        return "ETCGBP"

    def __call__(self):
        return "ETCGBP"


ETCGBP = ETCGBP()


@dataclass(slots=True, frozen=True)
class ETCPAX:
    name: str = "ETCPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETCPAX"

    def __str__(self):
        return "ETCPAX"

    def __call__(self):
        return "ETCPAX"


ETCPAX = ETCPAX()


@dataclass(slots=True, frozen=True)
class ETCTRY:
    name: str = "ETCTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ETCTRY"

    def __str__(self):
        return "ETCTRY"

    def __call__(self):
        return "ETCTRY"


ETCTRY = ETCTRY()


@dataclass(slots=True, frozen=True)
class ETCTUSD:
    name: str = "ETCTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETCTUSD"

    def __str__(self):
        return "ETCTUSD"

    def __call__(self):
        return "ETCTUSD"


ETCTUSD = ETCTUSD()


@dataclass(slots=True, frozen=True)
class ETCUSDC:
    name: str = "ETCUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETCUSDC"

    def __str__(self):
        return "ETCUSDC"

    def __call__(self):
        return "ETCUSDC"


ETCUSDC = ETCUSDC()


@dataclass(slots=True, frozen=True)
class ETCUSDT:
    name: str = "ETCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "ETCUSDT"

    def __str__(self):
        return "ETCUSDT"

    def __call__(self):
        return "ETCUSDT"


ETCUSDT = ETCUSDT()


@dataclass(slots=True, frozen=True)
class ETHAUD:
    name: str = "ETHAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHAUD"

    def __str__(self):
        return "ETHAUD"

    def __call__(self):
        return "ETHAUD"


ETHAUD = ETHAUD()


@dataclass(slots=True, frozen=True)
class ETHBEARBUSD:
    name: str = "ETHBEARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHBEARBUSD"

    def __str__(self):
        return "ETHBEARBUSD"

    def __call__(self):
        return "ETHBEARBUSD"


ETHBEARBUSD = ETHBEARBUSD()


@dataclass(slots=True, frozen=True)
class ETHBEARUSDT:
    name: str = "ETHBEARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHBEARUSDT"

    def __str__(self):
        return "ETHBEARUSDT"

    def __call__(self):
        return "ETHBEARUSDT"


ETHBEARUSDT = ETHBEARUSDT()


@dataclass(slots=True, frozen=True)
class ETHBIDR:
    name: str = "ETHBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHBIDR"

    def __str__(self):
        return "ETHBIDR"

    def __call__(self):
        return "ETHBIDR"


ETHBIDR = ETHBIDR()


@dataclass(slots=True, frozen=True)
class ETHBKRW:
    name: str = "ETHBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 8000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHBKRW"

    def __str__(self):
        return "ETHBKRW"

    def __call__(self):
        return "ETHBKRW"


ETHBKRW = ETHBKRW()


@dataclass(slots=True, frozen=True)
class ETHBRL:
    name: str = "ETHBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 45000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHBRL"

    def __str__(self):
        return "ETHBRL"

    def __call__(self):
        return "ETHBRL"


ETHBRL = ETHBRL()


@dataclass(slots=True, frozen=True)
class ETHBTC:
    name: str = "ETHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 100000.00000000
    margin: bool = True

    def __repr__(self):
        return "ETHBTC"

    def __str__(self):
        return "ETHBTC"

    def __call__(self):
        return "ETHBTC"


ETHBTC = ETHBTC()


@dataclass(slots=True, frozen=True)
class ETHBULLBUSD:
    name: str = "ETHBULLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00000100
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHBULLBUSD"

    def __str__(self):
        return "ETHBULLBUSD"

    def __call__(self):
        return "ETHBULLBUSD"


ETHBULLBUSD = ETHBULLBUSD()


@dataclass(slots=True, frozen=True)
class ETHBULLUSDT:
    name: str = "ETHBULLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00000100
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHBULLUSDT"

    def __str__(self):
        return "ETHBULLUSDT"

    def __call__(self):
        return "ETHBULLUSDT"


ETHBULLUSDT = ETHBULLUSDT()


@dataclass(slots=True, frozen=True)
class ETHBUSD:
    name: str = "ETHBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "ETHBUSD"

    def __str__(self):
        return "ETHBUSD"

    def __call__(self):
        return "ETHBUSD"


ETHBUSD = ETHBUSD()


@dataclass(slots=True, frozen=True)
class ETHDAI:
    name: str = "ETHDAI"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHDAI"

    def __str__(self):
        return "ETHDAI"

    def __call__(self):
        return "ETHDAI"


ETHDAI = ETHDAI()


@dataclass(slots=True, frozen=True)
class ETHDOWNUSDT:
    name: str = "ETHDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHDOWNUSDT"

    def __str__(self):
        return "ETHDOWNUSDT"

    def __call__(self):
        return "ETHDOWNUSDT"


ETHDOWNUSDT = ETHDOWNUSDT()


@dataclass(slots=True, frozen=True)
class ETHEUR:
    name: str = "ETHEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHEUR"

    def __str__(self):
        return "ETHEUR"

    def __call__(self):
        return "ETHEUR"


ETHEUR = ETHEUR()


@dataclass(slots=True, frozen=True)
class ETHGBP:
    name: str = "ETHGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHGBP"

    def __str__(self):
        return "ETHGBP"

    def __call__(self):
        return "ETHGBP"


ETHGBP = ETHGBP()


@dataclass(slots=True, frozen=True)
class ETHNGN:
    name: str = "ETHNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 900.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHNGN"

    def __str__(self):
        return "ETHNGN"

    def __call__(self):
        return "ETHNGN"


ETHNGN = ETHNGN()


@dataclass(slots=True, frozen=True)
class ETHPAX:
    name: str = "ETHPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHPAX"

    def __str__(self):
        return "ETHPAX"

    def __call__(self):
        return "ETHPAX"


ETHPAX = ETHPAX()


@dataclass(slots=True, frozen=True)
class ETHPLN:
    name: str = "ETHPLN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHPLN"

    def __str__(self):
        return "ETHPLN"

    def __call__(self):
        return "ETHPLN"


ETHPLN = ETHPLN()


@dataclass(slots=True, frozen=True)
class ETHRUB:
    name: str = "ETHRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 23055.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHRUB"

    def __str__(self):
        return "ETHRUB"

    def __call__(self):
        return "ETHRUB"


ETHRUB = ETHRUB()


@dataclass(slots=True, frozen=True)
class ETHTRY:
    name: str = "ETHTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 153719.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHTRY"

    def __str__(self):
        return "ETHTRY"

    def __call__(self):
        return "ETHTRY"


ETHTRY = ETHTRY()


@dataclass(slots=True, frozen=True)
class ETHTUSD:
    name: str = "ETHTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHTUSD"

    def __str__(self):
        return "ETHTUSD"

    def __call__(self):
        return "ETHTUSD"


ETHTUSD = ETHTUSD()


@dataclass(slots=True, frozen=True)
class ETHUAH:
    name: str = "ETHUAH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9220.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHUAH"

    def __str__(self):
        return "ETHUAH"

    def __call__(self):
        return "ETHUAH"


ETHUAH = ETHUAH()


@dataclass(slots=True, frozen=True)
class ETHUPUSDT:
    name: str = "ETHUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 3000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHUPUSDT"

    def __str__(self):
        return "ETHUPUSDT"

    def __call__(self):
        return "ETHUPUSDT"


ETHUPUSDT = ETHUPUSDT()


@dataclass(slots=True, frozen=True)
class ETHUSDC:
    name: str = "ETHUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHUSDC"

    def __str__(self):
        return "ETHUSDC"

    def __call__(self):
        return "ETHUSDC"


ETHUSDC = ETHUSDC()


@dataclass(slots=True, frozen=True)
class ETHUSDP:
    name: str = "ETHUSDP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHUSDP"

    def __str__(self):
        return "ETHUSDP"

    def __call__(self):
        return "ETHUSDP"


ETHUSDP = ETHUSDP()


@dataclass(slots=True, frozen=True)
class ETHUSDT:
    name: str = "ETHUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9000.00000000
    margin: bool = True

    def __repr__(self):
        return "ETHUSDT"

    def __str__(self):
        return "ETHUSDT"

    def __call__(self):
        return "ETHUSDT"


ETHUSDT = ETHUSDT()


@dataclass(slots=True, frozen=True)
class ETHUST:
    name: str = "ETHUST"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHUST"

    def __str__(self):
        return "ETHUST"

    def __call__(self):
        return "ETHUST"


ETHUST = ETHUST()


@dataclass(slots=True, frozen=True)
class ETHZAR:
    name: str = "ETHZAR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9223.00000000
    margin: bool = False

    def __repr__(self):
        return "ETHZAR"

    def __str__(self):
        return "ETHZAR"

    def __call__(self):
        return "ETHZAR"


ETHZAR = ETHZAR()


@dataclass(slots=True, frozen=True)
class EURBUSD:
    name: str = "EURBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "EURBUSD"

    def __str__(self):
        return "EURBUSD"

    def __call__(self):
        return "EURBUSD"


EURBUSD = EURBUSD()


@dataclass(slots=True, frozen=True)
class EURUSDT:
    name: str = "EURUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 6000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EURUSDT"

    def __str__(self):
        return "EURUSDT"

    def __call__(self):
        return "EURUSDT"


EURUSDT = EURUSDT()


@dataclass(slots=True, frozen=True)
class EVXBTC:
    name: str = "EVXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EVXBTC"

    def __str__(self):
        return "EVXBTC"

    def __call__(self):
        return "EVXBTC"


EVXBTC = EVXBTC()


@dataclass(slots=True, frozen=True)
class EVXETH:
    name: str = "EVXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EVXETH"

    def __str__(self):
        return "EVXETH"

    def __call__(self):
        return "EVXETH"


EVXETH = EVXETH()


@dataclass(slots=True, frozen=True)
class EZBTC:
    name: str = "EZBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EZBTC"

    def __str__(self):
        return "EZBTC"

    def __call__(self):
        return "EZBTC"


EZBTC = EZBTC()


@dataclass(slots=True, frozen=True)
class EZETH:
    name: str = "EZETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "EZETH"

    def __str__(self):
        return "EZETH"

    def __call__(self):
        return "EZETH"


EZETH = EZETH()


@dataclass(slots=True, frozen=True)
class FARMBNB:
    name: str = "FARMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FARMBNB"

    def __str__(self):
        return "FARMBNB"

    def __call__(self):
        return "FARMBNB"


FARMBNB = FARMBNB()


@dataclass(slots=True, frozen=True)
class FARMBTC:
    name: str = "FARMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FARMBTC"

    def __str__(self):
        return "FARMBTC"

    def __call__(self):
        return "FARMBTC"


FARMBTC = FARMBTC()


@dataclass(slots=True, frozen=True)
class FARMBUSD:
    name: str = "FARMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "FARMBUSD"

    def __str__(self):
        return "FARMBUSD"

    def __call__(self):
        return "FARMBUSD"


FARMBUSD = FARMBUSD()


@dataclass(slots=True, frozen=True)
class FARMETH:
    name: str = "FARMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FARMETH"

    def __str__(self):
        return "FARMETH"

    def __call__(self):
        return "FARMETH"


FARMETH = FARMETH()


@dataclass(slots=True, frozen=True)
class FARMUSDT:
    name: str = "FARMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "FARMUSDT"

    def __str__(self):
        return "FARMUSDT"

    def __call__(self):
        return "FARMUSDT"


FARMUSDT = FARMUSDT()


@dataclass(slots=True, frozen=True)
class FETBNB:
    name: str = "FETBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FETBNB"

    def __str__(self):
        return "FETBNB"

    def __call__(self):
        return "FETBNB"


FETBNB = FETBNB()


@dataclass(slots=True, frozen=True)
class FETBTC:
    name: str = "FETBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FETBTC"

    def __str__(self):
        return "FETBTC"

    def __call__(self):
        return "FETBTC"


FETBTC = FETBTC()


@dataclass(slots=True, frozen=True)
class FETBUSD:
    name: str = "FETBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FETBUSD"

    def __str__(self):
        return "FETBUSD"

    def __call__(self):
        return "FETBUSD"


FETBUSD = FETBUSD()


@dataclass(slots=True, frozen=True)
class FETUSDT:
    name: str = "FETUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FETUSDT"

    def __str__(self):
        return "FETUSDT"

    def __call__(self):
        return "FETUSDT"


FETUSDT = FETUSDT()


@dataclass(slots=True, frozen=True)
class FIDABNB:
    name: str = "FIDABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FIDABNB"

    def __str__(self):
        return "FIDABNB"

    def __call__(self):
        return "FIDABNB"


FIDABNB = FIDABNB()


@dataclass(slots=True, frozen=True)
class FIDABTC:
    name: str = "FIDABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FIDABTC"

    def __str__(self):
        return "FIDABTC"

    def __call__(self):
        return "FIDABTC"


FIDABTC = FIDABTC()


@dataclass(slots=True, frozen=True)
class FIDABUSD:
    name: str = "FIDABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "FIDABUSD"

    def __str__(self):
        return "FIDABUSD"

    def __call__(self):
        return "FIDABUSD"


FIDABUSD = FIDABUSD()


@dataclass(slots=True, frozen=True)
class FIDAUSDT:
    name: str = "FIDAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "FIDAUSDT"

    def __str__(self):
        return "FIDAUSDT"

    def __call__(self):
        return "FIDAUSDT"


FIDAUSDT = FIDAUSDT()


@dataclass(slots=True, frozen=True)
class FILBNB:
    name: str = "FILBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FILBNB"

    def __str__(self):
        return "FILBNB"

    def __call__(self):
        return "FILBNB"


FILBNB = FILBNB()


@dataclass(slots=True, frozen=True)
class FILBTC:
    name: str = "FILBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "FILBTC"

    def __str__(self):
        return "FILBTC"

    def __call__(self):
        return "FILBTC"


FILBTC = FILBTC()


@dataclass(slots=True, frozen=True)
class FILBUSD:
    name: str = "FILBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "FILBUSD"

    def __str__(self):
        return "FILBUSD"

    def __call__(self):
        return "FILBUSD"


FILBUSD = FILBUSD()


@dataclass(slots=True, frozen=True)
class FILDOWNUSDT:
    name: str = "FILDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 19998638.00000000
    margin: bool = False

    def __repr__(self):
        return "FILDOWNUSDT"

    def __str__(self):
        return "FILDOWNUSDT"

    def __call__(self):
        return "FILDOWNUSDT"


FILDOWNUSDT = FILDOWNUSDT()


@dataclass(slots=True, frozen=True)
class FILETH:
    name: str = "FILETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "FILETH"

    def __str__(self):
        return "FILETH"

    def __call__(self):
        return "FILETH"


FILETH = FILETH()


@dataclass(slots=True, frozen=True)
class FILTRY:
    name: str = "FILTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "FILTRY"

    def __str__(self):
        return "FILTRY"

    def __call__(self):
        return "FILTRY"


FILTRY = FILTRY()


@dataclass(slots=True, frozen=True)
class FILUPUSDT:
    name: str = "FILUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "FILUPUSDT"

    def __str__(self):
        return "FILUPUSDT"

    def __call__(self):
        return "FILUPUSDT"


FILUPUSDT = FILUPUSDT()


@dataclass(slots=True, frozen=True)
class FILUSDT:
    name: str = "FILUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "FILUSDT"

    def __str__(self):
        return "FILUSDT"

    def __call__(self):
        return "FILUSDT"


FILUSDT = FILUSDT()


@dataclass(slots=True, frozen=True)
class FIOBNB:
    name: str = "FIOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FIOBNB"

    def __str__(self):
        return "FIOBNB"

    def __call__(self):
        return "FIOBNB"


FIOBNB = FIOBNB()


@dataclass(slots=True, frozen=True)
class FIOBTC:
    name: str = "FIOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FIOBTC"

    def __str__(self):
        return "FIOBTC"

    def __call__(self):
        return "FIOBTC"


FIOBTC = FIOBTC()


@dataclass(slots=True, frozen=True)
class FIOBUSD:
    name: str = "FIOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "FIOBUSD"

    def __str__(self):
        return "FIOBUSD"

    def __call__(self):
        return "FIOBUSD"


FIOBUSD = FIOBUSD()


@dataclass(slots=True, frozen=True)
class FIOUSDT:
    name: str = "FIOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "FIOUSDT"

    def __str__(self):
        return "FIOUSDT"

    def __call__(self):
        return "FIOUSDT"


FIOUSDT = FIOUSDT()


@dataclass(slots=True, frozen=True)
class FIROBTC:
    name: str = "FIROBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FIROBTC"

    def __str__(self):
        return "FIROBTC"

    def __call__(self):
        return "FIROBTC"


FIROBTC = FIROBTC()


@dataclass(slots=True, frozen=True)
class FIROBUSD:
    name: str = "FIROBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "FIROBUSD"

    def __str__(self):
        return "FIROBUSD"

    def __call__(self):
        return "FIROBUSD"


FIROBUSD = FIROBUSD()


@dataclass(slots=True, frozen=True)
class FIROETH:
    name: str = "FIROETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FIROETH"

    def __str__(self):
        return "FIROETH"

    def __call__(self):
        return "FIROETH"


FIROETH = FIROETH()


@dataclass(slots=True, frozen=True)
class FIROUSDT:
    name: str = "FIROUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "FIROUSDT"

    def __str__(self):
        return "FIROUSDT"

    def __call__(self):
        return "FIROUSDT"


FIROUSDT = FIROUSDT()


@dataclass(slots=True, frozen=True)
class FISBIDR:
    name: str = "FISBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9223371114.00000000
    margin: bool = False

    def __repr__(self):
        return "FISBIDR"

    def __str__(self):
        return "FISBIDR"

    def __call__(self):
        return "FISBIDR"


FISBIDR = FISBIDR()


@dataclass(slots=True, frozen=True)
class FISBRL:
    name: str = "FISBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "FISBRL"

    def __str__(self):
        return "FISBRL"

    def __call__(self):
        return "FISBRL"


FISBRL = FISBRL()


@dataclass(slots=True, frozen=True)
class FISBTC:
    name: str = "FISBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FISBTC"

    def __str__(self):
        return "FISBTC"

    def __call__(self):
        return "FISBTC"


FISBTC = FISBTC()


@dataclass(slots=True, frozen=True)
class FISBUSD:
    name: str = "FISBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "FISBUSD"

    def __str__(self):
        return "FISBUSD"

    def __call__(self):
        return "FISBUSD"


FISBUSD = FISBUSD()


@dataclass(slots=True, frozen=True)
class FISTRY:
    name: str = "FISTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "FISTRY"

    def __str__(self):
        return "FISTRY"

    def __call__(self):
        return "FISTRY"


FISTRY = FISTRY()


@dataclass(slots=True, frozen=True)
class FISUSDT:
    name: str = "FISUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "FISUSDT"

    def __str__(self):
        return "FISUSDT"

    def __call__(self):
        return "FISUSDT"


FISUSDT = FISUSDT()


@dataclass(slots=True, frozen=True)
class FLMBNB:
    name: str = "FLMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FLMBNB"

    def __str__(self):
        return "FLMBNB"

    def __call__(self):
        return "FLMBNB"


FLMBNB = FLMBNB()


@dataclass(slots=True, frozen=True)
class FLMBTC:
    name: str = "FLMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FLMBTC"

    def __str__(self):
        return "FLMBTC"

    def __call__(self):
        return "FLMBTC"


FLMBTC = FLMBTC()


@dataclass(slots=True, frozen=True)
class FLMBUSD:
    name: str = "FLMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "FLMBUSD"

    def __str__(self):
        return "FLMBUSD"

    def __call__(self):
        return "FLMBUSD"


FLMBUSD = FLMBUSD()


@dataclass(slots=True, frozen=True)
class FLMUSDT:
    name: str = "FLMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "FLMUSDT"

    def __str__(self):
        return "FLMUSDT"

    def __call__(self):
        return "FLMUSDT"


FLMUSDT = FLMUSDT()


@dataclass(slots=True, frozen=True)
class FLOWBNB:
    name: str = "FLOWBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FLOWBNB"

    def __str__(self):
        return "FLOWBNB"

    def __call__(self):
        return "FLOWBNB"


FLOWBNB = FLOWBNB()


@dataclass(slots=True, frozen=True)
class FLOWBTC:
    name: str = "FLOWBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "FLOWBTC"

    def __str__(self):
        return "FLOWBTC"

    def __call__(self):
        return "FLOWBTC"


FLOWBTC = FLOWBTC()


@dataclass(slots=True, frozen=True)
class FLOWBUSD:
    name: str = "FLOWBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "FLOWBUSD"

    def __str__(self):
        return "FLOWBUSD"

    def __call__(self):
        return "FLOWBUSD"


FLOWBUSD = FLOWBUSD()


@dataclass(slots=True, frozen=True)
class FLOWUSDT:
    name: str = "FLOWUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "FLOWUSDT"

    def __str__(self):
        return "FLOWUSDT"

    def __call__(self):
        return "FLOWUSDT"


FLOWUSDT = FLOWUSDT()


@dataclass(slots=True, frozen=True)
class FLUXBTC:
    name: str = "FLUXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FLUXBTC"

    def __str__(self):
        return "FLUXBTC"

    def __call__(self):
        return "FLUXBTC"


FLUXBTC = FLUXBTC()


@dataclass(slots=True, frozen=True)
class FLUXBUSD:
    name: str = "FLUXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "FLUXBUSD"

    def __str__(self):
        return "FLUXBUSD"

    def __call__(self):
        return "FLUXBUSD"


FLUXBUSD = FLUXBUSD()


@dataclass(slots=True, frozen=True)
class FLUXUSDT:
    name: str = "FLUXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "FLUXUSDT"

    def __str__(self):
        return "FLUXUSDT"

    def __call__(self):
        return "FLUXUSDT"


FLUXUSDT = FLUXUSDT()


@dataclass(slots=True, frozen=True)
class FORBNB:
    name: str = "FORBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FORBNB"

    def __str__(self):
        return "FORBNB"

    def __call__(self):
        return "FORBNB"


FORBNB = FORBNB()


@dataclass(slots=True, frozen=True)
class FORBTC:
    name: str = "FORBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FORBTC"

    def __str__(self):
        return "FORBTC"

    def __call__(self):
        return "FORBTC"


FORBTC = FORBTC()


@dataclass(slots=True, frozen=True)
class FORBUSD:
    name: str = "FORBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FORBUSD"

    def __str__(self):
        return "FORBUSD"

    def __call__(self):
        return "FORBUSD"


FORBUSD = FORBUSD()


@dataclass(slots=True, frozen=True)
class FORTHBTC:
    name: str = "FORTHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FORTHBTC"

    def __str__(self):
        return "FORTHBTC"

    def __call__(self):
        return "FORTHBTC"


FORTHBTC = FORTHBTC()


@dataclass(slots=True, frozen=True)
class FORTHBUSD:
    name: str = "FORTHBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "FORTHBUSD"

    def __str__(self):
        return "FORTHBUSD"

    def __call__(self):
        return "FORTHBUSD"


FORTHBUSD = FORTHBUSD()


@dataclass(slots=True, frozen=True)
class FORTHUSDT:
    name: str = "FORTHUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "FORTHUSDT"

    def __str__(self):
        return "FORTHUSDT"

    def __call__(self):
        return "FORTHUSDT"


FORTHUSDT = FORTHUSDT()


@dataclass(slots=True, frozen=True)
class FORUSDT:
    name: str = "FORUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FORUSDT"

    def __str__(self):
        return "FORUSDT"

    def __call__(self):
        return "FORUSDT"


FORUSDT = FORUSDT()


@dataclass(slots=True, frozen=True)
class FRONTBTC:
    name: str = "FRONTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FRONTBTC"

    def __str__(self):
        return "FRONTBTC"

    def __call__(self):
        return "FRONTBTC"


FRONTBTC = FRONTBTC()


@dataclass(slots=True, frozen=True)
class FRONTBUSD:
    name: str = "FRONTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "FRONTBUSD"

    def __str__(self):
        return "FRONTBUSD"

    def __call__(self):
        return "FRONTBUSD"


FRONTBUSD = FRONTBUSD()


@dataclass(slots=True, frozen=True)
class FRONTETH:
    name: str = "FRONTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FRONTETH"

    def __str__(self):
        return "FRONTETH"

    def __call__(self):
        return "FRONTETH"


FRONTETH = FRONTETH()


@dataclass(slots=True, frozen=True)
class FRONTUSDT:
    name: str = "FRONTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FRONTUSDT"

    def __str__(self):
        return "FRONTUSDT"

    def __call__(self):
        return "FRONTUSDT"


FRONTUSDT = FRONTUSDT()


@dataclass(slots=True, frozen=True)
class FTMAUD:
    name: str = "FTMAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMAUD"

    def __str__(self):
        return "FTMAUD"

    def __call__(self):
        return "FTMAUD"


FTMAUD = FTMAUD()


@dataclass(slots=True, frozen=True)
class FTMBIDR:
    name: str = "FTMBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9223371114.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMBIDR"

    def __str__(self):
        return "FTMBIDR"

    def __call__(self):
        return "FTMBIDR"


FTMBIDR = FTMBIDR()


@dataclass(slots=True, frozen=True)
class FTMBNB:
    name: str = "FTMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMBNB"

    def __str__(self):
        return "FTMBNB"

    def __call__(self):
        return "FTMBNB"


FTMBNB = FTMBNB()


@dataclass(slots=True, frozen=True)
class FTMBRL:
    name: str = "FTMBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMBRL"

    def __str__(self):
        return "FTMBRL"

    def __call__(self):
        return "FTMBRL"


FTMBRL = FTMBRL()


@dataclass(slots=True, frozen=True)
class FTMBTC:
    name: str = "FTMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "FTMBTC"

    def __str__(self):
        return "FTMBTC"

    def __call__(self):
        return "FTMBTC"


FTMBTC = FTMBTC()


@dataclass(slots=True, frozen=True)
class FTMBUSD:
    name: str = "FTMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "FTMBUSD"

    def __str__(self):
        return "FTMBUSD"

    def __call__(self):
        return "FTMBUSD"


FTMBUSD = FTMBUSD()


@dataclass(slots=True, frozen=True)
class FTMETH:
    name: str = "FTMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMETH"

    def __str__(self):
        return "FTMETH"

    def __call__(self):
        return "FTMETH"


FTMETH = FTMETH()


@dataclass(slots=True, frozen=True)
class FTMEUR:
    name: str = "FTMEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMEUR"

    def __str__(self):
        return "FTMEUR"

    def __call__(self):
        return "FTMEUR"


FTMEUR = FTMEUR()


@dataclass(slots=True, frozen=True)
class FTMPAX:
    name: str = "FTMPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMPAX"

    def __str__(self):
        return "FTMPAX"

    def __call__(self):
        return "FTMPAX"


FTMPAX = FTMPAX()


@dataclass(slots=True, frozen=True)
class FTMRUB:
    name: str = "FTMRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMRUB"

    def __str__(self):
        return "FTMRUB"

    def __call__(self):
        return "FTMRUB"


FTMRUB = FTMRUB()


@dataclass(slots=True, frozen=True)
class FTMTRY:
    name: str = "FTMTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMTRY"

    def __str__(self):
        return "FTMTRY"

    def __call__(self):
        return "FTMTRY"


FTMTRY = FTMTRY()


@dataclass(slots=True, frozen=True)
class FTMTUSD:
    name: str = "FTMTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMTUSD"

    def __str__(self):
        return "FTMTUSD"

    def __call__(self):
        return "FTMTUSD"


FTMTUSD = FTMTUSD()


@dataclass(slots=True, frozen=True)
class FTMUSDC:
    name: str = "FTMUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FTMUSDC"

    def __str__(self):
        return "FTMUSDC"

    def __call__(self):
        return "FTMUSDC"


FTMUSDC = FTMUSDC()


@dataclass(slots=True, frozen=True)
class FTMUSDT:
    name: str = "FTMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "FTMUSDT"

    def __str__(self):
        return "FTMUSDT"

    def __call__(self):
        return "FTMUSDT"


FTMUSDT = FTMUSDT()


@dataclass(slots=True, frozen=True)
class FTTBNB:
    name: str = "FTTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FTTBNB"

    def __str__(self):
        return "FTTBNB"

    def __call__(self):
        return "FTTBNB"


FTTBNB = FTTBNB()


@dataclass(slots=True, frozen=True)
class FTTBTC:
    name: str = "FTTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FTTBTC"

    def __str__(self):
        return "FTTBTC"

    def __call__(self):
        return "FTTBTC"


FTTBTC = FTTBTC()


@dataclass(slots=True, frozen=True)
class FTTBUSD:
    name: str = "FTTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "FTTBUSD"

    def __str__(self):
        return "FTTBUSD"

    def __call__(self):
        return "FTTBUSD"


FTTBUSD = FTTBUSD()


@dataclass(slots=True, frozen=True)
class FTTETH:
    name: str = "FTTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FTTETH"

    def __str__(self):
        return "FTTETH"

    def __call__(self):
        return "FTTETH"


FTTETH = FTTETH()


@dataclass(slots=True, frozen=True)
class FTTUSDT:
    name: str = "FTTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "FTTUSDT"

    def __str__(self):
        return "FTTUSDT"

    def __call__(self):
        return "FTTUSDT"


FTTUSDT = FTTUSDT()


@dataclass(slots=True, frozen=True)
class FUELBTC:
    name: str = "FUELBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FUELBTC"

    def __str__(self):
        return "FUELBTC"

    def __call__(self):
        return "FUELBTC"


FUELBTC = FUELBTC()


@dataclass(slots=True, frozen=True)
class FUELETH:
    name: str = "FUELETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FUELETH"

    def __str__(self):
        return "FUELETH"

    def __call__(self):
        return "FUELETH"


FUELETH = FUELETH()


@dataclass(slots=True, frozen=True)
class FUNBNB:
    name: str = "FUNBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FUNBNB"

    def __str__(self):
        return "FUNBNB"

    def __call__(self):
        return "FUNBNB"


FUNBNB = FUNBNB()


@dataclass(slots=True, frozen=True)
class FUNBTC:
    name: str = "FUNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FUNBTC"

    def __str__(self):
        return "FUNBTC"

    def __call__(self):
        return "FUNBTC"


FUNBTC = FUNBTC()


@dataclass(slots=True, frozen=True)
class FUNETH:
    name: str = "FUNETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FUNETH"

    def __str__(self):
        return "FUNETH"

    def __call__(self):
        return "FUNETH"


FUNETH = FUNETH()


@dataclass(slots=True, frozen=True)
class FUNUSDT:
    name: str = "FUNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "FUNUSDT"

    def __str__(self):
        return "FUNUSDT"

    def __call__(self):
        return "FUNUSDT"


FUNUSDT = FUNUSDT()


@dataclass(slots=True, frozen=True)
class FXSBTC:
    name: str = "FXSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "FXSBTC"

    def __str__(self):
        return "FXSBTC"

    def __call__(self):
        return "FXSBTC"


FXSBTC = FXSBTC()


@dataclass(slots=True, frozen=True)
class FXSBUSD:
    name: str = "FXSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "FXSBUSD"

    def __str__(self):
        return "FXSBUSD"

    def __call__(self):
        return "FXSBUSD"


FXSBUSD = FXSBUSD()


@dataclass(slots=True, frozen=True)
class FXSUSDT:
    name: str = "FXSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "FXSUSDT"

    def __str__(self):
        return "FXSUSDT"

    def __call__(self):
        return "FXSUSDT"


FXSUSDT = FXSUSDT()


@dataclass(slots=True, frozen=True)
class GALAAUD:
    name: str = "GALAAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GALAAUD"

    def __str__(self):
        return "GALAAUD"

    def __call__(self):
        return "GALAAUD"


GALAAUD = GALAAUD()


@dataclass(slots=True, frozen=True)
class GALABNB:
    name: str = "GALABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "GALABNB"

    def __str__(self):
        return "GALABNB"

    def __call__(self):
        return "GALABNB"


GALABNB = GALABNB()


@dataclass(slots=True, frozen=True)
class GALABRL:
    name: str = "GALABRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GALABRL"

    def __str__(self):
        return "GALABRL"

    def __call__(self):
        return "GALABRL"


GALABRL = GALABRL()


@dataclass(slots=True, frozen=True)
class GALABTC:
    name: str = "GALABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = True

    def __repr__(self):
        return "GALABTC"

    def __str__(self):
        return "GALABTC"

    def __call__(self):
        return "GALABTC"


GALABTC = GALABTC()


@dataclass(slots=True, frozen=True)
class GALABUSD:
    name: str = "GALABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GALABUSD"

    def __str__(self):
        return "GALABUSD"

    def __call__(self):
        return "GALABUSD"


GALABUSD = GALABUSD()


@dataclass(slots=True, frozen=True)
class GALAETH:
    name: str = "GALAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GALAETH"

    def __str__(self):
        return "GALAETH"

    def __call__(self):
        return "GALAETH"


GALAETH = GALAETH()


@dataclass(slots=True, frozen=True)
class GALAEUR:
    name: str = "GALAEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GALAEUR"

    def __str__(self):
        return "GALAEUR"

    def __call__(self):
        return "GALAEUR"


GALAEUR = GALAEUR()


@dataclass(slots=True, frozen=True)
class GALATRY:
    name: str = "GALATRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GALATRY"

    def __str__(self):
        return "GALATRY"

    def __call__(self):
        return "GALATRY"


GALATRY = GALATRY()


@dataclass(slots=True, frozen=True)
class GALAUSDT:
    name: str = "GALAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GALAUSDT"

    def __str__(self):
        return "GALAUSDT"

    def __call__(self):
        return "GALAUSDT"


GALAUSDT = GALAUSDT()


@dataclass(slots=True, frozen=True)
class GALBNB:
    name: str = "GALBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GALBNB"

    def __str__(self):
        return "GALBNB"

    def __call__(self):
        return "GALBNB"


GALBNB = GALBNB()


@dataclass(slots=True, frozen=True)
class GALBRL:
    name: str = "GALBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "GALBRL"

    def __str__(self):
        return "GALBRL"

    def __call__(self):
        return "GALBRL"


GALBRL = GALBRL()


@dataclass(slots=True, frozen=True)
class GALBTC:
    name: str = "GALBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GALBTC"

    def __str__(self):
        return "GALBTC"

    def __call__(self):
        return "GALBTC"


GALBTC = GALBTC()


@dataclass(slots=True, frozen=True)
class GALBUSD:
    name: str = "GALBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GALBUSD"

    def __str__(self):
        return "GALBUSD"

    def __call__(self):
        return "GALBUSD"


GALBUSD = GALBUSD()


@dataclass(slots=True, frozen=True)
class GALETH:
    name: str = "GALETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GALETH"

    def __str__(self):
        return "GALETH"

    def __call__(self):
        return "GALETH"


GALETH = GALETH()


@dataclass(slots=True, frozen=True)
class GALEUR:
    name: str = "GALEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GALEUR"

    def __str__(self):
        return "GALEUR"

    def __call__(self):
        return "GALEUR"


GALEUR = GALEUR()


@dataclass(slots=True, frozen=True)
class GALTRY:
    name: str = "GALTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "GALTRY"

    def __str__(self):
        return "GALTRY"

    def __call__(self):
        return "GALTRY"


GALTRY = GALTRY()


@dataclass(slots=True, frozen=True)
class GALUSDT:
    name: str = "GALUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GALUSDT"

    def __str__(self):
        return "GALUSDT"

    def __call__(self):
        return "GALUSDT"


GALUSDT = GALUSDT()


@dataclass(slots=True, frozen=True)
class GASBTC:
    name: str = "GASBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GASBTC"

    def __str__(self):
        return "GASBTC"

    def __call__(self):
        return "GASBTC"


GASBTC = GASBTC()


@dataclass(slots=True, frozen=True)
class GASBUSD:
    name: str = "GASBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GASBUSD"

    def __str__(self):
        return "GASBUSD"

    def __call__(self):
        return "GASBUSD"


GASBUSD = GASBUSD()


@dataclass(slots=True, frozen=True)
class GBPBUSD:
    name: str = "GBPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "GBPBUSD"

    def __str__(self):
        return "GBPBUSD"

    def __call__(self):
        return "GBPBUSD"


GBPBUSD = GBPBUSD()


@dataclass(slots=True, frozen=True)
class GBPUSDT:
    name: str = "GBPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "GBPUSDT"

    def __str__(self):
        return "GBPUSDT"

    def __call__(self):
        return "GBPUSDT"


GBPUSDT = GBPUSDT()


@dataclass(slots=True, frozen=True)
class GHSTBUSD:
    name: str = "GHSTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "GHSTBUSD"

    def __str__(self):
        return "GHSTBUSD"

    def __call__(self):
        return "GHSTBUSD"


GHSTBUSD = GHSTBUSD()


@dataclass(slots=True, frozen=True)
class GHSTETH:
    name: str = "GHSTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GHSTETH"

    def __str__(self):
        return "GHSTETH"

    def __call__(self):
        return "GHSTETH"


GHSTETH = GHSTETH()


@dataclass(slots=True, frozen=True)
class GHSTUSDT:
    name: str = "GHSTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GHSTUSDT"

    def __str__(self):
        return "GHSTUSDT"

    def __call__(self):
        return "GHSTUSDT"


GHSTUSDT = GHSTUSDT()


@dataclass(slots=True, frozen=True)
class GLMBTC:
    name: str = "GLMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "GLMBTC"

    def __str__(self):
        return "GLMBTC"

    def __call__(self):
        return "GLMBTC"


GLMBTC = GLMBTC()


@dataclass(slots=True, frozen=True)
class GLMBUSD:
    name: str = "GLMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GLMBUSD"

    def __str__(self):
        return "GLMBUSD"

    def __call__(self):
        return "GLMBUSD"


GLMBUSD = GLMBUSD()


@dataclass(slots=True, frozen=True)
class GLMETH:
    name: str = "GLMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GLMETH"

    def __str__(self):
        return "GLMETH"

    def __call__(self):
        return "GLMETH"


GLMETH = GLMETH()


@dataclass(slots=True, frozen=True)
class GLMRBNB:
    name: str = "GLMRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GLMRBNB"

    def __str__(self):
        return "GLMRBNB"

    def __call__(self):
        return "GLMRBNB"


GLMRBNB = GLMRBNB()


@dataclass(slots=True, frozen=True)
class GLMRBTC:
    name: str = "GLMRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GLMRBTC"

    def __str__(self):
        return "GLMRBTC"

    def __call__(self):
        return "GLMRBTC"


GLMRBTC = GLMRBTC()


@dataclass(slots=True, frozen=True)
class GLMRBUSD:
    name: str = "GLMRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GLMRBUSD"

    def __str__(self):
        return "GLMRBUSD"

    def __call__(self):
        return "GLMRBUSD"


GLMRBUSD = GLMRBUSD()


@dataclass(slots=True, frozen=True)
class GLMRUSDT:
    name: str = "GLMRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GLMRUSDT"

    def __str__(self):
        return "GLMRUSDT"

    def __call__(self):
        return "GLMRUSDT"


GLMRUSDT = GLMRUSDT()


@dataclass(slots=True, frozen=True)
class GMTAUD:
    name: str = "GMTAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GMTAUD"

    def __str__(self):
        return "GMTAUD"

    def __call__(self):
        return "GMTAUD"


GMTAUD = GMTAUD()


@dataclass(slots=True, frozen=True)
class GMTBNB:
    name: str = "GMTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GMTBNB"

    def __str__(self):
        return "GMTBNB"

    def __call__(self):
        return "GMTBNB"


GMTBNB = GMTBNB()


@dataclass(slots=True, frozen=True)
class GMTBRL:
    name: str = "GMTBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GMTBRL"

    def __str__(self):
        return "GMTBRL"

    def __call__(self):
        return "GMTBRL"


GMTBRL = GMTBRL()


@dataclass(slots=True, frozen=True)
class GMTBTC:
    name: str = "GMTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GMTBTC"

    def __str__(self):
        return "GMTBTC"

    def __call__(self):
        return "GMTBTC"


GMTBTC = GMTBTC()


@dataclass(slots=True, frozen=True)
class GMTBUSD:
    name: str = "GMTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GMTBUSD"

    def __str__(self):
        return "GMTBUSD"

    def __call__(self):
        return "GMTBUSD"


GMTBUSD = GMTBUSD()


@dataclass(slots=True, frozen=True)
class GMTETH:
    name: str = "GMTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GMTETH"

    def __str__(self):
        return "GMTETH"

    def __call__(self):
        return "GMTETH"


GMTETH = GMTETH()


@dataclass(slots=True, frozen=True)
class GMTEUR:
    name: str = "GMTEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GMTEUR"

    def __str__(self):
        return "GMTEUR"

    def __call__(self):
        return "GMTEUR"


GMTEUR = GMTEUR()


@dataclass(slots=True, frozen=True)
class GMTGBP:
    name: str = "GMTGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GMTGBP"

    def __str__(self):
        return "GMTGBP"

    def __call__(self):
        return "GMTGBP"


GMTGBP = GMTGBP()


@dataclass(slots=True, frozen=True)
class GMTTRY:
    name: str = "GMTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "GMTTRY"

    def __str__(self):
        return "GMTTRY"

    def __call__(self):
        return "GMTTRY"


GMTTRY = GMTTRY()


@dataclass(slots=True, frozen=True)
class GMTUSDT:
    name: str = "GMTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GMTUSDT"

    def __str__(self):
        return "GMTUSDT"

    def __call__(self):
        return "GMTUSDT"


GMTUSDT = GMTUSDT()


@dataclass(slots=True, frozen=True)
class GMXBTC:
    name: str = "GMXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "GMXBTC"

    def __str__(self):
        return "GMXBTC"

    def __call__(self):
        return "GMXBTC"


GMXBTC = GMXBTC()


@dataclass(slots=True, frozen=True)
class GMXBUSD:
    name: str = "GMXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "GMXBUSD"

    def __str__(self):
        return "GMXBUSD"

    def __call__(self):
        return "GMXBUSD"


GMXBUSD = GMXBUSD()


@dataclass(slots=True, frozen=True)
class GMXUSDT:
    name: str = "GMXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "GMXUSDT"

    def __str__(self):
        return "GMXUSDT"

    def __call__(self):
        return "GMXUSDT"


GMXUSDT = GMXUSDT()


@dataclass(slots=True, frozen=True)
class GNOBNB:
    name: str = "GNOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GNOBNB"

    def __str__(self):
        return "GNOBNB"

    def __call__(self):
        return "GNOBNB"


GNOBNB = GNOBNB()


@dataclass(slots=True, frozen=True)
class GNOBTC:
    name: str = "GNOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GNOBTC"

    def __str__(self):
        return "GNOBTC"

    def __call__(self):
        return "GNOBTC"


GNOBTC = GNOBTC()


@dataclass(slots=True, frozen=True)
class GNOBUSD:
    name: str = "GNOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "GNOBUSD"

    def __str__(self):
        return "GNOBUSD"

    def __call__(self):
        return "GNOBUSD"


GNOBUSD = GNOBUSD()


@dataclass(slots=True, frozen=True)
class GNOUSDT:
    name: str = "GNOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "GNOUSDT"

    def __str__(self):
        return "GNOUSDT"

    def __call__(self):
        return "GNOUSDT"


GNOUSDT = GNOUSDT()


@dataclass(slots=True, frozen=True)
class GNTBNB:
    name: str = "GNTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "GNTBNB"

    def __str__(self):
        return "GNTBNB"

    def __call__(self):
        return "GNTBNB"


GNTBNB = GNTBNB()


@dataclass(slots=True, frozen=True)
class GNTBTC:
    name: str = "GNTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GNTBTC"

    def __str__(self):
        return "GNTBTC"

    def __call__(self):
        return "GNTBTC"


GNTBTC = GNTBTC()


@dataclass(slots=True, frozen=True)
class GNTETH:
    name: str = "GNTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GNTETH"

    def __str__(self):
        return "GNTETH"

    def __call__(self):
        return "GNTETH"


GNTETH = GNTETH()


@dataclass(slots=True, frozen=True)
class GOBNB:
    name: str = "GOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GOBNB"

    def __str__(self):
        return "GOBNB"

    def __call__(self):
        return "GOBNB"


GOBNB = GOBNB()


@dataclass(slots=True, frozen=True)
class GOBTC:
    name: str = "GOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GOBTC"

    def __str__(self):
        return "GOBTC"

    def __call__(self):
        return "GOBTC"


GOBTC = GOBTC()


@dataclass(slots=True, frozen=True)
class GRSBTC:
    name: str = "GRSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GRSBTC"

    def __str__(self):
        return "GRSBTC"

    def __call__(self):
        return "GRSBTC"


GRSBTC = GRSBTC()


@dataclass(slots=True, frozen=True)
class GRSETH:
    name: str = "GRSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GRSETH"

    def __str__(self):
        return "GRSETH"

    def __call__(self):
        return "GRSETH"


GRSETH = GRSETH()


@dataclass(slots=True, frozen=True)
class GRTBTC:
    name: str = "GRTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "GRTBTC"

    def __str__(self):
        return "GRTBTC"

    def __call__(self):
        return "GRTBTC"


GRTBTC = GRTBTC()


@dataclass(slots=True, frozen=True)
class GRTBUSD:
    name: str = "GRTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "GRTBUSD"

    def __str__(self):
        return "GRTBUSD"

    def __call__(self):
        return "GRTBUSD"


GRTBUSD = GRTBUSD()


@dataclass(slots=True, frozen=True)
class GRTETH:
    name: str = "GRTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "GRTETH"

    def __str__(self):
        return "GRTETH"

    def __call__(self):
        return "GRTETH"


GRTETH = GRTETH()


@dataclass(slots=True, frozen=True)
class GRTEUR:
    name: str = "GRTEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "GRTEUR"

    def __str__(self):
        return "GRTEUR"

    def __call__(self):
        return "GRTEUR"


GRTEUR = GRTEUR()


@dataclass(slots=True, frozen=True)
class GRTTRY:
    name: str = "GRTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GRTTRY"

    def __str__(self):
        return "GRTTRY"

    def __call__(self):
        return "GRTTRY"


GRTTRY = GRTTRY()


@dataclass(slots=True, frozen=True)
class GRTUSDT:
    name: str = "GRTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "GRTUSDT"

    def __str__(self):
        return "GRTUSDT"

    def __call__(self):
        return "GRTUSDT"


GRTUSDT = GRTUSDT()


@dataclass(slots=True, frozen=True)
class GTCBNB:
    name: str = "GTCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GTCBNB"

    def __str__(self):
        return "GTCBNB"

    def __call__(self):
        return "GTCBNB"


GTCBNB = GTCBNB()


@dataclass(slots=True, frozen=True)
class GTCBTC:
    name: str = "GTCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "GTCBTC"

    def __str__(self):
        return "GTCBTC"

    def __call__(self):
        return "GTCBTC"


GTCBTC = GTCBTC()


@dataclass(slots=True, frozen=True)
class GTCBUSD:
    name: str = "GTCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "GTCBUSD"

    def __str__(self):
        return "GTCBUSD"

    def __call__(self):
        return "GTCBUSD"


GTCBUSD = GTCBUSD()


@dataclass(slots=True, frozen=True)
class GTCUSDT:
    name: str = "GTCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "GTCUSDT"

    def __str__(self):
        return "GTCUSDT"

    def __call__(self):
        return "GTCUSDT"


GTCUSDT = GTCUSDT()


@dataclass(slots=True, frozen=True)
class GTOBNB:
    name: str = "GTOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GTOBNB"

    def __str__(self):
        return "GTOBNB"

    def __call__(self):
        return "GTOBNB"


GTOBNB = GTOBNB()


@dataclass(slots=True, frozen=True)
class GTOBTC:
    name: str = "GTOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GTOBTC"

    def __str__(self):
        return "GTOBTC"

    def __call__(self):
        return "GTOBTC"


GTOBTC = GTOBTC()


@dataclass(slots=True, frozen=True)
class GTOBUSD:
    name: str = "GTOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GTOBUSD"

    def __str__(self):
        return "GTOBUSD"

    def __call__(self):
        return "GTOBUSD"


GTOBUSD = GTOBUSD()


@dataclass(slots=True, frozen=True)
class GTOETH:
    name: str = "GTOETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GTOETH"

    def __str__(self):
        return "GTOETH"

    def __call__(self):
        return "GTOETH"


GTOETH = GTOETH()


@dataclass(slots=True, frozen=True)
class GTOPAX:
    name: str = "GTOPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GTOPAX"

    def __str__(self):
        return "GTOPAX"

    def __call__(self):
        return "GTOPAX"


GTOPAX = GTOPAX()


@dataclass(slots=True, frozen=True)
class GTOTUSD:
    name: str = "GTOTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GTOTUSD"

    def __str__(self):
        return "GTOTUSD"

    def __call__(self):
        return "GTOTUSD"


GTOTUSD = GTOTUSD()


@dataclass(slots=True, frozen=True)
class GTOUSDC:
    name: str = "GTOUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GTOUSDC"

    def __str__(self):
        return "GTOUSDC"

    def __call__(self):
        return "GTOUSDC"


GTOUSDC = GTOUSDC()


@dataclass(slots=True, frozen=True)
class GTOUSDT:
    name: str = "GTOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GTOUSDT"

    def __str__(self):
        return "GTOUSDT"

    def __call__(self):
        return "GTOUSDT"


GTOUSDT = GTOUSDT()


@dataclass(slots=True, frozen=True)
class GVTBTC:
    name: str = "GVTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GVTBTC"

    def __str__(self):
        return "GVTBTC"

    def __call__(self):
        return "GVTBTC"


GVTBTC = GVTBTC()


@dataclass(slots=True, frozen=True)
class GVTETH:
    name: str = "GVTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GVTETH"

    def __str__(self):
        return "GVTETH"

    def __call__(self):
        return "GVTETH"


GVTETH = GVTETH()


@dataclass(slots=True, frozen=True)
class GXSBNB:
    name: str = "GXSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "GXSBNB"

    def __str__(self):
        return "GXSBNB"

    def __call__(self):
        return "GXSBNB"


GXSBNB = GXSBNB()


@dataclass(slots=True, frozen=True)
class GXSBTC:
    name: str = "GXSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GXSBTC"

    def __str__(self):
        return "GXSBTC"

    def __call__(self):
        return "GXSBTC"


GXSBTC = GXSBTC()


@dataclass(slots=True, frozen=True)
class GXSETH:
    name: str = "GXSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "GXSETH"

    def __str__(self):
        return "GXSETH"

    def __call__(self):
        return "GXSETH"


GXSETH = GXSETH()


@dataclass(slots=True, frozen=True)
class GXSUSDT:
    name: str = "GXSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "GXSUSDT"

    def __str__(self):
        return "GXSUSDT"

    def __call__(self):
        return "GXSUSDT"


GXSUSDT = GXSUSDT()


@dataclass(slots=True, frozen=True)
class HARDBNB:
    name: str = "HARDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HARDBNB"

    def __str__(self):
        return "HARDBNB"

    def __call__(self):
        return "HARDBNB"


HARDBNB = HARDBNB()


@dataclass(slots=True, frozen=True)
class HARDBTC:
    name: str = "HARDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HARDBTC"

    def __str__(self):
        return "HARDBTC"

    def __call__(self):
        return "HARDBTC"


HARDBTC = HARDBTC()


@dataclass(slots=True, frozen=True)
class HARDBUSD:
    name: str = "HARDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "HARDBUSD"

    def __str__(self):
        return "HARDBUSD"

    def __call__(self):
        return "HARDBUSD"


HARDBUSD = HARDBUSD()


@dataclass(slots=True, frozen=True)
class HARDUSDT:
    name: str = "HARDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "HARDUSDT"

    def __str__(self):
        return "HARDUSDT"

    def __call__(self):
        return "HARDUSDT"


HARDUSDT = HARDUSDT()


@dataclass(slots=True, frozen=True)
class HBARBNB:
    name: str = "HBARBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HBARBNB"

    def __str__(self):
        return "HBARBNB"

    def __call__(self):
        return "HBARBNB"


HBARBNB = HBARBNB()


@dataclass(slots=True, frozen=True)
class HBARBTC:
    name: str = "HBARBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "HBARBTC"

    def __str__(self):
        return "HBARBTC"

    def __call__(self):
        return "HBARBTC"


HBARBTC = HBARBTC()


@dataclass(slots=True, frozen=True)
class HBARBUSD:
    name: str = "HBARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "HBARBUSD"

    def __str__(self):
        return "HBARBUSD"

    def __call__(self):
        return "HBARBUSD"


HBARBUSD = HBARBUSD()


@dataclass(slots=True, frozen=True)
class HBARUSDT:
    name: str = "HBARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "HBARUSDT"

    def __str__(self):
        return "HBARUSDT"

    def __call__(self):
        return "HBARUSDT"


HBARUSDT = HBARUSDT()


@dataclass(slots=True, frozen=True)
class HCBTC:
    name: str = "HCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HCBTC"

    def __str__(self):
        return "HCBTC"

    def __call__(self):
        return "HCBTC"


HCBTC = HCBTC()


@dataclass(slots=True, frozen=True)
class HCETH:
    name: str = "HCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HCETH"

    def __str__(self):
        return "HCETH"

    def __call__(self):
        return "HCETH"


HCETH = HCETH()


@dataclass(slots=True, frozen=True)
class HCUSDT:
    name: str = "HCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "HCUSDT"

    def __str__(self):
        return "HCUSDT"

    def __call__(self):
        return "HCUSDT"


HCUSDT = HCUSDT()


@dataclass(slots=True, frozen=True)
class HEGICBUSD:
    name: str = "HEGICBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "HEGICBUSD"

    def __str__(self):
        return "HEGICBUSD"

    def __call__(self):
        return "HEGICBUSD"


HEGICBUSD = HEGICBUSD()


@dataclass(slots=True, frozen=True)
class HEGICETH:
    name: str = "HEGICETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HEGICETH"

    def __str__(self):
        return "HEGICETH"

    def __call__(self):
        return "HEGICETH"


HEGICETH = HEGICETH()


@dataclass(slots=True, frozen=True)
class HFTBTC:
    name: str = "HFTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 46116860414.00000000
    margin: bool = False

    def __repr__(self):
        return "HFTBTC"

    def __str__(self):
        return "HFTBTC"

    def __call__(self):
        return "HFTBTC"


HFTBTC = HFTBTC()


@dataclass(slots=True, frozen=True)
class HFTBUSD:
    name: str = "HFTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HFTBUSD"

    def __str__(self):
        return "HFTBUSD"

    def __call__(self):
        return "HFTBUSD"


HFTBUSD = HFTBUSD()


@dataclass(slots=True, frozen=True)
class HFTUSDT:
    name: str = "HFTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HFTUSDT"

    def __str__(self):
        return "HFTUSDT"

    def __call__(self):
        return "HFTUSDT"


HFTUSDT = HFTUSDT()


@dataclass(slots=True, frozen=True)
class HIFIETH:
    name: str = "HIFIETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HIFIETH"

    def __str__(self):
        return "HIFIETH"

    def __call__(self):
        return "HIFIETH"


HIFIETH = HIFIETH()


@dataclass(slots=True, frozen=True)
class HIFIUSDT:
    name: str = "HIFIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HIFIUSDT"

    def __str__(self):
        return "HIFIUSDT"

    def __call__(self):
        return "HIFIUSDT"


HIFIUSDT = HIFIUSDT()


@dataclass(slots=True, frozen=True)
class HIGHBNB:
    name: str = "HIGHBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HIGHBNB"

    def __str__(self):
        return "HIGHBNB"

    def __call__(self):
        return "HIGHBNB"


HIGHBNB = HIGHBNB()


@dataclass(slots=True, frozen=True)
class HIGHBTC:
    name: str = "HIGHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HIGHBTC"

    def __str__(self):
        return "HIGHBTC"

    def __call__(self):
        return "HIGHBTC"


HIGHBTC = HIGHBTC()


@dataclass(slots=True, frozen=True)
class HIGHBUSD:
    name: str = "HIGHBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "HIGHBUSD"

    def __str__(self):
        return "HIGHBUSD"

    def __call__(self):
        return "HIGHBUSD"


HIGHBUSD = HIGHBUSD()


@dataclass(slots=True, frozen=True)
class HIGHUSDT:
    name: str = "HIGHUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "HIGHUSDT"

    def __str__(self):
        return "HIGHUSDT"

    def __call__(self):
        return "HIGHUSDT"


HIGHUSDT = HIGHUSDT()


@dataclass(slots=True, frozen=True)
class HIVEBNB:
    name: str = "HIVEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HIVEBNB"

    def __str__(self):
        return "HIVEBNB"

    def __call__(self):
        return "HIVEBNB"


HIVEBNB = HIVEBNB()


@dataclass(slots=True, frozen=True)
class HIVEBTC:
    name: str = "HIVEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "HIVEBTC"

    def __str__(self):
        return "HIVEBTC"

    def __call__(self):
        return "HIVEBTC"


HIVEBTC = HIVEBTC()


@dataclass(slots=True, frozen=True)
class HIVEBUSD:
    name: str = "HIVEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "HIVEBUSD"

    def __str__(self):
        return "HIVEBUSD"

    def __call__(self):
        return "HIVEBUSD"


HIVEBUSD = HIVEBUSD()


@dataclass(slots=True, frozen=True)
class HIVEUSDT:
    name: str = "HIVEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "HIVEUSDT"

    def __str__(self):
        return "HIVEUSDT"

    def __call__(self):
        return "HIVEUSDT"


HIVEUSDT = HIVEUSDT()


@dataclass(slots=True, frozen=True)
class HNTBTC:
    name: str = "HNTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HNTBTC"

    def __str__(self):
        return "HNTBTC"

    def __call__(self):
        return "HNTBTC"


HNTBTC = HNTBTC()


@dataclass(slots=True, frozen=True)
class HNTBUSD:
    name: str = "HNTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "HNTBUSD"

    def __str__(self):
        return "HNTBUSD"

    def __call__(self):
        return "HNTBUSD"


HNTBUSD = HNTBUSD()


@dataclass(slots=True, frozen=True)
class HNTUSDT:
    name: str = "HNTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "HNTUSDT"

    def __str__(self):
        return "HNTUSDT"

    def __call__(self):
        return "HNTUSDT"


HNTUSDT = HNTUSDT()


@dataclass(slots=True, frozen=True)
class HOOKBNB:
    name: str = "HOOKBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "HOOKBNB"

    def __str__(self):
        return "HOOKBNB"

    def __call__(self):
        return "HOOKBNB"


HOOKBNB = HOOKBNB()


@dataclass(slots=True, frozen=True)
class HOOKBTC:
    name: str = "HOOKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 46116860414.00000000
    margin: bool = False

    def __repr__(self):
        return "HOOKBTC"

    def __str__(self):
        return "HOOKBTC"

    def __call__(self):
        return "HOOKBTC"


HOOKBTC = HOOKBTC()


@dataclass(slots=True, frozen=True)
class HOOKBUSD:
    name: str = "HOOKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HOOKBUSD"

    def __str__(self):
        return "HOOKBUSD"

    def __call__(self):
        return "HOOKBUSD"


HOOKBUSD = HOOKBUSD()


@dataclass(slots=True, frozen=True)
class HOOKUSDT:
    name: str = "HOOKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HOOKUSDT"

    def __str__(self):
        return "HOOKUSDT"

    def __call__(self):
        return "HOOKUSDT"


HOOKUSDT = HOOKUSDT()


@dataclass(slots=True, frozen=True)
class HOTBNB:
    name: str = "HOTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HOTBNB"

    def __str__(self):
        return "HOTBNB"

    def __call__(self):
        return "HOTBNB"


HOTBNB = HOTBNB()


@dataclass(slots=True, frozen=True)
class HOTBRL:
    name: str = "HOTBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HOTBRL"

    def __str__(self):
        return "HOTBRL"

    def __call__(self):
        return "HOTBRL"


HOTBRL = HOTBRL()


@dataclass(slots=True, frozen=True)
class HOTBTC:
    name: str = "HOTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HOTBTC"

    def __str__(self):
        return "HOTBTC"

    def __call__(self):
        return "HOTBTC"


HOTBTC = HOTBTC()


@dataclass(slots=True, frozen=True)
class HOTBUSD:
    name: str = "HOTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "HOTBUSD"

    def __str__(self):
        return "HOTBUSD"

    def __call__(self):
        return "HOTBUSD"


HOTBUSD = HOTBUSD()


@dataclass(slots=True, frozen=True)
class HOTETH:
    name: str = "HOTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HOTETH"

    def __str__(self):
        return "HOTETH"

    def __call__(self):
        return "HOTETH"


HOTETH = HOTETH()


@dataclass(slots=True, frozen=True)
class HOTEUR:
    name: str = "HOTEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HOTEUR"

    def __str__(self):
        return "HOTEUR"

    def __call__(self):
        return "HOTEUR"


HOTEUR = HOTEUR()


@dataclass(slots=True, frozen=True)
class HOTTRY:
    name: str = "HOTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HOTTRY"

    def __str__(self):
        return "HOTTRY"

    def __call__(self):
        return "HOTTRY"


HOTTRY = HOTTRY()


@dataclass(slots=True, frozen=True)
class HOTUSDT:
    name: str = "HOTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "HOTUSDT"

    def __str__(self):
        return "HOTUSDT"

    def __call__(self):
        return "HOTUSDT"


HOTUSDT = HOTUSDT()


@dataclass(slots=True, frozen=True)
class HSRBTC:
    name: str = "HSRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "HSRBTC"

    def __str__(self):
        return "HSRBTC"

    def __call__(self):
        return "HSRBTC"


HSRBTC = HSRBTC()


@dataclass(slots=True, frozen=True)
class HSRETH:
    name: str = "HSRETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "HSRETH"

    def __str__(self):
        return "HSRETH"

    def __call__(self):
        return "HSRETH"


HSRETH = HSRETH()


@dataclass(slots=True, frozen=True)
class ICNBTC:
    name: str = "ICNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ICNBTC"

    def __str__(self):
        return "ICNBTC"

    def __call__(self):
        return "ICNBTC"


ICNBTC = ICNBTC()


@dataclass(slots=True, frozen=True)
class ICNETH:
    name: str = "ICNETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ICNETH"

    def __str__(self):
        return "ICNETH"

    def __call__(self):
        return "ICNETH"


ICNETH = ICNETH()


@dataclass(slots=True, frozen=True)
class ICPBNB:
    name: str = "ICPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ICPBNB"

    def __str__(self):
        return "ICPBNB"

    def __call__(self):
        return "ICPBNB"


ICPBNB = ICPBNB()


@dataclass(slots=True, frozen=True)
class ICPBTC:
    name: str = "ICPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "ICPBTC"

    def __str__(self):
        return "ICPBTC"

    def __call__(self):
        return "ICPBTC"


ICPBTC = ICPBTC()


@dataclass(slots=True, frozen=True)
class ICPBUSD:
    name: str = "ICPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "ICPBUSD"

    def __str__(self):
        return "ICPBUSD"

    def __call__(self):
        return "ICPBUSD"


ICPBUSD = ICPBUSD()


@dataclass(slots=True, frozen=True)
class ICPETH:
    name: str = "ICPETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ICPETH"

    def __str__(self):
        return "ICPETH"

    def __call__(self):
        return "ICPETH"


ICPETH = ICPETH()


@dataclass(slots=True, frozen=True)
class ICPEUR:
    name: str = "ICPEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ICPEUR"

    def __str__(self):
        return "ICPEUR"

    def __call__(self):
        return "ICPEUR"


ICPEUR = ICPEUR()


@dataclass(slots=True, frozen=True)
class ICPRUB:
    name: str = "ICPRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "ICPRUB"

    def __str__(self):
        return "ICPRUB"

    def __call__(self):
        return "ICPRUB"


ICPRUB = ICPRUB()


@dataclass(slots=True, frozen=True)
class ICPTRY:
    name: str = "ICPTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ICPTRY"

    def __str__(self):
        return "ICPTRY"

    def __call__(self):
        return "ICPTRY"


ICPTRY = ICPTRY()


@dataclass(slots=True, frozen=True)
class ICPUSDT:
    name: str = "ICPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "ICPUSDT"

    def __str__(self):
        return "ICPUSDT"

    def __call__(self):
        return "ICPUSDT"


ICPUSDT = ICPUSDT()


@dataclass(slots=True, frozen=True)
class ICXBNB:
    name: str = "ICXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ICXBNB"

    def __str__(self):
        return "ICXBNB"

    def __call__(self):
        return "ICXBNB"


ICXBNB = ICXBNB()


@dataclass(slots=True, frozen=True)
class ICXBTC:
    name: str = "ICXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ICXBTC"

    def __str__(self):
        return "ICXBTC"

    def __call__(self):
        return "ICXBTC"


ICXBTC = ICXBTC()


@dataclass(slots=True, frozen=True)
class ICXBUSD:
    name: str = "ICXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ICXBUSD"

    def __str__(self):
        return "ICXBUSD"

    def __call__(self):
        return "ICXBUSD"


ICXBUSD = ICXBUSD()


@dataclass(slots=True, frozen=True)
class ICXETH:
    name: str = "ICXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ICXETH"

    def __str__(self):
        return "ICXETH"

    def __call__(self):
        return "ICXETH"


ICXETH = ICXETH()


@dataclass(slots=True, frozen=True)
class ICXUSDT:
    name: str = "ICXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ICXUSDT"

    def __str__(self):
        return "ICXUSDT"

    def __call__(self):
        return "ICXUSDT"


ICXUSDT = ICXUSDT()


@dataclass(slots=True, frozen=True)
class IDEXBNB:
    name: str = "IDEXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "IDEXBNB"

    def __str__(self):
        return "IDEXBNB"

    def __call__(self):
        return "IDEXBNB"


IDEXBNB = IDEXBNB()


@dataclass(slots=True, frozen=True)
class IDEXBTC:
    name: str = "IDEXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "IDEXBTC"

    def __str__(self):
        return "IDEXBTC"

    def __call__(self):
        return "IDEXBTC"


IDEXBTC = IDEXBTC()


@dataclass(slots=True, frozen=True)
class IDEXBUSD:
    name: str = "IDEXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "IDEXBUSD"

    def __str__(self):
        return "IDEXBUSD"

    def __call__(self):
        return "IDEXBUSD"


IDEXBUSD = IDEXBUSD()


@dataclass(slots=True, frozen=True)
class IDEXUSDT:
    name: str = "IDEXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = True

    def __repr__(self):
        return "IDEXUSDT"

    def __str__(self):
        return "IDEXUSDT"

    def __call__(self):
        return "IDEXUSDT"


IDEXUSDT = IDEXUSDT()


@dataclass(slots=True, frozen=True)
class ILVBNB:
    name: str = "ILVBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ILVBNB"

    def __str__(self):
        return "ILVBNB"

    def __call__(self):
        return "ILVBNB"


ILVBNB = ILVBNB()


@dataclass(slots=True, frozen=True)
class ILVBTC:
    name: str = "ILVBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ILVBTC"

    def __str__(self):
        return "ILVBTC"

    def __call__(self):
        return "ILVBTC"


ILVBTC = ILVBTC()


@dataclass(slots=True, frozen=True)
class ILVBUSD:
    name: str = "ILVBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ILVBUSD"

    def __str__(self):
        return "ILVBUSD"

    def __call__(self):
        return "ILVBUSD"


ILVBUSD = ILVBUSD()


@dataclass(slots=True, frozen=True)
class ILVUSDT:
    name: str = "ILVUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "ILVUSDT"

    def __str__(self):
        return "ILVUSDT"

    def __call__(self):
        return "ILVUSDT"


ILVUSDT = ILVUSDT()


@dataclass(slots=True, frozen=True)
class IMXBNB:
    name: str = "IMXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "IMXBNB"

    def __str__(self):
        return "IMXBNB"

    def __call__(self):
        return "IMXBNB"


IMXBNB = IMXBNB()


@dataclass(slots=True, frozen=True)
class IMXBTC:
    name: str = "IMXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "IMXBTC"

    def __str__(self):
        return "IMXBTC"

    def __call__(self):
        return "IMXBTC"


IMXBTC = IMXBTC()


@dataclass(slots=True, frozen=True)
class IMXBUSD:
    name: str = "IMXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "IMXBUSD"

    def __str__(self):
        return "IMXBUSD"

    def __call__(self):
        return "IMXBUSD"


IMXBUSD = IMXBUSD()


@dataclass(slots=True, frozen=True)
class IMXUSDT:
    name: str = "IMXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "IMXUSDT"

    def __str__(self):
        return "IMXUSDT"

    def __call__(self):
        return "IMXUSDT"


IMXUSDT = IMXUSDT()


@dataclass(slots=True, frozen=True)
class INJBNB:
    name: str = "INJBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "INJBNB"

    def __str__(self):
        return "INJBNB"

    def __call__(self):
        return "INJBNB"


INJBNB = INJBNB()


@dataclass(slots=True, frozen=True)
class INJBTC:
    name: str = "INJBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "INJBTC"

    def __str__(self):
        return "INJBTC"

    def __call__(self):
        return "INJBTC"


INJBTC = INJBTC()


@dataclass(slots=True, frozen=True)
class INJBUSD:
    name: str = "INJBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "INJBUSD"

    def __str__(self):
        return "INJBUSD"

    def __call__(self):
        return "INJBUSD"


INJBUSD = INJBUSD()


@dataclass(slots=True, frozen=True)
class INJTRY:
    name: str = "INJTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "INJTRY"

    def __str__(self):
        return "INJTRY"

    def __call__(self):
        return "INJTRY"


INJTRY = INJTRY()


@dataclass(slots=True, frozen=True)
class INJUSDT:
    name: str = "INJUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "INJUSDT"

    def __str__(self):
        return "INJUSDT"

    def __call__(self):
        return "INJUSDT"


INJUSDT = INJUSDT()


@dataclass(slots=True, frozen=True)
class INSBTC:
    name: str = "INSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "INSBTC"

    def __str__(self):
        return "INSBTC"

    def __call__(self):
        return "INSBTC"


INSBTC = INSBTC()


@dataclass(slots=True, frozen=True)
class INSETH:
    name: str = "INSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "INSETH"

    def __str__(self):
        return "INSETH"

    def __call__(self):
        return "INSETH"


INSETH = INSETH()


@dataclass(slots=True, frozen=True)
class IOSTBTC:
    name: str = "IOSTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "IOSTBTC"

    def __str__(self):
        return "IOSTBTC"

    def __call__(self):
        return "IOSTBTC"


IOSTBTC = IOSTBTC()


@dataclass(slots=True, frozen=True)
class IOSTBUSD:
    name: str = "IOSTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IOSTBUSD"

    def __str__(self):
        return "IOSTBUSD"

    def __call__(self):
        return "IOSTBUSD"


IOSTBUSD = IOSTBUSD()


@dataclass(slots=True, frozen=True)
class IOSTETH:
    name: str = "IOSTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IOSTETH"

    def __str__(self):
        return "IOSTETH"

    def __call__(self):
        return "IOSTETH"


IOSTETH = IOSTETH()


@dataclass(slots=True, frozen=True)
class IOSTUSDT:
    name: str = "IOSTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "IOSTUSDT"

    def __str__(self):
        return "IOSTUSDT"

    def __call__(self):
        return "IOSTUSDT"


IOSTUSDT = IOSTUSDT()


@dataclass(slots=True, frozen=True)
class IOTABNB:
    name: str = "IOTABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IOTABNB"

    def __str__(self):
        return "IOTABNB"

    def __call__(self):
        return "IOTABNB"


IOTABNB = IOTABNB()


@dataclass(slots=True, frozen=True)
class IOTABTC:
    name: str = "IOTABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "IOTABTC"

    def __str__(self):
        return "IOTABTC"

    def __call__(self):
        return "IOTABTC"


IOTABTC = IOTABTC()


@dataclass(slots=True, frozen=True)
class IOTABUSD:
    name: str = "IOTABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "IOTABUSD"

    def __str__(self):
        return "IOTABUSD"

    def __call__(self):
        return "IOTABUSD"


IOTABUSD = IOTABUSD()


@dataclass(slots=True, frozen=True)
class IOTAETH:
    name: str = "IOTAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IOTAETH"

    def __str__(self):
        return "IOTAETH"

    def __call__(self):
        return "IOTAETH"


IOTAETH = IOTAETH()


@dataclass(slots=True, frozen=True)
class IOTAUSDT:
    name: str = "IOTAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "IOTAUSDT"

    def __str__(self):
        return "IOTAUSDT"

    def __call__(self):
        return "IOTAUSDT"


IOTAUSDT = IOTAUSDT()


@dataclass(slots=True, frozen=True)
class IOTXBTC:
    name: str = "IOTXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "IOTXBTC"

    def __str__(self):
        return "IOTXBTC"

    def __call__(self):
        return "IOTXBTC"


IOTXBTC = IOTXBTC()


@dataclass(slots=True, frozen=True)
class IOTXBUSD:
    name: str = "IOTXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "IOTXBUSD"

    def __str__(self):
        return "IOTXBUSD"

    def __call__(self):
        return "IOTXBUSD"


IOTXBUSD = IOTXBUSD()


@dataclass(slots=True, frozen=True)
class IOTXETH:
    name: str = "IOTXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IOTXETH"

    def __str__(self):
        return "IOTXETH"

    def __call__(self):
        return "IOTXETH"


IOTXETH = IOTXETH()


@dataclass(slots=True, frozen=True)
class IOTXUSDT:
    name: str = "IOTXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "IOTXUSDT"

    def __str__(self):
        return "IOTXUSDT"

    def __call__(self):
        return "IOTXUSDT"


IOTXUSDT = IOTXUSDT()


@dataclass(slots=True, frozen=True)
class IQBNB:
    name: str = "IQBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IQBNB"

    def __str__(self):
        return "IQBNB"

    def __call__(self):
        return "IQBNB"


IQBNB = IQBNB()


@dataclass(slots=True, frozen=True)
class IQBUSD:
    name: str = "IQBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "IQBUSD"

    def __str__(self):
        return "IQBUSD"

    def __call__(self):
        return "IQBUSD"


IQBUSD = IQBUSD()


@dataclass(slots=True, frozen=True)
class IRISBNB:
    name: str = "IRISBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IRISBNB"

    def __str__(self):
        return "IRISBNB"

    def __call__(self):
        return "IRISBNB"


IRISBNB = IRISBNB()


@dataclass(slots=True, frozen=True)
class IRISBTC:
    name: str = "IRISBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IRISBTC"

    def __str__(self):
        return "IRISBTC"

    def __call__(self):
        return "IRISBTC"


IRISBTC = IRISBTC()


@dataclass(slots=True, frozen=True)
class IRISBUSD:
    name: str = "IRISBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IRISBUSD"

    def __str__(self):
        return "IRISBUSD"

    def __call__(self):
        return "IRISBUSD"


IRISBUSD = IRISBUSD()


@dataclass(slots=True, frozen=True)
class IRISUSDT:
    name: str = "IRISUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "IRISUSDT"

    def __str__(self):
        return "IRISUSDT"

    def __call__(self):
        return "IRISUSDT"


IRISUSDT = IRISUSDT()


@dataclass(slots=True, frozen=True)
class JASMYBNB:
    name: str = "JASMYBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "JASMYBNB"

    def __str__(self):
        return "JASMYBNB"

    def __call__(self):
        return "JASMYBNB"


JASMYBNB = JASMYBNB()


@dataclass(slots=True, frozen=True)
class JASMYBTC:
    name: str = "JASMYBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "JASMYBTC"

    def __str__(self):
        return "JASMYBTC"

    def __call__(self):
        return "JASMYBTC"


JASMYBTC = JASMYBTC()


@dataclass(slots=True, frozen=True)
class JASMYBUSD:
    name: str = "JASMYBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "JASMYBUSD"

    def __str__(self):
        return "JASMYBUSD"

    def __call__(self):
        return "JASMYBUSD"


JASMYBUSD = JASMYBUSD()


@dataclass(slots=True, frozen=True)
class JASMYETH:
    name: str = "JASMYETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "JASMYETH"

    def __str__(self):
        return "JASMYETH"

    def __call__(self):
        return "JASMYETH"


JASMYETH = JASMYETH()


@dataclass(slots=True, frozen=True)
class JASMYEUR:
    name: str = "JASMYEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "JASMYEUR"

    def __str__(self):
        return "JASMYEUR"

    def __call__(self):
        return "JASMYEUR"


JASMYEUR = JASMYEUR()


@dataclass(slots=True, frozen=True)
class JASMYTRY:
    name: str = "JASMYTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "JASMYTRY"

    def __str__(self):
        return "JASMYTRY"

    def __call__(self):
        return "JASMYTRY"


JASMYTRY = JASMYTRY()


@dataclass(slots=True, frozen=True)
class JASMYUSDT:
    name: str = "JASMYUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "JASMYUSDT"

    def __str__(self):
        return "JASMYUSDT"

    def __call__(self):
        return "JASMYUSDT"


JASMYUSDT = JASMYUSDT()


@dataclass(slots=True, frozen=True)
class JOEBTC:
    name: str = "JOEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "JOEBTC"

    def __str__(self):
        return "JOEBTC"

    def __call__(self):
        return "JOEBTC"


JOEBTC = JOEBTC()


@dataclass(slots=True, frozen=True)
class JOEBUSD:
    name: str = "JOEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "JOEBUSD"

    def __str__(self):
        return "JOEBUSD"

    def __call__(self):
        return "JOEBUSD"


JOEBUSD = JOEBUSD()


@dataclass(slots=True, frozen=True)
class JOEUSDT:
    name: str = "JOEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "JOEUSDT"

    def __str__(self):
        return "JOEUSDT"

    def __call__(self):
        return "JOEUSDT"


JOEUSDT = JOEUSDT()


@dataclass(slots=True, frozen=True)
class JSTBNB:
    name: str = "JSTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "JSTBNB"

    def __str__(self):
        return "JSTBNB"

    def __call__(self):
        return "JSTBNB"


JSTBNB = JSTBNB()


@dataclass(slots=True, frozen=True)
class JSTBTC:
    name: str = "JSTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "JSTBTC"

    def __str__(self):
        return "JSTBTC"

    def __call__(self):
        return "JSTBTC"


JSTBTC = JSTBTC()


@dataclass(slots=True, frozen=True)
class JSTBUSD:
    name: str = "JSTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "JSTBUSD"

    def __str__(self):
        return "JSTBUSD"

    def __call__(self):
        return "JSTBUSD"


JSTBUSD = JSTBUSD()


@dataclass(slots=True, frozen=True)
class JSTUSDT:
    name: str = "JSTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "JSTUSDT"

    def __str__(self):
        return "JSTUSDT"

    def __call__(self):
        return "JSTUSDT"


JSTUSDT = JSTUSDT()


@dataclass(slots=True, frozen=True)
class JUVBTC:
    name: str = "JUVBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "JUVBTC"

    def __str__(self):
        return "JUVBTC"

    def __call__(self):
        return "JUVBTC"


JUVBTC = JUVBTC()


@dataclass(slots=True, frozen=True)
class JUVBUSD:
    name: str = "JUVBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "JUVBUSD"

    def __str__(self):
        return "JUVBUSD"

    def __call__(self):
        return "JUVBUSD"


JUVBUSD = JUVBUSD()


@dataclass(slots=True, frozen=True)
class JUVUSDT:
    name: str = "JUVUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "JUVUSDT"

    def __str__(self):
        return "JUVUSDT"

    def __call__(self):
        return "JUVUSDT"


JUVUSDT = JUVUSDT()


@dataclass(slots=True, frozen=True)
class KAVABNB:
    name: str = "KAVABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "KAVABNB"

    def __str__(self):
        return "KAVABNB"

    def __call__(self):
        return "KAVABNB"


KAVABNB = KAVABNB()


@dataclass(slots=True, frozen=True)
class KAVABTC:
    name: str = "KAVABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "KAVABTC"

    def __str__(self):
        return "KAVABTC"

    def __call__(self):
        return "KAVABTC"


KAVABTC = KAVABTC()


@dataclass(slots=True, frozen=True)
class KAVABUSD:
    name: str = "KAVABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "KAVABUSD"

    def __str__(self):
        return "KAVABUSD"

    def __call__(self):
        return "KAVABUSD"


KAVABUSD = KAVABUSD()


@dataclass(slots=True, frozen=True)
class KAVAETH:
    name: str = "KAVAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KAVAETH"

    def __str__(self):
        return "KAVAETH"

    def __call__(self):
        return "KAVAETH"


KAVAETH = KAVAETH()


@dataclass(slots=True, frozen=True)
class KAVAUSDT:
    name: str = "KAVAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "KAVAUSDT"

    def __str__(self):
        return "KAVAUSDT"

    def __call__(self):
        return "KAVAUSDT"


KAVAUSDT = KAVAUSDT()


@dataclass(slots=True, frozen=True)
class KDABTC:
    name: str = "KDABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KDABTC"

    def __str__(self):
        return "KDABTC"

    def __call__(self):
        return "KDABTC"


KDABTC = KDABTC()


@dataclass(slots=True, frozen=True)
class KDABUSD:
    name: str = "KDABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "KDABUSD"

    def __str__(self):
        return "KDABUSD"

    def __call__(self):
        return "KDABUSD"


KDABUSD = KDABUSD()


@dataclass(slots=True, frozen=True)
class KDAUSDT:
    name: str = "KDAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "KDAUSDT"

    def __str__(self):
        return "KDAUSDT"

    def __call__(self):
        return "KDAUSDT"


KDAUSDT = KDAUSDT()


@dataclass(slots=True, frozen=True)
class KEEPBNB:
    name: str = "KEEPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "KEEPBNB"

    def __str__(self):
        return "KEEPBNB"

    def __call__(self):
        return "KEEPBNB"


KEEPBNB = KEEPBNB()


@dataclass(slots=True, frozen=True)
class KEEPBTC:
    name: str = "KEEPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KEEPBTC"

    def __str__(self):
        return "KEEPBTC"

    def __call__(self):
        return "KEEPBTC"


KEEPBTC = KEEPBTC()


@dataclass(slots=True, frozen=True)
class KEEPBUSD:
    name: str = "KEEPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "KEEPBUSD"

    def __str__(self):
        return "KEEPBUSD"

    def __call__(self):
        return "KEEPBUSD"


KEEPBUSD = KEEPBUSD()


@dataclass(slots=True, frozen=True)
class KEEPUSDT:
    name: str = "KEEPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "KEEPUSDT"

    def __str__(self):
        return "KEEPUSDT"

    def __call__(self):
        return "KEEPUSDT"


KEEPUSDT = KEEPUSDT()


@dataclass(slots=True, frozen=True)
class KEYBTC:
    name: str = "KEYBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KEYBTC"

    def __str__(self):
        return "KEYBTC"

    def __call__(self):
        return "KEYBTC"


KEYBTC = KEYBTC()


@dataclass(slots=True, frozen=True)
class KEYBUSD:
    name: str = "KEYBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KEYBUSD"

    def __str__(self):
        return "KEYBUSD"

    def __call__(self):
        return "KEYBUSD"


KEYBUSD = KEYBUSD()


@dataclass(slots=True, frozen=True)
class KEYETH:
    name: str = "KEYETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "KEYETH"

    def __str__(self):
        return "KEYETH"

    def __call__(self):
        return "KEYETH"


KEYETH = KEYETH()


@dataclass(slots=True, frozen=True)
class KEYUSDT:
    name: str = "KEYUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KEYUSDT"

    def __str__(self):
        return "KEYUSDT"

    def __call__(self):
        return "KEYUSDT"


KEYUSDT = KEYUSDT()


@dataclass(slots=True, frozen=True)
class KLAYBNB:
    name: str = "KLAYBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KLAYBNB"

    def __str__(self):
        return "KLAYBNB"

    def __call__(self):
        return "KLAYBNB"


KLAYBNB = KLAYBNB()


@dataclass(slots=True, frozen=True)
class KLAYBTC:
    name: str = "KLAYBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KLAYBTC"

    def __str__(self):
        return "KLAYBTC"

    def __call__(self):
        return "KLAYBTC"


KLAYBTC = KLAYBTC()


@dataclass(slots=True, frozen=True)
class KLAYBUSD:
    name: str = "KLAYBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "KLAYBUSD"

    def __str__(self):
        return "KLAYBUSD"

    def __call__(self):
        return "KLAYBUSD"


KLAYBUSD = KLAYBUSD()


@dataclass(slots=True, frozen=True)
class KLAYUSDT:
    name: str = "KLAYUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "KLAYUSDT"

    def __str__(self):
        return "KLAYUSDT"

    def __call__(self):
        return "KLAYUSDT"


KLAYUSDT = KLAYUSDT()


@dataclass(slots=True, frozen=True)
class KMDBTC:
    name: str = "KMDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "KMDBTC"

    def __str__(self):
        return "KMDBTC"

    def __call__(self):
        return "KMDBTC"


KMDBTC = KMDBTC()


@dataclass(slots=True, frozen=True)
class KMDBUSD:
    name: str = "KMDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "KMDBUSD"

    def __str__(self):
        return "KMDBUSD"

    def __call__(self):
        return "KMDBUSD"


KMDBUSD = KMDBUSD()


@dataclass(slots=True, frozen=True)
class KMDETH:
    name: str = "KMDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KMDETH"

    def __str__(self):
        return "KMDETH"

    def __call__(self):
        return "KMDETH"


KMDETH = KMDETH()


@dataclass(slots=True, frozen=True)
class KMDUSDT:
    name: str = "KMDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "KMDUSDT"

    def __str__(self):
        return "KMDUSDT"

    def __call__(self):
        return "KMDUSDT"


KMDUSDT = KMDUSDT()


@dataclass(slots=True, frozen=True)
class KNCBNB:
    name: str = "KNCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KNCBNB"

    def __str__(self):
        return "KNCBNB"

    def __call__(self):
        return "KNCBNB"


KNCBNB = KNCBNB()


@dataclass(slots=True, frozen=True)
class KNCBTC:
    name: str = "KNCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "KNCBTC"

    def __str__(self):
        return "KNCBTC"

    def __call__(self):
        return "KNCBTC"


KNCBTC = KNCBTC()


@dataclass(slots=True, frozen=True)
class KNCBUSD:
    name: str = "KNCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "KNCBUSD"

    def __str__(self):
        return "KNCBUSD"

    def __call__(self):
        return "KNCBUSD"


KNCBUSD = KNCBUSD()


@dataclass(slots=True, frozen=True)
class KNCETH:
    name: str = "KNCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "KNCETH"

    def __str__(self):
        return "KNCETH"

    def __call__(self):
        return "KNCETH"


KNCETH = KNCETH()


@dataclass(slots=True, frozen=True)
class KNCUSDT:
    name: str = "KNCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "KNCUSDT"

    def __str__(self):
        return "KNCUSDT"

    def __call__(self):
        return "KNCUSDT"


KNCUSDT = KNCUSDT()


@dataclass(slots=True, frozen=True)
class KP3RBNB:
    name: str = "KP3RBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "KP3RBNB"

    def __str__(self):
        return "KP3RBNB"

    def __call__(self):
        return "KP3RBNB"


KP3RBNB = KP3RBNB()


@dataclass(slots=True, frozen=True)
class KP3RBUSD:
    name: str = "KP3RBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "KP3RBUSD"

    def __str__(self):
        return "KP3RBUSD"

    def __call__(self):
        return "KP3RBUSD"


KP3RBUSD = KP3RBUSD()


@dataclass(slots=True, frozen=True)
class KP3RUSDT:
    name: str = "KP3RUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92230.00000000
    margin: bool = True

    def __repr__(self):
        return "KP3RUSDT"

    def __str__(self):
        return "KP3RUSDT"

    def __call__(self):
        return "KP3RUSDT"


KP3RUSDT = KP3RUSDT()


@dataclass(slots=True, frozen=True)
class KSMAUD:
    name: str = "KSMAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "KSMAUD"

    def __str__(self):
        return "KSMAUD"

    def __call__(self):
        return "KSMAUD"


KSMAUD = KSMAUD()


@dataclass(slots=True, frozen=True)
class KSMBNB:
    name: str = "KSMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "KSMBNB"

    def __str__(self):
        return "KSMBNB"

    def __call__(self):
        return "KSMBNB"


KSMBNB = KSMBNB()


@dataclass(slots=True, frozen=True)
class KSMBTC:
    name: str = "KSMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "KSMBTC"

    def __str__(self):
        return "KSMBTC"

    def __call__(self):
        return "KSMBTC"


KSMBTC = KSMBTC()


@dataclass(slots=True, frozen=True)
class KSMBUSD:
    name: str = "KSMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "KSMBUSD"

    def __str__(self):
        return "KSMBUSD"

    def __call__(self):
        return "KSMBUSD"


KSMBUSD = KSMBUSD()


@dataclass(slots=True, frozen=True)
class KSMETH:
    name: str = "KSMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "KSMETH"

    def __str__(self):
        return "KSMETH"

    def __call__(self):
        return "KSMETH"


KSMETH = KSMETH()


@dataclass(slots=True, frozen=True)
class KSMUSDT:
    name: str = "KSMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "KSMUSDT"

    def __str__(self):
        return "KSMUSDT"

    def __call__(self):
        return "KSMUSDT"


KSMUSDT = KSMUSDT()


@dataclass(slots=True, frozen=True)
class LAZIOBTC:
    name: str = "LAZIOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LAZIOBTC"

    def __str__(self):
        return "LAZIOBTC"

    def __call__(self):
        return "LAZIOBTC"


LAZIOBTC = LAZIOBTC()


@dataclass(slots=True, frozen=True)
class LAZIOBUSD:
    name: str = "LAZIOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "LAZIOBUSD"

    def __str__(self):
        return "LAZIOBUSD"

    def __call__(self):
        return "LAZIOBUSD"


LAZIOBUSD = LAZIOBUSD()


@dataclass(slots=True, frozen=True)
class LAZIOEUR:
    name: str = "LAZIOEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LAZIOEUR"

    def __str__(self):
        return "LAZIOEUR"

    def __call__(self):
        return "LAZIOEUR"


LAZIOEUR = LAZIOEUR()


@dataclass(slots=True, frozen=True)
class LAZIOTRY:
    name: str = "LAZIOTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LAZIOTRY"

    def __str__(self):
        return "LAZIOTRY"

    def __call__(self):
        return "LAZIOTRY"


LAZIOTRY = LAZIOTRY()


@dataclass(slots=True, frozen=True)
class LAZIOUSDT:
    name: str = "LAZIOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "LAZIOUSDT"

    def __str__(self):
        return "LAZIOUSDT"

    def __call__(self):
        return "LAZIOUSDT"


LAZIOUSDT = LAZIOUSDT()


@dataclass(slots=True, frozen=True)
class LDOBTC:
    name: str = "LDOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LDOBTC"

    def __str__(self):
        return "LDOBTC"

    def __call__(self):
        return "LDOBTC"


LDOBTC = LDOBTC()


@dataclass(slots=True, frozen=True)
class LDOBUSD:
    name: str = "LDOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "LDOBUSD"

    def __str__(self):
        return "LDOBUSD"

    def __call__(self):
        return "LDOBUSD"


LDOBUSD = LDOBUSD()


@dataclass(slots=True, frozen=True)
class LDOUSDT:
    name: str = "LDOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "LDOUSDT"

    def __str__(self):
        return "LDOUSDT"

    def __call__(self):
        return "LDOUSDT"


LDOUSDT = LDOUSDT()


@dataclass(slots=True, frozen=True)
class LENDBKRW:
    name: str = "LENDBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92232.00000000
    margin: bool = False

    def __repr__(self):
        return "LENDBKRW"

    def __str__(self):
        return "LENDBKRW"

    def __call__(self):
        return "LENDBKRW"


LENDBKRW = LENDBKRW()


@dataclass(slots=True, frozen=True)
class LENDBTC:
    name: str = "LENDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LENDBTC"

    def __str__(self):
        return "LENDBTC"

    def __call__(self):
        return "LENDBTC"


LENDBTC = LENDBTC()


@dataclass(slots=True, frozen=True)
class LENDBUSD:
    name: str = "LENDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "LENDBUSD"

    def __str__(self):
        return "LENDBUSD"

    def __call__(self):
        return "LENDBUSD"


LENDBUSD = LENDBUSD()


@dataclass(slots=True, frozen=True)
class LENDETH:
    name: str = "LENDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LENDETH"

    def __str__(self):
        return "LENDETH"

    def __call__(self):
        return "LENDETH"


LENDETH = LENDETH()


@dataclass(slots=True, frozen=True)
class LENDUSDT:
    name: str = "LENDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LENDUSDT"

    def __str__(self):
        return "LENDUSDT"

    def __call__(self):
        return "LENDUSDT"


LENDUSDT = LENDUSDT()


@dataclass(slots=True, frozen=True)
class LEVERBUSD:
    name: str = "LEVERBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = True

    def __repr__(self):
        return "LEVERBUSD"

    def __str__(self):
        return "LEVERBUSD"

    def __call__(self):
        return "LEVERBUSD"


LEVERBUSD = LEVERBUSD()


@dataclass(slots=True, frozen=True)
class LEVERUSDT:
    name: str = "LEVERUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = True

    def __repr__(self):
        return "LEVERUSDT"

    def __str__(self):
        return "LEVERUSDT"

    def __call__(self):
        return "LEVERUSDT"


LEVERUSDT = LEVERUSDT()


@dataclass(slots=True, frozen=True)
class LINABNB:
    name: str = "LINABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LINABNB"

    def __str__(self):
        return "LINABNB"

    def __call__(self):
        return "LINABNB"


LINABNB = LINABNB()


@dataclass(slots=True, frozen=True)
class LINABTC:
    name: str = "LINABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LINABTC"

    def __str__(self):
        return "LINABTC"

    def __call__(self):
        return "LINABTC"


LINABTC = LINABTC()


@dataclass(slots=True, frozen=True)
class LINABUSD:
    name: str = "LINABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "LINABUSD"

    def __str__(self):
        return "LINABUSD"

    def __call__(self):
        return "LINABUSD"


LINABUSD = LINABUSD()


@dataclass(slots=True, frozen=True)
class LINAUSDT:
    name: str = "LINAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "LINAUSDT"

    def __str__(self):
        return "LINAUSDT"

    def __call__(self):
        return "LINAUSDT"


LINAUSDT = LINAUSDT()


@dataclass(slots=True, frozen=True)
class LINKAUD:
    name: str = "LINKAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKAUD"

    def __str__(self):
        return "LINKAUD"

    def __call__(self):
        return "LINKAUD"


LINKAUD = LINKAUD()


@dataclass(slots=True, frozen=True)
class LINKBKRW:
    name: str = "LINKBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9200.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKBKRW"

    def __str__(self):
        return "LINKBKRW"

    def __call__(self):
        return "LINKBKRW"


LINKBKRW = LINKBKRW()


@dataclass(slots=True, frozen=True)
class LINKBNB:
    name: str = "LINKBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKBNB"

    def __str__(self):
        return "LINKBNB"

    def __call__(self):
        return "LINKBNB"


LINKBNB = LINKBNB()


@dataclass(slots=True, frozen=True)
class LINKBRL:
    name: str = "LINKBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 45000.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKBRL"

    def __str__(self):
        return "LINKBRL"

    def __call__(self):
        return "LINKBRL"


LINKBRL = LINKBRL()


@dataclass(slots=True, frozen=True)
class LINKBTC:
    name: str = "LINKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LINKBTC"

    def __str__(self):
        return "LINKBTC"

    def __call__(self):
        return "LINKBTC"


LINKBTC = LINKBTC()


@dataclass(slots=True, frozen=True)
class LINKBUSD:
    name: str = "LINKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "LINKBUSD"

    def __str__(self):
        return "LINKBUSD"

    def __call__(self):
        return "LINKBUSD"


LINKBUSD = LINKBUSD()


@dataclass(slots=True, frozen=True)
class LINKDOWNUSDT:
    name: str = "LINKDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 300000.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKDOWNUSDT"

    def __str__(self):
        return "LINKDOWNUSDT"

    def __call__(self):
        return "LINKDOWNUSDT"


LINKDOWNUSDT = LINKDOWNUSDT()


@dataclass(slots=True, frozen=True)
class LINKETH:
    name: str = "LINKETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "LINKETH"

    def __str__(self):
        return "LINKETH"

    def __call__(self):
        return "LINKETH"


LINKETH = LINKETH()


@dataclass(slots=True, frozen=True)
class LINKEUR:
    name: str = "LINKEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKEUR"

    def __str__(self):
        return "LINKEUR"

    def __call__(self):
        return "LINKEUR"


LINKEUR = LINKEUR()


@dataclass(slots=True, frozen=True)
class LINKGBP:
    name: str = "LINKGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKGBP"

    def __str__(self):
        return "LINKGBP"

    def __call__(self):
        return "LINKGBP"


LINKGBP = LINKGBP()


@dataclass(slots=True, frozen=True)
class LINKNGN:
    name: str = "LINKNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 92232.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKNGN"

    def __str__(self):
        return "LINKNGN"

    def __call__(self):
        return "LINKNGN"


LINKNGN = LINKNGN()


@dataclass(slots=True, frozen=True)
class LINKPAX:
    name: str = "LINKPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKPAX"

    def __str__(self):
        return "LINKPAX"

    def __call__(self):
        return "LINKPAX"


LINKPAX = LINKPAX()


@dataclass(slots=True, frozen=True)
class LINKTRY:
    name: str = "LINKTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKTRY"

    def __str__(self):
        return "LINKTRY"

    def __call__(self):
        return "LINKTRY"


LINKTRY = LINKTRY()


@dataclass(slots=True, frozen=True)
class LINKTUSD:
    name: str = "LINKTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKTUSD"

    def __str__(self):
        return "LINKTUSD"

    def __call__(self):
        return "LINKTUSD"


LINKTUSD = LINKTUSD()


@dataclass(slots=True, frozen=True)
class LINKUPUSDT:
    name: str = "LINKUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKUPUSDT"

    def __str__(self):
        return "LINKUPUSDT"

    def __call__(self):
        return "LINKUPUSDT"


LINKUPUSDT = LINKUPUSDT()


@dataclass(slots=True, frozen=True)
class LINKUSDC:
    name: str = "LINKUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LINKUSDC"

    def __str__(self):
        return "LINKUSDC"

    def __call__(self):
        return "LINKUSDC"


LINKUSDC = LINKUSDC()


@dataclass(slots=True, frozen=True)
class LINKUSDT:
    name: str = "LINKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "LINKUSDT"

    def __str__(self):
        return "LINKUSDT"

    def __call__(self):
        return "LINKUSDT"


LINKUSDT = LINKUSDT()


@dataclass(slots=True, frozen=True)
class LITBTC:
    name: str = "LITBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LITBTC"

    def __str__(self):
        return "LITBTC"

    def __call__(self):
        return "LITBTC"


LITBTC = LITBTC()


@dataclass(slots=True, frozen=True)
class LITBUSD:
    name: str = "LITBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "LITBUSD"

    def __str__(self):
        return "LITBUSD"

    def __call__(self):
        return "LITBUSD"


LITBUSD = LITBUSD()


@dataclass(slots=True, frozen=True)
class LITETH:
    name: str = "LITETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LITETH"

    def __str__(self):
        return "LITETH"

    def __call__(self):
        return "LITETH"


LITETH = LITETH()


@dataclass(slots=True, frozen=True)
class LITUSDT:
    name: str = "LITUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "LITUSDT"

    def __str__(self):
        return "LITUSDT"

    def __call__(self):
        return "LITUSDT"


LITUSDT = LITUSDT()


@dataclass(slots=True, frozen=True)
class LOKABNB:
    name: str = "LOKABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LOKABNB"

    def __str__(self):
        return "LOKABNB"

    def __call__(self):
        return "LOKABNB"


LOKABNB = LOKABNB()


@dataclass(slots=True, frozen=True)
class LOKABTC:
    name: str = "LOKABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LOKABTC"

    def __str__(self):
        return "LOKABTC"

    def __call__(self):
        return "LOKABTC"


LOKABTC = LOKABTC()


@dataclass(slots=True, frozen=True)
class LOKABUSD:
    name: str = "LOKABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LOKABUSD"

    def __str__(self):
        return "LOKABUSD"

    def __call__(self):
        return "LOKABUSD"


LOKABUSD = LOKABUSD()


@dataclass(slots=True, frozen=True)
class LOKAUSDT:
    name: str = "LOKAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LOKAUSDT"

    def __str__(self):
        return "LOKAUSDT"

    def __call__(self):
        return "LOKAUSDT"


LOKAUSDT = LOKAUSDT()


@dataclass(slots=True, frozen=True)
class LOOMBNB:
    name: str = "LOOMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LOOMBNB"

    def __str__(self):
        return "LOOMBNB"

    def __call__(self):
        return "LOOMBNB"


LOOMBNB = LOOMBNB()


@dataclass(slots=True, frozen=True)
class LOOMBTC:
    name: str = "LOOMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LOOMBTC"

    def __str__(self):
        return "LOOMBTC"

    def __call__(self):
        return "LOOMBTC"


LOOMBTC = LOOMBTC()


@dataclass(slots=True, frozen=True)
class LOOMBUSD:
    name: str = "LOOMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "LOOMBUSD"

    def __str__(self):
        return "LOOMBUSD"

    def __call__(self):
        return "LOOMBUSD"


LOOMBUSD = LOOMBUSD()


@dataclass(slots=True, frozen=True)
class LOOMETH:
    name: str = "LOOMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LOOMETH"

    def __str__(self):
        return "LOOMETH"

    def __call__(self):
        return "LOOMETH"


LOOMETH = LOOMETH()


@dataclass(slots=True, frozen=True)
class LPTBNB:
    name: str = "LPTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141570.00000000
    margin: bool = False

    def __repr__(self):
        return "LPTBNB"

    def __str__(self):
        return "LPTBNB"

    def __call__(self):
        return "LPTBNB"


LPTBNB = LPTBNB()


@dataclass(slots=True, frozen=True)
class LPTBTC:
    name: str = "LPTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141570.00000000
    margin: bool = True

    def __repr__(self):
        return "LPTBTC"

    def __str__(self):
        return "LPTBTC"

    def __call__(self):
        return "LPTBTC"


LPTBTC = LPTBTC()


@dataclass(slots=True, frozen=True)
class LPTBUSD:
    name: str = "LPTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222440.00000000
    margin: bool = True

    def __repr__(self):
        return "LPTBUSD"

    def __str__(self):
        return "LPTBUSD"

    def __call__(self):
        return "LPTBUSD"


LPTBUSD = LPTBUSD()


@dataclass(slots=True, frozen=True)
class LPTUSDT:
    name: str = "LPTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222440.00000000
    margin: bool = True

    def __repr__(self):
        return "LPTUSDT"

    def __str__(self):
        return "LPTUSDT"

    def __call__(self):
        return "LPTUSDT"


LPTUSDT = LPTUSDT()


@dataclass(slots=True, frozen=True)
class LRCBNB:
    name: str = "LRCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LRCBNB"

    def __str__(self):
        return "LRCBNB"

    def __call__(self):
        return "LRCBNB"


LRCBNB = LRCBNB()


@dataclass(slots=True, frozen=True)
class LRCBTC:
    name: str = "LRCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LRCBTC"

    def __str__(self):
        return "LRCBTC"

    def __call__(self):
        return "LRCBTC"


LRCBTC = LRCBTC()


@dataclass(slots=True, frozen=True)
class LRCBUSD:
    name: str = "LRCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LRCBUSD"

    def __str__(self):
        return "LRCBUSD"

    def __call__(self):
        return "LRCBUSD"


LRCBUSD = LRCBUSD()


@dataclass(slots=True, frozen=True)
class LRCETH:
    name: str = "LRCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LRCETH"

    def __str__(self):
        return "LRCETH"

    def __call__(self):
        return "LRCETH"


LRCETH = LRCETH()


@dataclass(slots=True, frozen=True)
class LRCTRY:
    name: str = "LRCTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "LRCTRY"

    def __str__(self):
        return "LRCTRY"

    def __call__(self):
        return "LRCTRY"


LRCTRY = LRCTRY()


@dataclass(slots=True, frozen=True)
class LRCUSDT:
    name: str = "LRCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LRCUSDT"

    def __str__(self):
        return "LRCUSDT"

    def __call__(self):
        return "LRCUSDT"


LRCUSDT = LRCUSDT()


@dataclass(slots=True, frozen=True)
class LSKBNB:
    name: str = "LSKBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LSKBNB"

    def __str__(self):
        return "LSKBNB"

    def __call__(self):
        return "LSKBNB"


LSKBNB = LSKBNB()


@dataclass(slots=True, frozen=True)
class LSKBTC:
    name: str = "LSKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LSKBTC"

    def __str__(self):
        return "LSKBTC"

    def __call__(self):
        return "LSKBTC"


LSKBTC = LSKBTC()


@dataclass(slots=True, frozen=True)
class LSKBUSD:
    name: str = "LSKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LSKBUSD"

    def __str__(self):
        return "LSKBUSD"

    def __call__(self):
        return "LSKBUSD"


LSKBUSD = LSKBUSD()


@dataclass(slots=True, frozen=True)
class LSKETH:
    name: str = "LSKETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LSKETH"

    def __str__(self):
        return "LSKETH"

    def __call__(self):
        return "LSKETH"


LSKETH = LSKETH()


@dataclass(slots=True, frozen=True)
class LSKUSDT:
    name: str = "LSKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "LSKUSDT"

    def __str__(self):
        return "LSKUSDT"

    def __call__(self):
        return "LSKUSDT"


LSKUSDT = LSKUSDT()


@dataclass(slots=True, frozen=True)
class LTCBNB:
    name: str = "LTCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCBNB"

    def __str__(self):
        return "LTCBNB"

    def __call__(self):
        return "LTCBNB"


LTCBNB = LTCBNB()


@dataclass(slots=True, frozen=True)
class LTCBRL:
    name: str = "LTCBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 45000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCBRL"

    def __str__(self):
        return "LTCBRL"

    def __call__(self):
        return "LTCBRL"


LTCBRL = LTCBRL()


@dataclass(slots=True, frozen=True)
class LTCBTC:
    name: str = "LTCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 100000.00000000
    margin: bool = True

    def __repr__(self):
        return "LTCBTC"

    def __str__(self):
        return "LTCBTC"

    def __call__(self):
        return "LTCBTC"


LTCBTC = LTCBTC()


@dataclass(slots=True, frozen=True)
class LTCBUSD:
    name: str = "LTCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "LTCBUSD"

    def __str__(self):
        return "LTCBUSD"

    def __call__(self):
        return "LTCBUSD"


LTCBUSD = LTCBUSD()


@dataclass(slots=True, frozen=True)
class LTCDOWNUSDT:
    name: str = "LTCDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 610819340.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCDOWNUSDT"

    def __str__(self):
        return "LTCDOWNUSDT"

    def __call__(self):
        return "LTCDOWNUSDT"


LTCDOWNUSDT = LTCDOWNUSDT()


@dataclass(slots=True, frozen=True)
class LTCETH:
    name: str = "LTCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LTCETH"

    def __str__(self):
        return "LTCETH"

    def __call__(self):
        return "LTCETH"


LTCETH = LTCETH()


@dataclass(slots=True, frozen=True)
class LTCEUR:
    name: str = "LTCEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCEUR"

    def __str__(self):
        return "LTCEUR"

    def __call__(self):
        return "LTCEUR"


LTCEUR = LTCEUR()


@dataclass(slots=True, frozen=True)
class LTCGBP:
    name: str = "LTCGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCGBP"

    def __str__(self):
        return "LTCGBP"

    def __call__(self):
        return "LTCGBP"


LTCGBP = LTCGBP()


@dataclass(slots=True, frozen=True)
class LTCNGN:
    name: str = "LTCNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9221.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCNGN"

    def __str__(self):
        return "LTCNGN"

    def __call__(self):
        return "LTCNGN"


LTCNGN = LTCNGN()


@dataclass(slots=True, frozen=True)
class LTCPAX:
    name: str = "LTCPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCPAX"

    def __str__(self):
        return "LTCPAX"

    def __call__(self):
        return "LTCPAX"


LTCPAX = LTCPAX()


@dataclass(slots=True, frozen=True)
class LTCRUB:
    name: str = "LTCRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCRUB"

    def __str__(self):
        return "LTCRUB"

    def __call__(self):
        return "LTCRUB"


LTCRUB = LTCRUB()


@dataclass(slots=True, frozen=True)
class LTCTUSD:
    name: str = "LTCTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCTUSD"

    def __str__(self):
        return "LTCTUSD"

    def __call__(self):
        return "LTCTUSD"


LTCTUSD = LTCTUSD()


@dataclass(slots=True, frozen=True)
class LTCUAH:
    name: str = "LTCUAH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCUAH"

    def __str__(self):
        return "LTCUAH"

    def __call__(self):
        return "LTCUAH"


LTCUAH = LTCUAH()


@dataclass(slots=True, frozen=True)
class LTCUPUSDT:
    name: str = "LTCUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCUPUSDT"

    def __str__(self):
        return "LTCUPUSDT"

    def __call__(self):
        return "LTCUPUSDT"


LTCUPUSDT = LTCUPUSDT()


@dataclass(slots=True, frozen=True)
class LTCUSDC:
    name: str = "LTCUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTCUSDC"

    def __str__(self):
        return "LTCUSDC"

    def __call__(self):
        return "LTCUSDC"


LTCUSDC = LTCUSDC()


@dataclass(slots=True, frozen=True)
class LTCUSDT:
    name: str = "LTCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "LTCUSDT"

    def __str__(self):
        return "LTCUSDT"

    def __call__(self):
        return "LTCUSDT"


LTCUSDT = LTCUSDT()


@dataclass(slots=True, frozen=True)
class LTOBNB:
    name: str = "LTOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LTOBNB"

    def __str__(self):
        return "LTOBNB"

    def __call__(self):
        return "LTOBNB"


LTOBNB = LTOBNB()


@dataclass(slots=True, frozen=True)
class LTOBTC:
    name: str = "LTOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LTOBTC"

    def __str__(self):
        return "LTOBTC"

    def __call__(self):
        return "LTOBTC"


LTOBTC = LTOBTC()


@dataclass(slots=True, frozen=True)
class LTOBUSD:
    name: str = "LTOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LTOBUSD"

    def __str__(self):
        return "LTOBUSD"

    def __call__(self):
        return "LTOBUSD"


LTOBUSD = LTOBUSD()


@dataclass(slots=True, frozen=True)
class LTOUSDT:
    name: str = "LTOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LTOUSDT"

    def __str__(self):
        return "LTOUSDT"

    def __call__(self):
        return "LTOUSDT"


LTOUSDT = LTOUSDT()


@dataclass(slots=True, frozen=True)
class LUNAAUD:
    name: str = "LUNAAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNAAUD"

    def __str__(self):
        return "LUNAAUD"

    def __call__(self):
        return "LUNAAUD"


LUNAAUD = LUNAAUD()


@dataclass(slots=True, frozen=True)
class LUNABIDR:
    name: str = "LUNABIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922337194.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNABIDR"

    def __str__(self):
        return "LUNABIDR"

    def __call__(self):
        return "LUNABIDR"


LUNABIDR = LUNABIDR()


@dataclass(slots=True, frozen=True)
class LUNABNB:
    name: str = "LUNABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNABNB"

    def __str__(self):
        return "LUNABNB"

    def __call__(self):
        return "LUNABNB"


LUNABNB = LUNABNB()


@dataclass(slots=True, frozen=True)
class LUNABRL:
    name: str = "LUNABRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9221525.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNABRL"

    def __str__(self):
        return "LUNABRL"

    def __call__(self):
        return "LUNABRL"


LUNABRL = LUNABRL()


@dataclass(slots=True, frozen=True)
class LUNABTC:
    name: str = "LUNABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "LUNABTC"

    def __str__(self):
        return "LUNABTC"

    def __call__(self):
        return "LUNABTC"


LUNABTC = LUNABTC()


@dataclass(slots=True, frozen=True)
class LUNABUSD:
    name: str = "LUNABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "LUNABUSD"

    def __str__(self):
        return "LUNABUSD"

    def __call__(self):
        return "LUNABUSD"


LUNABUSD = LUNABUSD()


@dataclass(slots=True, frozen=True)
class LUNAETH:
    name: str = "LUNAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNAETH"

    def __str__(self):
        return "LUNAETH"

    def __call__(self):
        return "LUNAETH"


LUNAETH = LUNAETH()


@dataclass(slots=True, frozen=True)
class LUNAEUR:
    name: str = "LUNAEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNAEUR"

    def __str__(self):
        return "LUNAEUR"

    def __call__(self):
        return "LUNAEUR"


LUNAEUR = LUNAEUR()


@dataclass(slots=True, frozen=True)
class LUNAGBP:
    name: str = "LUNAGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNAGBP"

    def __str__(self):
        return "LUNAGBP"

    def __call__(self):
        return "LUNAGBP"


LUNAGBP = LUNAGBP()


@dataclass(slots=True, frozen=True)
class LUNATRY:
    name: str = "LUNATRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNATRY"

    def __str__(self):
        return "LUNATRY"

    def __call__(self):
        return "LUNATRY"


LUNATRY = LUNATRY()


@dataclass(slots=True, frozen=True)
class LUNAUSDT:
    name: str = "LUNAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "LUNAUSDT"

    def __str__(self):
        return "LUNAUSDT"

    def __call__(self):
        return "LUNAUSDT"


LUNAUSDT = LUNAUSDT()


@dataclass(slots=True, frozen=True)
class LUNAUST:
    name: str = "LUNAUST"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNAUST"

    def __str__(self):
        return "LUNAUST"

    def __call__(self):
        return "LUNAUST"


LUNAUST = LUNAUST()


@dataclass(slots=True, frozen=True)
class LUNBTC:
    name: str = "LUNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNBTC"

    def __str__(self):
        return "LUNBTC"

    def __call__(self):
        return "LUNBTC"


LUNBTC = LUNBTC()


@dataclass(slots=True, frozen=True)
class LUNCBUSD:
    name: str = "LUNCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 8384883677.00000000
    margin: bool = True

    def __repr__(self):
        return "LUNCBUSD"

    def __str__(self):
        return "LUNCBUSD"

    def __call__(self):
        return "LUNCBUSD"


LUNCBUSD = LUNCBUSD()


@dataclass(slots=True, frozen=True)
class LUNCUSDT:
    name: str = "LUNCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 8384883677.00000000
    margin: bool = True

    def __repr__(self):
        return "LUNCUSDT"

    def __str__(self):
        return "LUNCUSDT"

    def __call__(self):
        return "LUNCUSDT"


LUNCUSDT = LUNCUSDT()


@dataclass(slots=True, frozen=True)
class LUNETH:
    name: str = "LUNETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "LUNETH"

    def __str__(self):
        return "LUNETH"

    def __call__(self):
        return "LUNETH"


LUNETH = LUNETH()


@dataclass(slots=True, frozen=True)
class MAGICBTC:
    name: str = "MAGICBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MAGICBTC"

    def __str__(self):
        return "MAGICBTC"

    def __call__(self):
        return "MAGICBTC"


MAGICBTC = MAGICBTC()


@dataclass(slots=True, frozen=True)
class MAGICBUSD:
    name: str = "MAGICBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MAGICBUSD"

    def __str__(self):
        return "MAGICBUSD"

    def __call__(self):
        return "MAGICBUSD"


MAGICBUSD = MAGICBUSD()


@dataclass(slots=True, frozen=True)
class MAGICUSDT:
    name: str = "MAGICUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MAGICUSDT"

    def __str__(self):
        return "MAGICUSDT"

    def __call__(self):
        return "MAGICUSDT"


MAGICUSDT = MAGICUSDT()


@dataclass(slots=True, frozen=True)
class MANABIDR:
    name: str = "MANABIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9223371110.00000000
    margin: bool = False

    def __repr__(self):
        return "MANABIDR"

    def __str__(self):
        return "MANABIDR"

    def __call__(self):
        return "MANABIDR"


MANABIDR = MANABIDR()


@dataclass(slots=True, frozen=True)
class MANABNB:
    name: str = "MANABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MANABNB"

    def __str__(self):
        return "MANABNB"

    def __call__(self):
        return "MANABNB"


MANABNB = MANABNB()


@dataclass(slots=True, frozen=True)
class MANABRL:
    name: str = "MANABRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MANABRL"

    def __str__(self):
        return "MANABRL"

    def __call__(self):
        return "MANABRL"


MANABRL = MANABRL()


@dataclass(slots=True, frozen=True)
class MANABTC:
    name: str = "MANABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "MANABTC"

    def __str__(self):
        return "MANABTC"

    def __call__(self):
        return "MANABTC"


MANABTC = MANABTC()


@dataclass(slots=True, frozen=True)
class MANABUSD:
    name: str = "MANABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "MANABUSD"

    def __str__(self):
        return "MANABUSD"

    def __call__(self):
        return "MANABUSD"


MANABUSD = MANABUSD()


@dataclass(slots=True, frozen=True)
class MANAETH:
    name: str = "MANAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MANAETH"

    def __str__(self):
        return "MANAETH"

    def __call__(self):
        return "MANAETH"


MANAETH = MANAETH()


@dataclass(slots=True, frozen=True)
class MANATRY:
    name: str = "MANATRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MANATRY"

    def __str__(self):
        return "MANATRY"

    def __call__(self):
        return "MANATRY"


MANATRY = MANATRY()


@dataclass(slots=True, frozen=True)
class MANAUSDT:
    name: str = "MANAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "MANAUSDT"

    def __str__(self):
        return "MANAUSDT"

    def __call__(self):
        return "MANAUSDT"


MANAUSDT = MANAUSDT()


@dataclass(slots=True, frozen=True)
class MASKBNB:
    name: str = "MASKBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MASKBNB"

    def __str__(self):
        return "MASKBNB"

    def __call__(self):
        return "MASKBNB"


MASKBNB = MASKBNB()


@dataclass(slots=True, frozen=True)
class MASKBUSD:
    name: str = "MASKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "MASKBUSD"

    def __str__(self):
        return "MASKBUSD"

    def __call__(self):
        return "MASKBUSD"


MASKBUSD = MASKBUSD()


@dataclass(slots=True, frozen=True)
class MASKUSDT:
    name: str = "MASKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "MASKUSDT"

    def __str__(self):
        return "MASKUSDT"

    def __call__(self):
        return "MASKUSDT"


MASKUSDT = MASKUSDT()


@dataclass(slots=True, frozen=True)
class MATICAUD:
    name: str = "MATICAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MATICAUD"

    def __str__(self):
        return "MATICAUD"

    def __call__(self):
        return "MATICAUD"


MATICAUD = MATICAUD()


@dataclass(slots=True, frozen=True)
class MATICBIDR:
    name: str = "MATICBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 184467.00000000
    margin: bool = False

    def __repr__(self):
        return "MATICBIDR"

    def __str__(self):
        return "MATICBIDR"

    def __call__(self):
        return "MATICBIDR"


MATICBIDR = MATICBIDR()


@dataclass(slots=True, frozen=True)
class MATICBNB:
    name: str = "MATICBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MATICBNB"

    def __str__(self):
        return "MATICBNB"

    def __call__(self):
        return "MATICBNB"


MATICBNB = MATICBNB()


@dataclass(slots=True, frozen=True)
class MATICBRL:
    name: str = "MATICBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222440.00000000
    margin: bool = False

    def __repr__(self):
        return "MATICBRL"

    def __str__(self):
        return "MATICBRL"

    def __call__(self):
        return "MATICBRL"


MATICBRL = MATICBRL()


@dataclass(slots=True, frozen=True)
class MATICBTC:
    name: str = "MATICBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "MATICBTC"

    def __str__(self):
        return "MATICBTC"

    def __call__(self):
        return "MATICBTC"


MATICBTC = MATICBTC()


@dataclass(slots=True, frozen=True)
class MATICBUSD:
    name: str = "MATICBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "MATICBUSD"

    def __str__(self):
        return "MATICBUSD"

    def __call__(self):
        return "MATICBUSD"


MATICBUSD = MATICBUSD()


@dataclass(slots=True, frozen=True)
class MATICETH:
    name: str = "MATICETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MATICETH"

    def __str__(self):
        return "MATICETH"

    def __call__(self):
        return "MATICETH"


MATICETH = MATICETH()


@dataclass(slots=True, frozen=True)
class MATICEUR:
    name: str = "MATICEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "MATICEUR"

    def __str__(self):
        return "MATICEUR"

    def __call__(self):
        return "MATICEUR"


MATICEUR = MATICEUR()


@dataclass(slots=True, frozen=True)
class MATICGBP:
    name: str = "MATICGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MATICGBP"

    def __str__(self):
        return "MATICGBP"

    def __call__(self):
        return "MATICGBP"


MATICGBP = MATICGBP()


@dataclass(slots=True, frozen=True)
class MATICRUB:
    name: str = "MATICRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "MATICRUB"

    def __str__(self):
        return "MATICRUB"

    def __call__(self):
        return "MATICRUB"


MATICRUB = MATICRUB()


@dataclass(slots=True, frozen=True)
class MATICTRY:
    name: str = "MATICTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MATICTRY"

    def __str__(self):
        return "MATICTRY"

    def __call__(self):
        return "MATICTRY"


MATICTRY = MATICTRY()


@dataclass(slots=True, frozen=True)
class MATICUSDT:
    name: str = "MATICUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "MATICUSDT"

    def __str__(self):
        return "MATICUSDT"

    def __call__(self):
        return "MATICUSDT"


MATICUSDT = MATICUSDT()


@dataclass(slots=True, frozen=True)
class MBLBNB:
    name: str = "MBLBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MBLBNB"

    def __str__(self):
        return "MBLBNB"

    def __call__(self):
        return "MBLBNB"


MBLBNB = MBLBNB()


@dataclass(slots=True, frozen=True)
class MBLBTC:
    name: str = "MBLBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MBLBTC"

    def __str__(self):
        return "MBLBTC"

    def __call__(self):
        return "MBLBTC"


MBLBTC = MBLBTC()


@dataclass(slots=True, frozen=True)
class MBLBUSD:
    name: str = "MBLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "MBLBUSD"

    def __str__(self):
        return "MBLBUSD"

    def __call__(self):
        return "MBLBUSD"


MBLBUSD = MBLBUSD()


@dataclass(slots=True, frozen=True)
class MBLUSDT:
    name: str = "MBLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "MBLUSDT"

    def __str__(self):
        return "MBLUSDT"

    def __call__(self):
        return "MBLUSDT"


MBLUSDT = MBLUSDT()


@dataclass(slots=True, frozen=True)
class MBOXBNB:
    name: str = "MBOXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MBOXBNB"

    def __str__(self):
        return "MBOXBNB"

    def __call__(self):
        return "MBOXBNB"


MBOXBNB = MBOXBNB()


@dataclass(slots=True, frozen=True)
class MBOXBTC:
    name: str = "MBOXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MBOXBTC"

    def __str__(self):
        return "MBOXBTC"

    def __call__(self):
        return "MBOXBTC"


MBOXBTC = MBOXBTC()


@dataclass(slots=True, frozen=True)
class MBOXBUSD:
    name: str = "MBOXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MBOXBUSD"

    def __str__(self):
        return "MBOXBUSD"

    def __call__(self):
        return "MBOXBUSD"


MBOXBUSD = MBOXBUSD()


@dataclass(slots=True, frozen=True)
class MBOXTRY:
    name: str = "MBOXTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MBOXTRY"

    def __str__(self):
        return "MBOXTRY"

    def __call__(self):
        return "MBOXTRY"


MBOXTRY = MBOXTRY()


@dataclass(slots=True, frozen=True)
class MBOXUSDT:
    name: str = "MBOXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MBOXUSDT"

    def __str__(self):
        return "MBOXUSDT"

    def __call__(self):
        return "MBOXUSDT"


MBOXUSDT = MBOXUSDT()


@dataclass(slots=True, frozen=True)
class MCBNB:
    name: str = "MCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MCBNB"

    def __str__(self):
        return "MCBNB"

    def __call__(self):
        return "MCBNB"


MCBNB = MCBNB()


@dataclass(slots=True, frozen=True)
class MCBTC:
    name: str = "MCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MCBTC"

    def __str__(self):
        return "MCBTC"

    def __call__(self):
        return "MCBTC"


MCBTC = MCBTC()


@dataclass(slots=True, frozen=True)
class MCBUSD:
    name: str = "MCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MCBUSD"

    def __str__(self):
        return "MCBUSD"

    def __call__(self):
        return "MCBUSD"


MCBUSD = MCBUSD()


@dataclass(slots=True, frozen=True)
class MCOBNB:
    name: str = "MCOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MCOBNB"

    def __str__(self):
        return "MCOBNB"

    def __call__(self):
        return "MCOBNB"


MCOBNB = MCOBNB()


@dataclass(slots=True, frozen=True)
class MCOBTC:
    name: str = "MCOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MCOBTC"

    def __str__(self):
        return "MCOBTC"

    def __call__(self):
        return "MCOBTC"


MCOBTC = MCOBTC()


@dataclass(slots=True, frozen=True)
class MCOETH:
    name: str = "MCOETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MCOETH"

    def __str__(self):
        return "MCOETH"

    def __call__(self):
        return "MCOETH"


MCOETH = MCOETH()


@dataclass(slots=True, frozen=True)
class MCOUSDT:
    name: str = "MCOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "MCOUSDT"

    def __str__(self):
        return "MCOUSDT"

    def __call__(self):
        return "MCOUSDT"


MCOUSDT = MCOUSDT()


@dataclass(slots=True, frozen=True)
class MCUSDT:
    name: str = "MCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MCUSDT"

    def __str__(self):
        return "MCUSDT"

    def __call__(self):
        return "MCUSDT"


MCUSDT = MCUSDT()


@dataclass(slots=True, frozen=True)
class MDABTC:
    name: str = "MDABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MDABTC"

    def __str__(self):
        return "MDABTC"

    def __call__(self):
        return "MDABTC"


MDABTC = MDABTC()


@dataclass(slots=True, frozen=True)
class MDAETH:
    name: str = "MDAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MDAETH"

    def __str__(self):
        return "MDAETH"

    def __call__(self):
        return "MDAETH"


MDAETH = MDAETH()


@dataclass(slots=True, frozen=True)
class MDTBNB:
    name: str = "MDTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MDTBNB"

    def __str__(self):
        return "MDTBNB"

    def __call__(self):
        return "MDTBNB"


MDTBNB = MDTBNB()


@dataclass(slots=True, frozen=True)
class MDTBTC:
    name: str = "MDTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MDTBTC"

    def __str__(self):
        return "MDTBTC"

    def __call__(self):
        return "MDTBTC"


MDTBTC = MDTBTC()


@dataclass(slots=True, frozen=True)
class MDTBUSD:
    name: str = "MDTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MDTBUSD"

    def __str__(self):
        return "MDTBUSD"

    def __call__(self):
        return "MDTBUSD"


MDTBUSD = MDTBUSD()


@dataclass(slots=True, frozen=True)
class MDTUSDT:
    name: str = "MDTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MDTUSDT"

    def __str__(self):
        return "MDTUSDT"

    def __call__(self):
        return "MDTUSDT"


MDTUSDT = MDTUSDT()


@dataclass(slots=True, frozen=True)
class MDXBNB:
    name: str = "MDXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MDXBNB"

    def __str__(self):
        return "MDXBNB"

    def __call__(self):
        return "MDXBNB"


MDXBNB = MDXBNB()


@dataclass(slots=True, frozen=True)
class MDXBTC:
    name: str = "MDXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "MDXBTC"

    def __str__(self):
        return "MDXBTC"

    def __call__(self):
        return "MDXBTC"


MDXBTC = MDXBTC()


@dataclass(slots=True, frozen=True)
class MDXBUSD:
    name: str = "MDXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "MDXBUSD"

    def __str__(self):
        return "MDXBUSD"

    def __call__(self):
        return "MDXBUSD"


MDXBUSD = MDXBUSD()


@dataclass(slots=True, frozen=True)
class MDXUSDT:
    name: str = "MDXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "MDXUSDT"

    def __str__(self):
        return "MDXUSDT"

    def __call__(self):
        return "MDXUSDT"


MDXUSDT = MDXUSDT()


@dataclass(slots=True, frozen=True)
class MFTBNB:
    name: str = "MFTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MFTBNB"

    def __str__(self):
        return "MFTBNB"

    def __call__(self):
        return "MFTBNB"


MFTBNB = MFTBNB()


@dataclass(slots=True, frozen=True)
class MFTBTC:
    name: str = "MFTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MFTBTC"

    def __str__(self):
        return "MFTBTC"

    def __call__(self):
        return "MFTBTC"


MFTBTC = MFTBTC()


@dataclass(slots=True, frozen=True)
class MFTETH:
    name: str = "MFTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MFTETH"

    def __str__(self):
        return "MFTETH"

    def __call__(self):
        return "MFTETH"


MFTETH = MFTETH()


@dataclass(slots=True, frozen=True)
class MFTUSDT:
    name: str = "MFTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MFTUSDT"

    def __str__(self):
        return "MFTUSDT"

    def __call__(self):
        return "MFTUSDT"


MFTUSDT = MFTUSDT()


@dataclass(slots=True, frozen=True)
class MINABNB:
    name: str = "MINABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MINABNB"

    def __str__(self):
        return "MINABNB"

    def __call__(self):
        return "MINABNB"


MINABNB = MINABNB()


@dataclass(slots=True, frozen=True)
class MINABTC:
    name: str = "MINABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "MINABTC"

    def __str__(self):
        return "MINABTC"

    def __call__(self):
        return "MINABTC"


MINABTC = MINABTC()


@dataclass(slots=True, frozen=True)
class MINABUSD:
    name: str = "MINABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "MINABUSD"

    def __str__(self):
        return "MINABUSD"

    def __call__(self):
        return "MINABUSD"


MINABUSD = MINABUSD()


@dataclass(slots=True, frozen=True)
class MINATRY:
    name: str = "MINATRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MINATRY"

    def __str__(self):
        return "MINATRY"

    def __call__(self):
        return "MINATRY"


MINATRY = MINATRY()


@dataclass(slots=True, frozen=True)
class MINAUSDT:
    name: str = "MINAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "MINAUSDT"

    def __str__(self):
        return "MINAUSDT"

    def __call__(self):
        return "MINAUSDT"


MINAUSDT = MINAUSDT()


@dataclass(slots=True, frozen=True)
class MIRBTC:
    name: str = "MIRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MIRBTC"

    def __str__(self):
        return "MIRBTC"

    def __call__(self):
        return "MIRBTC"


MIRBTC = MIRBTC()


@dataclass(slots=True, frozen=True)
class MIRBUSD:
    name: str = "MIRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "MIRBUSD"

    def __str__(self):
        return "MIRBUSD"

    def __call__(self):
        return "MIRBUSD"


MIRBUSD = MIRBUSD()


@dataclass(slots=True, frozen=True)
class MIRUSDT:
    name: str = "MIRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "MIRUSDT"

    def __str__(self):
        return "MIRUSDT"

    def __call__(self):
        return "MIRUSDT"


MIRUSDT = MIRUSDT()


@dataclass(slots=True, frozen=True)
class MITHBNB:
    name: str = "MITHBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MITHBNB"

    def __str__(self):
        return "MITHBNB"

    def __call__(self):
        return "MITHBNB"


MITHBNB = MITHBNB()


@dataclass(slots=True, frozen=True)
class MITHBTC:
    name: str = "MITHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MITHBTC"

    def __str__(self):
        return "MITHBTC"

    def __call__(self):
        return "MITHBTC"


MITHBTC = MITHBTC()


@dataclass(slots=True, frozen=True)
class MITHUSDT:
    name: str = "MITHUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MITHUSDT"

    def __str__(self):
        return "MITHUSDT"

    def __call__(self):
        return "MITHUSDT"


MITHUSDT = MITHUSDT()


@dataclass(slots=True, frozen=True)
class MKRBNB:
    name: str = "MKRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "MKRBNB"

    def __str__(self):
        return "MKRBNB"

    def __call__(self):
        return "MKRBNB"


MKRBNB = MKRBNB()


@dataclass(slots=True, frozen=True)
class MKRBTC:
    name: str = "MKRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "MKRBTC"

    def __str__(self):
        return "MKRBTC"

    def __call__(self):
        return "MKRBTC"


MKRBTC = MKRBTC()


@dataclass(slots=True, frozen=True)
class MKRBUSD:
    name: str = "MKRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "MKRBUSD"

    def __str__(self):
        return "MKRBUSD"

    def __call__(self):
        return "MKRBUSD"


MKRBUSD = MKRBUSD()


@dataclass(slots=True, frozen=True)
class MKRUSDT:
    name: str = "MKRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "MKRUSDT"

    def __str__(self):
        return "MKRUSDT"

    def __call__(self):
        return "MKRUSDT"


MKRUSDT = MKRUSDT()


@dataclass(slots=True, frozen=True)
class MLNBNB:
    name: str = "MLNBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MLNBNB"

    def __str__(self):
        return "MLNBNB"

    def __call__(self):
        return "MLNBNB"


MLNBNB = MLNBNB()


@dataclass(slots=True, frozen=True)
class MLNBTC:
    name: str = "MLNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "MLNBTC"

    def __str__(self):
        return "MLNBTC"

    def __call__(self):
        return "MLNBTC"


MLNBTC = MLNBTC()


@dataclass(slots=True, frozen=True)
class MLNBUSD:
    name: str = "MLNBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "MLNBUSD"

    def __str__(self):
        return "MLNBUSD"

    def __call__(self):
        return "MLNBUSD"


MLNBUSD = MLNBUSD()


@dataclass(slots=True, frozen=True)
class MLNUSDT:
    name: str = "MLNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "MLNUSDT"

    def __str__(self):
        return "MLNUSDT"

    def __call__(self):
        return "MLNUSDT"


MLNUSDT = MLNUSDT()


@dataclass(slots=True, frozen=True)
class MOBBTC:
    name: str = "MOBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MOBBTC"

    def __str__(self):
        return "MOBBTC"

    def __call__(self):
        return "MOBBTC"


MOBBTC = MOBBTC()


@dataclass(slots=True, frozen=True)
class MOBBUSD:
    name: str = "MOBBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MOBBUSD"

    def __str__(self):
        return "MOBBUSD"

    def __call__(self):
        return "MOBBUSD"


MOBBUSD = MOBBUSD()


@dataclass(slots=True, frozen=True)
class MOBUSDT:
    name: str = "MOBUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MOBUSDT"

    def __str__(self):
        return "MOBUSDT"

    def __call__(self):
        return "MOBUSDT"


MOBUSDT = MOBUSDT()


@dataclass(slots=True, frozen=True)
class MODBTC:
    name: str = "MODBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MODBTC"

    def __str__(self):
        return "MODBTC"

    def __call__(self):
        return "MODBTC"


MODBTC = MODBTC()


@dataclass(slots=True, frozen=True)
class MODETH:
    name: str = "MODETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MODETH"

    def __str__(self):
        return "MODETH"

    def __call__(self):
        return "MODETH"


MODETH = MODETH()


@dataclass(slots=True, frozen=True)
class MOVRBNB:
    name: str = "MOVRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MOVRBNB"

    def __str__(self):
        return "MOVRBNB"

    def __call__(self):
        return "MOVRBNB"


MOVRBNB = MOVRBNB()


@dataclass(slots=True, frozen=True)
class MOVRBTC:
    name: str = "MOVRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MOVRBTC"

    def __str__(self):
        return "MOVRBTC"

    def __call__(self):
        return "MOVRBTC"


MOVRBTC = MOVRBTC()


@dataclass(slots=True, frozen=True)
class MOVRBUSD:
    name: str = "MOVRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "MOVRBUSD"

    def __str__(self):
        return "MOVRBUSD"

    def __call__(self):
        return "MOVRBUSD"


MOVRBUSD = MOVRBUSD()


@dataclass(slots=True, frozen=True)
class MOVRUSDT:
    name: str = "MOVRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "MOVRUSDT"

    def __str__(self):
        return "MOVRUSDT"

    def __call__(self):
        return "MOVRUSDT"


MOVRUSDT = MOVRUSDT()


@dataclass(slots=True, frozen=True)
class MTHBTC:
    name: str = "MTHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MTHBTC"

    def __str__(self):
        return "MTHBTC"

    def __call__(self):
        return "MTHBTC"


MTHBTC = MTHBTC()


@dataclass(slots=True, frozen=True)
class MTHETH:
    name: str = "MTHETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "MTHETH"

    def __str__(self):
        return "MTHETH"

    def __call__(self):
        return "MTHETH"


MTHETH = MTHETH()


@dataclass(slots=True, frozen=True)
class MTLBTC:
    name: str = "MTLBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "MTLBTC"

    def __str__(self):
        return "MTLBTC"

    def __call__(self):
        return "MTLBTC"


MTLBTC = MTLBTC()


@dataclass(slots=True, frozen=True)
class MTLBUSD:
    name: str = "MTLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "MTLBUSD"

    def __str__(self):
        return "MTLBUSD"

    def __call__(self):
        return "MTLBUSD"


MTLBUSD = MTLBUSD()


@dataclass(slots=True, frozen=True)
class MTLETH:
    name: str = "MTLETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MTLETH"

    def __str__(self):
        return "MTLETH"

    def __call__(self):
        return "MTLETH"


MTLETH = MTLETH()


@dataclass(slots=True, frozen=True)
class MTLUSDT:
    name: str = "MTLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "MTLUSDT"

    def __str__(self):
        return "MTLUSDT"

    def __call__(self):
        return "MTLUSDT"


MTLUSDT = MTLUSDT()


@dataclass(slots=True, frozen=True)
class MULTIBTC:
    name: str = "MULTIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "MULTIBTC"

    def __str__(self):
        return "MULTIBTC"

    def __call__(self):
        return "MULTIBTC"


MULTIBTC = MULTIBTC()


@dataclass(slots=True, frozen=True)
class MULTIBUSD:
    name: str = "MULTIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MULTIBUSD"

    def __str__(self):
        return "MULTIBUSD"

    def __call__(self):
        return "MULTIBUSD"


MULTIBUSD = MULTIBUSD()


@dataclass(slots=True, frozen=True)
class MULTIUSDT:
    name: str = "MULTIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "MULTIUSDT"

    def __str__(self):
        return "MULTIUSDT"

    def __call__(self):
        return "MULTIUSDT"


MULTIUSDT = MULTIUSDT()


@dataclass(slots=True, frozen=True)
class NANOBNB:
    name: str = "NANOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NANOBNB"

    def __str__(self):
        return "NANOBNB"

    def __call__(self):
        return "NANOBNB"


NANOBNB = NANOBNB()


@dataclass(slots=True, frozen=True)
class NANOBTC:
    name: str = "NANOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NANOBTC"

    def __str__(self):
        return "NANOBTC"

    def __call__(self):
        return "NANOBTC"


NANOBTC = NANOBTC()


@dataclass(slots=True, frozen=True)
class NANOBUSD:
    name: str = "NANOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "NANOBUSD"

    def __str__(self):
        return "NANOBUSD"

    def __call__(self):
        return "NANOBUSD"


NANOBUSD = NANOBUSD()


@dataclass(slots=True, frozen=True)
class NANOETH:
    name: str = "NANOETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NANOETH"

    def __str__(self):
        return "NANOETH"

    def __call__(self):
        return "NANOETH"


NANOETH = NANOETH()


@dataclass(slots=True, frozen=True)
class NANOUSDT:
    name: str = "NANOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "NANOUSDT"

    def __str__(self):
        return "NANOUSDT"

    def __call__(self):
        return "NANOUSDT"


NANOUSDT = NANOUSDT()


@dataclass(slots=True, frozen=True)
class NASBNB:
    name: str = "NASBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NASBNB"

    def __str__(self):
        return "NASBNB"

    def __call__(self):
        return "NASBNB"


NASBNB = NASBNB()


@dataclass(slots=True, frozen=True)
class NASBTC:
    name: str = "NASBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NASBTC"

    def __str__(self):
        return "NASBTC"

    def __call__(self):
        return "NASBTC"


NASBTC = NASBTC()


@dataclass(slots=True, frozen=True)
class NASETH:
    name: str = "NASETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NASETH"

    def __str__(self):
        return "NASETH"

    def __call__(self):
        return "NASETH"


NASETH = NASETH()


@dataclass(slots=True, frozen=True)
class NAVBNB:
    name: str = "NAVBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NAVBNB"

    def __str__(self):
        return "NAVBNB"

    def __call__(self):
        return "NAVBNB"


NAVBNB = NAVBNB()


@dataclass(slots=True, frozen=True)
class NAVBTC:
    name: str = "NAVBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NAVBTC"

    def __str__(self):
        return "NAVBTC"

    def __call__(self):
        return "NAVBTC"


NAVBTC = NAVBTC()


@dataclass(slots=True, frozen=True)
class NAVETH:
    name: str = "NAVETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NAVETH"

    def __str__(self):
        return "NAVETH"

    def __call__(self):
        return "NAVETH"


NAVETH = NAVETH()


@dataclass(slots=True, frozen=True)
class NBSBTC:
    name: str = "NBSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NBSBTC"

    def __str__(self):
        return "NBSBTC"

    def __call__(self):
        return "NBSBTC"


NBSBTC = NBSBTC()


@dataclass(slots=True, frozen=True)
class NBSUSDT:
    name: str = "NBSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NBSUSDT"

    def __str__(self):
        return "NBSUSDT"

    def __call__(self):
        return "NBSUSDT"


NBSUSDT = NBSUSDT()


@dataclass(slots=True, frozen=True)
class NBTBIDR:
    name: str = "NBTBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92232700.00000000
    margin: bool = False

    def __repr__(self):
        return "NBTBIDR"

    def __str__(self):
        return "NBTBIDR"

    def __call__(self):
        return "NBTBIDR"


NBTBIDR = NBTBIDR()


@dataclass(slots=True, frozen=True)
class NBTUSDT:
    name: str = "NBTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NBTUSDT"

    def __str__(self):
        return "NBTUSDT"

    def __call__(self):
        return "NBTUSDT"


NBTUSDT = NBTUSDT()


@dataclass(slots=True, frozen=True)
class NCASHBNB:
    name: str = "NCASHBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "NCASHBNB"

    def __str__(self):
        return "NCASHBNB"

    def __call__(self):
        return "NCASHBNB"


NCASHBNB = NCASHBNB()


@dataclass(slots=True, frozen=True)
class NCASHBTC:
    name: str = "NCASHBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NCASHBTC"

    def __str__(self):
        return "NCASHBTC"

    def __call__(self):
        return "NCASHBTC"


NCASHBTC = NCASHBTC()


@dataclass(slots=True, frozen=True)
class NCASHETH:
    name: str = "NCASHETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NCASHETH"

    def __str__(self):
        return "NCASHETH"

    def __call__(self):
        return "NCASHETH"


NCASHETH = NCASHETH()


@dataclass(slots=True, frozen=True)
class NEARBNB:
    name: str = "NEARBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NEARBNB"

    def __str__(self):
        return "NEARBNB"

    def __call__(self):
        return "NEARBNB"


NEARBNB = NEARBNB()


@dataclass(slots=True, frozen=True)
class NEARBTC:
    name: str = "NEARBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "NEARBTC"

    def __str__(self):
        return "NEARBTC"

    def __call__(self):
        return "NEARBTC"


NEARBTC = NEARBTC()


@dataclass(slots=True, frozen=True)
class NEARBUSD:
    name: str = "NEARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "NEARBUSD"

    def __str__(self):
        return "NEARBUSD"

    def __call__(self):
        return "NEARBUSD"


NEARBUSD = NEARBUSD()


@dataclass(slots=True, frozen=True)
class NEARETH:
    name: str = "NEARETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NEARETH"

    def __str__(self):
        return "NEARETH"

    def __call__(self):
        return "NEARETH"


NEARETH = NEARETH()


@dataclass(slots=True, frozen=True)
class NEAREUR:
    name: str = "NEAREUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "NEAREUR"

    def __str__(self):
        return "NEAREUR"

    def __call__(self):
        return "NEAREUR"


NEAREUR = NEAREUR()


@dataclass(slots=True, frozen=True)
class NEARRUB:
    name: str = "NEARRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "NEARRUB"

    def __str__(self):
        return "NEARRUB"

    def __call__(self):
        return "NEARRUB"


NEARRUB = NEARRUB()


@dataclass(slots=True, frozen=True)
class NEARTRY:
    name: str = "NEARTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "NEARTRY"

    def __str__(self):
        return "NEARTRY"

    def __call__(self):
        return "NEARTRY"


NEARTRY = NEARTRY()


@dataclass(slots=True, frozen=True)
class NEARUSDT:
    name: str = "NEARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "NEARUSDT"

    def __str__(self):
        return "NEARUSDT"

    def __call__(self):
        return "NEARUSDT"


NEARUSDT = NEARUSDT()


@dataclass(slots=True, frozen=True)
class NEBLBNB:
    name: str = "NEBLBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NEBLBNB"

    def __str__(self):
        return "NEBLBNB"

    def __call__(self):
        return "NEBLBNB"


NEBLBNB = NEBLBNB()


@dataclass(slots=True, frozen=True)
class NEBLBTC:
    name: str = "NEBLBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NEBLBTC"

    def __str__(self):
        return "NEBLBTC"

    def __call__(self):
        return "NEBLBTC"


NEBLBTC = NEBLBTC()


@dataclass(slots=True, frozen=True)
class NEBLBUSD:
    name: str = "NEBLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "NEBLBUSD"

    def __str__(self):
        return "NEBLBUSD"

    def __call__(self):
        return "NEBLBUSD"


NEBLBUSD = NEBLBUSD()


@dataclass(slots=True, frozen=True)
class NEBLUSDT:
    name: str = "NEBLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NEBLUSDT"

    def __str__(self):
        return "NEBLUSDT"

    def __call__(self):
        return "NEBLUSDT"


NEBLUSDT = NEBLUSDT()


@dataclass(slots=True, frozen=True)
class NEOBNB:
    name: str = "NEOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "NEOBNB"

    def __str__(self):
        return "NEOBNB"

    def __call__(self):
        return "NEOBNB"


NEOBNB = NEOBNB()


@dataclass(slots=True, frozen=True)
class NEOBTC:
    name: str = "NEOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000.00000000
    margin: bool = True

    def __repr__(self):
        return "NEOBTC"

    def __str__(self):
        return "NEOBTC"

    def __call__(self):
        return "NEOBTC"


NEOBTC = NEOBTC()


@dataclass(slots=True, frozen=True)
class NEOBUSD:
    name: str = "NEOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "NEOBUSD"

    def __str__(self):
        return "NEOBUSD"

    def __call__(self):
        return "NEOBUSD"


NEOBUSD = NEOBUSD()


@dataclass(slots=True, frozen=True)
class NEOETH:
    name: str = "NEOETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NEOETH"

    def __str__(self):
        return "NEOETH"

    def __call__(self):
        return "NEOETH"


NEOETH = NEOETH()


@dataclass(slots=True, frozen=True)
class NEOPAX:
    name: str = "NEOPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "NEOPAX"

    def __str__(self):
        return "NEOPAX"

    def __call__(self):
        return "NEOPAX"


NEOPAX = NEOPAX()


@dataclass(slots=True, frozen=True)
class NEORUB:
    name: str = "NEORUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "NEORUB"

    def __str__(self):
        return "NEORUB"

    def __call__(self):
        return "NEORUB"


NEORUB = NEORUB()


@dataclass(slots=True, frozen=True)
class NEOTRY:
    name: str = "NEOTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "NEOTRY"

    def __str__(self):
        return "NEOTRY"

    def __call__(self):
        return "NEOTRY"


NEOTRY = NEOTRY()


@dataclass(slots=True, frozen=True)
class NEOTUSD:
    name: str = "NEOTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "NEOTUSD"

    def __str__(self):
        return "NEOTUSD"

    def __call__(self):
        return "NEOTUSD"


NEOTUSD = NEOTUSD()


@dataclass(slots=True, frozen=True)
class NEOUSDC:
    name: str = "NEOUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "NEOUSDC"

    def __str__(self):
        return "NEOUSDC"

    def __call__(self):
        return "NEOUSDC"


NEOUSDC = NEOUSDC()


@dataclass(slots=True, frozen=True)
class NEOUSDT:
    name: str = "NEOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "NEOUSDT"

    def __str__(self):
        return "NEOUSDT"

    def __call__(self):
        return "NEOUSDT"


NEOUSDT = NEOUSDT()


@dataclass(slots=True, frozen=True)
class NEXOBTC:
    name: str = "NEXOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NEXOBTC"

    def __str__(self):
        return "NEXOBTC"

    def __call__(self):
        return "NEXOBTC"


NEXOBTC = NEXOBTC()


@dataclass(slots=True, frozen=True)
class NEXOBUSD:
    name: str = "NEXOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "NEXOBUSD"

    def __str__(self):
        return "NEXOBUSD"

    def __call__(self):
        return "NEXOBUSD"


NEXOBUSD = NEXOBUSD()


@dataclass(slots=True, frozen=True)
class NEXOUSDT:
    name: str = "NEXOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "NEXOUSDT"

    def __str__(self):
        return "NEXOUSDT"

    def __call__(self):
        return "NEXOUSDT"


NEXOUSDT = NEXOUSDT()


@dataclass(slots=True, frozen=True)
class NKNBNB:
    name: str = "NKNBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NKNBNB"

    def __str__(self):
        return "NKNBNB"

    def __call__(self):
        return "NKNBNB"


NKNBNB = NKNBNB()


@dataclass(slots=True, frozen=True)
class NKNBTC:
    name: str = "NKNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "NKNBTC"

    def __str__(self):
        return "NKNBTC"

    def __call__(self):
        return "NKNBTC"


NKNBTC = NKNBTC()


@dataclass(slots=True, frozen=True)
class NKNBUSD:
    name: str = "NKNBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NKNBUSD"

    def __str__(self):
        return "NKNBUSD"

    def __call__(self):
        return "NKNBUSD"


NKNBUSD = NKNBUSD()


@dataclass(slots=True, frozen=True)
class NKNUSDT:
    name: str = "NKNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "NKNUSDT"

    def __str__(self):
        return "NKNUSDT"

    def __call__(self):
        return "NKNUSDT"


NKNUSDT = NKNUSDT()


@dataclass(slots=True, frozen=True)
class NMRBTC:
    name: str = "NMRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "NMRBTC"

    def __str__(self):
        return "NMRBTC"

    def __call__(self):
        return "NMRBTC"


NMRBTC = NMRBTC()


@dataclass(slots=True, frozen=True)
class NMRBUSD:
    name: str = "NMRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "NMRBUSD"

    def __str__(self):
        return "NMRBUSD"

    def __call__(self):
        return "NMRBUSD"


NMRBUSD = NMRBUSD()


@dataclass(slots=True, frozen=True)
class NMRUSDT:
    name: str = "NMRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "NMRUSDT"

    def __str__(self):
        return "NMRUSDT"

    def __call__(self):
        return "NMRUSDT"


NMRUSDT = NMRUSDT()


@dataclass(slots=True, frozen=True)
class NPXSBTC:
    name: str = "NPXSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NPXSBTC"

    def __str__(self):
        return "NPXSBTC"

    def __call__(self):
        return "NPXSBTC"


NPXSBTC = NPXSBTC()


@dataclass(slots=True, frozen=True)
class NPXSETH:
    name: str = "NPXSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NPXSETH"

    def __str__(self):
        return "NPXSETH"

    def __call__(self):
        return "NPXSETH"


NPXSETH = NPXSETH()


@dataclass(slots=True, frozen=True)
class NPXSUSDC:
    name: str = "NPXSUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NPXSUSDC"

    def __str__(self):
        return "NPXSUSDC"

    def __call__(self):
        return "NPXSUSDC"


NPXSUSDC = NPXSUSDC()


@dataclass(slots=True, frozen=True)
class NPXSUSDT:
    name: str = "NPXSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NPXSUSDT"

    def __str__(self):
        return "NPXSUSDT"

    def __call__(self):
        return "NPXSUSDT"


NPXSUSDT = NPXSUSDT()


@dataclass(slots=True, frozen=True)
class NUAUD:
    name: str = "NUAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NUAUD"

    def __str__(self):
        return "NUAUD"

    def __call__(self):
        return "NUAUD"


NUAUD = NUAUD()


@dataclass(slots=True, frozen=True)
class NUBNB:
    name: str = "NUBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NUBNB"

    def __str__(self):
        return "NUBNB"

    def __call__(self):
        return "NUBNB"


NUBNB = NUBNB()


@dataclass(slots=True, frozen=True)
class NUBTC:
    name: str = "NUBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NUBTC"

    def __str__(self):
        return "NUBTC"

    def __call__(self):
        return "NUBTC"


NUBTC = NUBTC()


@dataclass(slots=True, frozen=True)
class NUBUSD:
    name: str = "NUBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NUBUSD"

    def __str__(self):
        return "NUBUSD"

    def __call__(self):
        return "NUBUSD"


NUBUSD = NUBUSD()


@dataclass(slots=True, frozen=True)
class NULSBNB:
    name: str = "NULSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NULSBNB"

    def __str__(self):
        return "NULSBNB"

    def __call__(self):
        return "NULSBNB"


NULSBNB = NULSBNB()


@dataclass(slots=True, frozen=True)
class NULSBTC:
    name: str = "NULSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "NULSBTC"

    def __str__(self):
        return "NULSBTC"

    def __call__(self):
        return "NULSBTC"


NULSBTC = NULSBTC()


@dataclass(slots=True, frozen=True)
class NULSBUSD:
    name: str = "NULSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "NULSBUSD"

    def __str__(self):
        return "NULSBUSD"

    def __call__(self):
        return "NULSBUSD"


NULSBUSD = NULSBUSD()


@dataclass(slots=True, frozen=True)
class NULSETH:
    name: str = "NULSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NULSETH"

    def __str__(self):
        return "NULSETH"

    def __call__(self):
        return "NULSETH"


NULSETH = NULSETH()


@dataclass(slots=True, frozen=True)
class NULSUSDT:
    name: str = "NULSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "NULSUSDT"

    def __str__(self):
        return "NULSUSDT"

    def __call__(self):
        return "NULSUSDT"


NULSUSDT = NULSUSDT()


@dataclass(slots=True, frozen=True)
class NURUB:
    name: str = "NURUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "NURUB"

    def __str__(self):
        return "NURUB"

    def __call__(self):
        return "NURUB"


NURUB = NURUB()


@dataclass(slots=True, frozen=True)
class NUUSDT:
    name: str = "NUUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "NUUSDT"

    def __str__(self):
        return "NUUSDT"

    def __call__(self):
        return "NUUSDT"


NUUSDT = NUUSDT()


@dataclass(slots=True, frozen=True)
class NXSBNB:
    name: str = "NXSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NXSBNB"

    def __str__(self):
        return "NXSBNB"

    def __call__(self):
        return "NXSBNB"


NXSBNB = NXSBNB()


@dataclass(slots=True, frozen=True)
class NXSBTC:
    name: str = "NXSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NXSBTC"

    def __str__(self):
        return "NXSBTC"

    def __call__(self):
        return "NXSBTC"


NXSBTC = NXSBTC()


@dataclass(slots=True, frozen=True)
class NXSETH:
    name: str = "NXSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "NXSETH"

    def __str__(self):
        return "NXSETH"

    def __call__(self):
        return "NXSETH"


NXSETH = NXSETH()


@dataclass(slots=True, frozen=True)
class OAXBTC:
    name: str = "OAXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OAXBTC"

    def __str__(self):
        return "OAXBTC"

    def __call__(self):
        return "OAXBTC"


OAXBTC = OAXBTC()


@dataclass(slots=True, frozen=True)
class OAXETH:
    name: str = "OAXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OAXETH"

    def __str__(self):
        return "OAXETH"

    def __call__(self):
        return "OAXETH"


OAXETH = OAXETH()


@dataclass(slots=True, frozen=True)
class OCEANBNB:
    name: str = "OCEANBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OCEANBNB"

    def __str__(self):
        return "OCEANBNB"

    def __call__(self):
        return "OCEANBNB"


OCEANBNB = OCEANBNB()


@dataclass(slots=True, frozen=True)
class OCEANBTC:
    name: str = "OCEANBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "OCEANBTC"

    def __str__(self):
        return "OCEANBTC"

    def __call__(self):
        return "OCEANBTC"


OCEANBTC = OCEANBTC()


@dataclass(slots=True, frozen=True)
class OCEANBUSD:
    name: str = "OCEANBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "OCEANBUSD"

    def __str__(self):
        return "OCEANBUSD"

    def __call__(self):
        return "OCEANBUSD"


OCEANBUSD = OCEANBUSD()


@dataclass(slots=True, frozen=True)
class OCEANUSDT:
    name: str = "OCEANUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "OCEANUSDT"

    def __str__(self):
        return "OCEANUSDT"

    def __call__(self):
        return "OCEANUSDT"


OCEANUSDT = OCEANUSDT()


@dataclass(slots=True, frozen=True)
class OGBTC:
    name: str = "OGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OGBTC"

    def __str__(self):
        return "OGBTC"

    def __call__(self):
        return "OGBTC"


OGBTC = OGBTC()


@dataclass(slots=True, frozen=True)
class OGBUSD:
    name: str = "OGBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "OGBUSD"

    def __str__(self):
        return "OGBUSD"

    def __call__(self):
        return "OGBUSD"


OGBUSD = OGBUSD()


@dataclass(slots=True, frozen=True)
class OGNBNB:
    name: str = "OGNBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OGNBNB"

    def __str__(self):
        return "OGNBNB"

    def __call__(self):
        return "OGNBNB"


OGNBNB = OGNBNB()


@dataclass(slots=True, frozen=True)
class OGNBTC:
    name: str = "OGNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "OGNBTC"

    def __str__(self):
        return "OGNBTC"

    def __call__(self):
        return "OGNBTC"


OGNBTC = OGNBTC()


@dataclass(slots=True, frozen=True)
class OGNBUSD:
    name: str = "OGNBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "OGNBUSD"

    def __str__(self):
        return "OGNBUSD"

    def __call__(self):
        return "OGNBUSD"


OGNBUSD = OGNBUSD()


@dataclass(slots=True, frozen=True)
class OGNUSDT:
    name: str = "OGNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "OGNUSDT"

    def __str__(self):
        return "OGNUSDT"

    def __call__(self):
        return "OGNUSDT"


OGNUSDT = OGNUSDT()


@dataclass(slots=True, frozen=True)
class OGUSDT:
    name: str = "OGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "OGUSDT"

    def __str__(self):
        return "OGUSDT"

    def __call__(self):
        return "OGUSDT"


OGUSDT = OGUSDT()


@dataclass(slots=True, frozen=True)
class OMBTC:
    name: str = "OMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "OMBTC"

    def __str__(self):
        return "OMBTC"

    def __call__(self):
        return "OMBTC"


OMBTC = OMBTC()


@dataclass(slots=True, frozen=True)
class OMBUSD:
    name: str = "OMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "OMBUSD"

    def __str__(self):
        return "OMBUSD"

    def __call__(self):
        return "OMBUSD"


OMBUSD = OMBUSD()


@dataclass(slots=True, frozen=True)
class OMGBNB:
    name: str = "OMGBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OMGBNB"

    def __str__(self):
        return "OMGBNB"

    def __call__(self):
        return "OMGBNB"


OMGBNB = OMGBNB()


@dataclass(slots=True, frozen=True)
class OMGBTC:
    name: str = "OMGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OMGBTC"

    def __str__(self):
        return "OMGBTC"

    def __call__(self):
        return "OMGBTC"


OMGBTC = OMGBTC()


@dataclass(slots=True, frozen=True)
class OMGBUSD:
    name: str = "OMGBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "OMGBUSD"

    def __str__(self):
        return "OMGBUSD"

    def __call__(self):
        return "OMGBUSD"


OMGBUSD = OMGBUSD()


@dataclass(slots=True, frozen=True)
class OMGETH:
    name: str = "OMGETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OMGETH"

    def __str__(self):
        return "OMGETH"

    def __call__(self):
        return "OMGETH"


OMGETH = OMGETH()


@dataclass(slots=True, frozen=True)
class OMGUSDT:
    name: str = "OMGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "OMGUSDT"

    def __str__(self):
        return "OMGUSDT"

    def __call__(self):
        return "OMGUSDT"


OMGUSDT = OMGUSDT()


@dataclass(slots=True, frozen=True)
class OMUSDT:
    name: str = "OMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "OMUSDT"

    def __str__(self):
        return "OMUSDT"

    def __call__(self):
        return "OMUSDT"


OMUSDT = OMUSDT()


@dataclass(slots=True, frozen=True)
class ONEBIDR:
    name: str = "ONEBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONEBIDR"

    def __str__(self):
        return "ONEBIDR"

    def __call__(self):
        return "ONEBIDR"


ONEBIDR = ONEBIDR()


@dataclass(slots=True, frozen=True)
class ONEBNB:
    name: str = "ONEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONEBNB"

    def __str__(self):
        return "ONEBNB"

    def __call__(self):
        return "ONEBNB"


ONEBNB = ONEBNB()


@dataclass(slots=True, frozen=True)
class ONEBTC:
    name: str = "ONEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ONEBTC"

    def __str__(self):
        return "ONEBTC"

    def __call__(self):
        return "ONEBTC"


ONEBTC = ONEBTC()


@dataclass(slots=True, frozen=True)
class ONEBUSD:
    name: str = "ONEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ONEBUSD"

    def __str__(self):
        return "ONEBUSD"

    def __call__(self):
        return "ONEBUSD"


ONEBUSD = ONEBUSD()


@dataclass(slots=True, frozen=True)
class ONEETH:
    name: str = "ONEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ONEETH"

    def __str__(self):
        return "ONEETH"

    def __call__(self):
        return "ONEETH"


ONEETH = ONEETH()


@dataclass(slots=True, frozen=True)
class ONEPAX:
    name: str = "ONEPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONEPAX"

    def __str__(self):
        return "ONEPAX"

    def __call__(self):
        return "ONEPAX"


ONEPAX = ONEPAX()


@dataclass(slots=True, frozen=True)
class ONETRY:
    name: str = "ONETRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ONETRY"

    def __str__(self):
        return "ONETRY"

    def __call__(self):
        return "ONETRY"


ONETRY = ONETRY()


@dataclass(slots=True, frozen=True)
class ONETUSD:
    name: str = "ONETUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONETUSD"

    def __str__(self):
        return "ONETUSD"

    def __call__(self):
        return "ONETUSD"


ONETUSD = ONETUSD()


@dataclass(slots=True, frozen=True)
class ONEUSDC:
    name: str = "ONEUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONEUSDC"

    def __str__(self):
        return "ONEUSDC"

    def __call__(self):
        return "ONEUSDC"


ONEUSDC = ONEUSDC()


@dataclass(slots=True, frozen=True)
class ONEUSDT:
    name: str = "ONEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ONEUSDT"

    def __str__(self):
        return "ONEUSDT"

    def __call__(self):
        return "ONEUSDT"


ONEUSDT = ONEUSDT()


@dataclass(slots=True, frozen=True)
class ONGBNB:
    name: str = "ONGBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONGBNB"

    def __str__(self):
        return "ONGBNB"

    def __call__(self):
        return "ONGBNB"


ONGBNB = ONGBNB()


@dataclass(slots=True, frozen=True)
class ONGBTC:
    name: str = "ONGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONGBTC"

    def __str__(self):
        return "ONGBTC"

    def __call__(self):
        return "ONGBTC"


ONGBTC = ONGBTC()


@dataclass(slots=True, frozen=True)
class ONGUSDT:
    name: str = "ONGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONGUSDT"

    def __str__(self):
        return "ONGUSDT"

    def __call__(self):
        return "ONGUSDT"


ONGUSDT = ONGUSDT()


@dataclass(slots=True, frozen=True)
class ONTBNB:
    name: str = "ONTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONTBNB"

    def __str__(self):
        return "ONTBNB"

    def __call__(self):
        return "ONTBNB"


ONTBNB = ONTBNB()


@dataclass(slots=True, frozen=True)
class ONTBTC:
    name: str = "ONTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ONTBTC"

    def __str__(self):
        return "ONTBTC"

    def __call__(self):
        return "ONTBTC"


ONTBTC = ONTBTC()


@dataclass(slots=True, frozen=True)
class ONTBUSD:
    name: str = "ONTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ONTBUSD"

    def __str__(self):
        return "ONTBUSD"

    def __call__(self):
        return "ONTBUSD"


ONTBUSD = ONTBUSD()


@dataclass(slots=True, frozen=True)
class ONTETH:
    name: str = "ONTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONTETH"

    def __str__(self):
        return "ONTETH"

    def __call__(self):
        return "ONTETH"


ONTETH = ONTETH()


@dataclass(slots=True, frozen=True)
class ONTPAX:
    name: str = "ONTPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONTPAX"

    def __str__(self):
        return "ONTPAX"

    def __call__(self):
        return "ONTPAX"


ONTPAX = ONTPAX()


@dataclass(slots=True, frozen=True)
class ONTTRY:
    name: str = "ONTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ONTTRY"

    def __str__(self):
        return "ONTTRY"

    def __call__(self):
        return "ONTTRY"


ONTTRY = ONTTRY()


@dataclass(slots=True, frozen=True)
class ONTUSDC:
    name: str = "ONTUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ONTUSDC"

    def __str__(self):
        return "ONTUSDC"

    def __call__(self):
        return "ONTUSDC"


ONTUSDC = ONTUSDC()


@dataclass(slots=True, frozen=True)
class ONTUSDT:
    name: str = "ONTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ONTUSDT"

    def __str__(self):
        return "ONTUSDT"

    def __call__(self):
        return "ONTUSDT"


ONTUSDT = ONTUSDT()


@dataclass(slots=True, frozen=True)
class OOKIBNB:
    name: str = "OOKIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "OOKIBNB"

    def __str__(self):
        return "OOKIBNB"

    def __call__(self):
        return "OOKIBNB"


OOKIBNB = OOKIBNB()


@dataclass(slots=True, frozen=True)
class OOKIBUSD:
    name: str = "OOKIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "OOKIBUSD"

    def __str__(self):
        return "OOKIBUSD"

    def __call__(self):
        return "OOKIBUSD"


OOKIBUSD = OOKIBUSD()


@dataclass(slots=True, frozen=True)
class OOKIETH:
    name: str = "OOKIETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "OOKIETH"

    def __str__(self):
        return "OOKIETH"

    def __call__(self):
        return "OOKIETH"


OOKIETH = OOKIETH()


@dataclass(slots=True, frozen=True)
class OOKIUSDT:
    name: str = "OOKIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "OOKIUSDT"

    def __str__(self):
        return "OOKIUSDT"

    def __call__(self):
        return "OOKIUSDT"


OOKIUSDT = OOKIUSDT()


@dataclass(slots=True, frozen=True)
class OPBNB:
    name: str = "OPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "OPBNB"

    def __str__(self):
        return "OPBNB"

    def __call__(self):
        return "OPBNB"


OPBNB = OPBNB()


@dataclass(slots=True, frozen=True)
class OPBTC:
    name: str = "OPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "OPBTC"

    def __str__(self):
        return "OPBTC"

    def __call__(self):
        return "OPBTC"


OPBTC = OPBTC()


@dataclass(slots=True, frozen=True)
class OPBUSD:
    name: str = "OPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "OPBUSD"

    def __str__(self):
        return "OPBUSD"

    def __call__(self):
        return "OPBUSD"


OPBUSD = OPBUSD()


@dataclass(slots=True, frozen=True)
class OPETH:
    name: str = "OPETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "OPETH"

    def __str__(self):
        return "OPETH"

    def __call__(self):
        return "OPETH"


OPETH = OPETH()


@dataclass(slots=True, frozen=True)
class OPEUR:
    name: str = "OPEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "OPEUR"

    def __str__(self):
        return "OPEUR"

    def __call__(self):
        return "OPEUR"


OPEUR = OPEUR()


@dataclass(slots=True, frozen=True)
class OPUSDT:
    name: str = "OPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "OPUSDT"

    def __str__(self):
        return "OPUSDT"

    def __call__(self):
        return "OPUSDT"


OPUSDT = OPUSDT()


@dataclass(slots=True, frozen=True)
class ORNBTC:
    name: str = "ORNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ORNBTC"

    def __str__(self):
        return "ORNBTC"

    def __call__(self):
        return "ORNBTC"


ORNBTC = ORNBTC()


@dataclass(slots=True, frozen=True)
class ORNBUSD:
    name: str = "ORNBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ORNBUSD"

    def __str__(self):
        return "ORNBUSD"

    def __call__(self):
        return "ORNBUSD"


ORNBUSD = ORNBUSD()


@dataclass(slots=True, frozen=True)
class ORNUSDT:
    name: str = "ORNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "ORNUSDT"

    def __str__(self):
        return "ORNUSDT"

    def __call__(self):
        return "ORNUSDT"


ORNUSDT = ORNUSDT()


@dataclass(slots=True, frozen=True)
class OSMOBTC:
    name: str = "OSMOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 8384883677.00000000
    margin: bool = False

    def __repr__(self):
        return "OSMOBTC"

    def __str__(self):
        return "OSMOBTC"

    def __call__(self):
        return "OSMOBTC"


OSMOBTC = OSMOBTC()


@dataclass(slots=True, frozen=True)
class OSMOBUSD:
    name: str = "OSMOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "OSMOBUSD"

    def __str__(self):
        return "OSMOBUSD"

    def __call__(self):
        return "OSMOBUSD"


OSMOBUSD = OSMOBUSD()


@dataclass(slots=True, frozen=True)
class OSMOUSDT:
    name: str = "OSMOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "OSMOUSDT"

    def __str__(self):
        return "OSMOUSDT"

    def __call__(self):
        return "OSMOUSDT"


OSMOUSDT = OSMOUSDT()


@dataclass(slots=True, frozen=True)
class OSTBNB:
    name: str = "OSTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OSTBNB"

    def __str__(self):
        return "OSTBNB"

    def __call__(self):
        return "OSTBNB"


OSTBNB = OSTBNB()


@dataclass(slots=True, frozen=True)
class OSTBTC:
    name: str = "OSTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OSTBTC"

    def __str__(self):
        return "OSTBTC"

    def __call__(self):
        return "OSTBTC"


OSTBTC = OSTBTC()


@dataclass(slots=True, frozen=True)
class OSTETH:
    name: str = "OSTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "OSTETH"

    def __str__(self):
        return "OSTETH"

    def __call__(self):
        return "OSTETH"


OSTETH = OSTETH()


@dataclass(slots=True, frozen=True)
class OXTBTC:
    name: str = "OXTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "OXTBTC"

    def __str__(self):
        return "OXTBTC"

    def __call__(self):
        return "OXTBTC"


OXTBTC = OXTBTC()


@dataclass(slots=True, frozen=True)
class OXTBUSD:
    name: str = "OXTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "OXTBUSD"

    def __str__(self):
        return "OXTBUSD"

    def __call__(self):
        return "OXTBUSD"


OXTBUSD = OXTBUSD()


@dataclass(slots=True, frozen=True)
class OXTUSDT:
    name: str = "OXTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "OXTUSDT"

    def __str__(self):
        return "OXTUSDT"

    def __call__(self):
        return "OXTUSDT"


OXTUSDT = OXTUSDT()


@dataclass(slots=True, frozen=True)
class PAXBNB:
    name: str = "PAXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PAXBNB"

    def __str__(self):
        return "PAXBNB"

    def __call__(self):
        return "PAXBNB"


PAXBNB = PAXBNB()


@dataclass(slots=True, frozen=True)
class PAXBTC:
    name: str = "PAXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PAXBTC"

    def __str__(self):
        return "PAXBTC"

    def __call__(self):
        return "PAXBTC"


PAXBTC = PAXBTC()


@dataclass(slots=True, frozen=True)
class PAXBUSD:
    name: str = "PAXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "PAXBUSD"

    def __str__(self):
        return "PAXBUSD"

    def __call__(self):
        return "PAXBUSD"


PAXBUSD = PAXBUSD()


@dataclass(slots=True, frozen=True)
class PAXETH:
    name: str = "PAXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PAXETH"

    def __str__(self):
        return "PAXETH"

    def __call__(self):
        return "PAXETH"


PAXETH = PAXETH()


@dataclass(slots=True, frozen=True)
class PAXGBNB:
    name: str = "PAXGBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "PAXGBNB"

    def __str__(self):
        return "PAXGBNB"

    def __call__(self):
        return "PAXGBNB"


PAXGBNB = PAXGBNB()


@dataclass(slots=True, frozen=True)
class PAXGBTC:
    name: str = "PAXGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "PAXGBTC"

    def __str__(self):
        return "PAXGBTC"

    def __call__(self):
        return "PAXGBTC"


PAXGBTC = PAXGBTC()


@dataclass(slots=True, frozen=True)
class PAXGBUSD:
    name: str = "PAXGBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9000.00000000
    margin: bool = True

    def __repr__(self):
        return "PAXGBUSD"

    def __str__(self):
        return "PAXGBUSD"

    def __call__(self):
        return "PAXGBUSD"


PAXGBUSD = PAXGBUSD()


@dataclass(slots=True, frozen=True)
class PAXGUSDT:
    name: str = "PAXGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9000.00000000
    margin: bool = True

    def __repr__(self):
        return "PAXGUSDT"

    def __str__(self):
        return "PAXGUSDT"

    def __call__(self):
        return "PAXGUSDT"


PAXGUSDT = PAXGUSDT()


@dataclass(slots=True, frozen=True)
class PAXTUSD:
    name: str = "PAXTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "PAXTUSD"

    def __str__(self):
        return "PAXTUSD"

    def __call__(self):
        return "PAXTUSD"


PAXTUSD = PAXTUSD()


@dataclass(slots=True, frozen=True)
class PAXUSDT:
    name: str = "PAXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "PAXUSDT"

    def __str__(self):
        return "PAXUSDT"

    def __call__(self):
        return "PAXUSDT"


PAXUSDT = PAXUSDT()


@dataclass(slots=True, frozen=True)
class PEOPLEBNB:
    name: str = "PEOPLEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PEOPLEBNB"

    def __str__(self):
        return "PEOPLEBNB"

    def __call__(self):
        return "PEOPLEBNB"


PEOPLEBNB = PEOPLEBNB()


@dataclass(slots=True, frozen=True)
class PEOPLEBTC:
    name: str = "PEOPLEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "PEOPLEBTC"

    def __str__(self):
        return "PEOPLEBTC"

    def __call__(self):
        return "PEOPLEBTC"


PEOPLEBTC = PEOPLEBTC()


@dataclass(slots=True, frozen=True)
class PEOPLEBUSD:
    name: str = "PEOPLEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "PEOPLEBUSD"

    def __str__(self):
        return "PEOPLEBUSD"

    def __call__(self):
        return "PEOPLEBUSD"


PEOPLEBUSD = PEOPLEBUSD()


@dataclass(slots=True, frozen=True)
class PEOPLEETH:
    name: str = "PEOPLEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PEOPLEETH"

    def __str__(self):
        return "PEOPLEETH"

    def __call__(self):
        return "PEOPLEETH"


PEOPLEETH = PEOPLEETH()


@dataclass(slots=True, frozen=True)
class PEOPLEUSDT:
    name: str = "PEOPLEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "PEOPLEUSDT"

    def __str__(self):
        return "PEOPLEUSDT"

    def __call__(self):
        return "PEOPLEUSDT"


PEOPLEUSDT = PEOPLEUSDT()


@dataclass(slots=True, frozen=True)
class PERLBNB:
    name: str = "PERLBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PERLBNB"

    def __str__(self):
        return "PERLBNB"

    def __call__(self):
        return "PERLBNB"


PERLBNB = PERLBNB()


@dataclass(slots=True, frozen=True)
class PERLBTC:
    name: str = "PERLBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PERLBTC"

    def __str__(self):
        return "PERLBTC"

    def __call__(self):
        return "PERLBTC"


PERLBTC = PERLBTC()


@dataclass(slots=True, frozen=True)
class PERLUSDC:
    name: str = "PERLUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PERLUSDC"

    def __str__(self):
        return "PERLUSDC"

    def __call__(self):
        return "PERLUSDC"


PERLUSDC = PERLUSDC()


@dataclass(slots=True, frozen=True)
class PERLUSDT:
    name: str = "PERLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PERLUSDT"

    def __str__(self):
        return "PERLUSDT"

    def __call__(self):
        return "PERLUSDT"


PERLUSDT = PERLUSDT()


@dataclass(slots=True, frozen=True)
class PERPBTC:
    name: str = "PERPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PERPBTC"

    def __str__(self):
        return "PERPBTC"

    def __call__(self):
        return "PERPBTC"


PERPBTC = PERPBTC()


@dataclass(slots=True, frozen=True)
class PERPBUSD:
    name: str = "PERPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "PERPBUSD"

    def __str__(self):
        return "PERPBUSD"

    def __call__(self):
        return "PERPBUSD"


PERPBUSD = PERPBUSD()


@dataclass(slots=True, frozen=True)
class PERPUSDT:
    name: str = "PERPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "PERPUSDT"

    def __str__(self):
        return "PERPUSDT"

    def __call__(self):
        return "PERPUSDT"


PERPUSDT = PERPUSDT()


@dataclass(slots=True, frozen=True)
class PHABTC:
    name: str = "PHABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PHABTC"

    def __str__(self):
        return "PHABTC"

    def __call__(self):
        return "PHABTC"


PHABTC = PHABTC()


@dataclass(slots=True, frozen=True)
class PHABUSD:
    name: str = "PHABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "PHABUSD"

    def __str__(self):
        return "PHABUSD"

    def __call__(self):
        return "PHABUSD"


PHABUSD = PHABUSD()


@dataclass(slots=True, frozen=True)
class PHAUSDT:
    name: str = "PHAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "PHAUSDT"

    def __str__(self):
        return "PHAUSDT"

    def __call__(self):
        return "PHAUSDT"


PHAUSDT = PHAUSDT()


@dataclass(slots=True, frozen=True)
class PHBBNB:
    name: str = "PHBBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PHBBNB"

    def __str__(self):
        return "PHBBNB"

    def __call__(self):
        return "PHBBNB"


PHBBNB = PHBBNB()


@dataclass(slots=True, frozen=True)
class PHBBTC:
    name: str = "PHBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PHBBTC"

    def __str__(self):
        return "PHBBTC"

    def __call__(self):
        return "PHBBTC"


PHBBTC = PHBBTC()


@dataclass(slots=True, frozen=True)
class PHBBUSD:
    name: str = "PHBBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "PHBBUSD"

    def __str__(self):
        return "PHBBUSD"

    def __call__(self):
        return "PHBBUSD"


PHBBUSD = PHBBUSD()


@dataclass(slots=True, frozen=True)
class PHBPAX:
    name: str = "PHBPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PHBPAX"

    def __str__(self):
        return "PHBPAX"

    def __call__(self):
        return "PHBPAX"


PHBPAX = PHBPAX()


@dataclass(slots=True, frozen=True)
class PHBTUSD:
    name: str = "PHBTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PHBTUSD"

    def __str__(self):
        return "PHBTUSD"

    def __call__(self):
        return "PHBTUSD"


PHBTUSD = PHBTUSD()


@dataclass(slots=True, frozen=True)
class PHBUSDC:
    name: str = "PHBUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PHBUSDC"

    def __str__(self):
        return "PHBUSDC"

    def __call__(self):
        return "PHBUSDC"


PHBUSDC = PHBUSDC()


@dataclass(slots=True, frozen=True)
class PHBUSDT:
    name: str = "PHBUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PHBUSDT"

    def __str__(self):
        return "PHBUSDT"

    def __call__(self):
        return "PHBUSDT"


PHBUSDT = PHBUSDT()


@dataclass(slots=True, frozen=True)
class PHXBNB:
    name: str = "PHXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PHXBNB"

    def __str__(self):
        return "PHXBNB"

    def __call__(self):
        return "PHXBNB"


PHXBNB = PHXBNB()


@dataclass(slots=True, frozen=True)
class PHXBTC:
    name: str = "PHXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PHXBTC"

    def __str__(self):
        return "PHXBTC"

    def __call__(self):
        return "PHXBTC"


PHXBTC = PHXBTC()


@dataclass(slots=True, frozen=True)
class PHXETH:
    name: str = "PHXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PHXETH"

    def __str__(self):
        return "PHXETH"

    def __call__(self):
        return "PHXETH"


PHXETH = PHXETH()


@dataclass(slots=True, frozen=True)
class PIVXBNB:
    name: str = "PIVXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "PIVXBNB"

    def __str__(self):
        return "PIVXBNB"

    def __call__(self):
        return "PIVXBNB"


PIVXBNB = PIVXBNB()


@dataclass(slots=True, frozen=True)
class PIVXBTC:
    name: str = "PIVXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PIVXBTC"

    def __str__(self):
        return "PIVXBTC"

    def __call__(self):
        return "PIVXBTC"


PIVXBTC = PIVXBTC()


@dataclass(slots=True, frozen=True)
class PLABNB:
    name: str = "PLABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PLABNB"

    def __str__(self):
        return "PLABNB"

    def __call__(self):
        return "PLABNB"


PLABNB = PLABNB()


@dataclass(slots=True, frozen=True)
class PLABTC:
    name: str = "PLABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PLABTC"

    def __str__(self):
        return "PLABTC"

    def __call__(self):
        return "PLABTC"


PLABTC = PLABTC()


@dataclass(slots=True, frozen=True)
class PLABUSD:
    name: str = "PLABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PLABUSD"

    def __str__(self):
        return "PLABUSD"

    def __call__(self):
        return "PLABUSD"


PLABUSD = PLABUSD()


@dataclass(slots=True, frozen=True)
class PLAUSDT:
    name: str = "PLAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PLAUSDT"

    def __str__(self):
        return "PLAUSDT"

    def __call__(self):
        return "PLAUSDT"


PLAUSDT = PLAUSDT()


@dataclass(slots=True, frozen=True)
class PNTBTC:
    name: str = "PNTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PNTBTC"

    def __str__(self):
        return "PNTBTC"

    def __call__(self):
        return "PNTBTC"


PNTBTC = PNTBTC()


@dataclass(slots=True, frozen=True)
class PNTUSDT:
    name: str = "PNTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "PNTUSDT"

    def __str__(self):
        return "PNTUSDT"

    def __call__(self):
        return "PNTUSDT"


PNTUSDT = PNTUSDT()


@dataclass(slots=True, frozen=True)
class POABNB:
    name: str = "POABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "POABNB"

    def __str__(self):
        return "POABNB"

    def __call__(self):
        return "POABNB"


POABNB = POABNB()


@dataclass(slots=True, frozen=True)
class POABTC:
    name: str = "POABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "POABTC"

    def __str__(self):
        return "POABTC"

    def __call__(self):
        return "POABTC"


POABTC = POABTC()


@dataclass(slots=True, frozen=True)
class POAETH:
    name: str = "POAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "POAETH"

    def __str__(self):
        return "POAETH"

    def __call__(self):
        return "POAETH"


POAETH = POAETH()


@dataclass(slots=True, frozen=True)
class POEBTC:
    name: str = "POEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "POEBTC"

    def __str__(self):
        return "POEBTC"

    def __call__(self):
        return "POEBTC"


POEBTC = POEBTC()


@dataclass(slots=True, frozen=True)
class POEETH:
    name: str = "POEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "POEETH"

    def __str__(self):
        return "POEETH"

    def __call__(self):
        return "POEETH"


POEETH = POEETH()


@dataclass(slots=True, frozen=True)
class POLSBNB:
    name: str = "POLSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "POLSBNB"

    def __str__(self):
        return "POLSBNB"

    def __call__(self):
        return "POLSBNB"


POLSBNB = POLSBNB()


@dataclass(slots=True, frozen=True)
class POLSBTC:
    name: str = "POLSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "POLSBTC"

    def __str__(self):
        return "POLSBTC"

    def __call__(self):
        return "POLSBTC"


POLSBTC = POLSBTC()


@dataclass(slots=True, frozen=True)
class POLSBUSD:
    name: str = "POLSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "POLSBUSD"

    def __str__(self):
        return "POLSBUSD"

    def __call__(self):
        return "POLSBUSD"


POLSBUSD = POLSBUSD()


@dataclass(slots=True, frozen=True)
class POLSUSDT:
    name: str = "POLSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "POLSUSDT"

    def __str__(self):
        return "POLSUSDT"

    def __call__(self):
        return "POLSUSDT"


POLSUSDT = POLSUSDT()


@dataclass(slots=True, frozen=True)
class POLYBNB:
    name: str = "POLYBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "POLYBNB"

    def __str__(self):
        return "POLYBNB"

    def __call__(self):
        return "POLYBNB"


POLYBNB = POLYBNB()


@dataclass(slots=True, frozen=True)
class POLYBTC:
    name: str = "POLYBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "POLYBTC"

    def __str__(self):
        return "POLYBTC"

    def __call__(self):
        return "POLYBTC"


POLYBTC = POLYBTC()


@dataclass(slots=True, frozen=True)
class POLYBUSD:
    name: str = "POLYBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "POLYBUSD"

    def __str__(self):
        return "POLYBUSD"

    def __call__(self):
        return "POLYBUSD"


POLYBUSD = POLYBUSD()


@dataclass(slots=True, frozen=True)
class POLYUSDT:
    name: str = "POLYUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "POLYUSDT"

    def __str__(self):
        return "POLYUSDT"

    def __call__(self):
        return "POLYUSDT"


POLYUSDT = POLYUSDT()


@dataclass(slots=True, frozen=True)
class POLYXBTC:
    name: str = "POLYXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "POLYXBTC"

    def __str__(self):
        return "POLYXBTC"

    def __call__(self):
        return "POLYXBTC"


POLYXBTC = POLYXBTC()


@dataclass(slots=True, frozen=True)
class POLYXBUSD:
    name: str = "POLYXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "POLYXBUSD"

    def __str__(self):
        return "POLYXBUSD"

    def __call__(self):
        return "POLYXBUSD"


POLYXBUSD = POLYXBUSD()


@dataclass(slots=True, frozen=True)
class POLYXUSDT:
    name: str = "POLYXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "POLYXUSDT"

    def __str__(self):
        return "POLYXUSDT"

    def __call__(self):
        return "POLYXUSDT"


POLYXUSDT = POLYXUSDT()


@dataclass(slots=True, frozen=True)
class PONDBTC:
    name: str = "PONDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "PONDBTC"

    def __str__(self):
        return "PONDBTC"

    def __call__(self):
        return "PONDBTC"


PONDBTC = PONDBTC()


@dataclass(slots=True, frozen=True)
class PONDBUSD:
    name: str = "PONDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "PONDBUSD"

    def __str__(self):
        return "PONDBUSD"

    def __call__(self):
        return "PONDBUSD"


PONDBUSD = PONDBUSD()


@dataclass(slots=True, frozen=True)
class PONDUSDT:
    name: str = "PONDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "PONDUSDT"

    def __str__(self):
        return "PONDUSDT"

    def __call__(self):
        return "PONDUSDT"


PONDUSDT = PONDUSDT()


@dataclass(slots=True, frozen=True)
class PORTOBTC:
    name: str = "PORTOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PORTOBTC"

    def __str__(self):
        return "PORTOBTC"

    def __call__(self):
        return "PORTOBTC"


PORTOBTC = PORTOBTC()


@dataclass(slots=True, frozen=True)
class PORTOBUSD:
    name: str = "PORTOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "PORTOBUSD"

    def __str__(self):
        return "PORTOBUSD"

    def __call__(self):
        return "PORTOBUSD"


PORTOBUSD = PORTOBUSD()


@dataclass(slots=True, frozen=True)
class PORTOEUR:
    name: str = "PORTOEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PORTOEUR"

    def __str__(self):
        return "PORTOEUR"

    def __call__(self):
        return "PORTOEUR"


PORTOEUR = PORTOEUR()


@dataclass(slots=True, frozen=True)
class PORTOTRY:
    name: str = "PORTOTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "PORTOTRY"

    def __str__(self):
        return "PORTOTRY"

    def __call__(self):
        return "PORTOTRY"


PORTOTRY = PORTOTRY()


@dataclass(slots=True, frozen=True)
class PORTOUSDT:
    name: str = "PORTOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "PORTOUSDT"

    def __str__(self):
        return "PORTOUSDT"

    def __call__(self):
        return "PORTOUSDT"


PORTOUSDT = PORTOUSDT()


@dataclass(slots=True, frozen=True)
class POWRBNB:
    name: str = "POWRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "POWRBNB"

    def __str__(self):
        return "POWRBNB"

    def __call__(self):
        return "POWRBNB"


POWRBNB = POWRBNB()


@dataclass(slots=True, frozen=True)
class POWRBTC:
    name: str = "POWRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "POWRBTC"

    def __str__(self):
        return "POWRBTC"

    def __call__(self):
        return "POWRBTC"


POWRBTC = POWRBTC()


@dataclass(slots=True, frozen=True)
class POWRBUSD:
    name: str = "POWRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "POWRBUSD"

    def __str__(self):
        return "POWRBUSD"

    def __call__(self):
        return "POWRBUSD"


POWRBUSD = POWRBUSD()


@dataclass(slots=True, frozen=True)
class POWRETH:
    name: str = "POWRETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "POWRETH"

    def __str__(self):
        return "POWRETH"

    def __call__(self):
        return "POWRETH"


POWRETH = POWRETH()


@dataclass(slots=True, frozen=True)
class POWRUSDT:
    name: str = "POWRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "POWRUSDT"

    def __str__(self):
        return "POWRUSDT"

    def __call__(self):
        return "POWRUSDT"


POWRUSDT = POWRUSDT()


@dataclass(slots=True, frozen=True)
class PPTBTC:
    name: str = "PPTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PPTBTC"

    def __str__(self):
        return "PPTBTC"

    def __call__(self):
        return "PPTBTC"


PPTBTC = PPTBTC()


@dataclass(slots=True, frozen=True)
class PPTETH:
    name: str = "PPTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PPTETH"

    def __str__(self):
        return "PPTETH"

    def __call__(self):
        return "PPTETH"


PPTETH = PPTETH()


@dataclass(slots=True, frozen=True)
class PROMBNB:
    name: str = "PROMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PROMBNB"

    def __str__(self):
        return "PROMBNB"

    def __call__(self):
        return "PROMBNB"


PROMBNB = PROMBNB()


@dataclass(slots=True, frozen=True)
class PROMBTC:
    name: str = "PROMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PROMBTC"

    def __str__(self):
        return "PROMBTC"

    def __call__(self):
        return "PROMBTC"


PROMBTC = PROMBTC()


@dataclass(slots=True, frozen=True)
class PROMBUSD:
    name: str = "PROMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "PROMBUSD"

    def __str__(self):
        return "PROMBUSD"

    def __call__(self):
        return "PROMBUSD"


PROMBUSD = PROMBUSD()


@dataclass(slots=True, frozen=True)
class PROSBUSD:
    name: str = "PROSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "PROSBUSD"

    def __str__(self):
        return "PROSBUSD"

    def __call__(self):
        return "PROSBUSD"


PROSBUSD = PROSBUSD()


@dataclass(slots=True, frozen=True)
class PROSETH:
    name: str = "PROSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PROSETH"

    def __str__(self):
        return "PROSETH"

    def __call__(self):
        return "PROSETH"


PROSETH = PROSETH()


@dataclass(slots=True, frozen=True)
class PSGBTC:
    name: str = "PSGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PSGBTC"

    def __str__(self):
        return "PSGBTC"

    def __call__(self):
        return "PSGBTC"


PSGBTC = PSGBTC()


@dataclass(slots=True, frozen=True)
class PSGBUSD:
    name: str = "PSGBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "PSGBUSD"

    def __str__(self):
        return "PSGBUSD"

    def __call__(self):
        return "PSGBUSD"


PSGBUSD = PSGBUSD()


@dataclass(slots=True, frozen=True)
class PSGUSDT:
    name: str = "PSGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "PSGUSDT"

    def __str__(self):
        return "PSGUSDT"

    def __call__(self):
        return "PSGUSDT"


PSGUSDT = PSGUSDT()


@dataclass(slots=True, frozen=True)
class PUNDIXBUSD:
    name: str = "PUNDIXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "PUNDIXBUSD"

    def __str__(self):
        return "PUNDIXBUSD"

    def __call__(self):
        return "PUNDIXBUSD"


PUNDIXBUSD = PUNDIXBUSD()


@dataclass(slots=True, frozen=True)
class PUNDIXETH:
    name: str = "PUNDIXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "PUNDIXETH"

    def __str__(self):
        return "PUNDIXETH"

    def __call__(self):
        return "PUNDIXETH"


PUNDIXETH = PUNDIXETH()


@dataclass(slots=True, frozen=True)
class PUNDIXUSDT:
    name: str = "PUNDIXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "PUNDIXUSDT"

    def __str__(self):
        return "PUNDIXUSDT"

    def __call__(self):
        return "PUNDIXUSDT"


PUNDIXUSDT = PUNDIXUSDT()


@dataclass(slots=True, frozen=True)
class PYRBTC:
    name: str = "PYRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "PYRBTC"

    def __str__(self):
        return "PYRBTC"

    def __call__(self):
        return "PYRBTC"


PYRBTC = PYRBTC()


@dataclass(slots=True, frozen=True)
class PYRBUSD:
    name: str = "PYRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "PYRBUSD"

    def __str__(self):
        return "PYRBUSD"

    def __call__(self):
        return "PYRBUSD"


PYRBUSD = PYRBUSD()


@dataclass(slots=True, frozen=True)
class PYRUSDT:
    name: str = "PYRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "PYRUSDT"

    def __str__(self):
        return "PYRUSDT"

    def __call__(self):
        return "PYRUSDT"


PYRUSDT = PYRUSDT()


@dataclass(slots=True, frozen=True)
class QIBNB:
    name: str = "QIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "QIBNB"

    def __str__(self):
        return "QIBNB"

    def __call__(self):
        return "QIBNB"


QIBNB = QIBNB()


@dataclass(slots=True, frozen=True)
class QIBTC:
    name: str = "QIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "QIBTC"

    def __str__(self):
        return "QIBTC"

    def __call__(self):
        return "QIBTC"


QIBTC = QIBTC()


@dataclass(slots=True, frozen=True)
class QIBUSD:
    name: str = "QIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "QIBUSD"

    def __str__(self):
        return "QIBUSD"

    def __call__(self):
        return "QIBUSD"


QIBUSD = QIBUSD()


@dataclass(slots=True, frozen=True)
class QIUSDT:
    name: str = "QIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "QIUSDT"

    def __str__(self):
        return "QIUSDT"

    def __call__(self):
        return "QIUSDT"


QIUSDT = QIUSDT()


@dataclass(slots=True, frozen=True)
class QKCBTC:
    name: str = "QKCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "QKCBTC"

    def __str__(self):
        return "QKCBTC"

    def __call__(self):
        return "QKCBTC"


QKCBTC = QKCBTC()


@dataclass(slots=True, frozen=True)
class QKCBUSD:
    name: str = "QKCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "QKCBUSD"

    def __str__(self):
        return "QKCBUSD"

    def __call__(self):
        return "QKCBUSD"


QKCBUSD = QKCBUSD()


@dataclass(slots=True, frozen=True)
class QKCETH:
    name: str = "QKCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "QKCETH"

    def __str__(self):
        return "QKCETH"

    def __call__(self):
        return "QKCETH"


QKCETH = QKCETH()


@dataclass(slots=True, frozen=True)
class QLCBNB:
    name: str = "QLCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "QLCBNB"

    def __str__(self):
        return "QLCBNB"

    def __call__(self):
        return "QLCBNB"


QLCBNB = QLCBNB()


@dataclass(slots=True, frozen=True)
class QLCBTC:
    name: str = "QLCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "QLCBTC"

    def __str__(self):
        return "QLCBTC"

    def __call__(self):
        return "QLCBTC"


QLCBTC = QLCBTC()


@dataclass(slots=True, frozen=True)
class QLCETH:
    name: str = "QLCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "QLCETH"

    def __str__(self):
        return "QLCETH"

    def __call__(self):
        return "QLCETH"


QLCETH = QLCETH()


@dataclass(slots=True, frozen=True)
class QNTBNB:
    name: str = "QNTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "QNTBNB"

    def __str__(self):
        return "QNTBNB"

    def __call__(self):
        return "QNTBNB"


QNTBNB = QNTBNB()


@dataclass(slots=True, frozen=True)
class QNTBTC:
    name: str = "QNTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "QNTBTC"

    def __str__(self):
        return "QNTBTC"

    def __call__(self):
        return "QNTBTC"


QNTBTC = QNTBTC()


@dataclass(slots=True, frozen=True)
class QNTBUSD:
    name: str = "QNTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "QNTBUSD"

    def __str__(self):
        return "QNTBUSD"

    def __call__(self):
        return "QNTBUSD"


QNTBUSD = QNTBUSD()


@dataclass(slots=True, frozen=True)
class QNTUSDT:
    name: str = "QNTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "QNTUSDT"

    def __str__(self):
        return "QNTUSDT"

    def __call__(self):
        return "QNTUSDT"


QNTUSDT = QNTUSDT()


@dataclass(slots=True, frozen=True)
class QSPBNB:
    name: str = "QSPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "QSPBNB"

    def __str__(self):
        return "QSPBNB"

    def __call__(self):
        return "QSPBNB"


QSPBNB = QSPBNB()


@dataclass(slots=True, frozen=True)
class QSPBTC:
    name: str = "QSPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "QSPBTC"

    def __str__(self):
        return "QSPBTC"

    def __call__(self):
        return "QSPBTC"


QSPBTC = QSPBTC()


@dataclass(slots=True, frozen=True)
class QSPETH:
    name: str = "QSPETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "QSPETH"

    def __str__(self):
        return "QSPETH"

    def __call__(self):
        return "QSPETH"


QSPETH = QSPETH()


@dataclass(slots=True, frozen=True)
class QTUMBNB:
    name: str = "QTUMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "QTUMBNB"

    def __str__(self):
        return "QTUMBNB"

    def __call__(self):
        return "QTUMBNB"


QTUMBNB = QTUMBNB()


@dataclass(slots=True, frozen=True)
class QTUMBTC:
    name: str = "QTUMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "QTUMBTC"

    def __str__(self):
        return "QTUMBTC"

    def __call__(self):
        return "QTUMBTC"


QTUMBTC = QTUMBTC()


@dataclass(slots=True, frozen=True)
class QTUMBUSD:
    name: str = "QTUMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "QTUMBUSD"

    def __str__(self):
        return "QTUMBUSD"

    def __call__(self):
        return "QTUMBUSD"


QTUMBUSD = QTUMBUSD()


@dataclass(slots=True, frozen=True)
class QTUMETH:
    name: str = "QTUMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "QTUMETH"

    def __str__(self):
        return "QTUMETH"

    def __call__(self):
        return "QTUMETH"


QTUMETH = QTUMETH()


@dataclass(slots=True, frozen=True)
class QTUMUSDT:
    name: str = "QTUMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "QTUMUSDT"

    def __str__(self):
        return "QTUMUSDT"

    def __call__(self):
        return "QTUMUSDT"


QTUMUSDT = QTUMUSDT()


@dataclass(slots=True, frozen=True)
class QUICKBNB:
    name: str = "QUICKBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "QUICKBNB"

    def __str__(self):
        return "QUICKBNB"

    def __call__(self):
        return "QUICKBNB"


QUICKBNB = QUICKBNB()


@dataclass(slots=True, frozen=True)
class QUICKBTC:
    name: str = "QUICKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "QUICKBTC"

    def __str__(self):
        return "QUICKBTC"

    def __call__(self):
        return "QUICKBTC"


QUICKBTC = QUICKBTC()


@dataclass(slots=True, frozen=True)
class QUICKBUSD:
    name: str = "QUICKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "QUICKBUSD"

    def __str__(self):
        return "QUICKBUSD"

    def __call__(self):
        return "QUICKBUSD"


QUICKBUSD = QUICKBUSD()


@dataclass(slots=True, frozen=True)
class QUICKUSDT:
    name: str = "QUICKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "QUICKUSDT"

    def __str__(self):
        return "QUICKUSDT"

    def __call__(self):
        return "QUICKUSDT"


QUICKUSDT = QUICKUSDT()


@dataclass(slots=True, frozen=True)
class RADBNB:
    name: str = "RADBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RADBNB"

    def __str__(self):
        return "RADBNB"

    def __call__(self):
        return "RADBNB"


RADBNB = RADBNB()


@dataclass(slots=True, frozen=True)
class RADBTC:
    name: str = "RADBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RADBTC"

    def __str__(self):
        return "RADBTC"

    def __call__(self):
        return "RADBTC"


RADBTC = RADBTC()


@dataclass(slots=True, frozen=True)
class RADBUSD:
    name: str = "RADBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "RADBUSD"

    def __str__(self):
        return "RADBUSD"

    def __call__(self):
        return "RADBUSD"


RADBUSD = RADBUSD()


@dataclass(slots=True, frozen=True)
class RADUSDT:
    name: str = "RADUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "RADUSDT"

    def __str__(self):
        return "RADUSDT"

    def __call__(self):
        return "RADUSDT"


RADUSDT = RADUSDT()


@dataclass(slots=True, frozen=True)
class RAMPBTC:
    name: str = "RAMPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RAMPBTC"

    def __str__(self):
        return "RAMPBTC"

    def __call__(self):
        return "RAMPBTC"


RAMPBTC = RAMPBTC()


@dataclass(slots=True, frozen=True)
class RAMPBUSD:
    name: str = "RAMPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RAMPBUSD"

    def __str__(self):
        return "RAMPBUSD"

    def __call__(self):
        return "RAMPBUSD"


RAMPBUSD = RAMPBUSD()


@dataclass(slots=True, frozen=True)
class RAMPUSDT:
    name: str = "RAMPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RAMPUSDT"

    def __str__(self):
        return "RAMPUSDT"

    def __call__(self):
        return "RAMPUSDT"


RAMPUSDT = RAMPUSDT()


@dataclass(slots=True, frozen=True)
class RAREBNB:
    name: str = "RAREBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RAREBNB"

    def __str__(self):
        return "RAREBNB"

    def __call__(self):
        return "RAREBNB"


RAREBNB = RAREBNB()


@dataclass(slots=True, frozen=True)
class RAREBTC:
    name: str = "RAREBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RAREBTC"

    def __str__(self):
        return "RAREBTC"

    def __call__(self):
        return "RAREBTC"


RAREBTC = RAREBTC()


@dataclass(slots=True, frozen=True)
class RAREBUSD:
    name: str = "RAREBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RAREBUSD"

    def __str__(self):
        return "RAREBUSD"

    def __call__(self):
        return "RAREBUSD"


RAREBUSD = RAREBUSD()


@dataclass(slots=True, frozen=True)
class RAREUSDT:
    name: str = "RAREUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RAREUSDT"

    def __str__(self):
        return "RAREUSDT"

    def __call__(self):
        return "RAREUSDT"


RAREUSDT = RAREUSDT()


@dataclass(slots=True, frozen=True)
class RAYBNB:
    name: str = "RAYBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RAYBNB"

    def __str__(self):
        return "RAYBNB"

    def __call__(self):
        return "RAYBNB"


RAYBNB = RAYBNB()


@dataclass(slots=True, frozen=True)
class RAYBUSD:
    name: str = "RAYBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "RAYBUSD"

    def __str__(self):
        return "RAYBUSD"

    def __call__(self):
        return "RAYBUSD"


RAYBUSD = RAYBUSD()


@dataclass(slots=True, frozen=True)
class RAYUSDT:
    name: str = "RAYUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "RAYUSDT"

    def __str__(self):
        return "RAYUSDT"

    def __call__(self):
        return "RAYUSDT"


RAYUSDT = RAYUSDT()


@dataclass(slots=True, frozen=True)
class RCNBNB:
    name: str = "RCNBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RCNBNB"

    def __str__(self):
        return "RCNBNB"

    def __call__(self):
        return "RCNBNB"


RCNBNB = RCNBNB()


@dataclass(slots=True, frozen=True)
class RCNBTC:
    name: str = "RCNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RCNBTC"

    def __str__(self):
        return "RCNBTC"

    def __call__(self):
        return "RCNBTC"


RCNBTC = RCNBTC()


@dataclass(slots=True, frozen=True)
class RCNETH:
    name: str = "RCNETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RCNETH"

    def __str__(self):
        return "RCNETH"

    def __call__(self):
        return "RCNETH"


RCNETH = RCNETH()


@dataclass(slots=True, frozen=True)
class RDNBNB:
    name: str = "RDNBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RDNBNB"

    def __str__(self):
        return "RDNBNB"

    def __call__(self):
        return "RDNBNB"


RDNBNB = RDNBNB()


@dataclass(slots=True, frozen=True)
class RDNBTC:
    name: str = "RDNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RDNBTC"

    def __str__(self):
        return "RDNBTC"

    def __call__(self):
        return "RDNBTC"


RDNBTC = RDNBTC()


@dataclass(slots=True, frozen=True)
class RDNETH:
    name: str = "RDNETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RDNETH"

    def __str__(self):
        return "RDNETH"

    def __call__(self):
        return "RDNETH"


RDNETH = RDNETH()


@dataclass(slots=True, frozen=True)
class REEFBIDR:
    name: str = "REEFBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "REEFBIDR"

    def __str__(self):
        return "REEFBIDR"

    def __call__(self):
        return "REEFBIDR"


REEFBIDR = REEFBIDR()


@dataclass(slots=True, frozen=True)
class REEFBTC:
    name: str = "REEFBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "REEFBTC"

    def __str__(self):
        return "REEFBTC"

    def __call__(self):
        return "REEFBTC"


REEFBTC = REEFBTC()


@dataclass(slots=True, frozen=True)
class REEFBUSD:
    name: str = "REEFBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "REEFBUSD"

    def __str__(self):
        return "REEFBUSD"

    def __call__(self):
        return "REEFBUSD"


REEFBUSD = REEFBUSD()


@dataclass(slots=True, frozen=True)
class REEFTRY:
    name: str = "REEFTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "REEFTRY"

    def __str__(self):
        return "REEFTRY"

    def __call__(self):
        return "REEFTRY"


REEFTRY = REEFTRY()


@dataclass(slots=True, frozen=True)
class REEFUSDT:
    name: str = "REEFUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "REEFUSDT"

    def __str__(self):
        return "REEFUSDT"

    def __call__(self):
        return "REEFUSDT"


REEFUSDT = REEFUSDT()


@dataclass(slots=True, frozen=True)
class REIBNB:
    name: str = "REIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "REIBNB"

    def __str__(self):
        return "REIBNB"

    def __call__(self):
        return "REIBNB"


REIBNB = REIBNB()


@dataclass(slots=True, frozen=True)
class REIBUSD:
    name: str = "REIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "REIBUSD"

    def __str__(self):
        return "REIBUSD"

    def __call__(self):
        return "REIBUSD"


REIBUSD = REIBUSD()


@dataclass(slots=True, frozen=True)
class REIETH:
    name: str = "REIETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "REIETH"

    def __str__(self):
        return "REIETH"

    def __call__(self):
        return "REIETH"


REIETH = REIETH()


@dataclass(slots=True, frozen=True)
class REIUSDT:
    name: str = "REIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "REIUSDT"

    def __str__(self):
        return "REIUSDT"

    def __call__(self):
        return "REIUSDT"


REIUSDT = REIUSDT()


@dataclass(slots=True, frozen=True)
class RENBNB:
    name: str = "RENBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RENBNB"

    def __str__(self):
        return "RENBNB"

    def __call__(self):
        return "RENBNB"


RENBNB = RENBNB()


@dataclass(slots=True, frozen=True)
class RENBTC:
    name: str = "RENBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "RENBTC"

    def __str__(self):
        return "RENBTC"

    def __call__(self):
        return "RENBTC"


RENBTC = RENBTC()


@dataclass(slots=True, frozen=True)
class RENBTCBTC:
    name: str = "RENBTCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RENBTCBTC"

    def __str__(self):
        return "RENBTCBTC"

    def __call__(self):
        return "RENBTCBTC"


RENBTCBTC = RENBTCBTC()


@dataclass(slots=True, frozen=True)
class RENBTCETH:
    name: str = "RENBTCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "RENBTCETH"

    def __str__(self):
        return "RENBTCETH"

    def __call__(self):
        return "RENBTCETH"


RENBTCETH = RENBTCETH()


@dataclass(slots=True, frozen=True)
class RENBUSD:
    name: str = "RENBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RENBUSD"

    def __str__(self):
        return "RENBUSD"

    def __call__(self):
        return "RENBUSD"


RENBUSD = RENBUSD()


@dataclass(slots=True, frozen=True)
class RENUSDT:
    name: str = "RENUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "RENUSDT"

    def __str__(self):
        return "RENUSDT"

    def __call__(self):
        return "RENUSDT"


RENUSDT = RENUSDT()


@dataclass(slots=True, frozen=True)
class REPBNB:
    name: str = "REPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "REPBNB"

    def __str__(self):
        return "REPBNB"

    def __call__(self):
        return "REPBNB"


REPBNB = REPBNB()


@dataclass(slots=True, frozen=True)
class REPBTC:
    name: str = "REPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "REPBTC"

    def __str__(self):
        return "REPBTC"

    def __call__(self):
        return "REPBTC"


REPBTC = REPBTC()


@dataclass(slots=True, frozen=True)
class REPBUSD:
    name: str = "REPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "REPBUSD"

    def __str__(self):
        return "REPBUSD"

    def __call__(self):
        return "REPBUSD"


REPBUSD = REPBUSD()


@dataclass(slots=True, frozen=True)
class REPUSDT:
    name: str = "REPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "REPUSDT"

    def __str__(self):
        return "REPUSDT"

    def __call__(self):
        return "REPUSDT"


REPUSDT = REPUSDT()


@dataclass(slots=True, frozen=True)
class REQBTC:
    name: str = "REQBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "REQBTC"

    def __str__(self):
        return "REQBTC"

    def __call__(self):
        return "REQBTC"


REQBTC = REQBTC()


@dataclass(slots=True, frozen=True)
class REQBUSD:
    name: str = "REQBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "REQBUSD"

    def __str__(self):
        return "REQBUSD"

    def __call__(self):
        return "REQBUSD"


REQBUSD = REQBUSD()


@dataclass(slots=True, frozen=True)
class REQETH:
    name: str = "REQETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "REQETH"

    def __str__(self):
        return "REQETH"

    def __call__(self):
        return "REQETH"


REQETH = REQETH()


@dataclass(slots=True, frozen=True)
class REQUSDT:
    name: str = "REQUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "REQUSDT"

    def __str__(self):
        return "REQUSDT"

    def __call__(self):
        return "REQUSDT"


REQUSDT = REQUSDT()


@dataclass(slots=True, frozen=True)
class RGTBNB:
    name: str = "RGTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RGTBNB"

    def __str__(self):
        return "RGTBNB"

    def __call__(self):
        return "RGTBNB"


RGTBNB = RGTBNB()


@dataclass(slots=True, frozen=True)
class RGTBTC:
    name: str = "RGTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RGTBTC"

    def __str__(self):
        return "RGTBTC"

    def __call__(self):
        return "RGTBTC"


RGTBTC = RGTBTC()


@dataclass(slots=True, frozen=True)
class RGTBUSD:
    name: str = "RGTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "RGTBUSD"

    def __str__(self):
        return "RGTBUSD"

    def __call__(self):
        return "RGTBUSD"


RGTBUSD = RGTBUSD()


@dataclass(slots=True, frozen=True)
class RGTUSDT:
    name: str = "RGTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "RGTUSDT"

    def __str__(self):
        return "RGTUSDT"

    def __call__(self):
        return "RGTUSDT"


RGTUSDT = RGTUSDT()


@dataclass(slots=True, frozen=True)
class RIFBTC:
    name: str = "RIFBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RIFBTC"

    def __str__(self):
        return "RIFBTC"

    def __call__(self):
        return "RIFBTC"


RIFBTC = RIFBTC()


@dataclass(slots=True, frozen=True)
class RIFUSDT:
    name: str = "RIFUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "RIFUSDT"

    def __str__(self):
        return "RIFUSDT"

    def __call__(self):
        return "RIFUSDT"


RIFUSDT = RIFUSDT()


@dataclass(slots=True, frozen=True)
class RLCBNB:
    name: str = "RLCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RLCBNB"

    def __str__(self):
        return "RLCBNB"

    def __call__(self):
        return "RLCBNB"


RLCBNB = RLCBNB()


@dataclass(slots=True, frozen=True)
class RLCBTC:
    name: str = "RLCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "RLCBTC"

    def __str__(self):
        return "RLCBTC"

    def __call__(self):
        return "RLCBTC"


RLCBTC = RLCBTC()


@dataclass(slots=True, frozen=True)
class RLCBUSD:
    name: str = "RLCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "RLCBUSD"

    def __str__(self):
        return "RLCBUSD"

    def __call__(self):
        return "RLCBUSD"


RLCBUSD = RLCBUSD()


@dataclass(slots=True, frozen=True)
class RLCETH:
    name: str = "RLCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RLCETH"

    def __str__(self):
        return "RLCETH"

    def __call__(self):
        return "RLCETH"


RLCETH = RLCETH()


@dataclass(slots=True, frozen=True)
class RLCUSDT:
    name: str = "RLCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "RLCUSDT"

    def __str__(self):
        return "RLCUSDT"

    def __call__(self):
        return "RLCUSDT"


RLCUSDT = RLCUSDT()


@dataclass(slots=True, frozen=True)
class RNDRBTC:
    name: str = "RNDRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "RNDRBTC"

    def __str__(self):
        return "RNDRBTC"

    def __call__(self):
        return "RNDRBTC"


RNDRBTC = RNDRBTC()


@dataclass(slots=True, frozen=True)
class RNDRBUSD:
    name: str = "RNDRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "RNDRBUSD"

    def __str__(self):
        return "RNDRBUSD"

    def __call__(self):
        return "RNDRBUSD"


RNDRBUSD = RNDRBUSD()


@dataclass(slots=True, frozen=True)
class RNDRUSDT:
    name: str = "RNDRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "RNDRUSDT"

    def __str__(self):
        return "RNDRUSDT"

    def __call__(self):
        return "RNDRUSDT"


RNDRUSDT = RNDRUSDT()


@dataclass(slots=True, frozen=True)
class ROSEBNB:
    name: str = "ROSEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ROSEBNB"

    def __str__(self):
        return "ROSEBNB"

    def __call__(self):
        return "ROSEBNB"


ROSEBNB = ROSEBNB()


@dataclass(slots=True, frozen=True)
class ROSEBTC:
    name: str = "ROSEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ROSEBTC"

    def __str__(self):
        return "ROSEBTC"

    def __call__(self):
        return "ROSEBTC"


ROSEBTC = ROSEBTC()


@dataclass(slots=True, frozen=True)
class ROSEBUSD:
    name: str = "ROSEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ROSEBUSD"

    def __str__(self):
        return "ROSEBUSD"

    def __call__(self):
        return "ROSEBUSD"


ROSEBUSD = ROSEBUSD()


@dataclass(slots=True, frozen=True)
class ROSEETH:
    name: str = "ROSEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ROSEETH"

    def __str__(self):
        return "ROSEETH"

    def __call__(self):
        return "ROSEETH"


ROSEETH = ROSEETH()


@dataclass(slots=True, frozen=True)
class ROSETRY:
    name: str = "ROSETRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "ROSETRY"

    def __str__(self):
        return "ROSETRY"

    def __call__(self):
        return "ROSETRY"


ROSETRY = ROSETRY()


@dataclass(slots=True, frozen=True)
class ROSEUSDT:
    name: str = "ROSEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ROSEUSDT"

    def __str__(self):
        return "ROSEUSDT"

    def __call__(self):
        return "ROSEUSDT"


ROSEUSDT = ROSEUSDT()


@dataclass(slots=True, frozen=True)
class RPXBNB:
    name: str = "RPXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RPXBNB"

    def __str__(self):
        return "RPXBNB"

    def __call__(self):
        return "RPXBNB"


RPXBNB = RPXBNB()


@dataclass(slots=True, frozen=True)
class RPXBTC:
    name: str = "RPXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RPXBTC"

    def __str__(self):
        return "RPXBTC"

    def __call__(self):
        return "RPXBTC"


RPXBTC = RPXBTC()


@dataclass(slots=True, frozen=True)
class RPXETH:
    name: str = "RPXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RPXETH"

    def __str__(self):
        return "RPXETH"

    def __call__(self):
        return "RPXETH"


RPXETH = RPXETH()


@dataclass(slots=True, frozen=True)
class RSRBNB:
    name: str = "RSRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RSRBNB"

    def __str__(self):
        return "RSRBNB"

    def __call__(self):
        return "RSRBNB"


RSRBNB = RSRBNB()


@dataclass(slots=True, frozen=True)
class RSRBTC:
    name: str = "RSRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RSRBTC"

    def __str__(self):
        return "RSRBTC"

    def __call__(self):
        return "RSRBTC"


RSRBTC = RSRBTC()


@dataclass(slots=True, frozen=True)
class RSRBUSD:
    name: str = "RSRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "RSRBUSD"

    def __str__(self):
        return "RSRBUSD"

    def __call__(self):
        return "RSRBUSD"


RSRBUSD = RSRBUSD()


@dataclass(slots=True, frozen=True)
class RSRUSDT:
    name: str = "RSRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "RSRUSDT"

    def __str__(self):
        return "RSRUSDT"

    def __call__(self):
        return "RSRUSDT"


RSRUSDT = RSRUSDT()


@dataclass(slots=True, frozen=True)
class RUNEAUD:
    name: str = "RUNEAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00000100
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "RUNEAUD"

    def __str__(self):
        return "RUNEAUD"

    def __call__(self):
        return "RUNEAUD"


RUNEAUD = RUNEAUD()


@dataclass(slots=True, frozen=True)
class RUNEBNB:
    name: str = "RUNEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RUNEBNB"

    def __str__(self):
        return "RUNEBNB"

    def __call__(self):
        return "RUNEBNB"


RUNEBNB = RUNEBNB()


@dataclass(slots=True, frozen=True)
class RUNEBTC:
    name: str = "RUNEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "RUNEBTC"

    def __str__(self):
        return "RUNEBTC"

    def __call__(self):
        return "RUNEBTC"


RUNEBTC = RUNEBTC()


@dataclass(slots=True, frozen=True)
class RUNEBUSD:
    name: str = "RUNEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "RUNEBUSD"

    def __str__(self):
        return "RUNEBUSD"

    def __call__(self):
        return "RUNEBUSD"


RUNEBUSD = RUNEBUSD()


@dataclass(slots=True, frozen=True)
class RUNEETH:
    name: str = "RUNEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RUNEETH"

    def __str__(self):
        return "RUNEETH"

    def __call__(self):
        return "RUNEETH"


RUNEETH = RUNEETH()


@dataclass(slots=True, frozen=True)
class RUNEEUR:
    name: str = "RUNEEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "RUNEEUR"

    def __str__(self):
        return "RUNEEUR"

    def __call__(self):
        return "RUNEEUR"


RUNEEUR = RUNEEUR()


@dataclass(slots=True, frozen=True)
class RUNEGBP:
    name: str = "RUNEGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "RUNEGBP"

    def __str__(self):
        return "RUNEGBP"

    def __call__(self):
        return "RUNEGBP"


RUNEGBP = RUNEGBP()


@dataclass(slots=True, frozen=True)
class RUNETRY:
    name: str = "RUNETRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "RUNETRY"

    def __str__(self):
        return "RUNETRY"

    def __call__(self):
        return "RUNETRY"


RUNETRY = RUNETRY()


@dataclass(slots=True, frozen=True)
class RUNEUSDT:
    name: str = "RUNEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "RUNEUSDT"

    def __str__(self):
        return "RUNEUSDT"

    def __call__(self):
        return "RUNEUSDT"


RUNEUSDT = RUNEUSDT()


@dataclass(slots=True, frozen=True)
class RVNBTC:
    name: str = "RVNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "RVNBTC"

    def __str__(self):
        return "RVNBTC"

    def __call__(self):
        return "RVNBTC"


RVNBTC = RVNBTC()


@dataclass(slots=True, frozen=True)
class RVNBUSD:
    name: str = "RVNBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "RVNBUSD"

    def __str__(self):
        return "RVNBUSD"

    def __call__(self):
        return "RVNBUSD"


RVNBUSD = RVNBUSD()


@dataclass(slots=True, frozen=True)
class RVNTRY:
    name: str = "RVNTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "RVNTRY"

    def __str__(self):
        return "RVNTRY"

    def __call__(self):
        return "RVNTRY"


RVNTRY = RVNTRY()


@dataclass(slots=True, frozen=True)
class RVNUSDT:
    name: str = "RVNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "RVNUSDT"

    def __str__(self):
        return "RVNUSDT"

    def __call__(self):
        return "RVNUSDT"


RVNUSDT = RVNUSDT()


@dataclass(slots=True, frozen=True)
class SALTBTC:
    name: str = "SALTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SALTBTC"

    def __str__(self):
        return "SALTBTC"

    def __call__(self):
        return "SALTBTC"


SALTBTC = SALTBTC()


@dataclass(slots=True, frozen=True)
class SALTETH:
    name: str = "SALTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SALTETH"

    def __str__(self):
        return "SALTETH"

    def __call__(self):
        return "SALTETH"


SALTETH = SALTETH()


@dataclass(slots=True, frozen=True)
class SANDAUD:
    name: str = "SANDAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "SANDAUD"

    def __str__(self):
        return "SANDAUD"

    def __call__(self):
        return "SANDAUD"


SANDAUD = SANDAUD()


@dataclass(slots=True, frozen=True)
class SANDBIDR:
    name: str = "SANDBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9223371110.00000000
    margin: bool = False

    def __repr__(self):
        return "SANDBIDR"

    def __str__(self):
        return "SANDBIDR"

    def __call__(self):
        return "SANDBIDR"


SANDBIDR = SANDBIDR()


@dataclass(slots=True, frozen=True)
class SANDBNB:
    name: str = "SANDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SANDBNB"

    def __str__(self):
        return "SANDBNB"

    def __call__(self):
        return "SANDBNB"


SANDBNB = SANDBNB()


@dataclass(slots=True, frozen=True)
class SANDBRL:
    name: str = "SANDBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "SANDBRL"

    def __str__(self):
        return "SANDBRL"

    def __call__(self):
        return "SANDBRL"


SANDBRL = SANDBRL()


@dataclass(slots=True, frozen=True)
class SANDBTC:
    name: str = "SANDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SANDBTC"

    def __str__(self):
        return "SANDBTC"

    def __call__(self):
        return "SANDBTC"


SANDBTC = SANDBTC()


@dataclass(slots=True, frozen=True)
class SANDBUSD:
    name: str = "SANDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SANDBUSD"

    def __str__(self):
        return "SANDBUSD"

    def __call__(self):
        return "SANDBUSD"


SANDBUSD = SANDBUSD()


@dataclass(slots=True, frozen=True)
class SANDETH:
    name: str = "SANDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SANDETH"

    def __str__(self):
        return "SANDETH"

    def __call__(self):
        return "SANDETH"


SANDETH = SANDETH()


@dataclass(slots=True, frozen=True)
class SANDTRY:
    name: str = "SANDTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "SANDTRY"

    def __str__(self):
        return "SANDTRY"

    def __call__(self):
        return "SANDTRY"


SANDTRY = SANDTRY()


@dataclass(slots=True, frozen=True)
class SANDUSDT:
    name: str = "SANDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SANDUSDT"

    def __str__(self):
        return "SANDUSDT"

    def __call__(self):
        return "SANDUSDT"


SANDUSDT = SANDUSDT()


@dataclass(slots=True, frozen=True)
class SANTOSBRL:
    name: str = "SANTOSBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "SANTOSBRL"

    def __str__(self):
        return "SANTOSBRL"

    def __call__(self):
        return "SANTOSBRL"


SANTOSBRL = SANTOSBRL()


@dataclass(slots=True, frozen=True)
class SANTOSBTC:
    name: str = "SANTOSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SANTOSBTC"

    def __str__(self):
        return "SANTOSBTC"

    def __call__(self):
        return "SANTOSBTC"


SANTOSBTC = SANTOSBTC()


@dataclass(slots=True, frozen=True)
class SANTOSBUSD:
    name: str = "SANTOSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "SANTOSBUSD"

    def __str__(self):
        return "SANTOSBUSD"

    def __call__(self):
        return "SANTOSBUSD"


SANTOSBUSD = SANTOSBUSD()


@dataclass(slots=True, frozen=True)
class SANTOSTRY:
    name: str = "SANTOSTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "SANTOSTRY"

    def __str__(self):
        return "SANTOSTRY"

    def __call__(self):
        return "SANTOSTRY"


SANTOSTRY = SANTOSTRY()


@dataclass(slots=True, frozen=True)
class SANTOSUSDT:
    name: str = "SANTOSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "SANTOSUSDT"

    def __str__(self):
        return "SANTOSUSDT"

    def __call__(self):
        return "SANTOSUSDT"


SANTOSUSDT = SANTOSUSDT()


@dataclass(slots=True, frozen=True)
class SCBTC:
    name: str = "SCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SCBTC"

    def __str__(self):
        return "SCBTC"

    def __call__(self):
        return "SCBTC"


SCBTC = SCBTC()


@dataclass(slots=True, frozen=True)
class SCBUSD:
    name: str = "SCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "SCBUSD"

    def __str__(self):
        return "SCBUSD"

    def __call__(self):
        return "SCBUSD"


SCBUSD = SCBUSD()


@dataclass(slots=True, frozen=True)
class SCETH:
    name: str = "SCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SCETH"

    def __str__(self):
        return "SCETH"

    def __call__(self):
        return "SCETH"


SCETH = SCETH()


@dataclass(slots=True, frozen=True)
class SCRTBTC:
    name: str = "SCRTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SCRTBTC"

    def __str__(self):
        return "SCRTBTC"

    def __call__(self):
        return "SCRTBTC"


SCRTBTC = SCRTBTC()


@dataclass(slots=True, frozen=True)
class SCRTBUSD:
    name: str = "SCRTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SCRTBUSD"

    def __str__(self):
        return "SCRTBUSD"

    def __call__(self):
        return "SCRTBUSD"


SCRTBUSD = SCRTBUSD()


@dataclass(slots=True, frozen=True)
class SCRTETH:
    name: str = "SCRTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SCRTETH"

    def __str__(self):
        return "SCRTETH"

    def __call__(self):
        return "SCRTETH"


SCRTETH = SCRTETH()


@dataclass(slots=True, frozen=True)
class SCRTUSDT:
    name: str = "SCRTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SCRTUSDT"

    def __str__(self):
        return "SCRTUSDT"

    def __call__(self):
        return "SCRTUSDT"


SCRTUSDT = SCRTUSDT()


@dataclass(slots=True, frozen=True)
class SCUSDT:
    name: str = "SCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "SCUSDT"

    def __str__(self):
        return "SCUSDT"

    def __call__(self):
        return "SCUSDT"


SCUSDT = SCUSDT()


@dataclass(slots=True, frozen=True)
class SFPBTC:
    name: str = "SFPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SFPBTC"

    def __str__(self):
        return "SFPBTC"

    def __call__(self):
        return "SFPBTC"


SFPBTC = SFPBTC()


@dataclass(slots=True, frozen=True)
class SFPBUSD:
    name: str = "SFPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "SFPBUSD"

    def __str__(self):
        return "SFPBUSD"

    def __call__(self):
        return "SFPBUSD"


SFPBUSD = SFPBUSD()


@dataclass(slots=True, frozen=True)
class SFPUSDT:
    name: str = "SFPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "SFPUSDT"

    def __str__(self):
        return "SFPUSDT"

    def __call__(self):
        return "SFPUSDT"


SFPUSDT = SFPUSDT()


@dataclass(slots=True, frozen=True)
class SHIBAUD:
    name: str = "SHIBAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = False

    def __repr__(self):
        return "SHIBAUD"

    def __str__(self):
        return "SHIBAUD"

    def __call__(self):
        return "SHIBAUD"


SHIBAUD = SHIBAUD()


@dataclass(slots=True, frozen=True)
class SHIBBRL:
    name: str = "SHIBBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = False

    def __repr__(self):
        return "SHIBBRL"

    def __str__(self):
        return "SHIBBRL"

    def __call__(self):
        return "SHIBBRL"


SHIBBRL = SHIBBRL()


@dataclass(slots=True, frozen=True)
class SHIBBUSD:
    name: str = "SHIBBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = True

    def __repr__(self):
        return "SHIBBUSD"

    def __str__(self):
        return "SHIBBUSD"

    def __call__(self):
        return "SHIBBUSD"


SHIBBUSD = SHIBBUSD()


@dataclass(slots=True, frozen=True)
class SHIBDOGE:
    name: str = "SHIBDOGE"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = True

    def __repr__(self):
        return "SHIBDOGE"

    def __str__(self):
        return "SHIBDOGE"

    def __call__(self):
        return "SHIBDOGE"


SHIBDOGE = SHIBDOGE()


@dataclass(slots=True, frozen=True)
class SHIBEUR:
    name: str = "SHIBEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = False

    def __repr__(self):
        return "SHIBEUR"

    def __str__(self):
        return "SHIBEUR"

    def __call__(self):
        return "SHIBEUR"


SHIBEUR = SHIBEUR()


@dataclass(slots=True, frozen=True)
class SHIBGBP:
    name: str = "SHIBGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = False

    def __repr__(self):
        return "SHIBGBP"

    def __str__(self):
        return "SHIBGBP"

    def __call__(self):
        return "SHIBGBP"


SHIBGBP = SHIBGBP()


@dataclass(slots=True, frozen=True)
class SHIBRUB:
    name: str = "SHIBRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = False

    def __repr__(self):
        return "SHIBRUB"

    def __str__(self):
        return "SHIBRUB"

    def __call__(self):
        return "SHIBRUB"


SHIBRUB = SHIBRUB()


@dataclass(slots=True, frozen=True)
class SHIBTRY:
    name: str = "SHIBTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = False

    def __repr__(self):
        return "SHIBTRY"

    def __str__(self):
        return "SHIBTRY"

    def __call__(self):
        return "SHIBTRY"


SHIBTRY = SHIBTRY()


@dataclass(slots=True, frozen=True)
class SHIBUAH:
    name: str = "SHIBUAH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 92141578.00
    margin: bool = False

    def __repr__(self):
        return "SHIBUAH"

    def __str__(self):
        return "SHIBUAH"

    def __call__(self):
        return "SHIBUAH"


SHIBUAH = SHIBUAH()


@dataclass(slots=True, frozen=True)
class SHIBUSDT:
    name: str = "SHIBUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = True

    def __repr__(self):
        return "SHIBUSDT"

    def __str__(self):
        return "SHIBUSDT"

    def __call__(self):
        return "SHIBUSDT"


SHIBUSDT = SHIBUSDT()


@dataclass(slots=True, frozen=True)
class SKLBTC:
    name: str = "SKLBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SKLBTC"

    def __str__(self):
        return "SKLBTC"

    def __call__(self):
        return "SKLBTC"


SKLBTC = SKLBTC()


@dataclass(slots=True, frozen=True)
class SKLBUSD:
    name: str = "SKLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SKLBUSD"

    def __str__(self):
        return "SKLBUSD"

    def __call__(self):
        return "SKLBUSD"


SKLBUSD = SKLBUSD()


@dataclass(slots=True, frozen=True)
class SKLUSDT:
    name: str = "SKLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SKLUSDT"

    def __str__(self):
        return "SKLUSDT"

    def __call__(self):
        return "SKLUSDT"


SKLUSDT = SKLUSDT()


@dataclass(slots=True, frozen=True)
class SKYBNB:
    name: str = "SKYBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SKYBNB"

    def __str__(self):
        return "SKYBNB"

    def __call__(self):
        return "SKYBNB"


SKYBNB = SKYBNB()


@dataclass(slots=True, frozen=True)
class SKYBTC:
    name: str = "SKYBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SKYBTC"

    def __str__(self):
        return "SKYBTC"

    def __call__(self):
        return "SKYBTC"


SKYBTC = SKYBTC()


@dataclass(slots=True, frozen=True)
class SKYETH:
    name: str = "SKYETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SKYETH"

    def __str__(self):
        return "SKYETH"

    def __call__(self):
        return "SKYETH"


SKYETH = SKYETH()


@dataclass(slots=True, frozen=True)
class SLPBIDR:
    name: str = "SLPBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9223362229.00000000
    margin: bool = False

    def __repr__(self):
        return "SLPBIDR"

    def __str__(self):
        return "SLPBIDR"

    def __call__(self):
        return "SLPBIDR"


SLPBIDR = SLPBIDR()


@dataclass(slots=True, frozen=True)
class SLPBNB:
    name: str = "SLPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SLPBNB"

    def __str__(self):
        return "SLPBNB"

    def __call__(self):
        return "SLPBNB"


SLPBNB = SLPBNB()


@dataclass(slots=True, frozen=True)
class SLPBUSD:
    name: str = "SLPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SLPBUSD"

    def __str__(self):
        return "SLPBUSD"

    def __call__(self):
        return "SLPBUSD"


SLPBUSD = SLPBUSD()


@dataclass(slots=True, frozen=True)
class SLPETH:
    name: str = "SLPETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SLPETH"

    def __str__(self):
        return "SLPETH"

    def __call__(self):
        return "SLPETH"


SLPETH = SLPETH()


@dataclass(slots=True, frozen=True)
class SLPTRY:
    name: str = "SLPTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SLPTRY"

    def __str__(self):
        return "SLPTRY"

    def __call__(self):
        return "SLPTRY"


SLPTRY = SLPTRY()


@dataclass(slots=True, frozen=True)
class SLPUSDT:
    name: str = "SLPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SLPUSDT"

    def __str__(self):
        return "SLPUSDT"

    def __call__(self):
        return "SLPUSDT"


SLPUSDT = SLPUSDT()


@dataclass(slots=True, frozen=True)
class SNGLSBTC:
    name: str = "SNGLSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SNGLSBTC"

    def __str__(self):
        return "SNGLSBTC"

    def __call__(self):
        return "SNGLSBTC"


SNGLSBTC = SNGLSBTC()


@dataclass(slots=True, frozen=True)
class SNGLSETH:
    name: str = "SNGLSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SNGLSETH"

    def __str__(self):
        return "SNGLSETH"

    def __call__(self):
        return "SNGLSETH"


SNGLSETH = SNGLSETH()


@dataclass(slots=True, frozen=True)
class SNMBTC:
    name: str = "SNMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SNMBTC"

    def __str__(self):
        return "SNMBTC"

    def __call__(self):
        return "SNMBTC"


SNMBTC = SNMBTC()


@dataclass(slots=True, frozen=True)
class SNMBUSD:
    name: str = "SNMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "SNMBUSD"

    def __str__(self):
        return "SNMBUSD"

    def __call__(self):
        return "SNMBUSD"


SNMBUSD = SNMBUSD()


@dataclass(slots=True, frozen=True)
class SNMETH:
    name: str = "SNMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SNMETH"

    def __str__(self):
        return "SNMETH"

    def __call__(self):
        return "SNMETH"


SNMETH = SNMETH()


@dataclass(slots=True, frozen=True)
class SNTBTC:
    name: str = "SNTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SNTBTC"

    def __str__(self):
        return "SNTBTC"

    def __call__(self):
        return "SNTBTC"


SNTBTC = SNTBTC()


@dataclass(slots=True, frozen=True)
class SNTBUSD:
    name: str = "SNTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SNTBUSD"

    def __str__(self):
        return "SNTBUSD"

    def __call__(self):
        return "SNTBUSD"


SNTBUSD = SNTBUSD()


@dataclass(slots=True, frozen=True)
class SNTETH:
    name: str = "SNTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SNTETH"

    def __str__(self):
        return "SNTETH"

    def __call__(self):
        return "SNTETH"


SNTETH = SNTETH()


@dataclass(slots=True, frozen=True)
class SNXBNB:
    name: str = "SNXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SNXBNB"

    def __str__(self):
        return "SNXBNB"

    def __call__(self):
        return "SNXBNB"


SNXBNB = SNXBNB()


@dataclass(slots=True, frozen=True)
class SNXBTC:
    name: str = "SNXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SNXBTC"

    def __str__(self):
        return "SNXBTC"

    def __call__(self):
        return "SNXBTC"


SNXBTC = SNXBTC()


@dataclass(slots=True, frozen=True)
class SNXBUSD:
    name: str = "SNXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "SNXBUSD"

    def __str__(self):
        return "SNXBUSD"

    def __call__(self):
        return "SNXBUSD"


SNXBUSD = SNXBUSD()


@dataclass(slots=True, frozen=True)
class SNXETH:
    name: str = "SNXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SNXETH"

    def __str__(self):
        return "SNXETH"

    def __call__(self):
        return "SNXETH"


SNXETH = SNXETH()


@dataclass(slots=True, frozen=True)
class SNXUSDT:
    name: str = "SNXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "SNXUSDT"

    def __str__(self):
        return "SNXUSDT"

    def __call__(self):
        return "SNXUSDT"


SNXUSDT = SNXUSDT()


@dataclass(slots=True, frozen=True)
class SOLAUD:
    name: str = "SOLAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLAUD"

    def __str__(self):
        return "SOLAUD"

    def __call__(self):
        return "SOLAUD"


SOLAUD = SOLAUD()


@dataclass(slots=True, frozen=True)
class SOLBIDR:
    name: str = "SOLBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9223372.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLBIDR"

    def __str__(self):
        return "SOLBIDR"

    def __call__(self):
        return "SOLBIDR"


SOLBIDR = SOLBIDR()


@dataclass(slots=True, frozen=True)
class SOLBNB:
    name: str = "SOLBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLBNB"

    def __str__(self):
        return "SOLBNB"

    def __call__(self):
        return "SOLBNB"


SOLBNB = SOLBNB()


@dataclass(slots=True, frozen=True)
class SOLBRL:
    name: str = "SOLBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLBRL"

    def __str__(self):
        return "SOLBRL"

    def __call__(self):
        return "SOLBRL"


SOLBRL = SOLBRL()


@dataclass(slots=True, frozen=True)
class SOLBTC:
    name: str = "SOLBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SOLBTC"

    def __str__(self):
        return "SOLBTC"

    def __call__(self):
        return "SOLBTC"


SOLBTC = SOLBTC()


@dataclass(slots=True, frozen=True)
class SOLBUSD:
    name: str = "SOLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "SOLBUSD"

    def __str__(self):
        return "SOLBUSD"

    def __call__(self):
        return "SOLBUSD"


SOLBUSD = SOLBUSD()


@dataclass(slots=True, frozen=True)
class SOLETH:
    name: str = "SOLETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLETH"

    def __str__(self):
        return "SOLETH"

    def __call__(self):
        return "SOLETH"


SOLETH = SOLETH()


@dataclass(slots=True, frozen=True)
class SOLEUR:
    name: str = "SOLEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222440.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLEUR"

    def __str__(self):
        return "SOLEUR"

    def __call__(self):
        return "SOLEUR"


SOLEUR = SOLEUR()


@dataclass(slots=True, frozen=True)
class SOLGBP:
    name: str = "SOLGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLGBP"

    def __str__(self):
        return "SOLGBP"

    def __call__(self):
        return "SOLGBP"


SOLGBP = SOLGBP()


@dataclass(slots=True, frozen=True)
class SOLRUB:
    name: str = "SOLRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLRUB"

    def __str__(self):
        return "SOLRUB"

    def __call__(self):
        return "SOLRUB"


SOLRUB = SOLRUB()


@dataclass(slots=True, frozen=True)
class SOLTRY:
    name: str = "SOLTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 3074353.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLTRY"

    def __str__(self):
        return "SOLTRY"

    def __call__(self):
        return "SOLTRY"


SOLTRY = SOLTRY()


@dataclass(slots=True, frozen=True)
class SOLUSDC:
    name: str = "SOLUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "SOLUSDC"

    def __str__(self):
        return "SOLUSDC"

    def __call__(self):
        return "SOLUSDC"


SOLUSDC = SOLUSDC()


@dataclass(slots=True, frozen=True)
class SOLUSDT:
    name: str = "SOLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "SOLUSDT"

    def __str__(self):
        return "SOLUSDT"

    def __call__(self):
        return "SOLUSDT"


SOLUSDT = SOLUSDT()


@dataclass(slots=True, frozen=True)
class SPARTABNB:
    name: str = "SPARTABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SPARTABNB"

    def __str__(self):
        return "SPARTABNB"

    def __call__(self):
        return "SPARTABNB"


SPARTABNB = SPARTABNB()


@dataclass(slots=True, frozen=True)
class SPELLBNB:
    name: str = "SPELLBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SPELLBNB"

    def __str__(self):
        return "SPELLBNB"

    def __call__(self):
        return "SPELLBNB"


SPELLBNB = SPELLBNB()


@dataclass(slots=True, frozen=True)
class SPELLBTC:
    name: str = "SPELLBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SPELLBTC"

    def __str__(self):
        return "SPELLBTC"

    def __call__(self):
        return "SPELLBTC"


SPELLBTC = SPELLBTC()


@dataclass(slots=True, frozen=True)
class SPELLBUSD:
    name: str = "SPELLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "SPELLBUSD"

    def __str__(self):
        return "SPELLBUSD"

    def __call__(self):
        return "SPELLBUSD"


SPELLBUSD = SPELLBUSD()


@dataclass(slots=True, frozen=True)
class SPELLTRY:
    name: str = "SPELLTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SPELLTRY"

    def __str__(self):
        return "SPELLTRY"

    def __call__(self):
        return "SPELLTRY"


SPELLTRY = SPELLTRY()


@dataclass(slots=True, frozen=True)
class SPELLUSDT:
    name: str = "SPELLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "SPELLUSDT"

    def __str__(self):
        return "SPELLUSDT"

    def __call__(self):
        return "SPELLUSDT"


SPELLUSDT = SPELLUSDT()


@dataclass(slots=True, frozen=True)
class SRMBIDR:
    name: str = "SRMBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "SRMBIDR"

    def __str__(self):
        return "SRMBIDR"

    def __call__(self):
        return "SRMBIDR"


SRMBIDR = SRMBIDR()


@dataclass(slots=True, frozen=True)
class SRMBNB:
    name: str = "SRMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SRMBNB"

    def __str__(self):
        return "SRMBNB"

    def __call__(self):
        return "SRMBNB"


SRMBNB = SRMBNB()


@dataclass(slots=True, frozen=True)
class SRMBTC:
    name: str = "SRMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SRMBTC"

    def __str__(self):
        return "SRMBTC"

    def __call__(self):
        return "SRMBTC"


SRMBTC = SRMBTC()


@dataclass(slots=True, frozen=True)
class SRMBUSD:
    name: str = "SRMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "SRMBUSD"

    def __str__(self):
        return "SRMBUSD"

    def __call__(self):
        return "SRMBUSD"


SRMBUSD = SRMBUSD()


@dataclass(slots=True, frozen=True)
class SRMUSDT:
    name: str = "SRMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "SRMUSDT"

    def __str__(self):
        return "SRMUSDT"

    def __call__(self):
        return "SRMUSDT"


SRMUSDT = SRMUSDT()


@dataclass(slots=True, frozen=True)
class SSVBTC:
    name: str = "SSVBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SSVBTC"

    def __str__(self):
        return "SSVBTC"

    def __call__(self):
        return "SSVBTC"


SSVBTC = SSVBTC()


@dataclass(slots=True, frozen=True)
class SSVBUSD:
    name: str = "SSVBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "SSVBUSD"

    def __str__(self):
        return "SSVBUSD"

    def __call__(self):
        return "SSVBUSD"


SSVBUSD = SSVBUSD()


@dataclass(slots=True, frozen=True)
class SSVETH:
    name: str = "SSVETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SSVETH"

    def __str__(self):
        return "SSVETH"

    def __call__(self):
        return "SSVETH"


SSVETH = SSVETH()


@dataclass(slots=True, frozen=True)
class STEEMBNB:
    name: str = "STEEMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STEEMBNB"

    def __str__(self):
        return "STEEMBNB"

    def __call__(self):
        return "STEEMBNB"


STEEMBNB = STEEMBNB()


@dataclass(slots=True, frozen=True)
class STEEMBTC:
    name: str = "STEEMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STEEMBTC"

    def __str__(self):
        return "STEEMBTC"

    def __call__(self):
        return "STEEMBTC"


STEEMBTC = STEEMBTC()


@dataclass(slots=True, frozen=True)
class STEEMBUSD:
    name: str = "STEEMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "STEEMBUSD"

    def __str__(self):
        return "STEEMBUSD"

    def __call__(self):
        return "STEEMBUSD"


STEEMBUSD = STEEMBUSD()


@dataclass(slots=True, frozen=True)
class STEEMETH:
    name: str = "STEEMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STEEMETH"

    def __str__(self):
        return "STEEMETH"

    def __call__(self):
        return "STEEMETH"


STEEMETH = STEEMETH()


@dataclass(slots=True, frozen=True)
class STEEMUSDT:
    name: str = "STEEMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "STEEMUSDT"

    def __str__(self):
        return "STEEMUSDT"

    def __call__(self):
        return "STEEMUSDT"


STEEMUSDT = STEEMUSDT()


@dataclass(slots=True, frozen=True)
class STGBTC:
    name: str = "STGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "STGBTC"

    def __str__(self):
        return "STGBTC"

    def __call__(self):
        return "STGBTC"


STGBTC = STGBTC()


@dataclass(slots=True, frozen=True)
class STGBUSD:
    name: str = "STGBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = True

    def __repr__(self):
        return "STGBUSD"

    def __str__(self):
        return "STGBUSD"

    def __call__(self):
        return "STGBUSD"


STGBUSD = STGBUSD()


@dataclass(slots=True, frozen=True)
class STGUSDT:
    name: str = "STGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = True

    def __repr__(self):
        return "STGUSDT"

    def __str__(self):
        return "STGUSDT"

    def __call__(self):
        return "STGUSDT"


STGUSDT = STGUSDT()


@dataclass(slots=True, frozen=True)
class STMXBTC:
    name: str = "STMXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "STMXBTC"

    def __str__(self):
        return "STMXBTC"

    def __call__(self):
        return "STMXBTC"


STMXBTC = STMXBTC()


@dataclass(slots=True, frozen=True)
class STMXBUSD:
    name: str = "STMXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "STMXBUSD"

    def __str__(self):
        return "STMXBUSD"

    def __call__(self):
        return "STMXBUSD"


STMXBUSD = STMXBUSD()


@dataclass(slots=True, frozen=True)
class STMXETH:
    name: str = "STMXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STMXETH"

    def __str__(self):
        return "STMXETH"

    def __call__(self):
        return "STMXETH"


STMXETH = STMXETH()


@dataclass(slots=True, frozen=True)
class STMXUSDT:
    name: str = "STMXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "STMXUSDT"

    def __str__(self):
        return "STMXUSDT"

    def __call__(self):
        return "STMXUSDT"


STMXUSDT = STMXUSDT()


@dataclass(slots=True, frozen=True)
class STORJBTC:
    name: str = "STORJBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "STORJBTC"

    def __str__(self):
        return "STORJBTC"

    def __call__(self):
        return "STORJBTC"


STORJBTC = STORJBTC()


@dataclass(slots=True, frozen=True)
class STORJBUSD:
    name: str = "STORJBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222448.00000000
    margin: bool = False

    def __repr__(self):
        return "STORJBUSD"

    def __str__(self):
        return "STORJBUSD"

    def __call__(self):
        return "STORJBUSD"


STORJBUSD = STORJBUSD()


@dataclass(slots=True, frozen=True)
class STORJETH:
    name: str = "STORJETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STORJETH"

    def __str__(self):
        return "STORJETH"

    def __call__(self):
        return "STORJETH"


STORJETH = STORJETH()


@dataclass(slots=True, frozen=True)
class STORJTRY:
    name: str = "STORJTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "STORJTRY"

    def __str__(self):
        return "STORJTRY"

    def __call__(self):
        return "STORJTRY"


STORJTRY = STORJTRY()


@dataclass(slots=True, frozen=True)
class STORJUSDT:
    name: str = "STORJUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "STORJUSDT"

    def __str__(self):
        return "STORJUSDT"

    def __call__(self):
        return "STORJUSDT"


STORJUSDT = STORJUSDT()


@dataclass(slots=True, frozen=True)
class STORMBNB:
    name: str = "STORMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "STORMBNB"

    def __str__(self):
        return "STORMBNB"

    def __call__(self):
        return "STORMBNB"


STORMBNB = STORMBNB()


@dataclass(slots=True, frozen=True)
class STORMBTC:
    name: str = "STORMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "STORMBTC"

    def __str__(self):
        return "STORMBTC"

    def __call__(self):
        return "STORMBTC"


STORMBTC = STORMBTC()


@dataclass(slots=True, frozen=True)
class STORMETH:
    name: str = "STORMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STORMETH"

    def __str__(self):
        return "STORMETH"

    def __call__(self):
        return "STORMETH"


STORMETH = STORMETH()


@dataclass(slots=True, frozen=True)
class STORMUSDT:
    name: str = "STORMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "STORMUSDT"

    def __str__(self):
        return "STORMUSDT"

    def __call__(self):
        return "STORMUSDT"


STORMUSDT = STORMUSDT()


@dataclass(slots=True, frozen=True)
class STPTBNB:
    name: str = "STPTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STPTBNB"

    def __str__(self):
        return "STPTBNB"

    def __call__(self):
        return "STPTBNB"


STPTBNB = STPTBNB()


@dataclass(slots=True, frozen=True)
class STPTBTC:
    name: str = "STPTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STPTBTC"

    def __str__(self):
        return "STPTBTC"

    def __call__(self):
        return "STPTBTC"


STPTBTC = STPTBTC()


@dataclass(slots=True, frozen=True)
class STPTBUSD:
    name: str = "STPTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "STPTBUSD"

    def __str__(self):
        return "STPTBUSD"

    def __call__(self):
        return "STPTBUSD"


STPTBUSD = STPTBUSD()


@dataclass(slots=True, frozen=True)
class STPTUSDT:
    name: str = "STPTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STPTUSDT"

    def __str__(self):
        return "STPTUSDT"

    def __call__(self):
        return "STPTUSDT"


STPTUSDT = STPTUSDT()


@dataclass(slots=True, frozen=True)
class STRATBNB:
    name: str = "STRATBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STRATBNB"

    def __str__(self):
        return "STRATBNB"

    def __call__(self):
        return "STRATBNB"


STRATBNB = STRATBNB()


@dataclass(slots=True, frozen=True)
class STRATBTC:
    name: str = "STRATBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STRATBTC"

    def __str__(self):
        return "STRATBTC"

    def __call__(self):
        return "STRATBTC"


STRATBTC = STRATBTC()


@dataclass(slots=True, frozen=True)
class STRATBUSD:
    name: str = "STRATBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "STRATBUSD"

    def __str__(self):
        return "STRATBUSD"

    def __call__(self):
        return "STRATBUSD"


STRATBUSD = STRATBUSD()


@dataclass(slots=True, frozen=True)
class STRATETH:
    name: str = "STRATETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STRATETH"

    def __str__(self):
        return "STRATETH"

    def __call__(self):
        return "STRATETH"


STRATETH = STRATETH()


@dataclass(slots=True, frozen=True)
class STRATUSDT:
    name: str = "STRATUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "STRATUSDT"

    def __str__(self):
        return "STRATUSDT"

    def __call__(self):
        return "STRATUSDT"


STRATUSDT = STRATUSDT()


@dataclass(slots=True, frozen=True)
class STRAXBTC:
    name: str = "STRAXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STRAXBTC"

    def __str__(self):
        return "STRAXBTC"

    def __call__(self):
        return "STRAXBTC"


STRAXBTC = STRAXBTC()


@dataclass(slots=True, frozen=True)
class STRAXBUSD:
    name: str = "STRAXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "STRAXBUSD"

    def __str__(self):
        return "STRAXBUSD"

    def __call__(self):
        return "STRAXBUSD"


STRAXBUSD = STRAXBUSD()


@dataclass(slots=True, frozen=True)
class STRAXETH:
    name: str = "STRAXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STRAXETH"

    def __str__(self):
        return "STRAXETH"

    def __call__(self):
        return "STRAXETH"


STRAXETH = STRAXETH()


@dataclass(slots=True, frozen=True)
class STRAXUSDT:
    name: str = "STRAXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "STRAXUSDT"

    def __str__(self):
        return "STRAXUSDT"

    def __call__(self):
        return "STRAXUSDT"


STRAXUSDT = STRAXUSDT()


@dataclass(slots=True, frozen=True)
class STXBNB:
    name: str = "STXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "STXBNB"

    def __str__(self):
        return "STXBNB"

    def __call__(self):
        return "STXBNB"


STXBNB = STXBNB()


@dataclass(slots=True, frozen=True)
class STXBTC:
    name: str = "STXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "STXBTC"

    def __str__(self):
        return "STXBTC"

    def __call__(self):
        return "STXBTC"


STXBTC = STXBTC()


@dataclass(slots=True, frozen=True)
class STXBUSD:
    name: str = "STXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "STXBUSD"

    def __str__(self):
        return "STXBUSD"

    def __call__(self):
        return "STXBUSD"


STXBUSD = STXBUSD()


@dataclass(slots=True, frozen=True)
class STXUSDT:
    name: str = "STXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "STXUSDT"

    def __str__(self):
        return "STXUSDT"

    def __call__(self):
        return "STXUSDT"


STXUSDT = STXUSDT()


@dataclass(slots=True, frozen=True)
class SUBBTC:
    name: str = "SUBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SUBBTC"

    def __str__(self):
        return "SUBBTC"

    def __call__(self):
        return "SUBBTC"


SUBBTC = SUBBTC()


@dataclass(slots=True, frozen=True)
class SUBETH:
    name: str = "SUBETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SUBETH"

    def __str__(self):
        return "SUBETH"

    def __call__(self):
        return "SUBETH"


SUBETH = SUBETH()


@dataclass(slots=True, frozen=True)
class SUNBTC:
    name: str = "SUNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SUNBTC"

    def __str__(self):
        return "SUNBTC"

    def __call__(self):
        return "SUNBTC"


SUNBTC = SUNBTC()


@dataclass(slots=True, frozen=True)
class SUNBUSD:
    name: str = "SUNBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "SUNBUSD"

    def __str__(self):
        return "SUNBUSD"

    def __call__(self):
        return "SUNBUSD"


SUNBUSD = SUNBUSD()


@dataclass(slots=True, frozen=True)
class SUNUSDT:
    name: str = "SUNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "SUNUSDT"

    def __str__(self):
        return "SUNUSDT"

    def __call__(self):
        return "SUNUSDT"


SUNUSDT = SUNUSDT()


@dataclass(slots=True, frozen=True)
class SUPERBTC:
    name: str = "SUPERBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SUPERBTC"

    def __str__(self):
        return "SUPERBTC"

    def __call__(self):
        return "SUPERBTC"


SUPERBTC = SUPERBTC()


@dataclass(slots=True, frozen=True)
class SUPERBUSD:
    name: str = "SUPERBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "SUPERBUSD"

    def __str__(self):
        return "SUPERBUSD"

    def __call__(self):
        return "SUPERBUSD"


SUPERBUSD = SUPERBUSD()


@dataclass(slots=True, frozen=True)
class SUPERUSDT:
    name: str = "SUPERUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "SUPERUSDT"

    def __str__(self):
        return "SUPERUSDT"

    def __call__(self):
        return "SUPERUSDT"


SUPERUSDT = SUPERUSDT()


@dataclass(slots=True, frozen=True)
class SUSDBTC:
    name: str = "SUSDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SUSDBTC"

    def __str__(self):
        return "SUSDBTC"

    def __call__(self):
        return "SUSDBTC"


SUSDBTC = SUSDBTC()


@dataclass(slots=True, frozen=True)
class SUSDETH:
    name: str = "SUSDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SUSDETH"

    def __str__(self):
        return "SUSDETH"

    def __call__(self):
        return "SUSDETH"


SUSDETH = SUSDETH()


@dataclass(slots=True, frozen=True)
class SUSDUSDT:
    name: str = "SUSDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "SUSDUSDT"

    def __str__(self):
        return "SUSDUSDT"

    def __call__(self):
        return "SUSDUSDT"


SUSDUSDT = SUSDUSDT()


@dataclass(slots=True, frozen=True)
class SUSHIBNB:
    name: str = "SUSHIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SUSHIBNB"

    def __str__(self):
        return "SUSHIBNB"

    def __call__(self):
        return "SUSHIBNB"


SUSHIBNB = SUSHIBNB()


@dataclass(slots=True, frozen=True)
class SUSHIBTC:
    name: str = "SUSHIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SUSHIBTC"

    def __str__(self):
        return "SUSHIBTC"

    def __call__(self):
        return "SUSHIBTC"


SUSHIBTC = SUSHIBTC()


@dataclass(slots=True, frozen=True)
class SUSHIBUSD:
    name: str = "SUSHIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "SUSHIBUSD"

    def __str__(self):
        return "SUSHIBUSD"

    def __call__(self):
        return "SUSHIBUSD"


SUSHIBUSD = SUSHIBUSD()


@dataclass(slots=True, frozen=True)
class SUSHIDOWNUSDT:
    name: str = "SUSHIDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 19998638.00000000
    margin: bool = False

    def __repr__(self):
        return "SUSHIDOWNUSDT"

    def __str__(self):
        return "SUSHIDOWNUSDT"

    def __call__(self):
        return "SUSHIDOWNUSDT"


SUSHIDOWNUSDT = SUSHIDOWNUSDT()


@dataclass(slots=True, frozen=True)
class SUSHIUPUSDT:
    name: str = "SUSHIUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 150000.00000000
    margin: bool = False

    def __repr__(self):
        return "SUSHIUPUSDT"

    def __str__(self):
        return "SUSHIUPUSDT"

    def __call__(self):
        return "SUSHIUPUSDT"


SUSHIUPUSDT = SUSHIUPUSDT()


@dataclass(slots=True, frozen=True)
class SUSHIUSDT:
    name: str = "SUSHIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "SUSHIUSDT"

    def __str__(self):
        return "SUSHIUSDT"

    def __call__(self):
        return "SUSHIUSDT"


SUSHIUSDT = SUSHIUSDT()


@dataclass(slots=True, frozen=True)
class SWRVBNB:
    name: str = "SWRVBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SWRVBNB"

    def __str__(self):
        return "SWRVBNB"

    def __call__(self):
        return "SWRVBNB"


SWRVBNB = SWRVBNB()


@dataclass(slots=True, frozen=True)
class SWRVBUSD:
    name: str = "SWRVBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "SWRVBUSD"

    def __str__(self):
        return "SWRVBUSD"

    def __call__(self):
        return "SWRVBUSD"


SWRVBUSD = SWRVBUSD()


@dataclass(slots=True, frozen=True)
class SXPAUD:
    name: str = "SXPAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "SXPAUD"

    def __str__(self):
        return "SXPAUD"

    def __call__(self):
        return "SXPAUD"


SXPAUD = SXPAUD()


@dataclass(slots=True, frozen=True)
class SXPBIDR:
    name: str = "SXPBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 1000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SXPBIDR"

    def __str__(self):
        return "SXPBIDR"

    def __call__(self):
        return "SXPBIDR"


SXPBIDR = SXPBIDR()


@dataclass(slots=True, frozen=True)
class SXPBNB:
    name: str = "SXPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SXPBNB"

    def __str__(self):
        return "SXPBNB"

    def __call__(self):
        return "SXPBNB"


SXPBNB = SXPBNB()


@dataclass(slots=True, frozen=True)
class SXPBTC:
    name: str = "SXPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "SXPBTC"

    def __str__(self):
        return "SXPBTC"

    def __call__(self):
        return "SXPBTC"


SXPBTC = SXPBTC()


@dataclass(slots=True, frozen=True)
class SXPBUSD:
    name: str = "SXPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "SXPBUSD"

    def __str__(self):
        return "SXPBUSD"

    def __call__(self):
        return "SXPBUSD"


SXPBUSD = SXPBUSD()


@dataclass(slots=True, frozen=True)
class SXPDOWNUSDT:
    name: str = "SXPDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 100000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SXPDOWNUSDT"

    def __str__(self):
        return "SXPDOWNUSDT"

    def __call__(self):
        return "SXPDOWNUSDT"


SXPDOWNUSDT = SXPDOWNUSDT()


@dataclass(slots=True, frozen=True)
class SXPEUR:
    name: str = "SXPEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "SXPEUR"

    def __str__(self):
        return "SXPEUR"

    def __call__(self):
        return "SXPEUR"


SXPEUR = SXPEUR()


@dataclass(slots=True, frozen=True)
class SXPGBP:
    name: str = "SXPGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "SXPGBP"

    def __str__(self):
        return "SXPGBP"

    def __call__(self):
        return "SXPGBP"


SXPGBP = SXPGBP()


@dataclass(slots=True, frozen=True)
class SXPTRY:
    name: str = "SXPTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "SXPTRY"

    def __str__(self):
        return "SXPTRY"

    def __call__(self):
        return "SXPTRY"


SXPTRY = SXPTRY()


@dataclass(slots=True, frozen=True)
class SXPUPUSDT:
    name: str = "SXPUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "SXPUPUSDT"

    def __str__(self):
        return "SXPUPUSDT"

    def __call__(self):
        return "SXPUPUSDT"


SXPUPUSDT = SXPUPUSDT()


@dataclass(slots=True, frozen=True)
class SXPUSDT:
    name: str = "SXPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = True

    def __repr__(self):
        return "SXPUSDT"

    def __str__(self):
        return "SXPUSDT"

    def __call__(self):
        return "SXPUSDT"


SXPUSDT = SXPUSDT()


@dataclass(slots=True, frozen=True)
class SYSBNB:
    name: str = "SYSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SYSBNB"

    def __str__(self):
        return "SYSBNB"

    def __call__(self):
        return "SYSBNB"


SYSBNB = SYSBNB()


@dataclass(slots=True, frozen=True)
class SYSBTC:
    name: str = "SYSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SYSBTC"

    def __str__(self):
        return "SYSBTC"

    def __call__(self):
        return "SYSBTC"


SYSBTC = SYSBTC()


@dataclass(slots=True, frozen=True)
class SYSBUSD:
    name: str = "SYSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SYSBUSD"

    def __str__(self):
        return "SYSBUSD"

    def __call__(self):
        return "SYSBUSD"


SYSBUSD = SYSBUSD()


@dataclass(slots=True, frozen=True)
class SYSETH:
    name: str = "SYSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "SYSETH"

    def __str__(self):
        return "SYSETH"

    def __call__(self):
        return "SYSETH"


SYSETH = SYSETH()


@dataclass(slots=True, frozen=True)
class SYSUSDT:
    name: str = "SYSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "SYSUSDT"

    def __str__(self):
        return "SYSUSDT"

    def __call__(self):
        return "SYSUSDT"


SYSUSDT = SYSUSDT()


@dataclass(slots=True, frozen=True)
class TBUSD:
    name: str = "TBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TBUSD"

    def __str__(self):
        return "TBUSD"

    def __call__(self):
        return "TBUSD"


TBUSD = TBUSD()


@dataclass(slots=True, frozen=True)
class TCTBNB:
    name: str = "TCTBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TCTBNB"

    def __str__(self):
        return "TCTBNB"

    def __call__(self):
        return "TCTBNB"


TCTBNB = TCTBNB()


@dataclass(slots=True, frozen=True)
class TCTBTC:
    name: str = "TCTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TCTBTC"

    def __str__(self):
        return "TCTBTC"

    def __call__(self):
        return "TCTBTC"


TCTBTC = TCTBTC()


@dataclass(slots=True, frozen=True)
class TCTUSDT:
    name: str = "TCTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TCTUSDT"

    def __str__(self):
        return "TCTUSDT"

    def __call__(self):
        return "TCTUSDT"


TCTUSDT = TCTUSDT()


@dataclass(slots=True, frozen=True)
class TFUELBNB:
    name: str = "TFUELBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TFUELBNB"

    def __str__(self):
        return "TFUELBNB"

    def __call__(self):
        return "TFUELBNB"


TFUELBNB = TFUELBNB()


@dataclass(slots=True, frozen=True)
class TFUELBTC:
    name: str = "TFUELBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TFUELBTC"

    def __str__(self):
        return "TFUELBTC"

    def __call__(self):
        return "TFUELBTC"


TFUELBTC = TFUELBTC()


@dataclass(slots=True, frozen=True)
class TFUELBUSD:
    name: str = "TFUELBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TFUELBUSD"

    def __str__(self):
        return "TFUELBUSD"

    def __call__(self):
        return "TFUELBUSD"


TFUELBUSD = TFUELBUSD()


@dataclass(slots=True, frozen=True)
class TFUELPAX:
    name: str = "TFUELPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TFUELPAX"

    def __str__(self):
        return "TFUELPAX"

    def __call__(self):
        return "TFUELPAX"


TFUELPAX = TFUELPAX()


@dataclass(slots=True, frozen=True)
class TFUELTUSD:
    name: str = "TFUELTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TFUELTUSD"

    def __str__(self):
        return "TFUELTUSD"

    def __call__(self):
        return "TFUELTUSD"


TFUELTUSD = TFUELTUSD()


@dataclass(slots=True, frozen=True)
class TFUELUSDC:
    name: str = "TFUELUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TFUELUSDC"

    def __str__(self):
        return "TFUELUSDC"

    def __call__(self):
        return "TFUELUSDC"


TFUELUSDC = TFUELUSDC()


@dataclass(slots=True, frozen=True)
class TFUELUSDT:
    name: str = "TFUELUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TFUELUSDT"

    def __str__(self):
        return "TFUELUSDT"

    def __call__(self):
        return "TFUELUSDT"


TFUELUSDT = TFUELUSDT()


@dataclass(slots=True, frozen=True)
class THETABNB:
    name: str = "THETABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "THETABNB"

    def __str__(self):
        return "THETABNB"

    def __call__(self):
        return "THETABNB"


THETABNB = THETABNB()


@dataclass(slots=True, frozen=True)
class THETABTC:
    name: str = "THETABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "THETABTC"

    def __str__(self):
        return "THETABTC"

    def __call__(self):
        return "THETABTC"


THETABTC = THETABTC()


@dataclass(slots=True, frozen=True)
class THETABUSD:
    name: str = "THETABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "THETABUSD"

    def __str__(self):
        return "THETABUSD"

    def __call__(self):
        return "THETABUSD"


THETABUSD = THETABUSD()


@dataclass(slots=True, frozen=True)
class THETAETH:
    name: str = "THETAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "THETAETH"

    def __str__(self):
        return "THETAETH"

    def __call__(self):
        return "THETAETH"


THETAETH = THETAETH()


@dataclass(slots=True, frozen=True)
class THETAEUR:
    name: str = "THETAEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "THETAEUR"

    def __str__(self):
        return "THETAEUR"

    def __call__(self):
        return "THETAEUR"


THETAEUR = THETAEUR()


@dataclass(slots=True, frozen=True)
class THETAUSDT:
    name: str = "THETAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "THETAUSDT"

    def __str__(self):
        return "THETAUSDT"

    def __call__(self):
        return "THETAUSDT"


THETAUSDT = THETAUSDT()


@dataclass(slots=True, frozen=True)
class TKOBIDR:
    name: str = "TKOBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TKOBIDR"

    def __str__(self):
        return "TKOBIDR"

    def __call__(self):
        return "TKOBIDR"


TKOBIDR = TKOBIDR()


@dataclass(slots=True, frozen=True)
class TKOBTC:
    name: str = "TKOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TKOBTC"

    def __str__(self):
        return "TKOBTC"

    def __call__(self):
        return "TKOBTC"


TKOBTC = TKOBTC()


@dataclass(slots=True, frozen=True)
class TKOBUSD:
    name: str = "TKOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "TKOBUSD"

    def __str__(self):
        return "TKOBUSD"

    def __call__(self):
        return "TKOBUSD"


TKOBUSD = TKOBUSD()


@dataclass(slots=True, frozen=True)
class TKOUSDT:
    name: str = "TKOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "TKOUSDT"

    def __str__(self):
        return "TKOUSDT"

    def __call__(self):
        return "TKOUSDT"


TKOUSDT = TKOUSDT()


@dataclass(slots=True, frozen=True)
class TLMBNB:
    name: str = "TLMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TLMBNB"

    def __str__(self):
        return "TLMBNB"

    def __call__(self):
        return "TLMBNB"


TLMBNB = TLMBNB()


@dataclass(slots=True, frozen=True)
class TLMBTC:
    name: str = "TLMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TLMBTC"

    def __str__(self):
        return "TLMBTC"

    def __call__(self):
        return "TLMBTC"


TLMBTC = TLMBTC()


@dataclass(slots=True, frozen=True)
class TLMBUSD:
    name: str = "TLMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "TLMBUSD"

    def __str__(self):
        return "TLMBUSD"

    def __call__(self):
        return "TLMBUSD"


TLMBUSD = TLMBUSD()


@dataclass(slots=True, frozen=True)
class TLMTRY:
    name: str = "TLMTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TLMTRY"

    def __str__(self):
        return "TLMTRY"

    def __call__(self):
        return "TLMTRY"


TLMTRY = TLMTRY()


@dataclass(slots=True, frozen=True)
class TLMUSDT:
    name: str = "TLMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "TLMUSDT"

    def __str__(self):
        return "TLMUSDT"

    def __call__(self):
        return "TLMUSDT"


TLMUSDT = TLMUSDT()


@dataclass(slots=True, frozen=True)
class TNBBTC:
    name: str = "TNBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TNBBTC"

    def __str__(self):
        return "TNBBTC"

    def __call__(self):
        return "TNBBTC"


TNBBTC = TNBBTC()


@dataclass(slots=True, frozen=True)
class TNBETH:
    name: str = "TNBETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TNBETH"

    def __str__(self):
        return "TNBETH"

    def __call__(self):
        return "TNBETH"


TNBETH = TNBETH()


@dataclass(slots=True, frozen=True)
class TNTBTC:
    name: str = "TNTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TNTBTC"

    def __str__(self):
        return "TNTBTC"

    def __call__(self):
        return "TNTBTC"


TNTBTC = TNTBTC()


@dataclass(slots=True, frozen=True)
class TNTETH:
    name: str = "TNTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TNTETH"

    def __str__(self):
        return "TNTETH"

    def __call__(self):
        return "TNTETH"


TNTETH = TNTETH()


@dataclass(slots=True, frozen=True)
class TOMOBNB:
    name: str = "TOMOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TOMOBNB"

    def __str__(self):
        return "TOMOBNB"

    def __call__(self):
        return "TOMOBNB"


TOMOBNB = TOMOBNB()


@dataclass(slots=True, frozen=True)
class TOMOBTC:
    name: str = "TOMOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TOMOBTC"

    def __str__(self):
        return "TOMOBTC"

    def __call__(self):
        return "TOMOBTC"


TOMOBTC = TOMOBTC()


@dataclass(slots=True, frozen=True)
class TOMOBUSD:
    name: str = "TOMOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "TOMOBUSD"

    def __str__(self):
        return "TOMOBUSD"

    def __call__(self):
        return "TOMOBUSD"


TOMOBUSD = TOMOBUSD()


@dataclass(slots=True, frozen=True)
class TOMOUSDC:
    name: str = "TOMOUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "TOMOUSDC"

    def __str__(self):
        return "TOMOUSDC"

    def __call__(self):
        return "TOMOUSDC"


TOMOUSDC = TOMOUSDC()


@dataclass(slots=True, frozen=True)
class TOMOUSDT:
    name: str = "TOMOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "TOMOUSDT"

    def __str__(self):
        return "TOMOUSDT"

    def __call__(self):
        return "TOMOUSDT"


TOMOUSDT = TOMOUSDT()


@dataclass(slots=True, frozen=True)
class TORNBNB:
    name: str = "TORNBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "TORNBNB"

    def __str__(self):
        return "TORNBNB"

    def __call__(self):
        return "TORNBNB"


TORNBNB = TORNBNB()


@dataclass(slots=True, frozen=True)
class TORNBTC:
    name: str = "TORNBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TORNBTC"

    def __str__(self):
        return "TORNBTC"

    def __call__(self):
        return "TORNBTC"


TORNBTC = TORNBTC()


@dataclass(slots=True, frozen=True)
class TORNBUSD:
    name: str = "TORNBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "TORNBUSD"

    def __str__(self):
        return "TORNBUSD"

    def __call__(self):
        return "TORNBUSD"


TORNBUSD = TORNBUSD()


@dataclass(slots=True, frozen=True)
class TORNUSDT:
    name: str = "TORNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "TORNUSDT"

    def __str__(self):
        return "TORNUSDT"

    def __call__(self):
        return "TORNUSDT"


TORNUSDT = TORNUSDT()


@dataclass(slots=True, frozen=True)
class TRBBNB:
    name: str = "TRBBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRBBNB"

    def __str__(self):
        return "TRBBNB"

    def __call__(self):
        return "TRBBNB"


TRBBNB = TRBBNB()


@dataclass(slots=True, frozen=True)
class TRBBTC:
    name: str = "TRBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TRBBTC"

    def __str__(self):
        return "TRBBTC"

    def __call__(self):
        return "TRBBTC"


TRBBTC = TRBBTC()


@dataclass(slots=True, frozen=True)
class TRBBUSD:
    name: str = "TRBBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "TRBBUSD"

    def __str__(self):
        return "TRBBUSD"

    def __call__(self):
        return "TRBBUSD"


TRBBUSD = TRBBUSD()


@dataclass(slots=True, frozen=True)
class TRBUSDT:
    name: str = "TRBUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "TRBUSDT"

    def __str__(self):
        return "TRBUSDT"

    def __call__(self):
        return "TRBUSDT"


TRBUSDT = TRBUSDT()


@dataclass(slots=True, frozen=True)
class TRIBEBNB:
    name: str = "TRIBEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TRIBEBNB"

    def __str__(self):
        return "TRIBEBNB"

    def __call__(self):
        return "TRIBEBNB"


TRIBEBNB = TRIBEBNB()


@dataclass(slots=True, frozen=True)
class TRIBEBTC:
    name: str = "TRIBEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TRIBEBTC"

    def __str__(self):
        return "TRIBEBTC"

    def __call__(self):
        return "TRIBEBTC"


TRIBEBTC = TRIBEBTC()


@dataclass(slots=True, frozen=True)
class TRIBEBUSD:
    name: str = "TRIBEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TRIBEBUSD"

    def __str__(self):
        return "TRIBEBUSD"

    def __call__(self):
        return "TRIBEBUSD"


TRIBEBUSD = TRIBEBUSD()


@dataclass(slots=True, frozen=True)
class TRIBEUSDT:
    name: str = "TRIBEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TRIBEUSDT"

    def __str__(self):
        return "TRIBEUSDT"

    def __call__(self):
        return "TRIBEUSDT"


TRIBEUSDT = TRIBEUSDT()


@dataclass(slots=True, frozen=True)
class TRIGBNB:
    name: str = "TRIGBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRIGBNB"

    def __str__(self):
        return "TRIGBNB"

    def __call__(self):
        return "TRIGBNB"


TRIGBNB = TRIGBNB()


@dataclass(slots=True, frozen=True)
class TRIGBTC:
    name: str = "TRIGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRIGBTC"

    def __str__(self):
        return "TRIGBTC"

    def __call__(self):
        return "TRIGBTC"


TRIGBTC = TRIGBTC()


@dataclass(slots=True, frozen=True)
class TRIGETH:
    name: str = "TRIGETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRIGETH"

    def __str__(self):
        return "TRIGETH"

    def __call__(self):
        return "TRIGETH"


TRIGETH = TRIGETH()


@dataclass(slots=True, frozen=True)
class TROYBNB:
    name: str = "TROYBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TROYBNB"

    def __str__(self):
        return "TROYBNB"

    def __call__(self):
        return "TROYBNB"


TROYBNB = TROYBNB()


@dataclass(slots=True, frozen=True)
class TROYBTC:
    name: str = "TROYBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "TROYBTC"

    def __str__(self):
        return "TROYBTC"

    def __call__(self):
        return "TROYBTC"


TROYBTC = TROYBTC()


@dataclass(slots=True, frozen=True)
class TROYBUSD:
    name: str = "TROYBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "TROYBUSD"

    def __str__(self):
        return "TROYBUSD"

    def __call__(self):
        return "TROYBUSD"


TROYBUSD = TROYBUSD()


@dataclass(slots=True, frozen=True)
class TROYUSDT:
    name: str = "TROYUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "TROYUSDT"

    def __str__(self):
        return "TROYUSDT"

    def __call__(self):
        return "TROYUSDT"


TROYUSDT = TROYUSDT()


@dataclass(slots=True, frozen=True)
class TRUBTC:
    name: str = "TRUBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TRUBTC"

    def __str__(self):
        return "TRUBTC"

    def __call__(self):
        return "TRUBTC"


TRUBTC = TRUBTC()


@dataclass(slots=True, frozen=True)
class TRUBUSD:
    name: str = "TRUBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "TRUBUSD"

    def __str__(self):
        return "TRUBUSD"

    def __call__(self):
        return "TRUBUSD"


TRUBUSD = TRUBUSD()


@dataclass(slots=True, frozen=True)
class TRURUB:
    name: str = "TRURUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "TRURUB"

    def __str__(self):
        return "TRURUB"

    def __call__(self):
        return "TRURUB"


TRURUB = TRURUB()


@dataclass(slots=True, frozen=True)
class TRUUSDT:
    name: str = "TRUUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "TRUUSDT"

    def __str__(self):
        return "TRUUSDT"

    def __call__(self):
        return "TRUUSDT"


TRUUSDT = TRUUSDT()


@dataclass(slots=True, frozen=True)
class TRXAUD:
    name: str = "TRXAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXAUD"

    def __str__(self):
        return "TRXAUD"

    def __call__(self):
        return "TRXAUD"


TRXAUD = TRXAUD()


@dataclass(slots=True, frozen=True)
class TRXBNB:
    name: str = "TRXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXBNB"

    def __str__(self):
        return "TRXBNB"

    def __call__(self):
        return "TRXBNB"


TRXBNB = TRXBNB()


@dataclass(slots=True, frozen=True)
class TRXBTC:
    name: str = "TRXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TRXBTC"

    def __str__(self):
        return "TRXBTC"

    def __call__(self):
        return "TRXBTC"


TRXBTC = TRXBTC()


@dataclass(slots=True, frozen=True)
class TRXBUSD:
    name: str = "TRXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TRXBUSD"

    def __str__(self):
        return "TRXBUSD"

    def __call__(self):
        return "TRXBUSD"


TRXBUSD = TRXBUSD()


@dataclass(slots=True, frozen=True)
class TRXDOWNUSDT:
    name: str = "TRXDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 89984117.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXDOWNUSDT"

    def __str__(self):
        return "TRXDOWNUSDT"

    def __call__(self):
        return "TRXDOWNUSDT"


TRXDOWNUSDT = TRXDOWNUSDT()


@dataclass(slots=True, frozen=True)
class TRXETH:
    name: str = "TRXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TRXETH"

    def __str__(self):
        return "TRXETH"

    def __call__(self):
        return "TRXETH"


TRXETH = TRXETH()


@dataclass(slots=True, frozen=True)
class TRXEUR:
    name: str = "TRXEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXEUR"

    def __str__(self):
        return "TRXEUR"

    def __call__(self):
        return "TRXEUR"


TRXEUR = TRXEUR()


@dataclass(slots=True, frozen=True)
class TRXNGN:
    name: str = "TRXNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922320.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXNGN"

    def __str__(self):
        return "TRXNGN"

    def __call__(self):
        return "TRXNGN"


TRXNGN = TRXNGN()


@dataclass(slots=True, frozen=True)
class TRXPAX:
    name: str = "TRXPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXPAX"

    def __str__(self):
        return "TRXPAX"

    def __call__(self):
        return "TRXPAX"


TRXPAX = TRXPAX()


@dataclass(slots=True, frozen=True)
class TRXTRY:
    name: str = "TRXTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXTRY"

    def __str__(self):
        return "TRXTRY"

    def __call__(self):
        return "TRXTRY"


TRXTRY = TRXTRY()


@dataclass(slots=True, frozen=True)
class TRXTUSD:
    name: str = "TRXTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXTUSD"

    def __str__(self):
        return "TRXTUSD"

    def __call__(self):
        return "TRXTUSD"


TRXTUSD = TRXTUSD()


@dataclass(slots=True, frozen=True)
class TRXUPUSDT:
    name: str = "TRXUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXUPUSDT"

    def __str__(self):
        return "TRXUPUSDT"

    def __call__(self):
        return "TRXUPUSDT"


TRXUPUSDT = TRXUPUSDT()


@dataclass(slots=True, frozen=True)
class TRXUSDC:
    name: str = "TRXUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXUSDC"

    def __str__(self):
        return "TRXUSDC"

    def __call__(self):
        return "TRXUSDC"


TRXUSDC = TRXUSDC()


@dataclass(slots=True, frozen=True)
class TRXUSDT:
    name: str = "TRXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TRXUSDT"

    def __str__(self):
        return "TRXUSDT"

    def __call__(self):
        return "TRXUSDT"


TRXUSDT = TRXUSDT()


@dataclass(slots=True, frozen=True)
class TRXXRP:
    name: str = "TRXXRP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TRXXRP"

    def __str__(self):
        return "TRXXRP"

    def __call__(self):
        return "TRXXRP"


TRXXRP = TRXXRP()


@dataclass(slots=True, frozen=True)
class TUSDBNB:
    name: str = "TUSDBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TUSDBNB"

    def __str__(self):
        return "TUSDBNB"

    def __call__(self):
        return "TUSDBNB"


TUSDBNB = TUSDBNB()


@dataclass(slots=True, frozen=True)
class TUSDBTC:
    name: str = "TUSDBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TUSDBTC"

    def __str__(self):
        return "TUSDBTC"

    def __call__(self):
        return "TUSDBTC"


TUSDBTC = TUSDBTC()


@dataclass(slots=True, frozen=True)
class TUSDBTUSD:
    name: str = "TUSDBTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "TUSDBTUSD"

    def __str__(self):
        return "TUSDBTUSD"

    def __call__(self):
        return "TUSDBTUSD"


TUSDBTUSD = TUSDBTUSD()


@dataclass(slots=True, frozen=True)
class TUSDBUSD:
    name: str = "TUSDBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "TUSDBUSD"

    def __str__(self):
        return "TUSDBUSD"

    def __call__(self):
        return "TUSDBUSD"


TUSDBUSD = TUSDBUSD()


@dataclass(slots=True, frozen=True)
class TUSDETH:
    name: str = "TUSDETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TUSDETH"

    def __str__(self):
        return "TUSDETH"

    def __call__(self):
        return "TUSDETH"


TUSDETH = TUSDETH()


@dataclass(slots=True, frozen=True)
class TUSDT:
    name: str = "TUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "TUSDT"

    def __str__(self):
        return "TUSDT"

    def __call__(self):
        return "TUSDT"


TUSDT = TUSDT()


@dataclass(slots=True, frozen=True)
class TUSDUSDT:
    name: str = "TUSDUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "TUSDUSDT"

    def __str__(self):
        return "TUSDUSDT"

    def __call__(self):
        return "TUSDUSDT"


TUSDUSDT = TUSDUSDT()


@dataclass(slots=True, frozen=True)
class TVKBTC:
    name: str = "TVKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "TVKBTC"

    def __str__(self):
        return "TVKBTC"

    def __call__(self):
        return "TVKBTC"


TVKBTC = TVKBTC()


@dataclass(slots=True, frozen=True)
class TVKBUSD:
    name: str = "TVKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "TVKBUSD"

    def __str__(self):
        return "TVKBUSD"

    def __call__(self):
        return "TVKBUSD"


TVKBUSD = TVKBUSD()


@dataclass(slots=True, frozen=True)
class TVKUSDT:
    name: str = "TVKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "TVKUSDT"

    def __str__(self):
        return "TVKUSDT"

    def __call__(self):
        return "TVKUSDT"


TVKUSDT = TVKUSDT()


@dataclass(slots=True, frozen=True)
class TWTBTC:
    name: str = "TWTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "TWTBTC"

    def __str__(self):
        return "TWTBTC"

    def __call__(self):
        return "TWTBTC"


TWTBTC = TWTBTC()


@dataclass(slots=True, frozen=True)
class TWTBUSD:
    name: str = "TWTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "TWTBUSD"

    def __str__(self):
        return "TWTBUSD"

    def __call__(self):
        return "TWTBUSD"


TWTBUSD = TWTBUSD()


@dataclass(slots=True, frozen=True)
class TWTTRY:
    name: str = "TWTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "TWTTRY"

    def __str__(self):
        return "TWTTRY"

    def __call__(self):
        return "TWTTRY"


TWTTRY = TWTTRY()


@dataclass(slots=True, frozen=True)
class TWTUSDT:
    name: str = "TWTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "TWTUSDT"

    def __str__(self):
        return "TWTUSDT"

    def __call__(self):
        return "TWTUSDT"


TWTUSDT = TWTUSDT()


@dataclass(slots=True, frozen=True)
class UFTBUSD:
    name: str = "UFTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "UFTBUSD"

    def __str__(self):
        return "UFTBUSD"

    def __call__(self):
        return "UFTBUSD"


UFTBUSD = UFTBUSD()


@dataclass(slots=True, frozen=True)
class UFTETH:
    name: str = "UFTETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "UFTETH"

    def __str__(self):
        return "UFTETH"

    def __call__(self):
        return "UFTETH"


UFTETH = UFTETH()


@dataclass(slots=True, frozen=True)
class UMABTC:
    name: str = "UMABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "UMABTC"

    def __str__(self):
        return "UMABTC"

    def __call__(self):
        return "UMABTC"


UMABTC = UMABTC()


@dataclass(slots=True, frozen=True)
class UMABUSD:
    name: str = "UMABUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "UMABUSD"

    def __str__(self):
        return "UMABUSD"

    def __call__(self):
        return "UMABUSD"


UMABUSD = UMABUSD()


@dataclass(slots=True, frozen=True)
class UMATRY:
    name: str = "UMATRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "UMATRY"

    def __str__(self):
        return "UMATRY"

    def __call__(self):
        return "UMATRY"


UMATRY = UMATRY()


@dataclass(slots=True, frozen=True)
class UMAUSDT:
    name: str = "UMAUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "UMAUSDT"

    def __str__(self):
        return "UMAUSDT"

    def __call__(self):
        return "UMAUSDT"


UMAUSDT = UMAUSDT()


@dataclass(slots=True, frozen=True)
class UNFIBNB:
    name: str = "UNFIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "UNFIBNB"

    def __str__(self):
        return "UNFIBNB"

    def __call__(self):
        return "UNFIBNB"


UNFIBNB = UNFIBNB()


@dataclass(slots=True, frozen=True)
class UNFIBTC:
    name: str = "UNFIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "UNFIBTC"

    def __str__(self):
        return "UNFIBTC"

    def __call__(self):
        return "UNFIBTC"


UNFIBTC = UNFIBTC()


@dataclass(slots=True, frozen=True)
class UNFIBUSD:
    name: str = "UNFIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "UNFIBUSD"

    def __str__(self):
        return "UNFIBUSD"

    def __call__(self):
        return "UNFIBUSD"


UNFIBUSD = UNFIBUSD()


@dataclass(slots=True, frozen=True)
class UNFIETH:
    name: str = "UNFIETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "UNFIETH"

    def __str__(self):
        return "UNFIETH"

    def __call__(self):
        return "UNFIETH"


UNFIETH = UNFIETH()


@dataclass(slots=True, frozen=True)
class UNFIUSDT:
    name: str = "UNFIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "UNFIUSDT"

    def __str__(self):
        return "UNFIUSDT"

    def __call__(self):
        return "UNFIUSDT"


UNFIUSDT = UNFIUSDT()


@dataclass(slots=True, frozen=True)
class UNIAUD:
    name: str = "UNIAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "UNIAUD"

    def __str__(self):
        return "UNIAUD"

    def __call__(self):
        return "UNIAUD"


UNIAUD = UNIAUD()


@dataclass(slots=True, frozen=True)
class UNIBNB:
    name: str = "UNIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "UNIBNB"

    def __str__(self):
        return "UNIBNB"

    def __call__(self):
        return "UNIBNB"


UNIBNB = UNIBNB()


@dataclass(slots=True, frozen=True)
class UNIBTC:
    name: str = "UNIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "UNIBTC"

    def __str__(self):
        return "UNIBTC"

    def __call__(self):
        return "UNIBTC"


UNIBTC = UNIBTC()


@dataclass(slots=True, frozen=True)
class UNIBUSD:
    name: str = "UNIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "UNIBUSD"

    def __str__(self):
        return "UNIBUSD"

    def __call__(self):
        return "UNIBUSD"


UNIBUSD = UNIBUSD()


@dataclass(slots=True, frozen=True)
class UNIDOWNUSDT:
    name: str = "UNIDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 99999999.00000000
    margin: bool = False

    def __repr__(self):
        return "UNIDOWNUSDT"

    def __str__(self):
        return "UNIDOWNUSDT"

    def __call__(self):
        return "UNIDOWNUSDT"


UNIDOWNUSDT = UNIDOWNUSDT()


@dataclass(slots=True, frozen=True)
class UNIETH:
    name: str = "UNIETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "UNIETH"

    def __str__(self):
        return "UNIETH"

    def __call__(self):
        return "UNIETH"


UNIETH = UNIETH()


@dataclass(slots=True, frozen=True)
class UNIEUR:
    name: str = "UNIEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "UNIEUR"

    def __str__(self):
        return "UNIEUR"

    def __call__(self):
        return "UNIEUR"


UNIEUR = UNIEUR()


@dataclass(slots=True, frozen=True)
class UNIUPUSDT:
    name: str = "UNIUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "UNIUPUSDT"

    def __str__(self):
        return "UNIUPUSDT"

    def __call__(self):
        return "UNIUPUSDT"


UNIUPUSDT = UNIUPUSDT()


@dataclass(slots=True, frozen=True)
class UNIUSDT:
    name: str = "UNIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "UNIUSDT"

    def __str__(self):
        return "UNIUSDT"

    def __call__(self):
        return "UNIUSDT"


UNIUSDT = UNIUSDT()


@dataclass(slots=True, frozen=True)
class USDCBNB:
    name: str = "USDCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDCBNB"

    def __str__(self):
        return "USDCBNB"

    def __call__(self):
        return "USDCBNB"


USDCBNB = USDCBNB()


@dataclass(slots=True, frozen=True)
class USDCBUSD:
    name: str = "USDCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDCBUSD"

    def __str__(self):
        return "USDCBUSD"

    def __call__(self):
        return "USDCBUSD"


USDCBUSD = USDCBUSD()


@dataclass(slots=True, frozen=True)
class USDCPAX:
    name: str = "USDCPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDCPAX"

    def __str__(self):
        return "USDCPAX"

    def __call__(self):
        return "USDCPAX"


USDCPAX = USDCPAX()


@dataclass(slots=True, frozen=True)
class USDCTUSD:
    name: str = "USDCTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDCTUSD"

    def __str__(self):
        return "USDCTUSD"

    def __call__(self):
        return "USDCTUSD"


USDCTUSD = USDCTUSD()


@dataclass(slots=True, frozen=True)
class USDCUSDT:
    name: str = "USDCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDCUSDT"

    def __str__(self):
        return "USDCUSDT"

    def __call__(self):
        return "USDCUSDT"


USDCUSDT = USDCUSDT()


@dataclass(slots=True, frozen=True)
class USDPBUSD:
    name: str = "USDPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "USDPBUSD"

    def __str__(self):
        return "USDPBUSD"

    def __call__(self):
        return "USDPBUSD"


USDPBUSD = USDPBUSD()


@dataclass(slots=True, frozen=True)
class USDPUSDT:
    name: str = "USDPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "USDPUSDT"

    def __str__(self):
        return "USDPUSDT"

    def __call__(self):
        return "USDPUSDT"


USDPUSDT = USDPUSDT()


@dataclass(slots=True, frozen=True)
class USDSBUSDS:
    name: str = "USDSBUSDS"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDSBUSDS"

    def __str__(self):
        return "USDSBUSDS"

    def __call__(self):
        return "USDSBUSDS"


USDSBUSDS = USDSBUSDS()


@dataclass(slots=True, frozen=True)
class USDSBUSDT:
    name: str = "USDSBUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDSBUSDT"

    def __str__(self):
        return "USDSBUSDT"

    def __call__(self):
        return "USDSBUSDT"


USDSBUSDT = USDSBUSDT()


@dataclass(slots=True, frozen=True)
class USDSPAX:
    name: str = "USDSPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDSPAX"

    def __str__(self):
        return "USDSPAX"

    def __call__(self):
        return "USDSPAX"


USDSPAX = USDSPAX()


@dataclass(slots=True, frozen=True)
class USDSTUSD:
    name: str = "USDSTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDSTUSD"

    def __str__(self):
        return "USDSTUSD"

    def __call__(self):
        return "USDSTUSD"


USDSTUSD = USDSTUSD()


@dataclass(slots=True, frozen=True)
class USDSUSDC:
    name: str = "USDSUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDSUSDC"

    def __str__(self):
        return "USDSUSDC"

    def __call__(self):
        return "USDSUSDC"


USDSUSDC = USDSUSDC()


@dataclass(slots=True, frozen=True)
class USDSUSDT:
    name: str = "USDSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDSUSDT"

    def __str__(self):
        return "USDSUSDT"

    def __call__(self):
        return "USDSUSDT"


USDSUSDT = USDSUSDT()


@dataclass(slots=True, frozen=True)
class USDTBIDR:
    name: str = "USDTBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 1000000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTBIDR"

    def __str__(self):
        return "USDTBIDR"

    def __call__(self):
        return "USDTBIDR"


USDTBIDR = USDTBIDR()


@dataclass(slots=True, frozen=True)
class USDTBKRW:
    name: str = "USDTBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTBKRW"

    def __str__(self):
        return "USDTBKRW"

    def __call__(self):
        return "USDTBKRW"


USDTBKRW = USDTBKRW()


@dataclass(slots=True, frozen=True)
class USDTBRL:
    name: str = "USDTBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTBRL"

    def __str__(self):
        return "USDTBRL"

    def __call__(self):
        return "USDTBRL"


USDTBRL = USDTBRL()


@dataclass(slots=True, frozen=True)
class USDTBVND:
    name: str = "USDTBVND"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 1000000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTBVND"

    def __str__(self):
        return "USDTBVND"

    def __call__(self):
        return "USDTBVND"


USDTBVND = USDTBVND()


@dataclass(slots=True, frozen=True)
class USDTDAI:
    name: str = "USDTDAI"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTDAI"

    def __str__(self):
        return "USDTDAI"

    def __call__(self):
        return "USDTDAI"


USDTDAI = USDTDAI()


@dataclass(slots=True, frozen=True)
class USDTIDRT:
    name: str = "USDTIDRT"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 1000000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTIDRT"

    def __str__(self):
        return "USDTIDRT"

    def __call__(self):
        return "USDTIDRT"


USDTIDRT = USDTIDRT()


@dataclass(slots=True, frozen=True)
class USDTNGN:
    name: str = "USDTNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922320.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTNGN"

    def __str__(self):
        return "USDTNGN"

    def __call__(self):
        return "USDTNGN"


USDTNGN = USDTNGN()


@dataclass(slots=True, frozen=True)
class USDTRUB:
    name: str = "USDTRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTRUB"

    def __str__(self):
        return "USDTRUB"

    def __call__(self):
        return "USDTRUB"


USDTRUB = USDTRUB()


@dataclass(slots=True, frozen=True)
class USDTTRY:
    name: str = "USDTTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTTRY"

    def __str__(self):
        return "USDTTRY"

    def __call__(self):
        return "USDTTRY"


USDTTRY = USDTTRY()


@dataclass(slots=True, frozen=True)
class USDTUAH:
    name: str = "USDTUAH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTUAH"

    def __str__(self):
        return "USDTUAH"

    def __call__(self):
        return "USDTUAH"


USDTUAH = USDTUAH()


@dataclass(slots=True, frozen=True)
class USDTZAR:
    name: str = "USDTZAR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "USDTZAR"

    def __str__(self):
        return "USDTZAR"

    def __call__(self):
        return "USDTZAR"


USDTZAR = USDTZAR()


@dataclass(slots=True, frozen=True)
class USTBTC:
    name: str = "USTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "USTBTC"

    def __str__(self):
        return "USTBTC"

    def __call__(self):
        return "USTBTC"


USTBTC = USTBTC()


@dataclass(slots=True, frozen=True)
class USTBUSD:
    name: str = "USTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "USTBUSD"

    def __str__(self):
        return "USTBUSD"

    def __call__(self):
        return "USTBUSD"


USTBUSD = USTBUSD()


@dataclass(slots=True, frozen=True)
class USTCBUSD:
    name: str = "USTCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "USTCBUSD"

    def __str__(self):
        return "USTCBUSD"

    def __call__(self):
        return "USTCBUSD"


USTCBUSD = USTCBUSD()


@dataclass(slots=True, frozen=True)
class USTUSDT:
    name: str = "USTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "USTUSDT"

    def __str__(self):
        return "USTUSDT"

    def __call__(self):
        return "USTUSDT"


USTUSDT = USTUSDT()


@dataclass(slots=True, frozen=True)
class UTKBTC:
    name: str = "UTKBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "UTKBTC"

    def __str__(self):
        return "UTKBTC"

    def __call__(self):
        return "UTKBTC"


UTKBTC = UTKBTC()


@dataclass(slots=True, frozen=True)
class UTKBUSD:
    name: str = "UTKBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "UTKBUSD"

    def __str__(self):
        return "UTKBUSD"

    def __call__(self):
        return "UTKBUSD"


UTKBUSD = UTKBUSD()


@dataclass(slots=True, frozen=True)
class UTKUSDT:
    name: str = "UTKUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "UTKUSDT"

    def __str__(self):
        return "UTKUSDT"

    def __call__(self):
        return "UTKUSDT"


UTKUSDT = UTKUSDT()


@dataclass(slots=True, frozen=True)
class VENBNB:
    name: str = "VENBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "VENBNB"

    def __str__(self):
        return "VENBNB"

    def __call__(self):
        return "VENBNB"


VENBNB = VENBNB()


@dataclass(slots=True, frozen=True)
class VENBTC:
    name: str = "VENBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VENBTC"

    def __str__(self):
        return "VENBTC"

    def __call__(self):
        return "VENBTC"


VENBTC = VENBTC()


@dataclass(slots=True, frozen=True)
class VENETH:
    name: str = "VENETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VENETH"

    def __str__(self):
        return "VENETH"

    def __call__(self):
        return "VENETH"


VENETH = VENETH()


@dataclass(slots=True, frozen=True)
class VENUSDT:
    name: str = "VENUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "VENUSDT"

    def __str__(self):
        return "VENUSDT"

    def __call__(self):
        return "VENUSDT"


VENUSDT = VENUSDT()


@dataclass(slots=True, frozen=True)
class VETBNB:
    name: str = "VETBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VETBNB"

    def __str__(self):
        return "VETBNB"

    def __call__(self):
        return "VETBNB"


VETBNB = VETBNB()


@dataclass(slots=True, frozen=True)
class VETBTC:
    name: str = "VETBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "VETBTC"

    def __str__(self):
        return "VETBTC"

    def __call__(self):
        return "VETBTC"


VETBTC = VETBTC()


@dataclass(slots=True, frozen=True)
class VETBUSD:
    name: str = "VETBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "VETBUSD"

    def __str__(self):
        return "VETBUSD"

    def __call__(self):
        return "VETBUSD"


VETBUSD = VETBUSD()


@dataclass(slots=True, frozen=True)
class VETETH:
    name: str = "VETETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VETETH"

    def __str__(self):
        return "VETETH"

    def __call__(self):
        return "VETETH"


VETETH = VETETH()


@dataclass(slots=True, frozen=True)
class VETEUR:
    name: str = "VETEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VETEUR"

    def __str__(self):
        return "VETEUR"

    def __call__(self):
        return "VETEUR"


VETEUR = VETEUR()


@dataclass(slots=True, frozen=True)
class VETGBP:
    name: str = "VETGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VETGBP"

    def __str__(self):
        return "VETGBP"

    def __call__(self):
        return "VETGBP"


VETGBP = VETGBP()


@dataclass(slots=True, frozen=True)
class VETTRY:
    name: str = "VETTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "VETTRY"

    def __str__(self):
        return "VETTRY"

    def __call__(self):
        return "VETTRY"


VETTRY = VETTRY()


@dataclass(slots=True, frozen=True)
class VETUSDT:
    name: str = "VETUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "VETUSDT"

    def __str__(self):
        return "VETUSDT"

    def __call__(self):
        return "VETUSDT"


VETUSDT = VETUSDT()


@dataclass(slots=True, frozen=True)
class VGXBTC:
    name: str = "VGXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VGXBTC"

    def __str__(self):
        return "VGXBTC"

    def __call__(self):
        return "VGXBTC"


VGXBTC = VGXBTC()


@dataclass(slots=True, frozen=True)
class VGXETH:
    name: str = "VGXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VGXETH"

    def __str__(self):
        return "VGXETH"

    def __call__(self):
        return "VGXETH"


VGXETH = VGXETH()


@dataclass(slots=True, frozen=True)
class VGXUSDT:
    name: str = "VGXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VGXUSDT"

    def __str__(self):
        return "VGXUSDT"

    def __call__(self):
        return "VGXUSDT"


VGXUSDT = VGXUSDT()


@dataclass(slots=True, frozen=True)
class VIABNB:
    name: str = "VIABNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VIABNB"

    def __str__(self):
        return "VIABNB"

    def __call__(self):
        return "VIABNB"


VIABNB = VIABNB()


@dataclass(slots=True, frozen=True)
class VIABTC:
    name: str = "VIABTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VIABTC"

    def __str__(self):
        return "VIABTC"

    def __call__(self):
        return "VIABTC"


VIABTC = VIABTC()


@dataclass(slots=True, frozen=True)
class VIAETH:
    name: str = "VIAETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VIAETH"

    def __str__(self):
        return "VIAETH"

    def __call__(self):
        return "VIAETH"


VIAETH = VIAETH()


@dataclass(slots=True, frozen=True)
class VIBBTC:
    name: str = "VIBBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VIBBTC"

    def __str__(self):
        return "VIBBTC"

    def __call__(self):
        return "VIBBTC"


VIBBTC = VIBBTC()


@dataclass(slots=True, frozen=True)
class VIBBUSD:
    name: str = "VIBBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "VIBBUSD"

    def __str__(self):
        return "VIBBUSD"

    def __call__(self):
        return "VIBBUSD"


VIBBUSD = VIBBUSD()


@dataclass(slots=True, frozen=True)
class VIBEBTC:
    name: str = "VIBEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VIBEBTC"

    def __str__(self):
        return "VIBEBTC"

    def __call__(self):
        return "VIBEBTC"


VIBEBTC = VIBEBTC()


@dataclass(slots=True, frozen=True)
class VIBEETH:
    name: str = "VIBEETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VIBEETH"

    def __str__(self):
        return "VIBEETH"

    def __call__(self):
        return "VIBEETH"


VIBEETH = VIBEETH()


@dataclass(slots=True, frozen=True)
class VIBETH:
    name: str = "VIBETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VIBETH"

    def __str__(self):
        return "VIBETH"

    def __call__(self):
        return "VIBETH"


VIBETH = VIBETH()


@dataclass(slots=True, frozen=True)
class VIDTBTC:
    name: str = "VIDTBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 46116860414.00000000
    margin: bool = False

    def __repr__(self):
        return "VIDTBTC"

    def __str__(self):
        return "VIDTBTC"

    def __call__(self):
        return "VIDTBTC"


VIDTBTC = VIDTBTC()


@dataclass(slots=True, frozen=True)
class VIDTBUSD:
    name: str = "VIDTBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "VIDTBUSD"

    def __str__(self):
        return "VIDTBUSD"

    def __call__(self):
        return "VIDTBUSD"


VIDTBUSD = VIDTBUSD()


@dataclass(slots=True, frozen=True)
class VIDTUSDT:
    name: str = "VIDTUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "VIDTUSDT"

    def __str__(self):
        return "VIDTUSDT"

    def __call__(self):
        return "VIDTUSDT"


VIDTUSDT = VIDTUSDT()


@dataclass(slots=True, frozen=True)
class VITEBNB:
    name: str = "VITEBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VITEBNB"

    def __str__(self):
        return "VITEBNB"

    def __call__(self):
        return "VITEBNB"


VITEBNB = VITEBNB()


@dataclass(slots=True, frozen=True)
class VITEBTC:
    name: str = "VITEBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VITEBTC"

    def __str__(self):
        return "VITEBTC"

    def __call__(self):
        return "VITEBTC"


VITEBTC = VITEBTC()


@dataclass(slots=True, frozen=True)
class VITEBUSD:
    name: str = "VITEBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VITEBUSD"

    def __str__(self):
        return "VITEBUSD"

    def __call__(self):
        return "VITEBUSD"


VITEBUSD = VITEBUSD()


@dataclass(slots=True, frozen=True)
class VITEUSDT:
    name: str = "VITEUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VITEUSDT"

    def __str__(self):
        return "VITEUSDT"

    def __call__(self):
        return "VITEUSDT"


VITEUSDT = VITEUSDT()


@dataclass(slots=True, frozen=True)
class VOXELBNB:
    name: str = "VOXELBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VOXELBNB"

    def __str__(self):
        return "VOXELBNB"

    def __call__(self):
        return "VOXELBNB"


VOXELBNB = VOXELBNB()


@dataclass(slots=True, frozen=True)
class VOXELBTC:
    name: str = "VOXELBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VOXELBTC"

    def __str__(self):
        return "VOXELBTC"

    def __call__(self):
        return "VOXELBTC"


VOXELBTC = VOXELBTC()


@dataclass(slots=True, frozen=True)
class VOXELBUSD:
    name: str = "VOXELBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VOXELBUSD"

    def __str__(self):
        return "VOXELBUSD"

    def __call__(self):
        return "VOXELBUSD"


VOXELBUSD = VOXELBUSD()


@dataclass(slots=True, frozen=True)
class VOXELETH:
    name: str = "VOXELETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VOXELETH"

    def __str__(self):
        return "VOXELETH"

    def __call__(self):
        return "VOXELETH"


VOXELETH = VOXELETH()


@dataclass(slots=True, frozen=True)
class VOXELUSDT:
    name: str = "VOXELUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VOXELUSDT"

    def __str__(self):
        return "VOXELUSDT"

    def __call__(self):
        return "VOXELUSDT"


VOXELUSDT = VOXELUSDT()


@dataclass(slots=True, frozen=True)
class VTHOBNB:
    name: str = "VTHOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VTHOBNB"

    def __str__(self):
        return "VTHOBNB"

    def __call__(self):
        return "VTHOBNB"


VTHOBNB = VTHOBNB()


@dataclass(slots=True, frozen=True)
class VTHOBUSD:
    name: str = "VTHOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "VTHOBUSD"

    def __str__(self):
        return "VTHOBUSD"

    def __call__(self):
        return "VTHOBUSD"


VTHOBUSD = VTHOBUSD()


@dataclass(slots=True, frozen=True)
class VTHOUSDT:
    name: str = "VTHOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "VTHOUSDT"

    def __str__(self):
        return "VTHOUSDT"

    def __call__(self):
        return "VTHOUSDT"


VTHOUSDT = VTHOUSDT()


@dataclass(slots=True, frozen=True)
class WABIBNB:
    name: str = "WABIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WABIBNB"

    def __str__(self):
        return "WABIBNB"

    def __call__(self):
        return "WABIBNB"


WABIBNB = WABIBNB()


@dataclass(slots=True, frozen=True)
class WABIBTC:
    name: str = "WABIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WABIBTC"

    def __str__(self):
        return "WABIBTC"

    def __call__(self):
        return "WABIBTC"


WABIBTC = WABIBTC()


@dataclass(slots=True, frozen=True)
class WABIETH:
    name: str = "WABIETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WABIETH"

    def __str__(self):
        return "WABIETH"

    def __call__(self):
        return "WABIETH"


WABIETH = WABIETH()


@dataclass(slots=True, frozen=True)
class WANBNB:
    name: str = "WANBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WANBNB"

    def __str__(self):
        return "WANBNB"

    def __call__(self):
        return "WANBNB"


WANBNB = WANBNB()


@dataclass(slots=True, frozen=True)
class WANBTC:
    name: str = "WANBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WANBTC"

    def __str__(self):
        return "WANBTC"

    def __call__(self):
        return "WANBTC"


WANBTC = WANBTC()


@dataclass(slots=True, frozen=True)
class WANETH:
    name: str = "WANETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WANETH"

    def __str__(self):
        return "WANETH"

    def __call__(self):
        return "WANETH"


WANETH = WANETH()


@dataclass(slots=True, frozen=True)
class WANUSDT:
    name: str = "WANUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "WANUSDT"

    def __str__(self):
        return "WANUSDT"

    def __call__(self):
        return "WANUSDT"


WANUSDT = WANUSDT()


@dataclass(slots=True, frozen=True)
class WAVESBNB:
    name: str = "WAVESBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WAVESBNB"

    def __str__(self):
        return "WAVESBNB"

    def __call__(self):
        return "WAVESBNB"


WAVESBNB = WAVESBNB()


@dataclass(slots=True, frozen=True)
class WAVESBTC:
    name: str = "WAVESBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "WAVESBTC"

    def __str__(self):
        return "WAVESBTC"

    def __call__(self):
        return "WAVESBTC"


WAVESBTC = WAVESBTC()


@dataclass(slots=True, frozen=True)
class WAVESBUSD:
    name: str = "WAVESBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "WAVESBUSD"

    def __str__(self):
        return "WAVESBUSD"

    def __call__(self):
        return "WAVESBUSD"


WAVESBUSD = WAVESBUSD()


@dataclass(slots=True, frozen=True)
class WAVESETH:
    name: str = "WAVESETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WAVESETH"

    def __str__(self):
        return "WAVESETH"

    def __call__(self):
        return "WAVESETH"


WAVESETH = WAVESETH()


@dataclass(slots=True, frozen=True)
class WAVESEUR:
    name: str = "WAVESEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "WAVESEUR"

    def __str__(self):
        return "WAVESEUR"

    def __call__(self):
        return "WAVESEUR"


WAVESEUR = WAVESEUR()


@dataclass(slots=True, frozen=True)
class WAVESPAX:
    name: str = "WAVESPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "WAVESPAX"

    def __str__(self):
        return "WAVESPAX"

    def __call__(self):
        return "WAVESPAX"


WAVESPAX = WAVESPAX()


@dataclass(slots=True, frozen=True)
class WAVESRUB:
    name: str = "WAVESRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "WAVESRUB"

    def __str__(self):
        return "WAVESRUB"

    def __call__(self):
        return "WAVESRUB"


WAVESRUB = WAVESRUB()


@dataclass(slots=True, frozen=True)
class WAVESTRY:
    name: str = "WAVESTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "WAVESTRY"

    def __str__(self):
        return "WAVESTRY"

    def __call__(self):
        return "WAVESTRY"


WAVESTRY = WAVESTRY()


@dataclass(slots=True, frozen=True)
class WAVESTUSD:
    name: str = "WAVESTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "WAVESTUSD"

    def __str__(self):
        return "WAVESTUSD"

    def __call__(self):
        return "WAVESTUSD"


WAVESTUSD = WAVESTUSD()


@dataclass(slots=True, frozen=True)
class WAVESUSDC:
    name: str = "WAVESUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "WAVESUSDC"

    def __str__(self):
        return "WAVESUSDC"

    def __call__(self):
        return "WAVESUSDC"


WAVESUSDC = WAVESUSDC()


@dataclass(slots=True, frozen=True)
class WAVESUSDT:
    name: str = "WAVESUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "WAVESUSDT"

    def __str__(self):
        return "WAVESUSDT"

    def __call__(self):
        return "WAVESUSDT"


WAVESUSDT = WAVESUSDT()


@dataclass(slots=True, frozen=True)
class WAXPBNB:
    name: str = "WAXPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "WAXPBNB"

    def __str__(self):
        return "WAXPBNB"

    def __call__(self):
        return "WAXPBNB"


WAXPBNB = WAXPBNB()


@dataclass(slots=True, frozen=True)
class WAXPBTC:
    name: str = "WAXPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "WAXPBTC"

    def __str__(self):
        return "WAXPBTC"

    def __call__(self):
        return "WAXPBTC"


WAXPBTC = WAXPBTC()


@dataclass(slots=True, frozen=True)
class WAXPBUSD:
    name: str = "WAXPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "WAXPBUSD"

    def __str__(self):
        return "WAXPBUSD"

    def __call__(self):
        return "WAXPBUSD"


WAXPBUSD = WAXPBUSD()


@dataclass(slots=True, frozen=True)
class WAXPUSDT:
    name: str = "WAXPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "WAXPUSDT"

    def __str__(self):
        return "WAXPUSDT"

    def __call__(self):
        return "WAXPUSDT"


WAXPUSDT = WAXPUSDT()


@dataclass(slots=True, frozen=True)
class WBTCBTC:
    name: str = "WBTCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "WBTCBTC"

    def __str__(self):
        return "WBTCBTC"

    def __call__(self):
        return "WBTCBTC"


WBTCBTC = WBTCBTC()


@dataclass(slots=True, frozen=True)
class WBTCBUSD:
    name: str = "WBTCBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "WBTCBUSD"

    def __str__(self):
        return "WBTCBUSD"

    def __call__(self):
        return "WBTCBUSD"


WBTCBUSD = WBTCBUSD()


@dataclass(slots=True, frozen=True)
class WBTCETH:
    name: str = "WBTCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 100000.00000000
    margin: bool = False

    def __repr__(self):
        return "WBTCETH"

    def __str__(self):
        return "WBTCETH"

    def __call__(self):
        return "WBTCETH"


WBTCETH = WBTCETH()


@dataclass(slots=True, frozen=True)
class WINBNB:
    name: str = "WINBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "WINBNB"

    def __str__(self):
        return "WINBNB"

    def __call__(self):
        return "WINBNB"


WINBNB = WINBNB()


@dataclass(slots=True, frozen=True)
class WINBRL:
    name: str = "WINBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "WINBRL"

    def __str__(self):
        return "WINBRL"

    def __call__(self):
        return "WINBRL"


WINBRL = WINBRL()


@dataclass(slots=True, frozen=True)
class WINBTC:
    name: str = "WINBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WINBTC"

    def __str__(self):
        return "WINBTC"

    def __call__(self):
        return "WINBTC"


WINBTC = WINBTC()


@dataclass(slots=True, frozen=True)
class WINBUSD:
    name: str = "WINBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "WINBUSD"

    def __str__(self):
        return "WINBUSD"

    def __call__(self):
        return "WINBUSD"


WINBUSD = WINBUSD()


@dataclass(slots=True, frozen=True)
class WINEUR:
    name: str = "WINEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "WINEUR"

    def __str__(self):
        return "WINEUR"

    def __call__(self):
        return "WINEUR"


WINEUR = WINEUR()


@dataclass(slots=True, frozen=True)
class WINGBNB:
    name: str = "WINGBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "WINGBNB"

    def __str__(self):
        return "WINGBNB"

    def __call__(self):
        return "WINGBNB"


WINGBNB = WINGBNB()


@dataclass(slots=True, frozen=True)
class WINGBTC:
    name: str = "WINGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 10000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WINGBTC"

    def __str__(self):
        return "WINGBTC"

    def __call__(self):
        return "WINGBTC"


WINGBTC = WINGBTC()


@dataclass(slots=True, frozen=True)
class WINGBUSD:
    name: str = "WINGBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "WINGBUSD"

    def __str__(self):
        return "WINGBUSD"

    def __call__(self):
        return "WINGBUSD"


WINGBUSD = WINGBUSD()


@dataclass(slots=True, frozen=True)
class WINGETH:
    name: str = "WINGETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "WINGETH"

    def __str__(self):
        return "WINGETH"

    def __call__(self):
        return "WINGETH"


WINGETH = WINGETH()


@dataclass(slots=True, frozen=True)
class WINGSBTC:
    name: str = "WINGSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WINGSBTC"

    def __str__(self):
        return "WINGSBTC"

    def __call__(self):
        return "WINGSBTC"


WINGSBTC = WINGSBTC()


@dataclass(slots=True, frozen=True)
class WINGSETH:
    name: str = "WINGSETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WINGSETH"

    def __str__(self):
        return "WINGSETH"

    def __call__(self):
        return "WINGSETH"


WINGSETH = WINGSETH()


@dataclass(slots=True, frozen=True)
class WINGUSDT:
    name: str = "WINGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "WINGUSDT"

    def __str__(self):
        return "WINGUSDT"

    def __call__(self):
        return "WINGUSDT"


WINGUSDT = WINGUSDT()


@dataclass(slots=True, frozen=True)
class WINTRX:
    name: str = "WINTRX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "WINTRX"

    def __str__(self):
        return "WINTRX"

    def __call__(self):
        return "WINTRX"


WINTRX = WINTRX()


@dataclass(slots=True, frozen=True)
class WINUSDC:
    name: str = "WINUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "WINUSDC"

    def __str__(self):
        return "WINUSDC"

    def __call__(self):
        return "WINUSDC"


WINUSDC = WINUSDC()


@dataclass(slots=True, frozen=True)
class WINUSDT:
    name: str = "WINUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 913205152.00000000
    margin: bool = False

    def __repr__(self):
        return "WINUSDT"

    def __str__(self):
        return "WINUSDT"

    def __call__(self):
        return "WINUSDT"


WINUSDT = WINUSDT()


@dataclass(slots=True, frozen=True)
class WNXMBNB:
    name: str = "WNXMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WNXMBNB"

    def __str__(self):
        return "WNXMBNB"

    def __call__(self):
        return "WNXMBNB"


WNXMBNB = WNXMBNB()


@dataclass(slots=True, frozen=True)
class WNXMBTC:
    name: str = "WNXMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 10000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WNXMBTC"

    def __str__(self):
        return "WNXMBTC"

    def __call__(self):
        return "WNXMBTC"


WNXMBTC = WNXMBTC()


@dataclass(slots=True, frozen=True)
class WNXMBUSD:
    name: str = "WNXMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "WNXMBUSD"

    def __str__(self):
        return "WNXMBUSD"

    def __call__(self):
        return "WNXMBUSD"


WNXMBUSD = WNXMBUSD()


@dataclass(slots=True, frozen=True)
class WNXMUSDT:
    name: str = "WNXMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "WNXMUSDT"

    def __str__(self):
        return "WNXMUSDT"

    def __call__(self):
        return "WNXMUSDT"


WNXMUSDT = WNXMUSDT()


@dataclass(slots=True, frozen=True)
class WOOBNB:
    name: str = "WOOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "WOOBNB"

    def __str__(self):
        return "WOOBNB"

    def __call__(self):
        return "WOOBNB"


WOOBNB = WOOBNB()


@dataclass(slots=True, frozen=True)
class WOOBTC:
    name: str = "WOOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "WOOBTC"

    def __str__(self):
        return "WOOBTC"

    def __call__(self):
        return "WOOBTC"


WOOBTC = WOOBTC()


@dataclass(slots=True, frozen=True)
class WOOBUSD:
    name: str = "WOOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "WOOBUSD"

    def __str__(self):
        return "WOOBUSD"

    def __call__(self):
        return "WOOBUSD"


WOOBUSD = WOOBUSD()


@dataclass(slots=True, frozen=True)
class WOOUSDT:
    name: str = "WOOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "WOOUSDT"

    def __str__(self):
        return "WOOUSDT"

    def __call__(self):
        return "WOOUSDT"


WOOUSDT = WOOUSDT()


@dataclass(slots=True, frozen=True)
class WPRBTC:
    name: str = "WPRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WPRBTC"

    def __str__(self):
        return "WPRBTC"

    def __call__(self):
        return "WPRBTC"


WPRBTC = WPRBTC()


@dataclass(slots=True, frozen=True)
class WPRETH:
    name: str = "WPRETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WPRETH"

    def __str__(self):
        return "WPRETH"

    def __call__(self):
        return "WPRETH"


WPRETH = WPRETH()


@dataclass(slots=True, frozen=True)
class WRXBNB:
    name: str = "WRXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WRXBNB"

    def __str__(self):
        return "WRXBNB"

    def __call__(self):
        return "WRXBNB"


WRXBNB = WRXBNB()


@dataclass(slots=True, frozen=True)
class WRXBTC:
    name: str = "WRXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WRXBTC"

    def __str__(self):
        return "WRXBTC"

    def __call__(self):
        return "WRXBTC"


WRXBTC = WRXBTC()


@dataclass(slots=True, frozen=True)
class WRXBUSD:
    name: str = "WRXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "WRXBUSD"

    def __str__(self):
        return "WRXBUSD"

    def __call__(self):
        return "WRXBUSD"


WRXBUSD = WRXBUSD()


@dataclass(slots=True, frozen=True)
class WRXEUR:
    name: str = "WRXEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "WRXEUR"

    def __str__(self):
        return "WRXEUR"

    def __call__(self):
        return "WRXEUR"


WRXEUR = WRXEUR()


@dataclass(slots=True, frozen=True)
class WRXUSDT:
    name: str = "WRXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "WRXUSDT"

    def __str__(self):
        return "WRXUSDT"

    def __call__(self):
        return "WRXUSDT"


WRXUSDT = WRXUSDT()


@dataclass(slots=True, frozen=True)
class WTCBNB:
    name: str = "WTCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "WTCBNB"

    def __str__(self):
        return "WTCBNB"

    def __call__(self):
        return "WTCBNB"


WTCBNB = WTCBNB()


@dataclass(slots=True, frozen=True)
class WTCBTC:
    name: str = "WTCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WTCBTC"

    def __str__(self):
        return "WTCBTC"

    def __call__(self):
        return "WTCBTC"


WTCBTC = WTCBTC()


@dataclass(slots=True, frozen=True)
class WTCETH:
    name: str = "WTCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "WTCETH"

    def __str__(self):
        return "WTCETH"

    def __call__(self):
        return "WTCETH"


WTCETH = WTCETH()


@dataclass(slots=True, frozen=True)
class WTCUSDT:
    name: str = "WTCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "WTCUSDT"

    def __str__(self):
        return "WTCUSDT"

    def __call__(self):
        return "WTCUSDT"


WTCUSDT = WTCUSDT()


@dataclass(slots=True, frozen=True)
class XECBUSD:
    name: str = "XECBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = True

    def __repr__(self):
        return "XECBUSD"

    def __str__(self):
        return "XECBUSD"

    def __call__(self):
        return "XECBUSD"


XECBUSD = XECBUSD()


@dataclass(slots=True, frozen=True)
class XECUSDT:
    name: str = "XECUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00
    maximum_order_size: float = 46116860414.00
    margin: bool = True

    def __repr__(self):
        return "XECUSDT"

    def __str__(self):
        return "XECUSDT"

    def __call__(self):
        return "XECUSDT"


XECUSDT = XECUSDT()


@dataclass(slots=True, frozen=True)
class XEMBNB:
    name: str = "XEMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XEMBNB"

    def __str__(self):
        return "XEMBNB"

    def __call__(self):
        return "XEMBNB"


XEMBNB = XEMBNB()


@dataclass(slots=True, frozen=True)
class XEMBTC:
    name: str = "XEMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XEMBTC"

    def __str__(self):
        return "XEMBTC"

    def __call__(self):
        return "XEMBTC"


XEMBTC = XEMBTC()


@dataclass(slots=True, frozen=True)
class XEMBUSD:
    name: str = "XEMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "XEMBUSD"

    def __str__(self):
        return "XEMBUSD"

    def __call__(self):
        return "XEMBUSD"


XEMBUSD = XEMBUSD()


@dataclass(slots=True, frozen=True)
class XEMETH:
    name: str = "XEMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XEMETH"

    def __str__(self):
        return "XEMETH"

    def __call__(self):
        return "XEMETH"


XEMETH = XEMETH()


@dataclass(slots=True, frozen=True)
class XEMUSDT:
    name: str = "XEMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "XEMUSDT"

    def __str__(self):
        return "XEMUSDT"

    def __call__(self):
        return "XEMUSDT"


XEMUSDT = XEMUSDT()


@dataclass(slots=True, frozen=True)
class XLMBNB:
    name: str = "XLMBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XLMBNB"

    def __str__(self):
        return "XLMBNB"

    def __call__(self):
        return "XLMBNB"


XLMBNB = XLMBNB()


@dataclass(slots=True, frozen=True)
class XLMBTC:
    name: str = "XLMBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "XLMBTC"

    def __str__(self):
        return "XLMBTC"

    def __call__(self):
        return "XLMBTC"


XLMBTC = XLMBTC()


@dataclass(slots=True, frozen=True)
class XLMBUSD:
    name: str = "XLMBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "XLMBUSD"

    def __str__(self):
        return "XLMBUSD"

    def __call__(self):
        return "XLMBUSD"


XLMBUSD = XLMBUSD()


@dataclass(slots=True, frozen=True)
class XLMDOWNUSDT:
    name: str = "XLMDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 399280174.00000000
    margin: bool = False

    def __repr__(self):
        return "XLMDOWNUSDT"

    def __str__(self):
        return "XLMDOWNUSDT"

    def __call__(self):
        return "XLMDOWNUSDT"


XLMDOWNUSDT = XLMDOWNUSDT()


@dataclass(slots=True, frozen=True)
class XLMETH:
    name: str = "XLMETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XLMETH"

    def __str__(self):
        return "XLMETH"

    def __call__(self):
        return "XLMETH"


XLMETH = XLMETH()


@dataclass(slots=True, frozen=True)
class XLMEUR:
    name: str = "XLMEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XLMEUR"

    def __str__(self):
        return "XLMEUR"

    def __call__(self):
        return "XLMEUR"


XLMEUR = XLMEUR()


@dataclass(slots=True, frozen=True)
class XLMPAX:
    name: str = "XLMPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XLMPAX"

    def __str__(self):
        return "XLMPAX"

    def __call__(self):
        return "XLMPAX"


XLMPAX = XLMPAX()


@dataclass(slots=True, frozen=True)
class XLMTRY:
    name: str = "XLMTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "XLMTRY"

    def __str__(self):
        return "XLMTRY"

    def __call__(self):
        return "XLMTRY"


XLMTRY = XLMTRY()


@dataclass(slots=True, frozen=True)
class XLMTUSD:
    name: str = "XLMTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XLMTUSD"

    def __str__(self):
        return "XLMTUSD"

    def __call__(self):
        return "XLMTUSD"


XLMTUSD = XLMTUSD()


@dataclass(slots=True, frozen=True)
class XLMUPUSDT:
    name: str = "XLMUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "XLMUPUSDT"

    def __str__(self):
        return "XLMUPUSDT"

    def __call__(self):
        return "XLMUPUSDT"


XLMUPUSDT = XLMUPUSDT()


@dataclass(slots=True, frozen=True)
class XLMUSDC:
    name: str = "XLMUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XLMUSDC"

    def __str__(self):
        return "XLMUSDC"

    def __call__(self):
        return "XLMUSDC"


XLMUSDC = XLMUSDC()


@dataclass(slots=True, frozen=True)
class XLMUSDT:
    name: str = "XLMUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "XLMUSDT"

    def __str__(self):
        return "XLMUSDT"

    def __call__(self):
        return "XLMUSDT"


XLMUSDT = XLMUSDT()


@dataclass(slots=True, frozen=True)
class XMRBNB:
    name: str = "XMRBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "XMRBNB"

    def __str__(self):
        return "XMRBNB"

    def __call__(self):
        return "XMRBNB"


XMRBNB = XMRBNB()


@dataclass(slots=True, frozen=True)
class XMRBTC:
    name: str = "XMRBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "XMRBTC"

    def __str__(self):
        return "XMRBTC"

    def __call__(self):
        return "XMRBTC"


XMRBTC = XMRBTC()


@dataclass(slots=True, frozen=True)
class XMRBUSD:
    name: str = "XMRBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "XMRBUSD"

    def __str__(self):
        return "XMRBUSD"

    def __call__(self):
        return "XMRBUSD"


XMRBUSD = XMRBUSD()


@dataclass(slots=True, frozen=True)
class XMRETH:
    name: str = "XMRETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "XMRETH"

    def __str__(self):
        return "XMRETH"

    def __call__(self):
        return "XMRETH"


XMRETH = XMRETH()


@dataclass(slots=True, frozen=True)
class XMRUSDT:
    name: str = "XMRUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "XMRUSDT"

    def __str__(self):
        return "XMRUSDT"

    def __call__(self):
        return "XMRUSDT"


XMRUSDT = XMRUSDT()


@dataclass(slots=True, frozen=True)
class XNOBTC:
    name: str = "XNOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "XNOBTC"

    def __str__(self):
        return "XNOBTC"

    def __call__(self):
        return "XNOBTC"


XNOBTC = XNOBTC()


@dataclass(slots=True, frozen=True)
class XNOBUSD:
    name: str = "XNOBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "XNOBUSD"

    def __str__(self):
        return "XNOBUSD"

    def __call__(self):
        return "XNOBUSD"


XNOBUSD = XNOBUSD()


@dataclass(slots=True, frozen=True)
class XNOETH:
    name: str = "XNOETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "XNOETH"

    def __str__(self):
        return "XNOETH"

    def __call__(self):
        return "XNOETH"


XNOETH = XNOETH()


@dataclass(slots=True, frozen=True)
class XNOUSDT:
    name: str = "XNOUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "XNOUSDT"

    def __str__(self):
        return "XNOUSDT"

    def __call__(self):
        return "XNOUSDT"


XNOUSDT = XNOUSDT()


@dataclass(slots=True, frozen=True)
class XRPAUD:
    name: str = "XRPAUD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPAUD"

    def __str__(self):
        return "XRPAUD"

    def __call__(self):
        return "XRPAUD"


XRPAUD = XRPAUD()


@dataclass(slots=True, frozen=True)
class XRPBEARBUSD:
    name: str = "XRPBEARBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPBEARBUSD"

    def __str__(self):
        return "XRPBEARBUSD"

    def __call__(self):
        return "XRPBEARBUSD"


XRPBEARBUSD = XRPBEARBUSD()


@dataclass(slots=True, frozen=True)
class XRPBEARUSDT:
    name: str = "XRPBEARUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPBEARUSDT"

    def __str__(self):
        return "XRPBEARUSDT"

    def __call__(self):
        return "XRPBEARUSDT"


XRPBEARUSDT = XRPBEARUSDT()


@dataclass(slots=True, frozen=True)
class XRPBIDR:
    name: str = "XRPBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92233.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPBIDR"

    def __str__(self):
        return "XRPBIDR"

    def __call__(self):
        return "XRPBIDR"


XRPBIDR = XRPBIDR()


@dataclass(slots=True, frozen=True)
class XRPBKRW:
    name: str = "XRPBKRW"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPBKRW"

    def __str__(self):
        return "XRPBKRW"

    def __call__(self):
        return "XRPBKRW"


XRPBKRW = XRPBKRW()


@dataclass(slots=True, frozen=True)
class XRPBNB:
    name: str = "XRPBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPBNB"

    def __str__(self):
        return "XRPBNB"

    def __call__(self):
        return "XRPBNB"


XRPBNB = XRPBNB()


@dataclass(slots=True, frozen=True)
class XRPBRL:
    name: str = "XRPBRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 922327.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPBRL"

    def __str__(self):
        return "XRPBRL"

    def __call__(self):
        return "XRPBRL"


XRPBRL = XRPBRL()


@dataclass(slots=True, frozen=True)
class XRPBTC:
    name: str = "XRPBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "XRPBTC"

    def __str__(self):
        return "XRPBTC"

    def __call__(self):
        return "XRPBTC"


XRPBTC = XRPBTC()


@dataclass(slots=True, frozen=True)
class XRPBULLBUSD:
    name: str = "XRPBULLBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPBULLBUSD"

    def __str__(self):
        return "XRPBULLBUSD"

    def __call__(self):
        return "XRPBULLBUSD"


XRPBULLBUSD = XRPBULLBUSD()


@dataclass(slots=True, frozen=True)
class XRPBULLUSDT:
    name: str = "XRPBULLUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPBULLUSDT"

    def __str__(self):
        return "XRPBULLUSDT"

    def __call__(self):
        return "XRPBULLUSDT"


XRPBULLUSDT = XRPBULLUSDT()


@dataclass(slots=True, frozen=True)
class XRPBUSD:
    name: str = "XRPBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "XRPBUSD"

    def __str__(self):
        return "XRPBUSD"

    def __call__(self):
        return "XRPBUSD"


XRPBUSD = XRPBUSD()


@dataclass(slots=True, frozen=True)
class XRPDOWNUSDT:
    name: str = "XRPDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 99999999.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPDOWNUSDT"

    def __str__(self):
        return "XRPDOWNUSDT"

    def __call__(self):
        return "XRPDOWNUSDT"


XRPDOWNUSDT = XRPDOWNUSDT()


@dataclass(slots=True, frozen=True)
class XRPETH:
    name: str = "XRPETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "XRPETH"

    def __str__(self):
        return "XRPETH"

    def __call__(self):
        return "XRPETH"


XRPETH = XRPETH()


@dataclass(slots=True, frozen=True)
class XRPEUR:
    name: str = "XRPEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPEUR"

    def __str__(self):
        return "XRPEUR"

    def __call__(self):
        return "XRPEUR"


XRPEUR = XRPEUR()


@dataclass(slots=True, frozen=True)
class XRPGBP:
    name: str = "XRPGBP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPGBP"

    def __str__(self):
        return "XRPGBP"

    def __call__(self):
        return "XRPGBP"


XRPGBP = XRPGBP()


@dataclass(slots=True, frozen=True)
class XRPNGN:
    name: str = "XRPNGN"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 922320.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPNGN"

    def __str__(self):
        return "XRPNGN"

    def __call__(self):
        return "XRPNGN"


XRPNGN = XRPNGN()


@dataclass(slots=True, frozen=True)
class XRPPAX:
    name: str = "XRPPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPPAX"

    def __str__(self):
        return "XRPPAX"

    def __call__(self):
        return "XRPPAX"


XRPPAX = XRPPAX()


@dataclass(slots=True, frozen=True)
class XRPRUB:
    name: str = "XRPRUB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPRUB"

    def __str__(self):
        return "XRPRUB"

    def __call__(self):
        return "XRPRUB"


XRPRUB = XRPRUB()


@dataclass(slots=True, frozen=True)
class XRPTRY:
    name: str = "XRPTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPTRY"

    def __str__(self):
        return "XRPTRY"

    def __call__(self):
        return "XRPTRY"


XRPTRY = XRPTRY()


@dataclass(slots=True, frozen=True)
class XRPTUSD:
    name: str = "XRPTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPTUSD"

    def __str__(self):
        return "XRPTUSD"

    def __call__(self):
        return "XRPTUSD"


XRPTUSD = XRPTUSD()


@dataclass(slots=True, frozen=True)
class XRPUPUSDT:
    name: str = "XRPUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPUPUSDT"

    def __str__(self):
        return "XRPUPUSDT"

    def __call__(self):
        return "XRPUPUSDT"


XRPUPUSDT = XRPUPUSDT()


@dataclass(slots=True, frozen=True)
class XRPUSDC:
    name: str = "XRPUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "XRPUSDC"

    def __str__(self):
        return "XRPUSDC"

    def __call__(self):
        return "XRPUSDC"


XRPUSDC = XRPUSDC()


@dataclass(slots=True, frozen=True)
class XRPUSDT:
    name: str = "XRPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = True

    def __repr__(self):
        return "XRPUSDT"

    def __str__(self):
        return "XRPUSDT"

    def __call__(self):
        return "XRPUSDT"


XRPUSDT = XRPUSDT()


@dataclass(slots=True, frozen=True)
class XTZBNB:
    name: str = "XTZBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XTZBNB"

    def __str__(self):
        return "XTZBNB"

    def __call__(self):
        return "XTZBNB"


XTZBNB = XTZBNB()


@dataclass(slots=True, frozen=True)
class XTZBTC:
    name: str = "XTZBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "XTZBTC"

    def __str__(self):
        return "XTZBTC"

    def __call__(self):
        return "XTZBTC"


XTZBTC = XTZBTC()


@dataclass(slots=True, frozen=True)
class XTZBUSD:
    name: str = "XTZBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "XTZBUSD"

    def __str__(self):
        return "XTZBUSD"

    def __call__(self):
        return "XTZBUSD"


XTZBUSD = XTZBUSD()


@dataclass(slots=True, frozen=True)
class XTZDOWNUSDT:
    name: str = "XTZDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 49991176.00000000
    margin: bool = False

    def __repr__(self):
        return "XTZDOWNUSDT"

    def __str__(self):
        return "XTZDOWNUSDT"

    def __call__(self):
        return "XTZDOWNUSDT"


XTZDOWNUSDT = XTZDOWNUSDT()


@dataclass(slots=True, frozen=True)
class XTZETH:
    name: str = "XTZETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "XTZETH"

    def __str__(self):
        return "XTZETH"

    def __call__(self):
        return "XTZETH"


XTZETH = XTZETH()


@dataclass(slots=True, frozen=True)
class XTZTRY:
    name: str = "XTZTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "XTZTRY"

    def __str__(self):
        return "XTZTRY"

    def __call__(self):
        return "XTZTRY"


XTZTRY = XTZTRY()


@dataclass(slots=True, frozen=True)
class XTZUPUSDT:
    name: str = "XTZUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "XTZUPUSDT"

    def __str__(self):
        return "XTZUPUSDT"

    def __call__(self):
        return "XTZUPUSDT"


XTZUPUSDT = XTZUPUSDT()


@dataclass(slots=True, frozen=True)
class XTZUSDT:
    name: str = "XTZUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "XTZUSDT"

    def __str__(self):
        return "XTZUSDT"

    def __call__(self):
        return "XTZUSDT"


XTZUSDT = XTZUSDT()


@dataclass(slots=True, frozen=True)
class XVGBTC:
    name: str = "XVGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XVGBTC"

    def __str__(self):
        return "XVGBTC"

    def __call__(self):
        return "XVGBTC"


XVGBTC = XVGBTC()


@dataclass(slots=True, frozen=True)
class XVGBUSD:
    name: str = "XVGBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XVGBUSD"

    def __str__(self):
        return "XVGBUSD"

    def __call__(self):
        return "XVGBUSD"


XVGBUSD = XVGBUSD()


@dataclass(slots=True, frozen=True)
class XVGETH:
    name: str = "XVGETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XVGETH"

    def __str__(self):
        return "XVGETH"

    def __call__(self):
        return "XVGETH"


XVGETH = XVGETH()


@dataclass(slots=True, frozen=True)
class XVGUSDT:
    name: str = "XVGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "XVGUSDT"

    def __str__(self):
        return "XVGUSDT"

    def __call__(self):
        return "XVGUSDT"


XVGUSDT = XVGUSDT()


@dataclass(slots=True, frozen=True)
class XVSBNB:
    name: str = "XVSBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "XVSBNB"

    def __str__(self):
        return "XVSBNB"

    def __call__(self):
        return "XVSBNB"


XVSBNB = XVSBNB()


@dataclass(slots=True, frozen=True)
class XVSBTC:
    name: str = "XVSBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "XVSBTC"

    def __str__(self):
        return "XVSBTC"

    def __call__(self):
        return "XVSBTC"


XVSBTC = XVSBTC()


@dataclass(slots=True, frozen=True)
class XVSBUSD:
    name: str = "XVSBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "XVSBUSD"

    def __str__(self):
        return "XVSBUSD"

    def __call__(self):
        return "XVSBUSD"


XVSBUSD = XVSBUSD()


@dataclass(slots=True, frozen=True)
class XVSUSDT:
    name: str = "XVSUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "XVSUSDT"

    def __str__(self):
        return "XVSUSDT"

    def __call__(self):
        return "XVSUSDT"


XVSUSDT = XVSUSDT()


@dataclass(slots=True, frozen=True)
class XZCBNB:
    name: str = "XZCBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "XZCBNB"

    def __str__(self):
        return "XZCBNB"

    def __call__(self):
        return "XZCBNB"


XZCBNB = XZCBNB()


@dataclass(slots=True, frozen=True)
class XZCBTC:
    name: str = "XZCBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XZCBTC"

    def __str__(self):
        return "XZCBTC"

    def __call__(self):
        return "XZCBTC"


XZCBTC = XZCBTC()


@dataclass(slots=True, frozen=True)
class XZCETH:
    name: str = "XZCETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "XZCETH"

    def __str__(self):
        return "XZCETH"

    def __call__(self):
        return "XZCETH"


XZCETH = XZCETH()


@dataclass(slots=True, frozen=True)
class XZCUSDT:
    name: str = "XZCUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "XZCUSDT"

    def __str__(self):
        return "XZCUSDT"

    def __call__(self):
        return "XZCUSDT"


XZCUSDT = XZCUSDT()


@dataclass(slots=True, frozen=True)
class XZCXRP:
    name: str = "XZCXRP"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "XZCXRP"

    def __str__(self):
        return "XZCXRP"

    def __call__(self):
        return "XZCXRP"


XZCXRP = XZCXRP()


@dataclass(slots=True, frozen=True)
class YFIBNB:
    name: str = "YFIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 10000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIBNB"

    def __str__(self):
        return "YFIBNB"

    def __call__(self):
        return "YFIBNB"


YFIBNB = YFIBNB()


@dataclass(slots=True, frozen=True)
class YFIBTC:
    name: str = "YFIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIBTC"

    def __str__(self):
        return "YFIBTC"

    def __call__(self):
        return "YFIBTC"


YFIBTC = YFIBTC()


@dataclass(slots=True, frozen=True)
class YFIBUSD:
    name: str = "YFIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIBUSD"

    def __str__(self):
        return "YFIBUSD"

    def __call__(self):
        return "YFIBUSD"


YFIBUSD = YFIBUSD()


@dataclass(slots=True, frozen=True)
class YFIDOWNUSDT:
    name: str = "YFIDOWNUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 30000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIDOWNUSDT"

    def __str__(self):
        return "YFIDOWNUSDT"

    def __call__(self):
        return "YFIDOWNUSDT"


YFIDOWNUSDT = YFIDOWNUSDT()


@dataclass(slots=True, frozen=True)
class YFIEUR:
    name: str = "YFIEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIEUR"

    def __str__(self):
        return "YFIEUR"

    def __call__(self):
        return "YFIEUR"


YFIEUR = YFIEUR()


@dataclass(slots=True, frozen=True)
class YFIIBNB:
    name: str = "YFIIBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIIBNB"

    def __str__(self):
        return "YFIIBNB"

    def __call__(self):
        return "YFIIBNB"


YFIIBNB = YFIIBNB()


@dataclass(slots=True, frozen=True)
class YFIIBTC:
    name: str = "YFIIBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIIBTC"

    def __str__(self):
        return "YFIIBTC"

    def __call__(self):
        return "YFIIBTC"


YFIIBTC = YFIIBTC()


@dataclass(slots=True, frozen=True)
class YFIIBUSD:
    name: str = "YFIIBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIIBUSD"

    def __str__(self):
        return "YFIIBUSD"

    def __call__(self):
        return "YFIIBUSD"


YFIIBUSD = YFIIBUSD()


@dataclass(slots=True, frozen=True)
class YFIIUSDT:
    name: str = "YFIIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00010000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIIUSDT"

    def __str__(self):
        return "YFIIUSDT"

    def __call__(self):
        return "YFIIUSDT"


YFIIUSDT = YFIIUSDT()


@dataclass(slots=True, frozen=True)
class YFIUPUSDT:
    name: str = "YFIUPUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 920000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIUPUSDT"

    def __str__(self):
        return "YFIUPUSDT"

    def __call__(self):
        return "YFIUPUSDT"


YFIUPUSDT = YFIUPUSDT()


@dataclass(slots=True, frozen=True)
class YFIUSDT:
    name: str = "YFIUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 9000.00000000
    margin: bool = False

    def __repr__(self):
        return "YFIUSDT"

    def __str__(self):
        return "YFIUSDT"

    def __call__(self):
        return "YFIUSDT"


YFIUSDT = YFIUSDT()


@dataclass(slots=True, frozen=True)
class YGGBNB:
    name: str = "YGGBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "YGGBNB"

    def __str__(self):
        return "YGGBNB"

    def __call__(self):
        return "YGGBNB"


YGGBNB = YGGBNB()


@dataclass(slots=True, frozen=True)
class YGGBTC:
    name: str = "YGGBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = False

    def __repr__(self):
        return "YGGBTC"

    def __str__(self):
        return "YGGBTC"

    def __call__(self):
        return "YGGBTC"


YGGBTC = YGGBTC()


@dataclass(slots=True, frozen=True)
class YGGBUSD:
    name: str = "YGGBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "YGGBUSD"

    def __str__(self):
        return "YGGBUSD"

    def __call__(self):
        return "YGGBUSD"


YGGBUSD = YGGBUSD()


@dataclass(slots=True, frozen=True)
class YGGUSDT:
    name: str = "YGGUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 92141578.00000000
    margin: bool = True

    def __repr__(self):
        return "YGGUSDT"

    def __str__(self):
        return "YGGUSDT"

    def __call__(self):
        return "YGGUSDT"


YGGUSDT = YGGUSDT()


@dataclass(slots=True, frozen=True)
class YOYOBNB:
    name: str = "YOYOBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "YOYOBNB"

    def __str__(self):
        return "YOYOBNB"

    def __call__(self):
        return "YOYOBNB"


YOYOBNB = YOYOBNB()


@dataclass(slots=True, frozen=True)
class YOYOBTC:
    name: str = "YOYOBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "YOYOBTC"

    def __str__(self):
        return "YOYOBTC"

    def __call__(self):
        return "YOYOBTC"


YOYOBTC = YOYOBTC()


@dataclass(slots=True, frozen=True)
class YOYOETH:
    name: str = "YOYOETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "YOYOETH"

    def __str__(self):
        return "YOYOETH"

    def __call__(self):
        return "YOYOETH"


YOYOETH = YOYOETH()


@dataclass(slots=True, frozen=True)
class ZECBNB:
    name: str = "ZECBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZECBNB"

    def __str__(self):
        return "ZECBNB"

    def __call__(self):
        return "ZECBNB"


ZECBNB = ZECBNB()


@dataclass(slots=True, frozen=True)
class ZECBTC:
    name: str = "ZECBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 10000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ZECBTC"

    def __str__(self):
        return "ZECBTC"

    def __call__(self):
        return "ZECBTC"


ZECBTC = ZECBTC()


@dataclass(slots=True, frozen=True)
class ZECBUSD:
    name: str = "ZECBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZECBUSD"

    def __str__(self):
        return "ZECBUSD"

    def __call__(self):
        return "ZECBUSD"


ZECBUSD = ZECBUSD()


@dataclass(slots=True, frozen=True)
class ZECETH:
    name: str = "ZECETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZECETH"

    def __str__(self):
        return "ZECETH"

    def __call__(self):
        return "ZECETH"


ZECETH = ZECETH()


@dataclass(slots=True, frozen=True)
class ZECPAX:
    name: str = "ZECPAX"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZECPAX"

    def __str__(self):
        return "ZECPAX"

    def __call__(self):
        return "ZECPAX"


ZECPAX = ZECPAX()


@dataclass(slots=True, frozen=True)
class ZECTUSD:
    name: str = "ZECTUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZECTUSD"

    def __str__(self):
        return "ZECTUSD"

    def __call__(self):
        return "ZECTUSD"


ZECTUSD = ZECTUSD()


@dataclass(slots=True, frozen=True)
class ZECUSDC:
    name: str = "ZECUSDC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZECUSDC"

    def __str__(self):
        return "ZECUSDC"

    def __call__(self):
        return "ZECUSDC"


ZECUSDC = ZECUSDC()


@dataclass(slots=True, frozen=True)
class ZECUSDT:
    name: str = "ZECUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00100000
    maximum_order_size: float = 90000.00000000
    margin: bool = True

    def __repr__(self):
        return "ZECUSDT"

    def __str__(self):
        return "ZECUSDT"

    def __call__(self):
        return "ZECUSDT"


ZECUSDT = ZECUSDT()


@dataclass(slots=True, frozen=True)
class ZENBNB:
    name: str = "ZENBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZENBNB"

    def __str__(self):
        return "ZENBNB"

    def __call__(self):
        return "ZENBNB"


ZENBNB = ZENBNB()


@dataclass(slots=True, frozen=True)
class ZENBTC:
    name: str = "ZENBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZENBTC"

    def __str__(self):
        return "ZENBTC"

    def __call__(self):
        return "ZENBTC"


ZENBTC = ZENBTC()


@dataclass(slots=True, frozen=True)
class ZENBUSD:
    name: str = "ZENBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ZENBUSD"

    def __str__(self):
        return "ZENBUSD"

    def __call__(self):
        return "ZENBUSD"


ZENBUSD = ZENBUSD()


@dataclass(slots=True, frozen=True)
class ZENETH:
    name: str = "ZENETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZENETH"

    def __str__(self):
        return "ZENETH"

    def __call__(self):
        return "ZENETH"


ZENETH = ZENETH()


@dataclass(slots=True, frozen=True)
class ZENUSDT:
    name: str = "ZENUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZENUSDT"

    def __str__(self):
        return "ZENUSDT"

    def __call__(self):
        return "ZENUSDT"


ZENUSDT = ZENUSDT()


@dataclass(slots=True, frozen=True)
class ZILBIDR:
    name: str = "ZILBIDR"
    precision: int = 2
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZILBIDR"

    def __str__(self):
        return "ZILBIDR"

    def __call__(self):
        return "ZILBIDR"


ZILBIDR = ZILBIDR()


@dataclass(slots=True, frozen=True)
class ZILBNB:
    name: str = "ZILBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZILBNB"

    def __str__(self):
        return "ZILBNB"

    def __call__(self):
        return "ZILBNB"


ZILBNB = ZILBNB()


@dataclass(slots=True, frozen=True)
class ZILBTC:
    name: str = "ZILBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ZILBTC"

    def __str__(self):
        return "ZILBTC"

    def __call__(self):
        return "ZILBTC"


ZILBTC = ZILBTC()


@dataclass(slots=True, frozen=True)
class ZILBUSD:
    name: str = "ZILBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ZILBUSD"

    def __str__(self):
        return "ZILBUSD"

    def __call__(self):
        return "ZILBUSD"


ZILBUSD = ZILBUSD()


@dataclass(slots=True, frozen=True)
class ZILETH:
    name: str = "ZILETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZILETH"

    def __str__(self):
        return "ZILETH"

    def __call__(self):
        return "ZILETH"


ZILETH = ZILETH()


@dataclass(slots=True, frozen=True)
class ZILEUR:
    name: str = "ZILEUR"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZILEUR"

    def __str__(self):
        return "ZILEUR"

    def __call__(self):
        return "ZILEUR"


ZILEUR = ZILEUR()


@dataclass(slots=True, frozen=True)
class ZILTRY:
    name: str = "ZILTRY"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9222449.00000000
    margin: bool = False

    def __repr__(self):
        return "ZILTRY"

    def __str__(self):
        return "ZILTRY"

    def __call__(self):
        return "ZILTRY"


ZILTRY = ZILTRY()


@dataclass(slots=True, frozen=True)
class ZILUSDT:
    name: str = "ZILUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ZILUSDT"

    def __str__(self):
        return "ZILUSDT"

    def __call__(self):
        return "ZILUSDT"


ZILUSDT = ZILUSDT()


@dataclass(slots=True, frozen=True)
class ZRXBNB:
    name: str = "ZRXBNB"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.10000000
    maximum_order_size: float = 9000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZRXBNB"

    def __str__(self):
        return "ZRXBNB"

    def __call__(self):
        return "ZRXBNB"


ZRXBNB = ZRXBNB()


@dataclass(slots=True, frozen=True)
class ZRXBTC:
    name: str = "ZRXBTC"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = True

    def __repr__(self):
        return "ZRXBTC"

    def __str__(self):
        return "ZRXBTC"

    def __call__(self):
        return "ZRXBTC"


ZRXBTC = ZRXBTC()


@dataclass(slots=True, frozen=True)
class ZRXBUSD:
    name: str = "ZRXBUSD"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZRXBUSD"

    def __str__(self):
        return "ZRXBUSD"

    def __call__(self):
        return "ZRXBUSD"


ZRXBUSD = ZRXBUSD()


@dataclass(slots=True, frozen=True)
class ZRXETH:
    name: str = "ZRXETH"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 90000000.00000000
    margin: bool = False

    def __repr__(self):
        return "ZRXETH"

    def __str__(self):
        return "ZRXETH"

    def __call__(self):
        return "ZRXETH"


ZRXETH = ZRXETH()


@dataclass(slots=True, frozen=True)
class ZRXUSDT:
    name: str = "ZRXUSDT"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.00000000
    maximum_order_size: float = 900000.00000000
    margin: bool = True

    def __repr__(self):
        return "ZRXUSDT"

    def __str__(self):
        return "ZRXUSDT"

    def __call__(self):
        return "ZRXUSDT"


ZRXUSDT = ZRXUSDT()


