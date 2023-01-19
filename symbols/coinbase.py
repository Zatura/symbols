from typing import NamedTuple


class ZERO0_USD(NamedTuple):
    """
        name: 00-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "00-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "00-USD"

    def __str__(self):
        return "00-USD"

    def __call__(self):
        return "00-USD"


ZERO0_USD = ZERO0_USD()
"""
    name: 00-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ONEINCH_BTC(NamedTuple):
    """
        name: 1INCH-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "1INCH-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "1INCH-BTC"

    def __str__(self):
        return "1INCH-BTC"

    def __call__(self):
        return "1INCH-BTC"


ONEINCH_BTC = ONEINCH_BTC()
"""
    name: 1INCH-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ONEINCH_EUR(NamedTuple):
    """
        name: 1INCH-EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "1INCH-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "1INCH-EUR"

    def __str__(self):
        return "1INCH-EUR"

    def __call__(self):
        return "1INCH-EUR"


ONEINCH_EUR = ONEINCH_EUR()
"""
    name: 1INCH-EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ONEINCH_GBP(NamedTuple):
    """
        name: 1INCH-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "1INCH-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "1INCH-GBP"

    def __str__(self):
        return "1INCH-GBP"

    def __call__(self):
        return "1INCH-GBP"


ONEINCH_GBP = ONEINCH_GBP()
"""
    name: 1INCH-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class ONEINCH_USD(NamedTuple):
    """
        name: 1INCH-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "1INCH-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "1INCH-USD"

    def __str__(self):
        return "1INCH-USD"

    def __call__(self):
        return "1INCH-USD"


ONEINCH_USD = ONEINCH_USD()
"""
    name: 1INCH-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AAVE_BTC(NamedTuple):
    """
        name: AAVE-BTC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "AAVE-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVE-BTC"

    def __str__(self):
        return "AAVE-BTC"

    def __call__(self):
        return "AAVE-BTC"


AAVE_BTC = AAVE_BTC()
"""
    name: AAVE-BTC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class AAVE_EUR(NamedTuple):
    """
        name: AAVE-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "AAVE-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVE-EUR"

    def __str__(self):
        return "AAVE-EUR"

    def __call__(self):
        return "AAVE-EUR"


AAVE_EUR = AAVE_EUR()
"""
    name: AAVE-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class AAVE_GBP(NamedTuple):
    """
        name: AAVE-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "AAVE-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVE-GBP"

    def __str__(self):
        return "AAVE-GBP"

    def __call__(self):
        return "AAVE-GBP"


AAVE_GBP = AAVE_GBP()
"""
    name: AAVE-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class AAVE_USD(NamedTuple):
    """
        name: AAVE-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AAVE-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVE-USD"

    def __str__(self):
        return "AAVE-USD"

    def __call__(self):
        return "AAVE-USD"


AAVE_USD = AAVE_USD()
"""
    name: AAVE-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ABT_USD(NamedTuple):
    """
        name: ABT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ABT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ABT-USD"

    def __str__(self):
        return "ABT-USD"

    def __call__(self):
        return "ABT-USD"


ABT_USD = ABT_USD()
"""
    name: ABT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ACH_USD(NamedTuple):
    """
        name: ACH-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ACH-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ACH-USD"

    def __str__(self):
        return "ACH-USD"

    def __call__(self):
        return "ACH-USD"


ACH_USD = ACH_USD()
"""
    name: ACH-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ACH_USDT(NamedTuple):
    """
        name: ACH-USDT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ACH-USDT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ACH-USDT"

    def __str__(self):
        return "ACH-USDT"

    def __call__(self):
        return "ACH-USDT"


ACH_USDT = ACH_USDT()
"""
    name: ACH-USDT
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ADA_BTC(NamedTuple):
    """
        name: ADA-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ADA-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADA-BTC"

    def __str__(self):
        return "ADA-BTC"

    def __call__(self):
        return "ADA-BTC"


ADA_BTC = ADA_BTC()
"""
    name: ADA-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ADA_ETH(NamedTuple):
    """
        name: ADA-ETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00022
        maximum_order_size: None
        margin: False
    """
    name: str = "ADA-ETH"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADA-ETH"

    def __str__(self):
        return "ADA-ETH"

    def __call__(self):
        return "ADA-ETH"


ADA_ETH = ADA_ETH()
"""
    name: ADA-ETH
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00022
    maximum_order_size: None
    margin: False
"""


class ADA_EUR(NamedTuple):
    """
        name: ADA-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ADA-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADA-EUR"

    def __str__(self):
        return "ADA-EUR"

    def __call__(self):
        return "ADA-EUR"


ADA_EUR = ADA_EUR()
"""
    name: ADA-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ADA_GBP(NamedTuple):
    """
        name: ADA-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "ADA-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADA-GBP"

    def __str__(self):
        return "ADA-GBP"

    def __call__(self):
        return "ADA-GBP"


ADA_GBP = ADA_GBP()
"""
    name: ADA-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class ADA_USD(NamedTuple):
    """
        name: ADA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ADA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADA-USD"

    def __str__(self):
        return "ADA-USD"

    def __call__(self):
        return "ADA-USD"


ADA_USD = ADA_USD()
"""
    name: ADA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ADA_USDC(NamedTuple):
    """
        name: ADA-USDC
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ADA-USDC"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADA-USDC"

    def __str__(self):
        return "ADA-USDC"

    def __call__(self):
        return "ADA-USDC"


ADA_USDC = ADA_USDC()
"""
    name: ADA-USDC
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ADA_USDT(NamedTuple):
    """
        name: ADA-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ADA-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADA-USDT"

    def __str__(self):
        return "ADA-USDT"

    def __call__(self):
        return "ADA-USDT"


ADA_USDT = ADA_USDT()
"""
    name: ADA-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AERGO_USD(NamedTuple):
    """
        name: AERGO-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AERGO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AERGO-USD"

    def __str__(self):
        return "AERGO-USD"

    def __call__(self):
        return "AERGO-USD"


AERGO_USD = AERGO_USD()
"""
    name: AERGO-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AGLD_USD(NamedTuple):
    """
        name: AGLD-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AGLD-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AGLD-USD"

    def __str__(self):
        return "AGLD-USD"

    def __call__(self):
        return "AGLD-USD"


AGLD_USD = AGLD_USD()
"""
    name: AGLD-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AGLD_USDT(NamedTuple):
    """
        name: AGLD-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AGLD-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AGLD-USDT"

    def __str__(self):
        return "AGLD-USDT"

    def __call__(self):
        return "AGLD-USDT"


AGLD_USDT = AGLD_USDT()
"""
    name: AGLD-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AIOZ_USD(NamedTuple):
    """
        name: AIOZ-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AIOZ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AIOZ-USD"

    def __str__(self):
        return "AIOZ-USD"

    def __call__(self):
        return "AIOZ-USD"


AIOZ_USD = AIOZ_USD()
"""
    name: AIOZ-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AIOZ_USDT(NamedTuple):
    """
        name: AIOZ-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AIOZ-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AIOZ-USDT"

    def __str__(self):
        return "AIOZ-USDT"

    def __call__(self):
        return "AIOZ-USDT"


AIOZ_USDT = AIOZ_USDT()
"""
    name: AIOZ-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ALCX_EUR(NamedTuple):
    """
        name: ALCX-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ALCX-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALCX-EUR"

    def __str__(self):
        return "ALCX-EUR"

    def __call__(self):
        return "ALCX-EUR"


ALCX_EUR = ALCX_EUR()
"""
    name: ALCX-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ALCX_USD(NamedTuple):
    """
        name: ALCX-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ALCX-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALCX-USD"

    def __str__(self):
        return "ALCX-USD"

    def __call__(self):
        return "ALCX-USD"


ALCX_USD = ALCX_USD()
"""
    name: ALCX-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ALCX_USDT(NamedTuple):
    """
        name: ALCX-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ALCX-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALCX-USDT"

    def __str__(self):
        return "ALCX-USDT"

    def __call__(self):
        return "ALCX-USDT"


ALCX_USDT = ALCX_USDT()
"""
    name: ALCX-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ALEPH_USD(NamedTuple):
    """
        name: ALEPH-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ALEPH-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALEPH-USD"

    def __str__(self):
        return "ALEPH-USD"

    def __call__(self):
        return "ALEPH-USD"


ALEPH_USD = ALEPH_USD()
"""
    name: ALEPH-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ALGO_BTC(NamedTuple):
    """
        name: ALGO-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ALGO-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGO-BTC"

    def __str__(self):
        return "ALGO-BTC"

    def __call__(self):
        return "ALGO-BTC"


ALGO_BTC = ALGO_BTC()
"""
    name: ALGO-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ALGO_EUR(NamedTuple):
    """
        name: ALGO-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ALGO-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGO-EUR"

    def __str__(self):
        return "ALGO-EUR"

    def __call__(self):
        return "ALGO-EUR"


ALGO_EUR = ALGO_EUR()
"""
    name: ALGO-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ALGO_GBP(NamedTuple):
    """
        name: ALGO-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "ALGO-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGO-GBP"

    def __str__(self):
        return "ALGO-GBP"

    def __call__(self):
        return "ALGO-GBP"


ALGO_GBP = ALGO_GBP()
"""
    name: ALGO-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class ALGO_USD(NamedTuple):
    """
        name: ALGO-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ALGO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGO-USD"

    def __str__(self):
        return "ALGO-USD"

    def __call__(self):
        return "ALGO-USD"


ALGO_USD = ALGO_USD()
"""
    name: ALGO-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ALICE_USD(NamedTuple):
    """
        name: ALICE-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ALICE-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALICE-USD"

    def __str__(self):
        return "ALICE-USD"

    def __call__(self):
        return "ALICE-USD"


ALICE_USD = ALICE_USD()
"""
    name: ALICE-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AMP_USD(NamedTuple):
    """
        name: AMP-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AMP-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AMP-USD"

    def __str__(self):
        return "AMP-USD"

    def __call__(self):
        return "AMP-USD"


AMP_USD = AMP_USD()
"""
    name: AMP-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ANKR_BTC(NamedTuple):
    """
        name: ANKR-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ANKR-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANKR-BTC"

    def __str__(self):
        return "ANKR-BTC"

    def __call__(self):
        return "ANKR-BTC"


ANKR_BTC = ANKR_BTC()
"""
    name: ANKR-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ANKR_EUR(NamedTuple):
    """
        name: ANKR-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ANKR-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANKR-EUR"

    def __str__(self):
        return "ANKR-EUR"

    def __call__(self):
        return "ANKR-EUR"


ANKR_EUR = ANKR_EUR()
"""
    name: ANKR-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ANKR_GBP(NamedTuple):
    """
        name: ANKR-GBP
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "ANKR-GBP"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANKR-GBP"

    def __str__(self):
        return "ANKR-GBP"

    def __call__(self):
        return "ANKR-GBP"


ANKR_GBP = ANKR_GBP()
"""
    name: ANKR-GBP
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class ANKR_USD(NamedTuple):
    """
        name: ANKR-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ANKR-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANKR-USD"

    def __str__(self):
        return "ANKR-USD"

    def __call__(self):
        return "ANKR-USD"


ANKR_USD = ANKR_USD()
"""
    name: ANKR-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ANT_USD(NamedTuple):
    """
        name: ANT-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5.0
        maximum_order_size: None
        margin: False
    """
    name: str = "ANT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5.0
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANT-USD"

    def __str__(self):
        return "ANT-USD"

    def __call__(self):
        return "ANT-USD"


ANT_USD = ANT_USD()
"""
    name: ANT-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5.0
    maximum_order_size: None
    margin: False
"""


class APE_EUR(NamedTuple):
    """
        name: APE-EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "APE-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APE-EUR"

    def __str__(self):
        return "APE-EUR"

    def __call__(self):
        return "APE-EUR"


APE_EUR = APE_EUR()
"""
    name: APE-EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class APE_USD(NamedTuple):
    """
        name: APE-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "APE-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APE-USD"

    def __str__(self):
        return "APE-USD"

    def __call__(self):
        return "APE-USD"


APE_USD = APE_USD()
"""
    name: APE-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class APE_USDT(NamedTuple):
    """
        name: APE-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "APE-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APE-USDT"

    def __str__(self):
        return "APE-USDT"

    def __call__(self):
        return "APE-USDT"


APE_USDT = APE_USDT()
"""
    name: APE-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class API3_USD(NamedTuple):
    """
        name: API3-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "API3-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "API3-USD"

    def __str__(self):
        return "API3-USD"

    def __call__(self):
        return "API3-USD"


API3_USD = API3_USD()
"""
    name: API3-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


class API3_USDT(NamedTuple):
    """
        name: API3-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "API3-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "API3-USDT"

    def __str__(self):
        return "API3-USDT"

    def __call__(self):
        return "API3-USDT"


API3_USDT = API3_USDT()
"""
    name: API3-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


class APT_USD(NamedTuple):
    """
        name: APT-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "APT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APT-USD"

    def __str__(self):
        return "APT-USD"

    def __call__(self):
        return "APT-USD"


APT_USD = APT_USD()
"""
    name: APT-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class APT_USDT(NamedTuple):
    """
        name: APT-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "APT-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APT-USDT"

    def __str__(self):
        return "APT-USDT"

    def __call__(self):
        return "APT-USDT"


APT_USDT = APT_USDT()
"""
    name: APT-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ARPA_EUR(NamedTuple):
    """
        name: ARPA-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ARPA-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARPA-EUR"

    def __str__(self):
        return "ARPA-EUR"

    def __call__(self):
        return "ARPA-EUR"


ARPA_EUR = ARPA_EUR()
"""
    name: ARPA-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ARPA_USD(NamedTuple):
    """
        name: ARPA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ARPA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARPA-USD"

    def __str__(self):
        return "ARPA-USD"

    def __call__(self):
        return "ARPA-USD"


ARPA_USD = ARPA_USD()
"""
    name: ARPA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ARPA_USDT(NamedTuple):
    """
        name: ARPA-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ARPA-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARPA-USDT"

    def __str__(self):
        return "ARPA-USDT"

    def __call__(self):
        return "ARPA-USDT"


ARPA_USDT = ARPA_USDT()
"""
    name: ARPA-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ASM_USD(NamedTuple):
    """
        name: ASM-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ASM-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ASM-USD"

    def __str__(self):
        return "ASM-USD"

    def __call__(self):
        return "ASM-USD"


ASM_USD = ASM_USD()
"""
    name: ASM-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ASM_USDT(NamedTuple):
    """
        name: ASM-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ASM-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ASM-USDT"

    def __str__(self):
        return "ASM-USDT"

    def __call__(self):
        return "ASM-USDT"


ASM_USDT = ASM_USDT()
"""
    name: ASM-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AST_USD(NamedTuple):
    """
        name: AST-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AST-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AST-USD"

    def __str__(self):
        return "AST-USD"

    def __call__(self):
        return "AST-USD"


AST_USD = AST_USD()
"""
    name: AST-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ATA_USD(NamedTuple):
    """
        name: ATA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ATA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATA-USD"

    def __str__(self):
        return "ATA-USD"

    def __call__(self):
        return "ATA-USD"


ATA_USD = ATA_USD()
"""
    name: ATA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ATA_USDT(NamedTuple):
    """
        name: ATA-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ATA-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATA-USDT"

    def __str__(self):
        return "ATA-USDT"

    def __call__(self):
        return "ATA-USDT"


ATA_USDT = ATA_USDT()
"""
    name: ATA-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ATOM_BTC(NamedTuple):
    """
        name: ATOM-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOM-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOM-BTC"

    def __str__(self):
        return "ATOM-BTC"

    def __call__(self):
        return "ATOM-BTC"


ATOM_BTC = ATOM_BTC()
"""
    name: ATOM-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ATOM_EUR(NamedTuple):
    """
        name: ATOM-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOM-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOM-EUR"

    def __str__(self):
        return "ATOM-EUR"

    def __call__(self):
        return "ATOM-EUR"


ATOM_EUR = ATOM_EUR()
"""
    name: ATOM-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ATOM_GBP(NamedTuple):
    """
        name: ATOM-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOM-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOM-GBP"

    def __str__(self):
        return "ATOM-GBP"

    def __call__(self):
        return "ATOM-GBP"


ATOM_GBP = ATOM_GBP()
"""
    name: ATOM-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class ATOM_USD(NamedTuple):
    """
        name: ATOM-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOM-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOM-USD"

    def __str__(self):
        return "ATOM-USD"

    def __call__(self):
        return "ATOM-USD"


ATOM_USD = ATOM_USD()
"""
    name: ATOM-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ATOM_USDT(NamedTuple):
    """
        name: ATOM-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOM-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOM-USDT"

    def __str__(self):
        return "ATOM-USDT"

    def __call__(self):
        return "ATOM-USDT"


ATOM_USDT = ATOM_USDT()
"""
    name: ATOM-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AUCTION_EUR(NamedTuple):
    """
        name: AUCTION-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "AUCTION-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AUCTION-EUR"

    def __str__(self):
        return "AUCTION-EUR"

    def __call__(self):
        return "AUCTION-EUR"


AUCTION_EUR = AUCTION_EUR()
"""
    name: AUCTION-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class AUCTION_USD(NamedTuple):
    """
        name: AUCTION-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AUCTION-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AUCTION-USD"

    def __str__(self):
        return "AUCTION-USD"

    def __call__(self):
        return "AUCTION-USD"


AUCTION_USD = AUCTION_USD()
"""
    name: AUCTION-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AUCTION_USDT(NamedTuple):
    """
        name: AUCTION-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AUCTION-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AUCTION-USDT"

    def __str__(self):
        return "AUCTION-USDT"

    def __call__(self):
        return "AUCTION-USDT"


AUCTION_USDT = AUCTION_USDT()
"""
    name: AUCTION-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AURORA_USD(NamedTuple):
    """
        name: AURORA-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AURORA-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AURORA-USD"

    def __str__(self):
        return "AURORA-USD"

    def __call__(self):
        return "AURORA-USD"


AURORA_USD = AURORA_USD()
"""
    name: AURORA-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AVAX_BTC(NamedTuple):
    """
        name: AVAX-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "AVAX-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AVAX-BTC"

    def __str__(self):
        return "AVAX-BTC"

    def __call__(self):
        return "AVAX-BTC"


AVAX_BTC = AVAX_BTC()
"""
    name: AVAX-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class AVAX_EUR(NamedTuple):
    """
        name: AVAX-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "AVAX-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AVAX-EUR"

    def __str__(self):
        return "AVAX-EUR"

    def __call__(self):
        return "AVAX-EUR"


AVAX_EUR = AVAX_EUR()
"""
    name: AVAX-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class AVAX_USD(NamedTuple):
    """
        name: AVAX-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AVAX-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AVAX-USD"

    def __str__(self):
        return "AVAX-USD"

    def __call__(self):
        return "AVAX-USD"


AVAX_USD = AVAX_USD()
"""
    name: AVAX-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AVAX_USDT(NamedTuple):
    """
        name: AVAX-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AVAX-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AVAX-USDT"

    def __str__(self):
        return "AVAX-USDT"

    def __call__(self):
        return "AVAX-USDT"


AVAX_USDT = AVAX_USDT()
"""
    name: AVAX-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AVT_USD(NamedTuple):
    """
        name: AVT-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AVT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AVT-USD"

    def __str__(self):
        return "AVT-USD"

    def __call__(self):
        return "AVT-USD"


AVT_USD = AVT_USD()
"""
    name: AVT-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AXS_BTC(NamedTuple):
    """
        name: AXS-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "AXS-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AXS-BTC"

    def __str__(self):
        return "AXS-BTC"

    def __call__(self):
        return "AXS-BTC"


AXS_BTC = AXS_BTC()
"""
    name: AXS-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class AXS_EUR(NamedTuple):
    """
        name: AXS-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "AXS-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AXS-EUR"

    def __str__(self):
        return "AXS-EUR"

    def __call__(self):
        return "AXS-EUR"


AXS_EUR = AXS_EUR()
"""
    name: AXS-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class AXS_USD(NamedTuple):
    """
        name: AXS-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AXS-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AXS-USD"

    def __str__(self):
        return "AXS-USD"

    def __call__(self):
        return "AXS-USD"


AXS_USD = AXS_USD()
"""
    name: AXS-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class AXS_USDT(NamedTuple):
    """
        name: AXS-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "AXS-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AXS-USDT"

    def __str__(self):
        return "AXS-USDT"

    def __call__(self):
        return "AXS-USDT"


AXS_USDT = AXS_USDT()
"""
    name: AXS-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BADGER_EUR(NamedTuple):
    """
        name: BADGER-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "BADGER-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BADGER-EUR"

    def __str__(self):
        return "BADGER-EUR"

    def __call__(self):
        return "BADGER-EUR"


BADGER_EUR = BADGER_EUR()
"""
    name: BADGER-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class BADGER_USD(NamedTuple):
    """
        name: BADGER-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BADGER-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BADGER-USD"

    def __str__(self):
        return "BADGER-USD"

    def __call__(self):
        return "BADGER-USD"


BADGER_USD = BADGER_USD()
"""
    name: BADGER-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BADGER_USDT(NamedTuple):
    """
        name: BADGER-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BADGER-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BADGER-USDT"

    def __str__(self):
        return "BADGER-USDT"

    def __call__(self):
        return "BADGER-USDT"


BADGER_USDT = BADGER_USDT()
"""
    name: BADGER-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BAL_BTC(NamedTuple):
    """
        name: BAL-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "BAL-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAL-BTC"

    def __str__(self):
        return "BAL-BTC"

    def __call__(self):
        return "BAL-BTC"


BAL_BTC = BAL_BTC()
"""
    name: BAL-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class BAL_USD(NamedTuple):
    """
        name: BAL-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BAL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAL-USD"

    def __str__(self):
        return "BAL-USD"

    def __call__(self):
        return "BAL-USD"


BAL_USD = BAL_USD()
"""
    name: BAL-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BAND_BTC(NamedTuple):
    """
        name: BAND-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "BAND-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAND-BTC"

    def __str__(self):
        return "BAND-BTC"

    def __call__(self):
        return "BAND-BTC"


BAND_BTC = BAND_BTC()
"""
    name: BAND-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class BAND_EUR(NamedTuple):
    """
        name: BAND-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "BAND-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAND-EUR"

    def __str__(self):
        return "BAND-EUR"

    def __call__(self):
        return "BAND-EUR"


BAND_EUR = BAND_EUR()
"""
    name: BAND-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class BAND_GBP(NamedTuple):
    """
        name: BAND-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "BAND-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAND-GBP"

    def __str__(self):
        return "BAND-GBP"

    def __call__(self):
        return "BAND-GBP"


BAND_GBP = BAND_GBP()
"""
    name: BAND-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class BAND_USD(NamedTuple):
    """
        name: BAND-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BAND-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAND-USD"

    def __str__(self):
        return "BAND-USD"

    def __call__(self):
        return "BAND-USD"


BAND_USD = BAND_USD()
"""
    name: BAND-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BAT_BTC(NamedTuple):
    """
        name: BAT-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "BAT-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAT-BTC"

    def __str__(self):
        return "BAT-BTC"

    def __call__(self):
        return "BAT-BTC"


BAT_BTC = BAT_BTC()
"""
    name: BAT-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class BAT_ETH(NamedTuple):
    """
        name: BAT-ETH
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00022
        maximum_order_size: None
        margin: False
    """
    name: str = "BAT-ETH"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAT-ETH"

    def __str__(self):
        return "BAT-ETH"

    def __call__(self):
        return "BAT-ETH"


