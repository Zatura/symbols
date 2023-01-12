from dataclasses import dataclass


@dataclass(slots=True)
class ZERO0_USD:
    name: str = "00-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "00-USD"

    def __str__(self):
        return "00-USD"

    def __call__(self):
        return "00-USD"


@dataclass(slots=True)
class ONEINCH_BTC:
    name: str = "1INCH-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "1INCH-BTC"

    def __str__(self):
        return "1INCH-BTC"

    def __call__(self):
        return "1INCH-BTC"


@dataclass(slots=True)
class ONEINCH_EUR:
    name: str = "1INCH-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "1INCH-EUR"

    def __str__(self):
        return "1INCH-EUR"

    def __call__(self):
        return "1INCH-EUR"


@dataclass(slots=True)
class ONEINCH_GBP:
    name: str = "1INCH-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "1INCH-GBP"

    def __str__(self):
        return "1INCH-GBP"

    def __call__(self):
        return "1INCH-GBP"


@dataclass(slots=True)
class ONEINCH_USD:
    name: str = "1INCH-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "1INCH-USD"

    def __str__(self):
        return "1INCH-USD"

    def __call__(self):
        return "1INCH-USD"


@dataclass(slots=True)
class AAVE_BTC:
    name: str = "AAVE-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AAVE-BTC"

    def __str__(self):
        return "AAVE-BTC"

    def __call__(self):
        return "AAVE-BTC"


@dataclass(slots=True)
class AAVE_EUR:
    name: str = "AAVE-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AAVE-EUR"

    def __str__(self):
        return "AAVE-EUR"

    def __call__(self):
        return "AAVE-EUR"


@dataclass(slots=True)
class AAVE_GBP:
    name: str = "AAVE-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AAVE-GBP"

    def __str__(self):
        return "AAVE-GBP"

    def __call__(self):
        return "AAVE-GBP"


@dataclass(slots=True)
class AAVE_USD:
    name: str = "AAVE-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AAVE-USD"

    def __str__(self):
        return "AAVE-USD"

    def __call__(self):
        return "AAVE-USD"


@dataclass(slots=True)
class ABT_USD:
    name: str = "ABT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ABT-USD"

    def __str__(self):
        return "ABT-USD"

    def __call__(self):
        return "ABT-USD"


@dataclass(slots=True)
class ACH_USD:
    name: str = "ACH-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ACH-USD"

    def __str__(self):
        return "ACH-USD"

    def __call__(self):
        return "ACH-USD"


@dataclass(slots=True)
class ACH_USDT:
    name: str = "ACH-USDT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ACH-USDT"

    def __str__(self):
        return "ACH-USDT"

    def __call__(self):
        return "ACH-USDT"


@dataclass(slots=True)
class ADA_BTC:
    name: str = "ADA-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ADA-BTC"

    def __str__(self):
        return "ADA-BTC"

    def __call__(self):
        return "ADA-BTC"


@dataclass(slots=True)
class ADA_ETH:
    name: str = "ADA-ETH"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ADA-ETH"

    def __str__(self):
        return "ADA-ETH"

    def __call__(self):
        return "ADA-ETH"


@dataclass(slots=True)
class ADA_EUR:
    name: str = "ADA-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ADA-EUR"

    def __str__(self):
        return "ADA-EUR"

    def __call__(self):
        return "ADA-EUR"


@dataclass(slots=True)
class ADA_GBP:
    name: str = "ADA-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ADA-GBP"

    def __str__(self):
        return "ADA-GBP"

    def __call__(self):
        return "ADA-GBP"


@dataclass(slots=True)
class ADA_USD:
    name: str = "ADA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ADA-USD"

    def __str__(self):
        return "ADA-USD"

    def __call__(self):
        return "ADA-USD"


@dataclass(slots=True)
class ADA_USDC:
    name: str = "ADA-USDC"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ADA-USDC"

    def __str__(self):
        return "ADA-USDC"

    def __call__(self):
        return "ADA-USDC"


@dataclass(slots=True)
class ADA_USDT:
    name: str = "ADA-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ADA-USDT"

    def __str__(self):
        return "ADA-USDT"

    def __call__(self):
        return "ADA-USDT"


@dataclass(slots=True)
class AERGO_USD:
    name: str = "AERGO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AERGO-USD"

    def __str__(self):
        return "AERGO-USD"

    def __call__(self):
        return "AERGO-USD"


@dataclass(slots=True)
class AGLD_USD:
    name: str = "AGLD-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AGLD-USD"

    def __str__(self):
        return "AGLD-USD"

    def __call__(self):
        return "AGLD-USD"


@dataclass(slots=True)
class AGLD_USDT:
    name: str = "AGLD-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AGLD-USDT"

    def __str__(self):
        return "AGLD-USDT"

    def __call__(self):
        return "AGLD-USDT"


@dataclass(slots=True)
class AIOZ_USD:
    name: str = "AIOZ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AIOZ-USD"

    def __str__(self):
        return "AIOZ-USD"

    def __call__(self):
        return "AIOZ-USD"


@dataclass(slots=True)
class AIOZ_USDT:
    name: str = "AIOZ-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AIOZ-USDT"

    def __str__(self):
        return "AIOZ-USDT"

    def __call__(self):
        return "AIOZ-USDT"


@dataclass(slots=True)
class ALCX_EUR:
    name: str = "ALCX-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ALCX-EUR"

    def __str__(self):
        return "ALCX-EUR"

    def __call__(self):
        return "ALCX-EUR"


@dataclass(slots=True)
class ALCX_USD:
    name: str = "ALCX-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ALCX-USD"

    def __str__(self):
        return "ALCX-USD"

    def __call__(self):
        return "ALCX-USD"


@dataclass(slots=True)
class ALCX_USDT:
    name: str = "ALCX-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ALCX-USDT"

    def __str__(self):
        return "ALCX-USDT"

    def __call__(self):
        return "ALCX-USDT"


@dataclass(slots=True)
class ALEPH_USD:
    name: str = "ALEPH-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ALEPH-USD"

    def __str__(self):
        return "ALEPH-USD"

    def __call__(self):
        return "ALEPH-USD"


@dataclass(slots=True)
class ALGO_BTC:
    name: str = "ALGO-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ALGO-BTC"

    def __str__(self):
        return "ALGO-BTC"

    def __call__(self):
        return "ALGO-BTC"


@dataclass(slots=True)
class ALGO_EUR:
    name: str = "ALGO-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ALGO-EUR"

    def __str__(self):
        return "ALGO-EUR"

    def __call__(self):
        return "ALGO-EUR"


@dataclass(slots=True)
class ALGO_GBP:
    name: str = "ALGO-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ALGO-GBP"

    def __str__(self):
        return "ALGO-GBP"

    def __call__(self):
        return "ALGO-GBP"


@dataclass(slots=True)
class ALGO_USD:
    name: str = "ALGO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ALGO-USD"

    def __str__(self):
        return "ALGO-USD"

    def __call__(self):
        return "ALGO-USD"


@dataclass(slots=True)
class ALICE_USD:
    name: str = "ALICE-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ALICE-USD"

    def __str__(self):
        return "ALICE-USD"

    def __call__(self):
        return "ALICE-USD"


@dataclass(slots=True)
class AMP_USD:
    name: str = "AMP-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AMP-USD"

    def __str__(self):
        return "AMP-USD"

    def __call__(self):
        return "AMP-USD"


@dataclass(slots=True)
class ANKR_BTC:
    name: str = "ANKR-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ANKR-BTC"

    def __str__(self):
        return "ANKR-BTC"

    def __call__(self):
        return "ANKR-BTC"


@dataclass(slots=True)
class ANKR_EUR:
    name: str = "ANKR-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ANKR-EUR"

    def __str__(self):
        return "ANKR-EUR"

    def __call__(self):
        return "ANKR-EUR"


@dataclass(slots=True)
class ANKR_GBP:
    name: str = "ANKR-GBP"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ANKR-GBP"

    def __str__(self):
        return "ANKR-GBP"

    def __call__(self):
        return "ANKR-GBP"


@dataclass(slots=True)
class ANKR_USD:
    name: str = "ANKR-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ANKR-USD"

    def __str__(self):
        return "ANKR-USD"

    def __call__(self):
        return "ANKR-USD"


@dataclass(slots=True)
class ANT_USD:
    name: str = "ANT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5.0
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ANT-USD"

    def __str__(self):
        return "ANT-USD"

    def __call__(self):
        return "ANT-USD"


@dataclass(slots=True)
class APE_EUR:
    name: str = "APE-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "APE-EUR"

    def __str__(self):
        return "APE-EUR"

    def __call__(self):
        return "APE-EUR"


@dataclass(slots=True)
class APE_USD:
    name: str = "APE-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "APE-USD"

    def __str__(self):
        return "APE-USD"

    def __call__(self):
        return "APE-USD"


@dataclass(slots=True)
class APE_USDT:
    name: str = "APE-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "APE-USDT"

    def __str__(self):
        return "APE-USDT"

    def __call__(self):
        return "APE-USDT"


@dataclass(slots=True)
class API3_USD:
    name: str = "API3-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "API3-USD"

    def __str__(self):
        return "API3-USD"

    def __call__(self):
        return "API3-USD"


@dataclass(slots=True)
class API3_USDT:
    name: str = "API3-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "API3-USDT"

    def __str__(self):
        return "API3-USDT"

    def __call__(self):
        return "API3-USDT"


@dataclass(slots=True)
class APT_USD:
    name: str = "APT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "APT-USD"

    def __str__(self):
        return "APT-USD"

    def __call__(self):
        return "APT-USD"


@dataclass(slots=True)
class APT_USDT:
    name: str = "APT-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "APT-USDT"

    def __str__(self):
        return "APT-USDT"

    def __call__(self):
        return "APT-USDT"


@dataclass(slots=True)
class ARPA_EUR:
    name: str = "ARPA-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ARPA-EUR"

    def __str__(self):
        return "ARPA-EUR"

    def __call__(self):
        return "ARPA-EUR"


@dataclass(slots=True)
class ARPA_USD:
    name: str = "ARPA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ARPA-USD"

    def __str__(self):
        return "ARPA-USD"

    def __call__(self):
        return "ARPA-USD"


@dataclass(slots=True)
class ARPA_USDT:
    name: str = "ARPA-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ARPA-USDT"

    def __str__(self):
        return "ARPA-USDT"

    def __call__(self):
        return "ARPA-USDT"


@dataclass(slots=True)
class ASM_USD:
    name: str = "ASM-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ASM-USD"

    def __str__(self):
        return "ASM-USD"

    def __call__(self):
        return "ASM-USD"


@dataclass(slots=True)
class ASM_USDT:
    name: str = "ASM-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ASM-USDT"

    def __str__(self):
        return "ASM-USDT"

    def __call__(self):
        return "ASM-USDT"


@dataclass(slots=True)
class AST_USD:
    name: str = "AST-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AST-USD"

    def __str__(self):
        return "AST-USD"

    def __call__(self):
        return "AST-USD"


@dataclass(slots=True)
class ATA_USD:
    name: str = "ATA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ATA-USD"

    def __str__(self):
        return "ATA-USD"

    def __call__(self):
        return "ATA-USD"


@dataclass(slots=True)
class ATA_USDT:
    name: str = "ATA-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ATA-USDT"

    def __str__(self):
        return "ATA-USDT"

    def __call__(self):
        return "ATA-USDT"


@dataclass(slots=True)
class ATOM_BTC:
    name: str = "ATOM-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ATOM-BTC"

    def __str__(self):
        return "ATOM-BTC"

    def __call__(self):
        return "ATOM-BTC"


@dataclass(slots=True)
class ATOM_EUR:
    name: str = "ATOM-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ATOM-EUR"

    def __str__(self):
        return "ATOM-EUR"

    def __call__(self):
        return "ATOM-EUR"


@dataclass(slots=True)
class ATOM_GBP:
    name: str = "ATOM-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ATOM-GBP"

    def __str__(self):
        return "ATOM-GBP"

    def __call__(self):
        return "ATOM-GBP"


@dataclass(slots=True)
class ATOM_USD:
    name: str = "ATOM-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ATOM-USD"

    def __str__(self):
        return "ATOM-USD"

    def __call__(self):
        return "ATOM-USD"


@dataclass(slots=True)
class ATOM_USDT:
    name: str = "ATOM-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ATOM-USDT"

    def __str__(self):
        return "ATOM-USDT"

    def __call__(self):
        return "ATOM-USDT"


@dataclass(slots=True)
class AUCTION_EUR:
    name: str = "AUCTION-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AUCTION-EUR"

    def __str__(self):
        return "AUCTION-EUR"

    def __call__(self):
        return "AUCTION-EUR"


@dataclass(slots=True)
class AUCTION_USD:
    name: str = "AUCTION-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AUCTION-USD"

    def __str__(self):
        return "AUCTION-USD"

    def __call__(self):
        return "AUCTION-USD"


@dataclass(slots=True)
class AUCTION_USDT:
    name: str = "AUCTION-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AUCTION-USDT"

    def __str__(self):
        return "AUCTION-USDT"

    def __call__(self):
        return "AUCTION-USDT"


@dataclass(slots=True)
class AURORA_USD:
    name: str = "AURORA-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AURORA-USD"

    def __str__(self):
        return "AURORA-USD"

    def __call__(self):
        return "AURORA-USD"


@dataclass(slots=True)
class AVAX_BTC:
    name: str = "AVAX-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AVAX-BTC"

    def __str__(self):
        return "AVAX-BTC"

    def __call__(self):
        return "AVAX-BTC"


@dataclass(slots=True)
class AVAX_EUR:
    name: str = "AVAX-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AVAX-EUR"

    def __str__(self):
        return "AVAX-EUR"

    def __call__(self):
        return "AVAX-EUR"


@dataclass(slots=True)
class AVAX_USD:
    name: str = "AVAX-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AVAX-USD"

    def __str__(self):
        return "AVAX-USD"

    def __call__(self):
        return "AVAX-USD"


@dataclass(slots=True)
class AVAX_USDT:
    name: str = "AVAX-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AVAX-USDT"

    def __str__(self):
        return "AVAX-USDT"

    def __call__(self):
        return "AVAX-USDT"


@dataclass(slots=True)
class AVT_USD:
    name: str = "AVT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AVT-USD"

    def __str__(self):
        return "AVT-USD"

    def __call__(self):
        return "AVT-USD"


@dataclass(slots=True)
class AXS_BTC:
    name: str = "AXS-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AXS-BTC"

    def __str__(self):
        return "AXS-BTC"

    def __call__(self):
        return "AXS-BTC"


@dataclass(slots=True)
class AXS_EUR:
    name: str = "AXS-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AXS-EUR"

    def __str__(self):
        return "AXS-EUR"

    def __call__(self):
        return "AXS-EUR"


