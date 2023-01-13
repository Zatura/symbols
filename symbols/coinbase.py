from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
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


ZERO0_USD = ZERO0_USD()


@dataclass(slots=True, frozen=True)
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


ONEINCH_BTC = ONEINCH_BTC()


@dataclass(slots=True, frozen=True)
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


ONEINCH_EUR = ONEINCH_EUR()


@dataclass(slots=True, frozen=True)
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


ONEINCH_GBP = ONEINCH_GBP()


@dataclass(slots=True, frozen=True)
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


ONEINCH_USD = ONEINCH_USD()


@dataclass(slots=True, frozen=True)
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


AAVE_BTC = AAVE_BTC()


@dataclass(slots=True, frozen=True)
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


AAVE_EUR = AAVE_EUR()


@dataclass(slots=True, frozen=True)
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


AAVE_GBP = AAVE_GBP()


@dataclass(slots=True, frozen=True)
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


AAVE_USD = AAVE_USD()


@dataclass(slots=True, frozen=True)
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


ABT_USD = ABT_USD()


@dataclass(slots=True, frozen=True)
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


ACH_USD = ACH_USD()


@dataclass(slots=True, frozen=True)
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


ACH_USDT = ACH_USDT()


@dataclass(slots=True, frozen=True)
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


ADA_BTC = ADA_BTC()


@dataclass(slots=True, frozen=True)
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


ADA_ETH = ADA_ETH()


@dataclass(slots=True, frozen=True)
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


ADA_EUR = ADA_EUR()


@dataclass(slots=True, frozen=True)
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


ADA_GBP = ADA_GBP()


@dataclass(slots=True, frozen=True)
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


ADA_USD = ADA_USD()


@dataclass(slots=True, frozen=True)
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


ADA_USDC = ADA_USDC()


@dataclass(slots=True, frozen=True)
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


ADA_USDT = ADA_USDT()


@dataclass(slots=True, frozen=True)
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


AERGO_USD = AERGO_USD()


@dataclass(slots=True, frozen=True)
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


AGLD_USD = AGLD_USD()


@dataclass(slots=True, frozen=True)
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


AGLD_USDT = AGLD_USDT()


@dataclass(slots=True, frozen=True)
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


AIOZ_USD = AIOZ_USD()


@dataclass(slots=True, frozen=True)
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


AIOZ_USDT = AIOZ_USDT()


@dataclass(slots=True, frozen=True)
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


ALCX_EUR = ALCX_EUR()


@dataclass(slots=True, frozen=True)
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


ALCX_USD = ALCX_USD()


@dataclass(slots=True, frozen=True)
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


ALCX_USDT = ALCX_USDT()


@dataclass(slots=True, frozen=True)
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


ALEPH_USD = ALEPH_USD()


@dataclass(slots=True, frozen=True)
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


ALGO_BTC = ALGO_BTC()


@dataclass(slots=True, frozen=True)
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


ALGO_EUR = ALGO_EUR()


@dataclass(slots=True, frozen=True)
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


ALGO_GBP = ALGO_GBP()


@dataclass(slots=True, frozen=True)
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


ALGO_USD = ALGO_USD()


@dataclass(slots=True, frozen=True)
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


ALICE_USD = ALICE_USD()


@dataclass(slots=True, frozen=True)
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


AMP_USD = AMP_USD()


@dataclass(slots=True, frozen=True)
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


ANKR_BTC = ANKR_BTC()


@dataclass(slots=True, frozen=True)
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


ANKR_EUR = ANKR_EUR()


@dataclass(slots=True, frozen=True)
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


ANKR_GBP = ANKR_GBP()


@dataclass(slots=True, frozen=True)
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


ANKR_USD = ANKR_USD()


@dataclass(slots=True, frozen=True)
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


ANT_USD = ANT_USD()


@dataclass(slots=True, frozen=True)
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


APE_EUR = APE_EUR()


@dataclass(slots=True, frozen=True)
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


APE_USD = APE_USD()


@dataclass(slots=True, frozen=True)
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


APE_USDT = APE_USDT()


@dataclass(slots=True, frozen=True)
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


API3_USD = API3_USD()


@dataclass(slots=True, frozen=True)
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


API3_USDT = API3_USDT()


@dataclass(slots=True, frozen=True)
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


APT_USD = APT_USD()


@dataclass(slots=True, frozen=True)
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


APT_USDT = APT_USDT()


@dataclass(slots=True, frozen=True)
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


ARPA_EUR = ARPA_EUR()


@dataclass(slots=True, frozen=True)
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


ARPA_USD = ARPA_USD()


@dataclass(slots=True, frozen=True)
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


ARPA_USDT = ARPA_USDT()


@dataclass(slots=True, frozen=True)
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


ASM_USD = ASM_USD()


@dataclass(slots=True, frozen=True)
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


ASM_USDT = ASM_USDT()


@dataclass(slots=True, frozen=True)
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


AST_USD = AST_USD()


@dataclass(slots=True, frozen=True)
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


ATA_USD = ATA_USD()


@dataclass(slots=True, frozen=True)
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


ATA_USDT = ATA_USDT()


@dataclass(slots=True, frozen=True)
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


ATOM_BTC = ATOM_BTC()


@dataclass(slots=True, frozen=True)
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


ATOM_EUR = ATOM_EUR()


@dataclass(slots=True, frozen=True)
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


ATOM_GBP = ATOM_GBP()


@dataclass(slots=True, frozen=True)
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


ATOM_USD = ATOM_USD()


@dataclass(slots=True, frozen=True)
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


ATOM_USDT = ATOM_USDT()


@dataclass(slots=True, frozen=True)
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


AUCTION_EUR = AUCTION_EUR()


@dataclass(slots=True, frozen=True)
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


AUCTION_USD = AUCTION_USD()


@dataclass(slots=True, frozen=True)
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


AUCTION_USDT = AUCTION_USDT()


@dataclass(slots=True, frozen=True)
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


AURORA_USD = AURORA_USD()


@dataclass(slots=True, frozen=True)
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


AVAX_BTC = AVAX_BTC()


@dataclass(slots=True, frozen=True)
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


AVAX_EUR = AVAX_EUR()


@dataclass(slots=True, frozen=True)
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


AVAX_USD = AVAX_USD()


@dataclass(slots=True, frozen=True)
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


AVAX_USDT = AVAX_USDT()


@dataclass(slots=True, frozen=True)
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


AVT_USD = AVT_USD()


@dataclass(slots=True, frozen=True)
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


AXS_BTC = AXS_BTC()


@dataclass(slots=True, frozen=True)
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


AXS_EUR = AXS_EUR()


