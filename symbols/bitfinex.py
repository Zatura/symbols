from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ONEINCH_USD:
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


ONEINCH_USD = ONEINCH_USD()


@dataclass(slots=True, frozen=True)
class ONEINCH_UST:
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


ONEINCH_UST = ONEINCH_UST()


@dataclass(slots=True, frozen=True)
class AAABBB:
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


AAABBB = AAABBB()


@dataclass(slots=True, frozen=True)
class AAVE_USD:
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


AAVE_USD = AAVE_USD()


@dataclass(slots=True, frozen=True)
class AAVE_UST:
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


AAVE_UST = AAVE_UST()


@dataclass(slots=True, frozen=True)
class AAVEF0_USTF0:
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


AAVEF0_USTF0 = AAVEF0_USTF0()


@dataclass(slots=True, frozen=True)
class ADABTC:
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


ADABTC = ADABTC()


@dataclass(slots=True, frozen=True)
class ADAF0_USTF0:
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


ADAF0_USTF0 = ADAF0_USTF0()


@dataclass(slots=True, frozen=True)
class ADAUSD:
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


ADAUSD = ADAUSD()


@dataclass(slots=True, frozen=True)
class ADAUST:
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


ADAUST = ADAUST()


@dataclass(slots=True, frozen=True)
class AIXUSD:
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


AIXUSD = AIXUSD()


@dataclass(slots=True, frozen=True)
class AIXUST:
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


AIXUST = AIXUST()


@dataclass(slots=True, frozen=True)
class ALBT_USD:
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


ALBT_USD = ALBT_USD()


@dataclass(slots=True, frozen=True)
class ALGBTC:
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


ALGBTC = ALGBTC()


@dataclass(slots=True, frozen=True)
class ALGF0_USTF0:
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


ALGF0_USTF0 = ALGF0_USTF0()


@dataclass(slots=True, frozen=True)
class ALGUSD:
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


ALGUSD = ALGUSD()


@dataclass(slots=True, frozen=True)
class ALGUST:
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


ALGUST = ALGUST()


@dataclass(slots=True, frozen=True)
class AMPBTC:
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


AMPBTC = AMPBTC()


@dataclass(slots=True, frozen=True)
class AMPF0_USTF0:
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


AMPF0_USTF0 = AMPF0_USTF0()


@dataclass(slots=True, frozen=True)
class AMPUSD:
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


AMPUSD = AMPUSD()


@dataclass(slots=True, frozen=True)
class AMPUST:
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


AMPUST = AMPUST()


@dataclass(slots=True, frozen=True)
class ANCUSD:
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


ANCUSD = ANCUSD()


@dataclass(slots=True, frozen=True)
class ANTBTC:
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


ANTBTC = ANTBTC()


@dataclass(slots=True, frozen=True)
class ANTUSD:
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


ANTUSD = ANTUSD()


@dataclass(slots=True, frozen=True)
class APEF0_USTF0:
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


APEF0_USTF0 = APEF0_USTF0()


@dataclass(slots=True, frozen=True)
class APENFT_USD:
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


APENFT_USD = APENFT_USD()


@dataclass(slots=True, frozen=True)
class APENFT_UST:
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


APENFT_UST = APENFT_UST()


@dataclass(slots=True, frozen=True)
class APEUSD:
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


APEUSD = APEUSD()


@dataclass(slots=True, frozen=True)
class APEUST:
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


APEUST = APEUST()


@dataclass(slots=True, frozen=True)
class APTF0_USTF0:
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


APTF0_USTF0 = APTF0_USTF0()


@dataclass(slots=True, frozen=True)
class APTUSD:
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


APTUSD = APTUSD()


@dataclass(slots=True, frozen=True)
class APTUST:
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


APTUST = APTUST()


@dataclass(slots=True, frozen=True)
class ATLAS_USD:
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


ATLAS_USD = ATLAS_USD()


@dataclass(slots=True, frozen=True)
class ATLAS_UST:
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


ATLAS_UST = ATLAS_UST()


@dataclass(slots=True, frozen=True)
class ATOBTC:
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


ATOBTC = ATOBTC()


@dataclass(slots=True, frozen=True)
class ATOETH:
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


ATOETH = ATOETH()


@dataclass(slots=True, frozen=True)
class ATOF0_USTF0:
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


ATOF0_USTF0 = ATOF0_USTF0()


@dataclass(slots=True, frozen=True)
class ATOUSD:
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


ATOUSD = ATOUSD()


@dataclass(slots=True, frozen=True)
class ATOUST:
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


ATOUST = ATOUST()


@dataclass(slots=True, frozen=True)
class AVAX_BTC:
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


AVAX_BTC = AVAX_BTC()


@dataclass(slots=True, frozen=True)
class AVAX_USD:
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


AVAX_USD = AVAX_USD()


@dataclass(slots=True, frozen=True)
class AVAX_UST:
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


AVAX_UST = AVAX_UST()


@dataclass(slots=True, frozen=True)
class AVAXF0_BTCF0:
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


AVAXF0_BTCF0 = AVAXF0_BTCF0()


@dataclass(slots=True, frozen=True)
class AVAXF0_USTF0:
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


AVAXF0_USTF0 = AVAXF0_USTF0()


@dataclass(slots=True, frozen=True)
class AXSF0_USTF0:
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


AXSF0_USTF0 = AXSF0_USTF0()


@dataclass(slots=True, frozen=True)
class AXSUSD:
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


AXSUSD = AXSUSD()


@dataclass(slots=True, frozen=True)
class AXSUST:
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


AXSUST = AXSUST()


@dataclass(slots=True, frozen=True)
class B2MUSD:
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


B2MUSD = B2MUSD()


@dataclass(slots=True, frozen=True)
class B2MUST:
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


B2MUST = B2MUST()


@dataclass(slots=True, frozen=True)
class BALUSD:
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


BALUSD = BALUSD()


@dataclass(slots=True, frozen=True)
class BALUST:
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


BALUST = BALUST()


@dataclass(slots=True, frozen=True)
class BAND_USD:
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


BAND_USD = BAND_USD()


@dataclass(slots=True, frozen=True)
class BAND_UST:
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


BAND_UST = BAND_UST()


@dataclass(slots=True, frozen=True)
class BATUSD:
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


BATUSD = BATUSD()


@dataclass(slots=True, frozen=True)
class BATUST:
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


BATUST = BATUST()


@dataclass(slots=True, frozen=True)
class BCHABC_USD:
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


BCHABC_USD = BCHABC_USD()