@dataclass(slots=True)
class AXS_USD:
    name: str = "AXS-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AXS-USD"

    def __str__(self):
        return "AXS-USD"

    def __call__(self):
        return "AXS-USD"


@dataclass(slots=True)
class AXS_USDT:
    name: str = "AXS-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "AXS-USDT"

    def __str__(self):
        return "AXS-USDT"

    def __call__(self):
        return "AXS-USDT"


@dataclass(slots=True)
class BADGER_EUR:
    name: str = "BADGER-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BADGER-EUR"

    def __str__(self):
        return "BADGER-EUR"

    def __call__(self):
        return "BADGER-EUR"


@dataclass(slots=True)
class BADGER_USD:
    name: str = "BADGER-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BADGER-USD"

    def __str__(self):
        return "BADGER-USD"

    def __call__(self):
        return "BADGER-USD"


@dataclass(slots=True)
class BADGER_USDT:
    name: str = "BADGER-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BADGER-USDT"

    def __str__(self):
        return "BADGER-USDT"

    def __call__(self):
        return "BADGER-USDT"


@dataclass(slots=True)
class BAL_BTC:
    name: str = "BAL-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAL-BTC"

    def __str__(self):
        return "BAL-BTC"

    def __call__(self):
        return "BAL-BTC"


@dataclass(slots=True)
class BAL_USD:
    name: str = "BAL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAL-USD"

    def __str__(self):
        return "BAL-USD"

    def __call__(self):
        return "BAL-USD"


@dataclass(slots=True)
class BAND_BTC:
    name: str = "BAND-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAND-BTC"

    def __str__(self):
        return "BAND-BTC"

    def __call__(self):
        return "BAND-BTC"


@dataclass(slots=True)
class BAND_EUR:
    name: str = "BAND-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAND-EUR"

    def __str__(self):
        return "BAND-EUR"

    def __call__(self):
        return "BAND-EUR"


@dataclass(slots=True)
class BAND_GBP:
    name: str = "BAND-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAND-GBP"

    def __str__(self):
        return "BAND-GBP"

    def __call__(self):
        return "BAND-GBP"


@dataclass(slots=True)
class BAND_USD:
    name: str = "BAND-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAND-USD"

    def __str__(self):
        return "BAND-USD"

    def __call__(self):
        return "BAND-USD"


@dataclass(slots=True)
class BAT_BTC:
    name: str = "BAT-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAT-BTC"

    def __str__(self):
        return "BAT-BTC"

    def __call__(self):
        return "BAT-BTC"


@dataclass(slots=True)
class BAT_ETH:
    name: str = "BAT-ETH"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAT-ETH"

    def __str__(self):
        return "BAT-ETH"

    def __call__(self):
        return "BAT-ETH"


@dataclass(slots=True)
class BAT_EUR:
    name: str = "BAT-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAT-EUR"

    def __str__(self):
        return "BAT-EUR"

    def __call__(self):
        return "BAT-EUR"


@dataclass(slots=True)
class BAT_USD:
    name: str = "BAT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAT-USD"

    def __str__(self):
        return "BAT-USD"

    def __call__(self):
        return "BAT-USD"


@dataclass(slots=True)
class BAT_USDC:
    name: str = "BAT-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BAT-USDC"

    def __str__(self):
        return "BAT-USDC"

    def __call__(self):
        return "BAT-USDC"


@dataclass(slots=True)
class BCH_BTC:
    name: str = "BCH-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BCH-BTC"

    def __str__(self):
        return "BCH-BTC"

    def __call__(self):
        return "BCH-BTC"


@dataclass(slots=True)
class BCH_EUR:
    name: str = "BCH-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BCH-EUR"

    def __str__(self):
        return "BCH-EUR"

    def __call__(self):
        return "BCH-EUR"


@dataclass(slots=True)
class BCH_GBP:
    name: str = "BCH-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BCH-GBP"

    def __str__(self):
        return "BCH-GBP"

    def __call__(self):
        return "BCH-GBP"


@dataclass(slots=True)
class BCH_USD:
    name: str = "BCH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BCH-USD"

    def __str__(self):
        return "BCH-USD"

    def __call__(self):
        return "BCH-USD"


@dataclass(slots=True)
class BICO_EUR:
    name: str = "BICO-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BICO-EUR"

    def __str__(self):
        return "BICO-EUR"

    def __call__(self):
        return "BICO-EUR"


@dataclass(slots=True)
class BICO_USD:
    name: str = "BICO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BICO-USD"

    def __str__(self):
        return "BICO-USD"

    def __call__(self):
        return "BICO-USD"


@dataclass(slots=True)
class BICO_USDT:
    name: str = "BICO-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BICO-USDT"

    def __str__(self):
        return "BICO-USDT"

    def __call__(self):
        return "BICO-USDT"


@dataclass(slots=True)
class BIT_USD:
    name: str = "BIT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BIT-USD"

    def __str__(self):
        return "BIT-USD"

    def __call__(self):
        return "BIT-USD"


@dataclass(slots=True)
class BIT_USDT:
    name: str = "BIT-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BIT-USDT"

    def __str__(self):
        return "BIT-USDT"

    def __call__(self):
        return "BIT-USDT"


@dataclass(slots=True)
class BLZ_USD:
    name: str = "BLZ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BLZ-USD"

    def __str__(self):
        return "BLZ-USD"

    def __call__(self):
        return "BLZ-USD"


@dataclass(slots=True)
class BNT_BTC:
    name: str = "BNT-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BNT-BTC"

    def __str__(self):
        return "BNT-BTC"

    def __call__(self):
        return "BNT-BTC"


@dataclass(slots=True)
class BNT_EUR:
    name: str = "BNT-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BNT-EUR"

    def __str__(self):
        return "BNT-EUR"

    def __call__(self):
        return "BNT-EUR"


@dataclass(slots=True)
class BNT_GBP:
    name: str = "BNT-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BNT-GBP"

    def __str__(self):
        return "BNT-GBP"

    def __call__(self):
        return "BNT-GBP"


@dataclass(slots=True)
class BNT_USD:
    name: str = "BNT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BNT-USD"

    def __str__(self):
        return "BNT-USD"

    def __call__(self):
        return "BNT-USD"


@dataclass(slots=True)
class BOBA_USD:
    name: str = "BOBA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BOBA-USD"

    def __str__(self):
        return "BOBA-USD"

    def __call__(self):
        return "BOBA-USD"


@dataclass(slots=True)
class BOBA_USDT:
    name: str = "BOBA-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BOBA-USDT"

    def __str__(self):
        return "BOBA-USDT"

    def __call__(self):
        return "BOBA-USDT"


@dataclass(slots=True)
class BOND_USD:
    name: str = "BOND-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BOND-USD"

    def __str__(self):
        return "BOND-USD"

    def __call__(self):
        return "BOND-USD"


@dataclass(slots=True)
class BOND_USDT:
    name: str = "BOND-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BOND-USDT"

    def __str__(self):
        return "BOND-USDT"

    def __call__(self):
        return "BOND-USDT"


@dataclass(slots=True)
class BTC_EUR:
    name: str = "BTC-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTC-EUR"

    def __str__(self):
        return "BTC-EUR"

    def __call__(self):
        return "BTC-EUR"


@dataclass(slots=True)
class BTC_GBP:
    name: str = "BTC-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTC-GBP"

    def __str__(self):
        return "BTC-GBP"

    def __call__(self):
        return "BTC-GBP"


@dataclass(slots=True)
class BTC_USD:
    name: str = "BTC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTC-USD"

    def __str__(self):
        return "BTC-USD"

    def __call__(self):
        return "BTC-USD"


@dataclass(slots=True)
class BTC_USDC:
    name: str = "BTC-USDC"
    precision: int = 1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTC-USDC"

    def __str__(self):
        return "BTC-USDC"

    def __call__(self):
        return "BTC-USDC"


@dataclass(slots=True)
class BTC_USDT:
    name: str = "BTC-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTC-USDT"

    def __str__(self):
        return "BTC-USDT"

    def __call__(self):
        return "BTC-USDT"


@dataclass(slots=True)
class BTRST_BTC:
    name: str = "BTRST-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTRST-BTC"

    def __str__(self):
        return "BTRST-BTC"

    def __call__(self):
        return "BTRST-BTC"


@dataclass(slots=True)
class BTRST_EUR:
    name: str = "BTRST-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTRST-EUR"

    def __str__(self):
        return "BTRST-EUR"

    def __call__(self):
        return "BTRST-EUR"


@dataclass(slots=True)
class BTRST_GBP:
    name: str = "BTRST-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTRST-GBP"

    def __str__(self):
        return "BTRST-GBP"

    def __call__(self):
        return "BTRST-GBP"


@dataclass(slots=True)
class BTRST_USD:
    name: str = "BTRST-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTRST-USD"

    def __str__(self):
        return "BTRST-USD"

    def __call__(self):
        return "BTRST-USD"


@dataclass(slots=True)
class BTRST_USDT:
    name: str = "BTRST-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BTRST-USDT"

    def __str__(self):
        return "BTRST-USDT"

    def __call__(self):
        return "BTRST-USDT"


@dataclass(slots=True)
class BUSD_USD:
    name: str = "BUSD-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "BUSD-USD"

    def __str__(self):
        return "BUSD-USD"

    def __call__(self):
        return "BUSD-USD"


@dataclass(slots=True)
class C98_USD:
    name: str = "C98-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "C98-USD"

    def __str__(self):
        return "C98-USD"

    def __call__(self):
        return "C98-USD"


@dataclass(slots=True)
class C98_USDT:
    name: str = "C98-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "C98-USDT"

    def __str__(self):
        return "C98-USDT"

    def __call__(self):
        return "C98-USDT"


@dataclass(slots=True)
class CBETH_ETH:
    name: str = "CBETH-ETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.002
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CBETH-ETH"

    def __str__(self):
        return "CBETH-ETH"

    def __call__(self):
        return "CBETH-ETH"


@dataclass(slots=True)
class CBETH_USD:
    name: str = "CBETH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CBETH-USD"

    def __str__(self):
        return "CBETH-USD"

    def __call__(self):
        return "CBETH-USD"


@dataclass(slots=True)
class CELR_USD:
    name: str = "CELR-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CELR-USD"

    def __str__(self):
        return "CELR-USD"

    def __call__(self):
        return "CELR-USD"


@dataclass(slots=True)
class CGLD_BTC:
    name: str = "CGLD-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CGLD-BTC"

    def __str__(self):
        return "CGLD-BTC"

    def __call__(self):
        return "CGLD-BTC"


@dataclass(slots=True)
class CGLD_EUR:
    name: str = "CGLD-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CGLD-EUR"

    def __str__(self):
        return "CGLD-EUR"

    def __call__(self):
        return "CGLD-EUR"


@dataclass(slots=True)
class CGLD_GBP:
    name: str = "CGLD-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CGLD-GBP"

    def __str__(self):
        return "CGLD-GBP"

    def __call__(self):
        return "CGLD-GBP"


@dataclass(slots=True)
class CGLD_USD:
    name: str = "CGLD-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CGLD-USD"

    def __str__(self):
        return "CGLD-USD"

    def __call__(self):
        return "CGLD-USD"


@dataclass(slots=True)
class CHZ_EUR:
    name: str = "CHZ-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CHZ-EUR"

    def __str__(self):
        return "CHZ-EUR"

    def __call__(self):
        return "CHZ-EUR"


@dataclass(slots=True)
class CHZ_GBP:
    name: str = "CHZ-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CHZ-GBP"

    def __str__(self):
        return "CHZ-GBP"

    def __call__(self):
        return "CHZ-GBP"


@dataclass(slots=True)
class CHZ_USD:
    name: str = "CHZ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CHZ-USD"

    def __str__(self):
        return "CHZ-USD"

    def __call__(self):
        return "CHZ-USD"


@dataclass(slots=True)
class CHZ_USDT:
    name: str = "CHZ-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CHZ-USDT"

    def __str__(self):
        return "CHZ-USDT"

    def __call__(self):
        return "CHZ-USDT"


@dataclass(slots=True)
class CLV_EUR:
    name: str = "CLV-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CLV-EUR"

    def __str__(self):
        return "CLV-EUR"

    def __call__(self):
        return "CLV-EUR"


@dataclass(slots=True)
class CLV_GBP:
    name: str = "CLV-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CLV-GBP"

    def __str__(self):
        return "CLV-GBP"

    def __call__(self):
        return "CLV-GBP"


@dataclass(slots=True)
class CLV_USD:
    name: str = "CLV-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CLV-USD"

    def __str__(self):
        return "CLV-USD"

    def __call__(self):
        return "CLV-USD"


@dataclass(slots=True)
class CLV_USDT:
    name: str = "CLV-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CLV-USDT"

    def __str__(self):
        return "CLV-USDT"

    def __call__(self):
        return "CLV-USDT"


@dataclass(slots=True)
class COMP_BTC:
    name: str = "COMP-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "COMP-BTC"

    def __str__(self):
        return "COMP-BTC"

    def __call__(self):
        return "COMP-BTC"


@dataclass(slots=True)
class COMP_USD:
    name: str = "COMP-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "COMP-USD"

    def __str__(self):
        return "COMP-USD"

    def __call__(self):
        return "COMP-USD"


@dataclass(slots=True)
class COTI_USD:
    name: str = "COTI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "COTI-USD"

    def __str__(self):
        return "COTI-USD"

    def __call__(self):
        return "COTI-USD"


@dataclass(slots=True)
class COVAL_USD:
    name: str = "COVAL-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "COVAL-USD"

    def __str__(self):
        return "COVAL-USD"

    def __call__(self):
        return "COVAL-USD"


@dataclass(slots=True)
class COVAL_USDT:
    name: str = "COVAL-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "COVAL-USDT"

    def __str__(self):
        return "COVAL-USDT"

    def __call__(self):
        return "COVAL-USDT"


@dataclass(slots=True)
class CRO_EUR:
    name: str = "CRO-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CRO-EUR"

    def __str__(self):
        return "CRO-EUR"

    def __call__(self):
        return "CRO-EUR"


@dataclass(slots=True)
class CRO_USD:
    name: str = "CRO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CRO-USD"

    def __str__(self):
        return "CRO-USD"

    def __call__(self):
        return "CRO-USD"


@dataclass(slots=True)
class CRO_USDT:
    name: str = "CRO-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CRO-USDT"

    def __str__(self):
        return "CRO-USDT"

    def __call__(self):
        return "CRO-USDT"


@dataclass(slots=True)
class CRPT_USD:
    name: str = "CRPT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CRPT-USD"

    def __str__(self):
        return "CRPT-USD"

    def __call__(self):
        return "CRPT-USD"


@dataclass(slots=True)
class CRV_BTC:
    name: str = "CRV-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CRV-BTC"

    def __str__(self):
        return "CRV-BTC"

    def __call__(self):
        return "CRV-BTC"


@dataclass(slots=True)
class CRV_EUR:
    name: str = "CRV-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CRV-EUR"

    def __str__(self):
        return "CRV-EUR"

    def __call__(self):
        return "CRV-EUR"


