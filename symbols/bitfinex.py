from dataclasses import dataclass




ONEINCH_USD = ONEINCH_USD()


@dataclass(slots=True, frozen=True)
class ONEINCH_USD:
    """
        name: t1INCH:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "t1INCH:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "t1INCH:USD"

    def __str__(self):
        return "t1INCH:USD"

    def __call__(self):
        return "t1INCH:USD"


ONEINCH_UST = ONEINCH_UST()


@dataclass(slots=True, frozen=True)
class ONEINCH_UST:
    """
        name: t1INCH:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "t1INCH:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "t1INCH:UST"

    def __str__(self):
        return "t1INCH:UST"

    def __call__(self):
        return "t1INCH:UST"


AAABBB = AAABBB()


@dataclass(slots=True, frozen=True)
class AAABBB:
    """
        name: tAAABBB
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100.0
        margin: False
    """
    name: str = "tAAABBB"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100.0
    margin: bool = False

    def __repr__(self):
        return "tAAABBB"

    def __str__(self):
        return "tAAABBB"

    def __call__(self):
        return "tAAABBB"


AAVE_USD = AAVE_USD()


@dataclass(slots=True, frozen=True)
class AAVE_USD:
    """
        name: tAAVE:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: False
    """
    name: str = "tAAVE:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = False

    def __repr__(self):
        return "tAAVE:USD"

    def __str__(self):
        return "tAAVE:USD"

    def __call__(self):
        return "tAAVE:USD"


AAVE_UST = AAVE_UST()


@dataclass(slots=True, frozen=True)
class AAVE_UST:
    """
        name: tAAVE:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: False
    """
    name: str = "tAAVE:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = False

    def __repr__(self):
        return "tAAVE:UST"

    def __str__(self):
        return "tAAVE:UST"

    def __call__(self):
        return "tAAVE:UST"


AAVEF0_USTF0 = AAVEF0_USTF0()


@dataclass(slots=True, frozen=True)
class AAVEF0_USTF0:
    """
        name: tAAVEF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tAAVEF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tAAVEF0:USTF0"

    def __str__(self):
        return "tAAVEF0:USTF0"

    def __call__(self):
        return "tAAVEF0:USTF0"


ADABTC = ADABTC()


@dataclass(slots=True, frozen=True)
class ADABTC:
    """
        name: tADABTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tADABTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tADABTC"

    def __str__(self):
        return "tADABTC"

    def __call__(self):
        return "tADABTC"


ADAF0_USTF0 = ADAF0_USTF0()


@dataclass(slots=True, frozen=True)
class ADAF0_USTF0:
    """
        name: tADAF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 4.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tADAF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tADAF0:USTF0"

    def __str__(self):
        return "tADAF0:USTF0"

    def __call__(self):
        return "tADAF0:USTF0"


ADAUSD = ADAUSD()


@dataclass(slots=True, frozen=True)
class ADAUSD:
    """
        name: tADAUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tADAUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tADAUSD"

    def __str__(self):
        return "tADAUSD"

    def __call__(self):
        return "tADAUSD"


ADAUST = ADAUST()


@dataclass(slots=True, frozen=True)
class ADAUST:
    """
        name: tADAUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tADAUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tADAUST"

    def __str__(self):
        return "tADAUST"

    def __call__(self):
        return "tADAUST"


AIXUSD = AIXUSD()


@dataclass(slots=True, frozen=True)
class AIXUSD:
    """
        name: tAIXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 570.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tAIXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 570.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tAIXUSD"

    def __str__(self):
        return "tAIXUSD"

    def __call__(self):
        return "tAIXUSD"


AIXUST = AIXUST()


@dataclass(slots=True, frozen=True)
class AIXUST:
    """
        name: tAIXUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 570.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tAIXUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 570.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tAIXUST"

    def __str__(self):
        return "tAIXUST"

    def __call__(self):
        return "tAIXUST"


ALBT_USD = ALBT_USD()


@dataclass(slots=True, frozen=True)
class ALBT_USD:
    """
        name: tALBT:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 22.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tALBT:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 22.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tALBT:USD"

    def __str__(self):
        return "tALBT:USD"

    def __call__(self):
        return "tALBT:USD"


ALGBTC = ALGBTC()


@dataclass(slots=True, frozen=True)
class ALGBTC:
    """
        name: tALGBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 150000.0
        margin: False
    """
    name: str = "tALGBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 150000.0
    margin: bool = False

    def __repr__(self):
        return "tALGBTC"

    def __str__(self):
        return "tALGBTC"

    def __call__(self):
        return "tALGBTC"


ALGF0_USTF0 = ALGF0_USTF0()


@dataclass(slots=True, frozen=True)
class ALGF0_USTF0:
    """
        name: tALGF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 6.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tALGF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tALGF0:USTF0"

    def __str__(self):
        return "tALGF0:USTF0"

    def __call__(self):
        return "tALGF0:USTF0"


ALGUSD = ALGUSD()


@dataclass(slots=True, frozen=True)
class ALGUSD:
    """
        name: tALGUSD
        precision: 5
        minimum_margin: 25.0
        initial_margin: 50.0
        minimum_order_size: 6.0
        maximum_order_size: 150000.0
        margin: True
    """
    name: str = "tALGUSD"
    precision: int = 5
    minimum_margin: float = 25.0
    initial_margin: float = 50.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 150000.0
    margin: bool = True

    def __repr__(self):
        return "tALGUSD"

    def __str__(self):
        return "tALGUSD"

    def __call__(self):
        return "tALGUSD"


ALGUST = ALGUST()


@dataclass(slots=True, frozen=True)
class ALGUST:
    """
        name: tALGUST
        precision: 5
        minimum_margin: 25.0
        initial_margin: 50.0
        minimum_order_size: 6.0
        maximum_order_size: 150000.0
        margin: True
    """
    name: str = "tALGUST"
    precision: int = 5
    minimum_margin: float = 25.0
    initial_margin: float = 50.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 150000.0
    margin: bool = True

    def __repr__(self):
        return "tALGUST"

    def __str__(self):
        return "tALGUST"

    def __call__(self):
        return "tALGUST"


AMPBTC = AMPBTC()


@dataclass(slots=True, frozen=True)
class AMPBTC:
    """
        name: tAMPBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 25000.0
        margin: False
    """
    name: str = "tAMPBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 25000.0
    margin: bool = False

    def __repr__(self):
        return "tAMPBTC"

    def __str__(self):
        return "tAMPBTC"

    def __call__(self):
        return "tAMPBTC"


AMPF0_USTF0 = AMPF0_USTF0()


@dataclass(slots=True, frozen=True)
class AMPF0_USTF0:
    """
        name: tAMPF0:USTF0
        precision: 5
        minimum_margin: 2.5
        initial_margin: 5.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tAMPF0:USTF0"
    precision: int = 5
    minimum_margin: float = 2.5
    initial_margin: float = 5.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tAMPF0:USTF0"

    def __str__(self):
        return "tAMPF0:USTF0"

    def __call__(self):
        return "tAMPF0:USTF0"


AMPUSD = AMPUSD()


@dataclass(slots=True, frozen=True)
class AMPUSD:
    """
        name: tAMPUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 25000.0
        margin: False
    """
    name: str = "tAMPUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 25000.0
    margin: bool = False

    def __repr__(self):
        return "tAMPUSD"

    def __str__(self):
        return "tAMPUSD"

    def __call__(self):
        return "tAMPUSD"


AMPUST = AMPUST()


@dataclass(slots=True, frozen=True)
class AMPUST:
    """
        name: tAMPUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 25000.0
        margin: False
    """
    name: str = "tAMPUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 25000.0
    margin: bool = False

    def __repr__(self):
        return "tAMPUST"

    def __str__(self):
        return "tAMPUST"

    def __call__(self):
        return "tAMPUST"


ANCUSD = ANCUSD()


@dataclass(slots=True, frozen=True)
class ANCUSD:
    """
        name: tANCUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 10.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tANCUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 10.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tANCUSD"

    def __str__(self):
        return "tANCUSD"

    def __call__(self):
        return "tANCUSD"


ANTBTC = ANTBTC()


@dataclass(slots=True, frozen=True)
class ANTBTC:
    """
        name: tANTBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tANTBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tANTBTC"

    def __str__(self):
        return "tANTBTC"

    def __call__(self):
        return "tANTBTC"


ANTUSD = ANTUSD()


@dataclass(slots=True, frozen=True)
class ANTUSD:
    """
        name: tANTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tANTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tANTUSD"

    def __str__(self):
        return "tANTUSD"

    def __call__(self):
        return "tANTUSD"


APEF0_USTF0 = APEF0_USTF0()


@dataclass(slots=True, frozen=True)
class APEF0_USTF0:
    """
        name: tAPEF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.4
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tAPEF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tAPEF0:USTF0"

    def __str__(self):
        return "tAPEF0:USTF0"

    def __call__(self):
        return "tAPEF0:USTF0"


APENFT_USD = APENFT_USD()


@dataclass(slots=True, frozen=True)
class APENFT_USD:
    """
        name: tAPENFT:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 40000000000.0
        margin: False
    """
    name: str = "tAPENFT:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 40000000000.0
    margin: bool = False

    def __repr__(self):
        return "tAPENFT:USD"

    def __str__(self):
        return "tAPENFT:USD"

    def __call__(self):
        return "tAPENFT:USD"


APENFT_UST = APENFT_UST()


@dataclass(slots=True, frozen=True)
class APENFT_UST:
    """
        name: tAPENFT:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 40000000000.0
        margin: False
    """
    name: str = "tAPENFT:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 40000000000.0
    margin: bool = False

    def __repr__(self):
        return "tAPENFT:UST"

    def __str__(self):
        return "tAPENFT:UST"

    def __call__(self):
        return "tAPENFT:UST"


APEUSD = APEUSD()


@dataclass(slots=True, frozen=True)
class APEUSD:
    """
        name: tAPEUSD
        precision: 5
        minimum_margin: 30.0
        initial_margin: 60.0
        minimum_order_size: 0.4
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tAPEUSD"
    precision: int = 5
    minimum_margin: float = 30.0
    initial_margin: float = 60.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tAPEUSD"

    def __str__(self):
        return "tAPEUSD"

    def __call__(self):
        return "tAPEUSD"


APEUST = APEUST()


@dataclass(slots=True, frozen=True)
class APEUST:
    """
        name: tAPEUST
        precision: 5
        minimum_margin: 30.0
        initial_margin: 60.0
        minimum_order_size: 0.4
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tAPEUST"
    precision: int = 5
    minimum_margin: float = 30.0
    initial_margin: float = 60.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tAPEUST"

    def __str__(self):
        return "tAPEUST"

    def __call__(self):
        return "tAPEUST"


APTF0_USTF0 = APTF0_USTF0()


@dataclass(slots=True, frozen=True)
class APTF0_USTF0:
    """
        name: tAPTF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.001
        maximum_order_size: 30000.0
        margin: True
    """
    name: str = "tAPTF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 30000.0
    margin: bool = True

    def __repr__(self):
        return "tAPTF0:USTF0"

    def __str__(self):
        return "tAPTF0:USTF0"

    def __call__(self):
        return "tAPTF0:USTF0"


APTUSD = APTUSD()


@dataclass(slots=True, frozen=True)
class APTUSD:
    """
        name: tAPTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 30000.0
        margin: False
    """
    name: str = "tAPTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 30000.0
    margin: bool = False

    def __repr__(self):
        return "tAPTUSD"

    def __str__(self):
        return "tAPTUSD"

    def __call__(self):
        return "tAPTUSD"


APTUST = APTUST()


@dataclass(slots=True, frozen=True)
class APTUST:
    """
        name: tAPTUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 30000.0
        margin: False
    """
    name: str = "tAPTUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 30000.0
    margin: bool = False

    def __repr__(self):
        return "tAPTUST"

    def __str__(self):
        return "tAPTUST"

    def __call__(self):
        return "tAPTUST"


ATLAS_USD = ATLAS_USD()


@dataclass(slots=True, frozen=True)
class ATLAS_USD:
    """
        name: tATLAS:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 232.0
        maximum_order_size: 25000000.0
        margin: False
    """
    name: str = "tATLAS:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 232.0
    maximum_order_size: float = 25000000.0
    margin: bool = False

    def __repr__(self):
        return "tATLAS:USD"

    def __str__(self):
        return "tATLAS:USD"

    def __call__(self):
        return "tATLAS:USD"


ATLAS_UST = ATLAS_UST()


@dataclass(slots=True, frozen=True)
class ATLAS_UST:
    """
        name: tATLAS:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 232.0
        maximum_order_size: 25000000.0
        margin: False
    """
    name: str = "tATLAS:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 232.0
    maximum_order_size: float = 25000000.0
    margin: bool = False

    def __repr__(self):
        return "tATLAS:UST"

    def __str__(self):
        return "tATLAS:UST"

    def __call__(self):
        return "tATLAS:UST"


ATOBTC = ATOBTC()


@dataclass(slots=True, frozen=True)
class ATOBTC:
    """
        name: tATOBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tATOBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tATOBTC"

    def __str__(self):
        return "tATOBTC"

    def __call__(self):
        return "tATOBTC"


ATOETH = ATOETH()


@dataclass(slots=True, frozen=True)
class ATOETH:
    """
        name: tATOETH
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tATOETH"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tATOETH"

    def __str__(self):
        return "tATOETH"

    def __call__(self):
        return "tATOETH"


ATOF0_USTF0 = ATOF0_USTF0()


@dataclass(slots=True, frozen=True)
class ATOF0_USTF0:
    """
        name: tATOF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.2
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tATOF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tATOF0:USTF0"

    def __str__(self):
        return "tATOF0:USTF0"

    def __call__(self):
        return "tATOF0:USTF0"


ATOUSD = ATOUSD()


@dataclass(slots=True, frozen=True)
class ATOUSD:
    """
        name: tATOUSD
        precision: 5
        minimum_margin: 25.0
        initial_margin: 50.0
        minimum_order_size: 0.2
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tATOUSD"
    precision: int = 5
    minimum_margin: float = 25.0
    initial_margin: float = 50.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tATOUSD"

    def __str__(self):
        return "tATOUSD"

    def __call__(self):
        return "tATOUSD"


ATOUST = ATOUST()


@dataclass(slots=True, frozen=True)
class ATOUST:
    """
        name: tATOUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tATOUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tATOUST"

    def __str__(self):
        return "tATOUST"

    def __call__(self):
        return "tATOUST"


AVAX_BTC = AVAX_BTC()


@dataclass(slots=True, frozen=True)
class AVAX_BTC:
    """
        name: tAVAX:BTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.08
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tAVAX:BTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.08
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tAVAX:BTC"

    def __str__(self):
        return "tAVAX:BTC"

    def __call__(self):
        return "tAVAX:BTC"


AVAX_USD = AVAX_USD()


@dataclass(slots=True, frozen=True)
class AVAX_USD:
    """
        name: tAVAX:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.08
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tAVAX:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.08
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tAVAX:USD"

    def __str__(self):
        return "tAVAX:USD"

    def __call__(self):
        return "tAVAX:USD"


AVAX_UST = AVAX_UST()


@dataclass(slots=True, frozen=True)
class AVAX_UST:
    """
        name: tAVAX:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.08
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tAVAX:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.08
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tAVAX:UST"

    def __str__(self):
        return "tAVAX:UST"

    def __call__(self):
        return "tAVAX:UST"


AVAXF0_BTCF0 = AVAXF0_BTCF0()


@dataclass(slots=True, frozen=True)
class AVAXF0_BTCF0:
    """
        name: tAVAXF0:BTCF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.08
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tAVAXF0:BTCF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.08
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tAVAXF0:BTCF0"

    def __str__(self):
        return "tAVAXF0:BTCF0"

    def __call__(self):
        return "tAVAXF0:BTCF0"


AVAXF0_USTF0 = AVAXF0_USTF0()


@dataclass(slots=True, frozen=True)
class AVAXF0_USTF0:
    """
        name: tAVAXF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.08
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tAVAXF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.08
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tAVAXF0:USTF0"

    def __str__(self):
        return "tAVAXF0:USTF0"

    def __call__(self):
        return "tAVAXF0:USTF0"


AXSF0_USTF0 = AXSF0_USTF0()


@dataclass(slots=True, frozen=True)
class AXSF0_USTF0:
    """
        name: tAXSF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tAXSF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tAXSF0:USTF0"

    def __str__(self):
        return "tAXSF0:USTF0"

    def __call__(self):
        return "tAXSF0:USTF0"


AXSUSD = AXSUSD()


@dataclass(slots=True, frozen=True)
class AXSUSD:
    """
        name: tAXSUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tAXSUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tAXSUSD"

    def __str__(self):
        return "tAXSUSD"

    def __call__(self):
        return "tAXSUSD"


AXSUST = AXSUST()


@dataclass(slots=True, frozen=True)
class AXSUST:
    """
        name: tAXSUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tAXSUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tAXSUST"

    def __str__(self):
        return "tAXSUST"

    def __call__(self):
        return "tAXSUST"


B2MUSD = B2MUSD()


@dataclass(slots=True, frozen=True)
class B2MUSD:
    """
        name: tB2MUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 144.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tB2MUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 144.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tB2MUSD"

    def __str__(self):
        return "tB2MUSD"

    def __call__(self):
        return "tB2MUSD"


B2MUST = B2MUST()


@dataclass(slots=True, frozen=True)
class B2MUST:
    """
        name: tB2MUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 144.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tB2MUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 144.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tB2MUST"

    def __str__(self):
        return "tB2MUST"

    def __call__(self):
        return "tB2MUST"


BALUSD = BALUSD()


@dataclass(slots=True, frozen=True)
class BALUSD:
    """
        name: tBALUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tBALUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tBALUSD"

    def __str__(self):
        return "tBALUSD"

    def __call__(self):
        return "tBALUSD"


BALUST = BALUST()


@dataclass(slots=True, frozen=True)
class BALUST:
    """
        name: tBALUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tBALUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tBALUST"

    def __str__(self):
        return "tBALUST"

    def __call__(self):
        return "tBALUST"


BAND_USD = BAND_USD()


@dataclass(slots=True, frozen=True)
class BAND_USD:
    """
        name: tBAND:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tBAND:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tBAND:USD"

    def __str__(self):
        return "tBAND:USD"

    def __call__(self):
        return "tBAND:USD"


BAND_UST = BAND_UST()


@dataclass(slots=True, frozen=True)
class BAND_UST:
    """
        name: tBAND:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tBAND:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tBAND:UST"

    def __str__(self):
        return "tBAND:UST"

    def __call__(self):
        return "tBAND:UST"


BATUSD = BATUSD()


@dataclass(slots=True, frozen=True)
class BATUSD:
    """
        name: tBATUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 200000.0
        margin: False
    """
    name: str = "tBATUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 200000.0
    margin: bool = False

    def __repr__(self):
        return "tBATUSD"

    def __str__(self):
        return "tBATUSD"

    def __call__(self):
        return "tBATUSD"


BATUST = BATUST()


@dataclass(slots=True, frozen=True)
class BATUST:
    """
        name: tBATUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 200000.0
        margin: False
    """
    name: str = "tBATUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 200000.0
    margin: bool = False

    def __repr__(self):
        return "tBATUST"

    def __str__(self):
        return "tBATUST"

    def __call__(self):
        return "tBATUST"


BCHABC_USD = BCHABC_USD()


@dataclass(slots=True, frozen=True)
class BCHABC_USD:
    """
        name: tBCHABC:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 40962.0
        maximum_order_size: 1000000000.0
        margin: False
    """
    name: str = "tBCHABC:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 40962.0
    maximum_order_size: float = 1000000000.0
    margin: bool = False

    def __repr__(self):
        return "tBCHABC:USD"

    def __str__(self):
        return "tBCHABC:USD"

    def __call__(self):
        return "tBCHABC:USD"


BCHN_USD = BCHN_USD()


@dataclass(slots=True, frozen=True)
class BCHN_USD:
    """
        name: tBCHN:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 1000.0
        margin: True
    """
    name: str = "tBCHN:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 1000.0
    margin: bool = True

    def __repr__(self):
        return "tBCHN:USD"

    def __str__(self):
        return "tBCHN:USD"

    def __call__(self):
        return "tBCHN:USD"


BEST_USD = BEST_USD()


@dataclass(slots=True, frozen=True)
class BEST_USD:
    """
        name: tBEST:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tBEST:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tBEST:USD"

    def __str__(self):
        return "tBEST:USD"

    def __call__(self):
        return "tBEST:USD"