BAT_ETH = BAT_ETH()
"""
    name: BAT-ETH
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00022
    maximum_order_size: None
    margin: False
"""


class BAT_EUR(NamedTuple):
    """
        name: BAT-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "BAT-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAT-EUR"

    def __str__(self):
        return "BAT-EUR"

    def __call__(self):
        return "BAT-EUR"


BAT_EUR = BAT_EUR()
"""
    name: BAT-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class BAT_USD(NamedTuple):
    """
        name: BAT-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BAT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAT-USD"

    def __str__(self):
        return "BAT-USD"

    def __call__(self):
        return "BAT-USD"


BAT_USD = BAT_USD()
"""
    name: BAT-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BAT_USDC(NamedTuple):
    """
        name: BAT-USDC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BAT-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAT-USDC"

    def __str__(self):
        return "BAT-USDC"

    def __call__(self):
        return "BAT-USDC"


BAT_USDC = BAT_USDC()
"""
    name: BAT-USDC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BCH_BTC(NamedTuple):
    """
        name: BCH-BTC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00001
        maximum_order_size: None
        margin: False
    """
    name: str = "BCH-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCH-BTC"

    def __str__(self):
        return "BCH-BTC"

    def __call__(self):
        return "BCH-BTC"


BCH_BTC = BCH_BTC()
"""
    name: BCH-BTC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00001
    maximum_order_size: None
    margin: False
"""


class BCH_EUR(NamedTuple):
    """
        name: BCH-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "BCH-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCH-EUR"

    def __str__(self):
        return "BCH-EUR"

    def __call__(self):
        return "BCH-EUR"


BCH_EUR = BCH_EUR()
"""
    name: BCH-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class BCH_GBP(NamedTuple):
    """
        name: BCH-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "BCH-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCH-GBP"

    def __str__(self):
        return "BCH-GBP"

    def __call__(self):
        return "BCH-GBP"


BCH_GBP = BCH_GBP()
"""
    name: BCH-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class BCH_USD(NamedTuple):
    """
        name: BCH-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BCH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCH-USD"

    def __str__(self):
        return "BCH-USD"

    def __call__(self):
        return "BCH-USD"


BCH_USD = BCH_USD()
"""
    name: BCH-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BICO_EUR(NamedTuple):
    """
        name: BICO-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BICO-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BICO-EUR"

    def __str__(self):
        return "BICO-EUR"

    def __call__(self):
        return "BICO-EUR"


BICO_EUR = BICO_EUR()
"""
    name: BICO-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BICO_USD(NamedTuple):
    """
        name: BICO-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BICO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BICO-USD"

    def __str__(self):
        return "BICO-USD"

    def __call__(self):
        return "BICO-USD"


BICO_USD = BICO_USD()
"""
    name: BICO-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BICO_USDT(NamedTuple):
    """
        name: BICO-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BICO-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BICO-USDT"

    def __str__(self):
        return "BICO-USDT"

    def __call__(self):
        return "BICO-USDT"


BICO_USDT = BICO_USDT()
"""
    name: BICO-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BIT_USD(NamedTuple):
    """
        name: BIT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BIT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BIT-USD"

    def __str__(self):
        return "BIT-USD"

    def __call__(self):
        return "BIT-USD"


BIT_USD = BIT_USD()
"""
    name: BIT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BIT_USDT(NamedTuple):
    """
        name: BIT-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BIT-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BIT-USDT"

    def __str__(self):
        return "BIT-USDT"

    def __call__(self):
        return "BIT-USDT"


BIT_USDT = BIT_USDT()
"""
    name: BIT-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BLZ_USD(NamedTuple):
    """
        name: BLZ-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BLZ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BLZ-USD"

    def __str__(self):
        return "BLZ-USD"

    def __call__(self):
        return "BLZ-USD"


BLZ_USD = BLZ_USD()
"""
    name: BLZ-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BNT_BTC(NamedTuple):
    """
        name: BNT-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "BNT-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNT-BTC"

    def __str__(self):
        return "BNT-BTC"

    def __call__(self):
        return "BNT-BTC"


BNT_BTC = BNT_BTC()
"""
    name: BNT-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class BNT_EUR(NamedTuple):
    """
        name: BNT-EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "BNT-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNT-EUR"

    def __str__(self):
        return "BNT-EUR"

    def __call__(self):
        return "BNT-EUR"


BNT_EUR = BNT_EUR()
"""
    name: BNT-EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class BNT_GBP(NamedTuple):
    """
        name: BNT-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "BNT-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNT-GBP"

    def __str__(self):
        return "BNT-GBP"

    def __call__(self):
        return "BNT-GBP"


BNT_GBP = BNT_GBP()
"""
    name: BNT-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class BNT_USD(NamedTuple):
    """
        name: BNT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BNT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNT-USD"

    def __str__(self):
        return "BNT-USD"

    def __call__(self):
        return "BNT-USD"


BNT_USD = BNT_USD()
"""
    name: BNT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BOBA_USD(NamedTuple):
    """
        name: BOBA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BOBA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BOBA-USD"

    def __str__(self):
        return "BOBA-USD"

    def __call__(self):
        return "BOBA-USD"


BOBA_USD = BOBA_USD()
"""
    name: BOBA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BOBA_USDT(NamedTuple):
    """
        name: BOBA-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BOBA-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BOBA-USDT"

    def __str__(self):
        return "BOBA-USDT"

    def __call__(self):
        return "BOBA-USDT"


BOBA_USDT = BOBA_USDT()
"""
    name: BOBA-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BOND_USD(NamedTuple):
    """
        name: BOND-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BOND-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BOND-USD"

    def __str__(self):
        return "BOND-USD"

    def __call__(self):
        return "BOND-USD"


BOND_USD = BOND_USD()
"""
    name: BOND-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BOND_USDT(NamedTuple):
    """
        name: BOND-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BOND-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BOND-USDT"

    def __str__(self):
        return "BOND-USDT"

    def __call__(self):
        return "BOND-USDT"


BOND_USDT = BOND_USDT()
"""
    name: BOND-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BTC_EUR(NamedTuple):
    """
        name: BTC-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "BTC-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTC-EUR"

    def __str__(self):
        return "BTC-EUR"

    def __call__(self):
        return "BTC-EUR"


BTC_EUR = BTC_EUR()
"""
    name: BTC-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class BTC_GBP(NamedTuple):
    """
        name: BTC-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "BTC-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTC-GBP"

    def __str__(self):
        return "BTC-GBP"

    def __call__(self):
        return "BTC-GBP"


BTC_GBP = BTC_GBP()
"""
    name: BTC-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class BTC_USD(NamedTuple):
    """
        name: BTC-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BTC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTC-USD"

    def __str__(self):
        return "BTC-USD"

    def __call__(self):
        return "BTC-USD"


BTC_USD = BTC_USD()
"""
    name: BTC-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BTC_USDC(NamedTuple):
    """
        name: BTC-USDC
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BTC-USDC"
    precision: int = 1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTC-USDC"

    def __str__(self):
        return "BTC-USDC"

    def __call__(self):
        return "BTC-USDC"


BTC_USDC = BTC_USDC()
"""
    name: BTC-USDC
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BTC_USDT(NamedTuple):
    """
        name: BTC-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BTC-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTC-USDT"

    def __str__(self):
        return "BTC-USDT"

    def __call__(self):
        return "BTC-USDT"


BTC_USDT = BTC_USDT()
"""
    name: BTC-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BTRST_BTC(NamedTuple):
    """
        name: BTRST-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "BTRST-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTRST-BTC"

    def __str__(self):
        return "BTRST-BTC"

    def __call__(self):
        return "BTRST-BTC"


BTRST_BTC = BTRST_BTC()
"""
    name: BTRST-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class BTRST_EUR(NamedTuple):
    """
        name: BTRST-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "BTRST-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTRST-EUR"

    def __str__(self):
        return "BTRST-EUR"

    def __call__(self):
        return "BTRST-EUR"


BTRST_EUR = BTRST_EUR()
"""
    name: BTRST-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class BTRST_GBP(NamedTuple):
    """
        name: BTRST-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "BTRST-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTRST-GBP"

    def __str__(self):
        return "BTRST-GBP"

    def __call__(self):
        return "BTRST-GBP"


BTRST_GBP = BTRST_GBP()
"""
    name: BTRST-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class BTRST_USD(NamedTuple):
    """
        name: BTRST-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BTRST-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTRST-USD"

    def __str__(self):
        return "BTRST-USD"

    def __call__(self):
        return "BTRST-USD"


BTRST_USD = BTRST_USD()
"""
    name: BTRST-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BTRST_USDT(NamedTuple):
    """
        name: BTRST-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BTRST-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTRST-USDT"

    def __str__(self):
        return "BTRST-USDT"

    def __call__(self):
        return "BTRST-USDT"


BTRST_USDT = BTRST_USDT()
"""
    name: BTRST-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class BUSD_USD(NamedTuple):
    """
        name: BUSD-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BUSD-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BUSD-USD"

    def __str__(self):
        return "BUSD-USD"

    def __call__(self):
        return "BUSD-USD"


BUSD_USD = BUSD_USD()
"""
    name: BUSD-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class C98_USD(NamedTuple):
    """
        name: C98-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "C98-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "C98-USD"

    def __str__(self):
        return "C98-USD"

    def __call__(self):
        return "C98-USD"


C98_USD = C98_USD()
"""
    name: C98-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class C98_USDT(NamedTuple):
    """
        name: C98-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "C98-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "C98-USDT"

    def __str__(self):
        return "C98-USDT"

    def __call__(self):
        return "C98-USDT"


C98_USDT = C98_USDT()
"""
    name: C98-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CBETH_ETH(NamedTuple):
    """
        name: CBETH-ETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.002
        maximum_order_size: None
        margin: False
    """
    name: str = "CBETH-ETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.002
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CBETH-ETH"

    def __str__(self):
        return "CBETH-ETH"

    def __call__(self):
        return "CBETH-ETH"


CBETH_ETH = CBETH_ETH()
"""
    name: CBETH-ETH
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.002
    maximum_order_size: None
    margin: False
"""


class CBETH_USD(NamedTuple):
    """
        name: CBETH-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CBETH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CBETH-USD"

    def __str__(self):
        return "CBETH-USD"

    def __call__(self):
        return "CBETH-USD"


CBETH_USD = CBETH_USD()
"""
    name: CBETH-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CELR_USD(NamedTuple):
    """
        name: CELR-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CELR-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CELR-USD"

    def __str__(self):
        return "CELR-USD"

    def __call__(self):
        return "CELR-USD"


CELR_USD = CELR_USD()
"""
    name: CELR-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CGLD_BTC(NamedTuple):
    """
        name: CGLD-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "CGLD-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CGLD-BTC"

    def __str__(self):
        return "CGLD-BTC"

    def __call__(self):
        return "CGLD-BTC"


CGLD_BTC = CGLD_BTC()
"""
    name: CGLD-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class CGLD_EUR(NamedTuple):
    """
        name: CGLD-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "CGLD-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CGLD-EUR"

    def __str__(self):
        return "CGLD-EUR"

    def __call__(self):
        return "CGLD-EUR"


CGLD_EUR = CGLD_EUR()
"""
    name: CGLD-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class CGLD_GBP(NamedTuple):
    """
        name: CGLD-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "CGLD-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CGLD-GBP"

    def __str__(self):
        return "CGLD-GBP"

    def __call__(self):
        return "CGLD-GBP"


CGLD_GBP = CGLD_GBP()
"""
    name: CGLD-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class CGLD_USD(NamedTuple):
    """
        name: CGLD-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CGLD-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CGLD-USD"

    def __str__(self):
        return "CGLD-USD"

    def __call__(self):
        return "CGLD-USD"


CGLD_USD = CGLD_USD()
"""
    name: CGLD-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CHZ_EUR(NamedTuple):
    """
        name: CHZ-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "CHZ-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CHZ-EUR"

    def __str__(self):
        return "CHZ-EUR"

    def __call__(self):
        return "CHZ-EUR"


CHZ_EUR = CHZ_EUR()
"""
    name: CHZ-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class CHZ_GBP(NamedTuple):
    """
        name: CHZ-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "CHZ-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CHZ-GBP"

    def __str__(self):
        return "CHZ-GBP"

    def __call__(self):
        return "CHZ-GBP"


CHZ_GBP = CHZ_GBP()
"""
    name: CHZ-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class CHZ_USD(NamedTuple):
    """
        name: CHZ-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CHZ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CHZ-USD"

    def __str__(self):
        return "CHZ-USD"

    def __call__(self):
        return "CHZ-USD"


CHZ_USD = CHZ_USD()
"""
    name: CHZ-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CHZ_USDT(NamedTuple):
    """
        name: CHZ-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CHZ-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CHZ-USDT"

    def __str__(self):
        return "CHZ-USDT"

    def __call__(self):
        return "CHZ-USDT"


CHZ_USDT = CHZ_USDT()
"""
    name: CHZ-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CLV_EUR(NamedTuple):
    """
        name: CLV-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "CLV-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CLV-EUR"

    def __str__(self):
        return "CLV-EUR"

    def __call__(self):
        return "CLV-EUR"


CLV_EUR = CLV_EUR()
"""
    name: CLV-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class CLV_GBP(NamedTuple):
    """
        name: CLV-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "CLV-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CLV-GBP"

    def __str__(self):
        return "CLV-GBP"

    def __call__(self):
        return "CLV-GBP"


CLV_GBP = CLV_GBP()
"""
    name: CLV-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class CLV_USD(NamedTuple):
    """
        name: CLV-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CLV-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CLV-USD"

    def __str__(self):
        return "CLV-USD"

    def __call__(self):
        return "CLV-USD"


CLV_USD = CLV_USD()
"""
    name: CLV-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CLV_USDT(NamedTuple):
    """
        name: CLV-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CLV-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CLV-USDT"

    def __str__(self):
        return "CLV-USDT"

    def __call__(self):
        return "CLV-USDT"


CLV_USDT = CLV_USDT()
"""
    name: CLV-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class COMP_BTC(NamedTuple):
    """
        name: COMP-BTC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "COMP-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COMP-BTC"

    def __str__(self):
        return "COMP-BTC"

    def __call__(self):
        return "COMP-BTC"


COMP_BTC = COMP_BTC()
"""
    name: COMP-BTC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class COMP_USD(NamedTuple):
    """
        name: COMP-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "COMP-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COMP-USD"

    def __str__(self):
        return "COMP-USD"

    def __call__(self):
        return "COMP-USD"


COMP_USD = COMP_USD()
"""
    name: COMP-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class COTI_USD(NamedTuple):
    """
        name: COTI-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "COTI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COTI-USD"

    def __str__(self):
        return "COTI-USD"

    def __call__(self):
        return "COTI-USD"


COTI_USD = COTI_USD()
"""
    name: COTI-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class COVAL_USD(NamedTuple):
    """
        name: COVAL-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "COVAL-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COVAL-USD"

    def __str__(self):
        return "COVAL-USD"

    def __call__(self):
        return "COVAL-USD"


COVAL_USD = COVAL_USD()
"""
    name: COVAL-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class COVAL_USDT(NamedTuple):
    """
        name: COVAL-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "COVAL-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COVAL-USDT"

    def __str__(self):
        return "COVAL-USDT"

    def __call__(self):
        return "COVAL-USDT"


COVAL_USDT = COVAL_USDT()
"""
    name: COVAL-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CRO_EUR(NamedTuple):
    """
        name: CRO-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "CRO-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRO-EUR"

    def __str__(self):
        return "CRO-EUR"

    def __call__(self):
        return "CRO-EUR"


CRO_EUR = CRO_EUR()
"""
    name: CRO-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class CRO_USD(NamedTuple):
    """
        name: CRO-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CRO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRO-USD"

    def __str__(self):
        return "CRO-USD"

    def __call__(self):
        return "CRO-USD"


CRO_USD = CRO_USD()
"""
    name: CRO-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CRO_USDT(NamedTuple):
    """
        name: CRO-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CRO-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRO-USDT"

    def __str__(self):
        return "CRO-USDT"

    def __call__(self):
        return "CRO-USDT"


CRO_USDT = CRO_USDT()
"""
    name: CRO-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CRPT_USD(NamedTuple):
    """
        name: CRPT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CRPT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRPT-USD"

    def __str__(self):
        return "CRPT-USD"

    def __call__(self):
        return "CRPT-USD"


CRPT_USD = CRPT_USD()
"""
    name: CRPT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CRV_BTC(NamedTuple):
    """
        name: CRV-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "CRV-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRV-BTC"

    def __str__(self):
        return "CRV-BTC"

    def __call__(self):
        return "CRV-BTC"


CRV_BTC = CRV_BTC()
"""
    name: CRV-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class CRV_EUR(NamedTuple):
    """
        name: CRV-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "CRV-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRV-EUR"

    def __str__(self):
        return "CRV-EUR"

    def __call__(self):
        return "CRV-EUR"


CRV_EUR = CRV_EUR()
"""
    name: CRV-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class CRV_GBP(NamedTuple):
    """
        name: CRV-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "CRV-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRV-GBP"

    def __str__(self):
        return "CRV-GBP"

    def __call__(self):
        return "CRV-GBP"


CRV_GBP = CRV_GBP()
"""
    name: CRV-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class CRV_USD(NamedTuple):
    """
        name: CRV-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CRV-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRV-USD"

    def __str__(self):
        return "CRV-USD"

    def __call__(self):
        return "CRV-USD"


CRV_USD = CRV_USD()
"""
    name: CRV-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CTSI_BTC(NamedTuple):
    """
        name: CTSI-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "CTSI-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CTSI-BTC"

    def __str__(self):
        return "CTSI-BTC"

    def __call__(self):
        return "CTSI-BTC"


CTSI_BTC = CTSI_BTC()
"""
    name: CTSI-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class CTSI_USD(NamedTuple):
    """
        name: CTSI-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CTSI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CTSI-USD"

    def __str__(self):
        return "CTSI-USD"

    def __call__(self):
        return "CTSI-USD"


CTSI_USD = CTSI_USD()
"""
    name: CTSI-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CTX_EUR(NamedTuple):
    """
        name: CTX-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CTX-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CTX-EUR"

    def __str__(self):
        return "CTX-EUR"

    def __call__(self):
        return "CTX-EUR"


CTX_EUR = CTX_EUR()
"""
    name: CTX-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CTX_USD(NamedTuple):
    """
        name: CTX-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "CTX-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CTX-USD"

    def __str__(self):
        return "CTX-USD"

    def __call__(self):
        return "CTX-USD"


CTX_USD = CTX_USD()
"""
    name: CTX-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