@dataclass(slots=True)
class CRV_GBP:
    name: str = "CRV-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CRV-GBP"

    def __str__(self):
        return "CRV-GBP"

    def __call__(self):
        return "CRV-GBP"


@dataclass(slots=True)
class CRV_USD:
    name: str = "CRV-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CRV-USD"

    def __str__(self):
        return "CRV-USD"

    def __call__(self):
        return "CRV-USD"


@dataclass(slots=True)
class CTSI_BTC:
    name: str = "CTSI-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CTSI-BTC"

    def __str__(self):
        return "CTSI-BTC"

    def __call__(self):
        return "CTSI-BTC"


@dataclass(slots=True)
class CTSI_USD:
    name: str = "CTSI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CTSI-USD"

    def __str__(self):
        return "CTSI-USD"

    def __call__(self):
        return "CTSI-USD"


@dataclass(slots=True)
class CTX_EUR:
    name: str = "CTX-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CTX-EUR"

    def __str__(self):
        return "CTX-EUR"

    def __call__(self):
        return "CTX-EUR"


@dataclass(slots=True)
class CTX_USD:
    name: str = "CTX-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CTX-USD"

    def __str__(self):
        return "CTX-USD"

    def __call__(self):
        return "CTX-USD"


@dataclass(slots=True)
class CTX_USDT:
    name: str = "CTX-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CTX-USDT"

    def __str__(self):
        return "CTX-USDT"

    def __call__(self):
        return "CTX-USDT"


@dataclass(slots=True)
class CVC_USD:
    name: str = "CVC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CVC-USD"

    def __str__(self):
        return "CVC-USD"

    def __call__(self):
        return "CVC-USD"


@dataclass(slots=True)
class CVC_USDC:
    name: str = "CVC-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CVC-USDC"

    def __str__(self):
        return "CVC-USDC"

    def __call__(self):
        return "CVC-USDC"


@dataclass(slots=True)
class CVX_USD:
    name: str = "CVX-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "CVX-USD"

    def __str__(self):
        return "CVX-USD"

    def __call__(self):
        return "CVX-USD"


@dataclass(slots=True)
class DAI_USD:
    name: str = "DAI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DAI-USD"

    def __str__(self):
        return "DAI-USD"

    def __call__(self):
        return "DAI-USD"


@dataclass(slots=True)
class DAI_USDC:
    name: str = "DAI-USDC"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DAI-USDC"

    def __str__(self):
        return "DAI-USDC"

    def __call__(self):
        return "DAI-USDC"


@dataclass(slots=True)
class DAR_USD:
    name: str = "DAR-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DAR-USD"

    def __str__(self):
        return "DAR-USD"

    def __call__(self):
        return "DAR-USD"


@dataclass(slots=True)
class DASH_BTC:
    name: str = "DASH-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DASH-BTC"

    def __str__(self):
        return "DASH-BTC"

    def __call__(self):
        return "DASH-BTC"


@dataclass(slots=True)
class DASH_USD:
    name: str = "DASH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DASH-USD"

    def __str__(self):
        return "DASH-USD"

    def __call__(self):
        return "DASH-USD"


@dataclass(slots=True)
class DDX_EUR:
    name: str = "DDX-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DDX-EUR"

    def __str__(self):
        return "DDX-EUR"

    def __call__(self):
        return "DDX-EUR"


@dataclass(slots=True)
class DDX_USD:
    name: str = "DDX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DDX-USD"

    def __str__(self):
        return "DDX-USD"

    def __call__(self):
        return "DDX-USD"


@dataclass(slots=True)
class DDX_USDT:
    name: str = "DDX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DDX-USDT"

    def __str__(self):
        return "DDX-USDT"

    def __call__(self):
        return "DDX-USDT"


@dataclass(slots=True)
class DESO_EUR:
    name: str = "DESO-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DESO-EUR"

    def __str__(self):
        return "DESO-EUR"

    def __call__(self):
        return "DESO-EUR"


@dataclass(slots=True)
class DESO_USD:
    name: str = "DESO-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DESO-USD"

    def __str__(self):
        return "DESO-USD"

    def __call__(self):
        return "DESO-USD"


@dataclass(slots=True)
class DESO_USDT:
    name: str = "DESO-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DESO-USDT"

    def __str__(self):
        return "DESO-USDT"

    def __call__(self):
        return "DESO-USDT"


@dataclass(slots=True)
class DEXT_USD:
    name: str = "DEXT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DEXT-USD"

    def __str__(self):
        return "DEXT-USD"

    def __call__(self):
        return "DEXT-USD"


@dataclass(slots=True)
class DIA_EUR:
    name: str = "DIA-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DIA-EUR"

    def __str__(self):
        return "DIA-EUR"

    def __call__(self):
        return "DIA-EUR"


@dataclass(slots=True)
class DIA_USD:
    name: str = "DIA-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DIA-USD"

    def __str__(self):
        return "DIA-USD"

    def __call__(self):
        return "DIA-USD"


@dataclass(slots=True)
class DIA_USDT:
    name: str = "DIA-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DIA-USDT"

    def __str__(self):
        return "DIA-USDT"

    def __call__(self):
        return "DIA-USDT"


@dataclass(slots=True)
class DNT_USD:
    name: str = "DNT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DNT-USD"

    def __str__(self):
        return "DNT-USD"

    def __call__(self):
        return "DNT-USD"


@dataclass(slots=True)
class DNT_USDC:
    name: str = "DNT-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DNT-USDC"

    def __str__(self):
        return "DNT-USDC"

    def __call__(self):
        return "DNT-USDC"


@dataclass(slots=True)
class DOGE_BTC:
    name: str = "DOGE-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOGE-BTC"

    def __str__(self):
        return "DOGE-BTC"

    def __call__(self):
        return "DOGE-BTC"


@dataclass(slots=True)
class DOGE_EUR:
    name: str = "DOGE-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOGE-EUR"

    def __str__(self):
        return "DOGE-EUR"

    def __call__(self):
        return "DOGE-EUR"


@dataclass(slots=True)
class DOGE_GBP:
    name: str = "DOGE-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOGE-GBP"

    def __str__(self):
        return "DOGE-GBP"

    def __call__(self):
        return "DOGE-GBP"


@dataclass(slots=True)
class DOGE_USD:
    name: str = "DOGE-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOGE-USD"

    def __str__(self):
        return "DOGE-USD"

    def __call__(self):
        return "DOGE-USD"


@dataclass(slots=True)
class DOGE_USDT:
    name: str = "DOGE-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOGE-USDT"

    def __str__(self):
        return "DOGE-USDT"

    def __call__(self):
        return "DOGE-USDT"


@dataclass(slots=True)
class DOT_BTC:
    name: str = "DOT-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOT-BTC"

    def __str__(self):
        return "DOT-BTC"

    def __call__(self):
        return "DOT-BTC"


@dataclass(slots=True)
class DOT_EUR:
    name: str = "DOT-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOT-EUR"

    def __str__(self):
        return "DOT-EUR"

    def __call__(self):
        return "DOT-EUR"


@dataclass(slots=True)
class DOT_GBP:
    name: str = "DOT-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOT-GBP"

    def __str__(self):
        return "DOT-GBP"

    def __call__(self):
        return "DOT-GBP"


@dataclass(slots=True)
class DOT_USD:
    name: str = "DOT-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOT-USD"

    def __str__(self):
        return "DOT-USD"

    def __call__(self):
        return "DOT-USD"


@dataclass(slots=True)
class DOT_USDT:
    name: str = "DOT-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DOT-USDT"

    def __str__(self):
        return "DOT-USDT"

    def __call__(self):
        return "DOT-USDT"


@dataclass(slots=True)
class DREP_USD:
    name: str = "DREP-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DREP-USD"

    def __str__(self):
        return "DREP-USD"

    def __call__(self):
        return "DREP-USD"


@dataclass(slots=True)
class DREP_USDT:
    name: str = "DREP-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DREP-USDT"

    def __str__(self):
        return "DREP-USDT"

    def __call__(self):
        return "DREP-USDT"


@dataclass(slots=True)
class DYP_USD:
    name: str = "DYP-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DYP-USD"

    def __str__(self):
        return "DYP-USD"

    def __call__(self):
        return "DYP-USD"


@dataclass(slots=True)
class DYP_USDT:
    name: str = "DYP-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "DYP-USDT"

    def __str__(self):
        return "DYP-USDT"

    def __call__(self):
        return "DYP-USDT"


@dataclass(slots=True)
class EGLD_USD:
    name: str = "EGLD-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "EGLD-USD"

    def __str__(self):
        return "EGLD-USD"

    def __call__(self):
        return "EGLD-USD"


@dataclass(slots=True)
class ELA_USD:
    name: str = "ELA-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ELA-USD"

    def __str__(self):
        return "ELA-USD"

    def __call__(self):
        return "ELA-USD"


@dataclass(slots=True)
class ELA_USDT:
    name: str = "ELA-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ELA-USDT"

    def __str__(self):
        return "ELA-USDT"

    def __call__(self):
        return "ELA-USDT"


@dataclass(slots=True)
class ENJ_BTC:
    name: str = "ENJ-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ENJ-BTC"

    def __str__(self):
        return "ENJ-BTC"

    def __call__(self):
        return "ENJ-BTC"


@dataclass(slots=True)
class ENJ_USD:
    name: str = "ENJ-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ENJ-USD"

    def __str__(self):
        return "ENJ-USD"

    def __call__(self):
        return "ENJ-USD"


@dataclass(slots=True)
class ENJ_USDT:
    name: str = "ENJ-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ENJ-USDT"

    def __str__(self):
        return "ENJ-USDT"

    def __call__(self):
        return "ENJ-USDT"


@dataclass(slots=True)
class ENS_EUR:
    name: str = "ENS-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ENS-EUR"

    def __str__(self):
        return "ENS-EUR"

    def __call__(self):
        return "ENS-EUR"


@dataclass(slots=True)
class ENS_USD:
    name: str = "ENS-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ENS-USD"

    def __str__(self):
        return "ENS-USD"

    def __call__(self):
        return "ENS-USD"


@dataclass(slots=True)
class ENS_USDT:
    name: str = "ENS-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ENS-USDT"

    def __str__(self):
        return "ENS-USDT"

    def __call__(self):
        return "ENS-USDT"


@dataclass(slots=True)
class EOS_BTC:
    name: str = "EOS-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "EOS-BTC"

    def __str__(self):
        return "EOS-BTC"

    def __call__(self):
        return "EOS-BTC"


@dataclass(slots=True)
class EOS_EUR:
    name: str = "EOS-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "EOS-EUR"

    def __str__(self):
        return "EOS-EUR"

    def __call__(self):
        return "EOS-EUR"


@dataclass(slots=True)
class EOS_USD:
    name: str = "EOS-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "EOS-USD"

    def __str__(self):
        return "EOS-USD"

    def __call__(self):
        return "EOS-USD"


@dataclass(slots=True)
class ERN_EUR:
    name: str = "ERN-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ERN-EUR"

    def __str__(self):
        return "ERN-EUR"

    def __call__(self):
        return "ERN-EUR"


@dataclass(slots=True)
class ERN_USD:
    name: str = "ERN-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ERN-USD"

    def __str__(self):
        return "ERN-USD"

    def __call__(self):
        return "ERN-USD"


@dataclass(slots=True)
class ERN_USDT:
    name: str = "ERN-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ERN-USDT"

    def __str__(self):
        return "ERN-USDT"

    def __call__(self):
        return "ERN-USDT"


@dataclass(slots=True)
class ETC_BTC:
    name: str = "ETC-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETC-BTC"

    def __str__(self):
        return "ETC-BTC"

    def __call__(self):
        return "ETC-BTC"


@dataclass(slots=True)
class ETC_EUR:
    name: str = "ETC-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETC-EUR"

    def __str__(self):
        return "ETC-EUR"

    def __call__(self):
        return "ETC-EUR"


@dataclass(slots=True)
class ETC_GBP:
    name: str = "ETC-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETC-GBP"

    def __str__(self):
        return "ETC-GBP"

    def __call__(self):
        return "ETC-GBP"


@dataclass(slots=True)
class ETC_USD:
    name: str = "ETC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETC-USD"

    def __str__(self):
        return "ETC-USD"

    def __call__(self):
        return "ETC-USD"


@dataclass(slots=True)
class ETH_BTC:
    name: str = "ETH-BTC"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETH-BTC"

    def __str__(self):
        return "ETH-BTC"

    def __call__(self):
        return "ETH-BTC"


@dataclass(slots=True)
class ETH_DAI:
    name: str = "ETH-DAI"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETH-DAI"

    def __str__(self):
        return "ETH-DAI"

    def __call__(self):
        return "ETH-DAI"


@dataclass(slots=True)
class ETH_EUR:
    name: str = "ETH-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETH-EUR"

    def __str__(self):
        return "ETH-EUR"

    def __call__(self):
        return "ETH-EUR"


@dataclass(slots=True)
class ETH_GBP:
    name: str = "ETH-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETH-GBP"

    def __str__(self):
        return "ETH-GBP"

    def __call__(self):
        return "ETH-GBP"


@dataclass(slots=True)
class ETH_USD:
    name: str = "ETH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETH-USD"

    def __str__(self):
        return "ETH-USD"

    def __call__(self):
        return "ETH-USD"


@dataclass(slots=True)
class ETH_USDC:
    name: str = "ETH-USDC"
    precision: int = 1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETH-USDC"

    def __str__(self):
        return "ETH-USDC"

    def __call__(self):
        return "ETH-USDC"


@dataclass(slots=True)
class ETH_USDT:
    name: str = "ETH-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ETH-USDT"

    def __str__(self):
        return "ETH-USDT"

    def __call__(self):
        return "ETH-USDT"


@dataclass(slots=True)
class FARM_USD:
    name: str = "FARM-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FARM-USD"

    def __str__(self):
        return "FARM-USD"

    def __call__(self):
        return "FARM-USD"


@dataclass(slots=True)
class FARM_USDT:
    name: str = "FARM-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FARM-USDT"

    def __str__(self):
        return "FARM-USDT"

    def __call__(self):
        return "FARM-USDT"


@dataclass(slots=True)
class FET_USD:
    name: str = "FET-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FET-USD"

    def __str__(self):
        return "FET-USD"

    def __call__(self):
        return "FET-USD"


@dataclass(slots=True)
class FET_USDT:
    name: str = "FET-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FET-USDT"

    def __str__(self):
        return "FET-USDT"

    def __call__(self):
        return "FET-USDT"


@dataclass(slots=True)
class FIDA_EUR:
    name: str = "FIDA-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FIDA-EUR"

    def __str__(self):
        return "FIDA-EUR"

    def __call__(self):
        return "FIDA-EUR"