@dataclass(slots=True, frozen=True)
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


AXS_USD = AXS_USD()


@dataclass(slots=True, frozen=True)
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


AXS_USDT = AXS_USDT()


@dataclass(slots=True, frozen=True)
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


BADGER_EUR = BADGER_EUR()


@dataclass(slots=True, frozen=True)
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


BADGER_USD = BADGER_USD()


@dataclass(slots=True, frozen=True)
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


BADGER_USDT = BADGER_USDT()


@dataclass(slots=True, frozen=True)
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


BAL_BTC = BAL_BTC()


@dataclass(slots=True, frozen=True)
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


BAL_USD = BAL_USD()


@dataclass(slots=True, frozen=True)
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


BAND_BTC = BAND_BTC()


@dataclass(slots=True, frozen=True)
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


BAND_EUR = BAND_EUR()


@dataclass(slots=True, frozen=True)
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


BAND_GBP = BAND_GBP()


@dataclass(slots=True, frozen=True)
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


BAND_USD = BAND_USD()


@dataclass(slots=True, frozen=True)
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


BAT_BTC = BAT_BTC()


@dataclass(slots=True, frozen=True)
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


BAT_ETH = BAT_ETH()


@dataclass(slots=True, frozen=True)
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


BAT_EUR = BAT_EUR()


@dataclass(slots=True, frozen=True)
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


BAT_USD = BAT_USD()


@dataclass(slots=True, frozen=True)
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


BAT_USDC = BAT_USDC()


@dataclass(slots=True, frozen=True)
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


BCH_BTC = BCH_BTC()


@dataclass(slots=True, frozen=True)
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


BCH_EUR = BCH_EUR()


@dataclass(slots=True, frozen=True)
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


BCH_GBP = BCH_GBP()


@dataclass(slots=True, frozen=True)
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


BCH_USD = BCH_USD()


@dataclass(slots=True, frozen=True)
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


BICO_EUR = BICO_EUR()


@dataclass(slots=True, frozen=True)
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


BICO_USD = BICO_USD()


@dataclass(slots=True, frozen=True)
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


BICO_USDT = BICO_USDT()


@dataclass(slots=True, frozen=True)
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


BIT_USD = BIT_USD()


@dataclass(slots=True, frozen=True)
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


BIT_USDT = BIT_USDT()


@dataclass(slots=True, frozen=True)
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


BLZ_USD = BLZ_USD()


@dataclass(slots=True, frozen=True)
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


BNT_BTC = BNT_BTC()


@dataclass(slots=True, frozen=True)
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


BNT_EUR = BNT_EUR()


@dataclass(slots=True, frozen=True)
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


BNT_GBP = BNT_GBP()


@dataclass(slots=True, frozen=True)
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


BNT_USD = BNT_USD()


@dataclass(slots=True, frozen=True)
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


BOBA_USD = BOBA_USD()


@dataclass(slots=True, frozen=True)
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


BOBA_USDT = BOBA_USDT()


@dataclass(slots=True, frozen=True)
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


BOND_USD = BOND_USD()


@dataclass(slots=True, frozen=True)
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


BOND_USDT = BOND_USDT()


@dataclass(slots=True, frozen=True)
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


BTC_EUR = BTC_EUR()


@dataclass(slots=True, frozen=True)
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


BTC_GBP = BTC_GBP()


@dataclass(slots=True, frozen=True)
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


BTC_USD = BTC_USD()


@dataclass(slots=True, frozen=True)
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


BTC_USDC = BTC_USDC()


@dataclass(slots=True, frozen=True)
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


BTC_USDT = BTC_USDT()


@dataclass(slots=True, frozen=True)
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


BTRST_BTC = BTRST_BTC()


@dataclass(slots=True, frozen=True)
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


BTRST_EUR = BTRST_EUR()


@dataclass(slots=True, frozen=True)
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


BTRST_GBP = BTRST_GBP()


@dataclass(slots=True, frozen=True)
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


BTRST_USD = BTRST_USD()


@dataclass(slots=True, frozen=True)
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


BTRST_USDT = BTRST_USDT()


@dataclass(slots=True, frozen=True)
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


BUSD_USD = BUSD_USD()


@dataclass(slots=True, frozen=True)
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


C98_USD = C98_USD()


@dataclass(slots=True, frozen=True)
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


C98_USDT = C98_USDT()


@dataclass(slots=True, frozen=True)
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


CBETH_ETH = CBETH_ETH()


@dataclass(slots=True, frozen=True)
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


CBETH_USD = CBETH_USD()


@dataclass(slots=True, frozen=True)
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


CELR_USD = CELR_USD()


@dataclass(slots=True, frozen=True)
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


CGLD_BTC = CGLD_BTC()


@dataclass(slots=True, frozen=True)
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


CGLD_EUR = CGLD_EUR()


@dataclass(slots=True, frozen=True)
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


CGLD_GBP = CGLD_GBP()


@dataclass(slots=True, frozen=True)
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


CGLD_USD = CGLD_USD()


@dataclass(slots=True, frozen=True)
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


CHZ_EUR = CHZ_EUR()


@dataclass(slots=True, frozen=True)
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


CHZ_GBP = CHZ_GBP()


@dataclass(slots=True, frozen=True)
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


CHZ_USD = CHZ_USD()


@dataclass(slots=True, frozen=True)
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


CHZ_USDT = CHZ_USDT()


@dataclass(slots=True, frozen=True)
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


CLV_EUR = CLV_EUR()


@dataclass(slots=True, frozen=True)
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


CLV_GBP = CLV_GBP()


@dataclass(slots=True, frozen=True)
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


CLV_USD = CLV_USD()


@dataclass(slots=True, frozen=True)
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


CLV_USDT = CLV_USDT()


@dataclass(slots=True, frozen=True)
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


COMP_BTC = COMP_BTC()


@dataclass(slots=True, frozen=True)
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


COMP_USD = COMP_USD()


@dataclass(slots=True, frozen=True)
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


COTI_USD = COTI_USD()


@dataclass(slots=True, frozen=True)
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


COVAL_USD = COVAL_USD()


@dataclass(slots=True, frozen=True)
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


COVAL_USDT = COVAL_USDT()


@dataclass(slots=True, frozen=True)
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


CRO_EUR = CRO_EUR()


@dataclass(slots=True, frozen=True)
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


CRO_USD = CRO_USD()


@dataclass(slots=True, frozen=True)
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


CRO_USDT = CRO_USDT()


@dataclass(slots=True, frozen=True)
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


CRPT_USD = CRPT_USD()


@dataclass(slots=True, frozen=True)
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


CRV_BTC = CRV_BTC()