BMNBTC = BMNBTC()


@dataclass(slots=True, frozen=True)
class BMNBTC:
    """
        name: tBMNBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00002
        maximum_order_size: 1.0
        margin: False
    """
    name: str = "tBMNBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00002
    maximum_order_size: float = 1.0
    margin: bool = False

    def __repr__(self):
        return "tBMNBTC"

    def __str__(self):
        return "tBMNBTC"

    def __call__(self):
        return "tBMNBTC"


BMNUSD = BMNUSD()


@dataclass(slots=True, frozen=True)
class BMNUSD:
    """
        name: tBMNUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00002
        maximum_order_size: 1.0
        margin: False
    """
    name: str = "tBMNUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00002
    maximum_order_size: float = 1.0
    margin: bool = False

    def __repr__(self):
        return "tBMNUSD"

    def __str__(self):
        return "tBMNUSD"

    def __call__(self):
        return "tBMNUSD"


BNTUSD = BNTUSD()


@dataclass(slots=True, frozen=True)
class BNTUSD:
    """
        name: tBNTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 20000.0
        margin: False
    """
    name: str = "tBNTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 20000.0
    margin: bool = False

    def __repr__(self):
        return "tBNTUSD"

    def __str__(self):
        return "tBNTUSD"

    def __call__(self):
        return "tBNTUSD"


BOBA_USD = BOBA_USD()


@dataclass(slots=True, frozen=True)
class BOBA_USD:
    """
        name: tBOBA:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tBOBA:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tBOBA:USD"

    def __str__(self):
        return "tBOBA:USD"

    def __call__(self):
        return "tBOBA:USD"


BOBA_UST = BOBA_UST()


@dataclass(slots=True, frozen=True)
class BOBA_UST:
    """
        name: tBOBA:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tBOBA:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tBOBA:UST"

    def __str__(self):
        return "tBOBA:UST"

    def __call__(self):
        return "tBOBA:UST"


BOOUSD = BOOUSD()


@dataclass(slots=True, frozen=True)
class BOOUSD:
    """
        name: tBOOUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 45000.0
        margin: False
    """
    name: str = "tBOOUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 45000.0
    margin: bool = False

    def __repr__(self):
        return "tBOOUSD"

    def __str__(self):
        return "tBOOUSD"

    def __call__(self):
        return "tBOOUSD"


BOOUST = BOOUST()


@dataclass(slots=True, frozen=True)
class BOOUST:
    """
        name: tBOOUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 45000.0
        margin: False
    """
    name: str = "tBOOUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 45000.0
    margin: bool = False

    def __repr__(self):
        return "tBOOUST"

    def __str__(self):
        return "tBOOUST"

    def __call__(self):
        return "tBOOUST"


BOSON_USD = BOSON_USD()


@dataclass(slots=True, frozen=True)
class BOSON_USD:
    """
        name: tBOSON:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tBOSON:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tBOSON:USD"

    def __str__(self):
        return "tBOSON:USD"

    def __call__(self):
        return "tBOSON:USD"


BOSON_UST = BOSON_UST()


@dataclass(slots=True, frozen=True)
class BOSON_UST:
    """
        name: tBOSON:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tBOSON:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tBOSON:UST"

    def __str__(self):
        return "tBOSON:UST"

    def __call__(self):
        return "tBOSON:UST"


BTC_CNHT = BTC_CNHT()


@dataclass(slots=True, frozen=True)
class BTC_CNHT:
    """
        name: tBTC:CNHT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00006
        maximum_order_size: 5000.0
        margin: False
    """
    name: str = "tBTC:CNHT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 5000.0
    margin: bool = False

    def __repr__(self):
        return "tBTC:CNHT"

    def __str__(self):
        return "tBTC:CNHT"

    def __call__(self):
        return "tBTC:CNHT"


BTC_MXNT = BTC_MXNT()


@dataclass(slots=True, frozen=True)
class BTC_MXNT:
    """
        name: tBTC:MXNT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 500.0
        margin: False
    """
    name: str = "tBTC:MXNT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 500.0
    margin: bool = False

    def __repr__(self):
        return "tBTC:MXNT"

    def __str__(self):
        return "tBTC:MXNT"

    def __call__(self):
        return "tBTC:MXNT"


BTC_XAUT = BTC_XAUT()


@dataclass(slots=True, frozen=True)
class BTC_XAUT:
    """
        name: tBTC:XAUT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.0002
        maximum_order_size: 250.0
        margin: False
    """
    name: str = "tBTC:XAUT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.0002
    maximum_order_size: float = 250.0
    margin: bool = False

    def __repr__(self):
        return "tBTC:XAUT"

    def __str__(self):
        return "tBTC:XAUT"

    def __call__(self):
        return "tBTC:XAUT"


BTCDOMF0_USTF0 = BTCDOMF0_USTF0()


@dataclass(slots=True, frozen=True)
class BTCDOMF0_USTF0:
    """
        name: tBTCDOMF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.01
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tBTCDOMF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.01
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tBTCDOMF0:USTF0"

    def __str__(self):
        return "tBTCDOMF0:USTF0"

    def __call__(self):
        return "tBTCDOMF0:USTF0"


BTCEUR = BTCEUR()


@dataclass(slots=True, frozen=True)
class BTCEUR:
    """
        name: tBTCEUR
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.00006
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tBTCEUR"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tBTCEUR"

    def __str__(self):
        return "tBTCEUR"

    def __call__(self):
        return "tBTCEUR"


BTCEUT = BTCEUT()


@dataclass(slots=True, frozen=True)
class BTCEUT:
    """
        name: tBTCEUT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00006
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tBTCEUT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tBTCEUT"

    def __str__(self):
        return "tBTCEUT"

    def __call__(self):
        return "tBTCEUT"


BTCF0_EUTF0 = BTCF0_EUTF0()


@dataclass(slots=True, frozen=True)
class BTCF0_EUTF0:
    """
        name: tBTCF0:EUTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.0002
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tBTCF0:EUTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.0002
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tBTCF0:EUTF0"

    def __str__(self):
        return "tBTCF0:EUTF0"

    def __call__(self):
        return "tBTCF0:EUTF0"


BTCF0_USTF0 = BTCF0_USTF0()


@dataclass(slots=True, frozen=True)
class BTCF0_USTF0:
    """
        name: tBTCF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.00006
        maximum_order_size: 100.0
        margin: True
    """
    name: str = "tBTCF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 100.0
    margin: bool = True

    def __repr__(self):
        return "tBTCF0:USTF0"

    def __str__(self):
        return "tBTCF0:USTF0"

    def __call__(self):
        return "tBTCF0:USTF0"


BTCGBP = BTCGBP()


@dataclass(slots=True, frozen=True)
class BTCGBP:
    """
        name: tBTCGBP
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00006
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tBTCGBP"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tBTCGBP"

    def __str__(self):
        return "tBTCGBP"

    def __call__(self):
        return "tBTCGBP"


BTCJPY = BTCJPY()


@dataclass(slots=True, frozen=True)
class BTCJPY:
    """
        name: tBTCJPY
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00006
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tBTCJPY"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tBTCJPY"

    def __str__(self):
        return "tBTCJPY"

    def __call__(self):
        return "tBTCJPY"


BTCMIM = BTCMIM()


@dataclass(slots=True, frozen=True)
class BTCMIM:
    """
        name: tBTCMIM
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.0002
        maximum_order_size: 2500.0
        margin: False
    """
    name: str = "tBTCMIM"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.0002
    maximum_order_size: float = 2500.0
    margin: bool = False

    def __repr__(self):
        return "tBTCMIM"

    def __str__(self):
        return "tBTCMIM"

    def __call__(self):
        return "tBTCMIM"


BTCTRY = BTCTRY()


@dataclass(slots=True, frozen=True)
class BTCTRY:
    """
        name: tBTCTRY
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tBTCTRY"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tBTCTRY"

    def __str__(self):
        return "tBTCTRY"

    def __call__(self):
        return "tBTCTRY"


BTCUSD = BTCUSD()


@dataclass(slots=True, frozen=True)
class BTCUSD:
    """
        name: tBTCUSD
        precision: 5
        minimum_margin: 5.0
        initial_margin: 10.0
        minimum_order_size: 0.00006
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tBTCUSD"
    precision: int = 5
    minimum_margin: float = 5.0
    initial_margin: float = 10.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tBTCUSD"

    def __str__(self):
        return "tBTCUSD"

    def __call__(self):
        return "tBTCUSD"


BTCUST = BTCUST()


@dataclass(slots=True, frozen=True)
class BTCUST:
    """
        name: tBTCUST
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.00006
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tBTCUST"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tBTCUST"

    def __str__(self):
        return "tBTCUST"

    def __call__(self):
        return "tBTCUST"


BTGBTC = BTGBTC()


@dataclass(slots=True, frozen=True)
class BTGBTC:
    """
        name: tBTGBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.1
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tBTGBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.1
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tBTGBTC"

    def __str__(self):
        return "tBTGBTC"

    def __call__(self):
        return "tBTGBTC"


BTGUSD = BTGUSD()


@dataclass(slots=True, frozen=True)
class BTGUSD:
    """
        name: tBTGUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.1
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tBTGUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.1
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tBTGUSD"

    def __str__(self):
        return "tBTGUSD"

    def __call__(self):
        return "tBTGUSD"


BTSE_USD = BTSE_USD()


@dataclass(slots=True, frozen=True)
class BTSE_USD:
    """
        name: tBTSE:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tBTSE:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tBTSE:USD"

    def __str__(self):
        return "tBTSE:USD"

    def __call__(self):
        return "tBTSE:USD"


BTTUSD = BTTUSD()


@dataclass(slots=True, frozen=True)
class BTTUSD:
    """
        name: tBTTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 1970444.0
        maximum_order_size: 25000000000.0
        margin: False
    """
    name: str = "tBTTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 1970444.0
    maximum_order_size: float = 25000000000.0
    margin: bool = False

    def __repr__(self):
        return "tBTTUSD"

    def __str__(self):
        return "tBTTUSD"

    def __call__(self):
        return "tBTTUSD"


CCDBTC = CCDBTC()


@dataclass(slots=True, frozen=True)
class CCDBTC:
    """
        name: tCCDBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 100.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tCCDBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 100.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tCCDBTC"

    def __str__(self):
        return "tCCDBTC"

    def __call__(self):
        return "tCCDBTC"


CCDUSD = CCDUSD()


@dataclass(slots=True, frozen=True)
class CCDUSD:
    """
        name: tCCDUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 100.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tCCDUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 100.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tCCDUSD"

    def __str__(self):
        return "tCCDUSD"

    def __call__(self):
        return "tCCDUSD"


CCDUST = CCDUST()


@dataclass(slots=True, frozen=True)
class CCDUST:
    """
        name: tCCDUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 100.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tCCDUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 100.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tCCDUST"

    def __str__(self):
        return "tCCDUST"

    def __call__(self):
        return "tCCDUST"


CHEX_USD = CHEX_USD()


@dataclass(slots=True, frozen=True)
class CHEX_USD:
    """
        name: tCHEX:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 88.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tCHEX:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 88.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tCHEX:USD"

    def __str__(self):
        return "tCHEX:USD"

    def __call__(self):
        return "tCHEX:USD"


CHSB_BTC = CHSB_BTC()


@dataclass(slots=True, frozen=True)
class CHSB_BTC:
    """
        name: tCHSB:BTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tCHSB:BTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tCHSB:BTC"

    def __str__(self):
        return "tCHSB:BTC"

    def __call__(self):
        return "tCHSB:BTC"


CHSB_USD = CHSB_USD()


@dataclass(slots=True, frozen=True)
class CHSB_USD:
    """
        name: tCHSB:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tCHSB:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tCHSB:USD"

    def __str__(self):
        return "tCHSB:USD"

    def __call__(self):
        return "tCHSB:USD"


CHSB_UST = CHSB_UST()


@dataclass(slots=True, frozen=True)
class CHSB_UST:
    """
        name: tCHSB:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tCHSB:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tCHSB:UST"

    def __str__(self):
        return "tCHSB:UST"

    def __call__(self):
        return "tCHSB:UST"


CHZUSD = CHZUSD()


@dataclass(slots=True, frozen=True)
class CHZUSD:
    """
        name: tCHZUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 16.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tCHZUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 16.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tCHZUSD"

    def __str__(self):
        return "tCHZUSD"

    def __call__(self):
        return "tCHZUSD"


CHZUST = CHZUST()


@dataclass(slots=True, frozen=True)
class CHZUST:
    """
        name: tCHZUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 16.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tCHZUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 16.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tCHZUST"

    def __str__(self):
        return "tCHZUST"

    def __call__(self):
        return "tCHZUST"


CLOUSD = CLOUSD()


@dataclass(slots=True, frozen=True)
class CLOUSD:
    """
        name: tCLOUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 624.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tCLOUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 624.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tCLOUSD"

    def __str__(self):
        return "tCLOUSD"

    def __call__(self):
        return "tCLOUSD"


CNH_CNHT = CNH_CNHT()


@dataclass(slots=True, frozen=True)
class CNH_CNHT:
    """
        name: tCNH:CNHT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 14.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tCNH:CNHT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 14.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tCNH:CNHT"

    def __str__(self):
        return "tCNH:CNHT"

    def __call__(self):
        return "tCNH:CNHT"


COMP_USD = COMP_USD()


@dataclass(slots=True, frozen=True)
class COMP_USD:
    """
        name: tCOMP:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.04
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tCOMP:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tCOMP:USD"

    def __str__(self):
        return "tCOMP:USD"

    def __call__(self):
        return "tCOMP:USD"


COMP_UST = COMP_UST()


@dataclass(slots=True, frozen=True)
class COMP_UST:
    """
        name: tCOMP:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.04
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tCOMP:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tCOMP:UST"

    def __str__(self):
        return "tCOMP:UST"

    def __call__(self):
        return "tCOMP:UST"


COMPF0_USTF0 = COMPF0_USTF0()


@dataclass(slots=True, frozen=True)
class COMPF0_USTF0:
    """
        name: tCOMPF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.04
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tCOMPF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tCOMPF0:USTF0"

    def __str__(self):
        return "tCOMPF0:USTF0"

    def __call__(self):
        return "tCOMPF0:USTF0"


CONV_USD = CONV_USD()


@dataclass(slots=True, frozen=True)
class CONV_USD:
    """
        name: tCONV:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 50000000.0
        margin: False
    """
    name: str = "tCONV:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 50000000.0
    margin: bool = False

    def __repr__(self):
        return "tCONV:USD"

    def __str__(self):
        return "tCONV:USD"

    def __call__(self):
        return "tCONV:USD"


CONV_UST = CONV_UST()


@dataclass(slots=True, frozen=True)
class CONV_UST:
    """
        name: tCONV:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 50000000.0
        margin: False
    """
    name: str = "tCONV:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 50000000.0
    margin: bool = False

    def __repr__(self):
        return "tCONV:UST"

    def __str__(self):
        return "tCONV:UST"

    def __call__(self):
        return "tCONV:UST"


CRVF0_USTF0 = CRVF0_USTF0()


@dataclass(slots=True, frozen=True)
class CRVF0_USTF0:
    """
        name: tCRVF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tCRVF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tCRVF0:USTF0"

    def __str__(self):
        return "tCRVF0:USTF0"

    def __call__(self):
        return "tCRVF0:USTF0"


CRVUSD = CRVUSD()


@dataclass(slots=True, frozen=True)
class CRVUSD:
    """
        name: tCRVUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tCRVUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tCRVUSD"

    def __str__(self):
        return "tCRVUSD"

    def __call__(self):
        return "tCRVUSD"


CRVUST = CRVUST()


@dataclass(slots=True, frozen=True)
class CRVUST:
    """
        name: tCRVUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tCRVUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tCRVUST"

    def __str__(self):
        return "tCRVUST"

    def __call__(self):
        return "tCRVUST"


DAIBTC = DAIBTC()


@dataclass(slots=True, frozen=True)
class DAIBTC:
    """
        name: tDAIBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 200000.0
        margin: False
    """
    name: str = "tDAIBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 200000.0
    margin: bool = False

    def __repr__(self):
        return "tDAIBTC"

    def __str__(self):
        return "tDAIBTC"

    def __call__(self):
        return "tDAIBTC"


DAIETH = DAIETH()


@dataclass(slots=True, frozen=True)
class DAIETH:
    """
        name: tDAIETH
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 200000.0
        margin: False
    """
    name: str = "tDAIETH"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 200000.0
    margin: bool = False

    def __repr__(self):
        return "tDAIETH"

    def __str__(self):
        return "tDAIETH"

    def __call__(self):
        return "tDAIETH"


DAIUSD = DAIUSD()


@dataclass(slots=True, frozen=True)
class DAIUSD:
    """
        name: tDAIUSD
        precision: 5
        minimum_margin: 33.0
        initial_margin: 66.0
        minimum_order_size: 2.0
        maximum_order_size: 200000.0
        margin: True
    """
    name: str = "tDAIUSD"
    precision: int = 5
    minimum_margin: float = 33.0
    initial_margin: float = 66.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 200000.0
    margin: bool = True

    def __repr__(self):
        return "tDAIUSD"

    def __str__(self):
        return "tDAIUSD"

    def __call__(self):
        return "tDAIUSD"


DGBUSD = DGBUSD()


@dataclass(slots=True, frozen=True)
class DGBUSD:
    """
        name: tDGBUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 184.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tDGBUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 184.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tDGBUSD"

    def __str__(self):
        return "tDGBUSD"

    def __call__(self):
        return "tDGBUSD"


DOGE_BTC = DOGE_BTC()


@dataclass(slots=True, frozen=True)
class DOGE_BTC:
    """
        name: tDOGE:BTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 26.0
        maximum_order_size: 1500000.0
        margin: True
    """
    name: str = "tDOGE:BTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 26.0
    maximum_order_size: float = 1500000.0
    margin: bool = True

    def __repr__(self):
        return "tDOGE:BTC"

    def __str__(self):
        return "tDOGE:BTC"

    def __call__(self):
        return "tDOGE:BTC"


DOGE_USD = DOGE_USD()


@dataclass(slots=True, frozen=True)
class DOGE_USD:
    """
        name: tDOGE:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 26.0
        maximum_order_size: 1500000.0
        margin: True
    """
    name: str = "tDOGE:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 26.0
    maximum_order_size: float = 1500000.0
    margin: bool = True

    def __repr__(self):
        return "tDOGE:USD"

    def __str__(self):
        return "tDOGE:USD"

    def __call__(self):
        return "tDOGE:USD"


DOGE_UST = DOGE_UST()