@dataclass(slots=True)
class FIDA_USD:
    name: str = "FIDA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FIDA-USD"

    def __str__(self):
        return "FIDA-USD"

    def __call__(self):
        return "FIDA-USD"


@dataclass(slots=True)
class FIDA_USDT:
    name: str = "FIDA-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FIDA-USDT"

    def __str__(self):
        return "FIDA-USDT"

    def __call__(self):
        return "FIDA-USDT"


@dataclass(slots=True)
class FIL_BTC:
    name: str = "FIL-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FIL-BTC"

    def __str__(self):
        return "FIL-BTC"

    def __call__(self):
        return "FIL-BTC"


@dataclass(slots=True)
class FIL_EUR:
    name: str = "FIL-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FIL-EUR"

    def __str__(self):
        return "FIL-EUR"

    def __call__(self):
        return "FIL-EUR"


@dataclass(slots=True)
class FIL_GBP:
    name: str = "FIL-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FIL-GBP"

    def __str__(self):
        return "FIL-GBP"

    def __call__(self):
        return "FIL-GBP"


@dataclass(slots=True)
class FIL_USD:
    name: str = "FIL-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FIL-USD"

    def __str__(self):
        return "FIL-USD"

    def __call__(self):
        return "FIL-USD"


@dataclass(slots=True)
class FIS_USD:
    name: str = "FIS-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FIS-USD"

    def __str__(self):
        return "FIS-USD"

    def __call__(self):
        return "FIS-USD"


@dataclass(slots=True)
class FIS_USDT:
    name: str = "FIS-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FIS-USDT"

    def __str__(self):
        return "FIS-USDT"

    def __call__(self):
        return "FIS-USDT"


@dataclass(slots=True)
class FLOW_USD:
    name: str = "FLOW-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FLOW-USD"

    def __str__(self):
        return "FLOW-USD"

    def __call__(self):
        return "FLOW-USD"


@dataclass(slots=True)
class FLOW_USDT:
    name: str = "FLOW-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FLOW-USDT"

    def __str__(self):
        return "FLOW-USDT"

    def __call__(self):
        return "FLOW-USDT"


@dataclass(slots=True)
class FORT_USD:
    name: str = "FORT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FORT-USD"

    def __str__(self):
        return "FORT-USD"

    def __call__(self):
        return "FORT-USD"


@dataclass(slots=True)
class FORT_USDT:
    name: str = "FORT-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FORT-USDT"

    def __str__(self):
        return "FORT-USDT"

    def __call__(self):
        return "FORT-USDT"


@dataclass(slots=True)
class FORTH_BTC:
    name: str = "FORTH-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FORTH-BTC"

    def __str__(self):
        return "FORTH-BTC"

    def __call__(self):
        return "FORTH-BTC"


@dataclass(slots=True)
class FORTH_EUR:
    name: str = "FORTH-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FORTH-EUR"

    def __str__(self):
        return "FORTH-EUR"

    def __call__(self):
        return "FORTH-EUR"


@dataclass(slots=True)
class FORTH_GBP:
    name: str = "FORTH-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FORTH-GBP"

    def __str__(self):
        return "FORTH-GBP"

    def __call__(self):
        return "FORTH-GBP"


@dataclass(slots=True)
class FORTH_USD:
    name: str = "FORTH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FORTH-USD"

    def __str__(self):
        return "FORTH-USD"

    def __call__(self):
        return "FORTH-USD"


@dataclass(slots=True)
class FOX_USD:
    name: str = "FOX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FOX-USD"

    def __str__(self):
        return "FOX-USD"

    def __call__(self):
        return "FOX-USD"


@dataclass(slots=True)
class FOX_USDT:
    name: str = "FOX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FOX-USDT"

    def __str__(self):
        return "FOX-USDT"

    def __call__(self):
        return "FOX-USDT"


@dataclass(slots=True)
class FX_USD:
    name: str = "FX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "FX-USD"

    def __str__(self):
        return "FX-USD"

    def __call__(self):
        return "FX-USD"


@dataclass(slots=True)
class GAL_USD:
    name: str = "GAL-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GAL-USD"

    def __str__(self):
        return "GAL-USD"

    def __call__(self):
        return "GAL-USD"


@dataclass(slots=True)
class GAL_USDT:
    name: str = "GAL-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GAL-USDT"

    def __str__(self):
        return "GAL-USDT"

    def __call__(self):
        return "GAL-USDT"


@dataclass(slots=True)
class GALA_EUR:
    name: str = "GALA-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GALA-EUR"

    def __str__(self):
        return "GALA-EUR"

    def __call__(self):
        return "GALA-EUR"


@dataclass(slots=True)
class GALA_USD:
    name: str = "GALA-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GALA-USD"

    def __str__(self):
        return "GALA-USD"

    def __call__(self):
        return "GALA-USD"


@dataclass(slots=True)
class GALA_USDT:
    name: str = "GALA-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GALA-USDT"

    def __str__(self):
        return "GALA-USDT"

    def __call__(self):
        return "GALA-USDT"


@dataclass(slots=True)
class GFI_USD:
    name: str = "GFI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GFI-USD"

    def __str__(self):
        return "GFI-USD"

    def __call__(self):
        return "GFI-USD"


@dataclass(slots=True)
class GHST_USD:
    name: str = "GHST-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GHST-USD"

    def __str__(self):
        return "GHST-USD"

    def __call__(self):
        return "GHST-USD"


@dataclass(slots=True)
class GLM_USD:
    name: str = "GLM-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GLM-USD"

    def __str__(self):
        return "GLM-USD"

    def __call__(self):
        return "GLM-USD"


@dataclass(slots=True)
class GMT_USD:
    name: str = "GMT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GMT-USD"

    def __str__(self):
        return "GMT-USD"

    def __call__(self):
        return "GMT-USD"


@dataclass(slots=True)
class GMT_USDT:
    name: str = "GMT-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GMT-USDT"

    def __str__(self):
        return "GMT-USDT"

    def __call__(self):
        return "GMT-USDT"


@dataclass(slots=True)
class GNO_USD:
    name: str = "GNO-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GNO-USD"

    def __str__(self):
        return "GNO-USD"

    def __call__(self):
        return "GNO-USD"


@dataclass(slots=True)
class GNO_USDT:
    name: str = "GNO-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GNO-USDT"

    def __str__(self):
        return "GNO-USDT"

    def __call__(self):
        return "GNO-USDT"


@dataclass(slots=True)
class GNT_USDC:
    name: str = "GNT-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GNT-USDC"

    def __str__(self):
        return "GNT-USDC"

    def __call__(self):
        return "GNT-USDC"


@dataclass(slots=True)
class GODS_USD:
    name: str = "GODS-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GODS-USD"

    def __str__(self):
        return "GODS-USD"

    def __call__(self):
        return "GODS-USD"


@dataclass(slots=True)
class GRT_BTC:
    name: str = "GRT-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GRT-BTC"

    def __str__(self):
        return "GRT-BTC"

    def __call__(self):
        return "GRT-BTC"


@dataclass(slots=True)
class GRT_EUR:
    name: str = "GRT-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GRT-EUR"

    def __str__(self):
        return "GRT-EUR"

    def __call__(self):
        return "GRT-EUR"


@dataclass(slots=True)
class GRT_GBP:
    name: str = "GRT-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GRT-GBP"

    def __str__(self):
        return "GRT-GBP"

    def __call__(self):
        return "GRT-GBP"


@dataclass(slots=True)
class GRT_USD:
    name: str = "GRT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GRT-USD"

    def __str__(self):
        return "GRT-USD"

    def __call__(self):
        return "GRT-USD"


@dataclass(slots=True)
class GST_USD:
    name: str = "GST-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GST-USD"

    def __str__(self):
        return "GST-USD"

    def __call__(self):
        return "GST-USD"


@dataclass(slots=True)
class GTC_USD:
    name: str = "GTC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GTC-USD"

    def __str__(self):
        return "GTC-USD"

    def __call__(self):
        return "GTC-USD"


@dataclass(slots=True)
class GUSD_USD:
    name: str = "GUSD-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GUSD-USD"

    def __str__(self):
        return "GUSD-USD"

    def __call__(self):
        return "GUSD-USD"


@dataclass(slots=True)
class GYEN_USD:
    name: str = "GYEN-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "GYEN-USD"

    def __str__(self):
        return "GYEN-USD"

    def __call__(self):
        return "GYEN-USD"


@dataclass(slots=True)
class HBAR_USD:
    name: str = "HBAR-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "HBAR-USD"

    def __str__(self):
        return "HBAR-USD"

    def __call__(self):
        return "HBAR-USD"


@dataclass(slots=True)
class HBAR_USDT:
    name: str = "HBAR-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "HBAR-USDT"

    def __str__(self):
        return "HBAR-USDT"

    def __call__(self):
        return "HBAR-USDT"


@dataclass(slots=True)
class HFT_USD:
    name: str = "HFT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "HFT-USD"

    def __str__(self):
        return "HFT-USD"

    def __call__(self):
        return "HFT-USD"


@dataclass(slots=True)
class HFT_USDT:
    name: str = "HFT-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "HFT-USDT"

    def __str__(self):
        return "HFT-USDT"

    def __call__(self):
        return "HFT-USDT"


@dataclass(slots=True)
class HIGH_USD:
    name: str = "HIGH-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "HIGH-USD"

    def __str__(self):
        return "HIGH-USD"

    def __call__(self):
        return "HIGH-USD"


@dataclass(slots=True)
class HOPR_USD:
    name: str = "HOPR-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "HOPR-USD"

    def __str__(self):
        return "HOPR-USD"

    def __call__(self):
        return "HOPR-USD"


@dataclass(slots=True)
class HOPR_USDT:
    name: str = "HOPR-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "HOPR-USDT"

    def __str__(self):
        return "HOPR-USDT"

    def __call__(self):
        return "HOPR-USDT"


@dataclass(slots=True)
class ICP_BTC:
    name: str = "ICP-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ICP-BTC"

    def __str__(self):
        return "ICP-BTC"

    def __call__(self):
        return "ICP-BTC"


@dataclass(slots=True)
class ICP_EUR:
    name: str = "ICP-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ICP-EUR"

    def __str__(self):
        return "ICP-EUR"

    def __call__(self):
        return "ICP-EUR"


@dataclass(slots=True)
class ICP_GBP:
    name: str = "ICP-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ICP-GBP"

    def __str__(self):
        return "ICP-GBP"

    def __call__(self):
        return "ICP-GBP"


@dataclass(slots=True)
class ICP_USD:
    name: str = "ICP-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ICP-USD"

    def __str__(self):
        return "ICP-USD"

    def __call__(self):
        return "ICP-USD"


@dataclass(slots=True)
class ICP_USDT:
    name: str = "ICP-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ICP-USDT"

    def __str__(self):
        return "ICP-USDT"

    def __call__(self):
        return "ICP-USDT"


@dataclass(slots=True)
class IDEX_USD:
    name: str = "IDEX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "IDEX-USD"

    def __str__(self):
        return "IDEX-USD"

    def __call__(self):
        return "IDEX-USD"


@dataclass(slots=True)
class IDEX_USDT:
    name: str = "IDEX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "IDEX-USDT"

    def __str__(self):
        return "IDEX-USDT"

    def __call__(self):
        return "IDEX-USDT"


@dataclass(slots=True)
class ILV_USD:
    name: str = "ILV-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ILV-USD"

    def __str__(self):
        return "ILV-USD"

    def __call__(self):
        return "ILV-USD"


@dataclass(slots=True)
class IMX_USD:
    name: str = "IMX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "IMX-USD"

    def __str__(self):
        return "IMX-USD"

    def __call__(self):
        return "IMX-USD"


@dataclass(slots=True)
class IMX_USDT:
    name: str = "IMX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "IMX-USDT"

    def __str__(self):
        return "IMX-USDT"

    def __call__(self):
        return "IMX-USDT"


@dataclass(slots=True)
class INDEX_USD:
    name: str = "INDEX-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "INDEX-USD"

    def __str__(self):
        return "INDEX-USD"

    def __call__(self):
        return "INDEX-USD"


@dataclass(slots=True)
class INDEX_USDT:
    name: str = "INDEX-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "INDEX-USDT"

    def __str__(self):
        return "INDEX-USDT"

    def __call__(self):
        return "INDEX-USDT"


@dataclass(slots=True)
class INJ_USD:
    name: str = "INJ-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "INJ-USD"

    def __str__(self):
        return "INJ-USD"

    def __call__(self):
        return "INJ-USD"


@dataclass(slots=True)
class INV_USD:
    name: str = "INV-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "INV-USD"

    def __str__(self):
        return "INV-USD"

    def __call__(self):
        return "INV-USD"


@dataclass(slots=True)
class IOTX_EUR:
    name: str = "IOTX-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "IOTX-EUR"

    def __str__(self):
        return "IOTX-EUR"

    def __call__(self):
        return "IOTX-EUR"


@dataclass(slots=True)
class IOTX_USD:
    name: str = "IOTX-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "IOTX-USD"

    def __str__(self):
        return "IOTX-USD"

    def __call__(self):
        return "IOTX-USD"


@dataclass(slots=True)
class JASMY_USD:
    name: str = "JASMY-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "JASMY-USD"

    def __str__(self):
        return "JASMY-USD"

    def __call__(self):
        return "JASMY-USD"


@dataclass(slots=True)
class JASMY_USDT:
    name: str = "JASMY-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "JASMY-USDT"

    def __str__(self):
        return "JASMY-USDT"

    def __call__(self):
        return "JASMY-USDT"


@dataclass(slots=True)
class JUP_USD:
    name: str = "JUP-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "JUP-USD"

    def __str__(self):
        return "JUP-USD"

    def __call__(self):
        return "JUP-USD"


@dataclass(slots=True)
class KEEP_USD:
    name: str = "KEEP-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "KEEP-USD"

    def __str__(self):
        return "KEEP-USD"

    def __call__(self):
        return "KEEP-USD"


@dataclass(slots=True)
class KNC_BTC:
    name: str = "KNC-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "KNC-BTC"

    def __str__(self):
        return "KNC-BTC"

    def __call__(self):
        return "KNC-BTC"


@dataclass(slots=True)
class KNC_USD:
    name: str = "KNC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "KNC-USD"

    def __str__(self):
        return "KNC-USD"

    def __call__(self):
        return "KNC-USD"


@dataclass(slots=True)
class KRL_EUR:
    name: str = "KRL-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "KRL-EUR"

    def __str__(self):
        return "KRL-EUR"

    def __call__(self):
        return "KRL-EUR"


@dataclass(slots=True)
class KRL_USD:
    name: str = "KRL-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "KRL-USD"

    def __str__(self):
        return "KRL-USD"

    def __call__(self):
        return "KRL-USD"


@dataclass(slots=True)
class KRL_USDT:
    name: str = "KRL-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "KRL-USDT"

    def __str__(self):
        return "KRL-USDT"

    def __call__(self):
        return "KRL-USDT"