class CTX_USDT(NamedTuple):
    """
        name: CTX-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "CTX-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CTX-USDT"

    def __str__(self):
        return "CTX-USDT"

    def __call__(self):
        return "CTX-USDT"


CTX_USDT = CTX_USDT()
"""
    name: CTX-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


class CVC_USD(NamedTuple):
    """
        name: CVC-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CVC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CVC-USD"

    def __str__(self):
        return "CVC-USD"

    def __call__(self):
        return "CVC-USD"


CVC_USD = CVC_USD()
"""
    name: CVC-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CVC_USDC(NamedTuple):
    """
        name: CVC-USDC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CVC-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CVC-USDC"

    def __str__(self):
        return "CVC-USDC"

    def __call__(self):
        return "CVC-USDC"


CVC_USDC = CVC_USDC()
"""
    name: CVC-USDC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class CVX_USD(NamedTuple):
    """
        name: CVX-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "CVX-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CVX-USD"

    def __str__(self):
        return "CVX-USD"

    def __call__(self):
        return "CVX-USD"


CVX_USD = CVX_USD()
"""
    name: CVX-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DAI_USD(NamedTuple):
    """
        name: DAI-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DAI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DAI-USD"

    def __str__(self):
        return "DAI-USD"

    def __call__(self):
        return "DAI-USD"


DAI_USD = DAI_USD()
"""
    name: DAI-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DAI_USDC(NamedTuple):
    """
        name: DAI-USDC
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DAI-USDC"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DAI-USDC"

    def __str__(self):
        return "DAI-USDC"

    def __call__(self):
        return "DAI-USDC"


DAI_USDC = DAI_USDC()
"""
    name: DAI-USDC
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DAR_USD(NamedTuple):
    """
        name: DAR-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DAR-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DAR-USD"

    def __str__(self):
        return "DAR-USD"

    def __call__(self):
        return "DAR-USD"


DAR_USD = DAR_USD()
"""
    name: DAR-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DASH_BTC(NamedTuple):
    """
        name: DASH-BTC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "DASH-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DASH-BTC"

    def __str__(self):
        return "DASH-BTC"

    def __call__(self):
        return "DASH-BTC"


DASH_BTC = DASH_BTC()
"""
    name: DASH-BTC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class DASH_USD(NamedTuple):
    """
        name: DASH-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DASH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DASH-USD"

    def __str__(self):
        return "DASH-USD"

    def __call__(self):
        return "DASH-USD"


DASH_USD = DASH_USD()
"""
    name: DASH-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DDX_EUR(NamedTuple):
    """
        name: DDX-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "DDX-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DDX-EUR"

    def __str__(self):
        return "DDX-EUR"

    def __call__(self):
        return "DDX-EUR"


DDX_EUR = DDX_EUR()
"""
    name: DDX-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class DDX_USD(NamedTuple):
    """
        name: DDX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DDX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DDX-USD"

    def __str__(self):
        return "DDX-USD"

    def __call__(self):
        return "DDX-USD"


DDX_USD = DDX_USD()
"""
    name: DDX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DDX_USDT(NamedTuple):
    """
        name: DDX-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DDX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DDX-USDT"

    def __str__(self):
        return "DDX-USDT"

    def __call__(self):
        return "DDX-USDT"


DDX_USDT = DDX_USDT()
"""
    name: DDX-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DESO_EUR(NamedTuple):
    """
        name: DESO-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DESO-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DESO-EUR"

    def __str__(self):
        return "DESO-EUR"

    def __call__(self):
        return "DESO-EUR"


DESO_EUR = DESO_EUR()
"""
    name: DESO-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DESO_USD(NamedTuple):
    """
        name: DESO-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DESO-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DESO-USD"

    def __str__(self):
        return "DESO-USD"

    def __call__(self):
        return "DESO-USD"


DESO_USD = DESO_USD()
"""
    name: DESO-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DESO_USDT(NamedTuple):
    """
        name: DESO-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DESO-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DESO-USDT"

    def __str__(self):
        return "DESO-USDT"

    def __call__(self):
        return "DESO-USDT"


DESO_USDT = DESO_USDT()
"""
    name: DESO-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DEXT_USD(NamedTuple):
    """
        name: DEXT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DEXT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DEXT-USD"

    def __str__(self):
        return "DEXT-USD"

    def __call__(self):
        return "DEXT-USD"


DEXT_USD = DEXT_USD()
"""
    name: DEXT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DIA_EUR(NamedTuple):
    """
        name: DIA-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DIA-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DIA-EUR"

    def __str__(self):
        return "DIA-EUR"

    def __call__(self):
        return "DIA-EUR"


DIA_EUR = DIA_EUR()
"""
    name: DIA-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DIA_USD(NamedTuple):
    """
        name: DIA-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DIA-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DIA-USD"

    def __str__(self):
        return "DIA-USD"

    def __call__(self):
        return "DIA-USD"


DIA_USD = DIA_USD()
"""
    name: DIA-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DIA_USDT(NamedTuple):
    """
        name: DIA-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DIA-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DIA-USDT"

    def __str__(self):
        return "DIA-USDT"

    def __call__(self):
        return "DIA-USDT"


DIA_USDT = DIA_USDT()
"""
    name: DIA-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DNT_USD(NamedTuple):
    """
        name: DNT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DNT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DNT-USD"

    def __str__(self):
        return "DNT-USD"

    def __call__(self):
        return "DNT-USD"


DNT_USD = DNT_USD()
"""
    name: DNT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DNT_USDC(NamedTuple):
    """
        name: DNT-USDC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DNT-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DNT-USDC"

    def __str__(self):
        return "DNT-USDC"

    def __call__(self):
        return "DNT-USDC"


DNT_USDC = DNT_USDC()
"""
    name: DNT-USDC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DOGE_BTC(NamedTuple):
    """
        name: DOGE-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "DOGE-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOGE-BTC"

    def __str__(self):
        return "DOGE-BTC"

    def __call__(self):
        return "DOGE-BTC"


DOGE_BTC = DOGE_BTC()
"""
    name: DOGE-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class DOGE_EUR(NamedTuple):
    """
        name: DOGE-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "DOGE-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOGE-EUR"

    def __str__(self):
        return "DOGE-EUR"

    def __call__(self):
        return "DOGE-EUR"


DOGE_EUR = DOGE_EUR()
"""
    name: DOGE-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class DOGE_GBP(NamedTuple):
    """
        name: DOGE-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "DOGE-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOGE-GBP"

    def __str__(self):
        return "DOGE-GBP"

    def __call__(self):
        return "DOGE-GBP"


DOGE_GBP = DOGE_GBP()
"""
    name: DOGE-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class DOGE_USD(NamedTuple):
    """
        name: DOGE-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DOGE-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOGE-USD"

    def __str__(self):
        return "DOGE-USD"

    def __call__(self):
        return "DOGE-USD"


DOGE_USD = DOGE_USD()
"""
    name: DOGE-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DOGE_USDT(NamedTuple):
    """
        name: DOGE-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DOGE-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOGE-USDT"

    def __str__(self):
        return "DOGE-USDT"

    def __call__(self):
        return "DOGE-USDT"


DOGE_USDT = DOGE_USDT()
"""
    name: DOGE-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DOT_BTC(NamedTuple):
    """
        name: DOT-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "DOT-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOT-BTC"

    def __str__(self):
        return "DOT-BTC"

    def __call__(self):
        return "DOT-BTC"


DOT_BTC = DOT_BTC()
"""
    name: DOT-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class DOT_EUR(NamedTuple):
    """
        name: DOT-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "DOT-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOT-EUR"

    def __str__(self):
        return "DOT-EUR"

    def __call__(self):
        return "DOT-EUR"


DOT_EUR = DOT_EUR()
"""
    name: DOT-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class DOT_GBP(NamedTuple):
    """
        name: DOT-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "DOT-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOT-GBP"

    def __str__(self):
        return "DOT-GBP"

    def __call__(self):
        return "DOT-GBP"


DOT_GBP = DOT_GBP()
"""
    name: DOT-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class DOT_USD(NamedTuple):
    """
        name: DOT-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DOT-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOT-USD"

    def __str__(self):
        return "DOT-USD"

    def __call__(self):
        return "DOT-USD"


DOT_USD = DOT_USD()
"""
    name: DOT-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DOT_USDT(NamedTuple):
    """
        name: DOT-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DOT-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOT-USDT"

    def __str__(self):
        return "DOT-USDT"

    def __call__(self):
        return "DOT-USDT"


DOT_USDT = DOT_USDT()
"""
    name: DOT-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DREP_USD(NamedTuple):
    """
        name: DREP-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DREP-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DREP-USD"

    def __str__(self):
        return "DREP-USD"

    def __call__(self):
        return "DREP-USD"


DREP_USD = DREP_USD()
"""
    name: DREP-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DREP_USDT(NamedTuple):
    """
        name: DREP-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DREP-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DREP-USDT"

    def __str__(self):
        return "DREP-USDT"

    def __call__(self):
        return "DREP-USDT"


DREP_USDT = DREP_USDT()
"""
    name: DREP-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DYP_USD(NamedTuple):
    """
        name: DYP-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DYP-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DYP-USD"

    def __str__(self):
        return "DYP-USD"

    def __call__(self):
        return "DYP-USD"


DYP_USD = DYP_USD()
"""
    name: DYP-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class DYP_USDT(NamedTuple):
    """
        name: DYP-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DYP-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DYP-USDT"

    def __str__(self):
        return "DYP-USDT"

    def __call__(self):
        return "DYP-USDT"


DYP_USDT = DYP_USDT()
"""
    name: DYP-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class EGLD_USD(NamedTuple):
    """
        name: EGLD-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "EGLD-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EGLD-USD"

    def __str__(self):
        return "EGLD-USD"

    def __call__(self):
        return "EGLD-USD"


EGLD_USD = EGLD_USD()
"""
    name: EGLD-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ELA_USD(NamedTuple):
    """
        name: ELA-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ELA-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ELA-USD"

    def __str__(self):
        return "ELA-USD"

    def __call__(self):
        return "ELA-USD"


ELA_USD = ELA_USD()
"""
    name: ELA-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ELA_USDT(NamedTuple):
    """
        name: ELA-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ELA-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ELA-USDT"

    def __str__(self):
        return "ELA-USDT"

    def __call__(self):
        return "ELA-USDT"


ELA_USDT = ELA_USDT()
"""
    name: ELA-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ENJ_BTC(NamedTuple):
    """
        name: ENJ-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ENJ-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENJ-BTC"

    def __str__(self):
        return "ENJ-BTC"

    def __call__(self):
        return "ENJ-BTC"


ENJ_BTC = ENJ_BTC()
"""
    name: ENJ-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ENJ_USD(NamedTuple):
    """
        name: ENJ-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ENJ-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENJ-USD"

    def __str__(self):
        return "ENJ-USD"

    def __call__(self):
        return "ENJ-USD"


ENJ_USD = ENJ_USD()
"""
    name: ENJ-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ENJ_USDT(NamedTuple):
    """
        name: ENJ-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ENJ-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENJ-USDT"

    def __str__(self):
        return "ENJ-USDT"

    def __call__(self):
        return "ENJ-USDT"


ENJ_USDT = ENJ_USDT()
"""
    name: ENJ-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ENS_EUR(NamedTuple):
    """
        name: ENS-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ENS-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENS-EUR"

    def __str__(self):
        return "ENS-EUR"

    def __call__(self):
        return "ENS-EUR"


ENS_EUR = ENS_EUR()
"""
    name: ENS-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ENS_USD(NamedTuple):
    """
        name: ENS-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ENS-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENS-USD"

    def __str__(self):
        return "ENS-USD"

    def __call__(self):
        return "ENS-USD"


ENS_USD = ENS_USD()
"""
    name: ENS-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ENS_USDT(NamedTuple):
    """
        name: ENS-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ENS-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENS-USDT"

    def __str__(self):
        return "ENS-USDT"

    def __call__(self):
        return "ENS-USDT"


ENS_USDT = ENS_USDT()
"""
    name: ENS-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class EOS_BTC(NamedTuple):
    """
        name: EOS-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "EOS-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EOS-BTC"

    def __str__(self):
        return "EOS-BTC"

    def __call__(self):
        return "EOS-BTC"


EOS_BTC = EOS_BTC()
"""
    name: EOS-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class EOS_EUR(NamedTuple):
    """
        name: EOS-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "EOS-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EOS-EUR"

    def __str__(self):
        return "EOS-EUR"

    def __call__(self):
        return "EOS-EUR"


EOS_EUR = EOS_EUR()
"""
    name: EOS-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class EOS_USD(NamedTuple):
    """
        name: EOS-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "EOS-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EOS-USD"

    def __str__(self):
        return "EOS-USD"

    def __call__(self):
        return "EOS-USD"


EOS_USD = EOS_USD()
"""
    name: EOS-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ERN_EUR(NamedTuple):
    """
        name: ERN-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ERN-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ERN-EUR"

    def __str__(self):
        return "ERN-EUR"

    def __call__(self):
        return "ERN-EUR"


ERN_EUR = ERN_EUR()
"""
    name: ERN-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ERN_USD(NamedTuple):
    """
        name: ERN-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ERN-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ERN-USD"

    def __str__(self):
        return "ERN-USD"

    def __call__(self):
        return "ERN-USD"


ERN_USD = ERN_USD()
"""
    name: ERN-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ERN_USDT(NamedTuple):
    """
        name: ERN-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ERN-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ERN-USDT"

    def __str__(self):
        return "ERN-USDT"

    def __call__(self):
        return "ERN-USDT"


ERN_USDT = ERN_USDT()
"""
    name: ERN-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ETC_BTC(NamedTuple):
    """
        name: ETC-BTC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ETC-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETC-BTC"

    def __str__(self):
        return "ETC-BTC"

    def __call__(self):
        return "ETC-BTC"


ETC_BTC = ETC_BTC()
"""
    name: ETC-BTC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ETC_EUR(NamedTuple):
    """
        name: ETC-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ETC-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETC-EUR"

    def __str__(self):
        return "ETC-EUR"

    def __call__(self):
        return "ETC-EUR"


ETC_EUR = ETC_EUR()
"""
    name: ETC-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ETC_GBP(NamedTuple):
    """
        name: ETC-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "ETC-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETC-GBP"

    def __str__(self):
        return "ETC-GBP"

    def __call__(self):
        return "ETC-GBP"


ETC_GBP = ETC_GBP()
"""
    name: ETC-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class ETC_USD(NamedTuple):
    """
        name: ETC-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ETC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETC-USD"

    def __str__(self):
        return "ETC-USD"

    def __call__(self):
        return "ETC-USD"


ETC_USD = ETC_USD()
"""
    name: ETC-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ETH_BTC(NamedTuple):
    """
        name: ETH-BTC
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00001
        maximum_order_size: None
        margin: False
    """
    name: str = "ETH-BTC"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH-BTC"

    def __str__(self):
        return "ETH-BTC"

    def __call__(self):
        return "ETH-BTC"


ETH_BTC = ETH_BTC()
"""
    name: ETH-BTC
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00001
    maximum_order_size: None
    margin: False
"""