@dataclass(slots=True, frozen=True)
class DOGE_UST:
    """
        name: tDOGE:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 26.0
        maximum_order_size: 1500000.0
        margin: True
    """
    name: str = "tDOGE:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 26.0
    maximum_order_size: float = 1500000.0
    margin: bool = True

    def __repr__(self):
        return "tDOGE:UST"

    def __str__(self):
        return "tDOGE:UST"

    def __call__(self):
        return "tDOGE:UST"


DOGEF0_USTF0 = DOGEF0_USTF0()


@dataclass(slots=True, frozen=True)
class DOGEF0_USTF0:
    """
        name: tDOGEF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 26.0
        maximum_order_size: 1500000.0
        margin: True
    """
    name: str = "tDOGEF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 26.0
    maximum_order_size: float = 1500000.0
    margin: bool = True

    def __repr__(self):
        return "tDOGEF0:USTF0"

    def __str__(self):
        return "tDOGEF0:USTF0"

    def __call__(self):
        return "tDOGEF0:USTF0"


DORA_USD = DORA_USD()


@dataclass(slots=True, frozen=True)
class DORA_USD:
    """
        name: tDORA:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.8
        maximum_order_size: 25000.0
        margin: False
    """
    name: str = "tDORA:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.8
    maximum_order_size: float = 25000.0
    margin: bool = False

    def __repr__(self):
        return "tDORA:USD"

    def __str__(self):
        return "tDORA:USD"

    def __call__(self):
        return "tDORA:USD"


DORA_UST = DORA_UST()


@dataclass(slots=True, frozen=True)
class DORA_UST:
    """
        name: tDORA:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.8
        maximum_order_size: 25000.0
        margin: False
    """
    name: str = "tDORA:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.8
    maximum_order_size: float = 25000.0
    margin: bool = False

    def __repr__(self):
        return "tDORA:UST"

    def __str__(self):
        return "tDORA:UST"

    def __call__(self):
        return "tDORA:UST"


DOTBTC = DOTBTC()


@dataclass(slots=True, frozen=True)
class DOTBTC:
    """
        name: tDOTBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tDOTBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tDOTBTC"

    def __str__(self):
        return "tDOTBTC"

    def __call__(self):
        return "tDOTBTC"


DOTF0_BTCF0 = DOTF0_BTCF0()


@dataclass(slots=True, frozen=True)
class DOTF0_BTCF0:
    """
        name: tDOTF0:BTCF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tDOTF0:BTCF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tDOTF0:BTCF0"

    def __str__(self):
        return "tDOTF0:BTCF0"

    def __call__(self):
        return "tDOTF0:BTCF0"


DOTF0_USTF0 = DOTF0_USTF0()


@dataclass(slots=True, frozen=True)
class DOTF0_USTF0:
    """
        name: tDOTF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tDOTF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tDOTF0:USTF0"

    def __str__(self):
        return "tDOTF0:USTF0"

    def __call__(self):
        return "tDOTF0:USTF0"


DOTUSD = DOTUSD()


@dataclass(slots=True, frozen=True)
class DOTUSD:
    """
        name: tDOTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tDOTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tDOTUSD"

    def __str__(self):
        return "tDOTUSD"

    def __call__(self):
        return "tDOTUSD"


DOTUST = DOTUST()


@dataclass(slots=True, frozen=True)
class DOTUST:
    """
        name: tDOTUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tDOTUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tDOTUST"

    def __str__(self):
        return "tDOTUST"

    def __call__(self):
        return "tDOTUST"


DSHBTC = DSHBTC()


@dataclass(slots=True, frozen=True)
class DSHBTC:
    """
        name: tDSHBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.04
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tDSHBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tDSHBTC"

    def __str__(self):
        return "tDSHBTC"

    def __call__(self):
        return "tDSHBTC"


DSHUSD = DSHUSD()


@dataclass(slots=True, frozen=True)
class DSHUSD:
    """
        name: tDSHUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.04
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tDSHUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tDSHUSD"

    def __str__(self):
        return "tDSHUSD"

    def __call__(self):
        return "tDSHUSD"


DUSK_BTC = DUSK_BTC()


@dataclass(slots=True, frozen=True)
class DUSK_BTC:
    """
        name: tDUSK:BTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 18.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tDUSK:BTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 18.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tDUSK:BTC"

    def __str__(self):
        return "tDUSK:BTC"

    def __call__(self):
        return "tDUSK:BTC"


DUSK_USD = DUSK_USD()


@dataclass(slots=True, frozen=True)
class DUSK_USD:
    """
        name: tDUSK:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 18.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tDUSK:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 18.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tDUSK:USD"

    def __str__(self):
        return "tDUSK:USD"

    def __call__(self):
        return "tDUSK:USD"


DVFUSD = DVFUSD()


@dataclass(slots=True, frozen=True)
class DVFUSD:
    """
        name: tDVFUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 1.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tDVFUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 1.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tDVFUSD"

    def __str__(self):
        return "tDVFUSD"

    def __call__(self):
        return "tDVFUSD"


EDOUSD = EDOUSD()


@dataclass(slots=True, frozen=True)
class EDOUSD:
    """
        name: tEDOUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tEDOUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tEDOUSD"

    def __str__(self):
        return "tEDOUSD"

    def __call__(self):
        return "tEDOUSD"


EGLD_USD = EGLD_USD()


@dataclass(slots=True, frozen=True)
class EGLD_USD:
    """
        name: tEGLD:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tEGLD:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tEGLD:USD"

    def __str__(self):
        return "tEGLD:USD"

    def __call__(self):
        return "tEGLD:USD"


EGLD_UST = EGLD_UST()


@dataclass(slots=True, frozen=True)
class EGLD_UST:
    """
        name: tEGLD:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tEGLD:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tEGLD:UST"

    def __str__(self):
        return "tEGLD:UST"

    def __call__(self):
        return "tEGLD:UST"


EGLDF0_USTF0 = EGLDF0_USTF0()


@dataclass(slots=True, frozen=True)
class EGLDF0_USTF0:
    """
        name: tEGLDF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tEGLDF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tEGLDF0:USTF0"

    def __str__(self):
        return "tEGLDF0:USTF0"

    def __call__(self):
        return "tEGLDF0:USTF0"


ENJUSD = ENJUSD()


@dataclass(slots=True, frozen=True)
class ENJUSD:
    """
        name: tENJUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tENJUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tENJUSD"

    def __str__(self):
        return "tENJUSD"

    def __call__(self):
        return "tENJUSD"


EOSBTC = EOSBTC()


@dataclass(slots=True, frozen=True)
class EOSBTC:
    """
        name: tEOSBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tEOSBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tEOSBTC"

    def __str__(self):
        return "tEOSBTC"

    def __call__(self):
        return "tEOSBTC"


EOSETH = EOSETH()


@dataclass(slots=True, frozen=True)
class EOSETH:
    """
        name: tEOSETH
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tEOSETH"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tEOSETH"

    def __str__(self):
        return "tEOSETH"

    def __call__(self):
        return "tEOSETH"


EOSEUR = EOSEUR()


@dataclass(slots=True, frozen=True)
class EOSEUR:
    """
        name: tEOSEUR
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tEOSEUR"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tEOSEUR"

    def __str__(self):
        return "tEOSEUR"

    def __call__(self):
        return "tEOSEUR"


EOSF0_USTF0 = EOSF0_USTF0()


@dataclass(slots=True, frozen=True)
class EOSF0_USTF0:
    """
        name: tEOSF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tEOSF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tEOSF0:USTF0"

    def __str__(self):
        return "tEOSF0:USTF0"

    def __call__(self):
        return "tEOSF0:USTF0"


EOSUSD = EOSUSD()


@dataclass(slots=True, frozen=True)
class EOSUSD:
    """
        name: tEOSUSD
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tEOSUSD"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tEOSUSD"

    def __str__(self):
        return "tEOSUSD"

    def __call__(self):
        return "tEOSUSD"


EOSUST = EOSUST()


@dataclass(slots=True, frozen=True)
class EOSUST:
    """
        name: tEOSUST
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tEOSUST"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tEOSUST"

    def __str__(self):
        return "tEOSUST"

    def __call__(self):
        return "tEOSUST"


ETCBTC = ETCBTC()


@dataclass(slots=True, frozen=True)
class ETCBTC:
    """
        name: tETCBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.1
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tETCBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.1
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tETCBTC"

    def __str__(self):
        return "tETCBTC"

    def __call__(self):
        return "tETCBTC"


ETCF0_USTF0 = ETCF0_USTF0()


@dataclass(slots=True, frozen=True)
class ETCF0_USTF0:
    """
        name: tETCF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.1
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tETCF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.1
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tETCF0:USTF0"

    def __str__(self):
        return "tETCF0:USTF0"

    def __call__(self):
        return "tETCF0:USTF0"


ETCUSD = ETCUSD()


@dataclass(slots=True, frozen=True)
class ETCUSD:
    """
        name: tETCUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.1
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tETCUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.1
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tETCUSD"

    def __str__(self):
        return "tETCUSD"

    def __call__(self):
        return "tETCUSD"


ETCUST = ETCUST()


@dataclass(slots=True, frozen=True)
class ETCUST:
    """
        name: tETCUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.1
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tETCUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.1
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tETCUST"

    def __str__(self):
        return "tETCUST"

    def __call__(self):
        return "tETCUST"


ETH2X_ETH = ETH2X_ETH()


@dataclass(slots=True, frozen=True)
class ETH2X_ETH:
    """
        name: tETH2X:ETH
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 5000.0
        margin: False
    """
    name: str = "tETH2X:ETH"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 5000.0
    margin: bool = False

    def __repr__(self):
        return "tETH2X:ETH"

    def __str__(self):
        return "tETH2X:ETH"

    def __call__(self):
        return "tETH2X:ETH"


ETH2X_USD = ETH2X_USD()


@dataclass(slots=True, frozen=True)
class ETH2X_USD:
    """
        name: tETH2X:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 5000.0
        margin: False
    """
    name: str = "tETH2X:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 5000.0
    margin: bool = False

    def __repr__(self):
        return "tETH2X:USD"

    def __str__(self):
        return "tETH2X:USD"

    def __call__(self):
        return "tETH2X:USD"


ETH2X_UST = ETH2X_UST()


@dataclass(slots=True, frozen=True)
class ETH2X_UST:
    """
        name: tETH2X:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 5000.0
        margin: False
    """
    name: str = "tETH2X:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 5000.0
    margin: bool = False

    def __repr__(self):
        return "tETH2X:UST"

    def __str__(self):
        return "tETH2X:UST"

    def __call__(self):
        return "tETH2X:UST"


ETH_MXNT = ETH_MXNT()


@dataclass(slots=True, frozen=True)
class ETH_MXNT:
    """
        name: tETH:MXNT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 2000.0
        margin: False
    """
    name: str = "tETH:MXNT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 2000.0
    margin: bool = False

    def __repr__(self):
        return "tETH:MXNT"

    def __str__(self):
        return "tETH:MXNT"

    def __call__(self):
        return "tETH:MXNT"


ETH_XAUT = ETH_XAUT()


@dataclass(slots=True, frozen=True)
class ETH_XAUT:
    """
        name: tETH:XAUT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 2500.0
        margin: False
    """
    name: str = "tETH:XAUT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 2500.0
    margin: bool = False

    def __repr__(self):
        return "tETH:XAUT"

    def __str__(self):
        return "tETH:XAUT"

    def __call__(self):
        return "tETH:XAUT"


ETHBTC = ETHBTC()


@dataclass(slots=True, frozen=True)
class ETHBTC:
    """
        name: tETHBTC
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.002
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tETHBTC"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tETHBTC"

    def __str__(self):
        return "tETHBTC"

    def __call__(self):
        return "tETHBTC"


ETHEUR = ETHEUR()


@dataclass(slots=True, frozen=True)
class ETHEUR:
    """
        name: tETHEUR
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tETHEUR"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tETHEUR"

    def __str__(self):
        return "tETHEUR"

    def __call__(self):
        return "tETHEUR"


ETHEUT = ETHEUT()


@dataclass(slots=True, frozen=True)
class ETHEUT:
    """
        name: tETHEUT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tETHEUT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tETHEUT"

    def __str__(self):
        return "tETHEUT"

    def __call__(self):
        return "tETHEUT"


ETHF0_BTCF0 = ETHF0_BTCF0()


@dataclass(slots=True, frozen=True)
class ETHF0_BTCF0:
    """
        name: tETHF0:BTCF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.002
        maximum_order_size: 100.0
        margin: True
    """
    name: str = "tETHF0:BTCF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 100.0
    margin: bool = True

    def __repr__(self):
        return "tETHF0:BTCF0"

    def __str__(self):
        return "tETHF0:BTCF0"

    def __call__(self):
        return "tETHF0:BTCF0"


ETHF0_EUTF0 = ETHF0_EUTF0()


@dataclass(slots=True, frozen=True)
class ETHF0_EUTF0:
    """
        name: tETHF0:EUTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.002
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tETHF0:EUTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tETHF0:EUTF0"

    def __str__(self):
        return "tETHF0:EUTF0"

    def __call__(self):
        return "tETHF0:EUTF0"


ETHF0_USTF0 = ETHF0_USTF0()


@dataclass(slots=True, frozen=True)
class ETHF0_USTF0:
    """
        name: tETHF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.002
        maximum_order_size: 1000.0
        margin: True
    """
    name: str = "tETHF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 1000.0
    margin: bool = True

    def __repr__(self):
        return "tETHF0:USTF0"

    def __str__(self):
        return "tETHF0:USTF0"

    def __call__(self):
        return "tETHF0:USTF0"


ETHGBP = ETHGBP()


@dataclass(slots=True, frozen=True)
class ETHGBP:
    """
        name: tETHGBP
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tETHGBP"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tETHGBP"

    def __str__(self):
        return "tETHGBP"

    def __call__(self):
        return "tETHGBP"


ETHJPY = ETHJPY()


@dataclass(slots=True, frozen=True)
class ETHJPY:
    """
        name: tETHJPY
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tETHJPY"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tETHJPY"

    def __str__(self):
        return "tETHJPY"

    def __call__(self):
        return "tETHJPY"


ETHUSD = ETHUSD()


@dataclass(slots=True, frozen=True)
class ETHUSD:
    """
        name: tETHUSD
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.002
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tETHUSD"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tETHUSD"

    def __str__(self):
        return "tETHUSD"

    def __call__(self):
        return "tETHUSD"


ETHUST = ETHUST()


@dataclass(slots=True, frozen=True)
class ETHUST:
    """
        name: tETHUST
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.002
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tETHUST"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tETHUST"

    def __str__(self):
        return "tETHUST"

    def __call__(self):
        return "tETHUST"


ETHW_USD = ETHW_USD()


@dataclass(slots=True, frozen=True)
class ETHW_USD:
    """
        name: tETHW:USD
        precision: 5
        minimum_margin: 30.0
        initial_margin: 60.0
        minimum_order_size: 0.001
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tETHW:USD"
    precision: int = 5
    minimum_margin: float = 30.0
    initial_margin: float = 60.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tETHW:USD"

    def __str__(self):
        return "tETHW:USD"

    def __call__(self):
        return "tETHW:USD"


ETHW_UST = ETHW_UST()


@dataclass(slots=True, frozen=True)
class ETHW_UST:
    """
        name: tETHW:UST
        precision: 5
        minimum_margin: 30.0
        initial_margin: 60.0
        minimum_order_size: 0.001
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tETHW:UST"
    precision: int = 5
    minimum_margin: float = 30.0
    initial_margin: float = 60.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tETHW:UST"

    def __str__(self):
        return "tETHW:UST"

    def __call__(self):
        return "tETHW:UST"


ETPUSD = ETPUSD()


@dataclass(slots=True, frozen=True)
class ETPUSD:
    """
        name: tETPUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 42.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tETPUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 42.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tETPUSD"

    def __str__(self):
        return "tETPUSD"

    def __call__(self):
        return "tETPUSD"


EURF0_USTF0 = EURF0_USTF0()


@dataclass(slots=True, frozen=True)
class EURF0_USTF0:
    """
        name: tEURF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tEURF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tEURF0:USTF0"

    def __str__(self):
        return "tEURF0:USTF0"

    def __call__(self):
        return "tEURF0:USTF0"


EURUST = EURUST()


@dataclass(slots=True, frozen=True)
class EURUST:
    """
        name: tEURUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tEURUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tEURUST"

    def __str__(self):
        return "tEURUST"

    def __call__(self):
        return "tEURUST"


EUSUSD = EUSUSD()


@dataclass(slots=True, frozen=True)
class EUSUSD:
    """
        name: tEUSUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tEUSUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tEUSUSD"

    def __str__(self):
        return "tEUSUSD"

    def __call__(self):
        return "tEUSUSD"


EUT_MXNT = EUT_MXNT()


@dataclass(slots=True, frozen=True)
class EUT_MXNT:
    """
        name: tEUT:MXNT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 10000000.0
        margin: False
    """
    name: str = "tEUT:MXNT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 10000000.0
    margin: bool = False

    def __repr__(self):
        return "tEUT:MXNT"

    def __str__(self):
        return "tEUT:MXNT"

    def __call__(self):
        return "tEUT:MXNT"


EUTEUR = EUTEUR()


@dataclass(slots=True, frozen=True)
class EUTEUR:
    """
        name: tEUTEUR
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tEUTEUR"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tEUTEUR"

    def __str__(self):
        return "tEUTEUR"

    def __call__(self):
        return "tEUTEUR"


EUTUSD = EUTUSD()


@dataclass(slots=True, frozen=True)
class EUTUSD:
    """
        name: tEUTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tEUTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tEUTUSD"

    def __str__(self):
        return "tEUTUSD"

    def __call__(self):
        return "tEUTUSD"


EUTUST = EUTUST()


@dataclass(slots=True, frozen=True)
class EUTUST:
    """
        name: tEUTUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tEUTUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tEUTUST"

    def __str__(self):
        return "tEUTUST"

    def __call__(self):
        return "tEUTUST"


EXOUSD = EXOUSD()


@dataclass(slots=True, frozen=True)
class EXOUSD:
    """
        name: tEXOUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tEXOUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tEXOUSD"

    def __str__(self):
        return "tEXOUSD"

    def __call__(self):
        return "tEXOUSD"


FBTUSD = FBTUSD()


@dataclass(slots=True, frozen=True)
class FBTUSD:
    """
        name: tFBTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tFBTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tFBTUSD"

    def __str__(self):
        return "tFBTUSD"

    def __call__(self):
        return "tFBTUSD"


FBTUST = FBTUST()


@dataclass(slots=True, frozen=True)
class FBTUST:
    """
        name: tFBTUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tFBTUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tFBTUST"

    def __str__(self):
        return "tFBTUST"

    def __call__(self):
        return "tFBTUST"


FCLUSD = FCLUSD()


@dataclass(slots=True, frozen=True)
class FCLUSD:
    """
        name: tFCLUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 62.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tFCLUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 62.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tFCLUSD"

    def __str__(self):
        return "tFCLUSD"

    def __call__(self):
        return "tFCLUSD"


FCLUST = FCLUST()


@dataclass(slots=True, frozen=True)
class FCLUST:
    """
        name: tFCLUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 62.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tFCLUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 62.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tFCLUST"

    def __str__(self):
        return "tFCLUST"

    def __call__(self):
        return "tFCLUST"


FETUSD = FETUSD()


@dataclass(slots=True, frozen=True)
class FETUSD:
    """
        name: tFETUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 14.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tFETUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 14.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tFETUSD"

    def __str__(self):
        return "tFETUSD"

    def __call__(self):
        return "tFETUSD"


