from typing import NamedTuple


class ZERO0_USD(NamedTuple):
    """
        name: 00-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "00-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ONEINCH_BTC(NamedTuple):
    """
        name: 1INCH-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "1INCH-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ONEINCH_EUR(NamedTuple):
    """
        name: 1INCH-EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "1INCH-EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ONEINCH_GBP(NamedTuple):
    """
        name: 1INCH-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "1INCH-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ONEINCH_USD(NamedTuple):
    """
        name: 1INCH-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "1INCH-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AAVE_BTC(NamedTuple):
    """
        name: AAVE-BTC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AAVE-BTC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AAVE_EUR(NamedTuple):
    """
        name: AAVE-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AAVE-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AAVE_GBP(NamedTuple):
    """
        name: AAVE-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AAVE-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AAVE_USD(NamedTuple):
    """
        name: AAVE-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AAVE-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ABT_USD(NamedTuple):
    """
        name: ABT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ABT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ACH_USD(NamedTuple):
    """
        name: ACH-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ACH-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ACH_USDT(NamedTuple):
    """
        name: ACH-USDT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ACH-USDT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ACS_USD(NamedTuple):
    """
        name: ACS-USD
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ACS-USD"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ACS-USD"

    def __str__(self):
        return "ACS-USD"

    def __call__(self):
        return "ACS-USD"


ACS_USD = ACS_USD()
"""
    name: ACS-USD
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ADA_BTC(NamedTuple):
    """
        name: ADA-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ADA-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ADA_ETH(NamedTuple):
    """
        name: ADA-ETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00022
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ADA-ETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00022
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00022
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ADA_EUR(NamedTuple):
    """
        name: ADA-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ADA-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ADA_GBP(NamedTuple):
    """
        name: ADA-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ADA-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ADA_USD(NamedTuple):
    """
        name: ADA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ADA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ADA_USDC(NamedTuple):
    """
        name: ADA-USDC
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ADA-USDC"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ADA_USDT(NamedTuple):
    """
        name: ADA-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ADA-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AERGO_USD(NamedTuple):
    """
        name: AERGO-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AERGO-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AGLD_USD(NamedTuple):
    """
        name: AGLD-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AGLD-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AGLD_USDT(NamedTuple):
    """
        name: AGLD-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AGLD-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AIOZ_USD(NamedTuple):
    """
        name: AIOZ-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AIOZ-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AIOZ_USDT(NamedTuple):
    """
        name: AIOZ-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AIOZ-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ALCX_EUR(NamedTuple):
    """
        name: ALCX-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ALCX-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ALCX_USD(NamedTuple):
    """
        name: ALCX-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ALCX-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ALCX_USDT(NamedTuple):
    """
        name: ALCX-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ALCX-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ALEPH_USD(NamedTuple):
    """
        name: ALEPH-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ALEPH-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ALGO_BTC(NamedTuple):
    """
        name: ALGO-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ALGO-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ALGO_EUR(NamedTuple):
    """
        name: ALGO-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ALGO-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ALGO_GBP(NamedTuple):
    """
        name: ALGO-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ALGO-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ALGO_USD(NamedTuple):
    """
        name: ALGO-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ALGO-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ALICE_USD(NamedTuple):
    """
        name: ALICE-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ALICE-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AMP_USD(NamedTuple):
    """
        name: AMP-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AMP-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ANKR_BTC(NamedTuple):
    """
        name: ANKR-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ANKR-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ANKR_EUR(NamedTuple):
    """
        name: ANKR-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ANKR-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ANKR_GBP(NamedTuple):
    """
        name: ANKR-GBP
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ANKR-GBP"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ANKR_USD(NamedTuple):
    """
        name: ANKR-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ANKR-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ANT_USD(NamedTuple):
    """
        name: ANT-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 5.0
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ANT-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5.0
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 5.0
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class APE_EUR(NamedTuple):
    """
        name: APE-EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "APE-EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class APE_USD(NamedTuple):
    """
        name: APE-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "APE-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class APE_USDT(NamedTuple):
    """
        name: APE-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "APE-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class API3_USD(NamedTuple):
    """
        name: API3-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "API3-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class API3_USDT(NamedTuple):
    """
        name: API3-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "API3-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class APT_USD(NamedTuple):
    """
        name: APT-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "APT-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class APT_USDT(NamedTuple):
    """
        name: APT-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "APT-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ARB_USD(NamedTuple):
    """
        name: ARB-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ARB-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARB-USD"

    def __str__(self):
        return "ARB-USD"

    def __call__(self):
        return "ARB-USD"


ARB_USD = ARB_USD()
"""
    name: ARB-USD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ARPA_EUR(NamedTuple):
    """
        name: ARPA-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ARPA-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ARPA_USD(NamedTuple):
    """
        name: ARPA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ARPA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ARPA_USDT(NamedTuple):
    """
        name: ARPA-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ARPA-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ASM_USD(NamedTuple):
    """
        name: ASM-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ASM-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ASM_USDT(NamedTuple):
    """
        name: ASM-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ASM-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AST_USD(NamedTuple):
    """
        name: AST-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AST-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ATA_USD(NamedTuple):
    """
        name: ATA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ATA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ATA_USDT(NamedTuple):
    """
        name: ATA-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ATA-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ATOM_BTC(NamedTuple):
    """
        name: ATOM-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ATOM-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ATOM_EUR(NamedTuple):
    """
        name: ATOM-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ATOM-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ATOM_GBP(NamedTuple):
    """
        name: ATOM-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ATOM-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ATOM_USD(NamedTuple):
    """
        name: ATOM-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ATOM-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ATOM_USDT(NamedTuple):
    """
        name: ATOM-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ATOM-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AUCTION_EUR(NamedTuple):
    """
        name: AUCTION-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AUCTION-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AUCTION_USD(NamedTuple):
    """
        name: AUCTION-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AUCTION-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AUCTION_USDT(NamedTuple):
    """
        name: AUCTION-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AUCTION-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AUDIO_USD(NamedTuple):
    """
        name: AUDIO-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AUDIO-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AUDIO-USD"

    def __str__(self):
        return "AUDIO-USD"

    def __call__(self):
        return "AUDIO-USD"


AUDIO_USD = AUDIO_USD()
"""
    name: AUDIO-USD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AURORA_USD(NamedTuple):
    """
        name: AURORA-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AURORA-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AVAX_BTC(NamedTuple):
    """
        name: AVAX-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AVAX-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AVAX_EUR(NamedTuple):
    """
        name: AVAX-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AVAX-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AVAX_USD(NamedTuple):
    """
        name: AVAX-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AVAX-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AVAX_USDT(NamedTuple):
    """
        name: AVAX-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AVAX-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AVT_USD(NamedTuple):
    """
        name: AVT-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AVT-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AXL_USD(NamedTuple):
    """
        name: AXL-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AXL-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AXL-USD"

    def __str__(self):
        return "AXL-USD"

    def __call__(self):
        return "AXL-USD"


AXL_USD = AXL_USD()
"""
    name: AXL-USD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AXS_BTC(NamedTuple):
    """
        name: AXS-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AXS-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AXS_EUR(NamedTuple):
    """
        name: AXS-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AXS-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AXS_USD(NamedTuple):
    """
        name: AXS-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AXS-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class AXS_USDT(NamedTuple):
    """
        name: AXS-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "AXS-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BADGER_EUR(NamedTuple):
    """
        name: BADGER-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BADGER-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BADGER_USD(NamedTuple):
    """
        name: BADGER-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BADGER-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BADGER_USDT(NamedTuple):
    """
        name: BADGER-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BADGER-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAL_BTC(NamedTuple):
    """
        name: BAL-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAL-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAL_USD(NamedTuple):
    """
        name: BAL-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAL-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAND_BTC(NamedTuple):
    """
        name: BAND-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAND-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAND_EUR(NamedTuple):
    """
        name: BAND-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAND-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAND_GBP(NamedTuple):
    """
        name: BAND-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAND-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAND_USD(NamedTuple):
    """
        name: BAND-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAND-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAT_BTC(NamedTuple):
    """
        name: BAT-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAT-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAT_ETH(NamedTuple):
    """
        name: BAT-ETH
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00022
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAT-ETH"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00022
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00022
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAT_EUR(NamedTuple):
    """
        name: BAT-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAT-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAT_USD(NamedTuple):
    """
        name: BAT-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAT-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BAT_USDC(NamedTuple):
    """
        name: BAT-USDC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BAT-USDC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BCH_BTC(NamedTuple):
    """
        name: BCH-BTC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00001
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BCH-BTC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00001
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BCH_EUR(NamedTuple):
    """
        name: BCH-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BCH-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BCH_GBP(NamedTuple):
    """
        name: BCH-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BCH-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BCH_USD(NamedTuple):
    """
        name: BCH-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BCH-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BICO_EUR(NamedTuple):
    """
        name: BICO-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BICO-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BICO_USD(NamedTuple):
    """
        name: BICO-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BICO-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BICO_USDT(NamedTuple):
    """
        name: BICO-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BICO-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BIT_USD(NamedTuple):
    """
        name: BIT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BIT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BIT_USDT(NamedTuple):
    """
        name: BIT-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BIT-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BLUR_USD(NamedTuple):
    """
        name: BLUR-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BLUR-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BLUR-USD"

    def __str__(self):
        return "BLUR-USD"

    def __call__(self):
        return "BLUR-USD"