@dataclass(slots=True, frozen=True)
class BCHN_USD:
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


BCHN_USD = BCHN_USD()


@dataclass(slots=True, frozen=True)
class BEST_USD:
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


BEST_USD = BEST_USD()


@dataclass(slots=True, frozen=True)
class BMNBTC:
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


BMNBTC = BMNBTC()


@dataclass(slots=True, frozen=True)
class BMNUSD:
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


BMNUSD = BMNUSD()


@dataclass(slots=True, frozen=True)
class BNTUSD:
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


BNTUSD = BNTUSD()


@dataclass(slots=True, frozen=True)
class BOBA_USD:
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


BOBA_USD = BOBA_USD()


@dataclass(slots=True, frozen=True)
class BOBA_UST:
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


BOBA_UST = BOBA_UST()


@dataclass(slots=True, frozen=True)
class BOOUSD:
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


BOOUSD = BOOUSD()


@dataclass(slots=True, frozen=True)
class BOOUST:
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


BOOUST = BOOUST()


@dataclass(slots=True, frozen=True)
class BOSON_USD:
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


BOSON_USD = BOSON_USD()


@dataclass(slots=True, frozen=True)
class BOSON_UST:
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


BOSON_UST = BOSON_UST()


@dataclass(slots=True, frozen=True)
class BTC_CNHT:
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


BTC_CNHT = BTC_CNHT()


@dataclass(slots=True, frozen=True)
class BTC_MXNT:
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


BTC_MXNT = BTC_MXNT()


@dataclass(slots=True, frozen=True)
class BTC_XAUT:
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


BTC_XAUT = BTC_XAUT()


@dataclass(slots=True, frozen=True)
class BTCDOMF0_USTF0:
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


BTCDOMF0_USTF0 = BTCDOMF0_USTF0()


@dataclass(slots=True, frozen=True)
class BTCEUR:
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


BTCEUR = BTCEUR()


@dataclass(slots=True, frozen=True)
class BTCEUT:
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


BTCEUT = BTCEUT()


@dataclass(slots=True, frozen=True)
class BTCF0_EUTF0:
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


BTCF0_EUTF0 = BTCF0_EUTF0()


@dataclass(slots=True, frozen=True)
class BTCF0_USTF0:
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


BTCF0_USTF0 = BTCF0_USTF0()


@dataclass(slots=True, frozen=True)
class BTCGBP:
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


BTCGBP = BTCGBP()


@dataclass(slots=True, frozen=True)
class BTCJPY:
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


BTCJPY = BTCJPY()


@dataclass(slots=True, frozen=True)
class BTCMIM:
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


BTCMIM = BTCMIM()


@dataclass(slots=True, frozen=True)
class BTCTRY:
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


BTCTRY = BTCTRY()


@dataclass(slots=True, frozen=True)
class BTCUSD:
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


BTCUSD = BTCUSD()


@dataclass(slots=True, frozen=True)
class BTCUST:
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


BTCUST = BTCUST()


@dataclass(slots=True, frozen=True)
class BTGBTC:
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


BTGBTC = BTGBTC()


@dataclass(slots=True, frozen=True)
class BTGUSD:
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


BTGUSD = BTGUSD()


@dataclass(slots=True, frozen=True)
class BTSE_USD:
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


BTSE_USD = BTSE_USD()


@dataclass(slots=True, frozen=True)
class BTTUSD:
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


BTTUSD = BTTUSD()


@dataclass(slots=True, frozen=True)
class CCDBTC:
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


CCDBTC = CCDBTC()


@dataclass(slots=True, frozen=True)
class CCDUSD:
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


CCDUSD = CCDUSD()


@dataclass(slots=True, frozen=True)
class CCDUST:
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


CCDUST = CCDUST()


@dataclass(slots=True, frozen=True)
class CHEX_USD:
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


CHEX_USD = CHEX_USD()


@dataclass(slots=True, frozen=True)
class CHSB_BTC:
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


CHSB_BTC = CHSB_BTC()


@dataclass(slots=True, frozen=True)
class CHSB_USD:
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


CHSB_USD = CHSB_USD()


@dataclass(slots=True, frozen=True)
class CHSB_UST:
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


CHSB_UST = CHSB_UST()


@dataclass(slots=True, frozen=True)
class CHZUSD:
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


CHZUSD = CHZUSD()


@dataclass(slots=True, frozen=True)
class CHZUST:
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


CHZUST = CHZUST()


@dataclass(slots=True, frozen=True)
class CLOUSD:
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


CLOUSD = CLOUSD()


@dataclass(slots=True, frozen=True)
class CNH_CNHT:
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


CNH_CNHT = CNH_CNHT()


@dataclass(slots=True, frozen=True)
class COMP_USD:
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


COMP_USD = COMP_USD()


@dataclass(slots=True, frozen=True)
class COMP_UST:
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


COMP_UST = COMP_UST()


@dataclass(slots=True, frozen=True)
class COMPF0_USTF0:
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


COMPF0_USTF0 = COMPF0_USTF0()


@dataclass(slots=True, frozen=True)
class CONV_USD:
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


CONV_USD = CONV_USD()


@dataclass(slots=True, frozen=True)
class CONV_UST:
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


CONV_UST = CONV_UST()


@dataclass(slots=True, frozen=True)
class CRVF0_USTF0:
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


CRVF0_USTF0 = CRVF0_USTF0()


@dataclass(slots=True, frozen=True)
class CRVUSD:
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


CRVUSD = CRVUSD()


@dataclass(slots=True, frozen=True)
class CRVUST:
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


CRVUST = CRVUST()


@dataclass(slots=True, frozen=True)
class DAIBTC:
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


DAIBTC = DAIBTC()


@dataclass(slots=True, frozen=True)
class DAIETH:
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


DAIETH = DAIETH()


@dataclass(slots=True, frozen=True)
class DAIUSD:
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


DAIUSD = DAIUSD()


@dataclass(slots=True, frozen=True)
class DGBUSD:
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


DGBUSD = DGBUSD()


@dataclass(slots=True, frozen=True)
class DOGE_BTC:
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


DOGE_BTC = DOGE_BTC()


@dataclass(slots=True, frozen=True)
class DOGE_USD:
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


DOGE_USD = DOGE_USD()


@dataclass(slots=True, frozen=True)
class DOGE_UST:
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


DOGE_UST = DOGE_UST()


@dataclass(slots=True, frozen=True)
class DOGEF0_USTF0:
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


DOGEF0_USTF0 = DOGEF0_USTF0()