FETUST = FETUST()


@dataclass(slots=True, frozen=True)
class FETUST:
    """
        name: tFETUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 14.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tFETUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 14.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tFETUST"

    def __str__(self):
        return "tFETUST"

    def __call__(self):
        return "tFETUST"


FILF0_USTF0 = FILF0_USTF0()


@dataclass(slots=True, frozen=True)
class FILF0_USTF0:
    """
        name: tFILF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tFILF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tFILF0:USTF0"

    def __str__(self):
        return "tFILF0:USTF0"

    def __call__(self):
        return "tFILF0:USTF0"


FILUSD = FILUSD()


@dataclass(slots=True, frozen=True)
class FILUSD:
    """
        name: tFILUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tFILUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tFILUSD"

    def __str__(self):
        return "tFILUSD"

    def __call__(self):
        return "tFILUSD"


FILUST = FILUST()


@dataclass(slots=True, frozen=True)
class FILUST:
    """
        name: tFILUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tFILUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tFILUST"

    def __str__(self):
        return "tFILUST"

    def __call__(self):
        return "tFILUST"


FLRUSD = FLRUSD()


@dataclass(slots=True, frozen=True)
class FLRUSD:
    """
        name: tFLRUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tFLRUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tFLRUSD"

    def __str__(self):
        return "tFLRUSD"

    def __call__(self):
        return "tFLRUSD"


FLRUST = FLRUST()


@dataclass(slots=True, frozen=True)
class FLRUST:
    """
        name: tFLRUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tFLRUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tFLRUST"

    def __str__(self):
        return "tFLRUST"

    def __call__(self):
        return "tFLRUST"


FORTH_USD = FORTH_USD()


@dataclass(slots=True, frozen=True)
class FORTH_USD:
    """
        name: tFORTH:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tFORTH:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tFORTH:USD"

    def __str__(self):
        return "tFORTH:USD"

    def __call__(self):
        return "tFORTH:USD"


FORTH_UST = FORTH_UST()


@dataclass(slots=True, frozen=True)
class FORTH_UST:
    """
        name: tFORTH:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tFORTH:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tFORTH:UST"

    def __str__(self):
        return "tFORTH:UST"

    def __call__(self):
        return "tFORTH:UST"


FTMF0_USTF0 = FTMF0_USTF0()


@dataclass(slots=True, frozen=True)
class FTMF0_USTF0:
    """
        name: tFTMF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 6.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tFTMF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tFTMF0:USTF0"

    def __str__(self):
        return "tFTMF0:USTF0"

    def __call__(self):
        return "tFTMF0:USTF0"


FTMUSD = FTMUSD()


@dataclass(slots=True, frozen=True)
class FTMUSD:
    """
        name: tFTMUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tFTMUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tFTMUSD"

    def __str__(self):
        return "tFTMUSD"

    def __call__(self):
        return "tFTMUSD"


FTMUST = FTMUST()


@dataclass(slots=True, frozen=True)
class FTMUST:
    """
        name: tFTMUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tFTMUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tFTMUST"

    def __str__(self):
        return "tFTMUST"

    def __call__(self):
        return "tFTMUST"


FUNUSD = FUNUSD()


@dataclass(slots=True, frozen=True)
class FUNUSD:
    """
        name: tFUNUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 226.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tFUNUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 226.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tFUNUSD"

    def __str__(self):
        return "tFUNUSD"

    def __call__(self):
        return "tFUNUSD"


GALA_USD = GALA_USD()


@dataclass(slots=True, frozen=True)
class GALA_USD:
    """
        name: tGALA:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 26.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tGALA:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 26.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tGALA:USD"

    def __str__(self):
        return "tGALA:USD"

    def __call__(self):
        return "tGALA:USD"


GALA_UST = GALA_UST()


@dataclass(slots=True, frozen=True)
class GALA_UST:
    """
        name: tGALA:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 26.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tGALA:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 26.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tGALA:UST"

    def __str__(self):
        return "tGALA:UST"

    def __call__(self):
        return "tGALA:UST"


GALAF0_USTF0 = GALAF0_USTF0()


@dataclass(slots=True, frozen=True)
class GALAF0_USTF0:
    """
        name: tGALAF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 26.0
        maximum_order_size: 500000.0
        margin: True
    """
    name: str = "tGALAF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 26.0
    maximum_order_size: float = 500000.0
    margin: bool = True

    def __repr__(self):
        return "tGALAF0:USTF0"

    def __str__(self):
        return "tGALAF0:USTF0"

    def __call__(self):
        return "tGALAF0:USTF0"


GBPEUT = GBPEUT()


@dataclass(slots=True, frozen=True)
class GBPEUT:
    """
        name: tGBPEUT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tGBPEUT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tGBPEUT"

    def __str__(self):
        return "tGBPEUT"

    def __call__(self):
        return "tGBPEUT"


GBPF0_USTF0 = GBPF0_USTF0()


@dataclass(slots=True, frozen=True)
class GBPF0_USTF0:
    """
        name: tGBPF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tGBPF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tGBPF0:USTF0"

    def __str__(self):
        return "tGBPF0:USTF0"

    def __call__(self):
        return "tGBPF0:USTF0"


GBPUST = GBPUST()


@dataclass(slots=True, frozen=True)
class GBPUST:
    """
        name: tGBPUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tGBPUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tGBPUST"

    def __str__(self):
        return "tGBPUST"

    def __call__(self):
        return "tGBPUST"


GNOUSD = GNOUSD()


@dataclass(slots=True, frozen=True)
class GNOUSD:
    """
        name: tGNOUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 1000.0
        margin: False
    """
    name: str = "tGNOUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 1000.0
    margin: bool = False

    def __repr__(self):
        return "tGNOUSD"

    def __str__(self):
        return "tGNOUSD"

    def __call__(self):
        return "tGNOUSD"


GNTUSD = GNTUSD()


@dataclass(slots=True, frozen=True)
class GNTUSD:
    """
        name: tGNTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tGNTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tGNTUSD"

    def __str__(self):
        return "tGNTUSD"

    def __call__(self):
        return "tGNTUSD"


GRTUSD = GRTUSD()


@dataclass(slots=True, frozen=True)
class GRTUSD:
    """
        name: tGRTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 14.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tGRTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 14.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tGRTUSD"

    def __str__(self):
        return "tGRTUSD"

    def __call__(self):
        return "tGRTUSD"


GRTUST = GRTUST()


@dataclass(slots=True, frozen=True)
class GRTUST:
    """
        name: tGRTUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 14.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tGRTUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 14.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tGRTUST"

    def __str__(self):
        return "tGRTUST"

    def __call__(self):
        return "tGRTUST"


GTXUSD = GTXUSD()


@dataclass(slots=True, frozen=True)
class GTXUSD:
    """
        name: tGTXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tGTXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tGTXUSD"

    def __str__(self):
        return "tGTXUSD"

    def __call__(self):
        return "tGTXUSD"


GTXUST = GTXUST()


@dataclass(slots=True, frozen=True)
class GTXUST:
    """
        name: tGTXUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tGTXUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tGTXUST"

    def __str__(self):
        return "tGTXUST"

    def __call__(self):
        return "tGTXUST"


GXTUSD = GXTUSD()


@dataclass(slots=True, frozen=True)
class GXTUSD:
    """
        name: tGXTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tGXTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tGXTUSD"

    def __str__(self):
        return "tGXTUSD"

    def __call__(self):
        return "tGXTUSD"


GXTUST = GXTUST()


@dataclass(slots=True, frozen=True)
class GXTUST:
    """
        name: tGXTUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tGXTUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tGXTUST"

    def __str__(self):
        return "tGXTUST"

    def __call__(self):
        return "tGXTUST"


HECUSD = HECUSD()


@dataclass(slots=True, frozen=True)
class HECUSD:
    """
        name: tHECUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tHECUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tHECUSD"

    def __str__(self):
        return "tHECUSD"

    def __call__(self):
        return "tHECUSD"


HECUST = HECUST()


@dataclass(slots=True, frozen=True)
class HECUST:
    """
        name: tHECUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tHECUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tHECUST"

    def __str__(self):
        return "tHECUST"

    def __call__(self):
        return "tHECUST"


HIXUSD = HIXUSD()


@dataclass(slots=True, frozen=True)
class HIXUSD:
    """
        name: tHIXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 18.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tHIXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 18.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tHIXUSD"

    def __str__(self):
        return "tHIXUSD"

    def __call__(self):
        return "tHIXUSD"


HIXUST = HIXUST()


@dataclass(slots=True, frozen=True)
class HIXUST:
    """
        name: tHIXUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 18.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tHIXUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 18.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tHIXUST"

    def __str__(self):
        return "tHIXUST"

    def __call__(self):
        return "tHIXUST"


HMTUSD = HMTUSD()


@dataclass(slots=True, frozen=True)
class HMTUSD:
    """
        name: tHMTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tHMTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tHMTUSD"

    def __str__(self):
        return "tHMTUSD"

    def __call__(self):
        return "tHMTUSD"


HMTUST = HMTUST()


@dataclass(slots=True, frozen=True)
class HMTUST:
    """
        name: tHMTUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tHMTUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tHMTUST"

    def __str__(self):
        return "tHMTUST"

    def __call__(self):
        return "tHMTUST"


HTXUSD = HTXUSD()


@dataclass(slots=True, frozen=True)
class HTXUSD:
    """
        name: tHTXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tHTXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tHTXUSD"

    def __str__(self):
        return "tHTXUSD"

    def __call__(self):
        return "tHTXUSD"


HTXUST = HTXUST()


@dataclass(slots=True, frozen=True)
class HTXUST:
    """
        name: tHTXUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tHTXUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tHTXUST"

    def __str__(self):
        return "tHTXUST"

    def __call__(self):
        return "tHTXUST"


ICEUSD = ICEUSD()


@dataclass(slots=True, frozen=True)
class ICEUSD:
    """
        name: tICEUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 25000.0
        margin: False
    """
    name: str = "tICEUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 25000.0
    margin: bool = False

    def __repr__(self):
        return "tICEUSD"

    def __str__(self):
        return "tICEUSD"

    def __call__(self):
        return "tICEUSD"


ICPBTC = ICPBTC()


@dataclass(slots=True, frozen=True)
class ICPBTC:
    """
        name: tICPBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tICPBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tICPBTC"

    def __str__(self):
        return "tICPBTC"

    def __call__(self):
        return "tICPBTC"


ICPF0_USTF0 = ICPF0_USTF0()


@dataclass(slots=True, frozen=True)
class ICPF0_USTF0:
    """
        name: tICPF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tICPF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tICPF0:USTF0"

    def __str__(self):
        return "tICPF0:USTF0"

    def __call__(self):
        return "tICPF0:USTF0"


ICPUSD = ICPUSD()


@dataclass(slots=True, frozen=True)
class ICPUSD:
    """
        name: tICPUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tICPUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tICPUSD"

    def __str__(self):
        return "tICPUSD"

    def __call__(self):
        return "tICPUSD"


ICPUST = ICPUST()


@dataclass(slots=True, frozen=True)
class ICPUST:
    """
        name: tICPUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tICPUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tICPUST"

    def __str__(self):
        return "tICPUST"

    def __call__(self):
        return "tICPUST"


IDXUSD = IDXUSD()


@dataclass(slots=True, frozen=True)
class IDXUSD:
    """
        name: tIDXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 20.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tIDXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 20.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tIDXUSD"

    def __str__(self):
        return "tIDXUSD"

    def __call__(self):
        return "tIDXUSD"


IDXUST = IDXUST()


@dataclass(slots=True, frozen=True)
class IDXUST:
    """
        name: tIDXUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 20.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tIDXUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 20.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tIDXUST"

    def __str__(self):
        return "tIDXUST"

    def __call__(self):
        return "tIDXUST"


IOTBTC = IOTBTC()


@dataclass(slots=True, frozen=True)
class IOTBTC:
    """
        name: tIOTBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tIOTBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tIOTBTC"

    def __str__(self):
        return "tIOTBTC"

    def __call__(self):
        return "tIOTBTC"


IOTETH = IOTETH()


@dataclass(slots=True, frozen=True)
class IOTETH:
    """
        name: tIOTETH
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tIOTETH"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tIOTETH"

    def __str__(self):
        return "tIOTETH"

    def __call__(self):
        return "tIOTETH"


IOTF0_USTF0 = IOTF0_USTF0()


@dataclass(slots=True, frozen=True)
class IOTF0_USTF0:
    """
        name: tIOTF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 6.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tIOTF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tIOTF0:USTF0"

    def __str__(self):
        return "tIOTF0:USTF0"

    def __call__(self):
        return "tIOTF0:USTF0"


IOTUSD = IOTUSD()


@dataclass(slots=True, frozen=True)
class IOTUSD:
    """
        name: tIOTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tIOTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tIOTUSD"

    def __str__(self):
        return "tIOTUSD"

    def __call__(self):
        return "tIOTUSD"


IQXUSD = IQXUSD()


@dataclass(slots=True, frozen=True)
class IQXUSD:
    """
        name: tIQXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 334.0
        maximum_order_size: 100000000.0
        margin: False
    """
    name: str = "tIQXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 334.0
    maximum_order_size: float = 100000000.0
    margin: bool = False

    def __repr__(self):
        return "tIQXUSD"

    def __str__(self):
        return "tIQXUSD"

    def __call__(self):
        return "tIQXUSD"


JASMY_USD = JASMY_USD()


@dataclass(slots=True, frozen=True)
class JASMY_USD:
    """
        name: tJASMY:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 168.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tJASMY:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 168.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tJASMY:USD"

    def __str__(self):
        return "tJASMY:USD"

    def __call__(self):
        return "tJASMY:USD"


JASMY_UST = JASMY_UST()


@dataclass(slots=True, frozen=True)
class JASMY_UST:
    """
        name: tJASMY:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 168.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tJASMY:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 168.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tJASMY:UST"

    def __str__(self):
        return "tJASMY:UST"

    def __call__(self):
        return "tJASMY:UST"


JASMYF0_USTF0 = JASMYF0_USTF0()


@dataclass(slots=True, frozen=True)
class JASMYF0_USTF0:
    """
        name: tJASMYF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 168.0
        maximum_order_size: 2500000.0
        margin: True
    """
    name: str = "tJASMYF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 168.0
    maximum_order_size: float = 2500000.0
    margin: bool = True

    def __repr__(self):
        return "tJASMYF0:USTF0"

    def __str__(self):
        return "tJASMYF0:USTF0"

    def __call__(self):
        return "tJASMYF0:USTF0"


JPYF0_USTF0 = JPYF0_USTF0()


@dataclass(slots=True, frozen=True)
class JPYF0_USTF0:
    """
        name: tJPYF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 262.0
        maximum_order_size: 100000000.0
        margin: True
    """
    name: str = "tJPYF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 262.0
    maximum_order_size: float = 100000000.0
    margin: bool = True

    def __repr__(self):
        return "tJPYF0:USTF0"

    def __str__(self):
        return "tJPYF0:USTF0"

    def __call__(self):
        return "tJPYF0:USTF0"


JPYUST = JPYUST()


@dataclass(slots=True, frozen=True)
class JPYUST:
    """
        name: tJPYUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 262.0
        maximum_order_size: 100000000.0
        margin: False
    """
    name: str = "tJPYUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 262.0
    maximum_order_size: float = 100000000.0
    margin: bool = False

    def __repr__(self):
        return "tJPYUST"

    def __str__(self):
        return "tJPYUST"

    def __call__(self):
        return "tJPYUST"


JSTBTC = JSTBTC()


@dataclass(slots=True, frozen=True)
class JSTBTC:
    """
        name: tJSTBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 48.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tJSTBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 48.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tJSTBTC"

    def __str__(self):
        return "tJSTBTC"

    def __call__(self):
        return "tJSTBTC"


JSTUSD = JSTUSD()


@dataclass(slots=True, frozen=True)
class JSTUSD:
    """
        name: tJSTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 48.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tJSTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 48.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tJSTUSD"

    def __str__(self):
        return "tJSTUSD"

    def __call__(self):
        return "tJSTUSD"


JSTUST = JSTUST()


@dataclass(slots=True, frozen=True)
class JSTUST:
    """
        name: tJSTUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 48.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tJSTUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 48.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tJSTUST"

    def __str__(self):
        return "tJSTUST"

    def __call__(self):
        return "tJSTUST"


KAIUSD = KAIUSD()


@dataclass(slots=True, frozen=True)
class KAIUSD:
    """
        name: tKAIUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 132.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tKAIUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 132.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tKAIUSD"

    def __str__(self):
        return "tKAIUSD"

    def __call__(self):
        return "tKAIUSD"


KAIUST = KAIUST()


@dataclass(slots=True, frozen=True)
class KAIUST:
    """
        name: tKAIUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 132.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tKAIUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 132.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tKAIUST"

    def __str__(self):
        return "tKAIUST"

    def __call__(self):
        return "tKAIUST"


KANUSD = KANUSD()


@dataclass(slots=True, frozen=True)
class KANUSD:
    """
        name: tKANUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 1542.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tKANUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 1542.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tKANUSD"

    def __str__(self):
        return "tKANUSD"

    def __call__(self):
        return "tKANUSD"


KANUST = KANUST()


@dataclass(slots=True, frozen=True)
class KANUST:
    """
        name: tKANUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 1542.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tKANUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 1542.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tKANUST"

    def __str__(self):
        return "tKANUST"

    def __call__(self):
        return "tKANUST"


KNCBTC = KNCBTC()


@dataclass(slots=True, frozen=True)
class KNCBTC:
    """
        name: tKNCBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 20000.0
        margin: False
    """
    name: str = "tKNCBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 20000.0
    margin: bool = False

    def __repr__(self):
        return "tKNCBTC"

    def __str__(self):
        return "tKNCBTC"

    def __call__(self):
        return "tKNCBTC"


KNCF0_USTF0 = KNCF0_USTF0()


@dataclass(slots=True, frozen=True)
class KNCF0_USTF0:
    """
        name: tKNCF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tKNCF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tKNCF0:USTF0"

    def __str__(self):
        return "tKNCF0:USTF0"

    def __call__(self):
        return "tKNCF0:USTF0"


KNCUSD = KNCUSD()


@dataclass(slots=True, frozen=True)
class KNCUSD:
    """
        name: tKNCUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tKNCUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tKNCUSD"

    def __str__(self):
        return "tKNCUSD"

    def __call__(self):
        return "tKNCUSD"


KSMUSD = KSMUSD()


@dataclass(slots=True, frozen=True)
class KSMUSD:
    """
        name: tKSMUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: False
    """
    name: str = "tKSMUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = False

    def __repr__(self):
        return "tKSMUSD"

    def __str__(self):
        return "tKSMUSD"

    def __call__(self):
        return "tKSMUSD"


KSMUST = KSMUST()


@dataclass(slots=True, frozen=True)
class KSMUST:
    """
        name: tKSMUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: False
    """
    name: str = "tKSMUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = False

    def __repr__(self):
        return "tKSMUST"

    def __str__(self):
        return "tKSMUST"

    def __call__(self):
        return "tKSMUST"


LEOBTC = LEOBTC()


@dataclass(slots=True, frozen=True)
class LEOBTC:
    """
        name: tLEOBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tLEOBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tLEOBTC"

    def __str__(self):
        return "tLEOBTC"

    def __call__(self):
        return "tLEOBTC"


LEOETH = LEOETH()