BLUR_USD = BLUR_USD()
"""
    name: BLUR-USD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BLZ_USD(NamedTuple):
    """
        name: BLZ-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BLZ-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BNT_BTC(NamedTuple):
    """
        name: BNT-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BNT-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BNT_EUR(NamedTuple):
    """
        name: BNT-EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BNT-EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BNT_GBP(NamedTuple):
    """
        name: BNT-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BNT-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BNT_USD(NamedTuple):
    """
        name: BNT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BNT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BOBA_USD(NamedTuple):
    """
        name: BOBA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BOBA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BOBA_USDT(NamedTuple):
    """
        name: BOBA-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BOBA-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BOND_USD(NamedTuple):
    """
        name: BOND-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BOND-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BOND_USDT(NamedTuple):
    """
        name: BOND-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BOND-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTC_EUR(NamedTuple):
    """
        name: BTC-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTC-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTC_GBP(NamedTuple):
    """
        name: BTC-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTC-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTC_USD(NamedTuple):
    """
        name: BTC-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTC-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTC_USDC(NamedTuple):
    """
        name: BTC-USDC
        significant_digits: None
        tick_size: 1
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTC-USDC"
    significant_digits: int = None
    tick_size: int = 1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 1
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTC_USDT(NamedTuple):
    """
        name: BTC-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTC-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTRST_BTC(NamedTuple):
    """
        name: BTRST-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTRST-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTRST_EUR(NamedTuple):
    """
        name: BTRST-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTRST-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTRST_GBP(NamedTuple):
    """
        name: BTRST-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTRST-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTRST_USD(NamedTuple):
    """
        name: BTRST-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTRST-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BTRST_USDT(NamedTuple):
    """
        name: BTRST-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BTRST-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class BUSD_USD(NamedTuple):
    """
        name: BUSD-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "BUSD-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class C98_USD(NamedTuple):
    """
        name: C98-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "C98-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class C98_USDT(NamedTuple):
    """
        name: C98-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "C98-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CBETH_ETH(NamedTuple):
    """
        name: CBETH-ETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.002
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CBETH-ETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.002
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.002
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CBETH_USD(NamedTuple):
    """
        name: CBETH-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CBETH-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CELR_USD(NamedTuple):
    """
        name: CELR-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CELR-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CGLD_BTC(NamedTuple):
    """
        name: CGLD-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CGLD-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CGLD_EUR(NamedTuple):
    """
        name: CGLD-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CGLD-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CGLD_GBP(NamedTuple):
    """
        name: CGLD-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CGLD-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CGLD_USD(NamedTuple):
    """
        name: CGLD-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CGLD-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CHZ_EUR(NamedTuple):
    """
        name: CHZ-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CHZ-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CHZ_GBP(NamedTuple):
    """
        name: CHZ-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CHZ-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CHZ_USD(NamedTuple):
    """
        name: CHZ-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CHZ-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CHZ_USDT(NamedTuple):
    """
        name: CHZ-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CHZ-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CLV_EUR(NamedTuple):
    """
        name: CLV-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CLV-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CLV_GBP(NamedTuple):
    """
        name: CLV-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CLV-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CLV_USD(NamedTuple):
    """
        name: CLV-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CLV-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CLV_USDT(NamedTuple):
    """
        name: CLV-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CLV-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class COMP_BTC(NamedTuple):
    """
        name: COMP-BTC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "COMP-BTC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class COMP_USD(NamedTuple):
    """
        name: COMP-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "COMP-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class COTI_USD(NamedTuple):
    """
        name: COTI-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "COTI-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class COVAL_USD(NamedTuple):
    """
        name: COVAL-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "COVAL-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class COVAL_USDT(NamedTuple):
    """
        name: COVAL-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "COVAL-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CRO_EUR(NamedTuple):
    """
        name: CRO-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CRO-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CRO_USD(NamedTuple):
    """
        name: CRO-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CRO-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CRO_USDT(NamedTuple):
    """
        name: CRO-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CRO-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CRPT_USD(NamedTuple):
    """
        name: CRPT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CRPT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CRV_BTC(NamedTuple):
    """
        name: CRV-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CRV-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CRV_EUR(NamedTuple):
    """
        name: CRV-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CRV-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CRV_GBP(NamedTuple):
    """
        name: CRV-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CRV-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CRV_USD(NamedTuple):
    """
        name: CRV-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CRV-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CTSI_BTC(NamedTuple):
    """
        name: CTSI-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CTSI-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CTSI_USD(NamedTuple):
    """
        name: CTSI-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CTSI-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CTX_EUR(NamedTuple):
    """
        name: CTX-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CTX-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CTX_USD(NamedTuple):
    """
        name: CTX-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CTX-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CTX_USDT(NamedTuple):
    """
        name: CTX-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CTX-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CVC_USD(NamedTuple):
    """
        name: CVC-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CVC-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CVC_USDC(NamedTuple):
    """
        name: CVC-USDC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CVC-USDC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class CVX_USD(NamedTuple):
    """
        name: CVX-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "CVX-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DAI_USD(NamedTuple):
    """
        name: DAI-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DAI-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DAI_USDC(NamedTuple):
    """
        name: DAI-USDC
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DAI-USDC"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DAR_USD(NamedTuple):
    """
        name: DAR-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DAR-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DASH_BTC(NamedTuple):
    """
        name: DASH-BTC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DASH-BTC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DASH_USD(NamedTuple):
    """
        name: DASH-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DASH-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DDX_EUR(NamedTuple):
    """
        name: DDX-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DDX-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DDX_USD(NamedTuple):
    """
        name: DDX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DDX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DDX_USDT(NamedTuple):
    """
        name: DDX-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DDX-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DESO_EUR(NamedTuple):
    """
        name: DESO-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DESO-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DESO_USD(NamedTuple):
    """
        name: DESO-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DESO-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DESO_USDT(NamedTuple):
    """
        name: DESO-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DESO-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DEXT_USD(NamedTuple):
    """
        name: DEXT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DEXT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DIA_EUR(NamedTuple):
    """
        name: DIA-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DIA-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DIA_USD(NamedTuple):
    """
        name: DIA-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DIA-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DIA_USDT(NamedTuple):
    """
        name: DIA-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DIA-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DIMO_USD(NamedTuple):
    """
        name: DIMO-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DIMO-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DIMO-USD"

    def __str__(self):
        return "DIMO-USD"

    def __call__(self):
        return "DIMO-USD"


DIMO_USD = DIMO_USD()
"""
    name: DIMO-USD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DNT_USD(NamedTuple):
    """
        name: DNT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DNT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DNT_USDC(NamedTuple):
    """
        name: DNT-USDC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DNT-USDC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOGE_BTC(NamedTuple):
    """
        name: DOGE-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOGE-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOGE_EUR(NamedTuple):
    """
        name: DOGE-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOGE-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOGE_GBP(NamedTuple):
    """
        name: DOGE-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOGE-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOGE_USD(NamedTuple):
    """
        name: DOGE-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOGE-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOGE_USDT(NamedTuple):
    """
        name: DOGE-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOGE-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOT_BTC(NamedTuple):
    """
        name: DOT-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOT-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOT_EUR(NamedTuple):
    """
        name: DOT-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOT-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOT_GBP(NamedTuple):
    """
        name: DOT-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOT-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOT_USD(NamedTuple):
    """
        name: DOT-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOT-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DOT_USDT(NamedTuple):
    """
        name: DOT-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DOT-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DREP_USD(NamedTuple):
    """
        name: DREP-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DREP-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DREP_USDT(NamedTuple):
    """
        name: DREP-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DREP-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DYP_USD(NamedTuple):
    """
        name: DYP-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DYP-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class DYP_USDT(NamedTuple):
    """
        name: DYP-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "DYP-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class EGLD_USD(NamedTuple):
    """
        name: EGLD-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "EGLD-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ELA_USD(NamedTuple):
    """
        name: ELA-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ELA-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ELA_USDT(NamedTuple):
    """
        name: ELA-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ELA-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ENJ_BTC(NamedTuple):
    """
        name: ENJ-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ENJ-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ENJ_USD(NamedTuple):
    """
        name: ENJ-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ENJ-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ENJ_USDT(NamedTuple):
    """
        name: ENJ-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ENJ-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ENS_EUR(NamedTuple):
    """
        name: ENS-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ENS-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ENS_USD(NamedTuple):
    """
        name: ENS-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ENS-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ENS_USDT(NamedTuple):
    """
        name: ENS-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ENS-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class EOS_BTC(NamedTuple):
    """
        name: EOS-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "EOS-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class EOS_EUR(NamedTuple):
    """
        name: EOS-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "EOS-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class EOS_USD(NamedTuple):
    """
        name: EOS-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "EOS-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ERN_EUR(NamedTuple):
    """
        name: ERN-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ERN-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ERN_USD(NamedTuple):
    """
        name: ERN-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ERN-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ERN_USDT(NamedTuple):
    """
        name: ERN-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ERN-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETC_BTC(NamedTuple):
    """
        name: ETC-BTC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETC-BTC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETC_EUR(NamedTuple):
    """
        name: ETC-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETC-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETC_GBP(NamedTuple):
    """
        name: ETC-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETC-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETC_USD(NamedTuple):
    """
        name: ETC-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETC-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETH_BTC(NamedTuple):
    """
        name: ETH-BTC
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00001
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETH-BTC"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00001
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETH_DAI(NamedTuple):
    """
        name: ETH-DAI
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETH-DAI"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETH_EUR(NamedTuple):
    """
        name: ETH-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETH-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETH_GBP(NamedTuple):
    """
        name: ETH-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETH-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETH_USD(NamedTuple):
    """
        name: ETH-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETH-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETH_USDC(NamedTuple):
    """
        name: ETH-USDC
        significant_digits: None
        tick_size: 1
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETH-USDC"
    significant_digits: int = None
    tick_size: int = 1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 1
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ETH_USDT(NamedTuple):
    """
        name: ETH-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ETH-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class EUROC_EUR(NamedTuple):
    """
        name: EUROC-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "EUROC-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EUROC-EUR"

    def __str__(self):
        return "EUROC-EUR"

    def __call__(self):
        return "EUROC-EUR"


EUROC_EUR = EUROC_EUR()
"""
    name: EUROC-EUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class EUROC_USD(NamedTuple):
    """
        name: EUROC-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "EUROC-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EUROC-USD"

    def __str__(self):
        return "EUROC-USD"

    def __call__(self):
        return "EUROC-USD"


EUROC_USD = EUROC_USD()
"""
    name: EUROC-USD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FARM_USD(NamedTuple):
    """
        name: FARM-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FARM-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FARM_USDT(NamedTuple):
    """
        name: FARM-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FARM-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FET_USD(NamedTuple):
    """
        name: FET-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FET-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FET_USDT(NamedTuple):
    """
        name: FET-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FET-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FIDA_EUR(NamedTuple):
    """
        name: FIDA-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FIDA-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FIDA_USD(NamedTuple):
    """
        name: FIDA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FIDA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FIDA_USDT(NamedTuple):
    """
        name: FIDA-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FIDA-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FIL_BTC(NamedTuple):
    """
        name: FIL-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FIL-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FIL_EUR(NamedTuple):
    """
        name: FIL-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FIL-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FIL_GBP(NamedTuple):
    """
        name: FIL-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FIL-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FIL_USD(NamedTuple):
    """
        name: FIL-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FIL-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FIS_USD(NamedTuple):
    """
        name: FIS-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FIS-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FIS_USDT(NamedTuple):
    """
        name: FIS-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FIS-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FLOW_USD(NamedTuple):
    """
        name: FLOW-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FLOW-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FLOW_USDT(NamedTuple):
    """
        name: FLOW-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FLOW-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FLR_USD(NamedTuple):
    """
        name: FLR-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FLR-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLR-USD"

    def __str__(self):
        return "FLR-USD"

    def __call__(self):
        return "FLR-USD"