@dataclass(slots=True)
class KSM_USD:
    name: str = "KSM-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "KSM-USD"

    def __str__(self):
        return "KSM-USD"

    def __call__(self):
        return "KSM-USD"


@dataclass(slots=True)
class KSM_USDT:
    name: str = "KSM-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "KSM-USDT"

    def __str__(self):
        return "KSM-USDT"

    def __call__(self):
        return "KSM-USDT"


@dataclass(slots=True)
class LCX_EUR:
    name: str = "LCX-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LCX-EUR"

    def __str__(self):
        return "LCX-EUR"

    def __call__(self):
        return "LCX-EUR"


@dataclass(slots=True)
class LCX_USD:
    name: str = "LCX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LCX-USD"

    def __str__(self):
        return "LCX-USD"

    def __call__(self):
        return "LCX-USD"


@dataclass(slots=True)
class LCX_USDT:
    name: str = "LCX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LCX-USDT"

    def __str__(self):
        return "LCX-USDT"

    def __call__(self):
        return "LCX-USDT"


@dataclass(slots=True)
class LDO_USD:
    name: str = "LDO-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LDO-USD"

    def __str__(self):
        return "LDO-USD"

    def __call__(self):
        return "LDO-USD"


@dataclass(slots=True)
class LINK_BTC:
    name: str = "LINK-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LINK-BTC"

    def __str__(self):
        return "LINK-BTC"

    def __call__(self):
        return "LINK-BTC"


@dataclass(slots=True)
class LINK_ETH:
    name: str = "LINK-ETH"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LINK-ETH"

    def __str__(self):
        return "LINK-ETH"

    def __call__(self):
        return "LINK-ETH"


@dataclass(slots=True)
class LINK_EUR:
    name: str = "LINK-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LINK-EUR"

    def __str__(self):
        return "LINK-EUR"

    def __call__(self):
        return "LINK-EUR"


@dataclass(slots=True)
class LINK_GBP:
    name: str = "LINK-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LINK-GBP"

    def __str__(self):
        return "LINK-GBP"

    def __call__(self):
        return "LINK-GBP"


@dataclass(slots=True)
class LINK_USD:
    name: str = "LINK-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LINK-USD"

    def __str__(self):
        return "LINK-USD"

    def __call__(self):
        return "LINK-USD"


@dataclass(slots=True)
class LINK_USDT:
    name: str = "LINK-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LINK-USDT"

    def __str__(self):
        return "LINK-USDT"

    def __call__(self):
        return "LINK-USDT"


@dataclass(slots=True)
class LIT_USD:
    name: str = "LIT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LIT-USD"

    def __str__(self):
        return "LIT-USD"

    def __call__(self):
        return "LIT-USD"


@dataclass(slots=True)
class LOKA_USD:
    name: str = "LOKA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LOKA-USD"

    def __str__(self):
        return "LOKA-USD"

    def __call__(self):
        return "LOKA-USD"


@dataclass(slots=True)
class LOOM_USD:
    name: str = "LOOM-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LOOM-USD"

    def __str__(self):
        return "LOOM-USD"

    def __call__(self):
        return "LOOM-USD"


@dataclass(slots=True)
class LOOM_USDC:
    name: str = "LOOM-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LOOM-USDC"

    def __str__(self):
        return "LOOM-USDC"

    def __call__(self):
        return "LOOM-USDC"


@dataclass(slots=True)
class LPT_USD:
    name: str = "LPT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LPT-USD"

    def __str__(self):
        return "LPT-USD"

    def __call__(self):
        return "LPT-USD"


@dataclass(slots=True)
class LQTY_EUR:
    name: str = "LQTY-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LQTY-EUR"

    def __str__(self):
        return "LQTY-EUR"

    def __call__(self):
        return "LQTY-EUR"


@dataclass(slots=True)
class LQTY_USD:
    name: str = "LQTY-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LQTY-USD"

    def __str__(self):
        return "LQTY-USD"

    def __call__(self):
        return "LQTY-USD"


@dataclass(slots=True)
class LQTY_USDT:
    name: str = "LQTY-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LQTY-USDT"

    def __str__(self):
        return "LQTY-USDT"

    def __call__(self):
        return "LQTY-USDT"


@dataclass(slots=True)
class LRC_BTC:
    name: str = "LRC-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LRC-BTC"

    def __str__(self):
        return "LRC-BTC"

    def __call__(self):
        return "LRC-BTC"


@dataclass(slots=True)
class LRC_USD:
    name: str = "LRC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LRC-USD"

    def __str__(self):
        return "LRC-USD"

    def __call__(self):
        return "LRC-USD"


@dataclass(slots=True)
class LRC_USDT:
    name: str = "LRC-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LRC-USDT"

    def __str__(self):
        return "LRC-USDT"

    def __call__(self):
        return "LRC-USDT"


@dataclass(slots=True)
class LTC_BTC:
    name: str = "LTC-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LTC-BTC"

    def __str__(self):
        return "LTC-BTC"

    def __call__(self):
        return "LTC-BTC"


@dataclass(slots=True)
class LTC_EUR:
    name: str = "LTC-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LTC-EUR"

    def __str__(self):
        return "LTC-EUR"

    def __call__(self):
        return "LTC-EUR"


@dataclass(slots=True)
class LTC_GBP:
    name: str = "LTC-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LTC-GBP"

    def __str__(self):
        return "LTC-GBP"

    def __call__(self):
        return "LTC-GBP"


@dataclass(slots=True)
class LTC_USD:
    name: str = "LTC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "LTC-USD"

    def __str__(self):
        return "LTC-USD"

    def __call__(self):
        return "LTC-USD"


@dataclass(slots=True)
class MAGIC_USD:
    name: str = "MAGIC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MAGIC-USD"

    def __str__(self):
        return "MAGIC-USD"

    def __call__(self):
        return "MAGIC-USD"


@dataclass(slots=True)
class MANA_BTC:
    name: str = "MANA-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MANA-BTC"

    def __str__(self):
        return "MANA-BTC"

    def __call__(self):
        return "MANA-BTC"


@dataclass(slots=True)
class MANA_ETH:
    name: str = "MANA-ETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MANA-ETH"

    def __str__(self):
        return "MANA-ETH"

    def __call__(self):
        return "MANA-ETH"


@dataclass(slots=True)
class MANA_EUR:
    name: str = "MANA-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MANA-EUR"

    def __str__(self):
        return "MANA-EUR"

    def __call__(self):
        return "MANA-EUR"


@dataclass(slots=True)
class MANA_USD:
    name: str = "MANA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MANA-USD"

    def __str__(self):
        return "MANA-USD"

    def __call__(self):
        return "MANA-USD"


@dataclass(slots=True)
class MANA_USDC:
    name: str = "MANA-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MANA-USDC"

    def __str__(self):
        return "MANA-USDC"

    def __call__(self):
        return "MANA-USDC"


@dataclass(slots=True)
class MASK_EUR:
    name: str = "MASK-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MASK-EUR"

    def __str__(self):
        return "MASK-EUR"

    def __call__(self):
        return "MASK-EUR"


@dataclass(slots=True)
class MASK_GBP:
    name: str = "MASK-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MASK-GBP"

    def __str__(self):
        return "MASK-GBP"

    def __call__(self):
        return "MASK-GBP"


@dataclass(slots=True)
class MASK_USD:
    name: str = "MASK-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MASK-USD"

    def __str__(self):
        return "MASK-USD"

    def __call__(self):
        return "MASK-USD"


@dataclass(slots=True)
class MASK_USDT:
    name: str = "MASK-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MASK-USDT"

    def __str__(self):
        return "MASK-USDT"

    def __call__(self):
        return "MASK-USDT"


@dataclass(slots=True)
class MATH_USD:
    name: str = "MATH-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MATH-USD"

    def __str__(self):
        return "MATH-USD"

    def __call__(self):
        return "MATH-USD"


@dataclass(slots=True)
class MATH_USDT:
    name: str = "MATH-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MATH-USDT"

    def __str__(self):
        return "MATH-USDT"

    def __call__(self):
        return "MATH-USDT"


@dataclass(slots=True)
class MATIC_BTC:
    name: str = "MATIC-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MATIC-BTC"

    def __str__(self):
        return "MATIC-BTC"

    def __call__(self):
        return "MATIC-BTC"


@dataclass(slots=True)
class MATIC_EUR:
    name: str = "MATIC-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MATIC-EUR"

    def __str__(self):
        return "MATIC-EUR"

    def __call__(self):
        return "MATIC-EUR"


@dataclass(slots=True)
class MATIC_GBP:
    name: str = "MATIC-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MATIC-GBP"

    def __str__(self):
        return "MATIC-GBP"

    def __call__(self):
        return "MATIC-GBP"


@dataclass(slots=True)
class MATIC_USD:
    name: str = "MATIC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MATIC-USD"

    def __str__(self):
        return "MATIC-USD"

    def __call__(self):
        return "MATIC-USD"


@dataclass(slots=True)
class MATIC_USDT:
    name: str = "MATIC-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MATIC-USDT"

    def __str__(self):
        return "MATIC-USDT"

    def __call__(self):
        return "MATIC-USDT"


@dataclass(slots=True)
class MCO2_USD:
    name: str = "MCO2-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MCO2-USD"

    def __str__(self):
        return "MCO2-USD"

    def __call__(self):
        return "MCO2-USD"


@dataclass(slots=True)
class MCO2_USDT:
    name: str = "MCO2-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MCO2-USDT"

    def __str__(self):
        return "MCO2-USDT"

    def __call__(self):
        return "MCO2-USDT"


@dataclass(slots=True)
class MDT_USD:
    name: str = "MDT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MDT-USD"

    def __str__(self):
        return "MDT-USD"

    def __call__(self):
        return "MDT-USD"


@dataclass(slots=True)
class MDT_USDT:
    name: str = "MDT-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MDT-USDT"

    def __str__(self):
        return "MDT-USDT"

    def __call__(self):
        return "MDT-USDT"


@dataclass(slots=True)
class MEDIA_USD:
    name: str = "MEDIA-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MEDIA-USD"

    def __str__(self):
        return "MEDIA-USD"

    def __call__(self):
        return "MEDIA-USD"


@dataclass(slots=True)
class MEDIA_USDT:
    name: str = "MEDIA-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MEDIA-USDT"

    def __str__(self):
        return "MEDIA-USDT"

    def __call__(self):
        return "MEDIA-USDT"


@dataclass(slots=True)
class METIS_USD:
    name: str = "METIS-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "METIS-USD"

    def __str__(self):
        return "METIS-USD"

    def __call__(self):
        return "METIS-USD"


@dataclass(slots=True)
class METIS_USDT:
    name: str = "METIS-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "METIS-USDT"

    def __str__(self):
        return "METIS-USDT"

    def __call__(self):
        return "METIS-USDT"


@dataclass(slots=True)
class MINA_EUR:
    name: str = "MINA-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MINA-EUR"

    def __str__(self):
        return "MINA-EUR"

    def __call__(self):
        return "MINA-EUR"


@dataclass(slots=True)
class MINA_USD:
    name: str = "MINA-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MINA-USD"

    def __str__(self):
        return "MINA-USD"

    def __call__(self):
        return "MINA-USD"


@dataclass(slots=True)
class MINA_USDT:
    name: str = "MINA-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MINA-USDT"

    def __str__(self):
        return "MINA-USDT"

    def __call__(self):
        return "MINA-USDT"


@dataclass(slots=True)
class MIR_BTC:
    name: str = "MIR-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MIR-BTC"

    def __str__(self):
        return "MIR-BTC"

    def __call__(self):
        return "MIR-BTC"


@dataclass(slots=True)
class MIR_EUR:
    name: str = "MIR-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MIR-EUR"

    def __str__(self):
        return "MIR-EUR"

    def __call__(self):
        return "MIR-EUR"


@dataclass(slots=True)
class MIR_GBP:
    name: str = "MIR-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MIR-GBP"

    def __str__(self):
        return "MIR-GBP"

    def __call__(self):
        return "MIR-GBP"


@dataclass(slots=True)
class MIR_USD:
    name: str = "MIR-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MIR-USD"

    def __str__(self):
        return "MIR-USD"

    def __call__(self):
        return "MIR-USD"


@dataclass(slots=True)
class MKR_BTC:
    name: str = "MKR-BTC"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MKR-BTC"

    def __str__(self):
        return "MKR-BTC"

    def __call__(self):
        return "MKR-BTC"


@dataclass(slots=True)
class MKR_USD:
    name: str = "MKR-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MKR-USD"

    def __str__(self):
        return "MKR-USD"

    def __call__(self):
        return "MKR-USD"


@dataclass(slots=True)
class MLN_USD:
    name: str = "MLN-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MLN-USD"

    def __str__(self):
        return "MLN-USD"

    def __call__(self):
        return "MLN-USD"


@dataclass(slots=True)
class MNDE_USD:
    name: str = "MNDE-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MNDE-USD"

    def __str__(self):
        return "MNDE-USD"

    def __call__(self):
        return "MNDE-USD"


@dataclass(slots=True)
class MONA_USD:
    name: str = "MONA-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MONA-USD"

    def __str__(self):
        return "MONA-USD"

    def __call__(self):
        return "MONA-USD"


@dataclass(slots=True)
class MPL_USD:
    name: str = "MPL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MPL-USD"

    def __str__(self):
        return "MPL-USD"

    def __call__(self):
        return "MPL-USD"


@dataclass(slots=True)
class MSOL_USD:
    name: str = "MSOL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MSOL-USD"

    def __str__(self):
        return "MSOL-USD"

    def __call__(self):
        return "MSOL-USD"


@dataclass(slots=True)
class MTL_USD:
    name: str = "MTL-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MTL-USD"

    def __str__(self):
        return "MTL-USD"

    def __call__(self):
        return "MTL-USD"


@dataclass(slots=True)
class MUSD_USD:
    name: str = "MUSD-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MUSD-USD"

    def __str__(self):
        return "MUSD-USD"

    def __call__(self):
        return "MUSD-USD"


@dataclass(slots=True)
class MUSE_USD:
    name: str = "MUSE-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MUSE-USD"

    def __str__(self):
        return "MUSE-USD"

    def __call__(self):
        return "MUSE-USD"


@dataclass(slots=True)
class MXC_USD:
    name: str = "MXC-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "MXC-USD"

    def __str__(self):
        return "MXC-USD"

    def __call__(self):
        return "MXC-USD"


@dataclass(slots=True)
class NCT_EUR:
    name: str = "NCT-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NCT-EUR"

    def __str__(self):
        return "NCT-EUR"

    def __call__(self):
        return "NCT-EUR"


@dataclass(slots=True)
class NCT_USD:
    name: str = "NCT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NCT-USD"

    def __str__(self):
        return "NCT-USD"

    def __call__(self):
        return "NCT-USD"