class ETH_DAI(NamedTuple):
    """
        name: ETH-DAI
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ETH-DAI"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH-DAI"

    def __str__(self):
        return "ETH-DAI"

    def __call__(self):
        return "ETH-DAI"


ETH_DAI = ETH_DAI()
"""
    name: ETH-DAI
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ETH_EUR(NamedTuple):
    """
        name: ETH-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ETH-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH-EUR"

    def __str__(self):
        return "ETH-EUR"

    def __call__(self):
        return "ETH-EUR"


ETH_EUR = ETH_EUR()
"""
    name: ETH-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ETH_GBP(NamedTuple):
    """
        name: ETH-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "ETH-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH-GBP"

    def __str__(self):
        return "ETH-GBP"

    def __call__(self):
        return "ETH-GBP"


ETH_GBP = ETH_GBP()
"""
    name: ETH-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class ETH_USD(NamedTuple):
    """
        name: ETH-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ETH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH-USD"

    def __str__(self):
        return "ETH-USD"

    def __call__(self):
        return "ETH-USD"


ETH_USD = ETH_USD()
"""
    name: ETH-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ETH_USDC(NamedTuple):
    """
        name: ETH-USDC
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ETH-USDC"
    precision: int = 1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH-USDC"

    def __str__(self):
        return "ETH-USDC"

    def __call__(self):
        return "ETH-USDC"


ETH_USDC = ETH_USDC()
"""
    name: ETH-USDC
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ETH_USDT(NamedTuple):
    """
        name: ETH-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ETH-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH-USDT"

    def __str__(self):
        return "ETH-USDT"

    def __call__(self):
        return "ETH-USDT"


ETH_USDT = ETH_USDT()
"""
    name: ETH-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FARM_USD(NamedTuple):
    """
        name: FARM-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FARM-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FARM-USD"

    def __str__(self):
        return "FARM-USD"

    def __call__(self):
        return "FARM-USD"


FARM_USD = FARM_USD()
"""
    name: FARM-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FARM_USDT(NamedTuple):
    """
        name: FARM-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FARM-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FARM-USDT"

    def __str__(self):
        return "FARM-USDT"

    def __call__(self):
        return "FARM-USDT"


FARM_USDT = FARM_USDT()
"""
    name: FARM-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FET_USD(NamedTuple):
    """
        name: FET-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FET-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FET-USD"

    def __str__(self):
        return "FET-USD"

    def __call__(self):
        return "FET-USD"


FET_USD = FET_USD()
"""
    name: FET-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FET_USDT(NamedTuple):
    """
        name: FET-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FET-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FET-USDT"

    def __str__(self):
        return "FET-USDT"

    def __call__(self):
        return "FET-USDT"


FET_USDT = FET_USDT()
"""
    name: FET-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FIDA_EUR(NamedTuple):
    """
        name: FIDA-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FIDA-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIDA-EUR"

    def __str__(self):
        return "FIDA-EUR"

    def __call__(self):
        return "FIDA-EUR"


FIDA_EUR = FIDA_EUR()
"""
    name: FIDA-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FIDA_USD(NamedTuple):
    """
        name: FIDA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FIDA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIDA-USD"

    def __str__(self):
        return "FIDA-USD"

    def __call__(self):
        return "FIDA-USD"


FIDA_USD = FIDA_USD()
"""
    name: FIDA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FIDA_USDT(NamedTuple):
    """
        name: FIDA-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FIDA-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIDA-USDT"

    def __str__(self):
        return "FIDA-USDT"

    def __call__(self):
        return "FIDA-USDT"


FIDA_USDT = FIDA_USDT()
"""
    name: FIDA-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FIL_BTC(NamedTuple):
    """
        name: FIL-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "FIL-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIL-BTC"

    def __str__(self):
        return "FIL-BTC"

    def __call__(self):
        return "FIL-BTC"


FIL_BTC = FIL_BTC()
"""
    name: FIL-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class FIL_EUR(NamedTuple):
    """
        name: FIL-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "FIL-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIL-EUR"

    def __str__(self):
        return "FIL-EUR"

    def __call__(self):
        return "FIL-EUR"


FIL_EUR = FIL_EUR()
"""
    name: FIL-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class FIL_GBP(NamedTuple):
    """
        name: FIL-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "FIL-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIL-GBP"

    def __str__(self):
        return "FIL-GBP"

    def __call__(self):
        return "FIL-GBP"


FIL_GBP = FIL_GBP()
"""
    name: FIL-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class FIL_USD(NamedTuple):
    """
        name: FIL-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FIL-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIL-USD"

    def __str__(self):
        return "FIL-USD"

    def __call__(self):
        return "FIL-USD"


FIL_USD = FIL_USD()
"""
    name: FIL-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FIS_USD(NamedTuple):
    """
        name: FIS-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FIS-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIS-USD"

    def __str__(self):
        return "FIS-USD"

    def __call__(self):
        return "FIS-USD"


FIS_USD = FIS_USD()
"""
    name: FIS-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FIS_USDT(NamedTuple):
    """
        name: FIS-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FIS-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIS-USDT"

    def __str__(self):
        return "FIS-USDT"

    def __call__(self):
        return "FIS-USDT"


FIS_USDT = FIS_USDT()
"""
    name: FIS-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FLOW_USD(NamedTuple):
    """
        name: FLOW-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FLOW-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLOW-USD"

    def __str__(self):
        return "FLOW-USD"

    def __call__(self):
        return "FLOW-USD"


FLOW_USD = FLOW_USD()
"""
    name: FLOW-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FLOW_USDT(NamedTuple):
    """
        name: FLOW-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FLOW-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLOW-USDT"

    def __str__(self):
        return "FLOW-USDT"

    def __call__(self):
        return "FLOW-USDT"


FLOW_USDT = FLOW_USDT()
"""
    name: FLOW-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FORT_USD(NamedTuple):
    """
        name: FORT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FORT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FORT-USD"

    def __str__(self):
        return "FORT-USD"

    def __call__(self):
        return "FORT-USD"


FORT_USD = FORT_USD()
"""
    name: FORT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FORT_USDT(NamedTuple):
    """
        name: FORT-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FORT-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FORT-USDT"

    def __str__(self):
        return "FORT-USDT"

    def __call__(self):
        return "FORT-USDT"


FORT_USDT = FORT_USDT()
"""
    name: FORT-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FORTH_BTC(NamedTuple):
    """
        name: FORTH-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "FORTH-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FORTH-BTC"

    def __str__(self):
        return "FORTH-BTC"

    def __call__(self):
        return "FORTH-BTC"


FORTH_BTC = FORTH_BTC()
"""
    name: FORTH-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class FORTH_EUR(NamedTuple):
    """
        name: FORTH-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "FORTH-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FORTH-EUR"

    def __str__(self):
        return "FORTH-EUR"

    def __call__(self):
        return "FORTH-EUR"


FORTH_EUR = FORTH_EUR()
"""
    name: FORTH-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class FORTH_GBP(NamedTuple):
    """
        name: FORTH-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "FORTH-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FORTH-GBP"

    def __str__(self):
        return "FORTH-GBP"

    def __call__(self):
        return "FORTH-GBP"


FORTH_GBP = FORTH_GBP()
"""
    name: FORTH-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class FORTH_USD(NamedTuple):
    """
        name: FORTH-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FORTH-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FORTH-USD"

    def __str__(self):
        return "FORTH-USD"

    def __call__(self):
        return "FORTH-USD"


FORTH_USD = FORTH_USD()
"""
    name: FORTH-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FOX_USD(NamedTuple):
    """
        name: FOX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FOX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FOX-USD"

    def __str__(self):
        return "FOX-USD"

    def __call__(self):
        return "FOX-USD"


FOX_USD = FOX_USD()
"""
    name: FOX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FOX_USDT(NamedTuple):
    """
        name: FOX-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FOX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FOX-USDT"

    def __str__(self):
        return "FOX-USDT"

    def __call__(self):
        return "FOX-USDT"


FOX_USDT = FOX_USDT()
"""
    name: FOX-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class FX_USD(NamedTuple):
    """
        name: FX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FX-USD"

    def __str__(self):
        return "FX-USD"

    def __call__(self):
        return "FX-USD"


FX_USD = FX_USD()
"""
    name: FX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GAL_USD(NamedTuple):
    """
        name: GAL-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GAL-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GAL-USD"

    def __str__(self):
        return "GAL-USD"

    def __call__(self):
        return "GAL-USD"


GAL_USD = GAL_USD()
"""
    name: GAL-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GAL_USDT(NamedTuple):
    """
        name: GAL-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GAL-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GAL-USDT"

    def __str__(self):
        return "GAL-USDT"

    def __call__(self):
        return "GAL-USDT"


GAL_USDT = GAL_USDT()
"""
    name: GAL-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GALA_EUR(NamedTuple):
    """
        name: GALA-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "GALA-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALA-EUR"

    def __str__(self):
        return "GALA-EUR"

    def __call__(self):
        return "GALA-EUR"


GALA_EUR = GALA_EUR()
"""
    name: GALA-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class GALA_USD(NamedTuple):
    """
        name: GALA-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GALA-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALA-USD"

    def __str__(self):
        return "GALA-USD"

    def __call__(self):
        return "GALA-USD"


GALA_USD = GALA_USD()
"""
    name: GALA-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GALA_USDT(NamedTuple):
    """
        name: GALA-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GALA-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALA-USDT"

    def __str__(self):
        return "GALA-USDT"

    def __call__(self):
        return "GALA-USDT"


GALA_USDT = GALA_USDT()
"""
    name: GALA-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GFI_USD(NamedTuple):
    """
        name: GFI-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GFI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GFI-USD"

    def __str__(self):
        return "GFI-USD"

    def __call__(self):
        return "GFI-USD"


GFI_USD = GFI_USD()
"""
    name: GFI-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GHST_USD(NamedTuple):
    """
        name: GHST-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GHST-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GHST-USD"

    def __str__(self):
        return "GHST-USD"

    def __call__(self):
        return "GHST-USD"


GHST_USD = GHST_USD()
"""
    name: GHST-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GLM_USD(NamedTuple):
    """
        name: GLM-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GLM-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GLM-USD"

    def __str__(self):
        return "GLM-USD"

    def __call__(self):
        return "GLM-USD"


GLM_USD = GLM_USD()
"""
    name: GLM-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GMT_USD(NamedTuple):
    """
        name: GMT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GMT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GMT-USD"

    def __str__(self):
        return "GMT-USD"

    def __call__(self):
        return "GMT-USD"


GMT_USD = GMT_USD()
"""
    name: GMT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GMT_USDT(NamedTuple):
    """
        name: GMT-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GMT-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GMT-USDT"

    def __str__(self):
        return "GMT-USDT"

    def __call__(self):
        return "GMT-USDT"


GMT_USDT = GMT_USDT()
"""
    name: GMT-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GNO_USD(NamedTuple):
    """
        name: GNO-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GNO-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GNO-USD"

    def __str__(self):
        return "GNO-USD"

    def __call__(self):
        return "GNO-USD"


GNO_USD = GNO_USD()
"""
    name: GNO-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GNO_USDT(NamedTuple):
    """
        name: GNO-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GNO-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GNO-USDT"

    def __str__(self):
        return "GNO-USDT"

    def __call__(self):
        return "GNO-USDT"


GNO_USDT = GNO_USDT()
"""
    name: GNO-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GNT_USDC(NamedTuple):
    """
        name: GNT-USDC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GNT-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GNT-USDC"

    def __str__(self):
        return "GNT-USDC"

    def __call__(self):
        return "GNT-USDC"


GNT_USDC = GNT_USDC()
"""
    name: GNT-USDC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GODS_USD(NamedTuple):
    """
        name: GODS-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GODS-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GODS-USD"

    def __str__(self):
        return "GODS-USD"

    def __call__(self):
        return "GODS-USD"


GODS_USD = GODS_USD()
"""
    name: GODS-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GRT_BTC(NamedTuple):
    """
        name: GRT-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "GRT-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRT-BTC"

    def __str__(self):
        return "GRT-BTC"

    def __call__(self):
        return "GRT-BTC"


GRT_BTC = GRT_BTC()
"""
    name: GRT-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class GRT_EUR(NamedTuple):
    """
        name: GRT-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "GRT-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRT-EUR"

    def __str__(self):
        return "GRT-EUR"

    def __call__(self):
        return "GRT-EUR"


GRT_EUR = GRT_EUR()
"""
    name: GRT-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class GRT_GBP(NamedTuple):
    """
        name: GRT-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "GRT-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRT-GBP"

    def __str__(self):
        return "GRT-GBP"

    def __call__(self):
        return "GRT-GBP"


GRT_GBP = GRT_GBP()
"""
    name: GRT-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class GRT_USD(NamedTuple):
    """
        name: GRT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GRT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRT-USD"

    def __str__(self):
        return "GRT-USD"

    def __call__(self):
        return "GRT-USD"


GRT_USD = GRT_USD()
"""
    name: GRT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GST_USD(NamedTuple):
    """
        name: GST-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GST-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GST-USD"

    def __str__(self):
        return "GST-USD"

    def __call__(self):
        return "GST-USD"


GST_USD = GST_USD()
"""
    name: GST-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GTC_USD(NamedTuple):
    """
        name: GTC-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GTC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GTC-USD"

    def __str__(self):
        return "GTC-USD"

    def __call__(self):
        return "GTC-USD"


GTC_USD = GTC_USD()
"""
    name: GTC-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GUSD_USD(NamedTuple):
    """
        name: GUSD-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GUSD-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GUSD-USD"

    def __str__(self):
        return "GUSD-USD"

    def __call__(self):
        return "GUSD-USD"


GUSD_USD = GUSD_USD()
"""
    name: GUSD-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class GYEN_USD(NamedTuple):
    """
        name: GYEN-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "GYEN-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GYEN-USD"

    def __str__(self):
        return "GYEN-USD"

    def __call__(self):
        return "GYEN-USD"


GYEN_USD = GYEN_USD()
"""
    name: GYEN-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class HBAR_USD(NamedTuple):
    """
        name: HBAR-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "HBAR-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HBAR-USD"

    def __str__(self):
        return "HBAR-USD"

    def __call__(self):
        return "HBAR-USD"


HBAR_USD = HBAR_USD()
"""
    name: HBAR-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class HBAR_USDT(NamedTuple):
    """
        name: HBAR-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "HBAR-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HBAR-USDT"

    def __str__(self):
        return "HBAR-USDT"

    def __call__(self):
        return "HBAR-USDT"


HBAR_USDT = HBAR_USDT()
"""
    name: HBAR-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class HFT_USD(NamedTuple):
    """
        name: HFT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "HFT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HFT-USD"

    def __str__(self):
        return "HFT-USD"

    def __call__(self):
        return "HFT-USD"


HFT_USD = HFT_USD()
"""
    name: HFT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class HFT_USDT(NamedTuple):
    """
        name: HFT-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "HFT-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HFT-USDT"

    def __str__(self):
        return "HFT-USDT"

    def __call__(self):
        return "HFT-USDT"


HFT_USDT = HFT_USDT()
"""
    name: HFT-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class HIGH_USD(NamedTuple):
    """
        name: HIGH-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "HIGH-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HIGH-USD"

    def __str__(self):
        return "HIGH-USD"

    def __call__(self):
        return "HIGH-USD"


HIGH_USD = HIGH_USD()
"""
    name: HIGH-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class HOPR_USD(NamedTuple):
    """
        name: HOPR-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "HOPR-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HOPR-USD"

    def __str__(self):
        return "HOPR-USD"

    def __call__(self):
        return "HOPR-USD"


HOPR_USD = HOPR_USD()
"""
    name: HOPR-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class HOPR_USDT(NamedTuple):
    """
        name: HOPR-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "HOPR-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HOPR-USDT"

    def __str__(self):
        return "HOPR-USDT"

    def __call__(self):
        return "HOPR-USDT"


HOPR_USDT = HOPR_USDT()
"""
    name: HOPR-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ICP_BTC(NamedTuple):
    """
        name: ICP-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ICP-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICP-BTC"

    def __str__(self):
        return "ICP-BTC"

    def __call__(self):
        return "ICP-BTC"


ICP_BTC = ICP_BTC()
"""
    name: ICP-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ICP_EUR(NamedTuple):
    """
        name: ICP-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ICP-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICP-EUR"

    def __str__(self):
        return "ICP-EUR"

    def __call__(self):
        return "ICP-EUR"


ICP_EUR = ICP_EUR()
"""
    name: ICP-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ICP_GBP(NamedTuple):
    """
        name: ICP-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "ICP-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICP-GBP"

    def __str__(self):
        return "ICP-GBP"

    def __call__(self):
        return "ICP-GBP"


ICP_GBP = ICP_GBP()
"""
    name: ICP-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class ICP_USD(NamedTuple):
    """
        name: ICP-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ICP-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICP-USD"

    def __str__(self):
        return "ICP-USD"

    def __call__(self):
        return "ICP-USD"


ICP_USD = ICP_USD()
"""
    name: ICP-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ICP_USDT(NamedTuple):
    """
        name: ICP-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ICP-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICP-USDT"

    def __str__(self):
        return "ICP-USDT"

    def __call__(self):
        return "ICP-USDT"


ICP_USDT = ICP_USDT()
"""
    name: ICP-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class IDEX_USD(NamedTuple):
    """
        name: IDEX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "IDEX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IDEX-USD"

    def __str__(self):
        return "IDEX-USD"

    def __call__(self):
        return "IDEX-USD"


IDEX_USD = IDEX_USD()
"""
    name: IDEX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class IDEX_USDT(NamedTuple):
    """
        name: IDEX-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "IDEX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IDEX-USDT"

    def __str__(self):
        return "IDEX-USDT"

    def __call__(self):
        return "IDEX-USDT"


IDEX_USDT = IDEX_USDT()
"""
    name: IDEX-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ILV_USD(NamedTuple):
    """
        name: ILV-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ILV-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ILV-USD"

    def __str__(self):
        return "ILV-USD"

    def __call__(self):
        return "ILV-USD"


ILV_USD = ILV_USD()
"""
    name: ILV-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class IMX_USD(NamedTuple):
    """
        name: IMX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "IMX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IMX-USD"

    def __str__(self):
        return "IMX-USD"

    def __call__(self):
        return "IMX-USD"


IMX_USD = IMX_USD()
"""
    name: IMX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class IMX_USDT(NamedTuple):
    """
        name: IMX-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "IMX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IMX-USDT"

    def __str__(self):
        return "IMX-USDT"

    def __call__(self):
        return "IMX-USDT"


IMX_USDT = IMX_USDT()
"""
    name: IMX-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class INDEX_USD(NamedTuple):
    """
        name: INDEX-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "INDEX-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "INDEX-USD"

    def __str__(self):
        return "INDEX-USD"

    def __call__(self):
        return "INDEX-USD"


INDEX_USD = INDEX_USD()
"""
    name: INDEX-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class INDEX_USDT(NamedTuple):
    """
        name: INDEX-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "INDEX-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "INDEX-USDT"

    def __str__(self):
        return "INDEX-USDT"

    def __call__(self):
        return "INDEX-USDT"


INDEX_USDT = INDEX_USDT()
"""
    name: INDEX-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class INJ_USD(NamedTuple):
    """
        name: INJ-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "INJ-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "INJ-USD"

    def __str__(self):
        return "INJ-USD"

    def __call__(self):
        return "INJ-USD"


INJ_USD = INJ_USD()
"""
    name: INJ-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class INV_USD(NamedTuple):
    """
        name: INV-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "INV-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "INV-USD"

    def __str__(self):
        return "INV-USD"

    def __call__(self):
        return "INV-USD"


INV_USD = INV_USD()
"""
    name: INV-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class IOTX_EUR(NamedTuple):
    """
        name: IOTX-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "IOTX-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IOTX-EUR"

    def __str__(self):
        return "IOTX-EUR"

    def __call__(self):
        return "IOTX-EUR"


IOTX_EUR = IOTX_EUR()
"""
    name: IOTX-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class IOTX_USD(NamedTuple):
    """
        name: IOTX-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "IOTX-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IOTX-USD"

    def __str__(self):
        return "IOTX-USD"

    def __call__(self):
        return "IOTX-USD"


IOTX_USD = IOTX_USD()
"""
    name: IOTX-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class JASMY_USD(NamedTuple):
    """
        name: JASMY-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "JASMY-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "JASMY-USD"

    def __str__(self):
        return "JASMY-USD"

    def __call__(self):
        return "JASMY-USD"


JASMY_USD = JASMY_USD()
"""
    name: JASMY-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class JASMY_USDT(NamedTuple):
    """
        name: JASMY-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "JASMY-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "JASMY-USDT"

    def __str__(self):
        return "JASMY-USDT"

    def __call__(self):
        return "JASMY-USDT"


JASMY_USDT = JASMY_USDT()
"""
    name: JASMY-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class JUP_USD(NamedTuple):
    """
        name: JUP-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "JUP-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "JUP-USD"

    def __str__(self):
        return "JUP-USD"

    def __call__(self):
        return "JUP-USD"


JUP_USD = JUP_USD()
"""
    name: JUP-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class KAVA_USD(NamedTuple):
    """
        name: KAVA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "KAVA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KAVA-USD"

    def __str__(self):
        return "KAVA-USD"

    def __call__(self):
        return "KAVA-USD"


KAVA_USD = KAVA_USD()
"""
    name: KAVA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class KEEP_USD(NamedTuple):
    """
        name: KEEP-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "KEEP-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KEEP-USD"

    def __str__(self):
        return "KEEP-USD"

    def __call__(self):
        return "KEEP-USD"


KEEP_USD = KEEP_USD()
"""
    name: KEEP-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class KNC_BTC(NamedTuple):
    """
        name: KNC-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "KNC-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KNC-BTC"

    def __str__(self):
        return "KNC-BTC"

    def __call__(self):
        return "KNC-BTC"


KNC_BTC = KNC_BTC()
"""
    name: KNC-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class KNC_USD(NamedTuple):
    """
        name: KNC-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "KNC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KNC-USD"

    def __str__(self):
        return "KNC-USD"

    def __call__(self):
        return "KNC-USD"


KNC_USD = KNC_USD()
"""
    name: KNC-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class KRL_EUR(NamedTuple):
    """
        name: KRL-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "KRL-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KRL-EUR"

    def __str__(self):
        return "KRL-EUR"

    def __call__(self):
        return "KRL-EUR"


KRL_EUR = KRL_EUR()
"""
    name: KRL-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class KRL_USD(NamedTuple):
    """
        name: KRL-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "KRL-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KRL-USD"

    def __str__(self):
        return "KRL-USD"

    def __call__(self):
        return "KRL-USD"


KRL_USD = KRL_USD()
"""
    name: KRL-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class KRL_USDT(NamedTuple):
    """
        name: KRL-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "KRL-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KRL-USDT"

    def __str__(self):
        return "KRL-USDT"

    def __call__(self):
        return "KRL-USDT"


KRL_USDT = KRL_USDT()
"""
    name: KRL-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class KSM_USD(NamedTuple):
    """
        name: KSM-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "KSM-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSM-USD"

    def __str__(self):
        return "KSM-USD"

    def __call__(self):
        return "KSM-USD"


KSM_USD = KSM_USD()
"""
    name: KSM-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class KSM_USDT(NamedTuple):
    """
        name: KSM-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "KSM-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSM-USDT"

    def __str__(self):
        return "KSM-USDT"

    def __call__(self):
        return "KSM-USDT"


KSM_USDT = KSM_USDT()
"""
    name: KSM-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LCX_EUR(NamedTuple):
    """
        name: LCX-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "LCX-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LCX-EUR"

    def __str__(self):
        return "LCX-EUR"

    def __call__(self):
        return "LCX-EUR"


LCX_EUR = LCX_EUR()
"""
    name: LCX-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class LCX_USD(NamedTuple):
    """
        name: LCX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LCX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LCX-USD"

    def __str__(self):
        return "LCX-USD"

    def __call__(self):
        return "LCX-USD"


LCX_USD = LCX_USD()
"""
    name: LCX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LCX_USDT(NamedTuple):
    """
        name: LCX-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LCX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LCX-USDT"

    def __str__(self):
        return "LCX-USDT"

    def __call__(self):
        return "LCX-USDT"


LCX_USDT = LCX_USDT()
"""
    name: LCX-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LDO_USD(NamedTuple):
    """
        name: LDO-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LDO-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LDO-USD"

    def __str__(self):
        return "LDO-USD"

    def __call__(self):
        return "LDO-USD"


LDO_USD = LDO_USD()
"""
    name: LDO-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LINK_BTC(NamedTuple):
    """
        name: LINK-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "LINK-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINK-BTC"

    def __str__(self):
        return "LINK-BTC"

    def __call__(self):
        return "LINK-BTC"


LINK_BTC = LINK_BTC()
"""
    name: LINK-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class LINK_ETH(NamedTuple):
    """
        name: LINK-ETH
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00022
        maximum_order_size: None
        margin: False
    """
    name: str = "LINK-ETH"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINK-ETH"

    def __str__(self):
        return "LINK-ETH"

    def __call__(self):
        return "LINK-ETH"