FLR_USD = FLR_USD()
"""
    name: FLR-USD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FORT_USD(NamedTuple):
    """
        name: FORT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FORT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FORT_USDT(NamedTuple):
    """
        name: FORT-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FORT-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FORTH_BTC(NamedTuple):
    """
        name: FORTH-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FORTH-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FORTH_EUR(NamedTuple):
    """
        name: FORTH-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FORTH-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FORTH_GBP(NamedTuple):
    """
        name: FORTH-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FORTH-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FORTH_USD(NamedTuple):
    """
        name: FORTH-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FORTH-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FOX_USD(NamedTuple):
    """
        name: FOX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FOX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FOX_USDT(NamedTuple):
    """
        name: FOX-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FOX-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class FX_USD(NamedTuple):
    """
        name: FX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "FX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GAL_USD(NamedTuple):
    """
        name: GAL-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GAL-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GAL_USDT(NamedTuple):
    """
        name: GAL-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GAL-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GALA_EUR(NamedTuple):
    """
        name: GALA-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GALA-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GALA_USD(NamedTuple):
    """
        name: GALA-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GALA-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GALA_USDT(NamedTuple):
    """
        name: GALA-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GALA-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GFI_USD(NamedTuple):
    """
        name: GFI-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GFI-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GHST_USD(NamedTuple):
    """
        name: GHST-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GHST-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GLM_USD(NamedTuple):
    """
        name: GLM-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GLM-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GMT_USD(NamedTuple):
    """
        name: GMT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GMT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GMT_USDT(NamedTuple):
    """
        name: GMT-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GMT-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GNO_USD(NamedTuple):
    """
        name: GNO-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GNO-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GNO_USDT(NamedTuple):
    """
        name: GNO-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GNO-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GNT_USDC(NamedTuple):
    """
        name: GNT-USDC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GNT-USDC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GODS_USD(NamedTuple):
    """
        name: GODS-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GODS-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GRT_BTC(NamedTuple):
    """
        name: GRT-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GRT-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GRT_EUR(NamedTuple):
    """
        name: GRT-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GRT-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GRT_GBP(NamedTuple):
    """
        name: GRT-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GRT-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GRT_USD(NamedTuple):
    """
        name: GRT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GRT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GST_USD(NamedTuple):
    """
        name: GST-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GST-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GTC_USD(NamedTuple):
    """
        name: GTC-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GTC-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GUSD_USD(NamedTuple):
    """
        name: GUSD-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GUSD-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class GYEN_USD(NamedTuple):
    """
        name: GYEN-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "GYEN-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class HBAR_USD(NamedTuple):
    """
        name: HBAR-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "HBAR-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class HBAR_USDT(NamedTuple):
    """
        name: HBAR-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "HBAR-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class HFT_USD(NamedTuple):
    """
        name: HFT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "HFT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class HFT_USDT(NamedTuple):
    """
        name: HFT-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "HFT-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class HIGH_USD(NamedTuple):
    """
        name: HIGH-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "HIGH-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class HOPR_USD(NamedTuple):
    """
        name: HOPR-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "HOPR-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class HOPR_USDT(NamedTuple):
    """
        name: HOPR-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "HOPR-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ICP_BTC(NamedTuple):
    """
        name: ICP-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ICP-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ICP_EUR(NamedTuple):
    """
        name: ICP-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ICP-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ICP_GBP(NamedTuple):
    """
        name: ICP-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ICP-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ICP_USD(NamedTuple):
    """
        name: ICP-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ICP-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ICP_USDT(NamedTuple):
    """
        name: ICP-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ICP-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class IDEX_USD(NamedTuple):
    """
        name: IDEX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "IDEX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class IDEX_USDT(NamedTuple):
    """
        name: IDEX-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "IDEX-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ILV_USD(NamedTuple):
    """
        name: ILV-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ILV-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class IMX_USD(NamedTuple):
    """
        name: IMX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "IMX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class IMX_USDT(NamedTuple):
    """
        name: IMX-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "IMX-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class INDEX_USD(NamedTuple):
    """
        name: INDEX-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "INDEX-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class INDEX_USDT(NamedTuple):
    """
        name: INDEX-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "INDEX-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class INJ_USD(NamedTuple):
    """
        name: INJ-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "INJ-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class INV_USD(NamedTuple):
    """
        name: INV-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "INV-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class IOTX_EUR(NamedTuple):
    """
        name: IOTX-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "IOTX-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class IOTX_USD(NamedTuple):
    """
        name: IOTX-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "IOTX-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class JASMY_USD(NamedTuple):
    """
        name: JASMY-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "JASMY-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class JASMY_USDT(NamedTuple):
    """
        name: JASMY-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "JASMY-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class JUP_USD(NamedTuple):
    """
        name: JUP-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "JUP-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class KAVA_USD(NamedTuple):
    """
        name: KAVA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "KAVA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class KEEP_USD(NamedTuple):
    """
        name: KEEP-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "KEEP-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class KNC_BTC(NamedTuple):
    """
        name: KNC-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "KNC-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class KNC_USD(NamedTuple):
    """
        name: KNC-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "KNC-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class KRL_EUR(NamedTuple):
    """
        name: KRL-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "KRL-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class KRL_USD(NamedTuple):
    """
        name: KRL-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "KRL-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class KRL_USDT(NamedTuple):
    """
        name: KRL-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "KRL-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class KSM_USD(NamedTuple):
    """
        name: KSM-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "KSM-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class KSM_USDT(NamedTuple):
    """
        name: KSM-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "KSM-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LCX_EUR(NamedTuple):
    """
        name: LCX-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LCX-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LCX_USD(NamedTuple):
    """
        name: LCX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LCX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LCX_USDT(NamedTuple):
    """
        name: LCX-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LCX-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LDO_USD(NamedTuple):
    """
        name: LDO-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LDO-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LINK_BTC(NamedTuple):
    """
        name: LINK-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LINK-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LINK_ETH(NamedTuple):
    """
        name: LINK-ETH
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00022
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LINK-ETH"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00022
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00022
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LINK_EUR(NamedTuple):
    """
        name: LINK-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LINK-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LINK_GBP(NamedTuple):
    """
        name: LINK-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LINK-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LINK_USD(NamedTuple):
    """
        name: LINK-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LINK-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LINK_USDT(NamedTuple):
    """
        name: LINK-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LINK-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LIT_USD(NamedTuple):
    """
        name: LIT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LIT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LOKA_USD(NamedTuple):
    """
        name: LOKA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LOKA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LOOM_USD(NamedTuple):
    """
        name: LOOM-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LOOM-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LOOM_USDC(NamedTuple):
    """
        name: LOOM-USDC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LOOM-USDC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LPT_USD(NamedTuple):
    """
        name: LPT-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LPT-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LQTY_EUR(NamedTuple):
    """
        name: LQTY-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LQTY-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LQTY_USD(NamedTuple):
    """
        name: LQTY-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LQTY-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LQTY_USDT(NamedTuple):
    """
        name: LQTY-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LQTY-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LRC_BTC(NamedTuple):
    """
        name: LRC-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LRC-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LRC_USD(NamedTuple):
    """
        name: LRC-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LRC-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LRC_USDT(NamedTuple):
    """
        name: LRC-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LRC-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LSETH_ETH(NamedTuple):
    """
        name: LSETH-ETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.002
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LSETH-ETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.002
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LSETH-ETH"

    def __str__(self):
        return "LSETH-ETH"

    def __call__(self):
        return "LSETH-ETH"


LSETH_ETH = LSETH_ETH()
"""
    name: LSETH-ETH
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.002
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LSETH_USD(NamedTuple):
    """
        name: LSETH-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LSETH-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LSETH-USD"

    def __str__(self):
        return "LSETH-USD"

    def __call__(self):
        return "LSETH-USD"


LSETH_USD = LSETH_USD()
"""
    name: LSETH-USD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LTC_BTC(NamedTuple):
    """
        name: LTC-BTC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LTC-BTC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LTC_EUR(NamedTuple):
    """
        name: LTC-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LTC-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LTC_GBP(NamedTuple):
    """
        name: LTC-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LTC-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class LTC_USD(NamedTuple):
    """
        name: LTC-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "LTC-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MAGIC_USD(NamedTuple):
    """
        name: MAGIC-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MAGIC-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MANA_BTC(NamedTuple):
    """
        name: MANA-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MANA-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MANA_ETH(NamedTuple):
    """
        name: MANA-ETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00022
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MANA-ETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00022
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00022
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MANA_EUR(NamedTuple):
    """
        name: MANA-EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MANA-EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MANA_USD(NamedTuple):
    """
        name: MANA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MANA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MANA_USDC(NamedTuple):
    """
        name: MANA-USDC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MANA-USDC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MASK_EUR(NamedTuple):
    """
        name: MASK-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MASK-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MASK_GBP(NamedTuple):
    """
        name: MASK-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MASK-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MASK_USD(NamedTuple):
    """
        name: MASK-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MASK-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MASK_USDT(NamedTuple):
    """
        name: MASK-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MASK-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MATH_USD(NamedTuple):
    """
        name: MATH-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MATH-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MATH_USDT(NamedTuple):
    """
        name: MATH-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MATH-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MATIC_BTC(NamedTuple):
    """
        name: MATIC-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MATIC-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MATIC_EUR(NamedTuple):
    """
        name: MATIC-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MATIC-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MATIC_GBP(NamedTuple):
    """
        name: MATIC-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MATIC-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MATIC_USD(NamedTuple):
    """
        name: MATIC-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MATIC-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MATIC_USDT(NamedTuple):
    """
        name: MATIC-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MATIC-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MCO2_USD(NamedTuple):
    """
        name: MCO2-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MCO2-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MCO2_USDT(NamedTuple):
    """
        name: MCO2-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MCO2-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MDT_USD(NamedTuple):
    """
        name: MDT-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MDT-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MDT_USDT(NamedTuple):
    """
        name: MDT-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MDT-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MEDIA_USD(NamedTuple):
    """
        name: MEDIA-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MEDIA-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MEDIA_USDT(NamedTuple):
    """
        name: MEDIA-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MEDIA-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class METIS_USD(NamedTuple):
    """
        name: METIS-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "METIS-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class METIS_USDT(NamedTuple):
    """
        name: METIS-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "METIS-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MINA_EUR(NamedTuple):
    """
        name: MINA-EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MINA-EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MINA_USD(NamedTuple):
    """
        name: MINA-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MINA-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MINA_USDT(NamedTuple):
    """
        name: MINA-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MINA-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MIR_BTC(NamedTuple):
    """
        name: MIR-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MIR-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MIR_EUR(NamedTuple):
    """
        name: MIR-EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MIR-EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MIR_GBP(NamedTuple):
    """
        name: MIR-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MIR-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MIR_USD(NamedTuple):
    """
        name: MIR-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MIR-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MKR_BTC(NamedTuple):
    """
        name: MKR-BTC
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00001
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MKR-BTC"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00001
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MKR_USD(NamedTuple):
    """
        name: MKR-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MKR-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MLN_USD(NamedTuple):
    """
        name: MLN-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MLN-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MNDE_USD(NamedTuple):
    """
        name: MNDE-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MNDE-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MONA_USD(NamedTuple):
    """
        name: MONA-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MONA-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MPL_USD(NamedTuple):
    """
        name: MPL-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MPL-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MSOL_USD(NamedTuple):
    """
        name: MSOL-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MSOL-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MTL_USD(NamedTuple):
    """
        name: MTL-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MTL-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MUSD_USD(NamedTuple):
    """
        name: MUSD-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MUSD-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MUSE_USD(NamedTuple):
    """
        name: MUSE-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MUSE-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class MXC_USD(NamedTuple):
    """
        name: MXC-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "MXC-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NCT_EUR(NamedTuple):
    """
        name: NCT-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NCT-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NCT_USD(NamedTuple):
    """
        name: NCT-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NCT-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NCT_USDT(NamedTuple):
    """
        name: NCT-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NCT-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NEAR_USD(NamedTuple):
    """
        name: NEAR-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NEAR-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NEAR_USDT(NamedTuple):
    """
        name: NEAR-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NEAR-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NEST_USD(NamedTuple):
    """
        name: NEST-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NEST-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NEST_USDT(NamedTuple):
    """
        name: NEST-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NEST-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NKN_BTC(NamedTuple):
    """
        name: NKN-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NKN-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NKN_EUR(NamedTuple):
    """
        name: NKN-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NKN-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NKN_GBP(NamedTuple):
    """
        name: NKN-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NKN-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NKN_USD(NamedTuple):
    """
        name: NKN-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NKN-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NMR_BTC(NamedTuple):
    """
        name: NMR-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NMR-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NMR_EUR(NamedTuple):
    """
        name: NMR-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NMR-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NMR_GBP(NamedTuple):
    """
        name: NMR-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NMR-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NMR_USD(NamedTuple):
    """
        name: NMR-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NMR-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NU_BTC(NamedTuple):
    """
        name: NU-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NU-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NU_EUR(NamedTuple):
    """
        name: NU-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NU-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NU_GBP(NamedTuple):
    """
        name: NU-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NU-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class NU_USD(NamedTuple):
    """
        name: NU-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "NU-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OCEAN_USD(NamedTuple):
    """
        name: OCEAN-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OCEAN-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OGN_BTC(NamedTuple):
    """
        name: OGN-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OGN-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OGN_USD(NamedTuple):
    """
        name: OGN-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OGN-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OMG_BTC(NamedTuple):
    """
        name: OMG-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OMG-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OMG_EUR(NamedTuple):
    """
        name: OMG-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OMG-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OMG_GBP(NamedTuple):
    """
        name: OMG-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OMG-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OMG_USD(NamedTuple):
    """
        name: OMG-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OMG-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OOKI_USD(NamedTuple):
    """
        name: OOKI-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OOKI-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OP_USD(NamedTuple):
    """
        name: OP-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OP-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OP_USDT(NamedTuple):
    """
        name: OP-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OP-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ORCA_USD(NamedTuple):
    """
        name: ORCA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ORCA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ORN_BTC(NamedTuple):
    """
        name: ORN-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ORN-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ORN_USD(NamedTuple):
    """
        name: ORN-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ORN-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ORN_USDT(NamedTuple):
    """
        name: ORN-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ORN-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class OXT_USD(NamedTuple):
    """
        name: OXT-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "OXT-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PAX_USD(NamedTuple):
    """
        name: PAX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PAX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PAX_USDT(NamedTuple):
    """
        name: PAX-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PAX-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PERP_EUR(NamedTuple):
    """
        name: PERP-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PERP-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PERP_USD(NamedTuple):
    """
        name: PERP-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PERP-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PERP_USDT(NamedTuple):
    """
        name: PERP-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PERP-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PLA_USD(NamedTuple):
    """
        name: PLA-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PLA-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PLU_USD(NamedTuple):
    """
        name: PLU-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PLU-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PNG_USD(NamedTuple):
    """
        name: PNG-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PNG-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class POLS_USD(NamedTuple):
    """
        name: POLS-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "POLS-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class POLS_USDT(NamedTuple):
    """
        name: POLS-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "POLS-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class POLY_USD(NamedTuple):
    """
        name: POLY-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "POLY-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class POLY_USDT(NamedTuple):
    """
        name: POLY-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "POLY-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class POND_USD(NamedTuple):
    """
        name: POND-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "POND-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class POND_USDT(NamedTuple):
    """
        name: POND-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "POND-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class POWR_EUR(NamedTuple):
    """
        name: POWR-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "POWR-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class POWR_USD(NamedTuple):
    """
        name: POWR-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "POWR-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class POWR_USDT(NamedTuple):
    """
        name: POWR-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "POWR-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PRIME_USD(NamedTuple):
    """
        name: PRIME-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PRIME-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PRIME-USD"

    def __str__(self):
        return "PRIME-USD"

    def __call__(self):
        return "PRIME-USD"


PRIME_USD = PRIME_USD()
"""
    name: PRIME-USD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PRO_USD(NamedTuple):
    """
        name: PRO-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PRO-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PRQ_USD(NamedTuple):
    """
        name: PRQ-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PRQ-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PRQ_USDT(NamedTuple):
    """
        name: PRQ-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PRQ-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PUNDIX_USD(NamedTuple):
    """
        name: PUNDIX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PUNDIX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class PYR_USD(NamedTuple):
    """
        name: PYR-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "PYR-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class QI_USD(NamedTuple):
    """
        name: QI-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "QI-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class QNT_USD(NamedTuple):
    """
        name: QNT-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "QNT-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class QNT_USDT(NamedTuple):
    """
        name: QNT-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "QNT-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class QSP_USD(NamedTuple):
    """
        name: QSP-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "QSP-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class QSP_USDT(NamedTuple):
    """
        name: QSP-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "QSP-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class QUICK_USD(NamedTuple):
    """
        name: QUICK-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "QUICK-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RAD_BTC(NamedTuple):
    """
        name: RAD-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RAD-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RAD_EUR(NamedTuple):
    """
        name: RAD-EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RAD-EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RAD_GBP(NamedTuple):
    """
        name: RAD-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RAD-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RAD_USD(NamedTuple):
    """
        name: RAD-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RAD-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RAD_USDT(NamedTuple):
    """
        name: RAD-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RAD-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RAI_USD(NamedTuple):
    """
        name: RAI-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RAI-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RARE_USD(NamedTuple):
    """
        name: RARE-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RARE-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RARI_USD(NamedTuple):
    """
        name: RARI-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RARI-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RBN_USD(NamedTuple):
    """
        name: RBN-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RBN-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class REN_BTC(NamedTuple):
    """
        name: REN-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "REN-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class REN_USD(NamedTuple):
    """
        name: REN-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "REN-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class REP_BTC(NamedTuple):
    """
        name: REP-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "REP-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class REP_USD(NamedTuple):
    """
        name: REP-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "REP-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class REQ_BTC(NamedTuple):
    """
        name: REQ-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "REQ-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class REQ_EUR(NamedTuple):
    """
        name: REQ-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "REQ-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class REQ_GBP(NamedTuple):
    """
        name: REQ-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "REQ-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class REQ_USD(NamedTuple):
    """
        name: REQ-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "REQ-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class REQ_USDT(NamedTuple):
    """
        name: REQ-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "REQ-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RGT_USD(NamedTuple):
    """
        name: RGT-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RGT-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RLC_BTC(NamedTuple):
    """
        name: RLC-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RLC-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RLC_USD(NamedTuple):
    """
        name: RLC-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RLC-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RLY_EUR(NamedTuple):
    """
        name: RLY-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RLY-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RLY_GBP(NamedTuple):
    """
        name: RLY-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RLY-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RLY_USD(NamedTuple):
    """
        name: RLY-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RLY-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RLY_USDT(NamedTuple):
    """
        name: RLY-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RLY-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RNDR_EUR(NamedTuple):
    """
        name: RNDR-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RNDR-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RNDR_USD(NamedTuple):
    """
        name: RNDR-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RNDR-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RNDR_USDT(NamedTuple):
    """
        name: RNDR-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RNDR-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ROSE_USD(NamedTuple):
    """
        name: ROSE-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ROSE-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ROSE_USDT(NamedTuple):
    """
        name: ROSE-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ROSE-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class RPL_USD(NamedTuple):
    """
        name: RPL-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "RPL-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SAND_USD(NamedTuple):
    """
        name: SAND-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SAND-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SAND_USDT(NamedTuple):
    """
        name: SAND-USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SAND-USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SHIB_EUR(NamedTuple):
    """
        name: SHIB-EUR
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SHIB-EUR"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SHIB_GBP(NamedTuple):
    """
        name: SHIB-GBP
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SHIB-GBP"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SHIB_USD(NamedTuple):
    """
        name: SHIB-USD
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SHIB-USD"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SHIB_USDT(NamedTuple):
    """
        name: SHIB-USDT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SHIB-USDT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SHPING_EUR(NamedTuple):
    """
        name: SHPING-EUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SHPING-EUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SHPING_USD(NamedTuple):
    """
        name: SHPING-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SHPING-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SHPING_USDT(NamedTuple):
    """
        name: SHPING-USDT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SHPING-USDT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SKL_BTC(NamedTuple):
    """
        name: SKL-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SKL-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SKL_EUR(NamedTuple):
    """
        name: SKL-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SKL-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SKL_GBP(NamedTuple):
    """
        name: SKL-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SKL-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SKL_USD(NamedTuple):
    """
        name: SKL-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SKL-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SNT_USD(NamedTuple):
    """
        name: SNT-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SNT-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SNX_BTC(NamedTuple):
    """
        name: SNX-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SNX-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SNX_EUR(NamedTuple):
    """
        name: SNX-EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SNX-EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SNX_GBP(NamedTuple):
    """
        name: SNX-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SNX-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SNX_USD(NamedTuple):
    """
        name: SNX-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SNX-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SOL_BTC(NamedTuple):
    """
        name: SOL-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SOL-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SOL_ETH(NamedTuple):
    """
        name: SOL-ETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00022
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SOL-ETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00022
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00022
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SOL_EUR(NamedTuple):
    """
        name: SOL-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SOL-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SOL_GBP(NamedTuple):
    """
        name: SOL-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SOL-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SOL_USD(NamedTuple):
    """
        name: SOL-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SOL-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SOL_USDT(NamedTuple):
    """
        name: SOL-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SOL-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SPELL_USD(NamedTuple):
    """
        name: SPELL-USD
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SPELL-USD"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SPELL_USDT(NamedTuple):
    """
        name: SPELL-USDT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SPELL-USDT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class STG_USD(NamedTuple):
    """
        name: STG-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "STG-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class STG_USDT(NamedTuple):
    """
        name: STG-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "STG-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class STORJ_BTC(NamedTuple):
    """
        name: STORJ-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "STORJ-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class STORJ_USD(NamedTuple):
    """
        name: STORJ-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "STORJ-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class STX_USD(NamedTuple):
    """
        name: STX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "STX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class STX_USDT(NamedTuple):
    """
        name: STX-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "STX-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUKU_EUR(NamedTuple):
    """
        name: SUKU-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUKU-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUKU_USD(NamedTuple):
    """
        name: SUKU-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUKU-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUKU_USDT(NamedTuple):
    """
        name: SUKU-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUKU-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUPER_USD(NamedTuple):
    """
        name: SUPER-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUPER-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUPER_USDT(NamedTuple):
    """
        name: SUPER-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUPER-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUSHI_BTC(NamedTuple):
    """
        name: SUSHI-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUSHI-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUSHI_ETH(NamedTuple):
    """
        name: SUSHI-ETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00022
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUSHI-ETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00022
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00022
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUSHI_EUR(NamedTuple):
    """
        name: SUSHI-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUSHI-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUSHI_GBP(NamedTuple):
    """
        name: SUSHI-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUSHI-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SUSHI_USD(NamedTuple):
    """
        name: SUSHI-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SUSHI-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SWFTC_USD(NamedTuple):
    """
        name: SWFTC-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SWFTC-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SYLO_USD(NamedTuple):
    """
        name: SYLO-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SYLO-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SYLO_USDT(NamedTuple):
    """
        name: SYLO-USDT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SYLO-USDT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class SYN_USD(NamedTuple):
    """
        name: SYN-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "SYN-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class T_USD(NamedTuple):
    """
        name: T-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "T-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "T-USD"

    def __str__(self):
        return "T-USD"

    def __call__(self):
        return "T-USD"


T_USD = T_USD()
"""
    name: T-USD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TIME_USD(NamedTuple):
    """
        name: TIME-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TIME-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TIME_USDT(NamedTuple):
    """
        name: TIME-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TIME-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TONE_USD(NamedTuple):
    """
        name: TONE-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TONE-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRAC_EUR(NamedTuple):
    """
        name: TRAC-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRAC-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRAC_USD(NamedTuple):
    """
        name: TRAC-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRAC-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRAC_USDT(NamedTuple):
    """
        name: TRAC-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRAC-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRB_BTC(NamedTuple):
    """
        name: TRB-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRB-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRB_USD(NamedTuple):
    """
        name: TRB-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRB-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRIBE_USD(NamedTuple):
    """
        name: TRIBE-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRIBE-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRU_BTC(NamedTuple):
    """
        name: TRU-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRU-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRU_EUR(NamedTuple):
    """
        name: TRU-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRU-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRU_USD(NamedTuple):
    """
        name: TRU-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRU-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TRU_USDT(NamedTuple):
    """
        name: TRU-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TRU-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class TVK_USD(NamedTuple):
    """
        name: TVK-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "TVK-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TVK-USD"

    def __str__(self):
        return "TVK-USD"

    def __call__(self):
        return "TVK-USD"