@dataclass(slots=True, frozen=True)
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


CRV_EUR = CRV_EUR()


@dataclass(slots=True, frozen=True)
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


CRV_GBP = CRV_GBP()


@dataclass(slots=True, frozen=True)
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


CRV_USD = CRV_USD()


@dataclass(slots=True, frozen=True)
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


CTSI_BTC = CTSI_BTC()


@dataclass(slots=True, frozen=True)
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


CTSI_USD = CTSI_USD()


@dataclass(slots=True, frozen=True)
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


CTX_EUR = CTX_EUR()


@dataclass(slots=True, frozen=True)
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


CTX_USD = CTX_USD()


@dataclass(slots=True, frozen=True)
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


CTX_USDT = CTX_USDT()


@dataclass(slots=True, frozen=True)
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


CVC_USD = CVC_USD()


@dataclass(slots=True, frozen=True)
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


CVC_USDC = CVC_USDC()


@dataclass(slots=True, frozen=True)
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


CVX_USD = CVX_USD()


@dataclass(slots=True, frozen=True)
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


DAI_USD = DAI_USD()


@dataclass(slots=True, frozen=True)
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


DAI_USDC = DAI_USDC()


@dataclass(slots=True, frozen=True)
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


DAR_USD = DAR_USD()


@dataclass(slots=True, frozen=True)
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


DASH_BTC = DASH_BTC()


@dataclass(slots=True, frozen=True)
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


DASH_USD = DASH_USD()


@dataclass(slots=True, frozen=True)
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


DDX_EUR = DDX_EUR()


@dataclass(slots=True, frozen=True)
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


DDX_USD = DDX_USD()


@dataclass(slots=True, frozen=True)
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


DDX_USDT = DDX_USDT()


@dataclass(slots=True, frozen=True)
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


DESO_EUR = DESO_EUR()


@dataclass(slots=True, frozen=True)
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


DESO_USD = DESO_USD()


@dataclass(slots=True, frozen=True)
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


DESO_USDT = DESO_USDT()


@dataclass(slots=True, frozen=True)
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


DEXT_USD = DEXT_USD()


@dataclass(slots=True, frozen=True)
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


DIA_EUR = DIA_EUR()


@dataclass(slots=True, frozen=True)
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


DIA_USD = DIA_USD()


@dataclass(slots=True, frozen=True)
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


DIA_USDT = DIA_USDT()


@dataclass(slots=True, frozen=True)
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


DNT_USD = DNT_USD()


@dataclass(slots=True, frozen=True)
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


DNT_USDC = DNT_USDC()


@dataclass(slots=True, frozen=True)
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


DOGE_BTC = DOGE_BTC()


@dataclass(slots=True, frozen=True)
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


DOGE_EUR = DOGE_EUR()


@dataclass(slots=True, frozen=True)
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


DOGE_GBP = DOGE_GBP()


@dataclass(slots=True, frozen=True)
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


DOGE_USD = DOGE_USD()


@dataclass(slots=True, frozen=True)
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


DOGE_USDT = DOGE_USDT()


@dataclass(slots=True, frozen=True)
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


DOT_BTC = DOT_BTC()


@dataclass(slots=True, frozen=True)
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


DOT_EUR = DOT_EUR()


@dataclass(slots=True, frozen=True)
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


DOT_GBP = DOT_GBP()


@dataclass(slots=True, frozen=True)
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


DOT_USD = DOT_USD()


@dataclass(slots=True, frozen=True)
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


DOT_USDT = DOT_USDT()


@dataclass(slots=True, frozen=True)
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


DREP_USD = DREP_USD()


@dataclass(slots=True, frozen=True)
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


DREP_USDT = DREP_USDT()


@dataclass(slots=True, frozen=True)
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


DYP_USD = DYP_USD()


@dataclass(slots=True, frozen=True)
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


DYP_USDT = DYP_USDT()


@dataclass(slots=True, frozen=True)
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


EGLD_USD = EGLD_USD()


@dataclass(slots=True, frozen=True)
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


ELA_USD = ELA_USD()


@dataclass(slots=True, frozen=True)
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


ELA_USDT = ELA_USDT()


@dataclass(slots=True, frozen=True)
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


ENJ_BTC = ENJ_BTC()


@dataclass(slots=True, frozen=True)
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


ENJ_USD = ENJ_USD()


@dataclass(slots=True, frozen=True)
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


ENJ_USDT = ENJ_USDT()


@dataclass(slots=True, frozen=True)
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


ENS_EUR = ENS_EUR()


@dataclass(slots=True, frozen=True)
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


ENS_USD = ENS_USD()


@dataclass(slots=True, frozen=True)
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


ENS_USDT = ENS_USDT()


@dataclass(slots=True, frozen=True)
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


EOS_BTC = EOS_BTC()


@dataclass(slots=True, frozen=True)
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


EOS_EUR = EOS_EUR()


@dataclass(slots=True, frozen=True)
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


EOS_USD = EOS_USD()


@dataclass(slots=True, frozen=True)
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


ERN_EUR = ERN_EUR()


@dataclass(slots=True, frozen=True)
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


ERN_USD = ERN_USD()


@dataclass(slots=True, frozen=True)
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


ERN_USDT = ERN_USDT()


@dataclass(slots=True, frozen=True)
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


ETC_BTC = ETC_BTC()


@dataclass(slots=True, frozen=True)
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


ETC_EUR = ETC_EUR()


@dataclass(slots=True, frozen=True)
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


ETC_GBP = ETC_GBP()


@dataclass(slots=True, frozen=True)
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


ETC_USD = ETC_USD()


@dataclass(slots=True, frozen=True)
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


ETH_BTC = ETH_BTC()


@dataclass(slots=True, frozen=True)
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


ETH_DAI = ETH_DAI()


@dataclass(slots=True, frozen=True)
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


ETH_EUR = ETH_EUR()


@dataclass(slots=True, frozen=True)
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


ETH_GBP = ETH_GBP()


@dataclass(slots=True, frozen=True)
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


ETH_USD = ETH_USD()


@dataclass(slots=True, frozen=True)
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


ETH_USDC = ETH_USDC()


@dataclass(slots=True, frozen=True)
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


ETH_USDT = ETH_USDT()


@dataclass(slots=True, frozen=True)
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


FARM_USD = FARM_USD()


@dataclass(slots=True, frozen=True)
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


FARM_USDT = FARM_USDT()


@dataclass(slots=True, frozen=True)
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


FET_USD = FET_USD()


@dataclass(slots=True, frozen=True)
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


FET_USDT = FET_USDT()


@dataclass(slots=True, frozen=True)
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