@dataclass(slots=True)
class NCT_USDT:
    name: str = "NCT-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NCT-USDT"

    def __str__(self):
        return "NCT-USDT"

    def __call__(self):
        return "NCT-USDT"


@dataclass(slots=True)
class NEAR_USD:
    name: str = "NEAR-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NEAR-USD"

    def __str__(self):
        return "NEAR-USD"

    def __call__(self):
        return "NEAR-USD"


@dataclass(slots=True)
class NEAR_USDT:
    name: str = "NEAR-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NEAR-USDT"

    def __str__(self):
        return "NEAR-USDT"

    def __call__(self):
        return "NEAR-USDT"


@dataclass(slots=True)
class NEST_USD:
    name: str = "NEST-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NEST-USD"

    def __str__(self):
        return "NEST-USD"

    def __call__(self):
        return "NEST-USD"


@dataclass(slots=True)
class NEST_USDT:
    name: str = "NEST-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NEST-USDT"

    def __str__(self):
        return "NEST-USDT"

    def __call__(self):
        return "NEST-USDT"


@dataclass(slots=True)
class NKN_BTC:
    name: str = "NKN-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NKN-BTC"

    def __str__(self):
        return "NKN-BTC"

    def __call__(self):
        return "NKN-BTC"


@dataclass(slots=True)
class NKN_EUR:
    name: str = "NKN-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NKN-EUR"

    def __str__(self):
        return "NKN-EUR"

    def __call__(self):
        return "NKN-EUR"


@dataclass(slots=True)
class NKN_GBP:
    name: str = "NKN-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NKN-GBP"

    def __str__(self):
        return "NKN-GBP"

    def __call__(self):
        return "NKN-GBP"


@dataclass(slots=True)
class NKN_USD:
    name: str = "NKN-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NKN-USD"

    def __str__(self):
        return "NKN-USD"

    def __call__(self):
        return "NKN-USD"


@dataclass(slots=True)
class NMR_BTC:
    name: str = "NMR-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NMR-BTC"

    def __str__(self):
        return "NMR-BTC"

    def __call__(self):
        return "NMR-BTC"


@dataclass(slots=True)
class NMR_EUR:
    name: str = "NMR-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NMR-EUR"

    def __str__(self):
        return "NMR-EUR"

    def __call__(self):
        return "NMR-EUR"


@dataclass(slots=True)
class NMR_GBP:
    name: str = "NMR-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NMR-GBP"

    def __str__(self):
        return "NMR-GBP"

    def __call__(self):
        return "NMR-GBP"


@dataclass(slots=True)
class NMR_USD:
    name: str = "NMR-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NMR-USD"

    def __str__(self):
        return "NMR-USD"

    def __call__(self):
        return "NMR-USD"


@dataclass(slots=True)
class NU_BTC:
    name: str = "NU-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NU-BTC"

    def __str__(self):
        return "NU-BTC"

    def __call__(self):
        return "NU-BTC"


@dataclass(slots=True)
class NU_EUR:
    name: str = "NU-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NU-EUR"

    def __str__(self):
        return "NU-EUR"

    def __call__(self):
        return "NU-EUR"


@dataclass(slots=True)
class NU_GBP:
    name: str = "NU-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NU-GBP"

    def __str__(self):
        return "NU-GBP"

    def __call__(self):
        return "NU-GBP"


@dataclass(slots=True)
class NU_USD:
    name: str = "NU-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "NU-USD"

    def __str__(self):
        return "NU-USD"

    def __call__(self):
        return "NU-USD"


@dataclass(slots=True)
class OCEAN_USD:
    name: str = "OCEAN-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OCEAN-USD"

    def __str__(self):
        return "OCEAN-USD"

    def __call__(self):
        return "OCEAN-USD"


@dataclass(slots=True)
class OGN_BTC:
    name: str = "OGN-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OGN-BTC"

    def __str__(self):
        return "OGN-BTC"

    def __call__(self):
        return "OGN-BTC"


@dataclass(slots=True)
class OGN_USD:
    name: str = "OGN-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OGN-USD"

    def __str__(self):
        return "OGN-USD"

    def __call__(self):
        return "OGN-USD"


@dataclass(slots=True)
class OMG_BTC:
    name: str = "OMG-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OMG-BTC"

    def __str__(self):
        return "OMG-BTC"

    def __call__(self):
        return "OMG-BTC"


@dataclass(slots=True)
class OMG_EUR:
    name: str = "OMG-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OMG-EUR"

    def __str__(self):
        return "OMG-EUR"

    def __call__(self):
        return "OMG-EUR"


@dataclass(slots=True)
class OMG_GBP:
    name: str = "OMG-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OMG-GBP"

    def __str__(self):
        return "OMG-GBP"

    def __call__(self):
        return "OMG-GBP"


@dataclass(slots=True)
class OMG_USD:
    name: str = "OMG-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OMG-USD"

    def __str__(self):
        return "OMG-USD"

    def __call__(self):
        return "OMG-USD"


@dataclass(slots=True)
class OOKI_USD:
    name: str = "OOKI-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OOKI-USD"

    def __str__(self):
        return "OOKI-USD"

    def __call__(self):
        return "OOKI-USD"


@dataclass(slots=True)
class OP_USD:
    name: str = "OP-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OP-USD"

    def __str__(self):
        return "OP-USD"

    def __call__(self):
        return "OP-USD"


@dataclass(slots=True)
class OP_USDT:
    name: str = "OP-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OP-USDT"

    def __str__(self):
        return "OP-USDT"

    def __call__(self):
        return "OP-USDT"


@dataclass(slots=True)
class ORCA_USD:
    name: str = "ORCA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ORCA-USD"

    def __str__(self):
        return "ORCA-USD"

    def __call__(self):
        return "ORCA-USD"


@dataclass(slots=True)
class ORN_BTC:
    name: str = "ORN-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ORN-BTC"

    def __str__(self):
        return "ORN-BTC"

    def __call__(self):
        return "ORN-BTC"


@dataclass(slots=True)
class ORN_USD:
    name: str = "ORN-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ORN-USD"

    def __str__(self):
        return "ORN-USD"

    def __call__(self):
        return "ORN-USD"


@dataclass(slots=True)
class ORN_USDT:
    name: str = "ORN-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ORN-USDT"

    def __str__(self):
        return "ORN-USDT"

    def __call__(self):
        return "ORN-USDT"


@dataclass(slots=True)
class OXT_USD:
    name: str = "OXT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "OXT-USD"

    def __str__(self):
        return "OXT-USD"

    def __call__(self):
        return "OXT-USD"


@dataclass(slots=True)
class PAX_USD:
    name: str = "PAX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PAX-USD"

    def __str__(self):
        return "PAX-USD"

    def __call__(self):
        return "PAX-USD"


@dataclass(slots=True)
class PAX_USDT:
    name: str = "PAX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PAX-USDT"

    def __str__(self):
        return "PAX-USDT"

    def __call__(self):
        return "PAX-USDT"


@dataclass(slots=True)
class PERP_EUR:
    name: str = "PERP-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PERP-EUR"

    def __str__(self):
        return "PERP-EUR"

    def __call__(self):
        return "PERP-EUR"


@dataclass(slots=True)
class PERP_USD:
    name: str = "PERP-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PERP-USD"

    def __str__(self):
        return "PERP-USD"

    def __call__(self):
        return "PERP-USD"


@dataclass(slots=True)
class PERP_USDT:
    name: str = "PERP-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PERP-USDT"

    def __str__(self):
        return "PERP-USDT"

    def __call__(self):
        return "PERP-USDT"


@dataclass(slots=True)
class PLA_USD:
    name: str = "PLA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PLA-USD"

    def __str__(self):
        return "PLA-USD"

    def __call__(self):
        return "PLA-USD"


@dataclass(slots=True)
class PLU_USD:
    name: str = "PLU-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PLU-USD"

    def __str__(self):
        return "PLU-USD"

    def __call__(self):
        return "PLU-USD"


@dataclass(slots=True)
class PNG_USD:
    name: str = "PNG-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PNG-USD"

    def __str__(self):
        return "PNG-USD"

    def __call__(self):
        return "PNG-USD"


@dataclass(slots=True)
class POLS_USD:
    name: str = "POLS-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "POLS-USD"

    def __str__(self):
        return "POLS-USD"

    def __call__(self):
        return "POLS-USD"


@dataclass(slots=True)
class POLS_USDT:
    name: str = "POLS-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "POLS-USDT"

    def __str__(self):
        return "POLS-USDT"

    def __call__(self):
        return "POLS-USDT"


@dataclass(slots=True)
class POLY_USD:
    name: str = "POLY-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "POLY-USD"

    def __str__(self):
        return "POLY-USD"

    def __call__(self):
        return "POLY-USD"


@dataclass(slots=True)
class POLY_USDT:
    name: str = "POLY-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "POLY-USDT"

    def __str__(self):
        return "POLY-USDT"

    def __call__(self):
        return "POLY-USDT"


@dataclass(slots=True)
class POND_USD:
    name: str = "POND-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "POND-USD"

    def __str__(self):
        return "POND-USD"

    def __call__(self):
        return "POND-USD"


@dataclass(slots=True)
class POND_USDT:
    name: str = "POND-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "POND-USDT"

    def __str__(self):
        return "POND-USDT"

    def __call__(self):
        return "POND-USDT"


@dataclass(slots=True)
class POWR_EUR:
    name: str = "POWR-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "POWR-EUR"

    def __str__(self):
        return "POWR-EUR"

    def __call__(self):
        return "POWR-EUR"


@dataclass(slots=True)
class POWR_USD:
    name: str = "POWR-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "POWR-USD"

    def __str__(self):
        return "POWR-USD"

    def __call__(self):
        return "POWR-USD"


@dataclass(slots=True)
class POWR_USDT:
    name: str = "POWR-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "POWR-USDT"

    def __str__(self):
        return "POWR-USDT"

    def __call__(self):
        return "POWR-USDT"


@dataclass(slots=True)
class PRO_USD:
    name: str = "PRO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PRO-USD"

    def __str__(self):
        return "PRO-USD"

    def __call__(self):
        return "PRO-USD"


@dataclass(slots=True)
class PRQ_USD:
    name: str = "PRQ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PRQ-USD"

    def __str__(self):
        return "PRQ-USD"

    def __call__(self):
        return "PRQ-USD"


@dataclass(slots=True)
class PRQ_USDT:
    name: str = "PRQ-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PRQ-USDT"

    def __str__(self):
        return "PRQ-USDT"

    def __call__(self):
        return "PRQ-USDT"


@dataclass(slots=True)
class PUNDIX_USD:
    name: str = "PUNDIX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PUNDIX-USD"

    def __str__(self):
        return "PUNDIX-USD"

    def __call__(self):
        return "PUNDIX-USD"


@dataclass(slots=True)
class PYR_USD:
    name: str = "PYR-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "PYR-USD"

    def __str__(self):
        return "PYR-USD"

    def __call__(self):
        return "PYR-USD"


@dataclass(slots=True)
class QI_USD:
    name: str = "QI-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "QI-USD"

    def __str__(self):
        return "QI-USD"

    def __call__(self):
        return "QI-USD"


@dataclass(slots=True)
class QNT_USD:
    name: str = "QNT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "QNT-USD"

    def __str__(self):
        return "QNT-USD"

    def __call__(self):
        return "QNT-USD"


@dataclass(slots=True)
class QNT_USDT:
    name: str = "QNT-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "QNT-USDT"

    def __str__(self):
        return "QNT-USDT"

    def __call__(self):
        return "QNT-USDT"


@dataclass(slots=True)
class QSP_USD:
    name: str = "QSP-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "QSP-USD"

    def __str__(self):
        return "QSP-USD"

    def __call__(self):
        return "QSP-USD"


@dataclass(slots=True)
class QSP_USDT:
    name: str = "QSP-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "QSP-USDT"

    def __str__(self):
        return "QSP-USDT"

    def __call__(self):
        return "QSP-USDT"


@dataclass(slots=True)
class QUICK_USD:
    name: str = "QUICK-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "QUICK-USD"

    def __str__(self):
        return "QUICK-USD"

    def __call__(self):
        return "QUICK-USD"


@dataclass(slots=True)
class RAD_BTC:
    name: str = "RAD-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RAD-BTC"

    def __str__(self):
        return "RAD-BTC"

    def __call__(self):
        return "RAD-BTC"


@dataclass(slots=True)
class RAD_EUR:
    name: str = "RAD-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RAD-EUR"

    def __str__(self):
        return "RAD-EUR"

    def __call__(self):
        return "RAD-EUR"


@dataclass(slots=True)
class RAD_GBP:
    name: str = "RAD-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RAD-GBP"

    def __str__(self):
        return "RAD-GBP"

    def __call__(self):
        return "RAD-GBP"


@dataclass(slots=True)
class RAD_USD:
    name: str = "RAD-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RAD-USD"

    def __str__(self):
        return "RAD-USD"

    def __call__(self):
        return "RAD-USD"


@dataclass(slots=True)
class RAD_USDT:
    name: str = "RAD-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RAD-USDT"

    def __str__(self):
        return "RAD-USDT"

    def __call__(self):
        return "RAD-USDT"


@dataclass(slots=True)
class RAI_USD:
    name: str = "RAI-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RAI-USD"

    def __str__(self):
        return "RAI-USD"

    def __call__(self):
        return "RAI-USD"


@dataclass(slots=True)
class RARE_USD:
    name: str = "RARE-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RARE-USD"

    def __str__(self):
        return "RARE-USD"

    def __call__(self):
        return "RARE-USD"


@dataclass(slots=True)
class RARI_USD:
    name: str = "RARI-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RARI-USD"

    def __str__(self):
        return "RARI-USD"

    def __call__(self):
        return "RARI-USD"


@dataclass(slots=True)
class RBN_USD:
    name: str = "RBN-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RBN-USD"

    def __str__(self):
        return "RBN-USD"

    def __call__(self):
        return "RBN-USD"


@dataclass(slots=True)
class REN_BTC:
    name: str = "REN-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "REN-BTC"

    def __str__(self):
        return "REN-BTC"

    def __call__(self):
        return "REN-BTC"


@dataclass(slots=True)
class REN_USD:
    name: str = "REN-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "REN-USD"

    def __str__(self):
        return "REN-USD"

    def __call__(self):
        return "REN-USD"


@dataclass(slots=True)
class REP_BTC:
    name: str = "REP-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "REP-BTC"

    def __str__(self):
        return "REP-BTC"

    def __call__(self):
        return "REP-BTC"


@dataclass(slots=True)
class REP_USD:
    name: str = "REP-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "REP-USD"

    def __str__(self):
        return "REP-USD"

    def __call__(self):
        return "REP-USD"


@dataclass(slots=True)
class REQ_BTC:
    name: str = "REQ-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "REQ-BTC"

    def __str__(self):
        return "REQ-BTC"

    def __call__(self):
        return "REQ-BTC"