@dataclass(slots=True, frozen=True)
class DORA_USD:
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


DORA_USD = DORA_USD()


@dataclass(slots=True, frozen=True)
class DORA_UST:
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


DORA_UST = DORA_UST()


@dataclass(slots=True, frozen=True)
class DOTBTC:
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


DOTBTC = DOTBTC()


@dataclass(slots=True, frozen=True)
class DOTF0_BTCF0:
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


DOTF0_BTCF0 = DOTF0_BTCF0()


@dataclass(slots=True, frozen=True)
class DOTF0_USTF0:
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


DOTF0_USTF0 = DOTF0_USTF0()


@dataclass(slots=True, frozen=True)
class DOTUSD:
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


DOTUSD = DOTUSD()


@dataclass(slots=True, frozen=True)
class DOTUST:
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


DOTUST = DOTUST()


@dataclass(slots=True, frozen=True)
class DSHBTC:
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


DSHBTC = DSHBTC()


@dataclass(slots=True, frozen=True)
class DSHUSD:
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


DSHUSD = DSHUSD()


@dataclass(slots=True, frozen=True)
class DUSK_BTC:
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


DUSK_BTC = DUSK_BTC()


@dataclass(slots=True, frozen=True)
class DUSK_USD:
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


DUSK_USD = DUSK_USD()


@dataclass(slots=True, frozen=True)
class DVFUSD:
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


DVFUSD = DVFUSD()


@dataclass(slots=True, frozen=True)
class EDOUSD:
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


EDOUSD = EDOUSD()


@dataclass(slots=True, frozen=True)
class EGLD_USD:
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


EGLD_USD = EGLD_USD()


@dataclass(slots=True, frozen=True)
class EGLD_UST:
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


EGLD_UST = EGLD_UST()


@dataclass(slots=True, frozen=True)
class EGLDF0_USTF0:
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


EGLDF0_USTF0 = EGLDF0_USTF0()


@dataclass(slots=True, frozen=True)
class ENJUSD:
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


ENJUSD = ENJUSD()


@dataclass(slots=True, frozen=True)
class EOSBTC:
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


EOSBTC = EOSBTC()


@dataclass(slots=True, frozen=True)
class EOSETH:
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


EOSETH = EOSETH()


@dataclass(slots=True, frozen=True)
class EOSEUR:
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


EOSEUR = EOSEUR()


@dataclass(slots=True, frozen=True)
class EOSF0_USTF0:
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


EOSF0_USTF0 = EOSF0_USTF0()


@dataclass(slots=True, frozen=True)
class EOSUSD:
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


EOSUSD = EOSUSD()


@dataclass(slots=True, frozen=True)
class EOSUST:
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


EOSUST = EOSUST()


@dataclass(slots=True, frozen=True)
class ETCBTC:
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


ETCBTC = ETCBTC()


@dataclass(slots=True, frozen=True)
class ETCF0_USTF0:
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


ETCF0_USTF0 = ETCF0_USTF0()


@dataclass(slots=True, frozen=True)
class ETCUSD:
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


ETCUSD = ETCUSD()


@dataclass(slots=True, frozen=True)
class ETCUST:
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


ETCUST = ETCUST()


@dataclass(slots=True, frozen=True)
class ETH2X_ETH:
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


ETH2X_ETH = ETH2X_ETH()


@dataclass(slots=True, frozen=True)
class ETH2X_USD:
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


ETH2X_USD = ETH2X_USD()


@dataclass(slots=True, frozen=True)
class ETH2X_UST:
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


ETH2X_UST = ETH2X_UST()


@dataclass(slots=True, frozen=True)
class ETH_MXNT:
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


ETH_MXNT = ETH_MXNT()


@dataclass(slots=True, frozen=True)
class ETH_XAUT:
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


ETH_XAUT = ETH_XAUT()


@dataclass(slots=True, frozen=True)
class ETHBTC:
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


ETHBTC = ETHBTC()


@dataclass(slots=True, frozen=True)
class ETHEUR:
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


ETHEUR = ETHEUR()


@dataclass(slots=True, frozen=True)
class ETHEUT:
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


ETHEUT = ETHEUT()


@dataclass(slots=True, frozen=True)
class ETHF0_BTCF0:
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


ETHF0_BTCF0 = ETHF0_BTCF0()


@dataclass(slots=True, frozen=True)
class ETHF0_EUTF0:
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


ETHF0_EUTF0 = ETHF0_EUTF0()


@dataclass(slots=True, frozen=True)
class ETHF0_USTF0:
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


ETHF0_USTF0 = ETHF0_USTF0()


@dataclass(slots=True, frozen=True)
class ETHGBP:
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


ETHGBP = ETHGBP()


@dataclass(slots=True, frozen=True)
class ETHJPY:
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


ETHJPY = ETHJPY()


@dataclass(slots=True, frozen=True)
class ETHUSD:
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


ETHUSD = ETHUSD()


@dataclass(slots=True, frozen=True)
class ETHUST:
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


ETHUST = ETHUST()


@dataclass(slots=True, frozen=True)
class ETHW_USD:
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


ETHW_USD = ETHW_USD()


@dataclass(slots=True, frozen=True)
class ETHW_UST:
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


ETHW_UST = ETHW_UST()


@dataclass(slots=True, frozen=True)
class ETPUSD:
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


ETPUSD = ETPUSD()


@dataclass(slots=True, frozen=True)
class EURF0_USTF0:
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


EURF0_USTF0 = EURF0_USTF0()


@dataclass(slots=True, frozen=True)
class EURUST:
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


EURUST = EURUST()


@dataclass(slots=True, frozen=True)
class EUSUSD:
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


EUSUSD = EUSUSD()


@dataclass(slots=True, frozen=True)
class EUT_MXNT:
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


EUT_MXNT = EUT_MXNT()


@dataclass(slots=True, frozen=True)
class EUTEUR:
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


EUTEUR = EUTEUR()


@dataclass(slots=True, frozen=True)
class EUTUSD:
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


EUTUSD = EUTUSD()


@dataclass(slots=True, frozen=True)
class EUTUST:
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


EUTUST = EUTUST()


@dataclass(slots=True, frozen=True)
class EXOUSD:
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


EXOUSD = EXOUSD()


@dataclass(slots=True, frozen=True)
class FBTUSD:
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


FBTUSD = FBTUSD()


@dataclass(slots=True, frozen=True)
class FBTUST:
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


FBTUST = FBTUST()