FIDA_EUR = FIDA_EUR()


@dataclass(slots=True, frozen=True)
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


FIDA_USD = FIDA_USD()


@dataclass(slots=True, frozen=True)
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


FIDA_USDT = FIDA_USDT()


@dataclass(slots=True, frozen=True)
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


FIL_BTC = FIL_BTC()


@dataclass(slots=True, frozen=True)
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


FIL_EUR = FIL_EUR()


@dataclass(slots=True, frozen=True)
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


FIL_GBP = FIL_GBP()


@dataclass(slots=True, frozen=True)
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


FIL_USD = FIL_USD()


@dataclass(slots=True, frozen=True)
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


FIS_USD = FIS_USD()


@dataclass(slots=True, frozen=True)
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


FIS_USDT = FIS_USDT()


@dataclass(slots=True, frozen=True)
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


FLOW_USD = FLOW_USD()


@dataclass(slots=True, frozen=True)
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


FLOW_USDT = FLOW_USDT()


@dataclass(slots=True, frozen=True)
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


FORT_USD = FORT_USD()


@dataclass(slots=True, frozen=True)
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


FORT_USDT = FORT_USDT()


@dataclass(slots=True, frozen=True)
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


FORTH_BTC = FORTH_BTC()


@dataclass(slots=True, frozen=True)
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


FORTH_EUR = FORTH_EUR()


@dataclass(slots=True, frozen=True)
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


FORTH_GBP = FORTH_GBP()


@dataclass(slots=True, frozen=True)
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


FORTH_USD = FORTH_USD()


@dataclass(slots=True, frozen=True)
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


FOX_USD = FOX_USD()


@dataclass(slots=True, frozen=True)
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


FOX_USDT = FOX_USDT()


@dataclass(slots=True, frozen=True)
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


FX_USD = FX_USD()


@dataclass(slots=True, frozen=True)
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


GAL_USD = GAL_USD()


@dataclass(slots=True, frozen=True)
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


GAL_USDT = GAL_USDT()


@dataclass(slots=True, frozen=True)
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


GALA_EUR = GALA_EUR()


@dataclass(slots=True, frozen=True)
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


GALA_USD = GALA_USD()


@dataclass(slots=True, frozen=True)
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


GALA_USDT = GALA_USDT()


@dataclass(slots=True, frozen=True)
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


GFI_USD = GFI_USD()


@dataclass(slots=True, frozen=True)
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


GHST_USD = GHST_USD()


@dataclass(slots=True, frozen=True)
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


GLM_USD = GLM_USD()


@dataclass(slots=True, frozen=True)
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


GMT_USD = GMT_USD()


@dataclass(slots=True, frozen=True)
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


GMT_USDT = GMT_USDT()


@dataclass(slots=True, frozen=True)
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


GNO_USD = GNO_USD()


@dataclass(slots=True, frozen=True)
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


GNO_USDT = GNO_USDT()


@dataclass(slots=True, frozen=True)
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


GNT_USDC = GNT_USDC()


@dataclass(slots=True, frozen=True)
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


GODS_USD = GODS_USD()


@dataclass(slots=True, frozen=True)
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


GRT_BTC = GRT_BTC()


@dataclass(slots=True, frozen=True)
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


GRT_EUR = GRT_EUR()


@dataclass(slots=True, frozen=True)
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


GRT_GBP = GRT_GBP()


@dataclass(slots=True, frozen=True)
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


GRT_USD = GRT_USD()


@dataclass(slots=True, frozen=True)
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


GST_USD = GST_USD()


@dataclass(slots=True, frozen=True)
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


GTC_USD = GTC_USD()


@dataclass(slots=True, frozen=True)
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


GUSD_USD = GUSD_USD()


@dataclass(slots=True, frozen=True)
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


GYEN_USD = GYEN_USD()


@dataclass(slots=True, frozen=True)
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


HBAR_USD = HBAR_USD()


@dataclass(slots=True, frozen=True)
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


HBAR_USDT = HBAR_USDT()


@dataclass(slots=True, frozen=True)
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


HFT_USD = HFT_USD()


@dataclass(slots=True, frozen=True)
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


HFT_USDT = HFT_USDT()


@dataclass(slots=True, frozen=True)
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


HIGH_USD = HIGH_USD()


@dataclass(slots=True, frozen=True)
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


HOPR_USD = HOPR_USD()


@dataclass(slots=True, frozen=True)
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


HOPR_USDT = HOPR_USDT()


@dataclass(slots=True, frozen=True)
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


ICP_BTC = ICP_BTC()


@dataclass(slots=True, frozen=True)
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


ICP_EUR = ICP_EUR()


@dataclass(slots=True, frozen=True)
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


ICP_GBP = ICP_GBP()


@dataclass(slots=True, frozen=True)
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


ICP_USD = ICP_USD()


@dataclass(slots=True, frozen=True)
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


ICP_USDT = ICP_USDT()


@dataclass(slots=True, frozen=True)
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


IDEX_USD = IDEX_USD()


@dataclass(slots=True, frozen=True)
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


IDEX_USDT = IDEX_USDT()


@dataclass(slots=True, frozen=True)
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


ILV_USD = ILV_USD()


@dataclass(slots=True, frozen=True)
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


IMX_USD = IMX_USD()


@dataclass(slots=True, frozen=True)
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


IMX_USDT = IMX_USDT()


@dataclass(slots=True, frozen=True)
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


INDEX_USD = INDEX_USD()


@dataclass(slots=True, frozen=True)
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


INDEX_USDT = INDEX_USDT()


@dataclass(slots=True, frozen=True)
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


INJ_USD = INJ_USD()


@dataclass(slots=True, frozen=True)
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


INV_USD = INV_USD()


@dataclass(slots=True, frozen=True)
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


IOTX_EUR = IOTX_EUR()


@dataclass(slots=True, frozen=True)
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


IOTX_USD = IOTX_USD()


@dataclass(slots=True, frozen=True)
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


JASMY_USD = JASMY_USD()


@dataclass(slots=True, frozen=True)
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


JASMY_USDT = JASMY_USDT()


@dataclass(slots=True, frozen=True)
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


JUP_USD = JUP_USD()


@dataclass(slots=True, frozen=True)
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


KEEP_USD = KEEP_USD()


@dataclass(slots=True, frozen=True)
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


KNC_BTC = KNC_BTC()


@dataclass(slots=True, frozen=True)
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


KNC_USD = KNC_USD()


@dataclass(slots=True, frozen=True)
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


KRL_EUR = KRL_EUR()


@dataclass(slots=True, frozen=True)
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


KRL_USD = KRL_USD()