LINK_ETH = LINK_ETH()
"""
    name: LINK-ETH
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00022
    maximum_order_size: None
    margin: False
"""


class LINK_EUR(NamedTuple):
    """
        name: LINK-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "LINK-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINK-EUR"

    def __str__(self):
        return "LINK-EUR"

    def __call__(self):
        return "LINK-EUR"


LINK_EUR = LINK_EUR()
"""
    name: LINK-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class LINK_GBP(NamedTuple):
    """
        name: LINK-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "LINK-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINK-GBP"

    def __str__(self):
        return "LINK-GBP"

    def __call__(self):
        return "LINK-GBP"


LINK_GBP = LINK_GBP()
"""
    name: LINK-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class LINK_USD(NamedTuple):
    """
        name: LINK-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LINK-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINK-USD"

    def __str__(self):
        return "LINK-USD"

    def __call__(self):
        return "LINK-USD"


LINK_USD = LINK_USD()
"""
    name: LINK-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LINK_USDT(NamedTuple):
    """
        name: LINK-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LINK-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINK-USDT"

    def __str__(self):
        return "LINK-USDT"

    def __call__(self):
        return "LINK-USDT"


LINK_USDT = LINK_USDT()
"""
    name: LINK-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LIT_USD(NamedTuple):
    """
        name: LIT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LIT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LIT-USD"

    def __str__(self):
        return "LIT-USD"

    def __call__(self):
        return "LIT-USD"


LIT_USD = LIT_USD()
"""
    name: LIT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LOKA_USD(NamedTuple):
    """
        name: LOKA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LOKA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LOKA-USD"

    def __str__(self):
        return "LOKA-USD"

    def __call__(self):
        return "LOKA-USD"


LOKA_USD = LOKA_USD()
"""
    name: LOKA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LOOM_USD(NamedTuple):
    """
        name: LOOM-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LOOM-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LOOM-USD"

    def __str__(self):
        return "LOOM-USD"

    def __call__(self):
        return "LOOM-USD"


LOOM_USD = LOOM_USD()
"""
    name: LOOM-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LOOM_USDC(NamedTuple):
    """
        name: LOOM-USDC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LOOM-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LOOM-USDC"

    def __str__(self):
        return "LOOM-USDC"

    def __call__(self):
        return "LOOM-USDC"


LOOM_USDC = LOOM_USDC()
"""
    name: LOOM-USDC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LPT_USD(NamedTuple):
    """
        name: LPT-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LPT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LPT-USD"

    def __str__(self):
        return "LPT-USD"

    def __call__(self):
        return "LPT-USD"


LPT_USD = LPT_USD()
"""
    name: LPT-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LQTY_EUR(NamedTuple):
    """
        name: LQTY-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LQTY-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LQTY-EUR"

    def __str__(self):
        return "LQTY-EUR"

    def __call__(self):
        return "LQTY-EUR"


LQTY_EUR = LQTY_EUR()
"""
    name: LQTY-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LQTY_USD(NamedTuple):
    """
        name: LQTY-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LQTY-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LQTY-USD"

    def __str__(self):
        return "LQTY-USD"

    def __call__(self):
        return "LQTY-USD"


LQTY_USD = LQTY_USD()
"""
    name: LQTY-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LQTY_USDT(NamedTuple):
    """
        name: LQTY-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LQTY-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LQTY-USDT"

    def __str__(self):
        return "LQTY-USDT"

    def __call__(self):
        return "LQTY-USDT"


LQTY_USDT = LQTY_USDT()
"""
    name: LQTY-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LRC_BTC(NamedTuple):
    """
        name: LRC-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "LRC-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LRC-BTC"

    def __str__(self):
        return "LRC-BTC"

    def __call__(self):
        return "LRC-BTC"


LRC_BTC = LRC_BTC()
"""
    name: LRC-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class LRC_USD(NamedTuple):
    """
        name: LRC-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LRC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LRC-USD"

    def __str__(self):
        return "LRC-USD"

    def __call__(self):
        return "LRC-USD"


LRC_USD = LRC_USD()
"""
    name: LRC-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LRC_USDT(NamedTuple):
    """
        name: LRC-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LRC-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LRC-USDT"

    def __str__(self):
        return "LRC-USDT"

    def __call__(self):
        return "LRC-USDT"


LRC_USDT = LRC_USDT()
"""
    name: LRC-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class LTC_BTC(NamedTuple):
    """
        name: LTC-BTC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "LTC-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTC-BTC"

    def __str__(self):
        return "LTC-BTC"

    def __call__(self):
        return "LTC-BTC"


LTC_BTC = LTC_BTC()
"""
    name: LTC-BTC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class LTC_EUR(NamedTuple):
    """
        name: LTC-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "LTC-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTC-EUR"

    def __str__(self):
        return "LTC-EUR"

    def __call__(self):
        return "LTC-EUR"


LTC_EUR = LTC_EUR()
"""
    name: LTC-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class LTC_GBP(NamedTuple):
    """
        name: LTC-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "LTC-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTC-GBP"

    def __str__(self):
        return "LTC-GBP"

    def __call__(self):
        return "LTC-GBP"


LTC_GBP = LTC_GBP()
"""
    name: LTC-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class LTC_USD(NamedTuple):
    """
        name: LTC-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "LTC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTC-USD"

    def __str__(self):
        return "LTC-USD"

    def __call__(self):
        return "LTC-USD"


LTC_USD = LTC_USD()
"""
    name: LTC-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MAGIC_USD(NamedTuple):
    """
        name: MAGIC-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MAGIC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MAGIC-USD"

    def __str__(self):
        return "MAGIC-USD"

    def __call__(self):
        return "MAGIC-USD"


MAGIC_USD = MAGIC_USD()
"""
    name: MAGIC-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MANA_BTC(NamedTuple):
    """
        name: MANA-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "MANA-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANA-BTC"

    def __str__(self):
        return "MANA-BTC"

    def __call__(self):
        return "MANA-BTC"


MANA_BTC = MANA_BTC()
"""
    name: MANA-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class MANA_ETH(NamedTuple):
    """
        name: MANA-ETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00022
        maximum_order_size: None
        margin: False
    """
    name: str = "MANA-ETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANA-ETH"

    def __str__(self):
        return "MANA-ETH"

    def __call__(self):
        return "MANA-ETH"


MANA_ETH = MANA_ETH()
"""
    name: MANA-ETH
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00022
    maximum_order_size: None
    margin: False
"""


class MANA_EUR(NamedTuple):
    """
        name: MANA-EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "MANA-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANA-EUR"

    def __str__(self):
        return "MANA-EUR"

    def __call__(self):
        return "MANA-EUR"


MANA_EUR = MANA_EUR()
"""
    name: MANA-EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class MANA_USD(NamedTuple):
    """
        name: MANA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MANA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANA-USD"

    def __str__(self):
        return "MANA-USD"

    def __call__(self):
        return "MANA-USD"


MANA_USD = MANA_USD()
"""
    name: MANA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MANA_USDC(NamedTuple):
    """
        name: MANA-USDC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MANA-USDC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANA-USDC"

    def __str__(self):
        return "MANA-USDC"

    def __call__(self):
        return "MANA-USDC"


MANA_USDC = MANA_USDC()
"""
    name: MANA-USDC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MASK_EUR(NamedTuple):
    """
        name: MASK-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "MASK-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MASK-EUR"

    def __str__(self):
        return "MASK-EUR"

    def __call__(self):
        return "MASK-EUR"


MASK_EUR = MASK_EUR()
"""
    name: MASK-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class MASK_GBP(NamedTuple):
    """
        name: MASK-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "MASK-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MASK-GBP"

    def __str__(self):
        return "MASK-GBP"

    def __call__(self):
        return "MASK-GBP"


MASK_GBP = MASK_GBP()
"""
    name: MASK-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class MASK_USD(NamedTuple):
    """
        name: MASK-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MASK-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MASK-USD"

    def __str__(self):
        return "MASK-USD"

    def __call__(self):
        return "MASK-USD"


MASK_USD = MASK_USD()
"""
    name: MASK-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MASK_USDT(NamedTuple):
    """
        name: MASK-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MASK-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MASK-USDT"

    def __str__(self):
        return "MASK-USDT"

    def __call__(self):
        return "MASK-USDT"


MASK_USDT = MASK_USDT()
"""
    name: MASK-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MATH_USD(NamedTuple):
    """
        name: MATH-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MATH-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATH-USD"

    def __str__(self):
        return "MATH-USD"

    def __call__(self):
        return "MATH-USD"


MATH_USD = MATH_USD()
"""
    name: MATH-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MATH_USDT(NamedTuple):
    """
        name: MATH-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MATH-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATH-USDT"

    def __str__(self):
        return "MATH-USDT"

    def __call__(self):
        return "MATH-USDT"


MATH_USDT = MATH_USDT()
"""
    name: MATH-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MATIC_BTC(NamedTuple):
    """
        name: MATIC-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "MATIC-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATIC-BTC"

    def __str__(self):
        return "MATIC-BTC"

    def __call__(self):
        return "MATIC-BTC"


MATIC_BTC = MATIC_BTC()
"""
    name: MATIC-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class MATIC_EUR(NamedTuple):
    """
        name: MATIC-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "MATIC-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATIC-EUR"

    def __str__(self):
        return "MATIC-EUR"

    def __call__(self):
        return "MATIC-EUR"


MATIC_EUR = MATIC_EUR()
"""
    name: MATIC-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class MATIC_GBP(NamedTuple):
    """
        name: MATIC-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "MATIC-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATIC-GBP"

    def __str__(self):
        return "MATIC-GBP"

    def __call__(self):
        return "MATIC-GBP"


MATIC_GBP = MATIC_GBP()
"""
    name: MATIC-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class MATIC_USD(NamedTuple):
    """
        name: MATIC-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MATIC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATIC-USD"

    def __str__(self):
        return "MATIC-USD"

    def __call__(self):
        return "MATIC-USD"


MATIC_USD = MATIC_USD()
"""
    name: MATIC-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MATIC_USDT(NamedTuple):
    """
        name: MATIC-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MATIC-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATIC-USDT"

    def __str__(self):
        return "MATIC-USDT"

    def __call__(self):
        return "MATIC-USDT"


MATIC_USDT = MATIC_USDT()
"""
    name: MATIC-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MCO2_USD(NamedTuple):
    """
        name: MCO2-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MCO2-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MCO2-USD"

    def __str__(self):
        return "MCO2-USD"

    def __call__(self):
        return "MCO2-USD"


MCO2_USD = MCO2_USD()
"""
    name: MCO2-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MCO2_USDT(NamedTuple):
    """
        name: MCO2-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MCO2-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MCO2-USDT"

    def __str__(self):
        return "MCO2-USDT"

    def __call__(self):
        return "MCO2-USDT"


MCO2_USDT = MCO2_USDT()
"""
    name: MCO2-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MDT_USD(NamedTuple):
    """
        name: MDT-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MDT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MDT-USD"

    def __str__(self):
        return "MDT-USD"

    def __call__(self):
        return "MDT-USD"


MDT_USD = MDT_USD()
"""
    name: MDT-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MDT_USDT(NamedTuple):
    """
        name: MDT-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MDT-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MDT-USDT"

    def __str__(self):
        return "MDT-USDT"

    def __call__(self):
        return "MDT-USDT"


MDT_USDT = MDT_USDT()
"""
    name: MDT-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MEDIA_USD(NamedTuple):
    """
        name: MEDIA-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MEDIA-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MEDIA-USD"

    def __str__(self):
        return "MEDIA-USD"

    def __call__(self):
        return "MEDIA-USD"


MEDIA_USD = MEDIA_USD()
"""
    name: MEDIA-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MEDIA_USDT(NamedTuple):
    """
        name: MEDIA-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MEDIA-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MEDIA-USDT"

    def __str__(self):
        return "MEDIA-USDT"

    def __call__(self):
        return "MEDIA-USDT"


MEDIA_USDT = MEDIA_USDT()
"""
    name: MEDIA-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class METIS_USD(NamedTuple):
    """
        name: METIS-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "METIS-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "METIS-USD"

    def __str__(self):
        return "METIS-USD"

    def __call__(self):
        return "METIS-USD"


METIS_USD = METIS_USD()
"""
    name: METIS-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class METIS_USDT(NamedTuple):
    """
        name: METIS-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "METIS-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "METIS-USDT"

    def __str__(self):
        return "METIS-USDT"

    def __call__(self):
        return "METIS-USDT"


METIS_USDT = METIS_USDT()
"""
    name: METIS-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MINA_EUR(NamedTuple):
    """
        name: MINA-EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MINA-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MINA-EUR"

    def __str__(self):
        return "MINA-EUR"

    def __call__(self):
        return "MINA-EUR"


MINA_EUR = MINA_EUR()
"""
    name: MINA-EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MINA_USD(NamedTuple):
    """
        name: MINA-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MINA-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MINA-USD"

    def __str__(self):
        return "MINA-USD"

    def __call__(self):
        return "MINA-USD"


MINA_USD = MINA_USD()
"""
    name: MINA-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MINA_USDT(NamedTuple):
    """
        name: MINA-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MINA-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MINA-USDT"

    def __str__(self):
        return "MINA-USDT"

    def __call__(self):
        return "MINA-USDT"


MINA_USDT = MINA_USDT()
"""
    name: MINA-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MIR_BTC(NamedTuple):
    """
        name: MIR-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "MIR-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MIR-BTC"

    def __str__(self):
        return "MIR-BTC"

    def __call__(self):
        return "MIR-BTC"


MIR_BTC = MIR_BTC()
"""
    name: MIR-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class MIR_EUR(NamedTuple):
    """
        name: MIR-EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "MIR-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MIR-EUR"

    def __str__(self):
        return "MIR-EUR"

    def __call__(self):
        return "MIR-EUR"


MIR_EUR = MIR_EUR()
"""
    name: MIR-EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class MIR_GBP(NamedTuple):
    """
        name: MIR-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "MIR-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MIR-GBP"

    def __str__(self):
        return "MIR-GBP"

    def __call__(self):
        return "MIR-GBP"


MIR_GBP = MIR_GBP()
"""
    name: MIR-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class MIR_USD(NamedTuple):
    """
        name: MIR-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MIR-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MIR-USD"

    def __str__(self):
        return "MIR-USD"

    def __call__(self):
        return "MIR-USD"


MIR_USD = MIR_USD()
"""
    name: MIR-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MKR_BTC(NamedTuple):
    """
        name: MKR-BTC
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00001
        maximum_order_size: None
        margin: False
    """
    name: str = "MKR-BTC"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MKR-BTC"

    def __str__(self):
        return "MKR-BTC"

    def __call__(self):
        return "MKR-BTC"


MKR_BTC = MKR_BTC()
"""
    name: MKR-BTC
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00001
    maximum_order_size: None
    margin: False
"""