@dataclass(slots=True)
class REQ_EUR:
    name: str = "REQ-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "REQ-EUR"

    def __str__(self):
        return "REQ-EUR"

    def __call__(self):
        return "REQ-EUR"


@dataclass(slots=True)
class REQ_GBP:
    name: str = "REQ-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "REQ-GBP"

    def __str__(self):
        return "REQ-GBP"

    def __call__(self):
        return "REQ-GBP"


@dataclass(slots=True)
class REQ_USD:
    name: str = "REQ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "REQ-USD"

    def __str__(self):
        return "REQ-USD"

    def __call__(self):
        return "REQ-USD"


@dataclass(slots=True)
class REQ_USDT:
    name: str = "REQ-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "REQ-USDT"

    def __str__(self):
        return "REQ-USDT"

    def __call__(self):
        return "REQ-USDT"


@dataclass(slots=True)
class RGT_USD:
    name: str = "RGT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RGT-USD"

    def __str__(self):
        return "RGT-USD"

    def __call__(self):
        return "RGT-USD"


@dataclass(slots=True)
class RLC_BTC:
    name: str = "RLC-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RLC-BTC"

    def __str__(self):
        return "RLC-BTC"

    def __call__(self):
        return "RLC-BTC"


@dataclass(slots=True)
class RLC_USD:
    name: str = "RLC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RLC-USD"

    def __str__(self):
        return "RLC-USD"

    def __call__(self):
        return "RLC-USD"


@dataclass(slots=True)
class RLY_EUR:
    name: str = "RLY-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RLY-EUR"

    def __str__(self):
        return "RLY-EUR"

    def __call__(self):
        return "RLY-EUR"


@dataclass(slots=True)
class RLY_GBP:
    name: str = "RLY-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RLY-GBP"

    def __str__(self):
        return "RLY-GBP"

    def __call__(self):
        return "RLY-GBP"


@dataclass(slots=True)
class RLY_USD:
    name: str = "RLY-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RLY-USD"

    def __str__(self):
        return "RLY-USD"

    def __call__(self):
        return "RLY-USD"


@dataclass(slots=True)
class RLY_USDT:
    name: str = "RLY-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RLY-USDT"

    def __str__(self):
        return "RLY-USDT"

    def __call__(self):
        return "RLY-USDT"


@dataclass(slots=True)
class RNDR_EUR:
    name: str = "RNDR-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RNDR-EUR"

    def __str__(self):
        return "RNDR-EUR"

    def __call__(self):
        return "RNDR-EUR"


@dataclass(slots=True)
class RNDR_USD:
    name: str = "RNDR-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RNDR-USD"

    def __str__(self):
        return "RNDR-USD"

    def __call__(self):
        return "RNDR-USD"


@dataclass(slots=True)
class RNDR_USDT:
    name: str = "RNDR-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RNDR-USDT"

    def __str__(self):
        return "RNDR-USDT"

    def __call__(self):
        return "RNDR-USDT"


@dataclass(slots=True)
class ROSE_USD:
    name: str = "ROSE-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ROSE-USD"

    def __str__(self):
        return "ROSE-USD"

    def __call__(self):
        return "ROSE-USD"


@dataclass(slots=True)
class ROSE_USDT:
    name: str = "ROSE-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ROSE-USDT"

    def __str__(self):
        return "ROSE-USDT"

    def __call__(self):
        return "ROSE-USDT"


@dataclass(slots=True)
class RPL_USD:
    name: str = "RPL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "RPL-USD"

    def __str__(self):
        return "RPL-USD"

    def __call__(self):
        return "RPL-USD"


@dataclass(slots=True)
class SAND_USD:
    name: str = "SAND-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SAND-USD"

    def __str__(self):
        return "SAND-USD"

    def __call__(self):
        return "SAND-USD"


@dataclass(slots=True)
class SAND_USDT:
    name: str = "SAND-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SAND-USDT"

    def __str__(self):
        return "SAND-USDT"

    def __call__(self):
        return "SAND-USDT"


@dataclass(slots=True)
class SHIB_EUR:
    name: str = "SHIB-EUR"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SHIB-EUR"

    def __str__(self):
        return "SHIB-EUR"

    def __call__(self):
        return "SHIB-EUR"


@dataclass(slots=True)
class SHIB_GBP:
    name: str = "SHIB-GBP"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SHIB-GBP"

    def __str__(self):
        return "SHIB-GBP"

    def __call__(self):
        return "SHIB-GBP"


@dataclass(slots=True)
class SHIB_USD:
    name: str = "SHIB-USD"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SHIB-USD"

    def __str__(self):
        return "SHIB-USD"

    def __call__(self):
        return "SHIB-USD"


@dataclass(slots=True)
class SHIB_USDT:
    name: str = "SHIB-USDT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SHIB-USDT"

    def __str__(self):
        return "SHIB-USDT"

    def __call__(self):
        return "SHIB-USDT"


@dataclass(slots=True)
class SHPING_EUR:
    name: str = "SHPING-EUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SHPING-EUR"

    def __str__(self):
        return "SHPING-EUR"

    def __call__(self):
        return "SHPING-EUR"


@dataclass(slots=True)
class SHPING_USD:
    name: str = "SHPING-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SHPING-USD"

    def __str__(self):
        return "SHPING-USD"

    def __call__(self):
        return "SHPING-USD"


@dataclass(slots=True)
class SHPING_USDT:
    name: str = "SHPING-USDT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SHPING-USDT"

    def __str__(self):
        return "SHPING-USDT"

    def __call__(self):
        return "SHPING-USDT"


@dataclass(slots=True)
class SKL_BTC:
    name: str = "SKL-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SKL-BTC"

    def __str__(self):
        return "SKL-BTC"

    def __call__(self):
        return "SKL-BTC"


@dataclass(slots=True)
class SKL_EUR:
    name: str = "SKL-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SKL-EUR"

    def __str__(self):
        return "SKL-EUR"

    def __call__(self):
        return "SKL-EUR"


@dataclass(slots=True)
class SKL_GBP:
    name: str = "SKL-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SKL-GBP"

    def __str__(self):
        return "SKL-GBP"

    def __call__(self):
        return "SKL-GBP"


@dataclass(slots=True)
class SKL_USD:
    name: str = "SKL-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SKL-USD"

    def __str__(self):
        return "SKL-USD"

    def __call__(self):
        return "SKL-USD"


@dataclass(slots=True)
class SNT_USD:
    name: str = "SNT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SNT-USD"

    def __str__(self):
        return "SNT-USD"

    def __call__(self):
        return "SNT-USD"


@dataclass(slots=True)
class SNX_BTC:
    name: str = "SNX-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SNX-BTC"

    def __str__(self):
        return "SNX-BTC"

    def __call__(self):
        return "SNX-BTC"


@dataclass(slots=True)
class SNX_EUR:
    name: str = "SNX-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SNX-EUR"

    def __str__(self):
        return "SNX-EUR"

    def __call__(self):
        return "SNX-EUR"


@dataclass(slots=True)
class SNX_GBP:
    name: str = "SNX-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SNX-GBP"

    def __str__(self):
        return "SNX-GBP"

    def __call__(self):
        return "SNX-GBP"


@dataclass(slots=True)
class SNX_USD:
    name: str = "SNX-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SNX-USD"

    def __str__(self):
        return "SNX-USD"

    def __call__(self):
        return "SNX-USD"


@dataclass(slots=True)
class SOL_BTC:
    name: str = "SOL-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SOL-BTC"

    def __str__(self):
        return "SOL-BTC"

    def __call__(self):
        return "SOL-BTC"


@dataclass(slots=True)
class SOL_ETH:
    name: str = "SOL-ETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SOL-ETH"

    def __str__(self):
        return "SOL-ETH"

    def __call__(self):
        return "SOL-ETH"


@dataclass(slots=True)
class SOL_EUR:
    name: str = "SOL-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SOL-EUR"

    def __str__(self):
        return "SOL-EUR"

    def __call__(self):
        return "SOL-EUR"


@dataclass(slots=True)
class SOL_GBP:
    name: str = "SOL-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SOL-GBP"

    def __str__(self):
        return "SOL-GBP"

    def __call__(self):
        return "SOL-GBP"


@dataclass(slots=True)
class SOL_USD:
    name: str = "SOL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SOL-USD"

    def __str__(self):
        return "SOL-USD"

    def __call__(self):
        return "SOL-USD"


@dataclass(slots=True)
class SOL_USDT:
    name: str = "SOL-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SOL-USDT"

    def __str__(self):
        return "SOL-USDT"

    def __call__(self):
        return "SOL-USDT"


@dataclass(slots=True)
class SPELL_USD:
    name: str = "SPELL-USD"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SPELL-USD"

    def __str__(self):
        return "SPELL-USD"

    def __call__(self):
        return "SPELL-USD"


@dataclass(slots=True)
class SPELL_USDT:
    name: str = "SPELL-USDT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SPELL-USDT"

    def __str__(self):
        return "SPELL-USDT"

    def __call__(self):
        return "SPELL-USDT"


@dataclass(slots=True)
class STG_USD:
    name: str = "STG-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "STG-USD"

    def __str__(self):
        return "STG-USD"

    def __call__(self):
        return "STG-USD"


@dataclass(slots=True)
class STG_USDT:
    name: str = "STG-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "STG-USDT"

    def __str__(self):
        return "STG-USDT"

    def __call__(self):
        return "STG-USDT"


@dataclass(slots=True)
class STORJ_BTC:
    name: str = "STORJ-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "STORJ-BTC"

    def __str__(self):
        return "STORJ-BTC"

    def __call__(self):
        return "STORJ-BTC"


@dataclass(slots=True)
class STORJ_USD:
    name: str = "STORJ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "STORJ-USD"

    def __str__(self):
        return "STORJ-USD"

    def __call__(self):
        return "STORJ-USD"


@dataclass(slots=True)
class STX_USD:
    name: str = "STX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "STX-USD"

    def __str__(self):
        return "STX-USD"

    def __call__(self):
        return "STX-USD"


@dataclass(slots=True)
class STX_USDT:
    name: str = "STX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "STX-USDT"

    def __str__(self):
        return "STX-USDT"

    def __call__(self):
        return "STX-USDT"


@dataclass(slots=True)
class SUKU_EUR:
    name: str = "SUKU-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUKU-EUR"

    def __str__(self):
        return "SUKU-EUR"

    def __call__(self):
        return "SUKU-EUR"


@dataclass(slots=True)
class SUKU_USD:
    name: str = "SUKU-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUKU-USD"

    def __str__(self):
        return "SUKU-USD"

    def __call__(self):
        return "SUKU-USD"


@dataclass(slots=True)
class SUKU_USDT:
    name: str = "SUKU-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUKU-USDT"

    def __str__(self):
        return "SUKU-USDT"

    def __call__(self):
        return "SUKU-USDT"


@dataclass(slots=True)
class SUPER_USD:
    name: str = "SUPER-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUPER-USD"

    def __str__(self):
        return "SUPER-USD"

    def __call__(self):
        return "SUPER-USD"


@dataclass(slots=True)
class SUPER_USDT:
    name: str = "SUPER-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUPER-USDT"

    def __str__(self):
        return "SUPER-USDT"

    def __call__(self):
        return "SUPER-USDT"


@dataclass(slots=True)
class SUSHI_BTC:
    name: str = "SUSHI-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUSHI-BTC"

    def __str__(self):
        return "SUSHI-BTC"

    def __call__(self):
        return "SUSHI-BTC"


@dataclass(slots=True)
class SUSHI_ETH:
    name: str = "SUSHI-ETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUSHI-ETH"

    def __str__(self):
        return "SUSHI-ETH"

    def __call__(self):
        return "SUSHI-ETH"


@dataclass(slots=True)
class SUSHI_EUR:
    name: str = "SUSHI-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUSHI-EUR"

    def __str__(self):
        return "SUSHI-EUR"

    def __call__(self):
        return "SUSHI-EUR"


@dataclass(slots=True)
class SUSHI_GBP:
    name: str = "SUSHI-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUSHI-GBP"

    def __str__(self):
        return "SUSHI-GBP"

    def __call__(self):
        return "SUSHI-GBP"


@dataclass(slots=True)
class SUSHI_USD:
    name: str = "SUSHI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SUSHI-USD"

    def __str__(self):
        return "SUSHI-USD"

    def __call__(self):
        return "SUSHI-USD"


@dataclass(slots=True)
class SWFTC_USD:
    name: str = "SWFTC-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SWFTC-USD"

    def __str__(self):
        return "SWFTC-USD"

    def __call__(self):
        return "SWFTC-USD"


@dataclass(slots=True)
class SYLO_USD:
    name: str = "SYLO-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SYLO-USD"

    def __str__(self):
        return "SYLO-USD"

    def __call__(self):
        return "SYLO-USD"


@dataclass(slots=True)
class SYLO_USDT:
    name: str = "SYLO-USDT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SYLO-USDT"

    def __str__(self):
        return "SYLO-USDT"

    def __call__(self):
        return "SYLO-USDT"


@dataclass(slots=True)
class SYN_USD:
    name: str = "SYN-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "SYN-USD"

    def __str__(self):
        return "SYN-USD"

    def __call__(self):
        return "SYN-USD"


@dataclass(slots=True)
class TIME_USD:
    name: str = "TIME-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TIME-USD"

    def __str__(self):
        return "TIME-USD"

    def __call__(self):
        return "TIME-USD"


@dataclass(slots=True)
class TIME_USDT:
    name: str = "TIME-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TIME-USDT"

    def __str__(self):
        return "TIME-USDT"

    def __call__(self):
        return "TIME-USDT"


@dataclass(slots=True)
class TONE_USD:
    name: str = "TONE-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TONE-USD"

    def __str__(self):
        return "TONE-USD"

    def __call__(self):
        return "TONE-USD"


@dataclass(slots=True)
class TRAC_EUR:
    name: str = "TRAC-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRAC-EUR"

    def __str__(self):
        return "TRAC-EUR"

    def __call__(self):
        return "TRAC-EUR"


@dataclass(slots=True)
class TRAC_USD:
    name: str = "TRAC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRAC-USD"

    def __str__(self):
        return "TRAC-USD"

    def __call__(self):
        return "TRAC-USD"


@dataclass(slots=True)
class TRAC_USDT:
    name: str = "TRAC-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRAC-USDT"

    def __str__(self):
        return "TRAC-USDT"

    def __call__(self):
        return "TRAC-USDT"


@dataclass(slots=True)
class TRB_BTC:
    name: str = "TRB-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRB-BTC"

    def __str__(self):
        return "TRB-BTC"

    def __call__(self):
        return "TRB-BTC"


@dataclass(slots=True)
class TRB_USD:
    name: str = "TRB-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRB-USD"

    def __str__(self):
        return "TRB-USD"

    def __call__(self):
        return "TRB-USD"