@dataclass(slots=True, frozen=True)
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


KRL_USDT = KRL_USDT()


@dataclass(slots=True, frozen=True)
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


KSM_USD = KSM_USD()


@dataclass(slots=True, frozen=True)
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


KSM_USDT = KSM_USDT()


@dataclass(slots=True, frozen=True)
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


LCX_EUR = LCX_EUR()


@dataclass(slots=True, frozen=True)
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


LCX_USD = LCX_USD()


@dataclass(slots=True, frozen=True)
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


LCX_USDT = LCX_USDT()


@dataclass(slots=True, frozen=True)
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


LDO_USD = LDO_USD()


@dataclass(slots=True, frozen=True)
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


LINK_BTC = LINK_BTC()


@dataclass(slots=True, frozen=True)
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


LINK_ETH = LINK_ETH()


@dataclass(slots=True, frozen=True)
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


LINK_EUR = LINK_EUR()


@dataclass(slots=True, frozen=True)
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


LINK_GBP = LINK_GBP()


@dataclass(slots=True, frozen=True)
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


LINK_USD = LINK_USD()


@dataclass(slots=True, frozen=True)
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


LINK_USDT = LINK_USDT()


@dataclass(slots=True, frozen=True)
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


LIT_USD = LIT_USD()


@dataclass(slots=True, frozen=True)
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


LOKA_USD = LOKA_USD()


@dataclass(slots=True, frozen=True)
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


LOOM_USD = LOOM_USD()


@dataclass(slots=True, frozen=True)
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


LOOM_USDC = LOOM_USDC()


@dataclass(slots=True, frozen=True)
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


LPT_USD = LPT_USD()


@dataclass(slots=True, frozen=True)
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


LQTY_EUR = LQTY_EUR()


@dataclass(slots=True, frozen=True)
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


LQTY_USD = LQTY_USD()


@dataclass(slots=True, frozen=True)
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


LQTY_USDT = LQTY_USDT()


@dataclass(slots=True, frozen=True)
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


LRC_BTC = LRC_BTC()


@dataclass(slots=True, frozen=True)
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


LRC_USD = LRC_USD()


@dataclass(slots=True, frozen=True)
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


LRC_USDT = LRC_USDT()


@dataclass(slots=True, frozen=True)
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


LTC_BTC = LTC_BTC()


@dataclass(slots=True, frozen=True)
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


LTC_EUR = LTC_EUR()


@dataclass(slots=True, frozen=True)
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


LTC_GBP = LTC_GBP()


@dataclass(slots=True, frozen=True)
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


LTC_USD = LTC_USD()


@dataclass(slots=True, frozen=True)
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


MAGIC_USD = MAGIC_USD()


@dataclass(slots=True, frozen=True)
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


MANA_BTC = MANA_BTC()


@dataclass(slots=True, frozen=True)
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


MANA_ETH = MANA_ETH()


@dataclass(slots=True, frozen=True)
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


MANA_EUR = MANA_EUR()


@dataclass(slots=True, frozen=True)
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


MANA_USD = MANA_USD()


@dataclass(slots=True, frozen=True)
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


MANA_USDC = MANA_USDC()


@dataclass(slots=True, frozen=True)
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


MASK_EUR = MASK_EUR()


@dataclass(slots=True, frozen=True)
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


MASK_GBP = MASK_GBP()


@dataclass(slots=True, frozen=True)
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


MASK_USD = MASK_USD()


@dataclass(slots=True, frozen=True)
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


MASK_USDT = MASK_USDT()


@dataclass(slots=True, frozen=True)
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


MATH_USD = MATH_USD()


@dataclass(slots=True, frozen=True)
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


MATH_USDT = MATH_USDT()


@dataclass(slots=True, frozen=True)
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


MATIC_BTC = MATIC_BTC()


@dataclass(slots=True, frozen=True)
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


MATIC_EUR = MATIC_EUR()


@dataclass(slots=True, frozen=True)
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


MATIC_GBP = MATIC_GBP()


@dataclass(slots=True, frozen=True)
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


MATIC_USD = MATIC_USD()


@dataclass(slots=True, frozen=True)
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


MATIC_USDT = MATIC_USDT()


@dataclass(slots=True, frozen=True)
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


MCO2_USD = MCO2_USD()


@dataclass(slots=True, frozen=True)
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


MCO2_USDT = MCO2_USDT()


@dataclass(slots=True, frozen=True)
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


MDT_USD = MDT_USD()


@dataclass(slots=True, frozen=True)
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


MDT_USDT = MDT_USDT()


@dataclass(slots=True, frozen=True)
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


MEDIA_USD = MEDIA_USD()


@dataclass(slots=True, frozen=True)
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


MEDIA_USDT = MEDIA_USDT()


@dataclass(slots=True, frozen=True)
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


METIS_USD = METIS_USD()


@dataclass(slots=True, frozen=True)
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


METIS_USDT = METIS_USDT()


@dataclass(slots=True, frozen=True)
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


MINA_EUR = MINA_EUR()


@dataclass(slots=True, frozen=True)
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


MINA_USD = MINA_USD()


@dataclass(slots=True, frozen=True)
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


MINA_USDT = MINA_USDT()


@dataclass(slots=True, frozen=True)
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


MIR_BTC = MIR_BTC()


@dataclass(slots=True, frozen=True)
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


MIR_EUR = MIR_EUR()


@dataclass(slots=True, frozen=True)
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


MIR_GBP = MIR_GBP()


@dataclass(slots=True, frozen=True)
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


MIR_USD = MIR_USD()


@dataclass(slots=True, frozen=True)
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


MKR_BTC = MKR_BTC()


@dataclass(slots=True, frozen=True)
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


MKR_USD = MKR_USD()


@dataclass(slots=True, frozen=True)
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


MLN_USD = MLN_USD()


@dataclass(slots=True, frozen=True)
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


MNDE_USD = MNDE_USD()


@dataclass(slots=True, frozen=True)
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


MONA_USD = MONA_USD()


@dataclass(slots=True, frozen=True)
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


MPL_USD = MPL_USD()


@dataclass(slots=True, frozen=True)
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


MSOL_USD = MSOL_USD()


@dataclass(slots=True, frozen=True)
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


MTL_USD = MTL_USD()


@dataclass(slots=True, frozen=True)
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


MUSD_USD = MUSD_USD()


@dataclass(slots=True, frozen=True)
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


MUSE_USD = MUSE_USD()


@dataclass(slots=True, frozen=True)
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


MXC_USD = MXC_USD()


@dataclass(slots=True, frozen=True)
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


NCT_EUR = NCT_EUR()


@dataclass(slots=True, frozen=True)
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