class MKR_USD(NamedTuple):
    """
        name: MKR-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MKR-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MKR-USD"

    def __str__(self):
        return "MKR-USD"

    def __call__(self):
        return "MKR-USD"


MKR_USD = MKR_USD()
"""
    name: MKR-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MLN_USD(NamedTuple):
    """
        name: MLN-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MLN-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MLN-USD"

    def __str__(self):
        return "MLN-USD"

    def __call__(self):
        return "MLN-USD"


MLN_USD = MLN_USD()
"""
    name: MLN-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MNDE_USD(NamedTuple):
    """
        name: MNDE-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MNDE-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MNDE-USD"

    def __str__(self):
        return "MNDE-USD"

    def __call__(self):
        return "MNDE-USD"


MNDE_USD = MNDE_USD()
"""
    name: MNDE-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MONA_USD(NamedTuple):
    """
        name: MONA-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MONA-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MONA-USD"

    def __str__(self):
        return "MONA-USD"

    def __call__(self):
        return "MONA-USD"


MONA_USD = MONA_USD()
"""
    name: MONA-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MPL_USD(NamedTuple):
    """
        name: MPL-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MPL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MPL-USD"

    def __str__(self):
        return "MPL-USD"

    def __call__(self):
        return "MPL-USD"


MPL_USD = MPL_USD()
"""
    name: MPL-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MSOL_USD(NamedTuple):
    """
        name: MSOL-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MSOL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MSOL-USD"

    def __str__(self):
        return "MSOL-USD"

    def __call__(self):
        return "MSOL-USD"


MSOL_USD = MSOL_USD()
"""
    name: MSOL-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MTL_USD(NamedTuple):
    """
        name: MTL-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MTL-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MTL-USD"

    def __str__(self):
        return "MTL-USD"

    def __call__(self):
        return "MTL-USD"


MTL_USD = MTL_USD()
"""
    name: MTL-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MUSD_USD(NamedTuple):
    """
        name: MUSD-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MUSD-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MUSD-USD"

    def __str__(self):
        return "MUSD-USD"

    def __call__(self):
        return "MUSD-USD"


MUSD_USD = MUSD_USD()
"""
    name: MUSD-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MUSE_USD(NamedTuple):
    """
        name: MUSE-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MUSE-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MUSE-USD"

    def __str__(self):
        return "MUSE-USD"

    def __call__(self):
        return "MUSE-USD"


MUSE_USD = MUSE_USD()
"""
    name: MUSE-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class MXC_USD(NamedTuple):
    """
        name: MXC-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "MXC-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MXC-USD"

    def __str__(self):
        return "MXC-USD"

    def __call__(self):
        return "MXC-USD"


MXC_USD = MXC_USD()
"""
    name: MXC-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NCT_EUR(NamedTuple):
    """
        name: NCT-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NCT-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NCT-EUR"

    def __str__(self):
        return "NCT-EUR"

    def __call__(self):
        return "NCT-EUR"


NCT_EUR = NCT_EUR()
"""
    name: NCT-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NCT_USD(NamedTuple):
    """
        name: NCT-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NCT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NCT-USD"

    def __str__(self):
        return "NCT-USD"

    def __call__(self):
        return "NCT-USD"


NCT_USD = NCT_USD()
"""
    name: NCT-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NCT_USDT(NamedTuple):
    """
        name: NCT-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NCT-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NCT-USDT"

    def __str__(self):
        return "NCT-USDT"

    def __call__(self):
        return "NCT-USDT"


NCT_USDT = NCT_USDT()
"""
    name: NCT-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NEAR_USD(NamedTuple):
    """
        name: NEAR-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NEAR-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NEAR-USD"

    def __str__(self):
        return "NEAR-USD"

    def __call__(self):
        return "NEAR-USD"


NEAR_USD = NEAR_USD()
"""
    name: NEAR-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NEAR_USDT(NamedTuple):
    """
        name: NEAR-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NEAR-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NEAR-USDT"

    def __str__(self):
        return "NEAR-USDT"

    def __call__(self):
        return "NEAR-USDT"


NEAR_USDT = NEAR_USDT()
"""
    name: NEAR-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NEST_USD(NamedTuple):
    """
        name: NEST-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NEST-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NEST-USD"

    def __str__(self):
        return "NEST-USD"

    def __call__(self):
        return "NEST-USD"


NEST_USD = NEST_USD()
"""
    name: NEST-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NEST_USDT(NamedTuple):
    """
        name: NEST-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NEST-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NEST-USDT"

    def __str__(self):
        return "NEST-USDT"

    def __call__(self):
        return "NEST-USDT"


NEST_USDT = NEST_USDT()
"""
    name: NEST-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NKN_BTC(NamedTuple):
    """
        name: NKN-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "NKN-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NKN-BTC"

    def __str__(self):
        return "NKN-BTC"

    def __call__(self):
        return "NKN-BTC"


NKN_BTC = NKN_BTC()
"""
    name: NKN-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class NKN_EUR(NamedTuple):
    """
        name: NKN-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "NKN-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NKN-EUR"

    def __str__(self):
        return "NKN-EUR"

    def __call__(self):
        return "NKN-EUR"


NKN_EUR = NKN_EUR()
"""
    name: NKN-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class NKN_GBP(NamedTuple):
    """
        name: NKN-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "NKN-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NKN-GBP"

    def __str__(self):
        return "NKN-GBP"

    def __call__(self):
        return "NKN-GBP"


NKN_GBP = NKN_GBP()
"""
    name: NKN-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class NKN_USD(NamedTuple):
    """
        name: NKN-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NKN-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NKN-USD"

    def __str__(self):
        return "NKN-USD"

    def __call__(self):
        return "NKN-USD"


NKN_USD = NKN_USD()
"""
    name: NKN-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NMR_BTC(NamedTuple):
    """
        name: NMR-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "NMR-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NMR-BTC"

    def __str__(self):
        return "NMR-BTC"

    def __call__(self):
        return "NMR-BTC"


NMR_BTC = NMR_BTC()
"""
    name: NMR-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class NMR_EUR(NamedTuple):
    """
        name: NMR-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "NMR-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NMR-EUR"

    def __str__(self):
        return "NMR-EUR"

    def __call__(self):
        return "NMR-EUR"


NMR_EUR = NMR_EUR()
"""
    name: NMR-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class NMR_GBP(NamedTuple):
    """
        name: NMR-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "NMR-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NMR-GBP"

    def __str__(self):
        return "NMR-GBP"

    def __call__(self):
        return "NMR-GBP"


NMR_GBP = NMR_GBP()
"""
    name: NMR-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class NMR_USD(NamedTuple):
    """
        name: NMR-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NMR-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NMR-USD"

    def __str__(self):
        return "NMR-USD"

    def __call__(self):
        return "NMR-USD"


NMR_USD = NMR_USD()
"""
    name: NMR-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class NU_BTC(NamedTuple):
    """
        name: NU-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "NU-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NU-BTC"

    def __str__(self):
        return "NU-BTC"

    def __call__(self):
        return "NU-BTC"


NU_BTC = NU_BTC()
"""
    name: NU-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class NU_EUR(NamedTuple):
    """
        name: NU-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "NU-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NU-EUR"

    def __str__(self):
        return "NU-EUR"

    def __call__(self):
        return "NU-EUR"


NU_EUR = NU_EUR()
"""
    name: NU-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class NU_GBP(NamedTuple):
    """
        name: NU-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "NU-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NU-GBP"

    def __str__(self):
        return "NU-GBP"

    def __call__(self):
        return "NU-GBP"


NU_GBP = NU_GBP()
"""
    name: NU-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class NU_USD(NamedTuple):
    """
        name: NU-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "NU-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NU-USD"

    def __str__(self):
        return "NU-USD"

    def __call__(self):
        return "NU-USD"


NU_USD = NU_USD()
"""
    name: NU-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class OCEAN_USD(NamedTuple):
    """
        name: OCEAN-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "OCEAN-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OCEAN-USD"

    def __str__(self):
        return "OCEAN-USD"

    def __call__(self):
        return "OCEAN-USD"


OCEAN_USD = OCEAN_USD()
"""
    name: OCEAN-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class OGN_BTC(NamedTuple):
    """
        name: OGN-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "OGN-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OGN-BTC"

    def __str__(self):
        return "OGN-BTC"

    def __call__(self):
        return "OGN-BTC"


OGN_BTC = OGN_BTC()
"""
    name: OGN-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class OGN_USD(NamedTuple):
    """
        name: OGN-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "OGN-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OGN-USD"

    def __str__(self):
        return "OGN-USD"

    def __call__(self):
        return "OGN-USD"


OGN_USD = OGN_USD()
"""
    name: OGN-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class OMG_BTC(NamedTuple):
    """
        name: OMG-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "OMG-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMG-BTC"

    def __str__(self):
        return "OMG-BTC"

    def __call__(self):
        return "OMG-BTC"


OMG_BTC = OMG_BTC()
"""
    name: OMG-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class OMG_EUR(NamedTuple):
    """
        name: OMG-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "OMG-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMG-EUR"

    def __str__(self):
        return "OMG-EUR"

    def __call__(self):
        return "OMG-EUR"


OMG_EUR = OMG_EUR()
"""
    name: OMG-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class OMG_GBP(NamedTuple):
    """
        name: OMG-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "OMG-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMG-GBP"

    def __str__(self):
        return "OMG-GBP"

    def __call__(self):
        return "OMG-GBP"


OMG_GBP = OMG_GBP()
"""
    name: OMG-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class OMG_USD(NamedTuple):
    """
        name: OMG-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "OMG-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMG-USD"

    def __str__(self):
        return "OMG-USD"

    def __call__(self):
        return "OMG-USD"


OMG_USD = OMG_USD()
"""
    name: OMG-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class OOKI_USD(NamedTuple):
    """
        name: OOKI-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "OOKI-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OOKI-USD"

    def __str__(self):
        return "OOKI-USD"

    def __call__(self):
        return "OOKI-USD"


OOKI_USD = OOKI_USD()
"""
    name: OOKI-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class OP_USD(NamedTuple):
    """
        name: OP-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "OP-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OP-USD"

    def __str__(self):
        return "OP-USD"

    def __call__(self):
        return "OP-USD"


OP_USD = OP_USD()
"""
    name: OP-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class OP_USDT(NamedTuple):
    """
        name: OP-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "OP-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OP-USDT"

    def __str__(self):
        return "OP-USDT"

    def __call__(self):
        return "OP-USDT"


OP_USDT = OP_USDT()
"""
    name: OP-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ORCA_USD(NamedTuple):
    """
        name: ORCA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ORCA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ORCA-USD"

    def __str__(self):
        return "ORCA-USD"

    def __call__(self):
        return "ORCA-USD"


ORCA_USD = ORCA_USD()
"""
    name: ORCA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ORN_BTC(NamedTuple):
    """
        name: ORN-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ORN-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ORN-BTC"

    def __str__(self):
        return "ORN-BTC"

    def __call__(self):
        return "ORN-BTC"


ORN_BTC = ORN_BTC()
"""
    name: ORN-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ORN_USD(NamedTuple):
    """
        name: ORN-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ORN-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ORN-USD"

    def __str__(self):
        return "ORN-USD"

    def __call__(self):
        return "ORN-USD"


ORN_USD = ORN_USD()
"""
    name: ORN-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ORN_USDT(NamedTuple):
    """
        name: ORN-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ORN-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ORN-USDT"

    def __str__(self):
        return "ORN-USDT"

    def __call__(self):
        return "ORN-USDT"


ORN_USDT = ORN_USDT()
"""
    name: ORN-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class OXT_USD(NamedTuple):
    """
        name: OXT-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "OXT-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OXT-USD"

    def __str__(self):
        return "OXT-USD"

    def __call__(self):
        return "OXT-USD"


OXT_USD = OXT_USD()
"""
    name: OXT-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PAX_USD(NamedTuple):
    """
        name: PAX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PAX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PAX-USD"

    def __str__(self):
        return "PAX-USD"

    def __call__(self):
        return "PAX-USD"


PAX_USD = PAX_USD()
"""
    name: PAX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PAX_USDT(NamedTuple):
    """
        name: PAX-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PAX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PAX-USDT"

    def __str__(self):
        return "PAX-USDT"

    def __call__(self):
        return "PAX-USDT"


PAX_USDT = PAX_USDT()
"""
    name: PAX-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PERP_EUR(NamedTuple):
    """
        name: PERP-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "PERP-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PERP-EUR"

    def __str__(self):
        return "PERP-EUR"

    def __call__(self):
        return "PERP-EUR"


PERP_EUR = PERP_EUR()
"""
    name: PERP-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class PERP_USD(NamedTuple):
    """
        name: PERP-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PERP-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PERP-USD"

    def __str__(self):
        return "PERP-USD"

    def __call__(self):
        return "PERP-USD"


PERP_USD = PERP_USD()
"""
    name: PERP-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PERP_USDT(NamedTuple):
    """
        name: PERP-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PERP-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PERP-USDT"

    def __str__(self):
        return "PERP-USDT"

    def __call__(self):
        return "PERP-USDT"


PERP_USDT = PERP_USDT()
"""
    name: PERP-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PLA_USD(NamedTuple):
    """
        name: PLA-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PLA-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PLA-USD"

    def __str__(self):
        return "PLA-USD"

    def __call__(self):
        return "PLA-USD"


PLA_USD = PLA_USD()
"""
    name: PLA-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PLU_USD(NamedTuple):
    """
        name: PLU-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PLU-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PLU-USD"

    def __str__(self):
        return "PLU-USD"

    def __call__(self):
        return "PLU-USD"


PLU_USD = PLU_USD()
"""
    name: PLU-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PNG_USD(NamedTuple):
    """
        name: PNG-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PNG-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PNG-USD"

    def __str__(self):
        return "PNG-USD"

    def __call__(self):
        return "PNG-USD"


PNG_USD = PNG_USD()
"""
    name: PNG-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class POLS_USD(NamedTuple):
    """
        name: POLS-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "POLS-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLS-USD"

    def __str__(self):
        return "POLS-USD"

    def __call__(self):
        return "POLS-USD"


POLS_USD = POLS_USD()
"""
    name: POLS-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class POLS_USDT(NamedTuple):
    """
        name: POLS-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "POLS-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLS-USDT"

    def __str__(self):
        return "POLS-USDT"

    def __call__(self):
        return "POLS-USDT"


POLS_USDT = POLS_USDT()
"""
    name: POLS-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class POLY_USD(NamedTuple):
    """
        name: POLY-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "POLY-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLY-USD"

    def __str__(self):
        return "POLY-USD"

    def __call__(self):
        return "POLY-USD"


POLY_USD = POLY_USD()
"""
    name: POLY-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class POLY_USDT(NamedTuple):
    """
        name: POLY-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "POLY-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLY-USDT"

    def __str__(self):
        return "POLY-USDT"

    def __call__(self):
        return "POLY-USDT"


POLY_USDT = POLY_USDT()
"""
    name: POLY-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class POND_USD(NamedTuple):
    """
        name: POND-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "POND-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POND-USD"

    def __str__(self):
        return "POND-USD"

    def __call__(self):
        return "POND-USD"


POND_USD = POND_USD()
"""
    name: POND-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class POND_USDT(NamedTuple):
    """
        name: POND-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "POND-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POND-USDT"

    def __str__(self):
        return "POND-USDT"

    def __call__(self):
        return "POND-USDT"


POND_USDT = POND_USDT()
"""
    name: POND-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class POWR_EUR(NamedTuple):
    """
        name: POWR-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "POWR-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POWR-EUR"

    def __str__(self):
        return "POWR-EUR"

    def __call__(self):
        return "POWR-EUR"


POWR_EUR = POWR_EUR()
"""
    name: POWR-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class POWR_USD(NamedTuple):
    """
        name: POWR-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "POWR-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POWR-USD"

    def __str__(self):
        return "POWR-USD"

    def __call__(self):
        return "POWR-USD"


POWR_USD = POWR_USD()
"""
    name: POWR-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class POWR_USDT(NamedTuple):
    """
        name: POWR-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "POWR-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POWR-USDT"

    def __str__(self):
        return "POWR-USDT"

    def __call__(self):
        return "POWR-USDT"


POWR_USDT = POWR_USDT()
"""
    name: POWR-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PRO_USD(NamedTuple):
    """
        name: PRO-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PRO-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PRO-USD"

    def __str__(self):
        return "PRO-USD"

    def __call__(self):
        return "PRO-USD"


PRO_USD = PRO_USD()
"""
    name: PRO-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PRQ_USD(NamedTuple):
    """
        name: PRQ-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PRQ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PRQ-USD"

    def __str__(self):
        return "PRQ-USD"

    def __call__(self):
        return "PRQ-USD"


PRQ_USD = PRQ_USD()
"""
    name: PRQ-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PRQ_USDT(NamedTuple):
    """
        name: PRQ-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PRQ-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PRQ-USDT"

    def __str__(self):
        return "PRQ-USDT"

    def __call__(self):
        return "PRQ-USDT"


PRQ_USDT = PRQ_USDT()
"""
    name: PRQ-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PUNDIX_USD(NamedTuple):
    """
        name: PUNDIX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PUNDIX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PUNDIX-USD"

    def __str__(self):
        return "PUNDIX-USD"

    def __call__(self):
        return "PUNDIX-USD"


PUNDIX_USD = PUNDIX_USD()
"""
    name: PUNDIX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class PYR_USD(NamedTuple):
    """
        name: PYR-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "PYR-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PYR-USD"

    def __str__(self):
        return "PYR-USD"

    def __call__(self):
        return "PYR-USD"


PYR_USD = PYR_USD()
"""
    name: PYR-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class QI_USD(NamedTuple):
    """
        name: QI-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "QI-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QI-USD"

    def __str__(self):
        return "QI-USD"

    def __call__(self):
        return "QI-USD"


QI_USD = QI_USD()
"""
    name: QI-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class QNT_USD(NamedTuple):
    """
        name: QNT-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "QNT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QNT-USD"

    def __str__(self):
        return "QNT-USD"

    def __call__(self):
        return "QNT-USD"


QNT_USD = QNT_USD()
"""
    name: QNT-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class QNT_USDT(NamedTuple):
    """
        name: QNT-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "QNT-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QNT-USDT"

    def __str__(self):
        return "QNT-USDT"

    def __call__(self):
        return "QNT-USDT"


QNT_USDT = QNT_USDT()
"""
    name: QNT-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class QSP_USD(NamedTuple):
    """
        name: QSP-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "QSP-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QSP-USD"

    def __str__(self):
        return "QSP-USD"

    def __call__(self):
        return "QSP-USD"


QSP_USD = QSP_USD()
"""
    name: QSP-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class QSP_USDT(NamedTuple):
    """
        name: QSP-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "QSP-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QSP-USDT"

    def __str__(self):
        return "QSP-USDT"

    def __call__(self):
        return "QSP-USDT"


QSP_USDT = QSP_USDT()
"""
    name: QSP-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class QUICK_USD(NamedTuple):
    """
        name: QUICK-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "QUICK-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QUICK-USD"

    def __str__(self):
        return "QUICK-USD"

    def __call__(self):
        return "QUICK-USD"


QUICK_USD = QUICK_USD()
"""
    name: QUICK-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RAD_BTC(NamedTuple):
    """
        name: RAD-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "RAD-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAD-BTC"

    def __str__(self):
        return "RAD-BTC"

    def __call__(self):
        return "RAD-BTC"


RAD_BTC = RAD_BTC()
"""
    name: RAD-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class RAD_EUR(NamedTuple):
    """
        name: RAD-EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "RAD-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAD-EUR"

    def __str__(self):
        return "RAD-EUR"

    def __call__(self):
        return "RAD-EUR"


RAD_EUR = RAD_EUR()
"""
    name: RAD-EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class RAD_GBP(NamedTuple):
    """
        name: RAD-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "RAD-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAD-GBP"

    def __str__(self):
        return "RAD-GBP"

    def __call__(self):
        return "RAD-GBP"


RAD_GBP = RAD_GBP()
"""
    name: RAD-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class RAD_USD(NamedTuple):
    """
        name: RAD-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RAD-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAD-USD"

    def __str__(self):
        return "RAD-USD"

    def __call__(self):
        return "RAD-USD"


RAD_USD = RAD_USD()
"""
    name: RAD-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RAD_USDT(NamedTuple):
    """
        name: RAD-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RAD-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAD-USDT"

    def __str__(self):
        return "RAD-USDT"

    def __call__(self):
        return "RAD-USDT"


RAD_USDT = RAD_USDT()
"""
    name: RAD-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RAI_USD(NamedTuple):
    """
        name: RAI-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RAI-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAI-USD"

    def __str__(self):
        return "RAI-USD"

    def __call__(self):
        return "RAI-USD"


RAI_USD = RAI_USD()
"""
    name: RAI-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RARE_USD(NamedTuple):
    """
        name: RARE-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RARE-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RARE-USD"

    def __str__(self):
        return "RARE-USD"

    def __call__(self):
        return "RARE-USD"


RARE_USD = RARE_USD()
"""
    name: RARE-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RARI_USD(NamedTuple):
    """
        name: RARI-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RARI-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RARI-USD"

    def __str__(self):
        return "RARI-USD"

    def __call__(self):
        return "RARI-USD"


RARI_USD = RARI_USD()
"""
    name: RARI-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RBN_USD(NamedTuple):
    """
        name: RBN-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RBN-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RBN-USD"

    def __str__(self):
        return "RBN-USD"

    def __call__(self):
        return "RBN-USD"


RBN_USD = RBN_USD()
"""
    name: RBN-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class REN_BTC(NamedTuple):
    """
        name: REN-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "REN-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REN-BTC"

    def __str__(self):
        return "REN-BTC"

    def __call__(self):
        return "REN-BTC"


REN_BTC = REN_BTC()
"""
    name: REN-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class REN_USD(NamedTuple):
    """
        name: REN-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "REN-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REN-USD"

    def __str__(self):
        return "REN-USD"

    def __call__(self):
        return "REN-USD"


REN_USD = REN_USD()
"""
    name: REN-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class REP_BTC(NamedTuple):
    """
        name: REP-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "REP-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REP-BTC"

    def __str__(self):
        return "REP-BTC"

    def __call__(self):
        return "REP-BTC"


REP_BTC = REP_BTC()
"""
    name: REP-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class REP_USD(NamedTuple):
    """
        name: REP-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "REP-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REP-USD"

    def __str__(self):
        return "REP-USD"

    def __call__(self):
        return "REP-USD"


REP_USD = REP_USD()
"""
    name: REP-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class REQ_BTC(NamedTuple):
    """
        name: REQ-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "REQ-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REQ-BTC"

    def __str__(self):
        return "REQ-BTC"

    def __call__(self):
        return "REQ-BTC"


REQ_BTC = REQ_BTC()
"""
    name: REQ-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class REQ_EUR(NamedTuple):
    """
        name: REQ-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "REQ-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REQ-EUR"

    def __str__(self):
        return "REQ-EUR"

    def __call__(self):
        return "REQ-EUR"


REQ_EUR = REQ_EUR()
"""
    name: REQ-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class REQ_GBP(NamedTuple):
    """
        name: REQ-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "REQ-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REQ-GBP"

    def __str__(self):
        return "REQ-GBP"

    def __call__(self):
        return "REQ-GBP"


REQ_GBP = REQ_GBP()
"""
    name: REQ-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class REQ_USD(NamedTuple):
    """
        name: REQ-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "REQ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REQ-USD"

    def __str__(self):
        return "REQ-USD"

    def __call__(self):
        return "REQ-USD"


REQ_USD = REQ_USD()
"""
    name: REQ-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class REQ_USDT(NamedTuple):
    """
        name: REQ-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "REQ-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REQ-USDT"

    def __str__(self):
        return "REQ-USDT"

    def __call__(self):
        return "REQ-USDT"


REQ_USDT = REQ_USDT()
"""
    name: REQ-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RGT_USD(NamedTuple):
    """
        name: RGT-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RGT-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RGT-USD"

    def __str__(self):
        return "RGT-USD"

    def __call__(self):
        return "RGT-USD"


RGT_USD = RGT_USD()
"""
    name: RGT-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RLC_BTC(NamedTuple):
    """
        name: RLC-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "RLC-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RLC-BTC"

    def __str__(self):
        return "RLC-BTC"

    def __call__(self):
        return "RLC-BTC"


RLC_BTC = RLC_BTC()
"""
    name: RLC-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class RLC_USD(NamedTuple):
    """
        name: RLC-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RLC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RLC-USD"

    def __str__(self):
        return "RLC-USD"

    def __call__(self):
        return "RLC-USD"


RLC_USD = RLC_USD()
"""
    name: RLC-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RLY_EUR(NamedTuple):
    """
        name: RLY-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "RLY-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RLY-EUR"

    def __str__(self):
        return "RLY-EUR"

    def __call__(self):
        return "RLY-EUR"


RLY_EUR = RLY_EUR()
"""
    name: RLY-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class RLY_GBP(NamedTuple):
    """
        name: RLY-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "RLY-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RLY-GBP"

    def __str__(self):
        return "RLY-GBP"

    def __call__(self):
        return "RLY-GBP"


RLY_GBP = RLY_GBP()
"""
    name: RLY-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class RLY_USD(NamedTuple):
    """
        name: RLY-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RLY-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RLY-USD"

    def __str__(self):
        return "RLY-USD"

    def __call__(self):
        return "RLY-USD"


RLY_USD = RLY_USD()
"""
    name: RLY-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RLY_USDT(NamedTuple):
    """
        name: RLY-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RLY-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RLY-USDT"

    def __str__(self):
        return "RLY-USDT"

    def __call__(self):
        return "RLY-USDT"


RLY_USDT = RLY_USDT()
"""
    name: RLY-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RNDR_EUR(NamedTuple):
    """
        name: RNDR-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RNDR-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RNDR-EUR"

    def __str__(self):
        return "RNDR-EUR"

    def __call__(self):
        return "RNDR-EUR"


RNDR_EUR = RNDR_EUR()
"""
    name: RNDR-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RNDR_USD(NamedTuple):
    """
        name: RNDR-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RNDR-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RNDR-USD"

    def __str__(self):
        return "RNDR-USD"

    def __call__(self):
        return "RNDR-USD"


RNDR_USD = RNDR_USD()
"""
    name: RNDR-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RNDR_USDT(NamedTuple):
    """
        name: RNDR-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RNDR-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RNDR-USDT"

    def __str__(self):
        return "RNDR-USDT"

    def __call__(self):
        return "RNDR-USDT"


RNDR_USDT = RNDR_USDT()
"""
    name: RNDR-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ROSE_USD(NamedTuple):
    """
        name: ROSE-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ROSE-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ROSE-USD"

    def __str__(self):
        return "ROSE-USD"

    def __call__(self):
        return "ROSE-USD"


ROSE_USD = ROSE_USD()
"""
    name: ROSE-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ROSE_USDT(NamedTuple):
    """
        name: ROSE-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ROSE-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ROSE-USDT"

    def __str__(self):
        return "ROSE-USDT"

    def __call__(self):
        return "ROSE-USDT"


ROSE_USDT = ROSE_USDT()
"""
    name: ROSE-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class RPL_USD(NamedTuple):
    """
        name: RPL-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "RPL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RPL-USD"

    def __str__(self):
        return "RPL-USD"

    def __call__(self):
        return "RPL-USD"


RPL_USD = RPL_USD()
"""
    name: RPL-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SAND_USD(NamedTuple):
    """
        name: SAND-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SAND-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SAND-USD"

    def __str__(self):
        return "SAND-USD"

    def __call__(self):
        return "SAND-USD"


SAND_USD = SAND_USD()
"""
    name: SAND-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SAND_USDT(NamedTuple):
    """
        name: SAND-USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SAND-USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SAND-USDT"

    def __str__(self):
        return "SAND-USDT"

    def __call__(self):
        return "SAND-USDT"


SAND_USDT = SAND_USDT()
"""
    name: SAND-USDT
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SHIB_EUR(NamedTuple):
    """
        name: SHIB-EUR
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "SHIB-EUR"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHIB-EUR"

    def __str__(self):
        return "SHIB-EUR"

    def __call__(self):
        return "SHIB-EUR"


SHIB_EUR = SHIB_EUR()
"""
    name: SHIB-EUR
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class SHIB_GBP(NamedTuple):
    """
        name: SHIB-GBP
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "SHIB-GBP"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHIB-GBP"

    def __str__(self):
        return "SHIB-GBP"

    def __call__(self):
        return "SHIB-GBP"


SHIB_GBP = SHIB_GBP()
"""
    name: SHIB-GBP
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class SHIB_USD(NamedTuple):
    """
        name: SHIB-USD
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SHIB-USD"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHIB-USD"

    def __str__(self):
        return "SHIB-USD"

    def __call__(self):
        return "SHIB-USD"


SHIB_USD = SHIB_USD()
"""
    name: SHIB-USD
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SHIB_USDT(NamedTuple):
    """
        name: SHIB-USDT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SHIB-USDT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHIB-USDT"

    def __str__(self):
        return "SHIB-USDT"

    def __call__(self):
        return "SHIB-USDT"


SHIB_USDT = SHIB_USDT()
"""
    name: SHIB-USDT
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SHPING_EUR(NamedTuple):
    """
        name: SHPING-EUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SHPING-EUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHPING-EUR"

    def __str__(self):
        return "SHPING-EUR"

    def __call__(self):
        return "SHPING-EUR"


SHPING_EUR = SHPING_EUR()
"""
    name: SHPING-EUR
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SHPING_USD(NamedTuple):
    """
        name: SHPING-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SHPING-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHPING-USD"

    def __str__(self):
        return "SHPING-USD"

    def __call__(self):
        return "SHPING-USD"


SHPING_USD = SHPING_USD()
"""
    name: SHPING-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SHPING_USDT(NamedTuple):
    """
        name: SHPING-USDT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SHPING-USDT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHPING-USDT"

    def __str__(self):
        return "SHPING-USDT"

    def __call__(self):
        return "SHPING-USDT"


SHPING_USDT = SHPING_USDT()
"""
    name: SHPING-USDT
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SKL_BTC(NamedTuple):
    """
        name: SKL-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "SKL-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SKL-BTC"

    def __str__(self):
        return "SKL-BTC"

    def __call__(self):
        return "SKL-BTC"


SKL_BTC = SKL_BTC()
"""
    name: SKL-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class SKL_EUR(NamedTuple):
    """
        name: SKL-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "SKL-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SKL-EUR"

    def __str__(self):
        return "SKL-EUR"

    def __call__(self):
        return "SKL-EUR"


SKL_EUR = SKL_EUR()
"""
    name: SKL-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class SKL_GBP(NamedTuple):
    """
        name: SKL-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "SKL-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SKL-GBP"

    def __str__(self):
        return "SKL-GBP"

    def __call__(self):
        return "SKL-GBP"


SKL_GBP = SKL_GBP()
"""
    name: SKL-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class SKL_USD(NamedTuple):
    """
        name: SKL-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SKL-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SKL-USD"

    def __str__(self):
        return "SKL-USD"

    def __call__(self):
        return "SKL-USD"


SKL_USD = SKL_USD()
"""
    name: SKL-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SNT_USD(NamedTuple):
    """
        name: SNT-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SNT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNT-USD"

    def __str__(self):
        return "SNT-USD"

    def __call__(self):
        return "SNT-USD"


SNT_USD = SNT_USD()
"""
    name: SNT-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SNX_BTC(NamedTuple):
    """
        name: SNX-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "SNX-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNX-BTC"

    def __str__(self):
        return "SNX-BTC"

    def __call__(self):
        return "SNX-BTC"


SNX_BTC = SNX_BTC()
"""
    name: SNX-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class SNX_EUR(NamedTuple):
    """
        name: SNX-EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "SNX-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNX-EUR"

    def __str__(self):
        return "SNX-EUR"

    def __call__(self):
        return "SNX-EUR"


SNX_EUR = SNX_EUR()
"""
    name: SNX-EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class SNX_GBP(NamedTuple):
    """
        name: SNX-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "SNX-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNX-GBP"

    def __str__(self):
        return "SNX-GBP"

    def __call__(self):
        return "SNX-GBP"


SNX_GBP = SNX_GBP()
"""
    name: SNX-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class SNX_USD(NamedTuple):
    """
        name: SNX-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SNX-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNX-USD"

    def __str__(self):
        return "SNX-USD"

    def __call__(self):
        return "SNX-USD"


SNX_USD = SNX_USD()
"""
    name: SNX-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SOL_BTC(NamedTuple):
    """
        name: SOL-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "SOL-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOL-BTC"

    def __str__(self):
        return "SOL-BTC"

    def __call__(self):
        return "SOL-BTC"


SOL_BTC = SOL_BTC()
"""
    name: SOL-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class SOL_ETH(NamedTuple):
    """
        name: SOL-ETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00022
        maximum_order_size: None
        margin: False
    """
    name: str = "SOL-ETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOL-ETH"

    def __str__(self):
        return "SOL-ETH"

    def __call__(self):
        return "SOL-ETH"