@dataclass(slots=True, frozen=True)
class FCLUSD:
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


FCLUSD = FCLUSD()


@dataclass(slots=True, frozen=True)
class FCLUST:
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


FCLUST = FCLUST()


@dataclass(slots=True, frozen=True)
class FETUSD:
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


FETUSD = FETUSD()


@dataclass(slots=True, frozen=True)
class FETUST:
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


FETUST = FETUST()


@dataclass(slots=True, frozen=True)
class FILF0_USTF0:
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


FILF0_USTF0 = FILF0_USTF0()


@dataclass(slots=True, frozen=True)
class FILUSD:
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


FILUSD = FILUSD()


@dataclass(slots=True, frozen=True)
class FILUST:
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


FILUST = FILUST()


@dataclass(slots=True, frozen=True)
class FLRUSD:
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


FLRUSD = FLRUSD()


@dataclass(slots=True, frozen=True)
class FLRUST:
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


FLRUST = FLRUST()


@dataclass(slots=True, frozen=True)
class FORTH_USD:
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


FORTH_USD = FORTH_USD()


@dataclass(slots=True, frozen=True)
class FORTH_UST:
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


FORTH_UST = FORTH_UST()


@dataclass(slots=True, frozen=True)
class FTMF0_USTF0:
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


FTMF0_USTF0 = FTMF0_USTF0()


@dataclass(slots=True, frozen=True)
class FTMUSD:
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


FTMUSD = FTMUSD()


@dataclass(slots=True, frozen=True)
class FTMUST:
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


FTMUST = FTMUST()


@dataclass(slots=True, frozen=True)
class FUNUSD:
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


FUNUSD = FUNUSD()


@dataclass(slots=True, frozen=True)
class GALA_USD:
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


GALA_USD = GALA_USD()


@dataclass(slots=True, frozen=True)
class GALA_UST:
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


GALA_UST = GALA_UST()


@dataclass(slots=True, frozen=True)
class GALAF0_USTF0:
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


GALAF0_USTF0 = GALAF0_USTF0()


@dataclass(slots=True, frozen=True)
class GBPEUT:
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


GBPEUT = GBPEUT()


@dataclass(slots=True, frozen=True)
class GBPF0_USTF0:
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


GBPF0_USTF0 = GBPF0_USTF0()


@dataclass(slots=True, frozen=True)
class GBPUST:
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


GBPUST = GBPUST()


@dataclass(slots=True, frozen=True)
class GNOUSD:
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


GNOUSD = GNOUSD()


@dataclass(slots=True, frozen=True)
class GNTUSD:
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


GNTUSD = GNTUSD()


@dataclass(slots=True, frozen=True)
class GRTUSD:
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


GRTUSD = GRTUSD()


@dataclass(slots=True, frozen=True)
class GRTUST:
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


GRTUST = GRTUST()


@dataclass(slots=True, frozen=True)
class GTXUSD:
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


GTXUSD = GTXUSD()


@dataclass(slots=True, frozen=True)
class GTXUST:
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


GTXUST = GTXUST()


@dataclass(slots=True, frozen=True)
class GXTUSD:
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


GXTUSD = GXTUSD()


@dataclass(slots=True, frozen=True)
class GXTUST:
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


GXTUST = GXTUST()


@dataclass(slots=True, frozen=True)
class HECUSD:
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


HECUSD = HECUSD()


@dataclass(slots=True, frozen=True)
class HECUST:
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


HECUST = HECUST()


@dataclass(slots=True, frozen=True)
class HIXUSD:
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


HIXUSD = HIXUSD()


@dataclass(slots=True, frozen=True)
class HIXUST:
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


HIXUST = HIXUST()


@dataclass(slots=True, frozen=True)
class HMTUSD:
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


HMTUSD = HMTUSD()


@dataclass(slots=True, frozen=True)
class HMTUST:
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


HMTUST = HMTUST()


@dataclass(slots=True, frozen=True)
class HTXUSD:
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


HTXUSD = HTXUSD()


@dataclass(slots=True, frozen=True)
class HTXUST:
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


HTXUST = HTXUST()


@dataclass(slots=True, frozen=True)
class ICEUSD:
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


ICEUSD = ICEUSD()


@dataclass(slots=True, frozen=True)
class ICPBTC:
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


ICPBTC = ICPBTC()


@dataclass(slots=True, frozen=True)
class ICPF0_USTF0:
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


ICPF0_USTF0 = ICPF0_USTF0()


@dataclass(slots=True, frozen=True)
class ICPUSD:
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


ICPUSD = ICPUSD()


@dataclass(slots=True, frozen=True)
class ICPUST:
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


ICPUST = ICPUST()


@dataclass(slots=True, frozen=True)
class IDXUSD:
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


IDXUSD = IDXUSD()


@dataclass(slots=True, frozen=True)
class IDXUST:
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


IDXUST = IDXUST()


@dataclass(slots=True, frozen=True)
class IOTBTC:
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


IOTBTC = IOTBTC()


@dataclass(slots=True, frozen=True)
class IOTETH:
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


IOTETH = IOTETH()


@dataclass(slots=True, frozen=True)
class IOTF0_USTF0:
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


IOTF0_USTF0 = IOTF0_USTF0()


@dataclass(slots=True, frozen=True)
class IOTUSD:
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


IOTUSD = IOTUSD()


@dataclass(slots=True, frozen=True)
class IQXUSD:
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


IQXUSD = IQXUSD()


@dataclass(slots=True, frozen=True)
class JASMY_USD:
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


JASMY_USD = JASMY_USD()


@dataclass(slots=True, frozen=True)
class JASMY_UST:
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


JASMY_UST = JASMY_UST()


@dataclass(slots=True, frozen=True)
class JASMYF0_USTF0:
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


JASMYF0_USTF0 = JASMYF0_USTF0()


@dataclass(slots=True, frozen=True)
class JPYF0_USTF0:
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


JPYF0_USTF0 = JPYF0_USTF0()


@dataclass(slots=True, frozen=True)
class JPYUST:
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


JPYUST = JPYUST()


@dataclass(slots=True, frozen=True)
class JSTBTC:
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


JSTBTC = JSTBTC()


@dataclass(slots=True, frozen=True)
class JSTUSD:
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


JSTUSD = JSTUSD()


@dataclass(slots=True, frozen=True)
class JSTUST:
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


JSTUST = JSTUST()


@dataclass(slots=True, frozen=True)
class KAIUSD:
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


KAIUSD = KAIUSD()


@dataclass(slots=True, frozen=True)
class KAIUST:
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