NCT_USD = NCT_USD()


@dataclass(slots=True, frozen=True)
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


NCT_USDT = NCT_USDT()


@dataclass(slots=True, frozen=True)
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


NEAR_USD = NEAR_USD()


@dataclass(slots=True, frozen=True)
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


NEAR_USDT = NEAR_USDT()


@dataclass(slots=True, frozen=True)
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


NEST_USD = NEST_USD()


@dataclass(slots=True, frozen=True)
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


NEST_USDT = NEST_USDT()


@dataclass(slots=True, frozen=True)
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


NKN_BTC = NKN_BTC()


@dataclass(slots=True, frozen=True)
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


NKN_EUR = NKN_EUR()


@dataclass(slots=True, frozen=True)
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


NKN_GBP = NKN_GBP()


@dataclass(slots=True, frozen=True)
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


NKN_USD = NKN_USD()


@dataclass(slots=True, frozen=True)
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


NMR_BTC = NMR_BTC()


@dataclass(slots=True, frozen=True)
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


NMR_EUR = NMR_EUR()


@dataclass(slots=True, frozen=True)
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


NMR_GBP = NMR_GBP()


@dataclass(slots=True, frozen=True)
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


NMR_USD = NMR_USD()


@dataclass(slots=True, frozen=True)
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


NU_BTC = NU_BTC()


@dataclass(slots=True, frozen=True)
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


NU_EUR = NU_EUR()


@dataclass(slots=True, frozen=True)
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


NU_GBP = NU_GBP()


@dataclass(slots=True, frozen=True)
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


NU_USD = NU_USD()


@dataclass(slots=True, frozen=True)
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


OCEAN_USD = OCEAN_USD()


@dataclass(slots=True, frozen=True)
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


OGN_BTC = OGN_BTC()


@dataclass(slots=True, frozen=True)
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


OGN_USD = OGN_USD()


@dataclass(slots=True, frozen=True)
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


OMG_BTC = OMG_BTC()


@dataclass(slots=True, frozen=True)
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


OMG_EUR = OMG_EUR()


@dataclass(slots=True, frozen=True)
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


OMG_GBP = OMG_GBP()


@dataclass(slots=True, frozen=True)
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


OMG_USD = OMG_USD()


@dataclass(slots=True, frozen=True)
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


OOKI_USD = OOKI_USD()


@dataclass(slots=True, frozen=True)
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


OP_USD = OP_USD()


@dataclass(slots=True, frozen=True)
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


OP_USDT = OP_USDT()


@dataclass(slots=True, frozen=True)
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


ORCA_USD = ORCA_USD()


@dataclass(slots=True, frozen=True)
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


ORN_BTC = ORN_BTC()


@dataclass(slots=True, frozen=True)
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


ORN_USD = ORN_USD()


@dataclass(slots=True, frozen=True)
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


ORN_USDT = ORN_USDT()


@dataclass(slots=True, frozen=True)
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


OXT_USD = OXT_USD()


@dataclass(slots=True, frozen=True)
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


PAX_USD = PAX_USD()


@dataclass(slots=True, frozen=True)
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


PAX_USDT = PAX_USDT()


@dataclass(slots=True, frozen=True)
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


PERP_EUR = PERP_EUR()


@dataclass(slots=True, frozen=True)
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


PERP_USD = PERP_USD()


@dataclass(slots=True, frozen=True)
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


PERP_USDT = PERP_USDT()


@dataclass(slots=True, frozen=True)
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


PLA_USD = PLA_USD()


@dataclass(slots=True, frozen=True)
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


PLU_USD = PLU_USD()


@dataclass(slots=True, frozen=True)
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


PNG_USD = PNG_USD()


@dataclass(slots=True, frozen=True)
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


POLS_USD = POLS_USD()


@dataclass(slots=True, frozen=True)
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


POLS_USDT = POLS_USDT()


@dataclass(slots=True, frozen=True)
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


POLY_USD = POLY_USD()


@dataclass(slots=True, frozen=True)
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


POLY_USDT = POLY_USDT()


@dataclass(slots=True, frozen=True)
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


POND_USD = POND_USD()


@dataclass(slots=True, frozen=True)
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


POND_USDT = POND_USDT()


@dataclass(slots=True, frozen=True)
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


POWR_EUR = POWR_EUR()


@dataclass(slots=True, frozen=True)
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


POWR_USD = POWR_USD()


@dataclass(slots=True, frozen=True)
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


POWR_USDT = POWR_USDT()


@dataclass(slots=True, frozen=True)
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


PRO_USD = PRO_USD()


@dataclass(slots=True, frozen=True)
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


PRQ_USD = PRQ_USD()


@dataclass(slots=True, frozen=True)
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


PRQ_USDT = PRQ_USDT()


@dataclass(slots=True, frozen=True)
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


PUNDIX_USD = PUNDIX_USD()


@dataclass(slots=True, frozen=True)
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


PYR_USD = PYR_USD()


@dataclass(slots=True, frozen=True)
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


QI_USD = QI_USD()


@dataclass(slots=True, frozen=True)
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


QNT_USD = QNT_USD()


@dataclass(slots=True, frozen=True)
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


QNT_USDT = QNT_USDT()


@dataclass(slots=True, frozen=True)
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


QSP_USD = QSP_USD()


@dataclass(slots=True, frozen=True)
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


QSP_USDT = QSP_USDT()


@dataclass(slots=True, frozen=True)
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


QUICK_USD = QUICK_USD()


@dataclass(slots=True, frozen=True)
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


RAD_BTC = RAD_BTC()


@dataclass(slots=True, frozen=True)
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


RAD_EUR = RAD_EUR()


@dataclass(slots=True, frozen=True)
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


RAD_GBP = RAD_GBP()


@dataclass(slots=True, frozen=True)
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


RAD_USD = RAD_USD()


@dataclass(slots=True, frozen=True)
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


RAD_USDT = RAD_USDT()


@dataclass(slots=True, frozen=True)
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


RAI_USD = RAI_USD()


@dataclass(slots=True, frozen=True)
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


RARE_USD = RARE_USD()


@dataclass(slots=True, frozen=True)
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


RARI_USD = RARI_USD()


@dataclass(slots=True, frozen=True)
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


RBN_USD = RBN_USD()


@dataclass(slots=True, frozen=True)
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


REN_BTC = REN_BTC()


@dataclass(slots=True, frozen=True)
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


REN_USD = REN_USD()


@dataclass(slots=True, frozen=True)
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


REP_BTC = REP_BTC()


@dataclass(slots=True, frozen=True)
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


REP_USD = REP_USD()


@dataclass(slots=True, frozen=True)
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