SOL_ETH = SOL_ETH()
"""
    name: SOL-ETH
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00022
    maximum_order_size: None
    margin: False
"""


class SOL_EUR(NamedTuple):
    """
        name: SOL-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "SOL-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOL-EUR"

    def __str__(self):
        return "SOL-EUR"

    def __call__(self):
        return "SOL-EUR"


SOL_EUR = SOL_EUR()
"""
    name: SOL-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class SOL_GBP(NamedTuple):
    """
        name: SOL-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "SOL-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOL-GBP"

    def __str__(self):
        return "SOL-GBP"

    def __call__(self):
        return "SOL-GBP"


SOL_GBP = SOL_GBP()
"""
    name: SOL-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class SOL_USD(NamedTuple):
    """
        name: SOL-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SOL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOL-USD"

    def __str__(self):
        return "SOL-USD"

    def __call__(self):
        return "SOL-USD"


SOL_USD = SOL_USD()
"""
    name: SOL-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SOL_USDT(NamedTuple):
    """
        name: SOL-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SOL-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOL-USDT"

    def __str__(self):
        return "SOL-USDT"

    def __call__(self):
        return "SOL-USDT"


SOL_USDT = SOL_USDT()
"""
    name: SOL-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SPELL_USD(NamedTuple):
    """
        name: SPELL-USD
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SPELL-USD"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SPELL-USD"

    def __str__(self):
        return "SPELL-USD"

    def __call__(self):
        return "SPELL-USD"


SPELL_USD = SPELL_USD()
"""
    name: SPELL-USD
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SPELL_USDT(NamedTuple):
    """
        name: SPELL-USDT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SPELL-USDT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SPELL-USDT"

    def __str__(self):
        return "SPELL-USDT"

    def __call__(self):
        return "SPELL-USDT"


SPELL_USDT = SPELL_USDT()
"""
    name: SPELL-USDT
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class STG_USD(NamedTuple):
    """
        name: STG-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "STG-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STG-USD"

    def __str__(self):
        return "STG-USD"

    def __call__(self):
        return "STG-USD"


STG_USD = STG_USD()
"""
    name: STG-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class STG_USDT(NamedTuple):
    """
        name: STG-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "STG-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STG-USDT"

    def __str__(self):
        return "STG-USDT"

    def __call__(self):
        return "STG-USDT"


STG_USDT = STG_USDT()
"""
    name: STG-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class STORJ_BTC(NamedTuple):
    """
        name: STORJ-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "STORJ-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STORJ-BTC"

    def __str__(self):
        return "STORJ-BTC"

    def __call__(self):
        return "STORJ-BTC"


STORJ_BTC = STORJ_BTC()
"""
    name: STORJ-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class STORJ_USD(NamedTuple):
    """
        name: STORJ-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "STORJ-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STORJ-USD"

    def __str__(self):
        return "STORJ-USD"

    def __call__(self):
        return "STORJ-USD"


STORJ_USD = STORJ_USD()
"""
    name: STORJ-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class STX_USD(NamedTuple):
    """
        name: STX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "STX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STX-USD"

    def __str__(self):
        return "STX-USD"

    def __call__(self):
        return "STX-USD"


STX_USD = STX_USD()
"""
    name: STX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class STX_USDT(NamedTuple):
    """
        name: STX-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "STX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STX-USDT"

    def __str__(self):
        return "STX-USDT"

    def __call__(self):
        return "STX-USDT"


STX_USDT = STX_USDT()
"""
    name: STX-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SUKU_EUR(NamedTuple):
    """
        name: SUKU-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "SUKU-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUKU-EUR"

    def __str__(self):
        return "SUKU-EUR"

    def __call__(self):
        return "SUKU-EUR"


SUKU_EUR = SUKU_EUR()
"""
    name: SUKU-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class SUKU_USD(NamedTuple):
    """
        name: SUKU-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SUKU-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUKU-USD"

    def __str__(self):
        return "SUKU-USD"

    def __call__(self):
        return "SUKU-USD"


SUKU_USD = SUKU_USD()
"""
    name: SUKU-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SUKU_USDT(NamedTuple):
    """
        name: SUKU-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SUKU-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUKU-USDT"

    def __str__(self):
        return "SUKU-USDT"

    def __call__(self):
        return "SUKU-USDT"


SUKU_USDT = SUKU_USDT()
"""
    name: SUKU-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SUPER_USD(NamedTuple):
    """
        name: SUPER-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SUPER-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUPER-USD"

    def __str__(self):
        return "SUPER-USD"

    def __call__(self):
        return "SUPER-USD"


SUPER_USD = SUPER_USD()
"""
    name: SUPER-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SUPER_USDT(NamedTuple):
    """
        name: SUPER-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SUPER-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUPER-USDT"

    def __str__(self):
        return "SUPER-USDT"

    def __call__(self):
        return "SUPER-USDT"


SUPER_USDT = SUPER_USDT()
"""
    name: SUPER-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SUSHI_BTC(NamedTuple):
    """
        name: SUSHI-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHI-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHI-BTC"

    def __str__(self):
        return "SUSHI-BTC"

    def __call__(self):
        return "SUSHI-BTC"


SUSHI_BTC = SUSHI_BTC()
"""
    name: SUSHI-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class SUSHI_ETH(NamedTuple):
    """
        name: SUSHI-ETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00022
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHI-ETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00022
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHI-ETH"

    def __str__(self):
        return "SUSHI-ETH"

    def __call__(self):
        return "SUSHI-ETH"


SUSHI_ETH = SUSHI_ETH()
"""
    name: SUSHI-ETH
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00022
    maximum_order_size: None
    margin: False
"""


class SUSHI_EUR(NamedTuple):
    """
        name: SUSHI-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHI-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHI-EUR"

    def __str__(self):
        return "SUSHI-EUR"

    def __call__(self):
        return "SUSHI-EUR"


SUSHI_EUR = SUSHI_EUR()
"""
    name: SUSHI-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class SUSHI_GBP(NamedTuple):
    """
        name: SUSHI-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHI-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHI-GBP"

    def __str__(self):
        return "SUSHI-GBP"

    def __call__(self):
        return "SUSHI-GBP"


SUSHI_GBP = SUSHI_GBP()
"""
    name: SUSHI-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class SUSHI_USD(NamedTuple):
    """
        name: SUSHI-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHI-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHI-USD"

    def __str__(self):
        return "SUSHI-USD"

    def __call__(self):
        return "SUSHI-USD"


SUSHI_USD = SUSHI_USD()
"""
    name: SUSHI-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SWFTC_USD(NamedTuple):
    """
        name: SWFTC-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SWFTC-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SWFTC-USD"

    def __str__(self):
        return "SWFTC-USD"

    def __call__(self):
        return "SWFTC-USD"


SWFTC_USD = SWFTC_USD()
"""
    name: SWFTC-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SYLO_USD(NamedTuple):
    """
        name: SYLO-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SYLO-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SYLO-USD"

    def __str__(self):
        return "SYLO-USD"

    def __call__(self):
        return "SYLO-USD"


SYLO_USD = SYLO_USD()
"""
    name: SYLO-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SYLO_USDT(NamedTuple):
    """
        name: SYLO-USDT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SYLO-USDT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SYLO-USDT"

    def __str__(self):
        return "SYLO-USDT"

    def __call__(self):
        return "SYLO-USDT"


SYLO_USDT = SYLO_USDT()
"""
    name: SYLO-USDT
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class SYN_USD(NamedTuple):
    """
        name: SYN-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "SYN-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SYN-USD"

    def __str__(self):
        return "SYN-USD"

    def __call__(self):
        return "SYN-USD"


SYN_USD = SYN_USD()
"""
    name: SYN-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class TIME_USD(NamedTuple):
    """
        name: TIME-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "TIME-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TIME-USD"

    def __str__(self):
        return "TIME-USD"

    def __call__(self):
        return "TIME-USD"


TIME_USD = TIME_USD()
"""
    name: TIME-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class TIME_USDT(NamedTuple):
    """
        name: TIME-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "TIME-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TIME-USDT"

    def __str__(self):
        return "TIME-USDT"

    def __call__(self):
        return "TIME-USDT"


TIME_USDT = TIME_USDT()
"""
    name: TIME-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class TONE_USD(NamedTuple):
    """
        name: TONE-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "TONE-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TONE-USD"

    def __str__(self):
        return "TONE-USD"

    def __call__(self):
        return "TONE-USD"


TONE_USD = TONE_USD()
"""
    name: TONE-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class TRAC_EUR(NamedTuple):
    """
        name: TRAC-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "TRAC-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRAC-EUR"

    def __str__(self):
        return "TRAC-EUR"

    def __call__(self):
        return "TRAC-EUR"


TRAC_EUR = TRAC_EUR()
"""
    name: TRAC-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class TRAC_USD(NamedTuple):
    """
        name: TRAC-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "TRAC-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRAC-USD"

    def __str__(self):
        return "TRAC-USD"

    def __call__(self):
        return "TRAC-USD"


TRAC_USD = TRAC_USD()
"""
    name: TRAC-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class TRAC_USDT(NamedTuple):
    """
        name: TRAC-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "TRAC-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRAC-USDT"

    def __str__(self):
        return "TRAC-USDT"

    def __call__(self):
        return "TRAC-USDT"


TRAC_USDT = TRAC_USDT()
"""
    name: TRAC-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class TRB_BTC(NamedTuple):
    """
        name: TRB-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "TRB-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRB-BTC"

    def __str__(self):
        return "TRB-BTC"

    def __call__(self):
        return "TRB-BTC"


TRB_BTC = TRB_BTC()
"""
    name: TRB-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class TRB_USD(NamedTuple):
    """
        name: TRB-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "TRB-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRB-USD"

    def __str__(self):
        return "TRB-USD"

    def __call__(self):
        return "TRB-USD"


TRB_USD = TRB_USD()
"""
    name: TRB-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class TRIBE_USD(NamedTuple):
    """
        name: TRIBE-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "TRIBE-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRIBE-USD"

    def __str__(self):
        return "TRIBE-USD"

    def __call__(self):
        return "TRIBE-USD"


TRIBE_USD = TRIBE_USD()
"""
    name: TRIBE-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class TRU_BTC(NamedTuple):
    """
        name: TRU-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "TRU-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRU-BTC"

    def __str__(self):
        return "TRU-BTC"

    def __call__(self):
        return "TRU-BTC"


TRU_BTC = TRU_BTC()
"""
    name: TRU-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class TRU_EUR(NamedTuple):
    """
        name: TRU-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "TRU-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRU-EUR"

    def __str__(self):
        return "TRU-EUR"

    def __call__(self):
        return "TRU-EUR"


TRU_EUR = TRU_EUR()
"""
    name: TRU-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class TRU_USD(NamedTuple):
    """
        name: TRU-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "TRU-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRU-USD"

    def __str__(self):
        return "TRU-USD"

    def __call__(self):
        return "TRU-USD"