KAIUST = KAIUST()


@dataclass(slots=True, frozen=True)
class KANUSD:
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


KANUSD = KANUSD()


@dataclass(slots=True, frozen=True)
class KANUST:
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


KANUST = KANUST()


@dataclass(slots=True, frozen=True)
class KNCBTC:
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


KNCBTC = KNCBTC()


@dataclass(slots=True, frozen=True)
class KNCF0_USTF0:
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


KNCF0_USTF0 = KNCF0_USTF0()


@dataclass(slots=True, frozen=True)
class KNCUSD:
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


KNCUSD = KNCUSD()


@dataclass(slots=True, frozen=True)
class KSMUSD:
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


KSMUSD = KSMUSD()


@dataclass(slots=True, frozen=True)
class KSMUST:
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


KSMUST = KSMUST()


@dataclass(slots=True, frozen=True)
class LEOBTC:
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


LEOBTC = LEOBTC()


@dataclass(slots=True, frozen=True)
class LEOETH:
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


LEOETH = LEOETH()


@dataclass(slots=True, frozen=True)
class LEOUSD:
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


LEOUSD = LEOUSD()


@dataclass(slots=True, frozen=True)
class LEOUST:
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


LEOUST = LEOUST()


@dataclass(slots=True, frozen=True)
class LINK_USD:
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


LINK_USD = LINK_USD()


@dataclass(slots=True, frozen=True)
class LINK_UST:
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


LINK_UST = LINK_UST()


@dataclass(slots=True, frozen=True)
class LINKF0_USTF0:
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


LINKF0_USTF0 = LINKF0_USTF0()


@dataclass(slots=True, frozen=True)
class LRCUSD:
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


LRCUSD = LRCUSD()


@dataclass(slots=True, frozen=True)
class LTCBTC:
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


LTCBTC = LTCBTC()


@dataclass(slots=True, frozen=True)
class LTCF0_BTCF0:
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


LTCF0_BTCF0 = LTCF0_BTCF0()


@dataclass(slots=True, frozen=True)
class LTCF0_USTF0:
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


LTCF0_USTF0 = LTCF0_USTF0()


@dataclass(slots=True, frozen=True)
class LTCUSD:
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


LTCUSD = LTCUSD()


@dataclass(slots=True, frozen=True)
class LTCUST:
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


LTCUST = LTCUST()


@dataclass(slots=True, frozen=True)
class LUNA2_USD:
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


LUNA2_USD = LUNA2_USD()


@dataclass(slots=True, frozen=True)
class LUNA2_UST:
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


LUNA2_UST = LUNA2_UST()


@dataclass(slots=True, frozen=True)
class LUNA_USD:
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


LUNA_USD = LUNA_USD()


@dataclass(slots=True, frozen=True)
class LUNA_UST:
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


LUNA_UST = LUNA_UST()


@dataclass(slots=True, frozen=True)
class LUXO_USD:
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


LUXO_USD = LUXO_USD()


@dataclass(slots=True, frozen=True)
class LYMUSD:
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


LYMUSD = LYMUSD()


@dataclass(slots=True, frozen=True)
class MATIC_BTC:
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


MATIC_BTC = MATIC_BTC()


@dataclass(slots=True, frozen=True)
class MATIC_USD:
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


MATIC_USD = MATIC_USD()


@dataclass(slots=True, frozen=True)
class MATIC_UST:
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


MATIC_UST = MATIC_UST()


@dataclass(slots=True, frozen=True)
class MATICF0_USTF0:
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


MATICF0_USTF0 = MATICF0_USTF0()


@dataclass(slots=True, frozen=True)
class MIMUSD:
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


MIMUSD = MIMUSD()


@dataclass(slots=True, frozen=True)
class MIMUST:
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


MIMUST = MIMUST()


@dataclass(slots=True, frozen=True)
class MIRUSD:
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


MIRUSD = MIRUSD()


@dataclass(slots=True, frozen=True)
class MKRF0_USTF0:
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


MKRF0_USTF0 = MKRF0_USTF0()


@dataclass(slots=True, frozen=True)
class MKRUSD:
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


MKRUSD = MKRUSD()


@dataclass(slots=True, frozen=True)
class MKRUST:
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


MKRUST = MKRUST()


@dataclass(slots=True, frozen=True)
class MLNUSD:
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


MLNUSD = MLNUSD()


@dataclass(slots=True, frozen=True)
class MNABTC:
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


MNABTC = MNABTC()


@dataclass(slots=True, frozen=True)
class MNAUSD:
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


MNAUSD = MNAUSD()


@dataclass(slots=True, frozen=True)
class MOBUSD:
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


MOBUSD = MOBUSD()


@dataclass(slots=True, frozen=True)
class MOBUST:
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


MOBUST = MOBUST()


@dataclass(slots=True, frozen=True)
class MXNT_USD:
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


MXNT_USD = MXNT_USD()


@dataclass(slots=True, frozen=True)
class NEAR_USD:
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


NEAR_USD = NEAR_USD()


@dataclass(slots=True, frozen=True)
class NEAR_UST:
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


NEAR_UST = NEAR_UST()


@dataclass(slots=True, frozen=True)
class NEARF0_USTF0:
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


NEARF0_USTF0 = NEARF0_USTF0()


@dataclass(slots=True, frozen=True)
class NEOBTC:
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


NEOBTC = NEOBTC()


@dataclass(slots=True, frozen=True)
class NEOF0_USTF0:
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


NEOF0_USTF0 = NEOF0_USTF0()


@dataclass(slots=True, frozen=True)
class NEOUSD:
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


NEOUSD = NEOUSD()


@dataclass(slots=True, frozen=True)
class NEOUST:
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


NEOUST = NEOUST()


@dataclass(slots=True, frozen=True)
class NEXO_BTC:
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


NEXO_BTC = NEXO_BTC()


@dataclass(slots=True, frozen=True)
class NEXO_USD:
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


NEXO_USD = NEXO_USD()


@dataclass(slots=True, frozen=True)
class NEXO_UST:
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


NEXO_UST = NEXO_UST()


@dataclass(slots=True, frozen=True)
class OCEAN_USD:
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


OCEAN_USD = OCEAN_USD()


@dataclass(slots=True, frozen=True)
class OCEAN_UST:
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


OCEAN_UST = OCEAN_UST()


@dataclass(slots=True, frozen=True)
class OMGBTC:
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


OMGBTC = OMGBTC()


@dataclass(slots=True, frozen=True)
class OMGETH:
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