REQ_BTC = REQ_BTC()


@dataclass(slots=True, frozen=True)
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


REQ_EUR = REQ_EUR()


@dataclass(slots=True, frozen=True)
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


REQ_GBP = REQ_GBP()


@dataclass(slots=True, frozen=True)
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


REQ_USD = REQ_USD()


@dataclass(slots=True, frozen=True)
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


REQ_USDT = REQ_USDT()


@dataclass(slots=True, frozen=True)
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


RGT_USD = RGT_USD()


@dataclass(slots=True, frozen=True)
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


RLC_BTC = RLC_BTC()


@dataclass(slots=True, frozen=True)
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


RLC_USD = RLC_USD()


@dataclass(slots=True, frozen=True)
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


RLY_EUR = RLY_EUR()


@dataclass(slots=True, frozen=True)
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


RLY_GBP = RLY_GBP()


@dataclass(slots=True, frozen=True)
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


RLY_USD = RLY_USD()


@dataclass(slots=True, frozen=True)
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


RLY_USDT = RLY_USDT()


@dataclass(slots=True, frozen=True)
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


RNDR_EUR = RNDR_EUR()


@dataclass(slots=True, frozen=True)
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


RNDR_USD = RNDR_USD()


@dataclass(slots=True, frozen=True)
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


RNDR_USDT = RNDR_USDT()


@dataclass(slots=True, frozen=True)
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


ROSE_USD = ROSE_USD()


@dataclass(slots=True, frozen=True)
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


ROSE_USDT = ROSE_USDT()


@dataclass(slots=True, frozen=True)
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


RPL_USD = RPL_USD()


@dataclass(slots=True, frozen=True)
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


SAND_USD = SAND_USD()


@dataclass(slots=True, frozen=True)
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


SAND_USDT = SAND_USDT()


@dataclass(slots=True, frozen=True)
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


SHIB_EUR = SHIB_EUR()


@dataclass(slots=True, frozen=True)
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


SHIB_GBP = SHIB_GBP()


@dataclass(slots=True, frozen=True)
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


SHIB_USD = SHIB_USD()


@dataclass(slots=True, frozen=True)
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


SHIB_USDT = SHIB_USDT()


@dataclass(slots=True, frozen=True)
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


SHPING_EUR = SHPING_EUR()


@dataclass(slots=True, frozen=True)
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


SHPING_USD = SHPING_USD()


@dataclass(slots=True, frozen=True)
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


SHPING_USDT = SHPING_USDT()


@dataclass(slots=True, frozen=True)
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


SKL_BTC = SKL_BTC()


@dataclass(slots=True, frozen=True)
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


SKL_EUR = SKL_EUR()


@dataclass(slots=True, frozen=True)
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


SKL_GBP = SKL_GBP()


@dataclass(slots=True, frozen=True)
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


SKL_USD = SKL_USD()


@dataclass(slots=True, frozen=True)
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


SNT_USD = SNT_USD()


@dataclass(slots=True, frozen=True)
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


SNX_BTC = SNX_BTC()


@dataclass(slots=True, frozen=True)
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


SNX_EUR = SNX_EUR()


@dataclass(slots=True, frozen=True)
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


SNX_GBP = SNX_GBP()


@dataclass(slots=True, frozen=True)
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


SNX_USD = SNX_USD()


@dataclass(slots=True, frozen=True)
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


SOL_BTC = SOL_BTC()


@dataclass(slots=True, frozen=True)
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


SOL_ETH = SOL_ETH()


@dataclass(slots=True, frozen=True)
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


SOL_EUR = SOL_EUR()


@dataclass(slots=True, frozen=True)
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


SOL_GBP = SOL_GBP()


@dataclass(slots=True, frozen=True)
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


SOL_USD = SOL_USD()


@dataclass(slots=True, frozen=True)
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


SOL_USDT = SOL_USDT()


@dataclass(slots=True, frozen=True)
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


SPELL_USD = SPELL_USD()


@dataclass(slots=True, frozen=True)
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


SPELL_USDT = SPELL_USDT()


@dataclass(slots=True, frozen=True)
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


STG_USD = STG_USD()


@dataclass(slots=True, frozen=True)
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


STG_USDT = STG_USDT()


@dataclass(slots=True, frozen=True)
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


STORJ_BTC = STORJ_BTC()


@dataclass(slots=True, frozen=True)
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


STORJ_USD = STORJ_USD()


@dataclass(slots=True, frozen=True)
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


STX_USD = STX_USD()


@dataclass(slots=True, frozen=True)
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


STX_USDT = STX_USDT()


@dataclass(slots=True, frozen=True)
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


SUKU_EUR = SUKU_EUR()


@dataclass(slots=True, frozen=True)
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


SUKU_USD = SUKU_USD()


@dataclass(slots=True, frozen=True)
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


SUKU_USDT = SUKU_USDT()


@dataclass(slots=True, frozen=True)
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


SUPER_USD = SUPER_USD()


@dataclass(slots=True, frozen=True)
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


SUPER_USDT = SUPER_USDT()


@dataclass(slots=True, frozen=True)
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


SUSHI_BTC = SUSHI_BTC()


@dataclass(slots=True, frozen=True)
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


SUSHI_ETH = SUSHI_ETH()


@dataclass(slots=True, frozen=True)
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


SUSHI_EUR = SUSHI_EUR()


@dataclass(slots=True, frozen=True)
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


SUSHI_GBP = SUSHI_GBP()


@dataclass(slots=True, frozen=True)
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


SUSHI_USD = SUSHI_USD()


@dataclass(slots=True, frozen=True)
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


SWFTC_USD = SWFTC_USD()


@dataclass(slots=True, frozen=True)
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


SYLO_USD = SYLO_USD()


@dataclass(slots=True, frozen=True)
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


SYLO_USDT = SYLO_USDT()


@dataclass(slots=True, frozen=True)
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


SYN_USD = SYN_USD()


@dataclass(slots=True, frozen=True)
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


TIME_USD = TIME_USD()


@dataclass(slots=True, frozen=True)
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


TIME_USDT = TIME_USDT()


@dataclass(slots=True, frozen=True)
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


TONE_USD = TONE_USD()


@dataclass(slots=True, frozen=True)
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


TRAC_EUR = TRAC_EUR()


@dataclass(slots=True, frozen=True)
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


TRAC_USD = TRAC_USD()


@dataclass(slots=True, frozen=True)
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


TRAC_USDT = TRAC_USDT()


@dataclass(slots=True, frozen=True)
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


TRB_BTC = TRB_BTC()


@dataclass(slots=True, frozen=True)
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