@dataclass(slots=True, frozen=True)
class LEOETH:
    """
        name: tLEOETH
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tLEOETH"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tLEOETH"

    def __str__(self):
        return "tLEOETH"

    def __call__(self):
        return "tLEOETH"


LEOUSD = LEOUSD()


@dataclass(slots=True, frozen=True)
class LEOUSD:
    """
        name: tLEOUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tLEOUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tLEOUSD"

    def __str__(self):
        return "tLEOUSD"

    def __call__(self):
        return "tLEOUSD"


LEOUST = LEOUST()


@dataclass(slots=True, frozen=True)
class LEOUST:
    """
        name: tLEOUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tLEOUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tLEOUST"

    def __str__(self):
        return "tLEOUST"

    def __call__(self):
        return "tLEOUST"


LINK_USD = LINK_USD()


@dataclass(slots=True, frozen=True)
class LINK_USD:
    """
        name: tLINK:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tLINK:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tLINK:USD"

    def __str__(self):
        return "tLINK:USD"

    def __call__(self):
        return "tLINK:USD"


LINK_UST = LINK_UST()


@dataclass(slots=True, frozen=True)
class LINK_UST:
    """
        name: tLINK:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tLINK:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tLINK:UST"

    def __str__(self):
        return "tLINK:UST"

    def __call__(self):
        return "tLINK:UST"


LINKF0_USTF0 = LINKF0_USTF0()


@dataclass(slots=True, frozen=True)
class LINKF0_USTF0:
    """
        name: tLINKF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.2
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tLINKF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tLINKF0:USTF0"

    def __str__(self):
        return "tLINKF0:USTF0"

    def __call__(self):
        return "tLINKF0:USTF0"


LRCUSD = LRCUSD()


@dataclass(slots=True, frozen=True)
class LRCUSD:
    """
        name: tLRCUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tLRCUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tLRCUSD"

    def __str__(self):
        return "tLRCUSD"

    def __call__(self):
        return "tLRCUSD"


LTCBTC = LTCBTC()


@dataclass(slots=True, frozen=True)
class LTCBTC:
    """
        name: tLTCBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.04
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tLTCBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tLTCBTC"

    def __str__(self):
        return "tLTCBTC"

    def __call__(self):
        return "tLTCBTC"


LTCF0_BTCF0 = LTCF0_BTCF0()


@dataclass(slots=True, frozen=True)
class LTCF0_BTCF0:
    """
        name: tLTCF0:BTCF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.04
        maximum_order_size: 7500.0
        margin: True
    """
    name: str = "tLTCF0:BTCF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 7500.0
    margin: bool = True

    def __repr__(self):
        return "tLTCF0:BTCF0"

    def __str__(self):
        return "tLTCF0:BTCF0"

    def __call__(self):
        return "tLTCF0:BTCF0"


LTCF0_USTF0 = LTCF0_USTF0()


@dataclass(slots=True, frozen=True)
class LTCF0_USTF0:
    """
        name: tLTCF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.04
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tLTCF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tLTCF0:USTF0"

    def __str__(self):
        return "tLTCF0:USTF0"

    def __call__(self):
        return "tLTCF0:USTF0"


LTCUSD = LTCUSD()


@dataclass(slots=True, frozen=True)
class LTCUSD:
    """
        name: tLTCUSD
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.04
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tLTCUSD"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tLTCUSD"

    def __str__(self):
        return "tLTCUSD"

    def __call__(self):
        return "tLTCUSD"


LTCUST = LTCUST()


@dataclass(slots=True, frozen=True)
class LTCUST:
    """
        name: tLTCUST
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.04
        maximum_order_size: 2000.0
        margin: True
    """
    name: str = "tLTCUST"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.04
    maximum_order_size: float = 2000.0
    margin: bool = True

    def __repr__(self):
        return "tLTCUST"

    def __str__(self):
        return "tLTCUST"

    def __call__(self):
        return "tLTCUST"


LUNA2_USD = LUNA2_USD()


@dataclass(slots=True, frozen=True)
class LUNA2_USD:
    """
        name: tLUNA2:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tLUNA2:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tLUNA2:USD"

    def __str__(self):
        return "tLUNA2:USD"

    def __call__(self):
        return "tLUNA2:USD"


LUNA2_UST = LUNA2_UST()


@dataclass(slots=True, frozen=True)
class LUNA2_UST:
    """
        name: tLUNA2:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tLUNA2:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tLUNA2:UST"

    def __str__(self):
        return "tLUNA2:UST"

    def __call__(self):
        return "tLUNA2:UST"


LUNA_USD = LUNA_USD()


@dataclass(slots=True, frozen=True)
class LUNA_USD:
    """
        name: tLUNA:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 20814.0
        maximum_order_size: 100000000000.0
        margin: False
    """
    name: str = "tLUNA:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 20814.0
    maximum_order_size: float = 100000000000.0
    margin: bool = False

    def __repr__(self):
        return "tLUNA:USD"

    def __str__(self):
        return "tLUNA:USD"

    def __call__(self):
        return "tLUNA:USD"


LUNA_UST = LUNA_UST()


@dataclass(slots=True, frozen=True)
class LUNA_UST:
    """
        name: tLUNA:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 20814.0
        maximum_order_size: 100000000000.0
        margin: False
    """
    name: str = "tLUNA:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 20814.0
    maximum_order_size: float = 100000000000.0
    margin: bool = False

    def __repr__(self):
        return "tLUNA:UST"

    def __str__(self):
        return "tLUNA:UST"

    def __call__(self):
        return "tLUNA:UST"


LUXO_USD = LUXO_USD()


@dataclass(slots=True, frozen=True)
class LUXO_USD:
    """
        name: tLUXO:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 20.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tLUXO:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 20.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tLUXO:USD"

    def __str__(self):
        return "tLUXO:USD"

    def __call__(self):
        return "tLUXO:USD"


LYMUSD = LYMUSD()


@dataclass(slots=True, frozen=True)
class LYMUSD:
    """
        name: tLYMUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 740.0
        maximum_order_size: 400000.0
        margin: False
    """
    name: str = "tLYMUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 740.0
    maximum_order_size: float = 400000.0
    margin: bool = False

    def __repr__(self):
        return "tLYMUSD"

    def __str__(self):
        return "tLYMUSD"

    def __call__(self):
        return "tLYMUSD"


MATIC_BTC = MATIC_BTC()


@dataclass(slots=True, frozen=True)
class MATIC_BTC:
    """
        name: tMATIC:BTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tMATIC:BTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tMATIC:BTC"

    def __str__(self):
        return "tMATIC:BTC"

    def __call__(self):
        return "tMATIC:BTC"


MATIC_USD = MATIC_USD()


@dataclass(slots=True, frozen=True)
class MATIC_USD:
    """
        name: tMATIC:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tMATIC:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tMATIC:USD"

    def __str__(self):
        return "tMATIC:USD"

    def __call__(self):
        return "tMATIC:USD"


MATIC_UST = MATIC_UST()


@dataclass(slots=True, frozen=True)
class MATIC_UST:
    """
        name: tMATIC:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tMATIC:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tMATIC:UST"

    def __str__(self):
        return "tMATIC:UST"

    def __call__(self):
        return "tMATIC:UST"


MATICF0_USTF0 = MATICF0_USTF0()


@dataclass(slots=True, frozen=True)
class MATICF0_USTF0:
    """
        name: tMATICF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 4.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tMATICF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tMATICF0:USTF0"

    def __str__(self):
        return "tMATICF0:USTF0"

    def __call__(self):
        return "tMATICF0:USTF0"


MIMUSD = MIMUSD()


@dataclass(slots=True, frozen=True)
class MIMUSD:
    """
        name: tMIMUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tMIMUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tMIMUSD"

    def __str__(self):
        return "tMIMUSD"

    def __call__(self):
        return "tMIMUSD"


MIMUST = MIMUST()


@dataclass(slots=True, frozen=True)
class MIMUST:
    """
        name: tMIMUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tMIMUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tMIMUST"

    def __str__(self):
        return "tMIMUST"

    def __call__(self):
        return "tMIMUST"


MIRUSD = MIRUSD()


@dataclass(slots=True, frozen=True)
class MIRUSD:
    """
        name: tMIRUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tMIRUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tMIRUSD"

    def __str__(self):
        return "tMIRUSD"

    def __call__(self):
        return "tMIRUSD"


MKRF0_USTF0 = MKRF0_USTF0()


@dataclass(slots=True, frozen=True)
class MKRF0_USTF0:
    """
        name: tMKRF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.002
        maximum_order_size: 2500.0
        margin: True
    """
    name: str = "tMKRF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 2500.0
    margin: bool = True

    def __repr__(self):
        return "tMKRF0:USTF0"

    def __str__(self):
        return "tMKRF0:USTF0"

    def __call__(self):
        return "tMKRF0:USTF0"


MKRUSD = MKRUSD()


@dataclass(slots=True, frozen=True)
class MKRUSD:
    """
        name: tMKRUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 2500.0
        margin: True
    """
    name: str = "tMKRUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 2500.0
    margin: bool = True

    def __repr__(self):
        return "tMKRUSD"

    def __str__(self):
        return "tMKRUSD"

    def __call__(self):
        return "tMKRUSD"


MKRUST = MKRUST()


@dataclass(slots=True, frozen=True)
class MKRUST:
    """
        name: tMKRUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.002
        maximum_order_size: 2500.0
        margin: False
    """
    name: str = "tMKRUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 2500.0
    margin: bool = False

    def __repr__(self):
        return "tMKRUST"

    def __str__(self):
        return "tMKRUST"

    def __call__(self):
        return "tMKRUST"


MLNUSD = MLNUSD()


@dataclass(slots=True, frozen=True)
class MLNUSD:
    """
        name: tMLNUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.08
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tMLNUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.08
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tMLNUSD"

    def __str__(self):
        return "tMLNUSD"

    def __call__(self):
        return "tMLNUSD"


MNABTC = MNABTC()


@dataclass(slots=True, frozen=True)
class MNABTC:
    """
        name: tMNABTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 200000.0
        margin: False
    """
    name: str = "tMNABTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 200000.0
    margin: bool = False

    def __repr__(self):
        return "tMNABTC"

    def __str__(self):
        return "tMNABTC"

    def __call__(self):
        return "tMNABTC"


MNAUSD = MNAUSD()


@dataclass(slots=True, frozen=True)
class MNAUSD:
    """
        name: tMNAUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 200000.0
        margin: False
    """
    name: str = "tMNAUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 200000.0
    margin: bool = False

    def __repr__(self):
        return "tMNAUSD"

    def __str__(self):
        return "tMNAUSD"

    def __call__(self):
        return "tMNAUSD"


MOBUSD = MOBUSD()


@dataclass(slots=True, frozen=True)
class MOBUSD:
    """
        name: tMOBUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tMOBUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tMOBUSD"

    def __str__(self):
        return "tMOBUSD"

    def __call__(self):
        return "tMOBUSD"


MOBUST = MOBUST()


@dataclass(slots=True, frozen=True)
class MOBUST:
    """
        name: tMOBUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tMOBUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tMOBUST"

    def __str__(self):
        return "tMOBUST"

    def __call__(self):
        return "tMOBUST"


MXNT_USD = MXNT_USD()


@dataclass(slots=True, frozen=True)
class MXNT_USD:
    """
        name: tMXNT:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 10000000.0
        margin: False
    """
    name: str = "tMXNT:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 10000000.0
    margin: bool = False

    def __repr__(self):
        return "tMXNT:USD"

    def __str__(self):
        return "tMXNT:USD"

    def __call__(self):
        return "tMXNT:USD"


NEAR_USD = NEAR_USD()


@dataclass(slots=True, frozen=True)
class NEAR_USD:
    """
        name: tNEAR:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 25000.0
        margin: False
    """
    name: str = "tNEAR:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 25000.0
    margin: bool = False

    def __repr__(self):
        return "tNEAR:USD"

    def __str__(self):
        return "tNEAR:USD"

    def __call__(self):
        return "tNEAR:USD"


NEAR_UST = NEAR_UST()


@dataclass(slots=True, frozen=True)
class NEAR_UST:
    """
        name: tNEAR:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 25000.0
        margin: False
    """
    name: str = "tNEAR:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 25000.0
    margin: bool = False

    def __repr__(self):
        return "tNEAR:UST"

    def __str__(self):
        return "tNEAR:UST"

    def __call__(self):
        return "tNEAR:UST"


NEARF0_USTF0 = NEARF0_USTF0()


@dataclass(slots=True, frozen=True)
class NEARF0_USTF0:
    """
        name: tNEARF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.4
        maximum_order_size: 25000.0
        margin: True
    """
    name: str = "tNEARF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 25000.0
    margin: bool = True

    def __repr__(self):
        return "tNEARF0:USTF0"

    def __str__(self):
        return "tNEARF0:USTF0"

    def __call__(self):
        return "tNEARF0:USTF0"


NEOBTC = NEOBTC()


@dataclass(slots=True, frozen=True)
class NEOBTC:
    """
        name: tNEOBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tNEOBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tNEOBTC"

    def __str__(self):
        return "tNEOBTC"

    def __call__(self):
        return "tNEOBTC"


NEOF0_USTF0 = NEOF0_USTF0()


@dataclass(slots=True, frozen=True)
class NEOF0_USTF0:
    """
        name: tNEOF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tNEOF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tNEOF0:USTF0"

    def __str__(self):
        return "tNEOF0:USTF0"

    def __call__(self):
        return "tNEOF0:USTF0"


NEOUSD = NEOUSD()


@dataclass(slots=True, frozen=True)
class NEOUSD:
    """
        name: tNEOUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tNEOUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tNEOUSD"

    def __str__(self):
        return "tNEOUSD"

    def __call__(self):
        return "tNEOUSD"


NEOUST = NEOUST()


@dataclass(slots=True, frozen=True)
class NEOUST:
    """
        name: tNEOUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tNEOUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tNEOUST"

    def __str__(self):
        return "tNEOUST"

    def __call__(self):
        return "tNEOUST"


NEXO_BTC = NEXO_BTC()


@dataclass(slots=True, frozen=True)
class NEXO_BTC:
    """
        name: tNEXO:BTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tNEXO:BTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tNEXO:BTC"

    def __str__(self):
        return "tNEXO:BTC"

    def __call__(self):
        return "tNEXO:BTC"


NEXO_USD = NEXO_USD()


@dataclass(slots=True, frozen=True)
class NEXO_USD:
    """
        name: tNEXO:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tNEXO:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tNEXO:USD"

    def __str__(self):
        return "tNEXO:USD"

    def __call__(self):
        return "tNEXO:USD"


NEXO_UST = NEXO_UST()


@dataclass(slots=True, frozen=True)
class NEXO_UST:
    """
        name: tNEXO:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tNEXO:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tNEXO:UST"

    def __str__(self):
        return "tNEXO:UST"

    def __call__(self):
        return "tNEXO:UST"


OCEAN_USD = OCEAN_USD()


@dataclass(slots=True, frozen=True)
class OCEAN_USD:
    """
        name: tOCEAN:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 10.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tOCEAN:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 10.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tOCEAN:USD"

    def __str__(self):
        return "tOCEAN:USD"

    def __call__(self):
        return "tOCEAN:USD"


OCEAN_UST = OCEAN_UST()


@dataclass(slots=True, frozen=True)
class OCEAN_UST:
    """
        name: tOCEAN:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 10.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tOCEAN:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 10.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tOCEAN:UST"

    def __str__(self):
        return "tOCEAN:UST"

    def __call__(self):
        return "tOCEAN:UST"


OMGBTC = OMGBTC()


@dataclass(slots=True, frozen=True)
class OMGBTC:
    """
        name: tOMGBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.8
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tOMGBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.8
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tOMGBTC"

    def __str__(self):
        return "tOMGBTC"

    def __call__(self):
        return "tOMGBTC"


OMGETH = OMGETH()


@dataclass(slots=True, frozen=True)
class OMGETH:
    """
        name: tOMGETH
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.8
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tOMGETH"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.8
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tOMGETH"

    def __str__(self):
        return "tOMGETH"

    def __call__(self):
        return "tOMGETH"


OMGF0_USTF0 = OMGF0_USTF0()


@dataclass(slots=True, frozen=True)
class OMGF0_USTF0:
    """
        name: tOMGF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.8
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tOMGF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.8
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tOMGF0:USTF0"

    def __str__(self):
        return "tOMGF0:USTF0"

    def __call__(self):
        return "tOMGF0:USTF0"


OMGUSD = OMGUSD()


@dataclass(slots=True, frozen=True)
class OMGUSD:
    """
        name: tOMGUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.8
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tOMGUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.8
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tOMGUSD"

    def __str__(self):
        return "tOMGUSD"

    def __call__(self):
        return "tOMGUSD"


OMNUSD = OMNUSD()


@dataclass(slots=True, frozen=True)
class OMNUSD:
    """
        name: tOMNUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 20000.0
        margin: False
    """
    name: str = "tOMNUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 20000.0
    margin: bool = False

    def __repr__(self):
        return "tOMNUSD"

    def __str__(self):
        return "tOMNUSD"

    def __call__(self):
        return "tOMNUSD"


ONEUSD = ONEUSD()


@dataclass(slots=True, frozen=True)
class ONEUSD:
    """
        name: tONEUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 3500000.0
        margin: False
    """
    name: str = "tONEUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 3500000.0
    margin: bool = False

    def __repr__(self):
        return "tONEUSD"

    def __str__(self):
        return "tONEUSD"

    def __call__(self):
        return "tONEUSD"


ONEUST = ONEUST()


@dataclass(slots=True, frozen=True)
class ONEUST:
    """
        name: tONEUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 3500000.0
        margin: False
    """
    name: str = "tONEUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 3500000.0
    margin: bool = False

    def __repr__(self):
        return "tONEUST"

    def __str__(self):
        return "tONEUST"

    def __call__(self):
        return "tONEUST"


OXYUSD = OXYUSD()


@dataclass(slots=True, frozen=True)
class OXYUSD:
    """
        name: tOXYUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 22.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tOXYUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 22.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tOXYUSD"

    def __str__(self):
        return "tOXYUSD"

    def __call__(self):
        return "tOXYUSD"


PASUSD = PASUSD()


@dataclass(slots=True, frozen=True)
class PASUSD:
    """
        name: tPASUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 1588.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tPASUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 1588.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tPASUSD"

    def __str__(self):
        return "tPASUSD"

    def __call__(self):
        return "tPASUSD"


PAXUSD = PAXUSD()


@dataclass(slots=True, frozen=True)
class PAXUSD:
    """
        name: tPAXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tPAXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tPAXUSD"

    def __str__(self):
        return "tPAXUSD"

    def __call__(self):
        return "tPAXUSD"


PAXUST = PAXUST()


@dataclass(slots=True, frozen=True)
class PAXUST:
    """
        name: tPAXUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tPAXUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tPAXUST"

    def __str__(self):
        return "tPAXUST"

    def __call__(self):
        return "tPAXUST"


PLANETS_USD = PLANETS_USD()


@dataclass(slots=True, frozen=True)
class PLANETS_USD:
    """
        name: tPLANETS:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 124.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tPLANETS:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 124.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tPLANETS:USD"

    def __str__(self):
        return "tPLANETS:USD"

    def __call__(self):
        return "tPLANETS:USD"


PLANETS_UST = PLANETS_UST()


@dataclass(slots=True, frozen=True)
class PLANETS_UST:
    """
        name: tPLANETS:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 124.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tPLANETS:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 124.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tPLANETS:UST"

    def __str__(self):
        return "tPLANETS:UST"

    def __call__(self):
        return "tPLANETS:UST"


PLUUSD = PLUUSD()