OMGETH = OMGETH()


@dataclass(slots=True, frozen=True)
class OMGF0_USTF0:
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


OMGF0_USTF0 = OMGF0_USTF0()


@dataclass(slots=True, frozen=True)
class OMGUSD:
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


OMGUSD = OMGUSD()


@dataclass(slots=True, frozen=True)
class OMNUSD:
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


OMNUSD = OMNUSD()


@dataclass(slots=True, frozen=True)
class ONEUSD:
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


ONEUSD = ONEUSD()


@dataclass(slots=True, frozen=True)
class ONEUST:
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


ONEUST = ONEUST()


@dataclass(slots=True, frozen=True)
class OXYUSD:
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


OXYUSD = OXYUSD()


@dataclass(slots=True, frozen=True)
class PASUSD:
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


PASUSD = PASUSD()


@dataclass(slots=True, frozen=True)
class PAXUSD:
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


PAXUSD = PAXUSD()


@dataclass(slots=True, frozen=True)
class PAXUST:
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


PAXUST = PAXUST()


@dataclass(slots=True, frozen=True)
class PLANETS_USD:
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


PLANETS_USD = PLANETS_USD()


@dataclass(slots=True, frozen=True)
class PLANETS_UST:
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


PLANETS_UST = PLANETS_UST()


@dataclass(slots=True, frozen=True)
class PLUUSD:
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


PLUUSD = PLUUSD()


@dataclass(slots=True, frozen=True)
class PNKUSD:
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


PNKUSD = PNKUSD()


@dataclass(slots=True, frozen=True)
class POLC_USD:
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


POLC_USD = POLC_USD()


@dataclass(slots=True, frozen=True)
class POLC_UST:
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


POLC_UST = POLC_UST()


@dataclass(slots=True, frozen=True)
class POLIS_USD:
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


POLIS_USD = POLIS_USD()


@dataclass(slots=True, frozen=True)
class POLIS_UST:
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


POLIS_UST = POLIS_UST()


@dataclass(slots=True, frozen=True)
class QRDO_USD:
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


QRDO_USD = QRDO_USD()


@dataclass(slots=True, frozen=True)
class QRDO_UST:
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


QRDO_UST = QRDO_UST()


@dataclass(slots=True, frozen=True)
class QTFBTC:
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


QTFBTC = QTFBTC()


@dataclass(slots=True, frozen=True)
class QTFUSD:
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


QTFUSD = QTFUSD()


@dataclass(slots=True, frozen=True)
class QTMUSD:
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


QTMUSD = QTMUSD()


@dataclass(slots=True, frozen=True)
class RBTBTC:
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


RBTBTC = RBTBTC()


@dataclass(slots=True, frozen=True)
class RBTUSD:
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


RBTUSD = RBTUSD()


@dataclass(slots=True, frozen=True)
class REEF_USD:
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


REEF_USD = REEF_USD()


@dataclass(slots=True, frozen=True)
class REEF_UST:
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


REEF_UST = REEF_UST()


@dataclass(slots=True, frozen=True)
class REPUSD:
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


REPUSD = REPUSD()


@dataclass(slots=True, frozen=True)
class REQUSD:
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


REQUSD = REQUSD()


@dataclass(slots=True, frozen=True)
class RLYUSD:
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


RLYUSD = RLYUSD()


@dataclass(slots=True, frozen=True)
class RLYUST:
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


RLYUST = RLYUST()


@dataclass(slots=True, frozen=True)
class ROSE_USD:
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


ROSE_USD = ROSE_USD()


@dataclass(slots=True, frozen=True)
class RRTUSD:
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


RRTUSD = RRTUSD()


@dataclass(slots=True, frozen=True)
class SAND_USD:
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


SAND_USD = SAND_USD()


@dataclass(slots=True, frozen=True)
class SAND_UST:
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


SAND_UST = SAND_UST()


@dataclass(slots=True, frozen=True)
class SANDF0_USTF0:
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


SANDF0_USTF0 = SANDF0_USTF0()


@dataclass(slots=True, frozen=True)
class SENATE_USD:
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


SENATE_USD = SENATE_USD()


@dataclass(slots=True, frozen=True)
class SENATE_UST:
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


SENATE_UST = SENATE_UST()


@dataclass(slots=True, frozen=True)
class SGBUSD:
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


SGBUSD = SGBUSD()


@dataclass(slots=True, frozen=True)
class SGBUST:
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


SGBUST = SGBUST()


@dataclass(slots=True, frozen=True)
class SHFT_USD:
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


SHFT_USD = SHFT_USD()


@dataclass(slots=True, frozen=True)
class SHFT_UST:
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


SHFT_UST = SHFT_UST()


@dataclass(slots=True, frozen=True)
class SHIB_USD:
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


SHIB_USD = SHIB_USD()


@dataclass(slots=True, frozen=True)
class SHIB_UST:
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


SHIB_UST = SHIB_UST()


@dataclass(slots=True, frozen=True)
class SHIBF0_USTF0:
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


SHIBF0_USTF0 = SHIBF0_USTF0()


@dataclass(slots=True, frozen=True)
class SIDUS_USD:
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


SIDUS_USD = SIDUS_USD()


@dataclass(slots=True, frozen=True)
class SMRUSD:
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


SMRUSD = SMRUSD()


@dataclass(slots=True, frozen=True)
class SMRUST:
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


SMRUST = SMRUST()


@dataclass(slots=True, frozen=True)
class SNTUSD:
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


SNTUSD = SNTUSD()


@dataclass(slots=True, frozen=True)
class SNXUSD:
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


SNXUSD = SNXUSD()


@dataclass(slots=True, frozen=True)
class SNXUST:
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


SNXUST = SNXUST()


@dataclass(slots=True, frozen=True)
class SOLBTC:
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


SOLBTC = SOLBTC()


@dataclass(slots=True, frozen=True)
class SOLF0_BTCF0:
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


SOLF0_BTCF0 = SOLF0_BTCF0()


@dataclass(slots=True, frozen=True)
class SOLF0_USTF0:
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


SOLF0_USTF0 = SOLF0_USTF0()


@dataclass(slots=True, frozen=True)
class SOLUSD:
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


SOLUSD = SOLUSD()


@dataclass(slots=True, frozen=True)
class SOLUST:
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


SOLUST = SOLUST()


@dataclass(slots=True, frozen=True)
class SPELL_USD:
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


SPELL_USD = SPELL_USD()


@dataclass(slots=True, frozen=True)
class SPELL_UST:
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