TRB_USD = TRB_USD()


@dataclass(slots=True, frozen=True)
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


TRIBE_USD = TRIBE_USD()


@dataclass(slots=True, frozen=True)
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


TRU_BTC = TRU_BTC()


@dataclass(slots=True, frozen=True)
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


TRU_EUR = TRU_EUR()


@dataclass(slots=True, frozen=True)
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


TRU_USD = TRU_USD()


@dataclass(slots=True, frozen=True)
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


TRU_USDT = TRU_USDT()


@dataclass(slots=True, frozen=True)
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


UMA_BTC = UMA_BTC()


@dataclass(slots=True, frozen=True)
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


UMA_EUR = UMA_EUR()


@dataclass(slots=True, frozen=True)
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


UMA_GBP = UMA_GBP()


@dataclass(slots=True, frozen=True)
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


UMA_USD = UMA_USD()


@dataclass(slots=True, frozen=True)
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


UNFI_USD = UNFI_USD()


@dataclass(slots=True, frozen=True)
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


UNI_BTC = UNI_BTC()


@dataclass(slots=True, frozen=True)
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


UNI_EUR = UNI_EUR()


@dataclass(slots=True, frozen=True)
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


UNI_GBP = UNI_GBP()


@dataclass(slots=True, frozen=True)
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


UNI_USD = UNI_USD()


@dataclass(slots=True, frozen=True)
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


UPI_USD = UPI_USD()


@dataclass(slots=True, frozen=True)
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


UPI_USDT = UPI_USDT()


@dataclass(slots=True, frozen=True)
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


USDC_EUR = USDC_EUR()


@dataclass(slots=True, frozen=True)
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


USDC_GBP = USDC_GBP()


@dataclass(slots=True, frozen=True)
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


USDT_EUR = USDT_EUR()


@dataclass(slots=True, frozen=True)
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


USDT_GBP = USDT_GBP()


@dataclass(slots=True, frozen=True)
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


USDT_USD = USDT_USD()


@dataclass(slots=True, frozen=True)
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


USDT_USDC = USDT_USDC()


@dataclass(slots=True, frozen=True)
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


UST_EUR = UST_EUR()


@dataclass(slots=True, frozen=True)
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


UST_USD = UST_USD()


@dataclass(slots=True, frozen=True)
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


UST_USDT = UST_USDT()


@dataclass(slots=True, frozen=True)
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


VGX_EUR = VGX_EUR()


@dataclass(slots=True, frozen=True)
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


VGX_USD = VGX_USD()


@dataclass(slots=True, frozen=True)
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


VGX_USDT = VGX_USDT()


@dataclass(slots=True, frozen=True)
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


WAMPL_USD = WAMPL_USD()


@dataclass(slots=True, frozen=True)
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


WAMPL_USDT = WAMPL_USDT()


@dataclass(slots=True, frozen=True)
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


WAXL_USD = WAXL_USD()


@dataclass(slots=True, frozen=True)
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


WBTC_BTC = WBTC_BTC()


@dataclass(slots=True, frozen=True)
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


WBTC_USD = WBTC_USD()


@dataclass(slots=True, frozen=True)
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


WCFG_BTC = WCFG_BTC()


@dataclass(slots=True, frozen=True)
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


WCFG_EUR = WCFG_EUR()


@dataclass(slots=True, frozen=True)
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


WCFG_USD = WCFG_USD()


@dataclass(slots=True, frozen=True)
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


WCFG_USDT = WCFG_USDT()


@dataclass(slots=True, frozen=True)
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


WLUNA_EUR = WLUNA_EUR()


@dataclass(slots=True, frozen=True)
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


WLUNA_GBP = WLUNA_GBP()


@dataclass(slots=True, frozen=True)
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


WLUNA_USD = WLUNA_USD()


@dataclass(slots=True, frozen=True)
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


WLUNA_USDT = WLUNA_USDT()


@dataclass(slots=True, frozen=True)
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


XCN_USD = XCN_USD()


@dataclass(slots=True, frozen=True)
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


XCN_USDT = XCN_USDT()


@dataclass(slots=True, frozen=True)
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


XLM_BTC = XLM_BTC()


@dataclass(slots=True, frozen=True)
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


XLM_EUR = XLM_EUR()


@dataclass(slots=True, frozen=True)
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


XLM_USD = XLM_USD()


@dataclass(slots=True, frozen=True)
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


XLM_USDT = XLM_USDT()


@dataclass(slots=True, frozen=True)
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


XRP_BTC = XRP_BTC()


@dataclass(slots=True, frozen=True)
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


XRP_EUR = XRP_EUR()


@dataclass(slots=True, frozen=True)
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


XRP_GBP = XRP_GBP()


@dataclass(slots=True, frozen=True)
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


XRP_USD = XRP_USD()


@dataclass(slots=True, frozen=True)
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


XTZ_BTC = XTZ_BTC()


@dataclass(slots=True, frozen=True)
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


XTZ_EUR = XTZ_EUR()


@dataclass(slots=True, frozen=True)
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


XTZ_GBP = XTZ_GBP()


@dataclass(slots=True, frozen=True)
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


XTZ_USD = XTZ_USD()


@dataclass(slots=True, frozen=True)
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


XYO_BTC = XYO_BTC()


@dataclass(slots=True, frozen=True)
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


XYO_EUR = XYO_EUR()


@dataclass(slots=True, frozen=True)
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


XYO_USD = XYO_USD()


@dataclass(slots=True, frozen=True)
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


XYO_USDT = XYO_USDT()


@dataclass(slots=True, frozen=True)
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


YFI_BTC = YFI_BTC()


@dataclass(slots=True, frozen=True)
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


YFI_USD = YFI_USD()


@dataclass(slots=True, frozen=True)
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


YFII_USD = YFII_USD()


@dataclass(slots=True, frozen=True)
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


ZEC_BTC = ZEC_BTC()


@dataclass(slots=True, frozen=True)
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


ZEC_USD = ZEC_USD()


@dataclass(slots=True, frozen=True)
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


ZEC_USDC = ZEC_USDC()


@dataclass(slots=True, frozen=True)
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


ZEN_BTC = ZEN_BTC()


@dataclass(slots=True, frozen=True)
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


ZEN_USD = ZEN_USD()


@dataclass(slots=True, frozen=True)
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


ZEN_USDT = ZEN_USDT()


@dataclass(slots=True, frozen=True)
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


ZRX_BTC = ZRX_BTC()


@dataclass(slots=True, frozen=True)
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


ZRX_EUR = ZRX_EUR()


@dataclass(slots=True, frozen=True)
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


ZRX_USD = ZRX_USD()