TVK_USD = TVK_USD()
"""
    name: TVK-USD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UMA_BTC(NamedTuple):
    """
        name: UMA-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UMA-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UMA_EUR(NamedTuple):
    """
        name: UMA-EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UMA-EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UMA_GBP(NamedTuple):
    """
        name: UMA-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UMA-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UMA_USD(NamedTuple):
    """
        name: UMA-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UMA-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UNFI_USD(NamedTuple):
    """
        name: UNFI-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UNFI-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UNI_BTC(NamedTuple):
    """
        name: UNI-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UNI-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UNI_EUR(NamedTuple):
    """
        name: UNI-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UNI-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UNI_GBP(NamedTuple):
    """
        name: UNI-GBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UNI-GBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UNI_USD(NamedTuple):
    """
        name: UNI-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UNI-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UPI_USD(NamedTuple):
    """
        name: UPI-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UPI-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UPI_USDT(NamedTuple):
    """
        name: UPI-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UPI-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class USDC_EUR(NamedTuple):
    """
        name: USDC-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "USDC-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class USDC_GBP(NamedTuple):
    """
        name: USDC-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "USDC-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class USDT_EUR(NamedTuple):
    """
        name: USDT-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "USDT-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class USDT_GBP(NamedTuple):
    """
        name: USDT-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "USDT-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class USDT_USD(NamedTuple):
    """
        name: USDT-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "USDT-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class USDT_USDC(NamedTuple):
    """
        name: USDT-USDC
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "USDT-USDC"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UST_EUR(NamedTuple):
    """
        name: UST-EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UST-EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UST_USD(NamedTuple):
    """
        name: UST-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UST-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class UST_USDT(NamedTuple):
    """
        name: UST-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "UST-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class VGX_EUR(NamedTuple):
    """
        name: VGX-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "VGX-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class VGX_USD(NamedTuple):
    """
        name: VGX-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "VGX-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class VGX_USDT(NamedTuple):
    """
        name: VGX-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "VGX-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class VOXEL_USD(NamedTuple):
    """
        name: VOXEL-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "VOXEL-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "VOXEL-USD"

    def __str__(self):
        return "VOXEL-USD"

    def __call__(self):
        return "VOXEL-USD"


VOXEL_USD = VOXEL_USD()
"""
    name: VOXEL-USD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WAMPL_USD(NamedTuple):
    """
        name: WAMPL-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WAMPL-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WAMPL_USDT(NamedTuple):
    """
        name: WAMPL-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WAMPL-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WAXL_USD(NamedTuple):
    """
        name: WAXL-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WAXL-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WBTC_BTC(NamedTuple):
    """
        name: WBTC-BTC
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WBTC-BTC"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WBTC_USD(NamedTuple):
    """
        name: WBTC-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WBTC-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WCFG_BTC(NamedTuple):
    """
        name: WCFG-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WCFG-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WCFG_EUR(NamedTuple):
    """
        name: WCFG-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WCFG-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WCFG_USD(NamedTuple):
    """
        name: WCFG-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WCFG-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WCFG_USDT(NamedTuple):
    """
        name: WCFG-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WCFG-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WLUNA_EUR(NamedTuple):
    """
        name: WLUNA-EUR
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WLUNA-EUR"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WLUNA_GBP(NamedTuple):
    """
        name: WLUNA-GBP
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WLUNA-GBP"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WLUNA_USD(NamedTuple):
    """
        name: WLUNA-USD
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WLUNA-USD"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class WLUNA_USDT(NamedTuple):
    """
        name: WLUNA-USDT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "WLUNA-USDT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XCN_USD(NamedTuple):
    """
        name: XCN-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XCN-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XCN_USDT(NamedTuple):
    """
        name: XCN-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XCN-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XLM_BTC(NamedTuple):
    """
        name: XLM-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XLM-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XLM_EUR(NamedTuple):
    """
        name: XLM-EUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XLM-EUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XLM_USD(NamedTuple):
    """
        name: XLM-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XLM-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XLM_USDT(NamedTuple):
    """
        name: XLM-USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XLM-USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XRP_BTC(NamedTuple):
    """
        name: XRP-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.001
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XRP-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.001
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XRP_EUR(NamedTuple):
    """
        name: XRP-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XRP-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XRP_GBP(NamedTuple):
    """
        name: XRP-GBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XRP-GBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XRP_USD(NamedTuple):
    """
        name: XRP-USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XRP-USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XTZ_BTC(NamedTuple):
    """
        name: XTZ-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XTZ-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XTZ_EUR(NamedTuple):
    """
        name: XTZ-EUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XTZ-EUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XTZ_GBP(NamedTuple):
    """
        name: XTZ-GBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.72
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XTZ-GBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.72
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.72
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XTZ_USD(NamedTuple):
    """
        name: XTZ-USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XTZ-USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XYO_BTC(NamedTuple):
    """
        name: XYO-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XYO-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XYO_EUR(NamedTuple):
    """
        name: XYO-EUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XYO-EUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XYO_USD(NamedTuple):
    """
        name: XYO-USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XYO-USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class XYO_USDT(NamedTuple):
    """
        name: XYO-USDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "XYO-USDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class YFI_BTC(NamedTuple):
    """
        name: YFI-BTC
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00001
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "YFI-BTC"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00001
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class YFI_USD(NamedTuple):
    """
        name: YFI-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "YFI-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class YFII_USD(NamedTuple):
    """
        name: YFII-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "YFII-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ZEC_BTC(NamedTuple):
    """
        name: ZEC-BTC
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ZEC-BTC"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ZEC_USD(NamedTuple):
    """
        name: ZEC-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ZEC-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ZEC_USDC(NamedTuple):
    """
        name: ZEC-USDC
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ZEC-USDC"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ZEN_BTC(NamedTuple):
    """
        name: ZEN-BTC
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ZEN-BTC"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ZEN_USD(NamedTuple):
    """
        name: ZEN-USD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ZEN-USD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ZEN_USDT(NamedTuple):
    """
        name: ZEN-USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ZEN-USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ZRX_BTC(NamedTuple):
    """
        name: ZRX-BTC
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.000016
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ZRX-BTC"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.000016
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.000016
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ZRX_EUR(NamedTuple):
    """
        name: ZRX-EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.84
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ZRX-EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.84
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.84
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""


class ZRX_USD(NamedTuple):
    """
        name: ZRX-USD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: coinbase
    """
    name: str = "ZRX-USD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "coinbase"

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
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: coinbase
"""