SPELL_UST = SPELL_UST()


@dataclass(slots=True, frozen=True)
class STGF0_USTF0:
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


STGF0_USTF0 = STGF0_USTF0()


@dataclass(slots=True, frozen=True)
class STGUSD:
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


STGUSD = STGUSD()


@dataclass(slots=True, frozen=True)
class STGUST:
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


STGUST = STGUST()


@dataclass(slots=True, frozen=True)
class STJUSD:
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


STJUSD = STJUSD()


@dataclass(slots=True, frozen=True)
class SUKU_USD:
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


SUKU_USD = SUKU_USD()


@dataclass(slots=True, frozen=True)
class SUKU_UST:
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


SUKU_UST = SUKU_UST()


@dataclass(slots=True, frozen=True)
class SUNUSD:
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


SUNUSD = SUNUSD()


@dataclass(slots=True, frozen=True)
class SUNUST:
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


SUNUST = SUNUST()


@dataclass(slots=True, frozen=True)
class SUSHI_USD:
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


SUSHI_USD = SUSHI_USD()


@dataclass(slots=True, frozen=True)
class SUSHI_UST:
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


SUSHI_UST = SUSHI_UST()


@dataclass(slots=True, frozen=True)
class SUSHIF0_USTF0:
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


SUSHIF0_USTF0 = SUSHIF0_USTF0()


@dataclass(slots=True, frozen=True)
class SWEAT_USD:
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


SWEAT_USD = SWEAT_USD()


@dataclass(slots=True, frozen=True)
class SWEAT_UST:
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


SWEAT_UST = SWEAT_UST()


@dataclass(slots=True, frozen=True)
class SXXUSD:
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


SXXUSD = SXXUSD()


@dataclass(slots=True, frozen=True)
class SXXUST:
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


SXXUST = SXXUST()


@dataclass(slots=True, frozen=True)
class TERRAUST_USD:
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


TERRAUST_USD = TERRAUST_USD()


@dataclass(slots=True, frozen=True)
class TESTBTC_TESTUSD:
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


TESTBTC_TESTUSD = TESTBTC_TESTUSD()


@dataclass(slots=True, frozen=True)
class TESTBTC_TESTUSDT:
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


TESTBTC_TESTUSDT = TESTBTC_TESTUSDT()


@dataclass(slots=True, frozen=True)
class TESTBTCF0_TESTUSDTF0:
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


TESTBTCF0_TESTUSDTF0 = TESTBTCF0_TESTUSDTF0()


@dataclass(slots=True, frozen=True)
class THETA_USD:
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


THETA_USD = THETA_USD()


@dataclass(slots=True, frozen=True)
class THETA_UST:
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


THETA_UST = THETA_UST()


@dataclass(slots=True, frozen=True)
class TLOS_USD:
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


TLOS_USD = TLOS_USD()


@dataclass(slots=True, frozen=True)
class TRADE_USD:
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


TRADE_USD = TRADE_USD()


@dataclass(slots=True, frozen=True)
class TRADE_UST:
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


TRADE_UST = TRADE_UST()


@dataclass(slots=True, frozen=True)
class TREEB_USD:
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


TREEB_USD = TREEB_USD()


@dataclass(slots=True, frozen=True)
class TREEB_UST:
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


TREEB_UST = TREEB_UST()


@dataclass(slots=True, frozen=True)
class TRXBTC:
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


TRXBTC = TRXBTC()


@dataclass(slots=True, frozen=True)
class TRXETH:
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


TRXETH = TRXETH()


@dataclass(slots=True, frozen=True)
class TRXEUR:
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


TRXEUR = TRXEUR()


@dataclass(slots=True, frozen=True)
class TRXF0_USTF0:
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


TRXF0_USTF0 = TRXF0_USTF0()


@dataclass(slots=True, frozen=True)
class TRXUSD:
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


TRXUSD = TRXUSD()


@dataclass(slots=True, frozen=True)
class TRXUST:
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


TRXUST = TRXUST()


@dataclass(slots=True, frozen=True)
class TRYUST:
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


TRYUST = TRYUST()


@dataclass(slots=True, frozen=True)
class TSDUSD:
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


TSDUSD = TSDUSD()


@dataclass(slots=True, frozen=True)
class TSDUST:
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


TSDUST = TSDUST()


@dataclass(slots=True, frozen=True)
class UDCUSD:
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


UDCUSD = UDCUSD()


@dataclass(slots=True, frozen=True)
class UDCUST:
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


UDCUST = UDCUST()


@dataclass(slots=True, frozen=True)
class UNIF0_USTF0:
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


UNIF0_USTF0 = UNIF0_USTF0()


@dataclass(slots=True, frozen=True)
class UNIUSD:
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


UNIUSD = UNIUSD()


@dataclass(slots=True, frozen=True)
class UNIUST:
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


UNIUST = UNIUST()


@dataclass(slots=True, frozen=True)
class UOSBTC:
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


UOSBTC = UOSBTC()


@dataclass(slots=True, frozen=True)
class UOSUSD:
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


UOSUSD = UOSUSD()


@dataclass(slots=True, frozen=True)
class UST_CNHT:
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


UST_CNHT = UST_CNHT()


@dataclass(slots=True, frozen=True)
class UST_MXNT:
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


UST_MXNT = UST_MXNT()


@dataclass(slots=True, frozen=True)
class USTUSD:
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


USTUSD = USTUSD()


@dataclass(slots=True, frozen=True)
class UTKUSD:
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


UTKUSD = UTKUSD()


@dataclass(slots=True, frozen=True)
class VEEUSD:
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


VEEUSD = VEEUSD()


@dataclass(slots=True, frozen=True)
class VELO_USD:
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


VELO_USD = VELO_USD()


@dataclass(slots=True, frozen=True)
class VELO_UST:
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


VELO_UST = VELO_UST()


@dataclass(slots=True, frozen=True)
class VETBTC:
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


VETBTC = VETBTC()


@dataclass(slots=True, frozen=True)
class VETUSD:
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


VETUSD = VETUSD()


@dataclass(slots=True, frozen=True)
class VETUST:
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


VETUST = VETUST()


@dataclass(slots=True, frozen=True)
class VRAUSD:
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


VRAUSD = VRAUSD()


@dataclass(slots=True, frozen=True)
class VRAUST:
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


VRAUST = VRAUST()


@dataclass(slots=True, frozen=True)
class VSYUSD:
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


VSYUSD = VSYUSD()


@dataclass(slots=True, frozen=True)
class WAVES_USD:
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