TRU_USD = TRU_USD()
"""
    name: TRU-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class TRU_USDT(NamedTuple):
    """
        name: TRU-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "TRU-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRU-USDT"

    def __str__(self):
        return "TRU-USDT"

    def __call__(self):
        return "TRU-USDT"


TRU_USDT = TRU_USDT()
"""
    name: TRU-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class UMA_BTC(NamedTuple):
    """
        name: UMA-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "UMA-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UMA-BTC"

    def __str__(self):
        return "UMA-BTC"

    def __call__(self):
        return "UMA-BTC"


UMA_BTC = UMA_BTC()
"""
    name: UMA-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class UMA_EUR(NamedTuple):
    """
        name: UMA-EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "UMA-EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UMA-EUR"

    def __str__(self):
        return "UMA-EUR"

    def __call__(self):
        return "UMA-EUR"


UMA_EUR = UMA_EUR()
"""
    name: UMA-EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class UMA_GBP(NamedTuple):
    """
        name: UMA-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "UMA-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UMA-GBP"

    def __str__(self):
        return "UMA-GBP"

    def __call__(self):
        return "UMA-GBP"


UMA_GBP = UMA_GBP()
"""
    name: UMA-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class UMA_USD(NamedTuple):
    """
        name: UMA-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "UMA-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UMA-USD"

    def __str__(self):
        return "UMA-USD"

    def __call__(self):
        return "UMA-USD"


UMA_USD = UMA_USD()
"""
    name: UMA-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class UNFI_USD(NamedTuple):
    """
        name: UNFI-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "UNFI-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNFI-USD"

    def __str__(self):
        return "UNFI-USD"

    def __call__(self):
        return "UNFI-USD"


UNFI_USD = UNFI_USD()
"""
    name: UNFI-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class UNI_BTC(NamedTuple):
    """
        name: UNI-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "UNI-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNI-BTC"

    def __str__(self):
        return "UNI-BTC"

    def __call__(self):
        return "UNI-BTC"


UNI_BTC = UNI_BTC()
"""
    name: UNI-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class UNI_EUR(NamedTuple):
    """
        name: UNI-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "UNI-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNI-EUR"

    def __str__(self):
        return "UNI-EUR"

    def __call__(self):
        return "UNI-EUR"


UNI_EUR = UNI_EUR()
"""
    name: UNI-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class UNI_GBP(NamedTuple):
    """
        name: UNI-GBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "UNI-GBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNI-GBP"

    def __str__(self):
        return "UNI-GBP"

    def __call__(self):
        return "UNI-GBP"


UNI_GBP = UNI_GBP()
"""
    name: UNI-GBP
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class UNI_USD(NamedTuple):
    """
        name: UNI-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "UNI-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNI-USD"

    def __str__(self):
        return "UNI-USD"

    def __call__(self):
        return "UNI-USD"


UNI_USD = UNI_USD()
"""
    name: UNI-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class UPI_USD(NamedTuple):
    """
        name: UPI-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "UPI-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UPI-USD"

    def __str__(self):
        return "UPI-USD"

    def __call__(self):
        return "UPI-USD"


UPI_USD = UPI_USD()
"""
    name: UPI-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class UPI_USDT(NamedTuple):
    """
        name: UPI-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "UPI-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UPI-USDT"

    def __str__(self):
        return "UPI-USDT"

    def __call__(self):
        return "UPI-USDT"


UPI_USDT = UPI_USDT()
"""
    name: UPI-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class USDC_EUR(NamedTuple):
    """
        name: USDC-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "USDC-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDC-EUR"

    def __str__(self):
        return "USDC-EUR"

    def __call__(self):
        return "USDC-EUR"


USDC_EUR = USDC_EUR()
"""
    name: USDC-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class USDC_GBP(NamedTuple):
    """
        name: USDC-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "USDC-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDC-GBP"

    def __str__(self):
        return "USDC-GBP"

    def __call__(self):
        return "USDC-GBP"


USDC_GBP = USDC_GBP()
"""
    name: USDC-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class USDT_EUR(NamedTuple):
    """
        name: USDT-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "USDT-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDT-EUR"

    def __str__(self):
        return "USDT-EUR"

    def __call__(self):
        return "USDT-EUR"


USDT_EUR = USDT_EUR()
"""
    name: USDT-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class USDT_GBP(NamedTuple):
    """
        name: USDT-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "USDT-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDT-GBP"

    def __str__(self):
        return "USDT-GBP"

    def __call__(self):
        return "USDT-GBP"


USDT_GBP = USDT_GBP()
"""
    name: USDT-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class USDT_USD(NamedTuple):
    """
        name: USDT-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "USDT-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDT-USD"

    def __str__(self):
        return "USDT-USD"

    def __call__(self):
        return "USDT-USD"


USDT_USD = USDT_USD()
"""
    name: USDT-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class USDT_USDC(NamedTuple):
    """
        name: USDT-USDC
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "USDT-USDC"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDT-USDC"

    def __str__(self):
        return "USDT-USDC"

    def __call__(self):
        return "USDT-USDC"


USDT_USDC = USDT_USDC()
"""
    name: USDT-USDC
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class UST_EUR(NamedTuple):
    """
        name: UST-EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "UST-EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UST-EUR"

    def __str__(self):
        return "UST-EUR"

    def __call__(self):
        return "UST-EUR"


UST_EUR = UST_EUR()
"""
    name: UST-EUR
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class UST_USD(NamedTuple):
    """
        name: UST-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "UST-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UST-USD"

    def __str__(self):
        return "UST-USD"

    def __call__(self):
        return "UST-USD"


UST_USD = UST_USD()
"""
    name: UST-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class UST_USDT(NamedTuple):
    """
        name: UST-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "UST-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UST-USDT"

    def __str__(self):
        return "UST-USDT"

    def __call__(self):
        return "UST-USDT"


UST_USDT = UST_USDT()
"""
    name: UST-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class VGX_EUR(NamedTuple):
    """
        name: VGX-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "VGX-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "VGX-EUR"

    def __str__(self):
        return "VGX-EUR"

    def __call__(self):
        return "VGX-EUR"


VGX_EUR = VGX_EUR()
"""
    name: VGX-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class VGX_USD(NamedTuple):
    """
        name: VGX-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "VGX-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "VGX-USD"

    def __str__(self):
        return "VGX-USD"

    def __call__(self):
        return "VGX-USD"


VGX_USD = VGX_USD()
"""
    name: VGX-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class VGX_USDT(NamedTuple):
    """
        name: VGX-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "VGX-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "VGX-USDT"

    def __str__(self):
        return "VGX-USDT"

    def __call__(self):
        return "VGX-USDT"


VGX_USDT = VGX_USDT()
"""
    name: VGX-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class WAMPL_USD(NamedTuple):
    """
        name: WAMPL-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "WAMPL-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WAMPL-USD"

    def __str__(self):
        return "WAMPL-USD"

    def __call__(self):
        return "WAMPL-USD"


WAMPL_USD = WAMPL_USD()
"""
    name: WAMPL-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class WAMPL_USDT(NamedTuple):
    """
        name: WAMPL-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "WAMPL-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WAMPL-USDT"

    def __str__(self):
        return "WAMPL-USDT"

    def __call__(self):
        return "WAMPL-USDT"


WAMPL_USDT = WAMPL_USDT()
"""
    name: WAMPL-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class WAXL_USD(NamedTuple):
    """
        name: WAXL-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "WAXL-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WAXL-USD"

    def __str__(self):
        return "WAXL-USD"

    def __call__(self):
        return "WAXL-USD"


WAXL_USD = WAXL_USD()
"""
    name: WAXL-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class WBTC_BTC(NamedTuple):
    """
        name: WBTC-BTC
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "WBTC-BTC"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WBTC-BTC"

    def __str__(self):
        return "WBTC-BTC"

    def __call__(self):
        return "WBTC-BTC"


WBTC_BTC = WBTC_BTC()
"""
    name: WBTC-BTC
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


class WBTC_USD(NamedTuple):
    """
        name: WBTC-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "WBTC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WBTC-USD"

    def __str__(self):
        return "WBTC-USD"

    def __call__(self):
        return "WBTC-USD"


WBTC_USD = WBTC_USD()
"""
    name: WBTC-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class WCFG_BTC(NamedTuple):
    """
        name: WCFG-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "WCFG-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WCFG-BTC"

    def __str__(self):
        return "WCFG-BTC"

    def __call__(self):
        return "WCFG-BTC"


WCFG_BTC = WCFG_BTC()
"""
    name: WCFG-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class WCFG_EUR(NamedTuple):
    """
        name: WCFG-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "WCFG-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WCFG-EUR"

    def __str__(self):
        return "WCFG-EUR"

    def __call__(self):
        return "WCFG-EUR"


WCFG_EUR = WCFG_EUR()
"""
    name: WCFG-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class WCFG_USD(NamedTuple):
    """
        name: WCFG-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "WCFG-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WCFG-USD"

    def __str__(self):
        return "WCFG-USD"

    def __call__(self):
        return "WCFG-USD"


WCFG_USD = WCFG_USD()
"""
    name: WCFG-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class WCFG_USDT(NamedTuple):
    """
        name: WCFG-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "WCFG-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WCFG-USDT"

    def __str__(self):
        return "WCFG-USDT"

    def __call__(self):
        return "WCFG-USDT"


WCFG_USDT = WCFG_USDT()
"""
    name: WCFG-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class WLUNA_EUR(NamedTuple):
    """
        name: WLUNA-EUR
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "WLUNA-EUR"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WLUNA-EUR"

    def __str__(self):
        return "WLUNA-EUR"

    def __call__(self):
        return "WLUNA-EUR"


WLUNA_EUR = WLUNA_EUR()
"""
    name: WLUNA-EUR
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class WLUNA_GBP(NamedTuple):
    """
        name: WLUNA-GBP
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "WLUNA-GBP"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WLUNA-GBP"

    def __str__(self):
        return "WLUNA-GBP"

    def __call__(self):
        return "WLUNA-GBP"


WLUNA_GBP = WLUNA_GBP()
"""
    name: WLUNA-GBP
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class WLUNA_USD(NamedTuple):
    """
        name: WLUNA-USD
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "WLUNA-USD"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WLUNA-USD"

    def __str__(self):
        return "WLUNA-USD"

    def __call__(self):
        return "WLUNA-USD"


WLUNA_USD = WLUNA_USD()
"""
    name: WLUNA-USD
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class WLUNA_USDT(NamedTuple):
    """
        name: WLUNA-USDT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "WLUNA-USDT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WLUNA-USDT"

    def __str__(self):
        return "WLUNA-USDT"

    def __call__(self):
        return "WLUNA-USDT"


WLUNA_USDT = WLUNA_USDT()
"""
    name: WLUNA-USDT
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class XCN_USD(NamedTuple):
    """
        name: XCN-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "XCN-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XCN-USD"

    def __str__(self):
        return "XCN-USD"

    def __call__(self):
        return "XCN-USD"


XCN_USD = XCN_USD()
"""
    name: XCN-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class XCN_USDT(NamedTuple):
    """
        name: XCN-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "XCN-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XCN-USDT"

    def __str__(self):
        return "XCN-USDT"

    def __call__(self):
        return "XCN-USDT"


XCN_USDT = XCN_USDT()
"""
    name: XCN-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class XLM_BTC(NamedTuple):
    """
        name: XLM-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "XLM-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLM-BTC"

    def __str__(self):
        return "XLM-BTC"

    def __call__(self):
        return "XLM-BTC"


XLM_BTC = XLM_BTC()
"""
    name: XLM-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class XLM_EUR(NamedTuple):
    """
        name: XLM-EUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "XLM-EUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLM-EUR"

    def __str__(self):
        return "XLM-EUR"

    def __call__(self):
        return "XLM-EUR"


XLM_EUR = XLM_EUR()
"""
    name: XLM-EUR
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class XLM_USD(NamedTuple):
    """
        name: XLM-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "XLM-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLM-USD"

    def __str__(self):
        return "XLM-USD"

    def __call__(self):
        return "XLM-USD"


XLM_USD = XLM_USD()
"""
    name: XLM-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class XLM_USDT(NamedTuple):
    """
        name: XLM-USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "XLM-USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLM-USDT"

    def __str__(self):
        return "XLM-USDT"

    def __call__(self):
        return "XLM-USDT"


XLM_USDT = XLM_USDT()
"""
    name: XLM-USDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class XRP_BTC(NamedTuple):
    """
        name: XRP-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.001
        maximum_order_size: None
        margin: False
    """
    name: str = "XRP-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.001
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRP-BTC"

    def __str__(self):
        return "XRP-BTC"

    def __call__(self):
        return "XRP-BTC"


XRP_BTC = XRP_BTC()
"""
    name: XRP-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.001
    maximum_order_size: None
    margin: False
"""


class XRP_EUR(NamedTuple):
    """
        name: XRP-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "XRP-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 10
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRP-EUR"

    def __str__(self):
        return "XRP-EUR"

    def __call__(self):
        return "XRP-EUR"


XRP_EUR = XRP_EUR()
"""
    name: XRP-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


class XRP_GBP(NamedTuple):
    """
        name: XRP-GBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "XRP-GBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 10
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRP-GBP"

    def __str__(self):
        return "XRP-GBP"

    def __call__(self):
        return "XRP-GBP"


XRP_GBP = XRP_GBP()
"""
    name: XRP-GBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


class XRP_USD(NamedTuple):
    """
        name: XRP-USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "XRP-USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 10
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRP-USD"

    def __str__(self):
        return "XRP-USD"

    def __call__(self):
        return "XRP-USD"


XRP_USD = XRP_USD()
"""
    name: XRP-USD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


class XTZ_BTC(NamedTuple):
    """
        name: XTZ-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "XTZ-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZ-BTC"

    def __str__(self):
        return "XTZ-BTC"

    def __call__(self):
        return "XTZ-BTC"


XTZ_BTC = XTZ_BTC()
"""
    name: XTZ-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class XTZ_EUR(NamedTuple):
    """
        name: XTZ-EUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "XTZ-EUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZ-EUR"

    def __str__(self):
        return "XTZ-EUR"

    def __call__(self):
        return "XTZ-EUR"


XTZ_EUR = XTZ_EUR()
"""
    name: XTZ-EUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class XTZ_GBP(NamedTuple):
    """
        name: XTZ-GBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.72
        maximum_order_size: None
        margin: False
    """
    name: str = "XTZ-GBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.72
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZ-GBP"

    def __str__(self):
        return "XTZ-GBP"

    def __call__(self):
        return "XTZ-GBP"


XTZ_GBP = XTZ_GBP()
"""
    name: XTZ-GBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.72
    maximum_order_size: None
    margin: False
"""


class XTZ_USD(NamedTuple):
    """
        name: XTZ-USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "XTZ-USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZ-USD"

    def __str__(self):
        return "XTZ-USD"

    def __call__(self):
        return "XTZ-USD"


XTZ_USD = XTZ_USD()
"""
    name: XTZ-USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class XYO_BTC(NamedTuple):
    """
        name: XYO-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "XYO-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XYO-BTC"

    def __str__(self):
        return "XYO-BTC"

    def __call__(self):
        return "XYO-BTC"


XYO_BTC = XYO_BTC()
"""
    name: XYO-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class XYO_EUR(NamedTuple):
    """
        name: XYO-EUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "XYO-EUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XYO-EUR"

    def __str__(self):
        return "XYO-EUR"

    def __call__(self):
        return "XYO-EUR"


XYO_EUR = XYO_EUR()
"""
    name: XYO-EUR
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class XYO_USD(NamedTuple):
    """
        name: XYO-USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "XYO-USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XYO-USD"

    def __str__(self):
        return "XYO-USD"

    def __call__(self):
        return "XYO-USD"


XYO_USD = XYO_USD()
"""
    name: XYO-USD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class XYO_USDT(NamedTuple):
    """
        name: XYO-USDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "XYO-USDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XYO-USDT"

    def __str__(self):
        return "XYO-USDT"

    def __call__(self):
        return "XYO-USDT"


XYO_USDT = XYO_USDT()
"""
    name: XYO-USDT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class YFI_BTC(NamedTuple):
    """
        name: YFI-BTC
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.00001
        maximum_order_size: None
        margin: False
    """
    name: str = "YFI-BTC"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.00001
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YFI-BTC"

    def __str__(self):
        return "YFI-BTC"

    def __call__(self):
        return "YFI-BTC"


YFI_BTC = YFI_BTC()
"""
    name: YFI-BTC
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.00001
    maximum_order_size: None
    margin: False
"""


class YFI_USD(NamedTuple):
    """
        name: YFI-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "YFI-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YFI-USD"

    def __str__(self):
        return "YFI-USD"

    def __call__(self):
        return "YFI-USD"


YFI_USD = YFI_USD()
"""
    name: YFI-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class YFII_USD(NamedTuple):
    """
        name: YFII-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "YFII-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YFII-USD"

    def __str__(self):
        return "YFII-USD"

    def __call__(self):
        return "YFII-USD"


YFII_USD = YFII_USD()
"""
    name: YFII-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ZEC_BTC(NamedTuple):
    """
        name: ZEC-BTC
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ZEC-BTC"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZEC-BTC"

    def __str__(self):
        return "ZEC-BTC"

    def __call__(self):
        return "ZEC-BTC"


ZEC_BTC = ZEC_BTC()
"""
    name: ZEC-BTC
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ZEC_USD(NamedTuple):
    """
        name: ZEC-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ZEC-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZEC-USD"

    def __str__(self):
        return "ZEC-USD"

    def __call__(self):
        return "ZEC-USD"


ZEC_USD = ZEC_USD()
"""
    name: ZEC-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ZEC_USDC(NamedTuple):
    """
        name: ZEC-USDC
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ZEC-USDC"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZEC-USDC"

    def __str__(self):
        return "ZEC-USDC"

    def __call__(self):
        return "ZEC-USDC"


ZEC_USDC = ZEC_USDC()
"""
    name: ZEC-USDC
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ZEN_BTC(NamedTuple):
    """
        name: ZEN-BTC
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ZEN-BTC"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZEN-BTC"

    def __str__(self):
        return "ZEN-BTC"

    def __call__(self):
        return "ZEN-BTC"


ZEN_BTC = ZEN_BTC()
"""
    name: ZEN-BTC
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ZEN_USD(NamedTuple):
    """
        name: ZEN-USD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ZEN-USD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZEN-USD"

    def __str__(self):
        return "ZEN-USD"

    def __call__(self):
        return "ZEN-USD"


ZEN_USD = ZEN_USD()
"""
    name: ZEN-USD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ZEN_USDT(NamedTuple):
    """
        name: ZEN-USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ZEN-USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZEN-USDT"

    def __str__(self):
        return "ZEN-USDT"

    def __call__(self):
        return "ZEN-USDT"


ZEN_USDT = ZEN_USDT()
"""
    name: ZEN-USDT
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


class ZRX_BTC(NamedTuple):
    """
        name: ZRX-BTC
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.000016
        maximum_order_size: None
        margin: False
    """
    name: str = "ZRX-BTC"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.000016
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZRX-BTC"

    def __str__(self):
        return "ZRX-BTC"

    def __call__(self):
        return "ZRX-BTC"


ZRX_BTC = ZRX_BTC()
"""
    name: ZRX-BTC
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.000016
    maximum_order_size: None
    margin: False
"""


class ZRX_EUR(NamedTuple):
    """
        name: ZRX-EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.84
        maximum_order_size: None
        margin: False
    """
    name: str = "ZRX-EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.84
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZRX-EUR"

    def __str__(self):
        return "ZRX-EUR"

    def __call__(self):
        return "ZRX-EUR"


ZRX_EUR = ZRX_EUR()
"""
    name: ZRX-EUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.84
    maximum_order_size: None
    margin: False
"""


class ZRX_USD(NamedTuple):
    """
        name: ZRX-USD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "ZRX-USD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZRX-USD"

    def __str__(self):
        return "ZRX-USD"

    def __call__(self):
        return "ZRX-USD"


ZRX_USD = ZRX_USD()
"""
    name: ZRX-USD
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""