@dataclass(slots=True, frozen=True)
class PLUUSD:
    """
        name: tPLUUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 10000.0
        margin: False
    """
    name: str = "tPLUUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 10000.0
    margin: bool = False

    def __repr__(self):
        return "tPLUUSD"

    def __str__(self):
        return "tPLUUSD"

    def __call__(self):
        return "tPLUUSD"


PNKUSD = PNKUSD()


@dataclass(slots=True, frozen=True)
class PNKUSD:
    """
        name: tPNKUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 52.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tPNKUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 52.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tPNKUSD"

    def __str__(self):
        return "tPNKUSD"

    def __call__(self):
        return "tPNKUSD"


POLC_USD = POLC_USD()


@dataclass(slots=True, frozen=True)
class POLC_USD:
    """
        name: tPOLC:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 26.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tPOLC:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 26.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tPOLC:USD"

    def __str__(self):
        return "tPOLC:USD"

    def __call__(self):
        return "tPOLC:USD"


POLC_UST = POLC_UST()


@dataclass(slots=True, frozen=True)
class POLC_UST:
    """
        name: tPOLC:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 26.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tPOLC:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 26.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tPOLC:UST"

    def __str__(self):
        return "tPOLC:UST"

    def __call__(self):
        return "tPOLC:UST"


POLIS_USD = POLIS_USD()


@dataclass(slots=True, frozen=True)
class POLIS_USD:
    """
        name: tPOLIS:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tPOLIS:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tPOLIS:USD"

    def __str__(self):
        return "tPOLIS:USD"

    def __call__(self):
        return "tPOLIS:USD"


POLIS_UST = POLIS_UST()


@dataclass(slots=True, frozen=True)
class POLIS_UST:
    """
        name: tPOLIS:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tPOLIS:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tPOLIS:UST"

    def __str__(self):
        return "tPOLIS:UST"

    def __call__(self):
        return "tPOLIS:UST"


QRDO_USD = QRDO_USD()


@dataclass(slots=True, frozen=True)
class QRDO_USD:
    """
        name: tQRDO:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tQRDO:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tQRDO:USD"

    def __str__(self):
        return "tQRDO:USD"

    def __call__(self):
        return "tQRDO:USD"


QRDO_UST = QRDO_UST()


@dataclass(slots=True, frozen=True)
class QRDO_UST:
    """
        name: tQRDO:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tQRDO:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tQRDO:UST"

    def __str__(self):
        return "tQRDO:UST"

    def __call__(self):
        return "tQRDO:UST"


QTFBTC = QTFBTC()


@dataclass(slots=True, frozen=True)
class QTFBTC:
    """
        name: tQTFBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tQTFBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tQTFBTC"

    def __str__(self):
        return "tQTFBTC"

    def __call__(self):
        return "tQTFBTC"


QTFUSD = QTFUSD()


@dataclass(slots=True, frozen=True)
class QTFUSD:
    """
        name: tQTFUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tQTFUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tQTFUSD"

    def __str__(self):
        return "tQTFUSD"

    def __call__(self):
        return "tQTFUSD"


QTMUSD = QTMUSD()


@dataclass(slots=True, frozen=True)
class QTMUSD:
    """
        name: tQTMUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.6
        maximum_order_size: 5000.0
        margin: False
    """
    name: str = "tQTMUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.6
    maximum_order_size: float = 5000.0
    margin: bool = False

    def __repr__(self):
        return "tQTMUSD"

    def __str__(self):
        return "tQTMUSD"

    def __call__(self):
        return "tQTMUSD"


RBTBTC = RBTBTC()


@dataclass(slots=True, frozen=True)
class RBTBTC:
    """
        name: tRBTBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00006
        maximum_order_size: 500.0
        margin: False
    """
    name: str = "tRBTBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 500.0
    margin: bool = False

    def __repr__(self):
        return "tRBTBTC"

    def __str__(self):
        return "tRBTBTC"

    def __call__(self):
        return "tRBTBTC"


RBTUSD = RBTUSD()


@dataclass(slots=True, frozen=True)
class RBTUSD:
    """
        name: tRBTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00006
        maximum_order_size: 500.0
        margin: False
    """
    name: str = "tRBTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 500.0
    margin: bool = False

    def __repr__(self):
        return "tRBTUSD"

    def __str__(self):
        return "tRBTUSD"

    def __call__(self):
        return "tRBTUSD"


REEF_USD = REEF_USD()


@dataclass(slots=True, frozen=True)
class REEF_USD:
    """
        name: tREEF:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 466.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tREEF:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 466.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tREEF:USD"

    def __str__(self):
        return "tREEF:USD"

    def __call__(self):
        return "tREEF:USD"


REEF_UST = REEF_UST()


@dataclass(slots=True, frozen=True)
class REEF_UST:
    """
        name: tREEF:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 466.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tREEF:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 466.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tREEF:UST"

    def __str__(self):
        return "tREEF:UST"

    def __call__(self):
        return "tREEF:UST"


REPUSD = REPUSD()


@dataclass(slots=True, frozen=True)
class REPUSD:
    """
        name: tREPUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 1000.0
        margin: False
    """
    name: str = "tREPUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 1000.0
    margin: bool = False

    def __repr__(self):
        return "tREPUSD"

    def __str__(self):
        return "tREPUSD"

    def __call__(self):
        return "tREPUSD"


REQUSD = REQUSD()


@dataclass(slots=True, frozen=True)
class REQUSD:
    """
        name: tREQUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 16.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tREQUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 16.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tREQUSD"

    def __str__(self):
        return "tREQUSD"

    def __call__(self):
        return "tREQUSD"


RLYUSD = RLYUSD()


@dataclass(slots=True, frozen=True)
class RLYUSD:
    """
        name: tRLYUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tRLYUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tRLYUSD"

    def __str__(self):
        return "tRLYUSD"

    def __call__(self):
        return "tRLYUSD"


RLYUST = RLYUST()


@dataclass(slots=True, frozen=True)
class RLYUST:
    """
        name: tRLYUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tRLYUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tRLYUST"

    def __str__(self):
        return "tRLYUST"

    def __call__(self):
        return "tRLYUST"


ROSE_USD = ROSE_USD()


@dataclass(slots=True, frozen=True)
class ROSE_USD:
    """
        name: tROSE:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 32.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tROSE:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 32.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tROSE:USD"

    def __str__(self):
        return "tROSE:USD"

    def __call__(self):
        return "tROSE:USD"


RRTUSD = RRTUSD()


@dataclass(slots=True, frozen=True)
class RRTUSD:
    """
        name: tRRTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 100000.0
        margin: False
    """
    name: str = "tRRTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 100000.0
    margin: bool = False

    def __repr__(self):
        return "tRRTUSD"

    def __str__(self):
        return "tRRTUSD"

    def __call__(self):
        return "tRRTUSD"


SAND_USD = SAND_USD()


@dataclass(slots=True, frozen=True)
class SAND_USD:
    """
        name: tSAND:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tSAND:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tSAND:USD"

    def __str__(self):
        return "tSAND:USD"

    def __call__(self):
        return "tSAND:USD"


SAND_UST = SAND_UST()


@dataclass(slots=True, frozen=True)
class SAND_UST:
    """
        name: tSAND:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tSAND:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tSAND:UST"

    def __str__(self):
        return "tSAND:UST"

    def __call__(self):
        return "tSAND:UST"


SANDF0_USTF0 = SANDF0_USTF0()


@dataclass(slots=True, frozen=True)
class SANDF0_USTF0:
    """
        name: tSANDF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 2.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tSANDF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tSANDF0:USTF0"

    def __str__(self):
        return "tSANDF0:USTF0"

    def __call__(self):
        return "tSANDF0:USTF0"


SENATE_USD = SENATE_USD()


@dataclass(slots=True, frozen=True)
class SENATE_USD:
    """
        name: tSENATE:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 20.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tSENATE:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 20.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tSENATE:USD"

    def __str__(self):
        return "tSENATE:USD"

    def __call__(self):
        return "tSENATE:USD"


SENATE_UST = SENATE_UST()


@dataclass(slots=True, frozen=True)
class SENATE_UST:
    """
        name: tSENATE:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 20.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tSENATE:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 20.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tSENATE:UST"

    def __str__(self):
        return "tSENATE:UST"

    def __call__(self):
        return "tSENATE:UST"


SGBUSD = SGBUSD()


@dataclass(slots=True, frozen=True)
class SGBUSD:
    """
        name: tSGBUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 52.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tSGBUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 52.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tSGBUSD"

    def __str__(self):
        return "tSGBUSD"

    def __call__(self):
        return "tSGBUSD"


SGBUST = SGBUST()


@dataclass(slots=True, frozen=True)
class SGBUST:
    """
        name: tSGBUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 52.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tSGBUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 52.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tSGBUST"

    def __str__(self):
        return "tSGBUST"

    def __call__(self):
        return "tSGBUST"


SHFT_USD = SHFT_USD()


@dataclass(slots=True, frozen=True)
class SHFT_USD:
    """
        name: tSHFT:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 52.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tSHFT:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 52.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tSHFT:USD"

    def __str__(self):
        return "tSHFT:USD"

    def __call__(self):
        return "tSHFT:USD"


SHFT_UST = SHFT_UST()


@dataclass(slots=True, frozen=True)
class SHFT_UST:
    """
        name: tSHFT:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 52.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tSHFT:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 52.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tSHFT:UST"

    def __str__(self):
        return "tSHFT:UST"

    def __call__(self):
        return "tSHFT:UST"


SHIB_USD = SHIB_USD()


@dataclass(slots=True, frozen=True)
class SHIB_USD:
    """
        name: tSHIB:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 187004.0
        maximum_order_size: 5000000000.0
        margin: True
    """
    name: str = "tSHIB:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 187004.0
    maximum_order_size: float = 5000000000.0
    margin: bool = True

    def __repr__(self):
        return "tSHIB:USD"

    def __str__(self):
        return "tSHIB:USD"

    def __call__(self):
        return "tSHIB:USD"


SHIB_UST = SHIB_UST()


@dataclass(slots=True, frozen=True)
class SHIB_UST:
    """
        name: tSHIB:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 187004.0
        maximum_order_size: 5000000000.0
        margin: True
    """
    name: str = "tSHIB:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 187004.0
    maximum_order_size: float = 5000000000.0
    margin: bool = True

    def __repr__(self):
        return "tSHIB:UST"

    def __str__(self):
        return "tSHIB:UST"

    def __call__(self):
        return "tSHIB:UST"


SHIBF0_USTF0 = SHIBF0_USTF0()


@dataclass(slots=True, frozen=True)
class SHIBF0_USTF0:
    """
        name: tSHIBF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 187004.0
        maximum_order_size: 5000000000.0
        margin: True
    """
    name: str = "tSHIBF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 187004.0
    maximum_order_size: float = 5000000000.0
    margin: bool = True

    def __repr__(self):
        return "tSHIBF0:USTF0"

    def __str__(self):
        return "tSHIBF0:USTF0"

    def __call__(self):
        return "tSHIBF0:USTF0"


SIDUS_USD = SIDUS_USD()


@dataclass(slots=True, frozen=True)
class SIDUS_USD:
    """
        name: tSIDUS:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 664.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tSIDUS:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 664.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tSIDUS:USD"

    def __str__(self):
        return "tSIDUS:USD"

    def __call__(self):
        return "tSIDUS:USD"


SMRUSD = SMRUSD()


@dataclass(slots=True, frozen=True)
class SMRUSD:
    """
        name: tSMRUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 700000.0
        margin: False
    """
    name: str = "tSMRUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 700000.0
    margin: bool = False

    def __repr__(self):
        return "tSMRUSD"

    def __str__(self):
        return "tSMRUSD"

    def __call__(self):
        return "tSMRUSD"


SMRUST = SMRUST()


@dataclass(slots=True, frozen=True)
class SMRUST:
    """
        name: tSMRUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 700000.0
        margin: False
    """
    name: str = "tSMRUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 700000.0
    margin: bool = False

    def __repr__(self):
        return "tSMRUST"

    def __str__(self):
        return "tSMRUST"

    def __call__(self):
        return "tSMRUST"


SNTUSD = SNTUSD()


@dataclass(slots=True, frozen=True)
class SNTUSD:
    """
        name: tSNTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 48.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tSNTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 48.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tSNTUSD"

    def __str__(self):
        return "tSNTUSD"

    def __call__(self):
        return "tSNTUSD"


SNXUSD = SNXUSD()


@dataclass(slots=True, frozen=True)
class SNXUSD:
    """
        name: tSNXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.8
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tSNXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.8
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tSNXUSD"

    def __str__(self):
        return "tSNXUSD"

    def __call__(self):
        return "tSNXUSD"


SNXUST = SNXUST()


@dataclass(slots=True, frozen=True)
class SNXUST:
    """
        name: tSNXUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.8
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tSNXUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.8
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tSNXUST"

    def __str__(self):
        return "tSNXUST"

    def __call__(self):
        return "tSNXUST"


SOLBTC = SOLBTC()


@dataclass(slots=True, frozen=True)
class SOLBTC:
    """
        name: tSOLBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.06
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tSOLBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.06
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tSOLBTC"

    def __str__(self):
        return "tSOLBTC"

    def __call__(self):
        return "tSOLBTC"


SOLF0_BTCF0 = SOLF0_BTCF0()


@dataclass(slots=True, frozen=True)
class SOLF0_BTCF0:
    """
        name: tSOLF0:BTCF0
        precision: 5
        minimum_margin: 2.5
        initial_margin: 5.0
        minimum_order_size: 0.06
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tSOLF0:BTCF0"
    precision: int = 5
    minimum_margin: float = 2.5
    initial_margin: float = 5.0
    minimum_order_size: float = 0.06
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tSOLF0:BTCF0"

    def __str__(self):
        return "tSOLF0:BTCF0"

    def __call__(self):
        return "tSOLF0:BTCF0"


SOLF0_USTF0 = SOLF0_USTF0()


@dataclass(slots=True, frozen=True)
class SOLF0_USTF0:
    """
        name: tSOLF0:USTF0
        precision: 5
        minimum_margin: 2.5
        initial_margin: 5.0
        minimum_order_size: 0.06
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tSOLF0:USTF0"
    precision: int = 5
    minimum_margin: float = 2.5
    initial_margin: float = 5.0
    minimum_order_size: float = 0.06
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tSOLF0:USTF0"

    def __str__(self):
        return "tSOLF0:USTF0"

    def __call__(self):
        return "tSOLF0:USTF0"


SOLUSD = SOLUSD()


@dataclass(slots=True, frozen=True)
class SOLUSD:
    """
        name: tSOLUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.06
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tSOLUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.06
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tSOLUSD"

    def __str__(self):
        return "tSOLUSD"

    def __call__(self):
        return "tSOLUSD"


SOLUST = SOLUST()


@dataclass(slots=True, frozen=True)
class SOLUST:
    """
        name: tSOLUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.06
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tSOLUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.06
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tSOLUST"

    def __str__(self):
        return "tSOLUST"

    def __call__(self):
        return "tSOLUST"


SPELL_USD = SPELL_USD()


@dataclass(slots=True, frozen=True)
class SPELL_USD:
    """
        name: tSPELL:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 1640.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tSPELL:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 1640.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tSPELL:USD"

    def __str__(self):
        return "tSPELL:USD"

    def __call__(self):
        return "tSPELL:USD"


SPELL_UST = SPELL_UST()


@dataclass(slots=True, frozen=True)
class SPELL_UST:
    """
        name: tSPELL:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 1640.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tSPELL:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 1640.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tSPELL:UST"

    def __str__(self):
        return "tSPELL:UST"

    def __call__(self):
        return "tSPELL:UST"


STGF0_USTF0 = STGF0_USTF0()


@dataclass(slots=True, frozen=True)
class STGF0_USTF0:
    """
        name: tSTGF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 4.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tSTGF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tSTGF0:USTF0"

    def __str__(self):
        return "tSTGF0:USTF0"

    def __call__(self):
        return "tSTGF0:USTF0"


STGUSD = STGUSD()


@dataclass(slots=True, frozen=True)
class STGUSD:
    """
        name: tSTGUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tSTGUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tSTGUSD"

    def __str__(self):
        return "tSTGUSD"

    def __call__(self):
        return "tSTGUSD"


STGUST = STGUST()


@dataclass(slots=True, frozen=True)
class STGUST:
    """
        name: tSTGUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tSTGUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tSTGUST"

    def __str__(self):
        return "tSTGUST"

    def __call__(self):
        return "tSTGUST"


STJUSD = STJUSD()


@dataclass(slots=True, frozen=True)
class STJUSD:
    """
        name: tSTJUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 30000.0
        margin: False
    """
    name: str = "tSTJUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 30000.0
    margin: bool = False

    def __repr__(self):
        return "tSTJUSD"

    def __str__(self):
        return "tSTJUSD"

    def __call__(self):
        return "tSTJUSD"


SUKU_USD = SUKU_USD()


@dataclass(slots=True, frozen=True)
class SUKU_USD:
    """
        name: tSUKU:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 18.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tSUKU:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 18.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tSUKU:USD"

    def __str__(self):
        return "tSUKU:USD"

    def __call__(self):
        return "tSUKU:USD"


SUKU_UST = SUKU_UST()


@dataclass(slots=True, frozen=True)
class SUKU_UST:
    """
        name: tSUKU:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 18.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tSUKU:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 18.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tSUKU:UST"

    def __str__(self):
        return "tSUKU:UST"

    def __call__(self):
        return "tSUKU:UST"


SUNUSD = SUNUSD()


@dataclass(slots=True, frozen=True)
class SUNUSD:
    """
        name: tSUNUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 216.0
        maximum_order_size: 10000000.0
        margin: False
    """
    name: str = "tSUNUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 216.0
    maximum_order_size: float = 10000000.0
    margin: bool = False

    def __repr__(self):
        return "tSUNUSD"

    def __str__(self):
        return "tSUNUSD"

    def __call__(self):
        return "tSUNUSD"


SUNUST = SUNUST()


@dataclass(slots=True, frozen=True)
class SUNUST:
    """
        name: tSUNUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 216.0
        maximum_order_size: 10000000.0
        margin: False
    """
    name: str = "tSUNUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 216.0
    maximum_order_size: float = 10000000.0
    margin: bool = False

    def __repr__(self):
        return "tSUNUST"

    def __str__(self):
        return "tSUNUST"

    def __call__(self):
        return "tSUNUST"


SUSHI_USD = SUSHI_USD()


@dataclass(slots=True, frozen=True)
class SUSHI_USD:
    """
        name: tSUSHI:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tSUSHI:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tSUSHI:USD"

    def __str__(self):
        return "tSUSHI:USD"

    def __call__(self):
        return "tSUSHI:USD"


SUSHI_UST = SUSHI_UST()


@dataclass(slots=True, frozen=True)
class SUSHI_UST:
    """
        name: tSUSHI:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tSUSHI:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tSUSHI:UST"

    def __str__(self):
        return "tSUSHI:UST"

    def __call__(self):
        return "tSUSHI:UST"


SUSHIF0_USTF0 = SUSHIF0_USTF0()