WAVES_USD = WAVES_USD()


@dataclass(slots=True, frozen=True)
class WAVES_UST:
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


WAVES_UST = WAVES_UST()


@dataclass(slots=True, frozen=True)
class WAVESF0_USTF0:
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


WAVESF0_USTF0 = WAVESF0_USTF0()


@dataclass(slots=True, frozen=True)
class WAXUSD:
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


WAXUSD = WAXUSD()


@dataclass(slots=True, frozen=True)
class WBTBTC:
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


WBTBTC = WBTBTC()


@dataclass(slots=True, frozen=True)
class WBTUSD:
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


WBTUSD = WBTUSD()


@dataclass(slots=True, frozen=True)
class WILD_USD:
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


WILD_USD = WILD_USD()


@dataclass(slots=True, frozen=True)
class WILD_UST:
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


WILD_UST = WILD_UST()


@dataclass(slots=True, frozen=True)
class WNCG_USD:
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


WNCG_USD = WNCG_USD()


@dataclass(slots=True, frozen=True)
class WOOUSD:
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


WOOUSD = WOOUSD()


@dataclass(slots=True, frozen=True)
class WOOUST:
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


WOOUST = WOOUST()


@dataclass(slots=True, frozen=True)
class XAGF0_USTF0:
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


XAGF0_USTF0 = XAGF0_USTF0()


@dataclass(slots=True, frozen=True)
class XAUT_BTC:
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


XAUT_BTC = XAUT_BTC()


@dataclass(slots=True, frozen=True)
class XAUT_USD:
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


XAUT_USD = XAUT_USD()


@dataclass(slots=True, frozen=True)
class XAUT_UST:
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


XAUT_UST = XAUT_UST()


@dataclass(slots=True, frozen=True)
class XAUTF0_BTCF0:
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


XAUTF0_BTCF0 = XAUTF0_BTCF0()


@dataclass(slots=True, frozen=True)
class XAUTF0_USTF0:
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


XAUTF0_USTF0 = XAUTF0_USTF0()


@dataclass(slots=True, frozen=True)
class XCAD_USD:
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


XCAD_USD = XCAD_USD()


@dataclass(slots=True, frozen=True)
class XCNUSD:
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


XCNUSD = XCNUSD()


@dataclass(slots=True, frozen=True)
class XCNUST:
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


XCNUST = XCNUST()


@dataclass(slots=True, frozen=True)
class XDCUSD:
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


XDCUSD = XDCUSD()


@dataclass(slots=True, frozen=True)
class XDCUST:
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


XDCUST = XDCUST()


@dataclass(slots=True, frozen=True)
class XLMBTC:
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


XLMBTC = XLMBTC()


@dataclass(slots=True, frozen=True)
class XLMF0_USTF0:
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


XLMF0_USTF0 = XLMF0_USTF0()


@dataclass(slots=True, frozen=True)
class XLMUSD:
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


XLMUSD = XLMUSD()


@dataclass(slots=True, frozen=True)
class XLMUST:
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


XLMUST = XLMUST()


@dataclass(slots=True, frozen=True)
class XMRBTC:
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


XMRBTC = XMRBTC()


@dataclass(slots=True, frozen=True)
class XMRF0_USTF0:
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


XMRF0_USTF0 = XMRF0_USTF0()


@dataclass(slots=True, frozen=True)
class XMRUSD:
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


XMRUSD = XMRUSD()


@dataclass(slots=True, frozen=True)
class XMRUST:
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


XMRUST = XMRUST()


@dataclass(slots=True, frozen=True)
class XRAUSD:
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


XRAUSD = XRAUSD()


@dataclass(slots=True, frozen=True)
class XRDBTC:
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


XRDBTC = XRDBTC()


@dataclass(slots=True, frozen=True)
class XRDUSD:
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


XRDUSD = XRDUSD()


@dataclass(slots=True, frozen=True)
class XRPBTC:
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


XRPBTC = XRPBTC()


@dataclass(slots=True, frozen=True)
class XRPF0_BTCF0:
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


XRPF0_BTCF0 = XRPF0_BTCF0()


@dataclass(slots=True, frozen=True)
class XRPF0_USTF0:
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


XRPF0_USTF0 = XRPF0_USTF0()


@dataclass(slots=True, frozen=True)
class XRPUSD:
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


XRPUSD = XRPUSD()


@dataclass(slots=True, frozen=True)
class XRPUST:
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


XRPUST = XRPUST()


@dataclass(slots=True, frozen=True)
class XTZBTC:
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


XTZBTC = XTZBTC()


@dataclass(slots=True, frozen=True)
class XTZF0_USTF0:
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


XTZF0_USTF0 = XTZF0_USTF0()


@dataclass(slots=True, frozen=True)
class XTZUSD:
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


XTZUSD = XTZUSD()


@dataclass(slots=True, frozen=True)
class XTZUST:
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


XTZUST = XTZUST()


@dataclass(slots=True, frozen=True)
class XVGUSD:
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


XVGUSD = XVGUSD()


@dataclass(slots=True, frozen=True)
class YFIUSD:
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


YFIUSD = YFIUSD()


@dataclass(slots=True, frozen=True)
class YFIUST:
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


YFIUST = YFIUST()


@dataclass(slots=True, frozen=True)
class ZCNUSD:
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


ZCNUSD = ZCNUSD()


@dataclass(slots=True, frozen=True)
class ZECBTC:
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


ZECBTC = ZECBTC()


@dataclass(slots=True, frozen=True)
class ZECF0_USTF0:
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


ZECF0_USTF0 = ZECF0_USTF0()


@dataclass(slots=True, frozen=True)
class ZECUSD:
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


ZECUSD = ZECUSD()


@dataclass(slots=True, frozen=True)
class ZILBTC:
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


ZILBTC = ZILBTC()


@dataclass(slots=True, frozen=True)
class ZILUSD:
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


ZILUSD = ZILUSD()


@dataclass(slots=True, frozen=True)
class ZMTUSD:
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


ZMTUSD = ZMTUSD()


@dataclass(slots=True, frozen=True)
class ZMTUST:
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


ZMTUST = ZMTUST()


@dataclass(slots=True, frozen=True)
class ZRXBTC:
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


ZRXBTC = ZRXBTC()


@dataclass(slots=True, frozen=True)
class ZRXETH:
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


ZRXETH = ZRXETH()


@dataclass(slots=True, frozen=True)
class ZRXUSD:
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


ZRXUSD = ZRXUSD()