@dataclass(slots=True)
class TRIBE_USD:
    name: str = "TRIBE-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRIBE-USD"

    def __str__(self):
        return "TRIBE-USD"

    def __call__(self):
        return "TRIBE-USD"


@dataclass(slots=True)
class TRU_BTC:
    name: str = "TRU-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRU-BTC"

    def __str__(self):
        return "TRU-BTC"

    def __call__(self):
        return "TRU-BTC"


@dataclass(slots=True)
class TRU_EUR:
    name: str = "TRU-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRU-EUR"

    def __str__(self):
        return "TRU-EUR"

    def __call__(self):
        return "TRU-EUR"


@dataclass(slots=True)
class TRU_USD:
    name: str = "TRU-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRU-USD"

    def __str__(self):
        return "TRU-USD"

    def __call__(self):
        return "TRU-USD"


@dataclass(slots=True)
class TRU_USDT:
    name: str = "TRU-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "TRU-USDT"

    def __str__(self):
        return "TRU-USDT"

    def __call__(self):
        return "TRU-USDT"


@dataclass(slots=True)
class UMA_BTC:
    name: str = "UMA-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UMA-BTC"

    def __str__(self):
        return "UMA-BTC"

    def __call__(self):
        return "UMA-BTC"


@dataclass(slots=True)
class UMA_EUR:
    name: str = "UMA-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UMA-EUR"

    def __str__(self):
        return "UMA-EUR"

    def __call__(self):
        return "UMA-EUR"


@dataclass(slots=True)
class UMA_GBP:
    name: str = "UMA-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UMA-GBP"

    def __str__(self):
        return "UMA-GBP"

    def __call__(self):
        return "UMA-GBP"


@dataclass(slots=True)
class UMA_USD:
    name: str = "UMA-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UMA-USD"

    def __str__(self):
        return "UMA-USD"

    def __call__(self):
        return "UMA-USD"


@dataclass(slots=True)
class UNFI_USD:
    name: str = "UNFI-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UNFI-USD"

    def __str__(self):
        return "UNFI-USD"

    def __call__(self):
        return "UNFI-USD"


@dataclass(slots=True)
class UNI_BTC:
    name: str = "UNI-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UNI-BTC"

    def __str__(self):
        return "UNI-BTC"

    def __call__(self):
        return "UNI-BTC"


@dataclass(slots=True)
class UNI_EUR:
    name: str = "UNI-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UNI-EUR"

    def __str__(self):
        return "UNI-EUR"

    def __call__(self):
        return "UNI-EUR"


@dataclass(slots=True)
class UNI_GBP:
    name: str = "UNI-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UNI-GBP"

    def __str__(self):
        return "UNI-GBP"

    def __call__(self):
        return "UNI-GBP"


@dataclass(slots=True)
class UNI_USD:
    name: str = "UNI-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UNI-USD"

    def __str__(self):
        return "UNI-USD"

    def __call__(self):
        return "UNI-USD"


@dataclass(slots=True)
class UPI_USD:
    name: str = "UPI-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UPI-USD"

    def __str__(self):
        return "UPI-USD"

    def __call__(self):
        return "UPI-USD"


@dataclass(slots=True)
class UPI_USDT:
    name: str = "UPI-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UPI-USDT"

    def __str__(self):
        return "UPI-USDT"

    def __call__(self):
        return "UPI-USDT"


@dataclass(slots=True)
class USDC_EUR:
    name: str = "USDC-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "USDC-EUR"

    def __str__(self):
        return "USDC-EUR"

    def __call__(self):
        return "USDC-EUR"


@dataclass(slots=True)
class USDC_GBP:
    name: str = "USDC-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "USDC-GBP"

    def __str__(self):
        return "USDC-GBP"

    def __call__(self):
        return "USDC-GBP"


@dataclass(slots=True)
class USDT_EUR:
    name: str = "USDT-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "USDT-EUR"

    def __str__(self):
        return "USDT-EUR"

    def __call__(self):
        return "USDT-EUR"


@dataclass(slots=True)
class USDT_GBP:
    name: str = "USDT-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "USDT-GBP"

    def __str__(self):
        return "USDT-GBP"

    def __call__(self):
        return "USDT-GBP"


@dataclass(slots=True)
class USDT_USD:
    name: str = "USDT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "USDT-USD"

    def __str__(self):
        return "USDT-USD"

    def __call__(self):
        return "USDT-USD"


@dataclass(slots=True)
class USDT_USDC:
    name: str = "USDT-USDC"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "USDT-USDC"

    def __str__(self):
        return "USDT-USDC"

    def __call__(self):
        return "USDT-USDC"


@dataclass(slots=True)
class UST_EUR:
    name: str = "UST-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UST-EUR"

    def __str__(self):
        return "UST-EUR"

    def __call__(self):
        return "UST-EUR"


@dataclass(slots=True)
class UST_USD:
    name: str = "UST-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UST-USD"

    def __str__(self):
        return "UST-USD"

    def __call__(self):
        return "UST-USD"


@dataclass(slots=True)
class UST_USDT:
    name: str = "UST-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "UST-USDT"

    def __str__(self):
        return "UST-USDT"

    def __call__(self):
        return "UST-USDT"


@dataclass(slots=True)
class VGX_EUR:
    name: str = "VGX-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "VGX-EUR"

    def __str__(self):
        return "VGX-EUR"

    def __call__(self):
        return "VGX-EUR"


@dataclass(slots=True)
class VGX_USD:
    name: str = "VGX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "VGX-USD"

    def __str__(self):
        return "VGX-USD"

    def __call__(self):
        return "VGX-USD"


@dataclass(slots=True)
class VGX_USDT:
    name: str = "VGX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "VGX-USDT"

    def __str__(self):
        return "VGX-USDT"

    def __call__(self):
        return "VGX-USDT"


@dataclass(slots=True)
class WAMPL_USD:
    name: str = "WAMPL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WAMPL-USD"

    def __str__(self):
        return "WAMPL-USD"

    def __call__(self):
        return "WAMPL-USD"


@dataclass(slots=True)
class WAMPL_USDT:
    name: str = "WAMPL-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WAMPL-USDT"

    def __str__(self):
        return "WAMPL-USDT"

    def __call__(self):
        return "WAMPL-USDT"


@dataclass(slots=True)
class WAXL_USD:
    name: str = "WAXL-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WAXL-USD"

    def __str__(self):
        return "WAXL-USD"

    def __call__(self):
        return "WAXL-USD"


@dataclass(slots=True)
class WBTC_BTC:
    name: str = "WBTC-BTC"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WBTC-BTC"

    def __str__(self):
        return "WBTC-BTC"

    def __call__(self):
        return "WBTC-BTC"


@dataclass(slots=True)
class WBTC_USD:
    name: str = "WBTC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WBTC-USD"

    def __str__(self):
        return "WBTC-USD"

    def __call__(self):
        return "WBTC-USD"


@dataclass(slots=True)
class WCFG_BTC:
    name: str = "WCFG-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WCFG-BTC"

    def __str__(self):
        return "WCFG-BTC"

    def __call__(self):
        return "WCFG-BTC"


@dataclass(slots=True)
class WCFG_EUR:
    name: str = "WCFG-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WCFG-EUR"

    def __str__(self):
        return "WCFG-EUR"

    def __call__(self):
        return "WCFG-EUR"


@dataclass(slots=True)
class WCFG_USD:
    name: str = "WCFG-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WCFG-USD"

    def __str__(self):
        return "WCFG-USD"

    def __call__(self):
        return "WCFG-USD"


@dataclass(slots=True)
class WCFG_USDT:
    name: str = "WCFG-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WCFG-USDT"

    def __str__(self):
        return "WCFG-USDT"

    def __call__(self):
        return "WCFG-USDT"


@dataclass(slots=True)
class WLUNA_EUR:
    name: str = "WLUNA-EUR"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WLUNA-EUR"

    def __str__(self):
        return "WLUNA-EUR"

    def __call__(self):
        return "WLUNA-EUR"


@dataclass(slots=True)
class WLUNA_GBP:
    name: str = "WLUNA-GBP"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WLUNA-GBP"

    def __str__(self):
        return "WLUNA-GBP"

    def __call__(self):
        return "WLUNA-GBP"


@dataclass(slots=True)
class WLUNA_USD:
    name: str = "WLUNA-USD"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WLUNA-USD"

    def __str__(self):
        return "WLUNA-USD"

    def __call__(self):
        return "WLUNA-USD"


@dataclass(slots=True)
class WLUNA_USDT:
    name: str = "WLUNA-USDT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "WLUNA-USDT"

    def __str__(self):
        return "WLUNA-USDT"

    def __call__(self):
        return "WLUNA-USDT"


@dataclass(slots=True)
class XCN_USD:
    name: str = "XCN-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XCN-USD"

    def __str__(self):
        return "XCN-USD"

    def __call__(self):
        return "XCN-USD"


@dataclass(slots=True)
class XCN_USDT:
    name: str = "XCN-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XCN-USDT"

    def __str__(self):
        return "XCN-USDT"

    def __call__(self):
        return "XCN-USDT"


@dataclass(slots=True)
class XLM_BTC:
    name: str = "XLM-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XLM-BTC"

    def __str__(self):
        return "XLM-BTC"

    def __call__(self):
        return "XLM-BTC"


@dataclass(slots=True)
class XLM_EUR:
    name: str = "XLM-EUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XLM-EUR"

    def __str__(self):
        return "XLM-EUR"

    def __call__(self):
        return "XLM-EUR"


@dataclass(slots=True)
class XLM_USD:
    name: str = "XLM-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XLM-USD"

    def __str__(self):
        return "XLM-USD"

    def __call__(self):
        return "XLM-USD"


@dataclass(slots=True)
class XLM_USDT:
    name: str = "XLM-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XLM-USDT"

    def __str__(self):
        return "XLM-USDT"

    def __call__(self):
        return "XLM-USDT"


@dataclass(slots=True)
class XRP_BTC:
    name: str = "XRP-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.001
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XRP-BTC"

    def __str__(self):
        return "XRP-BTC"

    def __call__(self):
        return "XRP-BTC"


@dataclass(slots=True)
class XRP_EUR:
    name: str = "XRP-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 10
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XRP-EUR"

    def __str__(self):
        return "XRP-EUR"

    def __call__(self):
        return "XRP-EUR"


@dataclass(slots=True)
class XRP_GBP:
    name: str = "XRP-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 10
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XRP-GBP"

    def __str__(self):
        return "XRP-GBP"

    def __call__(self):
        return "XRP-GBP"


@dataclass(slots=True)
class XRP_USD:
    name: str = "XRP-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 10
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XRP-USD"

    def __str__(self):
        return "XRP-USD"

    def __call__(self):
        return "XRP-USD"


@dataclass(slots=True)
class XTZ_BTC:
    name: str = "XTZ-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XTZ-BTC"

    def __str__(self):
        return "XTZ-BTC"

    def __call__(self):
        return "XTZ-BTC"


@dataclass(slots=True)
class XTZ_EUR:
    name: str = "XTZ-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XTZ-EUR"

    def __str__(self):
        return "XTZ-EUR"

    def __call__(self):
        return "XTZ-EUR"


@dataclass(slots=True)
class XTZ_GBP:
    name: str = "XTZ-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XTZ-GBP"

    def __str__(self):
        return "XTZ-GBP"

    def __call__(self):
        return "XTZ-GBP"


@dataclass(slots=True)
class XTZ_USD:
    name: str = "XTZ-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XTZ-USD"

    def __str__(self):
        return "XTZ-USD"

    def __call__(self):
        return "XTZ-USD"


@dataclass(slots=True)
class XYO_BTC:
    name: str = "XYO-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XYO-BTC"

    def __str__(self):
        return "XYO-BTC"

    def __call__(self):
        return "XYO-BTC"


@dataclass(slots=True)
class XYO_EUR:
    name: str = "XYO-EUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XYO-EUR"

    def __str__(self):
        return "XYO-EUR"

    def __call__(self):
        return "XYO-EUR"


@dataclass(slots=True)
class XYO_USD:
    name: str = "XYO-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XYO-USD"

    def __str__(self):
        return "XYO-USD"

    def __call__(self):
        return "XYO-USD"


@dataclass(slots=True)
class XYO_USDT:
    name: str = "XYO-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "XYO-USDT"

    def __str__(self):
        return "XYO-USDT"

    def __call__(self):
        return "XYO-USDT"


@dataclass(slots=True)
class YFI_BTC:
    name: str = "YFI-BTC"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "YFI-BTC"

    def __str__(self):
        return "YFI-BTC"

    def __call__(self):
        return "YFI-BTC"


@dataclass(slots=True)
class YFI_USD:
    name: str = "YFI-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "YFI-USD"

    def __str__(self):
        return "YFI-USD"

    def __call__(self):
        return "YFI-USD"


@dataclass(slots=True)
class YFII_USD:
    name: str = "YFII-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "YFII-USD"

    def __str__(self):
        return "YFII-USD"

    def __call__(self):
        return "YFII-USD"


@dataclass(slots=True)
class ZEC_BTC:
    name: str = "ZEC-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ZEC-BTC"

    def __str__(self):
        return "ZEC-BTC"

    def __call__(self):
        return "ZEC-BTC"


@dataclass(slots=True)
class ZEC_USD:
    name: str = "ZEC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ZEC-USD"

    def __str__(self):
        return "ZEC-USD"

    def __call__(self):
        return "ZEC-USD"


@dataclass(slots=True)
class ZEC_USDC:
    name: str = "ZEC-USDC"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ZEC-USDC"

    def __str__(self):
        return "ZEC-USDC"

    def __call__(self):
        return "ZEC-USDC"


@dataclass(slots=True)
class ZEN_BTC:
    name: str = "ZEN-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ZEN-BTC"

    def __str__(self):
        return "ZEN-BTC"

    def __call__(self):
        return "ZEN-BTC"


@dataclass(slots=True)
class ZEN_USD:
    name: str = "ZEN-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ZEN-USD"

    def __str__(self):
        return "ZEN-USD"

    def __call__(self):
        return "ZEN-USD"


@dataclass(slots=True)
class ZEN_USDT:
    name: str = "ZEN-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ZEN-USDT"

    def __str__(self):
        return "ZEN-USDT"

    def __call__(self):
        return "ZEN-USDT"


@dataclass(slots=True)
class ZRX_BTC:
    name: str = "ZRX-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ZRX-BTC"

    def __str__(self):
        return "ZRX-BTC"

    def __call__(self):
        return "ZRX-BTC"


@dataclass(slots=True)
class ZRX_EUR:
    name: str = "ZRX-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ZRX-EUR"

    def __str__(self):
        return "ZRX-EUR"

    def __call__(self):
        return "ZRX-EUR"


@dataclass(slots=True)
class ZRX_USD:
    name: str = "ZRX-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __repr__(self):
        return "ZRX-USD"

    def __str__(self):
        return "ZRX-USD"

    def __call__(self):
        return "ZRX-USD"