@dataclass(slots=True, frozen=True)
class SUSHIF0_USTF0:
    """
        name: tSUSHIF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 2.0
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tSUSHIF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tSUSHIF0:USTF0"

    def __str__(self):
        return "tSUSHIF0:USTF0"

    def __call__(self):
        return "tSUSHIF0:USTF0"


SWEAT_USD = SWEAT_USD()


@dataclass(slots=True, frozen=True)
class SWEAT_USD:
    """
        name: tSWEAT:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 7000000.0
        margin: False
    """
    name: str = "tSWEAT:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 7000000.0
    margin: bool = False

    def __repr__(self):
        return "tSWEAT:USD"

    def __str__(self):
        return "tSWEAT:USD"

    def __call__(self):
        return "tSWEAT:USD"


SWEAT_UST = SWEAT_UST()


@dataclass(slots=True, frozen=True)
class SWEAT_UST:
    """
        name: tSWEAT:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 7000000.0
        margin: False
    """
    name: str = "tSWEAT:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 7000000.0
    margin: bool = False

    def __repr__(self):
        return "tSWEAT:UST"

    def __str__(self):
        return "tSWEAT:UST"

    def __call__(self):
        return "tSWEAT:UST"


SXXUSD = SXXUSD()


@dataclass(slots=True, frozen=True)
class SXXUSD:
    """
        name: tSXXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tSXXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tSXXUSD"

    def __str__(self):
        return "tSXXUSD"

    def __call__(self):
        return "tSXXUSD"


SXXUST = SXXUST()


@dataclass(slots=True, frozen=True)
class SXXUST:
    """
        name: tSXXUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tSXXUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tSXXUST"

    def __str__(self):
        return "tSXXUST"

    def __call__(self):
        return "tSXXUST"


TERRAUST_USD = TERRAUST_USD()


@dataclass(slots=True, frozen=True)
class TERRAUST_USD:
    """
        name: tTERRAUST:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 100.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tTERRAUST:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 100.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tTERRAUST:USD"

    def __str__(self):
        return "tTERRAUST:USD"

    def __call__(self):
        return "tTERRAUST:USD"


TESTBTC_TESTUSD = TESTBTC_TESTUSD()


@dataclass(slots=True, frozen=True)
class TESTBTC_TESTUSD:
    """
        name: tTESTBTC:TESTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00006
        maximum_order_size: 100.0
        margin: True
    """
    name: str = "tTESTBTC:TESTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 100.0
    margin: bool = True

    def __repr__(self):
        return "tTESTBTC:TESTUSD"

    def __str__(self):
        return "tTESTBTC:TESTUSD"

    def __call__(self):
        return "tTESTBTC:TESTUSD"


TESTBTC_TESTUSDT = TESTBTC_TESTUSDT()


@dataclass(slots=True, frozen=True)
class TESTBTC_TESTUSDT:
    """
        name: tTESTBTC:TESTUSDT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00006
        maximum_order_size: 100.0
        margin: True
    """
    name: str = "tTESTBTC:TESTUSDT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 100.0
    margin: bool = True

    def __repr__(self):
        return "tTESTBTC:TESTUSDT"

    def __str__(self):
        return "tTESTBTC:TESTUSDT"

    def __call__(self):
        return "tTESTBTC:TESTUSDT"


TESTBTCF0_TESTUSDTF0 = TESTBTCF0_TESTUSDTF0()


@dataclass(slots=True, frozen=True)
class TESTBTCF0_TESTUSDTF0:
    """
        name: tTESTBTCF0:TESTUSDTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.00006
        maximum_order_size: 1000.0
        margin: True
    """
    name: str = "tTESTBTCF0:TESTUSDTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 1000.0
    margin: bool = True

    def __repr__(self):
        return "tTESTBTCF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTBTCF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTBTCF0:TESTUSDTF0"


THETA_USD = THETA_USD()


@dataclass(slots=True, frozen=True)
class THETA_USD:
    """
        name: tTHETA:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tTHETA:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tTHETA:USD"

    def __str__(self):
        return "tTHETA:USD"

    def __call__(self):
        return "tTHETA:USD"


THETA_UST = THETA_UST()


@dataclass(slots=True, frozen=True)
class THETA_UST:
    """
        name: tTHETA:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tTHETA:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tTHETA:UST"

    def __str__(self):
        return "tTHETA:UST"

    def __call__(self):
        return "tTHETA:UST"


TLOS_USD = TLOS_USD()


@dataclass(slots=True, frozen=True)
class TLOS_USD:
    """
        name: tTLOS:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 8.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tTLOS:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 8.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tTLOS:USD"

    def __str__(self):
        return "tTLOS:USD"

    def __call__(self):
        return "tTLOS:USD"


TRADE_USD = TRADE_USD()


@dataclass(slots=True, frozen=True)
class TRADE_USD:
    """
        name: tTRADE:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 28.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tTRADE:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 28.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tTRADE:USD"

    def __str__(self):
        return "tTRADE:USD"

    def __call__(self):
        return "tTRADE:USD"


TRADE_UST = TRADE_UST()


@dataclass(slots=True, frozen=True)
class TRADE_UST:
    """
        name: tTRADE:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 28.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tTRADE:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 28.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tTRADE:UST"

    def __str__(self):
        return "tTRADE:UST"

    def __call__(self):
        return "tTRADE:UST"


TREEB_USD = TREEB_USD()


@dataclass(slots=True, frozen=True)
class TREEB_USD:
    """
        name: tTREEB:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 3000000.0
        margin: False
    """
    name: str = "tTREEB:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 3000000.0
    margin: bool = False

    def __repr__(self):
        return "tTREEB:USD"

    def __str__(self):
        return "tTREEB:USD"

    def __call__(self):
        return "tTREEB:USD"


TREEB_UST = TREEB_UST()


@dataclass(slots=True, frozen=True)
class TREEB_UST:
    """
        name: tTREEB:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 3000000.0
        margin: False
    """
    name: str = "tTREEB:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 3000000.0
    margin: bool = False

    def __repr__(self):
        return "tTREEB:UST"

    def __str__(self):
        return "tTREEB:UST"

    def __call__(self):
        return "tTREEB:UST"


TRXBTC = TRXBTC()


@dataclass(slots=True, frozen=True)
class TRXBTC:
    """
        name: tTRXBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 34.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tTRXBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 34.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tTRXBTC"

    def __str__(self):
        return "tTRXBTC"

    def __call__(self):
        return "tTRXBTC"


TRXETH = TRXETH()


@dataclass(slots=True, frozen=True)
class TRXETH:
    """
        name: tTRXETH
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 34.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tTRXETH"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 34.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tTRXETH"

    def __str__(self):
        return "tTRXETH"

    def __call__(self):
        return "tTRXETH"


TRXEUR = TRXEUR()


@dataclass(slots=True, frozen=True)
class TRXEUR:
    """
        name: tTRXEUR
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 34.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tTRXEUR"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 34.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tTRXEUR"

    def __str__(self):
        return "tTRXEUR"

    def __call__(self):
        return "tTRXEUR"


TRXF0_USTF0 = TRXF0_USTF0()


@dataclass(slots=True, frozen=True)
class TRXF0_USTF0:
    """
        name: tTRXF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 24.0
        maximum_order_size: 1000000.0
        margin: True
    """
    name: str = "tTRXF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 24.0
    maximum_order_size: float = 1000000.0
    margin: bool = True

    def __repr__(self):
        return "tTRXF0:USTF0"

    def __str__(self):
        return "tTRXF0:USTF0"

    def __call__(self):
        return "tTRXF0:USTF0"


TRXUSD = TRXUSD()


@dataclass(slots=True, frozen=True)
class TRXUSD:
    """
        name: tTRXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 34.0
        maximum_order_size: 1000000.0
        margin: True
    """
    name: str = "tTRXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 34.0
    maximum_order_size: float = 1000000.0
    margin: bool = True

    def __repr__(self):
        return "tTRXUSD"

    def __str__(self):
        return "tTRXUSD"

    def __call__(self):
        return "tTRXUSD"


TRXUST = TRXUST()


@dataclass(slots=True, frozen=True)
class TRXUST:
    """
        name: tTRXUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 24.0
        maximum_order_size: 1000000.0
        margin: True
    """
    name: str = "tTRXUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 24.0
    maximum_order_size: float = 1000000.0
    margin: bool = True

    def __repr__(self):
        return "tTRXUST"

    def __str__(self):
        return "tTRXUST"

    def __call__(self):
        return "tTRXUST"


TRYUST = TRYUST()


@dataclass(slots=True, frozen=True)
class TRYUST:
    """
        name: tTRYUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tTRYUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tTRYUST"

    def __str__(self):
        return "tTRYUST"

    def __call__(self):
        return "tTRYUST"


TSDUSD = TSDUSD()


@dataclass(slots=True, frozen=True)
class TSDUSD:
    """
        name: tTSDUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tTSDUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tTSDUSD"

    def __str__(self):
        return "tTSDUSD"

    def __call__(self):
        return "tTSDUSD"


TSDUST = TSDUST()


@dataclass(slots=True, frozen=True)
class TSDUST:
    """
        name: tTSDUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tTSDUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tTSDUST"

    def __str__(self):
        return "tTSDUST"

    def __call__(self):
        return "tTSDUST"


UDCUSD = UDCUSD()


@dataclass(slots=True, frozen=True)
class UDCUSD:
    """
        name: tUDCUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tUDCUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tUDCUSD"

    def __str__(self):
        return "tUDCUSD"

    def __call__(self):
        return "tUDCUSD"


UDCUST = UDCUST()


@dataclass(slots=True, frozen=True)
class UDCUST:
    """
        name: tUDCUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tUDCUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tUDCUST"

    def __str__(self):
        return "tUDCUST"

    def __call__(self):
        return "tUDCUST"


UNIF0_USTF0 = UNIF0_USTF0()


@dataclass(slots=True, frozen=True)
class UNIF0_USTF0:
    """
        name: tUNIF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.4
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tUNIF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tUNIF0:USTF0"

    def __str__(self):
        return "tUNIF0:USTF0"

    def __call__(self):
        return "tUNIF0:USTF0"


UNIUSD = UNIUSD()


@dataclass(slots=True, frozen=True)
class UNIUSD:
    """
        name: tUNIUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tUNIUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tUNIUSD"

    def __str__(self):
        return "tUNIUSD"

    def __call__(self):
        return "tUNIUSD"


UNIUST = UNIUST()


@dataclass(slots=True, frozen=True)
class UNIUST:
    """
        name: tUNIUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.4
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tUNIUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.4
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tUNIUST"

    def __str__(self):
        return "tUNIUST"

    def __call__(self):
        return "tUNIUST"


UOSBTC = UOSBTC()


@dataclass(slots=True, frozen=True)
class UOSBTC:
    """
        name: tUOSBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 400000.0
        margin: False
    """
    name: str = "tUOSBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 400000.0
    margin: bool = False

    def __repr__(self):
        return "tUOSBTC"

    def __str__(self):
        return "tUOSBTC"

    def __call__(self):
        return "tUOSBTC"


UOSUSD = UOSUSD()


@dataclass(slots=True, frozen=True)
class UOSUSD:
    """
        name: tUOSUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 4.0
        maximum_order_size: 400000.0
        margin: False
    """
    name: str = "tUOSUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 4.0
    maximum_order_size: float = 400000.0
    margin: bool = False

    def __repr__(self):
        return "tUOSUSD"

    def __str__(self):
        return "tUOSUSD"

    def __call__(self):
        return "tUOSUSD"


UST_CNHT = UST_CNHT()


@dataclass(slots=True, frozen=True)
class UST_CNHT:
    """
        name: tUST:CNHT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tUST:CNHT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tUST:CNHT"

    def __str__(self):
        return "tUST:CNHT"

    def __call__(self):
        return "tUST:CNHT"


UST_MXNT = UST_MXNT()


@dataclass(slots=True, frozen=True)
class UST_MXNT:
    """
        name: tUST:MXNT
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 10000000.0
        margin: False
    """
    name: str = "tUST:MXNT"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 10000000.0
    margin: bool = False

    def __repr__(self):
        return "tUST:MXNT"

    def __str__(self):
        return "tUST:MXNT"

    def __call__(self):
        return "tUST:MXNT"


USTUSD = USTUSD()


@dataclass(slots=True, frozen=True)
class USTUSD:
    """
        name: tUSTUSD
        precision: 5
        minimum_margin: 5.0
        initial_margin: 10.0
        minimum_order_size: 2.0
        maximum_order_size: 5000000.0
        margin: True
    """
    name: str = "tUSTUSD"
    precision: int = 5
    minimum_margin: float = 5.0
    initial_margin: float = 10.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 5000000.0
    margin: bool = True

    def __repr__(self):
        return "tUSTUSD"

    def __str__(self):
        return "tUSTUSD"

    def __call__(self):
        return "tUSTUSD"


UTKUSD = UTKUSD()


@dataclass(slots=True, frozen=True)
class UTKUSD:
    """
        name: tUTKUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 10.0
        maximum_order_size: 300000.0
        margin: False
    """
    name: str = "tUTKUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 10.0
    maximum_order_size: float = 300000.0
    margin: bool = False

    def __repr__(self):
        return "tUTKUSD"

    def __str__(self):
        return "tUTKUSD"

    def __call__(self):
        return "tUTKUSD"


VEEUSD = VEEUSD()


@dataclass(slots=True, frozen=True)
class VEEUSD:
    """
        name: tVEEUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 1258.0
        maximum_order_size: 15000000.0
        margin: False
    """
    name: str = "tVEEUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 1258.0
    maximum_order_size: float = 15000000.0
    margin: bool = False

    def __repr__(self):
        return "tVEEUSD"

    def __str__(self):
        return "tVEEUSD"

    def __call__(self):
        return "tVEEUSD"


VELO_USD = VELO_USD()


@dataclass(slots=True, frozen=True)
class VELO_USD:
    """
        name: tVELO:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 66.0
        maximum_order_size: 75000.0
        margin: False
    """
    name: str = "tVELO:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 66.0
    maximum_order_size: float = 75000.0
    margin: bool = False

    def __repr__(self):
        return "tVELO:USD"

    def __str__(self):
        return "tVELO:USD"

    def __call__(self):
        return "tVELO:USD"


VELO_UST = VELO_UST()


@dataclass(slots=True, frozen=True)
class VELO_UST:
    """
        name: tVELO:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 66.0
        maximum_order_size: 75000.0
        margin: False
    """
    name: str = "tVELO:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 66.0
    maximum_order_size: float = 75000.0
    margin: bool = False

    def __repr__(self):
        return "tVELO:UST"

    def __str__(self):
        return "tVELO:UST"

    def __call__(self):
        return "tVELO:UST"


VETBTC = VETBTC()


@dataclass(slots=True, frozen=True)
class VETBTC:
    """
        name: tVETBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 66.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tVETBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 66.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tVETBTC"

    def __str__(self):
        return "tVETBTC"

    def __call__(self):
        return "tVETBTC"


VETUSD = VETUSD()


@dataclass(slots=True, frozen=True)
class VETUSD:
    """
        name: tVETUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 66.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tVETUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 66.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tVETUSD"

    def __str__(self):
        return "tVETUSD"

    def __call__(self):
        return "tVETUSD"


VETUST = VETUST()


@dataclass(slots=True, frozen=True)
class VETUST:
    """
        name: tVETUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 66.0
        maximum_order_size: 5000000.0
        margin: False
    """
    name: str = "tVETUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 66.0
    maximum_order_size: float = 5000000.0
    margin: bool = False

    def __repr__(self):
        return "tVETUST"

    def __str__(self):
        return "tVETUST"

    def __call__(self):
        return "tVETUST"


VRAUSD = VRAUSD()


@dataclass(slots=True, frozen=True)
class VRAUSD:
    """
        name: tVRAUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 286.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tVRAUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 286.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tVRAUSD"

    def __str__(self):
        return "tVRAUSD"

    def __call__(self):
        return "tVRAUSD"


VRAUST = VRAUST()


@dataclass(slots=True, frozen=True)
class VRAUST:
    """
        name: tVRAUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 286.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tVRAUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 286.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tVRAUST"

    def __str__(self):
        return "tVRAUST"

    def __call__(self):
        return "tVRAUST"


VSYUSD = VSYUSD()


@dataclass(slots=True, frozen=True)
class VSYUSD:
    """
        name: tVSYUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 432.0
        maximum_order_size: 250000.0
        margin: False
    """
    name: str = "tVSYUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 432.0
    maximum_order_size: float = 250000.0
    margin: bool = False

    def __repr__(self):
        return "tVSYUSD"

    def __str__(self):
        return "tVSYUSD"

    def __call__(self):
        return "tVSYUSD"


WAVES_USD = WAVES_USD()


@dataclass(slots=True, frozen=True)
class WAVES_USD:
    """
        name: tWAVES:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tWAVES:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tWAVES:USD"

    def __str__(self):
        return "tWAVES:USD"

    def __call__(self):
        return "tWAVES:USD"


WAVES_UST = WAVES_UST()


@dataclass(slots=True, frozen=True)
class WAVES_UST:
    """
        name: tWAVES:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tWAVES:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tWAVES:UST"

    def __str__(self):
        return "tWAVES:UST"

    def __call__(self):
        return "tWAVES:UST"


WAVESF0_USTF0 = WAVESF0_USTF0()


@dataclass(slots=True, frozen=True)
class WAVESF0_USTF0:
    """
        name: tWAVESF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.2
        maximum_order_size: 50000.0
        margin: True
    """
    name: str = "tWAVESF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.2
    maximum_order_size: float = 50000.0
    margin: bool = True

    def __repr__(self):
        return "tWAVESF0:USTF0"

    def __str__(self):
        return "tWAVESF0:USTF0"

    def __call__(self):
        return "tWAVESF0:USTF0"


WAXUSD = WAXUSD()


@dataclass(slots=True, frozen=True)
class WAXUSD:
    """
        name: tWAXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 16.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tWAXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 16.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tWAXUSD"

    def __str__(self):
        return "tWAXUSD"

    def __call__(self):
        return "tWAXUSD"


WBTBTC = WBTBTC()


@dataclass(slots=True, frozen=True)
class WBTBTC:
    """
        name: tWBTBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 10.0
        margin: False
    """
    name: str = "tWBTBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 10.0
    margin: bool = False

    def __repr__(self):
        return "tWBTBTC"

    def __str__(self):
        return "tWBTBTC"

    def __call__(self):
        return "tWBTBTC"


WBTUSD = WBTUSD()


@dataclass(slots=True, frozen=True)
class WBTUSD:
    """
        name: tWBTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.00006
        maximum_order_size: 10.0
        margin: False
    """
    name: str = "tWBTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.00006
    maximum_order_size: float = 10.0
    margin: bool = False

    def __repr__(self):
        return "tWBTUSD"

    def __str__(self):
        return "tWBTUSD"

    def __call__(self):
        return "tWBTUSD"


WILD_USD = WILD_USD()


@dataclass(slots=True, frozen=True)
class WILD_USD:
    """
        name: tWILD:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tWILD:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tWILD:USD"

    def __str__(self):
        return "tWILD:USD"

    def __call__(self):
        return "tWILD:USD"


WILD_UST = WILD_UST()


@dataclass(slots=True, frozen=True)
class WILD_UST:
    """
        name: tWILD:UST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tWILD:UST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tWILD:UST"

    def __str__(self):
        return "tWILD:UST"

    def __call__(self):
        return "tWILD:UST"


WNCG_USD = WNCG_USD()


@dataclass(slots=True, frozen=True)
class WNCG_USD:
    """
        name: tWNCG:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 12.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tWNCG:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 12.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tWNCG:USD"

    def __str__(self):
        return "tWNCG:USD"

    def __call__(self):
        return "tWNCG:USD"


WOOUSD = WOOUSD()


@dataclass(slots=True, frozen=True)
class WOOUSD:
    """
        name: tWOOUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 10.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tWOOUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 10.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tWOOUSD"

    def __str__(self):
        return "tWOOUSD"

    def __call__(self):
        return "tWOOUSD"


