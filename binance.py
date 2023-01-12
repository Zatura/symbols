from dataclasses import dataclass


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


