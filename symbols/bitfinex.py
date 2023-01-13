from dataclasses import dataclass


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


@dataclass(slots=True)
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