WOOUST = WOOUST()


@dataclass(slots=True, frozen=True)
class WOOUST:
    """
        name: tWOOUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 10.0
        maximum_order_size: 2500000.0
        margin: False
    """
    name: str = "tWOOUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 10.0
    maximum_order_size: float = 2500000.0
    margin: bool = False

    def __repr__(self):
        return "tWOOUST"

    def __str__(self):
        return "tWOOUST"

    def __call__(self):
        return "tWOOUST"


XAGF0_USTF0 = XAGF0_USTF0()


@dataclass(slots=True, frozen=True)
class XAGF0_USTF0:
    """
        name: tXAGF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.1
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tXAGF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.1
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tXAGF0:USTF0"

    def __str__(self):
        return "tXAGF0:USTF0"

    def __call__(self):
        return "tXAGF0:USTF0"


XAUT_BTC = XAUT_BTC()


@dataclass(slots=True, frozen=True)
class XAUT_BTC:
    """
        name: tXAUT:BTC
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.002
        maximum_order_size: 400.0
        margin: True
    """
    name: str = "tXAUT:BTC"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 400.0
    margin: bool = True

    def __repr__(self):
        return "tXAUT:BTC"

    def __str__(self):
        return "tXAUT:BTC"

    def __call__(self):
        return "tXAUT:BTC"


XAUT_USD = XAUT_USD()


@dataclass(slots=True, frozen=True)
class XAUT_USD:
    """
        name: tXAUT:USD
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.002
        maximum_order_size: 400.0
        margin: True
    """
    name: str = "tXAUT:USD"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 400.0
    margin: bool = True

    def __repr__(self):
        return "tXAUT:USD"

    def __str__(self):
        return "tXAUT:USD"

    def __call__(self):
        return "tXAUT:USD"


XAUT_UST = XAUT_UST()


@dataclass(slots=True, frozen=True)
class XAUT_UST:
    """
        name: tXAUT:UST
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 0.002
        maximum_order_size: 400.0
        margin: True
    """
    name: str = "tXAUT:UST"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 400.0
    margin: bool = True

    def __repr__(self):
        return "tXAUT:UST"

    def __str__(self):
        return "tXAUT:UST"

    def __call__(self):
        return "tXAUT:UST"


XAUTF0_BTCF0 = XAUTF0_BTCF0()


@dataclass(slots=True, frozen=True)
class XAUTF0_BTCF0:
    """
        name: tXAUTF0:BTCF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.002
        maximum_order_size: 500.0
        margin: True
    """
    name: str = "tXAUTF0:BTCF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 500.0
    margin: bool = True

    def __repr__(self):
        return "tXAUTF0:BTCF0"

    def __str__(self):
        return "tXAUTF0:BTCF0"

    def __call__(self):
        return "tXAUTF0:BTCF0"


XAUTF0_USTF0 = XAUTF0_USTF0()


@dataclass(slots=True, frozen=True)
class XAUTF0_USTF0:
    """
        name: tXAUTF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.002
        maximum_order_size: 400.0
        margin: True
    """
    name: str = "tXAUTF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.002
    maximum_order_size: float = 400.0
    margin: bool = True

    def __repr__(self):
        return "tXAUTF0:USTF0"

    def __str__(self):
        return "tXAUTF0:USTF0"

    def __call__(self):
        return "tXAUTF0:USTF0"


XCAD_USD = XCAD_USD()


@dataclass(slots=True, frozen=True)
class XCAD_USD:
    """
        name: tXCAD:USD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 15000.0
        margin: False
    """
    name: str = "tXCAD:USD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 15000.0
    margin: bool = False

    def __repr__(self):
        return "tXCAD:USD"

    def __str__(self):
        return "tXCAD:USD"

    def __call__(self):
        return "tXCAD:USD"


XCNUSD = XCNUSD()


@dataclass(slots=True, frozen=True)
class XCNUSD:
    """
        name: tXCNUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tXCNUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tXCNUSD"

    def __str__(self):
        return "tXCNUSD"

    def __call__(self):
        return "tXCNUSD"


XCNUST = XCNUST()


@dataclass(slots=True, frozen=True)
class XCNUST:
    """
        name: tXCNUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.001
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tXCNUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.001
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tXCNUST"

    def __str__(self):
        return "tXCNUST"

    def __call__(self):
        return "tXCNUST"


XDCUSD = XDCUSD()


@dataclass(slots=True, frozen=True)
class XDCUSD:
    """
        name: tXDCUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 54.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tXDCUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 54.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tXDCUSD"

    def __str__(self):
        return "tXDCUSD"

    def __call__(self):
        return "tXDCUSD"


XDCUST = XDCUST()


@dataclass(slots=True, frozen=True)
class XDCUST:
    """
        name: tXDCUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 54.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tXDCUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 54.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tXDCUST"

    def __str__(self):
        return "tXDCUST"

    def __call__(self):
        return "tXDCUST"


XLMBTC = XLMBTC()


@dataclass(slots=True, frozen=True)
class XLMBTC:
    """
        name: tXLMBTC
        precision: 5
        minimum_margin: 25.0
        initial_margin: 50.0
        minimum_order_size: 14.0
        maximum_order_size: 1000000.0
        margin: True
    """
    name: str = "tXLMBTC"
    precision: int = 5
    minimum_margin: float = 25.0
    initial_margin: float = 50.0
    minimum_order_size: float = 14.0
    maximum_order_size: float = 1000000.0
    margin: bool = True

    def __repr__(self):
        return "tXLMBTC"

    def __str__(self):
        return "tXLMBTC"

    def __call__(self):
        return "tXLMBTC"


XLMF0_USTF0 = XLMF0_USTF0()


@dataclass(slots=True, frozen=True)
class XLMF0_USTF0:
    """
        name: tXLMF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 14.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tXLMF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 14.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tXLMF0:USTF0"

    def __str__(self):
        return "tXLMF0:USTF0"

    def __call__(self):
        return "tXLMF0:USTF0"


XLMUSD = XLMUSD()


@dataclass(slots=True, frozen=True)
class XLMUSD:
    """
        name: tXLMUSD
        precision: 5
        minimum_margin: 25.0
        initial_margin: 50.0
        minimum_order_size: 14.0
        maximum_order_size: 1000000.0
        margin: True
    """
    name: str = "tXLMUSD"
    precision: int = 5
    minimum_margin: float = 25.0
    initial_margin: float = 50.0
    minimum_order_size: float = 14.0
    maximum_order_size: float = 1000000.0
    margin: bool = True

    def __repr__(self):
        return "tXLMUSD"

    def __str__(self):
        return "tXLMUSD"

    def __call__(self):
        return "tXLMUSD"


XLMUST = XLMUST()


@dataclass(slots=True, frozen=True)
class XLMUST:
    """
        name: tXLMUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 14.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tXLMUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 14.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tXLMUST"

    def __str__(self):
        return "tXLMUST"

    def __call__(self):
        return "tXLMUST"


XMRBTC = XMRBTC()


@dataclass(slots=True, frozen=True)
class XMRBTC:
    """
        name: tXMRBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tXMRBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tXMRBTC"

    def __str__(self):
        return "tXMRBTC"

    def __call__(self):
        return "tXMRBTC"


XMRF0_USTF0 = XMRF0_USTF0()


@dataclass(slots=True, frozen=True)
class XMRF0_USTF0:
    """
        name: tXMRF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.02
        maximum_order_size: 10000.0
        margin: True
    """
    name: str = "tXMRF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 10000.0
    margin: bool = True

    def __repr__(self):
        return "tXMRF0:USTF0"

    def __str__(self):
        return "tXMRF0:USTF0"

    def __call__(self):
        return "tXMRF0:USTF0"


XMRUSD = XMRUSD()


@dataclass(slots=True, frozen=True)
class XMRUSD:
    """
        name: tXMRUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tXMRUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tXMRUSD"

    def __str__(self):
        return "tXMRUSD"

    def __call__(self):
        return "tXMRUSD"


XMRUST = XMRUST()


@dataclass(slots=True, frozen=True)
class XMRUST:
    """
        name: tXMRUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 5000.0
        margin: True
    """
    name: str = "tXMRUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 5000.0
    margin: bool = True

    def __repr__(self):
        return "tXMRUST"

    def __str__(self):
        return "tXMRUST"

    def __call__(self):
        return "tXMRUST"


XRAUSD = XRAUSD()


@dataclass(slots=True, frozen=True)
class XRAUSD:
    """
        name: tXRAUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 196.0
        maximum_order_size: 500000.0
        margin: False
    """
    name: str = "tXRAUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 196.0
    maximum_order_size: float = 500000.0
    margin: bool = False

    def __repr__(self):
        return "tXRAUSD"

    def __str__(self):
        return "tXRAUSD"

    def __call__(self):
        return "tXRAUSD"


XRDBTC = XRDBTC()


@dataclass(slots=True, frozen=True)
class XRDBTC:
    """
        name: tXRDBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 24.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tXRDBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 24.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tXRDBTC"

    def __str__(self):
        return "tXRDBTC"

    def __call__(self):
        return "tXRDBTC"


XRDUSD = XRDUSD()


@dataclass(slots=True, frozen=True)
class XRDUSD:
    """
        name: tXRDUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 24.0
        maximum_order_size: 1000000.0
        margin: False
    """
    name: str = "tXRDUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 24.0
    maximum_order_size: float = 1000000.0
    margin: bool = False

    def __repr__(self):
        return "tXRDUSD"

    def __str__(self):
        return "tXRDUSD"

    def __call__(self):
        return "tXRDUSD"


XRPBTC = XRPBTC()


@dataclass(slots=True, frozen=True)
class XRPBTC:
    """
        name: tXRPBTC
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 6.0
        maximum_order_size: 2000000.0
        margin: True
    """
    name: str = "tXRPBTC"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 2000000.0
    margin: bool = True

    def __repr__(self):
        return "tXRPBTC"

    def __str__(self):
        return "tXRPBTC"

    def __call__(self):
        return "tXRPBTC"


XRPF0_BTCF0 = XRPF0_BTCF0()


@dataclass(slots=True, frozen=True)
class XRPF0_BTCF0:
    """
        name: tXRPF0:BTCF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 6.0
        maximum_order_size: 250000.0
        margin: True
    """
    name: str = "tXRPF0:BTCF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 250000.0
    margin: bool = True

    def __repr__(self):
        return "tXRPF0:BTCF0"

    def __str__(self):
        return "tXRPF0:BTCF0"

    def __call__(self):
        return "tXRPF0:BTCF0"


XRPF0_USTF0 = XRPF0_USTF0()


@dataclass(slots=True, frozen=True)
class XRPF0_USTF0:
    """
        name: tXRPF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 6.0
        maximum_order_size: 500000.0
        margin: True
    """
    name: str = "tXRPF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 500000.0
    margin: bool = True

    def __repr__(self):
        return "tXRPF0:USTF0"

    def __str__(self):
        return "tXRPF0:USTF0"

    def __call__(self):
        return "tXRPF0:USTF0"


XRPUSD = XRPUSD()


@dataclass(slots=True, frozen=True)
class XRPUSD:
    """
        name: tXRPUSD
        precision: 5
        minimum_margin: 10.0
        initial_margin: 20.0
        minimum_order_size: 6.0
        maximum_order_size: 2000000.0
        margin: True
    """
    name: str = "tXRPUSD"
    precision: int = 5
    minimum_margin: float = 10.0
    initial_margin: float = 20.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 2000000.0
    margin: bool = True

    def __repr__(self):
        return "tXRPUSD"

    def __str__(self):
        return "tXRPUSD"

    def __call__(self):
        return "tXRPUSD"


XRPUST = XRPUST()


@dataclass(slots=True, frozen=True)
class XRPUST:
    """
        name: tXRPUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 2000000.0
        margin: True
    """
    name: str = "tXRPUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 2000000.0
    margin: bool = True

    def __repr__(self):
        return "tXRPUST"

    def __str__(self):
        return "tXRPUST"

    def __call__(self):
        return "tXRPUST"


XTZBTC = XTZBTC()


@dataclass(slots=True, frozen=True)
class XTZBTC:
    """
        name: tXTZBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tXTZBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tXTZBTC"

    def __str__(self):
        return "tXTZBTC"

    def __call__(self):
        return "tXTZBTC"


XTZF0_USTF0 = XTZF0_USTF0()


@dataclass(slots=True, frozen=True)
class XTZF0_USTF0:
    """
        name: tXTZF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tXTZF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tXTZF0:USTF0"

    def __str__(self):
        return "tXTZF0:USTF0"

    def __call__(self):
        return "tXTZF0:USTF0"


XTZUSD = XTZUSD()


@dataclass(slots=True, frozen=True)
class XTZUSD:
    """
        name: tXTZUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tXTZUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tXTZUSD"

    def __str__(self):
        return "tXTZUSD"

    def __call__(self):
        return "tXTZUSD"


XTZUST = XTZUST()


@dataclass(slots=True, frozen=True)
class XTZUST:
    """
        name: tXTZUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 100000.0
        margin: True
    """
    name: str = "tXTZUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 100000.0
    margin: bool = True

    def __repr__(self):
        return "tXTZUST"

    def __str__(self):
        return "tXTZUST"

    def __call__(self):
        return "tXTZUST"


XVGUSD = XVGUSD()


@dataclass(slots=True, frozen=True)
class XVGUSD:
    """
        name: tXVGUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 432.0
        maximum_order_size: 1500000.0
        margin: False
    """
    name: str = "tXVGUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 432.0
    maximum_order_size: float = 1500000.0
    margin: bool = False

    def __repr__(self):
        return "tXVGUSD"

    def __str__(self):
        return "tXVGUSD"

    def __call__(self):
        return "tXVGUSD"


YFIUSD = YFIUSD()


@dataclass(slots=True, frozen=True)
class YFIUSD:
    """
        name: tYFIUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.0002
        maximum_order_size: 100.0
        margin: True
    """
    name: str = "tYFIUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.0002
    maximum_order_size: float = 100.0
    margin: bool = True

    def __repr__(self):
        return "tYFIUSD"

    def __str__(self):
        return "tYFIUSD"

    def __call__(self):
        return "tYFIUSD"


YFIUST = YFIUST()


@dataclass(slots=True, frozen=True)
class YFIUST:
    """
        name: tYFIUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.0002
        maximum_order_size: 100.0
        margin: True
    """
    name: str = "tYFIUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.0002
    maximum_order_size: float = 100.0
    margin: bool = True

    def __repr__(self):
        return "tYFIUST"

    def __str__(self):
        return "tYFIUST"

    def __call__(self):
        return "tYFIUST"


ZCNUSD = ZCNUSD()


@dataclass(slots=True, frozen=True)
class ZCNUSD:
    """
        name: tZCNUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 10.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tZCNUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 10.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tZCNUSD"

    def __str__(self):
        return "tZCNUSD"

    def __call__(self):
        return "tZCNUSD"


ZECBTC = ZECBTC()


@dataclass(slots=True, frozen=True)
class ZECBTC:
    """
        name: tZECBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 20000.0
        margin: True
    """
    name: str = "tZECBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 20000.0
    margin: bool = True

    def __repr__(self):
        return "tZECBTC"

    def __str__(self):
        return "tZECBTC"

    def __call__(self):
        return "tZECBTC"


ZECF0_USTF0 = ZECF0_USTF0()


@dataclass(slots=True, frozen=True)
class ZECF0_USTF0:
    """
        name: tZECF0:USTF0
        precision: 5
        minimum_margin: 0.5
        initial_margin: 1.0
        minimum_order_size: 0.02
        maximum_order_size: 20000.0
        margin: True
    """
    name: str = "tZECF0:USTF0"
    precision: int = 5
    minimum_margin: float = 0.5
    initial_margin: float = 1.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 20000.0
    margin: bool = True

    def __repr__(self):
        return "tZECF0:USTF0"

    def __str__(self):
        return "tZECF0:USTF0"

    def __call__(self):
        return "tZECF0:USTF0"


ZECUSD = ZECUSD()


@dataclass(slots=True, frozen=True)
class ZECUSD:
    """
        name: tZECUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 0.02
        maximum_order_size: 20000.0
        margin: True
    """
    name: str = "tZECUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 0.02
    maximum_order_size: float = 20000.0
    margin: bool = True

    def __repr__(self):
        return "tZECUSD"

    def __str__(self):
        return "tZECUSD"

    def __call__(self):
        return "tZECUSD"


ZILBTC = ZILBTC()


@dataclass(slots=True, frozen=True)
class ZILBTC:
    """
        name: tZILBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 40.0
        maximum_order_size: 1500000.0
        margin: False
    """
    name: str = "tZILBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 40.0
    maximum_order_size: float = 1500000.0
    margin: bool = False

    def __repr__(self):
        return "tZILBTC"

    def __str__(self):
        return "tZILBTC"

    def __call__(self):
        return "tZILBTC"


ZILUSD = ZILUSD()


@dataclass(slots=True, frozen=True)
class ZILUSD:
    """
        name: tZILUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 40.0
        maximum_order_size: 1500000.0
        margin: False
    """
    name: str = "tZILUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 40.0
    maximum_order_size: float = 1500000.0
    margin: bool = False

    def __repr__(self):
        return "tZILUSD"

    def __str__(self):
        return "tZILUSD"

    def __call__(self):
        return "tZILUSD"


ZMTUSD = ZMTUSD()


@dataclass(slots=True, frozen=True)
class ZMTUSD:
    """
        name: tZMTUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tZMTUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tZMTUSD"

    def __str__(self):
        return "tZMTUSD"

    def __call__(self):
        return "tZMTUSD"


ZMTUST = ZMTUST()


@dataclass(slots=True, frozen=True)
class ZMTUST:
    """
        name: tZMTUST
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 2.0
        maximum_order_size: 50000.0
        margin: False
    """
    name: str = "tZMTUST"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 2.0
    maximum_order_size: float = 50000.0
    margin: bool = False

    def __repr__(self):
        return "tZMTUST"

    def __str__(self):
        return "tZMTUST"

    def __call__(self):
        return "tZMTUST"


ZRXBTC = ZRXBTC()


@dataclass(slots=True, frozen=True)
class ZRXBTC:
    """
        name: tZRXBTC
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 200000.0
        margin: False
    """
    name: str = "tZRXBTC"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 200000.0
    margin: bool = False

    def __repr__(self):
        return "tZRXBTC"

    def __str__(self):
        return "tZRXBTC"

    def __call__(self):
        return "tZRXBTC"


ZRXETH = ZRXETH()


@dataclass(slots=True, frozen=True)
class ZRXETH:
    """
        name: tZRXETH
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 200000.0
        margin: True
    """
    name: str = "tZRXETH"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 200000.0
    margin: bool = True

    def __repr__(self):
        return "tZRXETH"

    def __str__(self):
        return "tZRXETH"

    def __call__(self):
        return "tZRXETH"


ZRXUSD = ZRXUSD()


@dataclass(slots=True, frozen=True)
class ZRXUSD:
    """
        name: tZRXUSD
        precision: 5
        minimum_margin: 15.0
        initial_margin: 30.0
        minimum_order_size: 6.0
        maximum_order_size: 200000.0
        margin: True
    """
    name: str = "tZRXUSD"
    precision: int = 5
    minimum_margin: float = 15.0
    initial_margin: float = 30.0
    minimum_order_size: float = 6.0
    maximum_order_size: float = 200000.0
    margin: bool = True

    def __repr__(self):
        return "tZRXUSD"

    def __str__(self):
        return "tZRXUSD"

    def __call__(self):
        return "tZRXUSD"
