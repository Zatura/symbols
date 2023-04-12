from typing import NamedTuple


class ONEINCH_USD(NamedTuple):
    """
        name: t1INCH:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "t1INCH:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "t1INCH:USD"

    def __str__(self):
        return "t1INCH:USD"

    def __call__(self):
        return "t1INCH:USD"


ONEINCH_USD = ONEINCH_USD()
"""
    name: t1INCH:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class ONEINCH_UST(NamedTuple):
    """
        name: t1INCH:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "t1INCH:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "t1INCH:UST"

    def __str__(self):
        return "t1INCH:UST"

    def __call__(self):
        return "t1INCH:UST"


ONEINCH_UST = ONEINCH_UST()
"""
    name: t1INCH:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class AAABBB(NamedTuple):
    """
        name: tAAABBB
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAAABBB"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAAABBB"

    def __str__(self):
        return "tAAABBB"

    def __call__(self):
        return "tAAABBB"


AAABBB = AAABBB()
"""
    name: tAAABBB
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100.0
    has_margin: False
    exchange: bitfinex
"""


class AAVE_USD(NamedTuple):
    """
        name: tAAVE:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAAVE:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAAVE:USD"

    def __str__(self):
        return "tAAVE:USD"

    def __call__(self):
        return "tAAVE:USD"


AAVE_USD = AAVE_USD()
"""
    name: tAAVE:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: False
    exchange: bitfinex
"""


class AAVE_UST(NamedTuple):
    """
        name: tAAVE:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAAVE:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAAVE:UST"

    def __str__(self):
        return "tAAVE:UST"

    def __call__(self):
        return "tAAVE:UST"


AAVE_UST = AAVE_UST()
"""
    name: tAAVE:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: False
    exchange: bitfinex
"""


class AAVEF0_USTF0(NamedTuple):
    """
        name: tAAVEF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAAVEF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAAVEF0:USTF0"

    def __str__(self):
        return "tAAVEF0:USTF0"

    def __call__(self):
        return "tAAVEF0:USTF0"


AAVEF0_USTF0 = AAVEF0_USTF0()
"""
    name: tAAVEF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class ADABTC(NamedTuple):
    """
        name: tADABTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tADABTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tADABTC"

    def __str__(self):
        return "tADABTC"

    def __call__(self):
        return "tADABTC"


ADABTC = ADABTC()
"""
    name: tADABTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class ADAF0_USTF0(NamedTuple):
    """
        name: tADAF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tADAF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 4.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tADAF0:USTF0"

    def __str__(self):
        return "tADAF0:USTF0"

    def __call__(self):
        return "tADAF0:USTF0"


ADAF0_USTF0 = ADAF0_USTF0()
"""
    name: tADAF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 4.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class ADAUSD(NamedTuple):
    """
        name: tADAUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tADAUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tADAUSD"

    def __str__(self):
        return "tADAUSD"

    def __call__(self):
        return "tADAUSD"


ADAUSD = ADAUSD()
"""
    name: tADAUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class ADAUST(NamedTuple):
    """
        name: tADAUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tADAUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tADAUST"

    def __str__(self):
        return "tADAUST"

    def __call__(self):
        return "tADAUST"


ADAUST = ADAUST()
"""
    name: tADAUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class AIXUSD(NamedTuple):
    """
        name: tAIXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 570.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAIXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 570.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAIXUSD"

    def __str__(self):
        return "tAIXUSD"

    def __call__(self):
        return "tAIXUSD"


AIXUSD = AIXUSD()
"""
    name: tAIXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 570.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class AIXUST(NamedTuple):
    """
        name: tAIXUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 570.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAIXUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 570.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAIXUST"

    def __str__(self):
        return "tAIXUST"

    def __call__(self):
        return "tAIXUST"


AIXUST = AIXUST()
"""
    name: tAIXUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 570.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class ALGBTC(NamedTuple):
    """
        name: tALGBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 150000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tALGBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 150000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tALGBTC"

    def __str__(self):
        return "tALGBTC"

    def __call__(self):
        return "tALGBTC"


ALGBTC = ALGBTC()
"""
    name: tALGBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 150000.0
    has_margin: False
    exchange: bitfinex
"""


class ALGF0_USTF0(NamedTuple):
    """
        name: tALGF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tALGF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 6.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tALGF0:USTF0"

    def __str__(self):
        return "tALGF0:USTF0"

    def __call__(self):
        return "tALGF0:USTF0"


ALGF0_USTF0 = ALGF0_USTF0()
"""
    name: tALGF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 6.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class ALGUSD(NamedTuple):
    """
        name: tALGUSD
        precision: 5
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 6.0
        max_order_size: 150000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tALGUSD"
    precision: int = 5
    min_margin: float = 25.0
    initial_margin: float = 50.0
    min_order_size: float = 6.0
    max_order_size: float = 150000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tALGUSD"

    def __str__(self):
        return "tALGUSD"

    def __call__(self):
        return "tALGUSD"


ALGUSD = ALGUSD()
"""
    name: tALGUSD
    precision: 5
    min_margin: 25.0
    initial_margin: 50.0
    min_order_size: 6.0
    max_order_size: 150000.0
    has_margin: True
    exchange: bitfinex
"""


class ALGUST(NamedTuple):
    """
        name: tALGUST
        precision: 5
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 6.0
        max_order_size: 150000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tALGUST"
    precision: int = 5
    min_margin: float = 25.0
    initial_margin: float = 50.0
    min_order_size: float = 6.0
    max_order_size: float = 150000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tALGUST"

    def __str__(self):
        return "tALGUST"

    def __call__(self):
        return "tALGUST"


ALGUST = ALGUST()
"""
    name: tALGUST
    precision: 5
    min_margin: 25.0
    initial_margin: 50.0
    min_order_size: 6.0
    max_order_size: 150000.0
    has_margin: True
    exchange: bitfinex
"""


class AMPBTC(NamedTuple):
    """
        name: tAMPBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAMPBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 25000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAMPBTC"

    def __str__(self):
        return "tAMPBTC"

    def __call__(self):
        return "tAMPBTC"


AMPBTC = AMPBTC()
"""
    name: tAMPBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 25000.0
    has_margin: False
    exchange: bitfinex
"""


class AMPF0_USTF0(NamedTuple):
    """
        name: tAMPF0:USTF0
        precision: 5
        min_margin: 2.5
        initial_margin: 5.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAMPF0:USTF0"
    precision: int = 5
    min_margin: float = 2.5
    initial_margin: float = 5.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAMPF0:USTF0"

    def __str__(self):
        return "tAMPF0:USTF0"

    def __call__(self):
        return "tAMPF0:USTF0"


AMPF0_USTF0 = AMPF0_USTF0()
"""
    name: tAMPF0:USTF0
    precision: 5
    min_margin: 2.5
    initial_margin: 5.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class AMPUSD(NamedTuple):
    """
        name: tAMPUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAMPUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 25000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAMPUSD"

    def __str__(self):
        return "tAMPUSD"

    def __call__(self):
        return "tAMPUSD"


AMPUSD = AMPUSD()
"""
    name: tAMPUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 25000.0
    has_margin: False
    exchange: bitfinex
"""


class AMPUST(NamedTuple):
    """
        name: tAMPUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAMPUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 25000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAMPUST"

    def __str__(self):
        return "tAMPUST"

    def __call__(self):
        return "tAMPUST"


AMPUST = AMPUST()
"""
    name: tAMPUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 25000.0
    has_margin: False
    exchange: bitfinex
"""


class ANTBTC(NamedTuple):
    """
        name: tANTBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tANTBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tANTBTC"

    def __str__(self):
        return "tANTBTC"

    def __call__(self):
        return "tANTBTC"


ANTBTC = ANTBTC()
"""
    name: tANTBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class ANTUSD(NamedTuple):
    """
        name: tANTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tANTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tANTUSD"

    def __str__(self):
        return "tANTUSD"

    def __call__(self):
        return "tANTUSD"


ANTUSD = ANTUSD()
"""
    name: tANTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class APEF0_USTF0(NamedTuple):
    """
        name: tAPEF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPEF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.4
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAPEF0:USTF0"

    def __str__(self):
        return "tAPEF0:USTF0"

    def __call__(self):
        return "tAPEF0:USTF0"


APEF0_USTF0 = APEF0_USTF0()
"""
    name: tAPEF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.4
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class APENFT_USD(NamedTuple):
    """
        name: tAPENFT:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 40000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAPENFT:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 40000000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAPENFT:USD"

    def __str__(self):
        return "tAPENFT:USD"

    def __call__(self):
        return "tAPENFT:USD"


APENFT_USD = APENFT_USD()
"""
    name: tAPENFT:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 40000000000.0
    has_margin: False
    exchange: bitfinex
"""


class APENFT_UST(NamedTuple):
    """
        name: tAPENFT:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 40000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAPENFT:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 40000000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAPENFT:UST"

    def __str__(self):
        return "tAPENFT:UST"

    def __call__(self):
        return "tAPENFT:UST"


APENFT_UST = APENFT_UST()
"""
    name: tAPENFT:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 40000000000.0
    has_margin: False
    exchange: bitfinex
"""


class APEUSD(NamedTuple):
    """
        name: tAPEUSD
        precision: 5
        min_margin: 30.0
        initial_margin: 60.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPEUSD"
    precision: int = 5
    min_margin: float = 30.0
    initial_margin: float = 60.0
    min_order_size: float = 0.4
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAPEUSD"

    def __str__(self):
        return "tAPEUSD"

    def __call__(self):
        return "tAPEUSD"


APEUSD = APEUSD()
"""
    name: tAPEUSD
    precision: 5
    min_margin: 30.0
    initial_margin: 60.0
    min_order_size: 0.4
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class APEUST(NamedTuple):
    """
        name: tAPEUST
        precision: 5
        min_margin: 30.0
        initial_margin: 60.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPEUST"
    precision: int = 5
    min_margin: float = 30.0
    initial_margin: float = 60.0
    min_order_size: float = 0.4
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAPEUST"

    def __str__(self):
        return "tAPEUST"

    def __call__(self):
        return "tAPEUST"


APEUST = APEUST()
"""
    name: tAPEUST
    precision: 5
    min_margin: 30.0
    initial_margin: 60.0
    min_order_size: 0.4
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class APTF0_USTF0(NamedTuple):
    """
        name: tAPTF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 30000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPTF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 30000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAPTF0:USTF0"

    def __str__(self):
        return "tAPTF0:USTF0"

    def __call__(self):
        return "tAPTF0:USTF0"


APTF0_USTF0 = APTF0_USTF0()
"""
    name: tAPTF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 30000.0
    has_margin: True
    exchange: bitfinex
"""


class APTUSD(NamedTuple):
    """
        name: tAPTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 30000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 30000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAPTUSD"

    def __str__(self):
        return "tAPTUSD"

    def __call__(self):
        return "tAPTUSD"


APTUSD = APTUSD()
"""
    name: tAPTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 30000.0
    has_margin: True
    exchange: bitfinex
"""


class APTUST(NamedTuple):
    """
        name: tAPTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 30000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 30000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAPTUST"

    def __str__(self):
        return "tAPTUST"

    def __call__(self):
        return "tAPTUST"


APTUST = APTUST()
"""
    name: tAPTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 30000.0
    has_margin: True
    exchange: bitfinex
"""


class ARBF0_USTF0(NamedTuple):
    """
        name: tARBF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tARBF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 75000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tARBF0:USTF0"

    def __str__(self):
        return "tARBF0:USTF0"

    def __call__(self):
        return "tARBF0:USTF0"


ARBF0_USTF0 = ARBF0_USTF0()
"""
    name: tARBF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 75000.0
    has_margin: True
    exchange: bitfinex
"""


class ARBUSD(NamedTuple):
    """
        name: tARBUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tARBUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 75000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tARBUSD"

    def __str__(self):
        return "tARBUSD"

    def __call__(self):
        return "tARBUSD"


ARBUSD = ARBUSD()
"""
    name: tARBUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 75000.0
    has_margin: False
    exchange: bitfinex
"""


class ARBUST(NamedTuple):
    """
        name: tARBUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tARBUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 75000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tARBUST"

    def __str__(self):
        return "tARBUST"

    def __call__(self):
        return "tARBUST"


ARBUST = ARBUST()
"""
    name: tARBUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 75000.0
    has_margin: False
    exchange: bitfinex
"""


class ATLAS_USD(NamedTuple):
    """
        name: tATLAS:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 232.0
        max_order_size: 25000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tATLAS:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 232.0
    max_order_size: float = 25000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tATLAS:USD"

    def __str__(self):
        return "tATLAS:USD"

    def __call__(self):
        return "tATLAS:USD"


ATLAS_USD = ATLAS_USD()
"""
    name: tATLAS:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 232.0
    max_order_size: 25000000.0
    has_margin: False
    exchange: bitfinex
"""


class ATLAS_UST(NamedTuple):
    """
        name: tATLAS:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 232.0
        max_order_size: 25000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tATLAS:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 232.0
    max_order_size: float = 25000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tATLAS:UST"

    def __str__(self):
        return "tATLAS:UST"

    def __call__(self):
        return "tATLAS:UST"


ATLAS_UST = ATLAS_UST()
"""
    name: tATLAS:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 232.0
    max_order_size: 25000000.0
    has_margin: False
    exchange: bitfinex
"""


class ATOBTC(NamedTuple):
    """
        name: tATOBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tATOBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tATOBTC"

    def __str__(self):
        return "tATOBTC"

    def __call__(self):
        return "tATOBTC"


ATOBTC = ATOBTC()
"""
    name: tATOBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class ATOETH(NamedTuple):
    """
        name: tATOETH
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tATOETH"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tATOETH"

    def __str__(self):
        return "tATOETH"

    def __call__(self):
        return "tATOETH"


ATOETH = ATOETH()
"""
    name: tATOETH
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class ATOF0_USTF0(NamedTuple):
    """
        name: tATOF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tATOF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.2
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tATOF0:USTF0"

    def __str__(self):
        return "tATOF0:USTF0"

    def __call__(self):
        return "tATOF0:USTF0"


ATOF0_USTF0 = ATOF0_USTF0()
"""
    name: tATOF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.2
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class ATOUSD(NamedTuple):
    """
        name: tATOUSD
        precision: 5
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tATOUSD"
    precision: int = 5
    min_margin: float = 25.0
    initial_margin: float = 50.0
    min_order_size: float = 0.2
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tATOUSD"

    def __str__(self):
        return "tATOUSD"

    def __call__(self):
        return "tATOUSD"


ATOUSD = ATOUSD()
"""
    name: tATOUSD
    precision: 5
    min_margin: 25.0
    initial_margin: 50.0
    min_order_size: 0.2
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class ATOUST(NamedTuple):
    """
        name: tATOUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tATOUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tATOUST"

    def __str__(self):
        return "tATOUST"

    def __call__(self):
        return "tATOUST"


ATOUST = ATOUST()
"""
    name: tATOUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class AUSTRALIA200IXF0_USTF0(NamedTuple):
    """
        name: tAUSTRALIA200IXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAUSTRALIA200IXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 10.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAUSTRALIA200IXF0:USTF0"

    def __str__(self):
        return "tAUSTRALIA200IXF0:USTF0"

    def __call__(self):
        return "tAUSTRALIA200IXF0:USTF0"


AUSTRALIA200IXF0_USTF0 = AUSTRALIA200IXF0_USTF0()
"""
    name: tAUSTRALIA200IXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 10.0
    has_margin: True
    exchange: bitfinex
"""


class AVAX_BTC(NamedTuple):
    """
        name: tAVAX:BTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.08
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAX:BTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.08
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAVAX:BTC"

    def __str__(self):
        return "tAVAX:BTC"

    def __call__(self):
        return "tAVAX:BTC"


AVAX_BTC = AVAX_BTC()
"""
    name: tAVAX:BTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.08
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class AVAX_USD(NamedTuple):
    """
        name: tAVAX:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.08
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAX:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.08
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAVAX:USD"

    def __str__(self):
        return "tAVAX:USD"

    def __call__(self):
        return "tAVAX:USD"


AVAX_USD = AVAX_USD()
"""
    name: tAVAX:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.08
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class AVAX_UST(NamedTuple):
    """
        name: tAVAX:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.08
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAX:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.08
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAVAX:UST"

    def __str__(self):
        return "tAVAX:UST"

    def __call__(self):
        return "tAVAX:UST"


AVAX_UST = AVAX_UST()
"""
    name: tAVAX:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.08
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class AVAXF0_BTCF0(NamedTuple):
    """
        name: tAVAXF0:BTCF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.08
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAXF0:BTCF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.08
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAVAXF0:BTCF0"

    def __str__(self):
        return "tAVAXF0:BTCF0"

    def __call__(self):
        return "tAVAXF0:BTCF0"


AVAXF0_BTCF0 = AVAXF0_BTCF0()
"""
    name: tAVAXF0:BTCF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.08
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class AVAXF0_USTF0(NamedTuple):
    """
        name: tAVAXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.08
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.08
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAVAXF0:USTF0"

    def __str__(self):
        return "tAVAXF0:USTF0"

    def __call__(self):
        return "tAVAXF0:USTF0"


AVAXF0_USTF0 = AVAXF0_USTF0()
"""
    name: tAVAXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.08
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class AXSF0_USTF0(NamedTuple):
    """
        name: tAXSF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAXSF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAXSF0:USTF0"

    def __str__(self):
        return "tAXSF0:USTF0"

    def __call__(self):
        return "tAXSF0:USTF0"


AXSF0_USTF0 = AXSF0_USTF0()
"""
    name: tAXSF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class AXSUSD(NamedTuple):
    """
        name: tAXSUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAXSUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAXSUSD"

    def __str__(self):
        return "tAXSUSD"

    def __call__(self):
        return "tAXSUSD"


AXSUSD = AXSUSD()
"""
    name: tAXSUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class AXSUST(NamedTuple):
    """
        name: tAXSUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAXSUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tAXSUST"

    def __str__(self):
        return "tAXSUST"

    def __call__(self):
        return "tAXSUST"


AXSUST = AXSUST()
"""
    name: tAXSUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class B2MUSD(NamedTuple):
    """
        name: tB2MUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 144.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tB2MUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 144.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tB2MUSD"

    def __str__(self):
        return "tB2MUSD"

    def __call__(self):
        return "tB2MUSD"


B2MUSD = B2MUSD()
"""
    name: tB2MUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 144.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class B2MUST(NamedTuple):
    """
        name: tB2MUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 144.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tB2MUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 144.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tB2MUST"

    def __str__(self):
        return "tB2MUST"

    def __call__(self):
        return "tB2MUST"


B2MUST = B2MUST()
"""
    name: tB2MUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 144.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class BALUSD(NamedTuple):
    """
        name: tBALUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBALUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBALUSD"

    def __str__(self):
        return "tBALUSD"

    def __call__(self):
        return "tBALUSD"


BALUSD = BALUSD()
"""
    name: tBALUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class BALUST(NamedTuple):
    """
        name: tBALUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBALUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBALUST"

    def __str__(self):
        return "tBALUST"

    def __call__(self):
        return "tBALUST"


BALUST = BALUST()
"""
    name: tBALUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class BAND_USD(NamedTuple):
    """
        name: tBAND:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBAND:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBAND:USD"

    def __str__(self):
        return "tBAND:USD"

    def __call__(self):
        return "tBAND:USD"


BAND_USD = BAND_USD()
"""
    name: tBAND:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class BAND_UST(NamedTuple):
    """
        name: tBAND:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBAND:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBAND:UST"

    def __str__(self):
        return "tBAND:UST"

    def __call__(self):
        return "tBAND:UST"


BAND_UST = BAND_UST()
"""
    name: tBAND:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class BATUSD(NamedTuple):
    """
        name: tBATUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBATUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 200000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBATUSD"

    def __str__(self):
        return "tBATUSD"

    def __call__(self):
        return "tBATUSD"


BATUSD = BATUSD()
"""
    name: tBATUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 200000.0
    has_margin: False
    exchange: bitfinex
"""


class BATUST(NamedTuple):
    """
        name: tBATUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBATUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 200000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBATUST"

    def __str__(self):
        return "tBATUST"

    def __call__(self):
        return "tBATUST"


BATUST = BATUST()
"""
    name: tBATUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 200000.0
    has_margin: False
    exchange: bitfinex
"""


class BCHABC_USD(NamedTuple):
    """
        name: tBCHABC:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 40962.0
        max_order_size: 1000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBCHABC:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 40962.0
    max_order_size: float = 1000000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBCHABC:USD"

    def __str__(self):
        return "tBCHABC:USD"

    def __call__(self):
        return "tBCHABC:USD"


BCHABC_USD = BCHABC_USD()
"""
    name: tBCHABC:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 40962.0
    max_order_size: 1000000000.0
    has_margin: False
    exchange: bitfinex
"""


class BCHN_USD(NamedTuple):
    """
        name: tBCHN:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBCHN:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 1000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBCHN:USD"

    def __str__(self):
        return "tBCHN:USD"

    def __call__(self):
        return "tBCHN:USD"


BCHN_USD = BCHN_USD()
"""
    name: tBCHN:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 1000.0
    has_margin: True
    exchange: bitfinex
"""


class BEST_USD(NamedTuple):
    """
        name: tBEST:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBEST:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBEST:USD"

    def __str__(self):
        return "tBEST:USD"

    def __call__(self):
        return "tBEST:USD"


BEST_USD = BEST_USD()
"""
    name: tBEST:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class BLUR_USD(NamedTuple):
    """
        name: tBLUR:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBLUR:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 75000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBLUR:USD"

    def __str__(self):
        return "tBLUR:USD"

    def __call__(self):
        return "tBLUR:USD"


BLUR_USD = BLUR_USD()
"""
    name: tBLUR:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 75000.0
    has_margin: False
    exchange: bitfinex
"""


class BLUR_UST(NamedTuple):
    """
        name: tBLUR:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBLUR:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 75000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBLUR:UST"

    def __str__(self):
        return "tBLUR:UST"

    def __call__(self):
        return "tBLUR:UST"


BLUR_UST = BLUR_UST()
"""
    name: tBLUR:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 75000.0
    has_margin: False
    exchange: bitfinex
"""


class BMNBTC(NamedTuple):
    """
        name: tBMNBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00002
        max_order_size: 1.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBMNBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00002
    max_order_size: float = 1.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBMNBTC"

    def __str__(self):
        return "tBMNBTC"

    def __call__(self):
        return "tBMNBTC"


BMNBTC = BMNBTC()
"""
    name: tBMNBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00002
    max_order_size: 1.0
    has_margin: False
    exchange: bitfinex
"""


class BMNUSD(NamedTuple):
    """
        name: tBMNUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00002
        max_order_size: 1.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBMNUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00002
    max_order_size: float = 1.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBMNUSD"

    def __str__(self):
        return "tBMNUSD"

    def __call__(self):
        return "tBMNUSD"


BMNUSD = BMNUSD()
"""
    name: tBMNUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00002
    max_order_size: 1.0
    has_margin: False
    exchange: bitfinex
"""


class BNTUSD(NamedTuple):
    """
        name: tBNTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBNTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 20000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBNTUSD"

    def __str__(self):
        return "tBNTUSD"

    def __call__(self):
        return "tBNTUSD"


BNTUSD = BNTUSD()
"""
    name: tBNTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 20000.0
    has_margin: False
    exchange: bitfinex
"""


class BOBA_USD(NamedTuple):
    """
        name: tBOBA:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOBA:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBOBA:USD"

    def __str__(self):
        return "tBOBA:USD"

    def __call__(self):
        return "tBOBA:USD"


BOBA_USD = BOBA_USD()
"""
    name: tBOBA:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class BOBA_UST(NamedTuple):
    """
        name: tBOBA:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOBA:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBOBA:UST"

    def __str__(self):
        return "tBOBA:UST"

    def __call__(self):
        return "tBOBA:UST"


BOBA_UST = BOBA_UST()
"""
    name: tBOBA:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class BOOUSD(NamedTuple):
    """
        name: tBOOUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 45000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOOUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 45000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBOOUSD"

    def __str__(self):
        return "tBOOUSD"

    def __call__(self):
        return "tBOOUSD"


BOOUSD = BOOUSD()
"""
    name: tBOOUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 45000.0
    has_margin: False
    exchange: bitfinex
"""


class BOOUST(NamedTuple):
    """
        name: tBOOUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 45000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOOUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 45000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBOOUST"

    def __str__(self):
        return "tBOOUST"

    def __call__(self):
        return "tBOOUST"


BOOUST = BOOUST()
"""
    name: tBOOUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 45000.0
    has_margin: False
    exchange: bitfinex
"""


class BOSON_USD(NamedTuple):
    """
        name: tBOSON:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOSON:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBOSON:USD"

    def __str__(self):
        return "tBOSON:USD"

    def __call__(self):
        return "tBOSON:USD"


BOSON_USD = BOSON_USD()
"""
    name: tBOSON:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class BOSON_UST(NamedTuple):
    """
        name: tBOSON:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOSON:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBOSON:UST"

    def __str__(self):
        return "tBOSON:UST"

    def __call__(self):
        return "tBOSON:UST"


BOSON_UST = BOSON_UST()
"""
    name: tBOSON:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class BRISE_USD(NamedTuple):
    """
        name: tBRISE:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBRISE:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBRISE:USD"

    def __str__(self):
        return "tBRISE:USD"

    def __call__(self):
        return "tBRISE:USD"


BRISE_USD = BRISE_USD()
"""
    name: tBRISE:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000000000.0
    has_margin: False
    exchange: bitfinex
"""


class BRISE_UST(NamedTuple):
    """
        name: tBRISE:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBRISE:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBRISE:UST"

    def __str__(self):
        return "tBRISE:UST"

    def __call__(self):
        return "tBRISE:UST"


BRISE_UST = BRISE_UST()
"""
    name: tBRISE:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000000000.0
    has_margin: False
    exchange: bitfinex
"""


class BTC_CNHT(NamedTuple):
    """
        name: tBTC:CNHT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTC:CNHT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00006
    max_order_size: float = 5000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTC:CNHT"

    def __str__(self):
        return "tBTC:CNHT"

    def __call__(self):
        return "tBTC:CNHT"


BTC_CNHT = BTC_CNHT()
"""
    name: tBTC:CNHT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00006
    max_order_size: 5000.0
    has_margin: False
    exchange: bitfinex
"""


class BTC_MXNT(NamedTuple):
    """
        name: tBTC:MXNT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTC:MXNT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 500.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTC:MXNT"

    def __str__(self):
        return "tBTC:MXNT"

    def __call__(self):
        return "tBTC:MXNT"


BTC_MXNT = BTC_MXNT()
"""
    name: tBTC:MXNT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 500.0
    has_margin: False
    exchange: bitfinex
"""


class BTC_XAUT(NamedTuple):
    """
        name: tBTC:XAUT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.0002
        max_order_size: 250.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTC:XAUT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.0002
    max_order_size: float = 250.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTC:XAUT"

    def __str__(self):
        return "tBTC:XAUT"

    def __call__(self):
        return "tBTC:XAUT"


BTC_XAUT = BTC_XAUT()
"""
    name: tBTC:XAUT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.0002
    max_order_size: 250.0
    has_margin: False
    exchange: bitfinex
"""


class BTCDOMF0_USTF0(NamedTuple):
    """
        name: tBTCDOMF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.01
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCDOMF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.01
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCDOMF0:USTF0"

    def __str__(self):
        return "tBTCDOMF0:USTF0"

    def __call__(self):
        return "tBTCDOMF0:USTF0"


BTCDOMF0_USTF0 = BTCDOMF0_USTF0()
"""
    name: tBTCDOMF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.01
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class BTCEUR(NamedTuple):
    """
        name: tBTCEUR
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCEUR"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.00006
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCEUR"

    def __str__(self):
        return "tBTCEUR"

    def __call__(self):
        return "tBTCEUR"


BTCEUR = BTCEUR()
"""
    name: tBTCEUR
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.00006
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class BTCEUT(NamedTuple):
    """
        name: tBTCEUT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCEUT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00006
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCEUT"

    def __str__(self):
        return "tBTCEUT"

    def __call__(self):
        return "tBTCEUT"


BTCEUT = BTCEUT()
"""
    name: tBTCEUT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00006
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class BTCF0_EUTF0(NamedTuple):
    """
        name: tBTCF0:EUTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.0002
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCF0:EUTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.0002
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCF0:EUTF0"

    def __str__(self):
        return "tBTCF0:EUTF0"

    def __call__(self):
        return "tBTCF0:EUTF0"


BTCF0_EUTF0 = BTCF0_EUTF0()
"""
    name: tBTCF0:EUTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.0002
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class BTCF0_USTF0(NamedTuple):
    """
        name: tBTCF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.00006
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.00006
    max_order_size: float = 100.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCF0:USTF0"

    def __str__(self):
        return "tBTCF0:USTF0"

    def __call__(self):
        return "tBTCF0:USTF0"


BTCF0_USTF0 = BTCF0_USTF0()
"""
    name: tBTCF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.00006
    max_order_size: 100.0
    has_margin: True
    exchange: bitfinex
"""


class BTCGBP(NamedTuple):
    """
        name: tBTCGBP
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCGBP"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00006
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCGBP"

    def __str__(self):
        return "tBTCGBP"

    def __call__(self):
        return "tBTCGBP"


BTCGBP = BTCGBP()
"""
    name: tBTCGBP
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00006
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class BTCJPY(NamedTuple):
    """
        name: tBTCJPY
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCJPY"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00006
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCJPY"

    def __str__(self):
        return "tBTCJPY"

    def __call__(self):
        return "tBTCJPY"


BTCJPY = BTCJPY()
"""
    name: tBTCJPY
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00006
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class BTCMIM(NamedTuple):
    """
        name: tBTCMIM
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.0002
        max_order_size: 2500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTCMIM"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.0002
    max_order_size: float = 2500.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCMIM"

    def __str__(self):
        return "tBTCMIM"

    def __call__(self):
        return "tBTCMIM"


BTCMIM = BTCMIM()
"""
    name: tBTCMIM
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.0002
    max_order_size: 2500.0
    has_margin: False
    exchange: bitfinex
"""


class BTCTRY(NamedTuple):
    """
        name: tBTCTRY
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTCTRY"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCTRY"

    def __str__(self):
        return "tBTCTRY"

    def __call__(self):
        return "tBTCTRY"


BTCTRY = BTCTRY()
"""
    name: tBTCTRY
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class BTCUSD(NamedTuple):
    """
        name: tBTCUSD
        precision: 5
        min_margin: 5.0
        initial_margin: 10.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCUSD"
    precision: int = 5
    min_margin: float = 5.0
    initial_margin: float = 10.0
    min_order_size: float = 0.00006
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCUSD"

    def __str__(self):
        return "tBTCUSD"

    def __call__(self):
        return "tBTCUSD"


BTCUSD = BTCUSD()
"""
    name: tBTCUSD
    precision: 5
    min_margin: 5.0
    initial_margin: 10.0
    min_order_size: 0.00006
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class BTCUST(NamedTuple):
    """
        name: tBTCUST
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCUST"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.00006
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTCUST"

    def __str__(self):
        return "tBTCUST"

    def __call__(self):
        return "tBTCUST"


BTCUST = BTCUST()
"""
    name: tBTCUST
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.00006
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class BTGBTC(NamedTuple):
    """
        name: tBTGBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTGBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.1
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTGBTC"

    def __str__(self):
        return "tBTGBTC"

    def __call__(self):
        return "tBTGBTC"


BTGBTC = BTGBTC()
"""
    name: tBTGBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.1
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class BTGUSD(NamedTuple):
    """
        name: tBTGUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTGUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.1
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTGUSD"

    def __str__(self):
        return "tBTGUSD"

    def __call__(self):
        return "tBTGUSD"


BTGUSD = BTGUSD()
"""
    name: tBTGUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.1
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class BTSE_USD(NamedTuple):
    """
        name: tBTSE:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTSE:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTSE:USD"

    def __str__(self):
        return "tBTSE:USD"

    def __call__(self):
        return "tBTSE:USD"


BTSE_USD = BTSE_USD()
"""
    name: tBTSE:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class BTTUSD(NamedTuple):
    """
        name: tBTTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1970444.0
        max_order_size: 25000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 1970444.0
    max_order_size: float = 25000000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBTTUSD"

    def __str__(self):
        return "tBTTUSD"

    def __call__(self):
        return "tBTTUSD"


BTTUSD = BTTUSD()
"""
    name: tBTTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 1970444.0
    max_order_size: 25000000000.0
    has_margin: False
    exchange: bitfinex
"""


class CCDBTC(NamedTuple):
    """
        name: tCCDBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 100.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCCDBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 100.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCCDBTC"

    def __str__(self):
        return "tCCDBTC"

    def __call__(self):
        return "tCCDBTC"


CCDBTC = CCDBTC()
"""
    name: tCCDBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 100.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class CCDUSD(NamedTuple):
    """
        name: tCCDUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 100.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCCDUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 100.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCCDUSD"

    def __str__(self):
        return "tCCDUSD"

    def __call__(self):
        return "tCCDUSD"


CCDUSD = CCDUSD()
"""
    name: tCCDUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 100.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class CCDUST(NamedTuple):
    """
        name: tCCDUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 100.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCCDUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 100.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCCDUST"

    def __str__(self):
        return "tCCDUST"

    def __call__(self):
        return "tCCDUST"


CCDUST = CCDUST()
"""
    name: tCCDUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 100.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class CHEX_USD(NamedTuple):
    """
        name: tCHEX:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 88.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHEX:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 88.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCHEX:USD"

    def __str__(self):
        return "tCHEX:USD"

    def __call__(self):
        return "tCHEX:USD"


CHEX_USD = CHEX_USD()
"""
    name: tCHEX:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 88.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class CHSB_BTC(NamedTuple):
    """
        name: tCHSB:BTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHSB:BTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 8.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCHSB:BTC"

    def __str__(self):
        return "tCHSB:BTC"

    def __call__(self):
        return "tCHSB:BTC"


CHSB_BTC = CHSB_BTC()
"""
    name: tCHSB:BTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 8.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class CHSB_USD(NamedTuple):
    """
        name: tCHSB:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHSB:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 8.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCHSB:USD"

    def __str__(self):
        return "tCHSB:USD"

    def __call__(self):
        return "tCHSB:USD"


CHSB_USD = CHSB_USD()
"""
    name: tCHSB:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 8.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class CHSB_UST(NamedTuple):
    """
        name: tCHSB:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHSB:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 8.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCHSB:UST"

    def __str__(self):
        return "tCHSB:UST"

    def __call__(self):
        return "tCHSB:UST"


CHSB_UST = CHSB_UST()
"""
    name: tCHSB:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 8.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class CHZUSD(NamedTuple):
    """
        name: tCHZUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 16.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHZUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 16.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCHZUSD"

    def __str__(self):
        return "tCHZUSD"

    def __call__(self):
        return "tCHZUSD"


CHZUSD = CHZUSD()
"""
    name: tCHZUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 16.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class CHZUST(NamedTuple):
    """
        name: tCHZUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 16.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHZUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 16.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCHZUST"

    def __str__(self):
        return "tCHZUST"

    def __call__(self):
        return "tCHZUST"


CHZUST = CHZUST()
"""
    name: tCHZUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 16.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class CLOUSD(NamedTuple):
    """
        name: tCLOUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 624.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCLOUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 624.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCLOUSD"

    def __str__(self):
        return "tCLOUSD"

    def __call__(self):
        return "tCLOUSD"


CLOUSD = CLOUSD()
"""
    name: tCLOUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 624.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class CNH_CNHT(NamedTuple):
    """
        name: tCNH:CNHT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCNH:CNHT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 14.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCNH:CNHT"

    def __str__(self):
        return "tCNH:CNHT"

    def __call__(self):
        return "tCNH:CNHT"


CNH_CNHT = CNH_CNHT()
"""
    name: tCNH:CNHT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 14.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class COMP_USD(NamedTuple):
    """
        name: tCOMP:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tCOMP:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.04
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCOMP:USD"

    def __str__(self):
        return "tCOMP:USD"

    def __call__(self):
        return "tCOMP:USD"


COMP_USD = COMP_USD()
"""
    name: tCOMP:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.04
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class COMP_UST(NamedTuple):
    """
        name: tCOMP:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tCOMP:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.04
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCOMP:UST"

    def __str__(self):
        return "tCOMP:UST"

    def __call__(self):
        return "tCOMP:UST"


COMP_UST = COMP_UST()
"""
    name: tCOMP:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.04
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class COMPF0_USTF0(NamedTuple):
    """
        name: tCOMPF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tCOMPF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.04
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCOMPF0:USTF0"

    def __str__(self):
        return "tCOMPF0:USTF0"

    def __call__(self):
        return "tCOMPF0:USTF0"


COMPF0_USTF0 = COMPF0_USTF0()
"""
    name: tCOMPF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.04
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class CONV_USD(NamedTuple):
    """
        name: tCONV:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCONV:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 50000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCONV:USD"

    def __str__(self):
        return "tCONV:USD"

    def __call__(self):
        return "tCONV:USD"


CONV_USD = CONV_USD()
"""
    name: tCONV:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 50000000.0
    has_margin: False
    exchange: bitfinex
"""


class CONV_UST(NamedTuple):
    """
        name: tCONV:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCONV:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 50000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCONV:UST"

    def __str__(self):
        return "tCONV:UST"

    def __call__(self):
        return "tCONV:UST"


CONV_UST = CONV_UST()
"""
    name: tCONV:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 50000000.0
    has_margin: False
    exchange: bitfinex
"""


class CRVF0_USTF0(NamedTuple):
    """
        name: tCRVF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tCRVF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCRVF0:USTF0"

    def __str__(self):
        return "tCRVF0:USTF0"

    def __call__(self):
        return "tCRVF0:USTF0"


CRVF0_USTF0 = CRVF0_USTF0()
"""
    name: tCRVF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class CRVUSD(NamedTuple):
    """
        name: tCRVUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCRVUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCRVUSD"

    def __str__(self):
        return "tCRVUSD"

    def __call__(self):
        return "tCRVUSD"


CRVUSD = CRVUSD()
"""
    name: tCRVUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class CRVUST(NamedTuple):
    """
        name: tCRVUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCRVUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tCRVUST"

    def __str__(self):
        return "tCRVUST"

    def __call__(self):
        return "tCRVUST"


CRVUST = CRVUST()
"""
    name: tCRVUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class DAIBTC(NamedTuple):
    """
        name: tDAIBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDAIBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 200000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDAIBTC"

    def __str__(self):
        return "tDAIBTC"

    def __call__(self):
        return "tDAIBTC"


DAIBTC = DAIBTC()
"""
    name: tDAIBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 200000.0
    has_margin: False
    exchange: bitfinex
"""


class DAIUSD(NamedTuple):
    """
        name: tDAIUSD
        precision: 5
        min_margin: 33.0
        initial_margin: 66.0
        min_order_size: 2.0
        max_order_size: 200000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDAIUSD"
    precision: int = 5
    min_margin: float = 33.0
    initial_margin: float = 66.0
    min_order_size: float = 2.0
    max_order_size: float = 200000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDAIUSD"

    def __str__(self):
        return "tDAIUSD"

    def __call__(self):
        return "tDAIUSD"


DAIUSD = DAIUSD()
"""
    name: tDAIUSD
    precision: 5
    min_margin: 33.0
    initial_margin: 66.0
    min_order_size: 2.0
    max_order_size: 200000.0
    has_margin: True
    exchange: bitfinex
"""


class DGBUSD(NamedTuple):
    """
        name: tDGBUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 184.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDGBUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 184.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDGBUSD"

    def __str__(self):
        return "tDGBUSD"

    def __call__(self):
        return "tDGBUSD"


DGBUSD = DGBUSD()
"""
    name: tDGBUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 184.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class DOGE_BTC(NamedTuple):
    """
        name: tDOGE:BTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 1500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOGE:BTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 26.0
    max_order_size: float = 1500000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDOGE:BTC"

    def __str__(self):
        return "tDOGE:BTC"

    def __call__(self):
        return "tDOGE:BTC"


DOGE_BTC = DOGE_BTC()
"""
    name: tDOGE:BTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 26.0
    max_order_size: 1500000.0
    has_margin: True
    exchange: bitfinex
"""


class DOGE_USD(NamedTuple):
    """
        name: tDOGE:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 1500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOGE:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 26.0
    max_order_size: float = 1500000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDOGE:USD"

    def __str__(self):
        return "tDOGE:USD"

    def __call__(self):
        return "tDOGE:USD"


DOGE_USD = DOGE_USD()
"""
    name: tDOGE:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 26.0
    max_order_size: 1500000.0
    has_margin: True
    exchange: bitfinex
"""


class DOGE_UST(NamedTuple):
    """
        name: tDOGE:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 1500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOGE:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 26.0
    max_order_size: float = 1500000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDOGE:UST"

    def __str__(self):
        return "tDOGE:UST"

    def __call__(self):
        return "tDOGE:UST"


DOGE_UST = DOGE_UST()
"""
    name: tDOGE:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 26.0
    max_order_size: 1500000.0
    has_margin: True
    exchange: bitfinex
"""


class DOGEF0_USTF0(NamedTuple):
    """
        name: tDOGEF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 26.0
        max_order_size: 1500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOGEF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 26.0
    max_order_size: float = 1500000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDOGEF0:USTF0"

    def __str__(self):
        return "tDOGEF0:USTF0"

    def __call__(self):
        return "tDOGEF0:USTF0"


DOGEF0_USTF0 = DOGEF0_USTF0()
"""
    name: tDOGEF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 26.0
    max_order_size: 1500000.0
    has_margin: True
    exchange: bitfinex
"""


class DORA_USD(NamedTuple):
    """
        name: tDORA:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDORA:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.8
    max_order_size: float = 25000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDORA:USD"

    def __str__(self):
        return "tDORA:USD"

    def __call__(self):
        return "tDORA:USD"


DORA_USD = DORA_USD()
"""
    name: tDORA:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.8
    max_order_size: 25000.0
    has_margin: False
    exchange: bitfinex
"""


class DORA_UST(NamedTuple):
    """
        name: tDORA:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDORA:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.8
    max_order_size: float = 25000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDORA:UST"

    def __str__(self):
        return "tDORA:UST"

    def __call__(self):
        return "tDORA:UST"


DORA_UST = DORA_UST()
"""
    name: tDORA:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.8
    max_order_size: 25000.0
    has_margin: False
    exchange: bitfinex
"""


class DOTBTC(NamedTuple):
    """
        name: tDOTBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDOTBTC"

    def __str__(self):
        return "tDOTBTC"

    def __call__(self):
        return "tDOTBTC"


DOTBTC = DOTBTC()
"""
    name: tDOTBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class DOTF0_BTCF0(NamedTuple):
    """
        name: tDOTF0:BTCF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTF0:BTCF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDOTF0:BTCF0"

    def __str__(self):
        return "tDOTF0:BTCF0"

    def __call__(self):
        return "tDOTF0:BTCF0"


DOTF0_BTCF0 = DOTF0_BTCF0()
"""
    name: tDOTF0:BTCF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class DOTF0_USTF0(NamedTuple):
    """
        name: tDOTF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDOTF0:USTF0"

    def __str__(self):
        return "tDOTF0:USTF0"

    def __call__(self):
        return "tDOTF0:USTF0"


DOTF0_USTF0 = DOTF0_USTF0()
"""
    name: tDOTF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class DOTUSD(NamedTuple):
    """
        name: tDOTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDOTUSD"

    def __str__(self):
        return "tDOTUSD"

    def __call__(self):
        return "tDOTUSD"


DOTUSD = DOTUSD()
"""
    name: tDOTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class DOTUST(NamedTuple):
    """
        name: tDOTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDOTUST"

    def __str__(self):
        return "tDOTUST"

    def __call__(self):
        return "tDOTUST"


DOTUST = DOTUST()
"""
    name: tDOTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class DSHBTC(NamedTuple):
    """
        name: tDSHBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDSHBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.04
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDSHBTC"

    def __str__(self):
        return "tDSHBTC"

    def __call__(self):
        return "tDSHBTC"


DSHBTC = DSHBTC()
"""
    name: tDSHBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.04
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class DSHUSD(NamedTuple):
    """
        name: tDSHUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDSHUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.04
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDSHUSD"

    def __str__(self):
        return "tDSHUSD"

    def __call__(self):
        return "tDSHUSD"


DSHUSD = DSHUSD()
"""
    name: tDSHUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.04
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class DUSK_BTC(NamedTuple):
    """
        name: tDUSK:BTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDUSK:BTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 18.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDUSK:BTC"

    def __str__(self):
        return "tDUSK:BTC"

    def __call__(self):
        return "tDUSK:BTC"


DUSK_BTC = DUSK_BTC()
"""
    name: tDUSK:BTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 18.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class DUSK_USD(NamedTuple):
    """
        name: tDUSK:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDUSK:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 18.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDUSK:USD"

    def __str__(self):
        return "tDUSK:USD"

    def __call__(self):
        return "tDUSK:USD"


DUSK_USD = DUSK_USD()
"""
    name: tDUSK:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 18.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class DVFUSD(NamedTuple):
    """
        name: tDVFUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDVFUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 1.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tDVFUSD"

    def __str__(self):
        return "tDVFUSD"

    def __call__(self):
        return "tDVFUSD"


DVFUSD = DVFUSD()
"""
    name: tDVFUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 1.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class EDOUSD(NamedTuple):
    """
        name: tEDOUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEDOUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 8.0
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEDOUSD"

    def __str__(self):
        return "tEDOUSD"

    def __call__(self):
        return "tEDOUSD"


EDOUSD = EDOUSD()
"""
    name: tEDOUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 8.0
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class EGLD_USD(NamedTuple):
    """
        name: tEGLD:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEGLD:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEGLD:USD"

    def __str__(self):
        return "tEGLD:USD"

    def __call__(self):
        return "tEGLD:USD"


EGLD_USD = EGLD_USD()
"""
    name: tEGLD:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class EGLD_UST(NamedTuple):
    """
        name: tEGLD:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEGLD:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEGLD:UST"

    def __str__(self):
        return "tEGLD:UST"

    def __call__(self):
        return "tEGLD:UST"


EGLD_UST = EGLD_UST()
"""
    name: tEGLD:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class EGLDF0_USTF0(NamedTuple):
    """
        name: tEGLDF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEGLDF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEGLDF0:USTF0"

    def __str__(self):
        return "tEGLDF0:USTF0"

    def __call__(self):
        return "tEGLDF0:USTF0"


EGLDF0_USTF0 = EGLDF0_USTF0()
"""
    name: tEGLDF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class ENJUSD(NamedTuple):
    """
        name: tENJUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tENJUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tENJUSD"

    def __str__(self):
        return "tENJUSD"

    def __call__(self):
        return "tENJUSD"


ENJUSD = ENJUSD()
"""
    name: tENJUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class EOSBTC(NamedTuple):
    """
        name: tEOSBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEOSBTC"

    def __str__(self):
        return "tEOSBTC"

    def __call__(self):
        return "tEOSBTC"


EOSBTC = EOSBTC()
"""
    name: tEOSBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class EOSETH(NamedTuple):
    """
        name: tEOSETH
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSETH"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEOSETH"

    def __str__(self):
        return "tEOSETH"

    def __call__(self):
        return "tEOSETH"


EOSETH = EOSETH()
"""
    name: tEOSETH
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class EOSEUR(NamedTuple):
    """
        name: tEOSEUR
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSEUR"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEOSEUR"

    def __str__(self):
        return "tEOSEUR"

    def __call__(self):
        return "tEOSEUR"


EOSEUR = EOSEUR()
"""
    name: tEOSEUR
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class EOSF0_USTF0(NamedTuple):
    """
        name: tEOSF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEOSF0:USTF0"

    def __str__(self):
        return "tEOSF0:USTF0"

    def __call__(self):
        return "tEOSF0:USTF0"


EOSF0_USTF0 = EOSF0_USTF0()
"""
    name: tEOSF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class EOSUSD(NamedTuple):
    """
        name: tEOSUSD
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSUSD"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEOSUSD"

    def __str__(self):
        return "tEOSUSD"

    def __call__(self):
        return "tEOSUSD"


EOSUSD = EOSUSD()
"""
    name: tEOSUSD
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class EOSUST(NamedTuple):
    """
        name: tEOSUST
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSUST"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEOSUST"

    def __str__(self):
        return "tEOSUST"

    def __call__(self):
        return "tEOSUST"


EOSUST = EOSUST()
"""
    name: tEOSUST
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class ETCBTC(NamedTuple):
    """
        name: tETCBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETCBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.1
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETCBTC"

    def __str__(self):
        return "tETCBTC"

    def __call__(self):
        return "tETCBTC"


ETCBTC = ETCBTC()
"""
    name: tETCBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.1
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class ETCF0_USTF0(NamedTuple):
    """
        name: tETCF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.1
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETCF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.1
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETCF0:USTF0"

    def __str__(self):
        return "tETCF0:USTF0"

    def __call__(self):
        return "tETCF0:USTF0"


ETCF0_USTF0 = ETCF0_USTF0()
"""
    name: tETCF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.1
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class ETCUSD(NamedTuple):
    """
        name: tETCUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETCUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.1
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETCUSD"

    def __str__(self):
        return "tETCUSD"

    def __call__(self):
        return "tETCUSD"


ETCUSD = ETCUSD()
"""
    name: tETCUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.1
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class ETCUST(NamedTuple):
    """
        name: tETCUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETCUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.1
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETCUST"

    def __str__(self):
        return "tETCUST"

    def __call__(self):
        return "tETCUST"


ETCUST = ETCUST()
"""
    name: tETCUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.1
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class ETH2X_ETH(NamedTuple):
    """
        name: tETH2X:ETH
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH2X:ETH"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 5000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETH2X:ETH"

    def __str__(self):
        return "tETH2X:ETH"

    def __call__(self):
        return "tETH2X:ETH"


ETH2X_ETH = ETH2X_ETH()
"""
    name: tETH2X:ETH
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 5000.0
    has_margin: False
    exchange: bitfinex
"""


class ETH2X_USD(NamedTuple):
    """
        name: tETH2X:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH2X:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 5000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETH2X:USD"

    def __str__(self):
        return "tETH2X:USD"

    def __call__(self):
        return "tETH2X:USD"


ETH2X_USD = ETH2X_USD()
"""
    name: tETH2X:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 5000.0
    has_margin: False
    exchange: bitfinex
"""


class ETH2X_UST(NamedTuple):
    """
        name: tETH2X:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH2X:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 5000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETH2X:UST"

    def __str__(self):
        return "tETH2X:UST"

    def __call__(self):
        return "tETH2X:UST"


ETH2X_UST = ETH2X_UST()
"""
    name: tETH2X:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 5000.0
    has_margin: False
    exchange: bitfinex
"""


class ETH_MXNT(NamedTuple):
    """
        name: tETH:MXNT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 2000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH:MXNT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 2000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETH:MXNT"

    def __str__(self):
        return "tETH:MXNT"

    def __call__(self):
        return "tETH:MXNT"


ETH_MXNT = ETH_MXNT()
"""
    name: tETH:MXNT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 2000.0
    has_margin: False
    exchange: bitfinex
"""


class ETH_XAUT(NamedTuple):
    """
        name: tETH:XAUT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 2500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH:XAUT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 2500.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETH:XAUT"

    def __str__(self):
        return "tETH:XAUT"

    def __call__(self):
        return "tETH:XAUT"


ETH_XAUT = ETH_XAUT()
"""
    name: tETH:XAUT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 2500.0
    has_margin: False
    exchange: bitfinex
"""


class ETHBTC(NamedTuple):
    """
        name: tETHBTC
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHBTC"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.002
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHBTC"

    def __str__(self):
        return "tETHBTC"

    def __call__(self):
        return "tETHBTC"


ETHBTC = ETHBTC()
"""
    name: tETHBTC
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.002
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHEUR(NamedTuple):
    """
        name: tETHEUR
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHEUR"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHEUR"

    def __str__(self):
        return "tETHEUR"

    def __call__(self):
        return "tETHEUR"


ETHEUR = ETHEUR()
"""
    name: tETHEUR
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHEUT(NamedTuple):
    """
        name: tETHEUT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHEUT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHEUT"

    def __str__(self):
        return "tETHEUT"

    def __call__(self):
        return "tETHEUT"


ETHEUT = ETHEUT()
"""
    name: tETHEUT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHF0_BTCF0(NamedTuple):
    """
        name: tETHF0:BTCF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHF0:BTCF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.002
    max_order_size: float = 100.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHF0:BTCF0"

    def __str__(self):
        return "tETHF0:BTCF0"

    def __call__(self):
        return "tETHF0:BTCF0"


ETHF0_BTCF0 = ETHF0_BTCF0()
"""
    name: tETHF0:BTCF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.002
    max_order_size: 100.0
    has_margin: True
    exchange: bitfinex
"""


class ETHF0_EUTF0(NamedTuple):
    """
        name: tETHF0:EUTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHF0:EUTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.002
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHF0:EUTF0"

    def __str__(self):
        return "tETHF0:EUTF0"

    def __call__(self):
        return "tETHF0:EUTF0"


ETHF0_EUTF0 = ETHF0_EUTF0()
"""
    name: tETHF0:EUTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.002
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHF0_USTF0(NamedTuple):
    """
        name: tETHF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.002
    max_order_size: float = 1000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHF0:USTF0"

    def __str__(self):
        return "tETHF0:USTF0"

    def __call__(self):
        return "tETHF0:USTF0"


ETHF0_USTF0 = ETHF0_USTF0()
"""
    name: tETHF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.002
    max_order_size: 1000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHGBP(NamedTuple):
    """
        name: tETHGBP
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHGBP"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHGBP"

    def __str__(self):
        return "tETHGBP"

    def __call__(self):
        return "tETHGBP"


ETHGBP = ETHGBP()
"""
    name: tETHGBP
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHJPY(NamedTuple):
    """
        name: tETHJPY
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHJPY"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHJPY"

    def __str__(self):
        return "tETHJPY"

    def __call__(self):
        return "tETHJPY"


ETHJPY = ETHJPY()
"""
    name: tETHJPY
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHUSD(NamedTuple):
    """
        name: tETHUSD
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHUSD"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.002
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHUSD"

    def __str__(self):
        return "tETHUSD"

    def __call__(self):
        return "tETHUSD"


ETHUSD = ETHUSD()
"""
    name: tETHUSD
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.002
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHUST(NamedTuple):
    """
        name: tETHUST
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHUST"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.002
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHUST"

    def __str__(self):
        return "tETHUST"

    def __call__(self):
        return "tETHUST"


ETHUST = ETHUST()
"""
    name: tETHUST
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.002
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHW_USD(NamedTuple):
    """
        name: tETHW:USD
        precision: 5
        min_margin: 30.0
        initial_margin: 60.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHW:USD"
    precision: int = 5
    min_margin: float = 30.0
    initial_margin: float = 60.0
    min_order_size: float = 0.001
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHW:USD"

    def __str__(self):
        return "tETHW:USD"

    def __call__(self):
        return "tETHW:USD"


ETHW_USD = ETHW_USD()
"""
    name: tETHW:USD
    precision: 5
    min_margin: 30.0
    initial_margin: 60.0
    min_order_size: 0.001
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class ETHW_UST(NamedTuple):
    """
        name: tETHW:UST
        precision: 5
        min_margin: 30.0
        initial_margin: 60.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHW:UST"
    precision: int = 5
    min_margin: float = 30.0
    initial_margin: float = 60.0
    min_order_size: float = 0.001
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETHW:UST"

    def __str__(self):
        return "tETHW:UST"

    def __call__(self):
        return "tETHW:UST"


ETHW_UST = ETHW_UST()
"""
    name: tETHW:UST
    precision: 5
    min_margin: 30.0
    initial_margin: 60.0
    min_order_size: 0.001
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class ETPUSD(NamedTuple):
    """
        name: tETPUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 42.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETPUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 42.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tETPUSD"

    def __str__(self):
        return "tETPUSD"

    def __call__(self):
        return "tETPUSD"


ETPUSD = ETPUSD()
"""
    name: tETPUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 42.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class EURF0_USTF0(NamedTuple):
    """
        name: tEURF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEURF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEURF0:USTF0"

    def __str__(self):
        return "tEURF0:USTF0"

    def __call__(self):
        return "tEURF0:USTF0"


EURF0_USTF0 = EURF0_USTF0()
"""
    name: tEURF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class EUROPE50IXF0_USTF0(NamedTuple):
    """
        name: tEUROPE50IXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.0006
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEUROPE50IXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.0006
    max_order_size: float = 10.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEUROPE50IXF0:USTF0"

    def __str__(self):
        return "tEUROPE50IXF0:USTF0"

    def __call__(self):
        return "tEUROPE50IXF0:USTF0"


EUROPE50IXF0_USTF0 = EUROPE50IXF0_USTF0()
"""
    name: tEUROPE50IXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.0006
    max_order_size: 10.0
    has_margin: True
    exchange: bitfinex
"""


class EURUST(NamedTuple):
    """
        name: tEURUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEURUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEURUST"

    def __str__(self):
        return "tEURUST"

    def __call__(self):
        return "tEURUST"


EURUST = EURUST()
"""
    name: tEURUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class EUSUSD(NamedTuple):
    """
        name: tEUSUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUSUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEUSUSD"

    def __str__(self):
        return "tEUSUSD"

    def __call__(self):
        return "tEUSUSD"


EUSUSD = EUSUSD()
"""
    name: tEUSUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class EUT_MXNT(NamedTuple):
    """
        name: tEUT:MXNT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUT:MXNT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEUT:MXNT"

    def __str__(self):
        return "tEUT:MXNT"

    def __call__(self):
        return "tEUT:MXNT"


EUT_MXNT = EUT_MXNT()
"""
    name: tEUT:MXNT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000000.0
    has_margin: False
    exchange: bitfinex
"""


class EUTEUR(NamedTuple):
    """
        name: tEUTEUR
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUTEUR"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEUTEUR"

    def __str__(self):
        return "tEUTEUR"

    def __call__(self):
        return "tEUTEUR"


EUTEUR = EUTEUR()
"""
    name: tEUTEUR
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class EUTUSD(NamedTuple):
    """
        name: tEUTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEUTUSD"

    def __str__(self):
        return "tEUTUSD"

    def __call__(self):
        return "tEUTUSD"


EUTUSD = EUTUSD()
"""
    name: tEUTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class EUTUST(NamedTuple):
    """
        name: tEUTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tEUTUST"

    def __str__(self):
        return "tEUTUST"

    def __call__(self):
        return "tEUTUST"


EUTUST = EUTUST()
"""
    name: tEUTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class FBTUSD(NamedTuple):
    """
        name: tFBTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFBTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFBTUSD"

    def __str__(self):
        return "tFBTUSD"

    def __call__(self):
        return "tFBTUSD"


FBTUSD = FBTUSD()
"""
    name: tFBTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class FBTUST(NamedTuple):
    """
        name: tFBTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFBTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFBTUST"

    def __str__(self):
        return "tFBTUST"

    def __call__(self):
        return "tFBTUST"


FBTUST = FBTUST()
"""
    name: tFBTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class FCLUSD(NamedTuple):
    """
        name: tFCLUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 62.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFCLUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 62.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFCLUSD"

    def __str__(self):
        return "tFCLUSD"

    def __call__(self):
        return "tFCLUSD"


FCLUSD = FCLUSD()
"""
    name: tFCLUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 62.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class FCLUST(NamedTuple):
    """
        name: tFCLUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 62.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFCLUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 62.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFCLUST"

    def __str__(self):
        return "tFCLUST"

    def __call__(self):
        return "tFCLUST"


FCLUST = FCLUST()
"""
    name: tFCLUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 62.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class FETUSD(NamedTuple):
    """
        name: tFETUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFETUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 14.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFETUSD"

    def __str__(self):
        return "tFETUSD"

    def __call__(self):
        return "tFETUSD"


FETUSD = FETUSD()
"""
    name: tFETUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 14.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class FETUST(NamedTuple):
    """
        name: tFETUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFETUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 14.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFETUST"

    def __str__(self):
        return "tFETUST"

    def __call__(self):
        return "tFETUST"


FETUST = FETUST()
"""
    name: tFETUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 14.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class FILF0_USTF0(NamedTuple):
    """
        name: tFILF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFILF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFILF0:USTF0"

    def __str__(self):
        return "tFILF0:USTF0"

    def __call__(self):
        return "tFILF0:USTF0"


FILF0_USTF0 = FILF0_USTF0()
"""
    name: tFILF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class FILUSD(NamedTuple):
    """
        name: tFILUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFILUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFILUSD"

    def __str__(self):
        return "tFILUSD"

    def __call__(self):
        return "tFILUSD"


FILUSD = FILUSD()
"""
    name: tFILUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class FILUST(NamedTuple):
    """
        name: tFILUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFILUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFILUST"

    def __str__(self):
        return "tFILUST"

    def __call__(self):
        return "tFILUST"


FILUST = FILUST()
"""
    name: tFILUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class FLRUSD(NamedTuple):
    """
        name: tFLRUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFLRUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFLRUSD"

    def __str__(self):
        return "tFLRUSD"

    def __call__(self):
        return "tFLRUSD"


FLRUSD = FLRUSD()
"""
    name: tFLRUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class FLRUST(NamedTuple):
    """
        name: tFLRUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFLRUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFLRUST"

    def __str__(self):
        return "tFLRUST"

    def __call__(self):
        return "tFLRUST"


FLRUST = FLRUST()
"""
    name: tFLRUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class FORTH_USD(NamedTuple):
    """
        name: tFORTH:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFORTH:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFORTH:USD"

    def __str__(self):
        return "tFORTH:USD"

    def __call__(self):
        return "tFORTH:USD"


FORTH_USD = FORTH_USD()
"""
    name: tFORTH:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class FORTH_UST(NamedTuple):
    """
        name: tFORTH:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFORTH:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFORTH:UST"

    def __str__(self):
        return "tFORTH:UST"

    def __call__(self):
        return "tFORTH:UST"


FORTH_UST = FORTH_UST()
"""
    name: tFORTH:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class FRANCE40IXF0_USTF0(NamedTuple):
    """
        name: tFRANCE40IXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFRANCE40IXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 10.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFRANCE40IXF0:USTF0"

    def __str__(self):
        return "tFRANCE40IXF0:USTF0"

    def __call__(self):
        return "tFRANCE40IXF0:USTF0"


FRANCE40IXF0_USTF0 = FRANCE40IXF0_USTF0()
"""
    name: tFRANCE40IXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 10.0
    has_margin: True
    exchange: bitfinex
"""


class FTMF0_USTF0(NamedTuple):
    """
        name: tFTMF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFTMF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 6.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFTMF0:USTF0"

    def __str__(self):
        return "tFTMF0:USTF0"

    def __call__(self):
        return "tFTMF0:USTF0"


FTMF0_USTF0 = FTMF0_USTF0()
"""
    name: tFTMF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 6.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class FTMUSD(NamedTuple):
    """
        name: tFTMUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFTMUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFTMUSD"

    def __str__(self):
        return "tFTMUSD"

    def __call__(self):
        return "tFTMUSD"


FTMUSD = FTMUSD()
"""
    name: tFTMUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class FTMUST(NamedTuple):
    """
        name: tFTMUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFTMUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFTMUST"

    def __str__(self):
        return "tFTMUST"

    def __call__(self):
        return "tFTMUST"


FTMUST = FTMUST()
"""
    name: tFTMUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class FUNUSD(NamedTuple):
    """
        name: tFUNUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 226.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFUNUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 226.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFUNUSD"

    def __str__(self):
        return "tFUNUSD"

    def __call__(self):
        return "tFUNUSD"


FUNUSD = FUNUSD()
"""
    name: tFUNUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 226.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class GALA_USD(NamedTuple):
    """
        name: tGALA:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGALA:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 26.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGALA:USD"

    def __str__(self):
        return "tGALA:USD"

    def __call__(self):
        return "tGALA:USD"


GALA_USD = GALA_USD()
"""
    name: tGALA:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 26.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class GALA_UST(NamedTuple):
    """
        name: tGALA:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGALA:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 26.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGALA:UST"

    def __str__(self):
        return "tGALA:UST"

    def __call__(self):
        return "tGALA:UST"


GALA_UST = GALA_UST()
"""
    name: tGALA:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 26.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class GALAF0_USTF0(NamedTuple):
    """
        name: tGALAF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tGALAF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 26.0
    max_order_size: float = 500000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGALAF0:USTF0"

    def __str__(self):
        return "tGALAF0:USTF0"

    def __call__(self):
        return "tGALAF0:USTF0"


GALAF0_USTF0 = GALAF0_USTF0()
"""
    name: tGALAF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 26.0
    max_order_size: 500000.0
    has_margin: True
    exchange: bitfinex
"""


class GBPEUT(NamedTuple):
    """
        name: tGBPEUT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGBPEUT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGBPEUT"

    def __str__(self):
        return "tGBPEUT"

    def __call__(self):
        return "tGBPEUT"


GBPEUT = GBPEUT()
"""
    name: tGBPEUT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class GBPF0_USTF0(NamedTuple):
    """
        name: tGBPF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tGBPF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGBPF0:USTF0"

    def __str__(self):
        return "tGBPF0:USTF0"

    def __call__(self):
        return "tGBPF0:USTF0"


GBPF0_USTF0 = GBPF0_USTF0()
"""
    name: tGBPF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class GBPUST(NamedTuple):
    """
        name: tGBPUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGBPUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGBPUST"

    def __str__(self):
        return "tGBPUST"

    def __call__(self):
        return "tGBPUST"


GBPUST = GBPUST()
"""
    name: tGBPUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class GERMANY40IXF0_USTF0(NamedTuple):
    """
        name: tGERMANY40IXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.0004
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tGERMANY40IXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.0004
    max_order_size: float = 10.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGERMANY40IXF0:USTF0"

    def __str__(self):
        return "tGERMANY40IXF0:USTF0"

    def __call__(self):
        return "tGERMANY40IXF0:USTF0"


GERMANY40IXF0_USTF0 = GERMANY40IXF0_USTF0()
"""
    name: tGERMANY40IXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.0004
    max_order_size: 10.0
    has_margin: True
    exchange: bitfinex
"""


class GNOUSD(NamedTuple):
    """
        name: tGNOUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 1000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGNOUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 1000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGNOUSD"

    def __str__(self):
        return "tGNOUSD"

    def __call__(self):
        return "tGNOUSD"


GNOUSD = GNOUSD()
"""
    name: tGNOUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 1000.0
    has_margin: False
    exchange: bitfinex
"""


class GNTUSD(NamedTuple):
    """
        name: tGNTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGNTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGNTUSD"

    def __str__(self):
        return "tGNTUSD"

    def __call__(self):
        return "tGNTUSD"


GNTUSD = GNTUSD()
"""
    name: tGNTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class GPTUSD(NamedTuple):
    """
        name: tGPTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 400000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGPTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 400000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGPTUSD"

    def __str__(self):
        return "tGPTUSD"

    def __call__(self):
        return "tGPTUSD"


GPTUSD = GPTUSD()
"""
    name: tGPTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 400000.0
    has_margin: False
    exchange: bitfinex
"""


class GPTUST(NamedTuple):
    """
        name: tGPTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 400000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGPTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 400000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGPTUST"

    def __str__(self):
        return "tGPTUST"

    def __call__(self):
        return "tGPTUST"


GPTUST = GPTUST()
"""
    name: tGPTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 400000.0
    has_margin: False
    exchange: bitfinex
"""


class GRTUSD(NamedTuple):
    """
        name: tGRTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGRTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 14.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGRTUSD"

    def __str__(self):
        return "tGRTUSD"

    def __call__(self):
        return "tGRTUSD"


GRTUSD = GRTUSD()
"""
    name: tGRTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 14.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class GRTUST(NamedTuple):
    """
        name: tGRTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGRTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 14.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGRTUST"

    def __str__(self):
        return "tGRTUST"

    def __call__(self):
        return "tGRTUST"


GRTUST = GRTUST()
"""
    name: tGRTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 14.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class GTXUSD(NamedTuple):
    """
        name: tGTXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGTXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGTXUSD"

    def __str__(self):
        return "tGTXUSD"

    def __call__(self):
        return "tGTXUSD"


GTXUSD = GTXUSD()
"""
    name: tGTXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class GTXUST(NamedTuple):
    """
        name: tGTXUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGTXUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGTXUST"

    def __str__(self):
        return "tGTXUST"

    def __call__(self):
        return "tGTXUST"


GTXUST = GTXUST()
"""
    name: tGTXUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class GXTUSD(NamedTuple):
    """
        name: tGXTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGXTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGXTUSD"

    def __str__(self):
        return "tGXTUSD"

    def __call__(self):
        return "tGXTUSD"


GXTUSD = GXTUSD()
"""
    name: tGXTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class GXTUST(NamedTuple):
    """
        name: tGXTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGXTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tGXTUST"

    def __str__(self):
        return "tGXTUST"

    def __call__(self):
        return "tGXTUST"


GXTUST = GXTUST()
"""
    name: tGXTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class HECUSD(NamedTuple):
    """
        name: tHECUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHECUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tHECUSD"

    def __str__(self):
        return "tHECUSD"

    def __call__(self):
        return "tHECUSD"


HECUSD = HECUSD()
"""
    name: tHECUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class HECUST(NamedTuple):
    """
        name: tHECUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHECUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tHECUST"

    def __str__(self):
        return "tHECUST"

    def __call__(self):
        return "tHECUST"


HECUST = HECUST()
"""
    name: tHECUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class HIXUSD(NamedTuple):
    """
        name: tHIXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHIXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 18.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tHIXUSD"

    def __str__(self):
        return "tHIXUSD"

    def __call__(self):
        return "tHIXUSD"


HIXUSD = HIXUSD()
"""
    name: tHIXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 18.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class HIXUST(NamedTuple):
    """
        name: tHIXUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHIXUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 18.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tHIXUST"

    def __str__(self):
        return "tHIXUST"

    def __call__(self):
        return "tHIXUST"


HIXUST = HIXUST()
"""
    name: tHIXUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 18.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class HMTUSD(NamedTuple):
    """
        name: tHMTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHMTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 8.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tHMTUSD"

    def __str__(self):
        return "tHMTUSD"

    def __call__(self):
        return "tHMTUSD"


HMTUSD = HMTUSD()
"""
    name: tHMTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 8.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class HMTUST(NamedTuple):
    """
        name: tHMTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHMTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 8.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tHMTUST"

    def __str__(self):
        return "tHMTUST"

    def __call__(self):
        return "tHMTUST"


HMTUST = HMTUST()
"""
    name: tHMTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 8.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class HONGKONG50IXF0_USTF0(NamedTuple):
    """
        name: tHONGKONG50IXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tHONGKONG50IXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 10.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tHONGKONG50IXF0:USTF0"

    def __str__(self):
        return "tHONGKONG50IXF0:USTF0"

    def __call__(self):
        return "tHONGKONG50IXF0:USTF0"


HONGKONG50IXF0_USTF0 = HONGKONG50IXF0_USTF0()
"""
    name: tHONGKONG50IXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 10.0
    has_margin: True
    exchange: bitfinex
"""


class HTXUSD(NamedTuple):
    """
        name: tHTXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHTXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tHTXUSD"

    def __str__(self):
        return "tHTXUSD"

    def __call__(self):
        return "tHTXUSD"


HTXUSD = HTXUSD()
"""
    name: tHTXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class HTXUST(NamedTuple):
    """
        name: tHTXUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHTXUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tHTXUST"

    def __str__(self):
        return "tHTXUST"

    def __call__(self):
        return "tHTXUST"


HTXUST = HTXUST()
"""
    name: tHTXUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class ICEUSD(NamedTuple):
    """
        name: tICEUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tICEUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 25000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tICEUSD"

    def __str__(self):
        return "tICEUSD"

    def __call__(self):
        return "tICEUSD"


ICEUSD = ICEUSD()
"""
    name: tICEUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 25000.0
    has_margin: False
    exchange: bitfinex
"""


class ICPBTC(NamedTuple):
    """
        name: tICPBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tICPBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tICPBTC"

    def __str__(self):
        return "tICPBTC"

    def __call__(self):
        return "tICPBTC"


ICPBTC = ICPBTC()
"""
    name: tICPBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class ICPF0_USTF0(NamedTuple):
    """
        name: tICPF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tICPF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tICPF0:USTF0"

    def __str__(self):
        return "tICPF0:USTF0"

    def __call__(self):
        return "tICPF0:USTF0"


ICPF0_USTF0 = ICPF0_USTF0()
"""
    name: tICPF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class ICPUSD(NamedTuple):
    """
        name: tICPUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tICPUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tICPUSD"

    def __str__(self):
        return "tICPUSD"

    def __call__(self):
        return "tICPUSD"


ICPUSD = ICPUSD()
"""
    name: tICPUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class ICPUST(NamedTuple):
    """
        name: tICPUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tICPUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tICPUST"

    def __str__(self):
        return "tICPUST"

    def __call__(self):
        return "tICPUST"


ICPUST = ICPUST()
"""
    name: tICPUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class IDXUSD(NamedTuple):
    """
        name: tIDXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tIDXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 20.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tIDXUSD"

    def __str__(self):
        return "tIDXUSD"

    def __call__(self):
        return "tIDXUSD"


IDXUSD = IDXUSD()
"""
    name: tIDXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 20.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class IDXUST(NamedTuple):
    """
        name: tIDXUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tIDXUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 20.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tIDXUST"

    def __str__(self):
        return "tIDXUST"

    def __call__(self):
        return "tIDXUST"


IDXUST = IDXUST()
"""
    name: tIDXUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 20.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class IOTBTC(NamedTuple):
    """
        name: tIOTBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tIOTBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tIOTBTC"

    def __str__(self):
        return "tIOTBTC"

    def __call__(self):
        return "tIOTBTC"


IOTBTC = IOTBTC()
"""
    name: tIOTBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class IOTF0_USTF0(NamedTuple):
    """
        name: tIOTF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tIOTF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 6.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tIOTF0:USTF0"

    def __str__(self):
        return "tIOTF0:USTF0"

    def __call__(self):
        return "tIOTF0:USTF0"


IOTF0_USTF0 = IOTF0_USTF0()
"""
    name: tIOTF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 6.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class IOTUSD(NamedTuple):
    """
        name: tIOTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tIOTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tIOTUSD"

    def __str__(self):
        return "tIOTUSD"

    def __call__(self):
        return "tIOTUSD"


IOTUSD = IOTUSD()
"""
    name: tIOTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class JAPAN225IXF0_USTF0(NamedTuple):
    """
        name: tJAPAN225IXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tJAPAN225IXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 10.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tJAPAN225IXF0:USTF0"

    def __str__(self):
        return "tJAPAN225IXF0:USTF0"

    def __call__(self):
        return "tJAPAN225IXF0:USTF0"


JAPAN225IXF0_USTF0 = JAPAN225IXF0_USTF0()
"""
    name: tJAPAN225IXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 10.0
    has_margin: True
    exchange: bitfinex
"""


class JASMY_USD(NamedTuple):
    """
        name: tJASMY:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 168.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJASMY:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 168.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tJASMY:USD"

    def __str__(self):
        return "tJASMY:USD"

    def __call__(self):
        return "tJASMY:USD"


JASMY_USD = JASMY_USD()
"""
    name: tJASMY:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 168.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class JASMY_UST(NamedTuple):
    """
        name: tJASMY:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 168.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJASMY:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 168.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tJASMY:UST"

    def __str__(self):
        return "tJASMY:UST"

    def __call__(self):
        return "tJASMY:UST"


JASMY_UST = JASMY_UST()
"""
    name: tJASMY:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 168.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class JASMYF0_USTF0(NamedTuple):
    """
        name: tJASMYF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 168.0
        max_order_size: 2500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tJASMYF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 168.0
    max_order_size: float = 2500000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tJASMYF0:USTF0"

    def __str__(self):
        return "tJASMYF0:USTF0"

    def __call__(self):
        return "tJASMYF0:USTF0"


JASMYF0_USTF0 = JASMYF0_USTF0()
"""
    name: tJASMYF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 168.0
    max_order_size: 2500000.0
    has_margin: True
    exchange: bitfinex
"""


class JPYF0_USTF0(NamedTuple):
    """
        name: tJPYF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 262.0
        max_order_size: 100000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tJPYF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 262.0
    max_order_size: float = 100000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tJPYF0:USTF0"

    def __str__(self):
        return "tJPYF0:USTF0"

    def __call__(self):
        return "tJPYF0:USTF0"


JPYF0_USTF0 = JPYF0_USTF0()
"""
    name: tJPYF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 262.0
    max_order_size: 100000000.0
    has_margin: True
    exchange: bitfinex
"""


class JPYUST(NamedTuple):
    """
        name: tJPYUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 262.0
        max_order_size: 100000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJPYUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 262.0
    max_order_size: float = 100000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tJPYUST"

    def __str__(self):
        return "tJPYUST"

    def __call__(self):
        return "tJPYUST"


JPYUST = JPYUST()
"""
    name: tJPYUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 262.0
    max_order_size: 100000000.0
    has_margin: False
    exchange: bitfinex
"""


class JSTBTC(NamedTuple):
    """
        name: tJSTBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 48.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJSTBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 48.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tJSTBTC"

    def __str__(self):
        return "tJSTBTC"

    def __call__(self):
        return "tJSTBTC"


JSTBTC = JSTBTC()
"""
    name: tJSTBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 48.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class JSTUSD(NamedTuple):
    """
        name: tJSTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 48.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJSTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 48.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tJSTUSD"

    def __str__(self):
        return "tJSTUSD"

    def __call__(self):
        return "tJSTUSD"


JSTUSD = JSTUSD()
"""
    name: tJSTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 48.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class JSTUST(NamedTuple):
    """
        name: tJSTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 48.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJSTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 48.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tJSTUST"

    def __str__(self):
        return "tJSTUST"

    def __call__(self):
        return "tJSTUST"


JSTUST = JSTUST()
"""
    name: tJSTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 48.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class KANUSD(NamedTuple):
    """
        name: tKANUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1542.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKANUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 1542.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tKANUSD"

    def __str__(self):
        return "tKANUSD"

    def __call__(self):
        return "tKANUSD"


KANUSD = KANUSD()
"""
    name: tKANUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 1542.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class KANUST(NamedTuple):
    """
        name: tKANUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1542.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKANUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 1542.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tKANUST"

    def __str__(self):
        return "tKANUST"

    def __call__(self):
        return "tKANUST"


KANUST = KANUST()
"""
    name: tKANUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 1542.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class KNCBTC(NamedTuple):
    """
        name: tKNCBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKNCBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 20000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tKNCBTC"

    def __str__(self):
        return "tKNCBTC"

    def __call__(self):
        return "tKNCBTC"


KNCBTC = KNCBTC()
"""
    name: tKNCBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 20000.0
    has_margin: False
    exchange: bitfinex
"""


class KNCF0_USTF0(NamedTuple):
    """
        name: tKNCF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tKNCF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tKNCF0:USTF0"

    def __str__(self):
        return "tKNCF0:USTF0"

    def __call__(self):
        return "tKNCF0:USTF0"


KNCF0_USTF0 = KNCF0_USTF0()
"""
    name: tKNCF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class KNCUSD(NamedTuple):
    """
        name: tKNCUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKNCUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tKNCUSD"

    def __str__(self):
        return "tKNCUSD"

    def __call__(self):
        return "tKNCUSD"


KNCUSD = KNCUSD()
"""
    name: tKNCUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class KSMUSD(NamedTuple):
    """
        name: tKSMUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKSMUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tKSMUSD"

    def __str__(self):
        return "tKSMUSD"

    def __call__(self):
        return "tKSMUSD"


KSMUSD = KSMUSD()
"""
    name: tKSMUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: False
    exchange: bitfinex
"""


class KSMUST(NamedTuple):
    """
        name: tKSMUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKSMUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tKSMUST"

    def __str__(self):
        return "tKSMUST"

    def __call__(self):
        return "tKSMUST"


KSMUST = KSMUST()
"""
    name: tKSMUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: False
    exchange: bitfinex
"""


class LDOUSD(NamedTuple):
    """
        name: tLDOUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLDOUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLDOUSD"

    def __str__(self):
        return "tLDOUSD"

    def __call__(self):
        return "tLDOUSD"


LDOUSD = LDOUSD()
"""
    name: tLDOUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class LDOUST(NamedTuple):
    """
        name: tLDOUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLDOUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLDOUST"

    def __str__(self):
        return "tLDOUST"

    def __call__(self):
        return "tLDOUST"


LDOUST = LDOUST()
"""
    name: tLDOUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class LEOBTC(NamedTuple):
    """
        name: tLEOBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLEOBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLEOBTC"

    def __str__(self):
        return "tLEOBTC"

    def __call__(self):
        return "tLEOBTC"


LEOBTC = LEOBTC()
"""
    name: tLEOBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class LEOETH(NamedTuple):
    """
        name: tLEOETH
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLEOETH"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLEOETH"

    def __str__(self):
        return "tLEOETH"

    def __call__(self):
        return "tLEOETH"


LEOETH = LEOETH()
"""
    name: tLEOETH
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class LEOUSD(NamedTuple):
    """
        name: tLEOUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLEOUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLEOUSD"

    def __str__(self):
        return "tLEOUSD"

    def __call__(self):
        return "tLEOUSD"


LEOUSD = LEOUSD()
"""
    name: tLEOUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class LEOUST(NamedTuple):
    """
        name: tLEOUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLEOUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLEOUST"

    def __str__(self):
        return "tLEOUST"

    def __call__(self):
        return "tLEOUST"


LEOUST = LEOUST()
"""
    name: tLEOUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class LINK_USD(NamedTuple):
    """
        name: tLINK:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLINK:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLINK:USD"

    def __str__(self):
        return "tLINK:USD"

    def __call__(self):
        return "tLINK:USD"


LINK_USD = LINK_USD()
"""
    name: tLINK:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class LINK_UST(NamedTuple):
    """
        name: tLINK:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLINK:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLINK:UST"

    def __str__(self):
        return "tLINK:UST"

    def __call__(self):
        return "tLINK:UST"


LINK_UST = LINK_UST()
"""
    name: tLINK:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class LINKF0_USTF0(NamedTuple):
    """
        name: tLINKF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLINKF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.2
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLINKF0:USTF0"

    def __str__(self):
        return "tLINKF0:USTF0"

    def __call__(self):
        return "tLINKF0:USTF0"


LINKF0_USTF0 = LINKF0_USTF0()
"""
    name: tLINKF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.2
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class LRCUSD(NamedTuple):
    """
        name: tLRCUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLRCUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLRCUSD"

    def __str__(self):
        return "tLRCUSD"

    def __call__(self):
        return "tLRCUSD"


LRCUSD = LRCUSD()
"""
    name: tLRCUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class LTCBTC(NamedTuple):
    """
        name: tLTCBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.04
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLTCBTC"

    def __str__(self):
        return "tLTCBTC"

    def __call__(self):
        return "tLTCBTC"


LTCBTC = LTCBTC()
"""
    name: tLTCBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.04
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class LTCF0_BTCF0(NamedTuple):
    """
        name: tLTCF0:BTCF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.04
        max_order_size: 7500.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCF0:BTCF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.04
    max_order_size: float = 7500.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLTCF0:BTCF0"

    def __str__(self):
        return "tLTCF0:BTCF0"

    def __call__(self):
        return "tLTCF0:BTCF0"


LTCF0_BTCF0 = LTCF0_BTCF0()
"""
    name: tLTCF0:BTCF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.04
    max_order_size: 7500.0
    has_margin: True
    exchange: bitfinex
"""


class LTCF0_USTF0(NamedTuple):
    """
        name: tLTCF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.04
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.04
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLTCF0:USTF0"

    def __str__(self):
        return "tLTCF0:USTF0"

    def __call__(self):
        return "tLTCF0:USTF0"


LTCF0_USTF0 = LTCF0_USTF0()
"""
    name: tLTCF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.04
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class LTCUSD(NamedTuple):
    """
        name: tLTCUSD
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCUSD"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.04
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLTCUSD"

    def __str__(self):
        return "tLTCUSD"

    def __call__(self):
        return "tLTCUSD"


LTCUSD = LTCUSD()
"""
    name: tLTCUSD
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.04
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class LTCUST(NamedTuple):
    """
        name: tLTCUST
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.04
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCUST"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.04
    max_order_size: float = 2000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLTCUST"

    def __str__(self):
        return "tLTCUST"

    def __call__(self):
        return "tLTCUST"


LTCUST = LTCUST()
"""
    name: tLTCUST
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.04
    max_order_size: 2000.0
    has_margin: True
    exchange: bitfinex
"""


class LUNA2_USD(NamedTuple):
    """
        name: tLUNA2:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUNA2:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLUNA2:USD"

    def __str__(self):
        return "tLUNA2:USD"

    def __call__(self):
        return "tLUNA2:USD"


LUNA2_USD = LUNA2_USD()
"""
    name: tLUNA2:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class LUNA2_UST(NamedTuple):
    """
        name: tLUNA2:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUNA2:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLUNA2:UST"

    def __str__(self):
        return "tLUNA2:UST"

    def __call__(self):
        return "tLUNA2:UST"


LUNA2_UST = LUNA2_UST()
"""
    name: tLUNA2:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class LUNA_USD(NamedTuple):
    """
        name: tLUNA:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20814.0
        max_order_size: 100000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUNA:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 20814.0
    max_order_size: float = 100000000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLUNA:USD"

    def __str__(self):
        return "tLUNA:USD"

    def __call__(self):
        return "tLUNA:USD"


LUNA_USD = LUNA_USD()
"""
    name: tLUNA:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 20814.0
    max_order_size: 100000000000.0
    has_margin: False
    exchange: bitfinex
"""


class LUNA_UST(NamedTuple):
    """
        name: tLUNA:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20814.0
        max_order_size: 100000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUNA:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 20814.0
    max_order_size: float = 100000000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLUNA:UST"

    def __str__(self):
        return "tLUNA:UST"

    def __call__(self):
        return "tLUNA:UST"


LUNA_UST = LUNA_UST()
"""
    name: tLUNA:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 20814.0
    max_order_size: 100000000000.0
    has_margin: False
    exchange: bitfinex
"""


class LUXO_USD(NamedTuple):
    """
        name: tLUXO:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUXO:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 20.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLUXO:USD"

    def __str__(self):
        return "tLUXO:USD"

    def __call__(self):
        return "tLUXO:USD"


LUXO_USD = LUXO_USD()
"""
    name: tLUXO:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 20.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class LYMUSD(NamedTuple):
    """
        name: tLYMUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 740.0
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLYMUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 740.0
    max_order_size: float = 10000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tLYMUSD"

    def __str__(self):
        return "tLYMUSD"

    def __call__(self):
        return "tLYMUSD"


LYMUSD = LYMUSD()
"""
    name: tLYMUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 740.0
    max_order_size: 10000000.0
    has_margin: False
    exchange: bitfinex
"""


class MATIC_BTC(NamedTuple):
    """
        name: tMATIC:BTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMATIC:BTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMATIC:BTC"

    def __str__(self):
        return "tMATIC:BTC"

    def __call__(self):
        return "tMATIC:BTC"


MATIC_BTC = MATIC_BTC()
"""
    name: tMATIC:BTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class MATIC_USD(NamedTuple):
    """
        name: tMATIC:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMATIC:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMATIC:USD"

    def __str__(self):
        return "tMATIC:USD"

    def __call__(self):
        return "tMATIC:USD"


MATIC_USD = MATIC_USD()
"""
    name: tMATIC:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class MATIC_UST(NamedTuple):
    """
        name: tMATIC:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMATIC:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMATIC:UST"

    def __str__(self):
        return "tMATIC:UST"

    def __call__(self):
        return "tMATIC:UST"


MATIC_UST = MATIC_UST()
"""
    name: tMATIC:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class MATICF0_USTF0(NamedTuple):
    """
        name: tMATICF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMATICF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 4.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMATICF0:USTF0"

    def __str__(self):
        return "tMATICF0:USTF0"

    def __call__(self):
        return "tMATICF0:USTF0"


MATICF0_USTF0 = MATICF0_USTF0()
"""
    name: tMATICF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 4.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class MIMUSD(NamedTuple):
    """
        name: tMIMUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMIMUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMIMUSD"

    def __str__(self):
        return "tMIMUSD"

    def __call__(self):
        return "tMIMUSD"


MIMUSD = MIMUSD()
"""
    name: tMIMUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class MIMUST(NamedTuple):
    """
        name: tMIMUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMIMUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMIMUST"

    def __str__(self):
        return "tMIMUST"

    def __call__(self):
        return "tMIMUST"


MIMUST = MIMUST()
"""
    name: tMIMUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class MKRF0_USTF0(NamedTuple):
    """
        name: tMKRF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 2500.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMKRF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.002
    max_order_size: float = 2500.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMKRF0:USTF0"

    def __str__(self):
        return "tMKRF0:USTF0"

    def __call__(self):
        return "tMKRF0:USTF0"


MKRF0_USTF0 = MKRF0_USTF0()
"""
    name: tMKRF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.002
    max_order_size: 2500.0
    has_margin: True
    exchange: bitfinex
"""


class MKRUSD(NamedTuple):
    """
        name: tMKRUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 2500.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMKRUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 2500.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMKRUSD"

    def __str__(self):
        return "tMKRUSD"

    def __call__(self):
        return "tMKRUSD"


MKRUSD = MKRUSD()
"""
    name: tMKRUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 2500.0
    has_margin: True
    exchange: bitfinex
"""


class MKRUST(NamedTuple):
    """
        name: tMKRUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 2500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMKRUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.002
    max_order_size: float = 2500.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMKRUST"

    def __str__(self):
        return "tMKRUST"

    def __call__(self):
        return "tMKRUST"


MKRUST = MKRUST()
"""
    name: tMKRUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.002
    max_order_size: 2500.0
    has_margin: False
    exchange: bitfinex
"""


class MLNUSD(NamedTuple):
    """
        name: tMLNUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.08
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMLNUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.08
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMLNUSD"

    def __str__(self):
        return "tMLNUSD"

    def __call__(self):
        return "tMLNUSD"


MLNUSD = MLNUSD()
"""
    name: tMLNUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.08
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class MNABTC(NamedTuple):
    """
        name: tMNABTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMNABTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 200000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMNABTC"

    def __str__(self):
        return "tMNABTC"

    def __call__(self):
        return "tMNABTC"


MNABTC = MNABTC()
"""
    name: tMNABTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 200000.0
    has_margin: False
    exchange: bitfinex
"""


class MNAUSD(NamedTuple):
    """
        name: tMNAUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMNAUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 200000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMNAUSD"

    def __str__(self):
        return "tMNAUSD"

    def __call__(self):
        return "tMNAUSD"


MNAUSD = MNAUSD()
"""
    name: tMNAUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 200000.0
    has_margin: False
    exchange: bitfinex
"""


class MOBUSD(NamedTuple):
    """
        name: tMOBUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMOBUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMOBUSD"

    def __str__(self):
        return "tMOBUSD"

    def __call__(self):
        return "tMOBUSD"


MOBUSD = MOBUSD()
"""
    name: tMOBUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class MOBUST(NamedTuple):
    """
        name: tMOBUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMOBUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMOBUST"

    def __str__(self):
        return "tMOBUST"

    def __call__(self):
        return "tMOBUST"


MOBUST = MOBUST()
"""
    name: tMOBUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class MXNT_USD(NamedTuple):
    """
        name: tMXNT:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMXNT:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tMXNT:USD"

    def __str__(self):
        return "tMXNT:USD"

    def __call__(self):
        return "tMXNT:USD"


MXNT_USD = MXNT_USD()
"""
    name: tMXNT:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000000.0
    has_margin: False
    exchange: bitfinex
"""


class NEAR_USD(NamedTuple):
    """
        name: tNEAR:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEAR:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 25000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEAR:USD"

    def __str__(self):
        return "tNEAR:USD"

    def __call__(self):
        return "tNEAR:USD"


NEAR_USD = NEAR_USD()
"""
    name: tNEAR:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 25000.0
    has_margin: False
    exchange: bitfinex
"""


class NEAR_UST(NamedTuple):
    """
        name: tNEAR:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEAR:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 25000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEAR:UST"

    def __str__(self):
        return "tNEAR:UST"

    def __call__(self):
        return "tNEAR:UST"


NEAR_UST = NEAR_UST()
"""
    name: tNEAR:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 25000.0
    has_margin: False
    exchange: bitfinex
"""


class NEARF0_USTF0(NamedTuple):
    """
        name: tNEARF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.4
        max_order_size: 25000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEARF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.4
    max_order_size: float = 25000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEARF0:USTF0"

    def __str__(self):
        return "tNEARF0:USTF0"

    def __call__(self):
        return "tNEARF0:USTF0"


NEARF0_USTF0 = NEARF0_USTF0()
"""
    name: tNEARF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.4
    max_order_size: 25000.0
    has_margin: True
    exchange: bitfinex
"""


class NEOBTC(NamedTuple):
    """
        name: tNEOBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEOBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEOBTC"

    def __str__(self):
        return "tNEOBTC"

    def __call__(self):
        return "tNEOBTC"


NEOBTC = NEOBTC()
"""
    name: tNEOBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class NEOF0_USTF0(NamedTuple):
    """
        name: tNEOF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEOF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEOF0:USTF0"

    def __str__(self):
        return "tNEOF0:USTF0"

    def __call__(self):
        return "tNEOF0:USTF0"


NEOF0_USTF0 = NEOF0_USTF0()
"""
    name: tNEOF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class NEOUSD(NamedTuple):
    """
        name: tNEOUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEOUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEOUSD"

    def __str__(self):
        return "tNEOUSD"

    def __call__(self):
        return "tNEOUSD"


NEOUSD = NEOUSD()
"""
    name: tNEOUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class NEOUST(NamedTuple):
    """
        name: tNEOUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEOUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEOUST"

    def __str__(self):
        return "tNEOUST"

    def __call__(self):
        return "tNEOUST"


NEOUST = NEOUST()
"""
    name: tNEOUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class NEXO_BTC(NamedTuple):
    """
        name: tNEXO:BTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEXO:BTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEXO:BTC"

    def __str__(self):
        return "tNEXO:BTC"

    def __call__(self):
        return "tNEXO:BTC"


NEXO_BTC = NEXO_BTC()
"""
    name: tNEXO:BTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class NEXO_USD(NamedTuple):
    """
        name: tNEXO:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEXO:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEXO:USD"

    def __str__(self):
        return "tNEXO:USD"

    def __call__(self):
        return "tNEXO:USD"


NEXO_USD = NEXO_USD()
"""
    name: tNEXO:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class NEXO_UST(NamedTuple):
    """
        name: tNEXO:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEXO:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNEXO:UST"

    def __str__(self):
        return "tNEXO:UST"

    def __call__(self):
        return "tNEXO:UST"


NEXO_UST = NEXO_UST()
"""
    name: tNEXO:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class NOMUSD(NamedTuple):
    """
        name: tNOMUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNOMUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 20000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNOMUSD"

    def __str__(self):
        return "tNOMUSD"

    def __call__(self):
        return "tNOMUSD"


NOMUSD = NOMUSD()
"""
    name: tNOMUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 20000.0
    has_margin: False
    exchange: bitfinex
"""


class NOMUST(NamedTuple):
    """
        name: tNOMUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNOMUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 20000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNOMUST"

    def __str__(self):
        return "tNOMUST"

    def __call__(self):
        return "tNOMUST"


NOMUST = NOMUST()
"""
    name: tNOMUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 20000.0
    has_margin: False
    exchange: bitfinex
"""


class NXRA_USD(NamedTuple):
    """
        name: tNXRA:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNXRA:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 200000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tNXRA:USD"

    def __str__(self):
        return "tNXRA:USD"

    def __call__(self):
        return "tNXRA:USD"


NXRA_USD = NXRA_USD()
"""
    name: tNXRA:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 200000.0
    has_margin: False
    exchange: bitfinex
"""


class OCEAN_USD(NamedTuple):
    """
        name: tOCEAN:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOCEAN:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 10.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tOCEAN:USD"

    def __str__(self):
        return "tOCEAN:USD"

    def __call__(self):
        return "tOCEAN:USD"


OCEAN_USD = OCEAN_USD()
"""
    name: tOCEAN:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 10.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class OCEAN_UST(NamedTuple):
    """
        name: tOCEAN:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOCEAN:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 10.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tOCEAN:UST"

    def __str__(self):
        return "tOCEAN:UST"

    def __call__(self):
        return "tOCEAN:UST"


OCEAN_UST = OCEAN_UST()
"""
    name: tOCEAN:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 10.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class OGNUSD(NamedTuple):
    """
        name: tOGNUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOGNUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tOGNUSD"

    def __str__(self):
        return "tOGNUSD"

    def __call__(self):
        return "tOGNUSD"


OGNUSD = OGNUSD()
"""
    name: tOGNUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class OGNUST(NamedTuple):
    """
        name: tOGNUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOGNUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tOGNUST"

    def __str__(self):
        return "tOGNUST"

    def __call__(self):
        return "tOGNUST"


OGNUST = OGNUST()
"""
    name: tOGNUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class OMGBTC(NamedTuple):
    """
        name: tOMGBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tOMGBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.8
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tOMGBTC"

    def __str__(self):
        return "tOMGBTC"

    def __call__(self):
        return "tOMGBTC"


OMGBTC = OMGBTC()
"""
    name: tOMGBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.8
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class OMGETH(NamedTuple):
    """
        name: tOMGETH
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tOMGETH"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.8
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tOMGETH"

    def __str__(self):
        return "tOMGETH"

    def __call__(self):
        return "tOMGETH"


OMGETH = OMGETH()
"""
    name: tOMGETH
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.8
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class OMGF0_USTF0(NamedTuple):
    """
        name: tOMGF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.8
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tOMGF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.8
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tOMGF0:USTF0"

    def __str__(self):
        return "tOMGF0:USTF0"

    def __call__(self):
        return "tOMGF0:USTF0"


OMGF0_USTF0 = OMGF0_USTF0()
"""
    name: tOMGF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.8
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class OMGUSD(NamedTuple):
    """
        name: tOMGUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tOMGUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.8
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tOMGUSD"

    def __str__(self):
        return "tOMGUSD"

    def __call__(self):
        return "tOMGUSD"


OMGUSD = OMGUSD()
"""
    name: tOMGUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.8
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class OMNUSD(NamedTuple):
    """
        name: tOMNUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOMNUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 20000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tOMNUSD"

    def __str__(self):
        return "tOMNUSD"

    def __call__(self):
        return "tOMNUSD"


OMNUSD = OMNUSD()
"""
    name: tOMNUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 20000.0
    has_margin: False
    exchange: bitfinex
"""


class ONEUSD(NamedTuple):
    """
        name: tONEUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tONEUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tONEUSD"

    def __str__(self):
        return "tONEUSD"

    def __call__(self):
        return "tONEUSD"


ONEUSD = ONEUSD()
"""
    name: tONEUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class ONEUST(NamedTuple):
    """
        name: tONEUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tONEUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tONEUST"

    def __str__(self):
        return "tONEUST"

    def __call__(self):
        return "tONEUST"


ONEUST = ONEUST()
"""
    name: tONEUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class PASUSD(NamedTuple):
    """
        name: tPASUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1588.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPASUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 1588.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPASUSD"

    def __str__(self):
        return "tPASUSD"

    def __call__(self):
        return "tPASUSD"


PASUSD = PASUSD()
"""
    name: tPASUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 1588.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class PAXUSD(NamedTuple):
    """
        name: tPAXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPAXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPAXUSD"

    def __str__(self):
        return "tPAXUSD"

    def __call__(self):
        return "tPAXUSD"


PAXUSD = PAXUSD()
"""
    name: tPAXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class PAXUST(NamedTuple):
    """
        name: tPAXUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPAXUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPAXUST"

    def __str__(self):
        return "tPAXUST"

    def __call__(self):
        return "tPAXUST"


PAXUST = PAXUST()
"""
    name: tPAXUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class PLANETS_USD(NamedTuple):
    """
        name: tPLANETS:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 124.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPLANETS:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 124.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPLANETS:USD"

    def __str__(self):
        return "tPLANETS:USD"

    def __call__(self):
        return "tPLANETS:USD"


PLANETS_USD = PLANETS_USD()
"""
    name: tPLANETS:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 124.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class PLANETS_UST(NamedTuple):
    """
        name: tPLANETS:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 124.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPLANETS:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 124.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPLANETS:UST"

    def __str__(self):
        return "tPLANETS:UST"

    def __call__(self):
        return "tPLANETS:UST"


PLANETS_UST = PLANETS_UST()
"""
    name: tPLANETS:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 124.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class PLUUSD(NamedTuple):
    """
        name: tPLUUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPLUUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 10000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPLUUSD"

    def __str__(self):
        return "tPLUUSD"

    def __call__(self):
        return "tPLUUSD"


PLUUSD = PLUUSD()
"""
    name: tPLUUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 10000.0
    has_margin: False
    exchange: bitfinex
"""


class PNKUSD(NamedTuple):
    """
        name: tPNKUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPNKUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 52.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPNKUSD"

    def __str__(self):
        return "tPNKUSD"

    def __call__(self):
        return "tPNKUSD"


PNKUSD = PNKUSD()
"""
    name: tPNKUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 52.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class POLC_USD(NamedTuple):
    """
        name: tPOLC:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPOLC:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 26.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPOLC:USD"

    def __str__(self):
        return "tPOLC:USD"

    def __call__(self):
        return "tPOLC:USD"


POLC_USD = POLC_USD()
"""
    name: tPOLC:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 26.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class POLC_UST(NamedTuple):
    """
        name: tPOLC:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPOLC:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 26.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPOLC:UST"

    def __str__(self):
        return "tPOLC:UST"

    def __call__(self):
        return "tPOLC:UST"


POLC_UST = POLC_UST()
"""
    name: tPOLC:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 26.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class POLIS_USD(NamedTuple):
    """
        name: tPOLIS:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPOLIS:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPOLIS:USD"

    def __str__(self):
        return "tPOLIS:USD"

    def __call__(self):
        return "tPOLIS:USD"


POLIS_USD = POLIS_USD()
"""
    name: tPOLIS:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class POLIS_UST(NamedTuple):
    """
        name: tPOLIS:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPOLIS:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPOLIS:UST"

    def __str__(self):
        return "tPOLIS:UST"

    def __call__(self):
        return "tPOLIS:UST"


POLIS_UST = POLIS_UST()
"""
    name: tPOLIS:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class PRMX_USD(NamedTuple):
    """
        name: tPRMX:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 4000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPRMX:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 4000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPRMX:USD"

    def __str__(self):
        return "tPRMX:USD"

    def __call__(self):
        return "tPRMX:USD"


PRMX_USD = PRMX_USD()
"""
    name: tPRMX:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 4000000.0
    has_margin: False
    exchange: bitfinex
"""


class PRMX_UST(NamedTuple):
    """
        name: tPRMX:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 4000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPRMX:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 4000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tPRMX:UST"

    def __str__(self):
        return "tPRMX:UST"

    def __call__(self):
        return "tPRMX:UST"


PRMX_UST = PRMX_UST()
"""
    name: tPRMX:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 4000000.0
    has_margin: False
    exchange: bitfinex
"""


class QRDO_USD(NamedTuple):
    """
        name: tQRDO:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQRDO:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tQRDO:USD"

    def __str__(self):
        return "tQRDO:USD"

    def __call__(self):
        return "tQRDO:USD"


QRDO_USD = QRDO_USD()
"""
    name: tQRDO:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class QRDO_UST(NamedTuple):
    """
        name: tQRDO:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQRDO:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tQRDO:UST"

    def __str__(self):
        return "tQRDO:UST"

    def __call__(self):
        return "tQRDO:UST"


QRDO_UST = QRDO_UST()
"""
    name: tQRDO:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class QTFBTC(NamedTuple):
    """
        name: tQTFBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQTFBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tQTFBTC"

    def __str__(self):
        return "tQTFBTC"

    def __call__(self):
        return "tQTFBTC"


QTFBTC = QTFBTC()
"""
    name: tQTFBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class QTFUSD(NamedTuple):
    """
        name: tQTFUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQTFUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tQTFUSD"

    def __str__(self):
        return "tQTFUSD"

    def __call__(self):
        return "tQTFUSD"


QTFUSD = QTFUSD()
"""
    name: tQTFUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class QTMUSD(NamedTuple):
    """
        name: tQTMUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQTMUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.6
    max_order_size: float = 5000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tQTMUSD"

    def __str__(self):
        return "tQTMUSD"

    def __call__(self):
        return "tQTMUSD"


QTMUSD = QTMUSD()
"""
    name: tQTMUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.6
    max_order_size: 5000.0
    has_margin: False
    exchange: bitfinex
"""


class RBTUSD(NamedTuple):
    """
        name: tRBTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tRBTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00006
    max_order_size: float = 500.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tRBTUSD"

    def __str__(self):
        return "tRBTUSD"

    def __call__(self):
        return "tRBTUSD"


RBTUSD = RBTUSD()
"""
    name: tRBTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00006
    max_order_size: 500.0
    has_margin: False
    exchange: bitfinex
"""


class REEF_USD(NamedTuple):
    """
        name: tREEF:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 466.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tREEF:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 466.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tREEF:USD"

    def __str__(self):
        return "tREEF:USD"

    def __call__(self):
        return "tREEF:USD"


REEF_USD = REEF_USD()
"""
    name: tREEF:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 466.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class REEF_UST(NamedTuple):
    """
        name: tREEF:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 466.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tREEF:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 466.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tREEF:UST"

    def __str__(self):
        return "tREEF:UST"

    def __call__(self):
        return "tREEF:UST"


REEF_UST = REEF_UST()
"""
    name: tREEF:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 466.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class REPUSD(NamedTuple):
    """
        name: tREPUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 1000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tREPUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 1000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tREPUSD"

    def __str__(self):
        return "tREPUSD"

    def __call__(self):
        return "tREPUSD"


REPUSD = REPUSD()
"""
    name: tREPUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 1000.0
    has_margin: False
    exchange: bitfinex
"""


class REQUSD(NamedTuple):
    """
        name: tREQUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 16.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tREQUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 16.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tREQUSD"

    def __str__(self):
        return "tREQUSD"

    def __call__(self):
        return "tREQUSD"


REQUSD = REQUSD()
"""
    name: tREQUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 16.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class RLYUSD(NamedTuple):
    """
        name: tRLYUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tRLYUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tRLYUSD"

    def __str__(self):
        return "tRLYUSD"

    def __call__(self):
        return "tRLYUSD"


RLYUSD = RLYUSD()
"""
    name: tRLYUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class RLYUST(NamedTuple):
    """
        name: tRLYUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tRLYUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tRLYUST"

    def __str__(self):
        return "tRLYUST"

    def __call__(self):
        return "tRLYUST"


RLYUST = RLYUST()
"""
    name: tRLYUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class RRTUSD(NamedTuple):
    """
        name: tRRTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tRRTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tRRTUSD"

    def __str__(self):
        return "tRRTUSD"

    def __call__(self):
        return "tRRTUSD"


RRTUSD = RRTUSD()
"""
    name: tRRTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class SAND_USD(NamedTuple):
    """
        name: tSAND:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSAND:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSAND:USD"

    def __str__(self):
        return "tSAND:USD"

    def __call__(self):
        return "tSAND:USD"


SAND_USD = SAND_USD()
"""
    name: tSAND:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class SAND_UST(NamedTuple):
    """
        name: tSAND:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSAND:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSAND:UST"

    def __str__(self):
        return "tSAND:UST"

    def __call__(self):
        return "tSAND:UST"


SAND_UST = SAND_UST()
"""
    name: tSAND:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class SANDF0_USTF0(NamedTuple):
    """
        name: tSANDF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSANDF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 2.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSANDF0:USTF0"

    def __str__(self):
        return "tSANDF0:USTF0"

    def __call__(self):
        return "tSANDF0:USTF0"


SANDF0_USTF0 = SANDF0_USTF0()
"""
    name: tSANDF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 2.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class SENATE_USD(NamedTuple):
    """
        name: tSENATE:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSENATE:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 20.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSENATE:USD"

    def __str__(self):
        return "tSENATE:USD"

    def __call__(self):
        return "tSENATE:USD"


SENATE_USD = SENATE_USD()
"""
    name: tSENATE:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 20.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class SGBUSD(NamedTuple):
    """
        name: tSGBUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSGBUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 52.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSGBUSD"

    def __str__(self):
        return "tSGBUSD"

    def __call__(self):
        return "tSGBUSD"


SGBUSD = SGBUSD()
"""
    name: tSGBUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 52.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class SGBUST(NamedTuple):
    """
        name: tSGBUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSGBUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 52.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSGBUST"

    def __str__(self):
        return "tSGBUST"

    def __call__(self):
        return "tSGBUST"


SGBUST = SGBUST()
"""
    name: tSGBUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 52.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class SHFT_USD(NamedTuple):
    """
        name: tSHFT:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSHFT:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 52.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSHFT:USD"

    def __str__(self):
        return "tSHFT:USD"

    def __call__(self):
        return "tSHFT:USD"


SHFT_USD = SHFT_USD()
"""
    name: tSHFT:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 52.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class SHFT_UST(NamedTuple):
    """
        name: tSHFT:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSHFT:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 52.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSHFT:UST"

    def __str__(self):
        return "tSHFT:UST"

    def __call__(self):
        return "tSHFT:UST"


SHFT_UST = SHFT_UST()
"""
    name: tSHFT:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 52.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class SHIB_USD(NamedTuple):
    """
        name: tSHIB:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 187004.0
        max_order_size: 5000000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSHIB:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 187004.0
    max_order_size: float = 5000000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSHIB:USD"

    def __str__(self):
        return "tSHIB:USD"

    def __call__(self):
        return "tSHIB:USD"


SHIB_USD = SHIB_USD()
"""
    name: tSHIB:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 187004.0
    max_order_size: 5000000000.0
    has_margin: True
    exchange: bitfinex
"""


class SHIB_UST(NamedTuple):
    """
        name: tSHIB:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 187004.0
        max_order_size: 5000000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSHIB:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 187004.0
    max_order_size: float = 5000000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSHIB:UST"

    def __str__(self):
        return "tSHIB:UST"

    def __call__(self):
        return "tSHIB:UST"


SHIB_UST = SHIB_UST()
"""
    name: tSHIB:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 187004.0
    max_order_size: 5000000000.0
    has_margin: True
    exchange: bitfinex
"""


class SHIBF0_USTF0(NamedTuple):
    """
        name: tSHIBF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 187004.0
        max_order_size: 5000000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSHIBF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 187004.0
    max_order_size: float = 5000000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSHIBF0:USTF0"

    def __str__(self):
        return "tSHIBF0:USTF0"

    def __call__(self):
        return "tSHIBF0:USTF0"


SHIBF0_USTF0 = SHIBF0_USTF0()
"""
    name: tSHIBF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 187004.0
    max_order_size: 5000000000.0
    has_margin: True
    exchange: bitfinex
"""


class SIDUS_USD(NamedTuple):
    """
        name: tSIDUS:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 664.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSIDUS:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 664.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSIDUS:USD"

    def __str__(self):
        return "tSIDUS:USD"

    def __call__(self):
        return "tSIDUS:USD"


SIDUS_USD = SIDUS_USD()
"""
    name: tSIDUS:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 664.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class SMRUSD(NamedTuple):
    """
        name: tSMRUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 700000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSMRUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 700000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSMRUSD"

    def __str__(self):
        return "tSMRUSD"

    def __call__(self):
        return "tSMRUSD"


SMRUSD = SMRUSD()
"""
    name: tSMRUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 700000.0
    has_margin: False
    exchange: bitfinex
"""


class SMRUST(NamedTuple):
    """
        name: tSMRUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 700000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSMRUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 700000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSMRUST"

    def __str__(self):
        return "tSMRUST"

    def __call__(self):
        return "tSMRUST"


SMRUST = SMRUST()
"""
    name: tSMRUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 700000.0
    has_margin: False
    exchange: bitfinex
"""


class SNTUSD(NamedTuple):
    """
        name: tSNTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 48.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSNTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 48.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSNTUSD"

    def __str__(self):
        return "tSNTUSD"

    def __call__(self):
        return "tSNTUSD"


SNTUSD = SNTUSD()
"""
    name: tSNTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 48.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class SNXUSD(NamedTuple):
    """
        name: tSNXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSNXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.8
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSNXUSD"

    def __str__(self):
        return "tSNXUSD"

    def __call__(self):
        return "tSNXUSD"


SNXUSD = SNXUSD()
"""
    name: tSNXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.8
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class SNXUST(NamedTuple):
    """
        name: tSNXUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSNXUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.8
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSNXUST"

    def __str__(self):
        return "tSNXUST"

    def __call__(self):
        return "tSNXUST"


SNXUST = SNXUST()
"""
    name: tSNXUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.8
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class SOLBTC(NamedTuple):
    """
        name: tSOLBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.06
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.06
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSOLBTC"

    def __str__(self):
        return "tSOLBTC"

    def __call__(self):
        return "tSOLBTC"


SOLBTC = SOLBTC()
"""
    name: tSOLBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.06
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class SOLF0_BTCF0(NamedTuple):
    """
        name: tSOLF0:BTCF0
        precision: 5
        min_margin: 2.5
        initial_margin: 5.0
        min_order_size: 0.06
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLF0:BTCF0"
    precision: int = 5
    min_margin: float = 2.5
    initial_margin: float = 5.0
    min_order_size: float = 0.06
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSOLF0:BTCF0"

    def __str__(self):
        return "tSOLF0:BTCF0"

    def __call__(self):
        return "tSOLF0:BTCF0"


SOLF0_BTCF0 = SOLF0_BTCF0()
"""
    name: tSOLF0:BTCF0
    precision: 5
    min_margin: 2.5
    initial_margin: 5.0
    min_order_size: 0.06
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class SOLF0_USTF0(NamedTuple):
    """
        name: tSOLF0:USTF0
        precision: 5
        min_margin: 2.5
        initial_margin: 5.0
        min_order_size: 0.06
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLF0:USTF0"
    precision: int = 5
    min_margin: float = 2.5
    initial_margin: float = 5.0
    min_order_size: float = 0.06
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSOLF0:USTF0"

    def __str__(self):
        return "tSOLF0:USTF0"

    def __call__(self):
        return "tSOLF0:USTF0"


SOLF0_USTF0 = SOLF0_USTF0()
"""
    name: tSOLF0:USTF0
    precision: 5
    min_margin: 2.5
    initial_margin: 5.0
    min_order_size: 0.06
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class SOLUSD(NamedTuple):
    """
        name: tSOLUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.06
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.06
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSOLUSD"

    def __str__(self):
        return "tSOLUSD"

    def __call__(self):
        return "tSOLUSD"


SOLUSD = SOLUSD()
"""
    name: tSOLUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.06
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class SOLUST(NamedTuple):
    """
        name: tSOLUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.06
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.06
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSOLUST"

    def __str__(self):
        return "tSOLUST"

    def __call__(self):
        return "tSOLUST"


SOLUST = SOLUST()
"""
    name: tSOLUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.06
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class SPAIN35IXF0_USTF0(NamedTuple):
    """
        name: tSPAIN35IXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSPAIN35IXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 10.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSPAIN35IXF0:USTF0"

    def __str__(self):
        return "tSPAIN35IXF0:USTF0"

    def __call__(self):
        return "tSPAIN35IXF0:USTF0"


SPAIN35IXF0_USTF0 = SPAIN35IXF0_USTF0()
"""
    name: tSPAIN35IXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 10.0
    has_margin: True
    exchange: bitfinex
"""


class SPELL_USD(NamedTuple):
    """
        name: tSPELL:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1640.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSPELL:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 1640.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSPELL:USD"

    def __str__(self):
        return "tSPELL:USD"

    def __call__(self):
        return "tSPELL:USD"


SPELL_USD = SPELL_USD()
"""
    name: tSPELL:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 1640.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class STGF0_USTF0(NamedTuple):
    """
        name: tSTGF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSTGF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 4.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSTGF0:USTF0"

    def __str__(self):
        return "tSTGF0:USTF0"

    def __call__(self):
        return "tSTGF0:USTF0"


STGF0_USTF0 = STGF0_USTF0()
"""
    name: tSTGF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 4.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class STGUSD(NamedTuple):
    """
        name: tSTGUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSTGUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSTGUSD"

    def __str__(self):
        return "tSTGUSD"

    def __call__(self):
        return "tSTGUSD"


STGUSD = STGUSD()
"""
    name: tSTGUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class STGUST(NamedTuple):
    """
        name: tSTGUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSTGUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSTGUST"

    def __str__(self):
        return "tSTGUST"

    def __call__(self):
        return "tSTGUST"


STGUST = STGUST()
"""
    name: tSTGUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class STJUSD(NamedTuple):
    """
        name: tSTJUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 30000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSTJUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 30000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSTJUSD"

    def __str__(self):
        return "tSTJUSD"

    def __call__(self):
        return "tSTJUSD"


STJUSD = STJUSD()
"""
    name: tSTJUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 30000.0
    has_margin: False
    exchange: bitfinex
"""


class SUKU_USD(NamedTuple):
    """
        name: tSUKU:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUKU:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 18.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSUKU:USD"

    def __str__(self):
        return "tSUKU:USD"

    def __call__(self):
        return "tSUKU:USD"


SUKU_USD = SUKU_USD()
"""
    name: tSUKU:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 18.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class SUKU_UST(NamedTuple):
    """
        name: tSUKU:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUKU:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 18.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSUKU:UST"

    def __str__(self):
        return "tSUKU:UST"

    def __call__(self):
        return "tSUKU:UST"


SUKU_UST = SUKU_UST()
"""
    name: tSUKU:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 18.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class SUNUSD(NamedTuple):
    """
        name: tSUNUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 216.0
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUNUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 216.0
    max_order_size: float = 10000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSUNUSD"

    def __str__(self):
        return "tSUNUSD"

    def __call__(self):
        return "tSUNUSD"


SUNUSD = SUNUSD()
"""
    name: tSUNUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 216.0
    max_order_size: 10000000.0
    has_margin: False
    exchange: bitfinex
"""


class SUNUST(NamedTuple):
    """
        name: tSUNUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 216.0
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUNUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 216.0
    max_order_size: float = 10000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSUNUST"

    def __str__(self):
        return "tSUNUST"

    def __call__(self):
        return "tSUNUST"


SUNUST = SUNUST()
"""
    name: tSUNUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 216.0
    max_order_size: 10000000.0
    has_margin: False
    exchange: bitfinex
"""


class SUSHI_USD(NamedTuple):
    """
        name: tSUSHI:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSUSHI:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSUSHI:USD"

    def __str__(self):
        return "tSUSHI:USD"

    def __call__(self):
        return "tSUSHI:USD"


SUSHI_USD = SUSHI_USD()
"""
    name: tSUSHI:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class SUSHI_UST(NamedTuple):
    """
        name: tSUSHI:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSUSHI:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSUSHI:UST"

    def __str__(self):
        return "tSUSHI:UST"

    def __call__(self):
        return "tSUSHI:UST"


SUSHI_UST = SUSHI_UST()
"""
    name: tSUSHI:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class SUSHIF0_USTF0(NamedTuple):
    """
        name: tSUSHIF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSUSHIF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 2.0
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSUSHIF0:USTF0"

    def __str__(self):
        return "tSUSHIF0:USTF0"

    def __call__(self):
        return "tSUSHIF0:USTF0"


SUSHIF0_USTF0 = SUSHIF0_USTF0()
"""
    name: tSUSHIF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 2.0
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class SWEAT_USD(NamedTuple):
    """
        name: tSWEAT:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 7000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSWEAT:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 7000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSWEAT:USD"

    def __str__(self):
        return "tSWEAT:USD"

    def __call__(self):
        return "tSWEAT:USD"


SWEAT_USD = SWEAT_USD()
"""
    name: tSWEAT:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 7000000.0
    has_margin: False
    exchange: bitfinex
"""


class SWEAT_UST(NamedTuple):
    """
        name: tSWEAT:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 7000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSWEAT:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 7000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSWEAT:UST"

    def __str__(self):
        return "tSWEAT:UST"

    def __call__(self):
        return "tSWEAT:UST"


SWEAT_UST = SWEAT_UST()
"""
    name: tSWEAT:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 7000000.0
    has_margin: False
    exchange: bitfinex
"""


class SXXUSD(NamedTuple):
    """
        name: tSXXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSXXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 8.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tSXXUSD"

    def __str__(self):
        return "tSXXUSD"

    def __call__(self):
        return "tSXXUSD"


SXXUSD = SXXUSD()
"""
    name: tSXXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 8.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class TERRAUST_USD(NamedTuple):
    """
        name: tTERRAUST:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 100.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTERRAUST:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 100.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTERRAUST:USD"

    def __str__(self):
        return "tTERRAUST:USD"

    def __call__(self):
        return "tTERRAUST:USD"


TERRAUST_USD = TERRAUST_USD()
"""
    name: tTERRAUST:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 100.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class TESTADA_TESTUSD(NamedTuple):
    """
        name: tTESTADA:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTADA:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTADA:TESTUSD"

    def __str__(self):
        return "tTESTADA:TESTUSD"

    def __call__(self):
        return "tTESTADA:TESTUSD"


TESTADA_TESTUSD = TESTADA_TESTUSD()
"""
    name: tTESTADA:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTALGO_TESTUSD(NamedTuple):
    """
        name: tTESTALGO:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTALGO:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTALGO:TESTUSD"

    def __str__(self):
        return "tTESTALGO:TESTUSD"

    def __call__(self):
        return "tTESTALGO:TESTUSD"


TESTALGO_TESTUSD = TESTALGO_TESTUSD()
"""
    name: tTESTALGO:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTAPT_TESTUSD(NamedTuple):
    """
        name: tTESTAPT:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTAPT:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTAPT:TESTUSD"

    def __str__(self):
        return "tTESTAPT:TESTUSD"

    def __call__(self):
        return "tTESTAPT:TESTUSD"


TESTAPT_TESTUSD = TESTAPT_TESTUSD()
"""
    name: tTESTAPT:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTAVAX_TESTUSD(NamedTuple):
    """
        name: tTESTAVAX:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTAVAX:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTAVAX:TESTUSD"

    def __str__(self):
        return "tTESTAVAX:TESTUSD"

    def __call__(self):
        return "tTESTAVAX:TESTUSD"


TESTAVAX_TESTUSD = TESTAVAX_TESTUSD()
"""
    name: tTESTAVAX:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTBTC_TESTUSD(NamedTuple):
    """
        name: tTESTBTC:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTBTC:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00006
    max_order_size: float = 100.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTBTC:TESTUSD"

    def __str__(self):
        return "tTESTBTC:TESTUSD"

    def __call__(self):
        return "tTESTBTC:TESTUSD"


TESTBTC_TESTUSD = TESTBTC_TESTUSD()
"""
    name: tTESTBTC:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00006
    max_order_size: 100.0
    has_margin: True
    exchange: bitfinex
"""


class TESTBTC_TESTUSDT(NamedTuple):
    """
        name: tTESTBTC:TESTUSDT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTBTC:TESTUSDT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00006
    max_order_size: float = 100.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTBTC:TESTUSDT"

    def __str__(self):
        return "tTESTBTC:TESTUSDT"

    def __call__(self):
        return "tTESTBTC:TESTUSDT"


TESTBTC_TESTUSDT = TESTBTC_TESTUSDT()
"""
    name: tTESTBTC:TESTUSDT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00006
    max_order_size: 100.0
    has_margin: True
    exchange: bitfinex
"""


class TESTBTCF0_TESTUSDTF0(NamedTuple):
    """
        name: tTESTBTCF0:TESTUSDTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.00006
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTBTCF0:TESTUSDTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.00006
    max_order_size: float = 1000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTBTCF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTBTCF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTBTCF0:TESTUSDTF0"


TESTBTCF0_TESTUSDTF0 = TESTBTCF0_TESTUSDTF0()
"""
    name: tTESTBTCF0:TESTUSDTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.00006
    max_order_size: 1000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTDOGE_TESTUSD(NamedTuple):
    """
        name: tTESTDOGE:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTDOGE:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTDOGE:TESTUSD"

    def __str__(self):
        return "tTESTDOGE:TESTUSD"

    def __call__(self):
        return "tTESTDOGE:TESTUSD"


TESTDOGE_TESTUSD = TESTDOGE_TESTUSD()
"""
    name: tTESTDOGE:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTDOT_TESTUSD(NamedTuple):
    """
        name: tTESTDOT:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTDOT:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTDOT:TESTUSD"

    def __str__(self):
        return "tTESTDOT:TESTUSD"

    def __call__(self):
        return "tTESTDOT:TESTUSD"


TESTDOT_TESTUSD = TESTDOT_TESTUSD()
"""
    name: tTESTDOT:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTDOTF0_TESTUSDTF0(NamedTuple):
    """
        name: tTESTDOTF0:TESTUSDTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTDOTF0:TESTUSDTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTDOTF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTDOTF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTDOTF0:TESTUSDTF0"


TESTDOTF0_TESTUSDTF0 = TESTDOTF0_TESTUSDTF0()
"""
    name: tTESTDOTF0:TESTUSDTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTEOS_TESTUSD(NamedTuple):
    """
        name: tTESTEOS:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTEOS:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTEOS:TESTUSD"

    def __str__(self):
        return "tTESTEOS:TESTUSD"

    def __call__(self):
        return "tTESTEOS:TESTUSD"


TESTEOS_TESTUSD = TESTEOS_TESTUSD()
"""
    name: tTESTEOS:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTETH_TESTUSD(NamedTuple):
    """
        name: tTESTETH:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTETH:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTETH:TESTUSD"

    def __str__(self):
        return "tTESTETH:TESTUSD"

    def __call__(self):
        return "tTESTETH:TESTUSD"


TESTETH_TESTUSD = TESTETH_TESTUSD()
"""
    name: tTESTETH:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTFIL_TESTUSD(NamedTuple):
    """
        name: tTESTFIL:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTFIL:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTFIL:TESTUSD"

    def __str__(self):
        return "tTESTFIL:TESTUSD"

    def __call__(self):
        return "tTESTFIL:TESTUSD"


TESTFIL_TESTUSD = TESTFIL_TESTUSD()
"""
    name: tTESTFIL:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTLTC_TESTUSD(NamedTuple):
    """
        name: tTESTLTC:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTLTC:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTLTC:TESTUSD"

    def __str__(self):
        return "tTESTLTC:TESTUSD"

    def __call__(self):
        return "tTESTLTC:TESTUSD"


TESTLTC_TESTUSD = TESTLTC_TESTUSD()
"""
    name: tTESTLTC:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTMATIC_TESTUSD(NamedTuple):
    """
        name: tTESTMATIC:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTMATIC:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTMATIC:TESTUSD"

    def __str__(self):
        return "tTESTMATIC:TESTUSD"

    def __call__(self):
        return "tTESTMATIC:TESTUSD"


TESTMATIC_TESTUSD = TESTMATIC_TESTUSD()
"""
    name: tTESTMATIC:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTMATIC_TESTUSDT(NamedTuple):
    """
        name: tTESTMATIC:TESTUSDT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTESTMATIC:TESTUSDT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTMATIC:TESTUSDT"

    def __str__(self):
        return "tTESTMATIC:TESTUSDT"

    def __call__(self):
        return "tTESTMATIC:TESTUSDT"


TESTMATIC_TESTUSDT = TESTMATIC_TESTUSDT()
"""
    name: tTESTMATIC:TESTUSDT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: False
    exchange: bitfinex
"""


class TESTMATICF0_TESTUSDTF0(NamedTuple):
    """
        name: tTESTMATICF0:TESTUSDTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTMATICF0:TESTUSDTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTMATICF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTMATICF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTMATICF0:TESTUSDTF0"


TESTMATICF0_TESTUSDTF0 = TESTMATICF0_TESTUSDTF0()
"""
    name: tTESTMATICF0:TESTUSDTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTNEAR_TESTUSD(NamedTuple):
    """
        name: tTESTNEAR:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTNEAR:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTNEAR:TESTUSD"

    def __str__(self):
        return "tTESTNEAR:TESTUSD"

    def __call__(self):
        return "tTESTNEAR:TESTUSD"


TESTNEAR_TESTUSD = TESTNEAR_TESTUSD()
"""
    name: tTESTNEAR:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTSOL_TESTUSD(NamedTuple):
    """
        name: tTESTSOL:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTSOL:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTSOL:TESTUSD"

    def __str__(self):
        return "tTESTSOL:TESTUSD"

    def __call__(self):
        return "tTESTSOL:TESTUSD"


TESTSOL_TESTUSD = TESTSOL_TESTUSD()
"""
    name: tTESTSOL:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTSOLF0_TESTUSDTF0(NamedTuple):
    """
        name: tTESTSOLF0:TESTUSDTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTSOLF0:TESTUSDTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTSOLF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTSOLF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTSOLF0:TESTUSDTF0"


TESTSOLF0_TESTUSDTF0 = TESTSOLF0_TESTUSDTF0()
"""
    name: tTESTSOLF0:TESTUSDTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTXAUT_TESTUSD(NamedTuple):
    """
        name: tTESTXAUT:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTXAUT:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTXAUT:TESTUSD"

    def __str__(self):
        return "tTESTXAUT:TESTUSD"

    def __call__(self):
        return "tTESTXAUT:TESTUSD"


TESTXAUT_TESTUSD = TESTXAUT_TESTUSD()
"""
    name: tTESTXAUT:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class TESTXTZ_TESTUSD(NamedTuple):
    """
        name: tTESTXTZ:TESTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTXTZ:TESTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTXTZ:TESTUSD"

    def __str__(self):
        return "tTESTXTZ:TESTUSD"

    def __call__(self):
        return "tTESTXTZ:TESTUSD"


TESTXTZ_TESTUSD = TESTXTZ_TESTUSD()
"""
    name: tTESTXTZ:TESTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class THETA_USD(NamedTuple):
    """
        name: tTHETA:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTHETA:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTHETA:USD"

    def __str__(self):
        return "tTHETA:USD"

    def __call__(self):
        return "tTHETA:USD"


THETA_USD = THETA_USD()
"""
    name: tTHETA:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class THETA_UST(NamedTuple):
    """
        name: tTHETA:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTHETA:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTHETA:UST"

    def __str__(self):
        return "tTHETA:UST"

    def __call__(self):
        return "tTHETA:UST"


THETA_UST = THETA_UST()
"""
    name: tTHETA:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class TLOS_USD(NamedTuple):
    """
        name: tTLOS:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTLOS:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 8.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTLOS:USD"

    def __str__(self):
        return "tTLOS:USD"

    def __call__(self):
        return "tTLOS:USD"


TLOS_USD = TLOS_USD()
"""
    name: tTLOS:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 8.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class TONUSD(NamedTuple):
    """
        name: tTONUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTONUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTONUSD"

    def __str__(self):
        return "tTONUSD"

    def __call__(self):
        return "tTONUSD"


TONUSD = TONUSD()
"""
    name: tTONUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class TONUST(NamedTuple):
    """
        name: tTONUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTONUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTONUST"

    def __str__(self):
        return "tTONUST"

    def __call__(self):
        return "tTONUST"


TONUST = TONUST()
"""
    name: tTONUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class TRADE_USD(NamedTuple):
    """
        name: tTRADE:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 28.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRADE:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 28.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTRADE:USD"

    def __str__(self):
        return "tTRADE:USD"

    def __call__(self):
        return "tTRADE:USD"


TRADE_USD = TRADE_USD()
"""
    name: tTRADE:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 28.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class TRADE_UST(NamedTuple):
    """
        name: tTRADE:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 28.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRADE:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 28.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTRADE:UST"

    def __str__(self):
        return "tTRADE:UST"

    def __call__(self):
        return "tTRADE:UST"


TRADE_UST = TRADE_UST()
"""
    name: tTRADE:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 28.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class TREEB_USD(NamedTuple):
    """
        name: tTREEB:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 3000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTREEB:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 3000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTREEB:USD"

    def __str__(self):
        return "tTREEB:USD"

    def __call__(self):
        return "tTREEB:USD"


TREEB_USD = TREEB_USD()
"""
    name: tTREEB:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 3000000.0
    has_margin: False
    exchange: bitfinex
"""


class TREEB_UST(NamedTuple):
    """
        name: tTREEB:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 3000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTREEB:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 3000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTREEB:UST"

    def __str__(self):
        return "tTREEB:UST"

    def __call__(self):
        return "tTREEB:UST"


TREEB_UST = TREEB_UST()
"""
    name: tTREEB:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 3000000.0
    has_margin: False
    exchange: bitfinex
"""


class TRXBTC(NamedTuple):
    """
        name: tTRXBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 34.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRXBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 34.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTRXBTC"

    def __str__(self):
        return "tTRXBTC"

    def __call__(self):
        return "tTRXBTC"


TRXBTC = TRXBTC()
"""
    name: tTRXBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 34.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class TRXETH(NamedTuple):
    """
        name: tTRXETH
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 34.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRXETH"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 34.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTRXETH"

    def __str__(self):
        return "tTRXETH"

    def __call__(self):
        return "tTRXETH"


TRXETH = TRXETH()
"""
    name: tTRXETH
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 34.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class TRXEUR(NamedTuple):
    """
        name: tTRXEUR
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 34.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRXEUR"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 34.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTRXEUR"

    def __str__(self):
        return "tTRXEUR"

    def __call__(self):
        return "tTRXEUR"


TRXEUR = TRXEUR()
"""
    name: tTRXEUR
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 34.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class TRXF0_USTF0(NamedTuple):
    """
        name: tTRXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 24.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTRXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 24.0
    max_order_size: float = 1000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTRXF0:USTF0"

    def __str__(self):
        return "tTRXF0:USTF0"

    def __call__(self):
        return "tTRXF0:USTF0"


TRXF0_USTF0 = TRXF0_USTF0()
"""
    name: tTRXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 24.0
    max_order_size: 1000000.0
    has_margin: True
    exchange: bitfinex
"""


class TRXUSD(NamedTuple):
    """
        name: tTRXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 34.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTRXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 34.0
    max_order_size: float = 1000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTRXUSD"

    def __str__(self):
        return "tTRXUSD"

    def __call__(self):
        return "tTRXUSD"


TRXUSD = TRXUSD()
"""
    name: tTRXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 34.0
    max_order_size: 1000000.0
    has_margin: True
    exchange: bitfinex
"""


class TRXUST(NamedTuple):
    """
        name: tTRXUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 24.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTRXUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 24.0
    max_order_size: float = 1000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTRXUST"

    def __str__(self):
        return "tTRXUST"

    def __call__(self):
        return "tTRXUST"


TRXUST = TRXUST()
"""
    name: tTRXUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 24.0
    max_order_size: 1000000.0
    has_margin: True
    exchange: bitfinex
"""


class TRYUST(NamedTuple):
    """
        name: tTRYUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRYUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTRYUST"

    def __str__(self):
        return "tTRYUST"

    def __call__(self):
        return "tTRYUST"


TRYUST = TRYUST()
"""
    name: tTRYUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class TSDUSD(NamedTuple):
    """
        name: tTSDUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTSDUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTSDUSD"

    def __str__(self):
        return "tTSDUSD"

    def __call__(self):
        return "tTSDUSD"


TSDUSD = TSDUSD()
"""
    name: tTSDUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class TSDUST(NamedTuple):
    """
        name: tTSDUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTSDUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTSDUST"

    def __str__(self):
        return "tTSDUST"

    def __call__(self):
        return "tTSDUST"


TSDUST = TSDUST()
"""
    name: tTSDUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class UDCUSD(NamedTuple):
    """
        name: tUDCUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUDCUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUDCUSD"

    def __str__(self):
        return "tUDCUSD"

    def __call__(self):
        return "tUDCUSD"


UDCUSD = UDCUSD()
"""
    name: tUDCUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class UDCUST(NamedTuple):
    """
        name: tUDCUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUDCUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUDCUST"

    def __str__(self):
        return "tUDCUST"

    def __call__(self):
        return "tUDCUST"


UDCUST = UDCUST()
"""
    name: tUDCUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 500000.0
    has_margin: False
    exchange: bitfinex
"""


class UK100IXF0_USTF0(NamedTuple):
    """
        name: tUK100IXF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUK100IXF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 10.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUK100IXF0:USTF0"

    def __str__(self):
        return "tUK100IXF0:USTF0"

    def __call__(self):
        return "tUK100IXF0:USTF0"


UK100IXF0_USTF0 = UK100IXF0_USTF0()
"""
    name: tUK100IXF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 10.0
    has_margin: True
    exchange: bitfinex
"""


class UKOILF0_USTF0(NamedTuple):
    """
        name: tUKOILF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUKOILF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUKOILF0:USTF0"

    def __str__(self):
        return "tUKOILF0:USTF0"

    def __call__(self):
        return "tUKOILF0:USTF0"


UKOILF0_USTF0 = UKOILF0_USTF0()
"""
    name: tUKOILF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class UNIF0_USTF0(NamedTuple):
    """
        name: tUNIF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.4
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUNIF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.4
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUNIF0:USTF0"

    def __str__(self):
        return "tUNIF0:USTF0"

    def __call__(self):
        return "tUNIF0:USTF0"


UNIF0_USTF0 = UNIF0_USTF0()
"""
    name: tUNIF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.4
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class UNIUSD(NamedTuple):
    """
        name: tUNIUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUNIUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUNIUSD"

    def __str__(self):
        return "tUNIUSD"

    def __call__(self):
        return "tUNIUSD"


UNIUSD = UNIUSD()
"""
    name: tUNIUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class UNIUST(NamedTuple):
    """
        name: tUNIUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUNIUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.4
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUNIUST"

    def __str__(self):
        return "tUNIUST"

    def __call__(self):
        return "tUNIUST"


UNIUST = UNIUST()
"""
    name: tUNIUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.4
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class UOSBTC(NamedTuple):
    """
        name: tUOSBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 400000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUOSBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 400000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUOSBTC"

    def __str__(self):
        return "tUOSBTC"

    def __call__(self):
        return "tUOSBTC"


UOSBTC = UOSBTC()
"""
    name: tUOSBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 400000.0
    has_margin: False
    exchange: bitfinex
"""


class UOSUSD(NamedTuple):
    """
        name: tUOSUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 400000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUOSUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 4.0
    max_order_size: float = 400000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUOSUSD"

    def __str__(self):
        return "tUOSUSD"

    def __call__(self):
        return "tUOSUSD"


UOSUSD = UOSUSD()
"""
    name: tUOSUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 4.0
    max_order_size: 400000.0
    has_margin: False
    exchange: bitfinex
"""


class UST_CNHT(NamedTuple):
    """
        name: tUST:CNHT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUST:CNHT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUST:CNHT"

    def __str__(self):
        return "tUST:CNHT"

    def __call__(self):
        return "tUST:CNHT"


UST_CNHT = UST_CNHT()
"""
    name: tUST:CNHT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class UST_MXNT(NamedTuple):
    """
        name: tUST:MXNT
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUST:MXNT"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUST:MXNT"

    def __str__(self):
        return "tUST:MXNT"

    def __call__(self):
        return "tUST:MXNT"


UST_MXNT = UST_MXNT()
"""
    name: tUST:MXNT
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10000000.0
    has_margin: False
    exchange: bitfinex
"""


class USTUSD(NamedTuple):
    """
        name: tUSTUSD
        precision: 5
        min_margin: 5.0
        initial_margin: 10.0
        min_order_size: 2.0
        max_order_size: 5000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUSTUSD"
    precision: int = 5
    min_margin: float = 5.0
    initial_margin: float = 10.0
    min_order_size: float = 2.0
    max_order_size: float = 5000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUSTUSD"

    def __str__(self):
        return "tUSTUSD"

    def __call__(self):
        return "tUSTUSD"


USTUSD = USTUSD()
"""
    name: tUSTUSD
    precision: 5
    min_margin: 5.0
    initial_margin: 10.0
    min_order_size: 2.0
    max_order_size: 5000000.0
    has_margin: True
    exchange: bitfinex
"""


class UTKUSD(NamedTuple):
    """
        name: tUTKUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 300000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUTKUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 10.0
    max_order_size: float = 300000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tUTKUSD"

    def __str__(self):
        return "tUTKUSD"

    def __call__(self):
        return "tUTKUSD"


UTKUSD = UTKUSD()
"""
    name: tUTKUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 10.0
    max_order_size: 300000.0
    has_margin: False
    exchange: bitfinex
"""


class VELO_USD(NamedTuple):
    """
        name: tVELO:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 1750000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVELO:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 66.0
    max_order_size: float = 1750000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tVELO:USD"

    def __str__(self):
        return "tVELO:USD"

    def __call__(self):
        return "tVELO:USD"


VELO_USD = VELO_USD()
"""
    name: tVELO:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 66.0
    max_order_size: 1750000.0
    has_margin: False
    exchange: bitfinex
"""


class VELO_UST(NamedTuple):
    """
        name: tVELO:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 1750000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVELO:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 66.0
    max_order_size: float = 1750000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tVELO:UST"

    def __str__(self):
        return "tVELO:UST"

    def __call__(self):
        return "tVELO:UST"


VELO_UST = VELO_UST()
"""
    name: tVELO:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 66.0
    max_order_size: 1750000.0
    has_margin: False
    exchange: bitfinex
"""


class VETBTC(NamedTuple):
    """
        name: tVETBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVETBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 66.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tVETBTC"

    def __str__(self):
        return "tVETBTC"

    def __call__(self):
        return "tVETBTC"


VETBTC = VETBTC()
"""
    name: tVETBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 66.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class VETUSD(NamedTuple):
    """
        name: tVETUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVETUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 66.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tVETUSD"

    def __str__(self):
        return "tVETUSD"

    def __call__(self):
        return "tVETUSD"


VETUSD = VETUSD()
"""
    name: tVETUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 66.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class VETUST(NamedTuple):
    """
        name: tVETUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVETUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 66.0
    max_order_size: float = 5000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tVETUST"

    def __str__(self):
        return "tVETUST"

    def __call__(self):
        return "tVETUST"


VETUST = VETUST()
"""
    name: tVETUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 66.0
    max_order_size: 5000000.0
    has_margin: False
    exchange: bitfinex
"""


class VRAUSD(NamedTuple):
    """
        name: tVRAUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 286.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVRAUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 286.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tVRAUSD"

    def __str__(self):
        return "tVRAUSD"

    def __call__(self):
        return "tVRAUSD"


VRAUSD = VRAUSD()
"""
    name: tVRAUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 286.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class VRAUST(NamedTuple):
    """
        name: tVRAUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 286.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVRAUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 286.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tVRAUST"

    def __str__(self):
        return "tVRAUST"

    def __call__(self):
        return "tVRAUST"


VRAUST = VRAUST()
"""
    name: tVRAUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 286.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class VSYUSD(NamedTuple):
    """
        name: tVSYUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 432.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVSYUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 432.0
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tVSYUSD"

    def __str__(self):
        return "tVSYUSD"

    def __call__(self):
        return "tVSYUSD"


VSYUSD = VSYUSD()
"""
    name: tVSYUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 432.0
    max_order_size: 250000.0
    has_margin: False
    exchange: bitfinex
"""


class WAVES_USD(NamedTuple):
    """
        name: tWAVES:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWAVES:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWAVES:USD"

    def __str__(self):
        return "tWAVES:USD"

    def __call__(self):
        return "tWAVES:USD"


WAVES_USD = WAVES_USD()
"""
    name: tWAVES:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class WAVES_UST(NamedTuple):
    """
        name: tWAVES:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWAVES:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWAVES:UST"

    def __str__(self):
        return "tWAVES:UST"

    def __call__(self):
        return "tWAVES:UST"


WAVES_UST = WAVES_UST()
"""
    name: tWAVES:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class WAVESF0_USTF0(NamedTuple):
    """
        name: tWAVESF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tWAVESF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.2
    max_order_size: float = 50000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWAVESF0:USTF0"

    def __str__(self):
        return "tWAVESF0:USTF0"

    def __call__(self):
        return "tWAVESF0:USTF0"


WAVESF0_USTF0 = WAVESF0_USTF0()
"""
    name: tWAVESF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.2
    max_order_size: 50000.0
    has_margin: True
    exchange: bitfinex
"""


class WAXUSD(NamedTuple):
    """
        name: tWAXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 16.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWAXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 16.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWAXUSD"

    def __str__(self):
        return "tWAXUSD"

    def __call__(self):
        return "tWAXUSD"


WAXUSD = WAXUSD()
"""
    name: tWAXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 16.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class WBTBTC(NamedTuple):
    """
        name: tWBTBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWBTBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 10.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWBTBTC"

    def __str__(self):
        return "tWBTBTC"

    def __call__(self):
        return "tWBTBTC"


WBTBTC = WBTBTC()
"""
    name: tWBTBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 10.0
    has_margin: False
    exchange: bitfinex
"""


class WBTUSD(NamedTuple):
    """
        name: tWBTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 10.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWBTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.00006
    max_order_size: float = 10.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWBTUSD"

    def __str__(self):
        return "tWBTUSD"

    def __call__(self):
        return "tWBTUSD"


WBTUSD = WBTUSD()
"""
    name: tWBTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.00006
    max_order_size: 10.0
    has_margin: False
    exchange: bitfinex
"""


class WILD_USD(NamedTuple):
    """
        name: tWILD:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWILD:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWILD:USD"

    def __str__(self):
        return "tWILD:USD"

    def __call__(self):
        return "tWILD:USD"


WILD_USD = WILD_USD()
"""
    name: tWILD:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class WILD_UST(NamedTuple):
    """
        name: tWILD:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWILD:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWILD:UST"

    def __str__(self):
        return "tWILD:UST"

    def __call__(self):
        return "tWILD:UST"


WILD_UST = WILD_UST()
"""
    name: tWILD:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class WMINIMA_USD(NamedTuple):
    """
        name: tWMINIMA:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 150000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWMINIMA:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 150000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWMINIMA:USD"

    def __str__(self):
        return "tWMINIMA:USD"

    def __call__(self):
        return "tWMINIMA:USD"


WMINIMA_USD = WMINIMA_USD()
"""
    name: tWMINIMA:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 150000.0
    has_margin: False
    exchange: bitfinex
"""


class WMINIMA_UST(NamedTuple):
    """
        name: tWMINIMA:UST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 150000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWMINIMA:UST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 150000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWMINIMA:UST"

    def __str__(self):
        return "tWMINIMA:UST"

    def __call__(self):
        return "tWMINIMA:UST"


WMINIMA_UST = WMINIMA_UST()
"""
    name: tWMINIMA:UST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 150000.0
    has_margin: False
    exchange: bitfinex
"""


class WNCG_USD(NamedTuple):
    """
        name: tWNCG:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 12.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWNCG:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 12.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWNCG:USD"

    def __str__(self):
        return "tWNCG:USD"

    def __call__(self):
        return "tWNCG:USD"


WNCG_USD = WNCG_USD()
"""
    name: tWNCG:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 12.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class WOOUSD(NamedTuple):
    """
        name: tWOOUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWOOUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 10.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWOOUSD"

    def __str__(self):
        return "tWOOUSD"

    def __call__(self):
        return "tWOOUSD"


WOOUSD = WOOUSD()
"""
    name: tWOOUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 10.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class WOOUST(NamedTuple):
    """
        name: tWOOUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWOOUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 10.0
    max_order_size: float = 2500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tWOOUST"

    def __str__(self):
        return "tWOOUST"

    def __call__(self):
        return "tWOOUST"


WOOUST = WOOUST()
"""
    name: tWOOUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 10.0
    max_order_size: 2500000.0
    has_margin: False
    exchange: bitfinex
"""


class XAGF0_USTF0(NamedTuple):
    """
        name: tXAGF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.1
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAGF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.1
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXAGF0:USTF0"

    def __str__(self):
        return "tXAGF0:USTF0"

    def __call__(self):
        return "tXAGF0:USTF0"


XAGF0_USTF0 = XAGF0_USTF0()
"""
    name: tXAGF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.1
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class XAUT_BTC(NamedTuple):
    """
        name: tXAUT:BTC
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 400.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUT:BTC"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.002
    max_order_size: float = 400.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXAUT:BTC"

    def __str__(self):
        return "tXAUT:BTC"

    def __call__(self):
        return "tXAUT:BTC"


XAUT_BTC = XAUT_BTC()
"""
    name: tXAUT:BTC
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.002
    max_order_size: 400.0
    has_margin: True
    exchange: bitfinex
"""


class XAUT_USD(NamedTuple):
    """
        name: tXAUT:USD
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 400.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUT:USD"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.002
    max_order_size: float = 400.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXAUT:USD"

    def __str__(self):
        return "tXAUT:USD"

    def __call__(self):
        return "tXAUT:USD"


XAUT_USD = XAUT_USD()
"""
    name: tXAUT:USD
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.002
    max_order_size: 400.0
    has_margin: True
    exchange: bitfinex
"""


class XAUT_UST(NamedTuple):
    """
        name: tXAUT:UST
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 400.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUT:UST"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 0.002
    max_order_size: float = 400.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXAUT:UST"

    def __str__(self):
        return "tXAUT:UST"

    def __call__(self):
        return "tXAUT:UST"


XAUT_UST = XAUT_UST()
"""
    name: tXAUT:UST
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 0.002
    max_order_size: 400.0
    has_margin: True
    exchange: bitfinex
"""


class XAUTF0_BTCF0(NamedTuple):
    """
        name: tXAUTF0:BTCF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 500.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUTF0:BTCF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.002
    max_order_size: float = 500.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXAUTF0:BTCF0"

    def __str__(self):
        return "tXAUTF0:BTCF0"

    def __call__(self):
        return "tXAUTF0:BTCF0"


XAUTF0_BTCF0 = XAUTF0_BTCF0()
"""
    name: tXAUTF0:BTCF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.002
    max_order_size: 500.0
    has_margin: True
    exchange: bitfinex
"""


class XAUTF0_USTF0(NamedTuple):
    """
        name: tXAUTF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 400.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUTF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.002
    max_order_size: float = 400.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXAUTF0:USTF0"

    def __str__(self):
        return "tXAUTF0:USTF0"

    def __call__(self):
        return "tXAUTF0:USTF0"


XAUTF0_USTF0 = XAUTF0_USTF0()
"""
    name: tXAUTF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.002
    max_order_size: 400.0
    has_margin: True
    exchange: bitfinex
"""


class XCAD_USD(NamedTuple):
    """
        name: tXCAD:USD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 15000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXCAD:USD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 15000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXCAD:USD"

    def __str__(self):
        return "tXCAD:USD"

    def __call__(self):
        return "tXCAD:USD"


XCAD_USD = XCAD_USD()
"""
    name: tXCAD:USD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 15000.0
    has_margin: False
    exchange: bitfinex
"""


class XCNUSD(NamedTuple):
    """
        name: tXCNUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXCNUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXCNUSD"

    def __str__(self):
        return "tXCNUSD"

    def __call__(self):
        return "tXCNUSD"


XCNUSD = XCNUSD()
"""
    name: tXCNUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class XCNUST(NamedTuple):
    """
        name: tXCNUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXCNUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXCNUST"

    def __str__(self):
        return "tXCNUST"

    def __call__(self):
        return "tXCNUST"


XCNUST = XCNUST()
"""
    name: tXCNUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.001
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class XDCUSD(NamedTuple):
    """
        name: tXDCUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 54.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXDCUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 54.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXDCUSD"

    def __str__(self):
        return "tXDCUSD"

    def __call__(self):
        return "tXDCUSD"


XDCUSD = XDCUSD()
"""
    name: tXDCUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 54.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class XDCUST(NamedTuple):
    """
        name: tXDCUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 54.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXDCUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 54.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXDCUST"

    def __str__(self):
        return "tXDCUST"

    def __call__(self):
        return "tXDCUST"


XDCUST = XDCUST()
"""
    name: tXDCUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 54.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class XLMBTC(NamedTuple):
    """
        name: tXLMBTC
        precision: 5
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 14.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXLMBTC"
    precision: int = 5
    min_margin: float = 25.0
    initial_margin: float = 50.0
    min_order_size: float = 14.0
    max_order_size: float = 1000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXLMBTC"

    def __str__(self):
        return "tXLMBTC"

    def __call__(self):
        return "tXLMBTC"


XLMBTC = XLMBTC()
"""
    name: tXLMBTC
    precision: 5
    min_margin: 25.0
    initial_margin: 50.0
    min_order_size: 14.0
    max_order_size: 1000000.0
    has_margin: True
    exchange: bitfinex
"""


class XLMF0_USTF0(NamedTuple):
    """
        name: tXLMF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 14.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXLMF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 14.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXLMF0:USTF0"

    def __str__(self):
        return "tXLMF0:USTF0"

    def __call__(self):
        return "tXLMF0:USTF0"


XLMF0_USTF0 = XLMF0_USTF0()
"""
    name: tXLMF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 14.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class XLMUSD(NamedTuple):
    """
        name: tXLMUSD
        precision: 5
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 14.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXLMUSD"
    precision: int = 5
    min_margin: float = 25.0
    initial_margin: float = 50.0
    min_order_size: float = 14.0
    max_order_size: float = 1000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXLMUSD"

    def __str__(self):
        return "tXLMUSD"

    def __call__(self):
        return "tXLMUSD"


XLMUSD = XLMUSD()
"""
    name: tXLMUSD
    precision: 5
    min_margin: 25.0
    initial_margin: 50.0
    min_order_size: 14.0
    max_order_size: 1000000.0
    has_margin: True
    exchange: bitfinex
"""


class XLMUST(NamedTuple):
    """
        name: tXLMUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXLMUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 14.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXLMUST"

    def __str__(self):
        return "tXLMUST"

    def __call__(self):
        return "tXLMUST"


XLMUST = XLMUST()
"""
    name: tXLMUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 14.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class XMRBTC(NamedTuple):
    """
        name: tXMRBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXMRBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXMRBTC"

    def __str__(self):
        return "tXMRBTC"

    def __call__(self):
        return "tXMRBTC"


XMRBTC = XMRBTC()
"""
    name: tXMRBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class XMRF0_USTF0(NamedTuple):
    """
        name: tXMRF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.02
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXMRF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.02
    max_order_size: float = 10000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXMRF0:USTF0"

    def __str__(self):
        return "tXMRF0:USTF0"

    def __call__(self):
        return "tXMRF0:USTF0"


XMRF0_USTF0 = XMRF0_USTF0()
"""
    name: tXMRF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.02
    max_order_size: 10000.0
    has_margin: True
    exchange: bitfinex
"""


class XMRUSD(NamedTuple):
    """
        name: tXMRUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXMRUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXMRUSD"

    def __str__(self):
        return "tXMRUSD"

    def __call__(self):
        return "tXMRUSD"


XMRUSD = XMRUSD()
"""
    name: tXMRUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class XMRUST(NamedTuple):
    """
        name: tXMRUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXMRUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 5000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXMRUST"

    def __str__(self):
        return "tXMRUST"

    def __call__(self):
        return "tXMRUST"


XMRUST = XMRUST()
"""
    name: tXMRUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 5000.0
    has_margin: True
    exchange: bitfinex
"""


class XPDF0_USTF0(NamedTuple):
    """
        name: tXPDF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXPDF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 1000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXPDF0:USTF0"

    def __str__(self):
        return "tXPDF0:USTF0"

    def __call__(self):
        return "tXPDF0:USTF0"


XPDF0_USTF0 = XPDF0_USTF0()
"""
    name: tXPDF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 1000.0
    has_margin: True
    exchange: bitfinex
"""


class XPTF0_USTF0(NamedTuple):
    """
        name: tXPTF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXPTF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 1000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXPTF0:USTF0"

    def __str__(self):
        return "tXPTF0:USTF0"

    def __call__(self):
        return "tXPTF0:USTF0"


XPTF0_USTF0 = XPTF0_USTF0()
"""
    name: tXPTF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.001
    max_order_size: 1000.0
    has_margin: True
    exchange: bitfinex
"""


class XRDBTC(NamedTuple):
    """
        name: tXRDBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 24.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXRDBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 24.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXRDBTC"

    def __str__(self):
        return "tXRDBTC"

    def __call__(self):
        return "tXRDBTC"


XRDBTC = XRDBTC()
"""
    name: tXRDBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 24.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class XRDUSD(NamedTuple):
    """
        name: tXRDUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 24.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXRDUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 24.0
    max_order_size: float = 1000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXRDUSD"

    def __str__(self):
        return "tXRDUSD"

    def __call__(self):
        return "tXRDUSD"


XRDUSD = XRDUSD()
"""
    name: tXRDUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 24.0
    max_order_size: 1000000.0
    has_margin: False
    exchange: bitfinex
"""


class XRPBTC(NamedTuple):
    """
        name: tXRPBTC
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 6.0
        max_order_size: 2000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPBTC"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 6.0
    max_order_size: float = 2000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXRPBTC"

    def __str__(self):
        return "tXRPBTC"

    def __call__(self):
        return "tXRPBTC"


XRPBTC = XRPBTC()
"""
    name: tXRPBTC
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 6.0
    max_order_size: 2000000.0
    has_margin: True
    exchange: bitfinex
"""


class XRPF0_BTCF0(NamedTuple):
    """
        name: tXRPF0:BTCF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPF0:BTCF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 6.0
    max_order_size: float = 250000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXRPF0:BTCF0"

    def __str__(self):
        return "tXRPF0:BTCF0"

    def __call__(self):
        return "tXRPF0:BTCF0"


XRPF0_BTCF0 = XRPF0_BTCF0()
"""
    name: tXRPF0:BTCF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 6.0
    max_order_size: 250000.0
    has_margin: True
    exchange: bitfinex
"""


class XRPF0_USTF0(NamedTuple):
    """
        name: tXRPF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 6.0
    max_order_size: float = 500000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXRPF0:USTF0"

    def __str__(self):
        return "tXRPF0:USTF0"

    def __call__(self):
        return "tXRPF0:USTF0"


XRPF0_USTF0 = XRPF0_USTF0()
"""
    name: tXRPF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 6.0
    max_order_size: 500000.0
    has_margin: True
    exchange: bitfinex
"""


class XRPUSD(NamedTuple):
    """
        name: tXRPUSD
        precision: 5
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 6.0
        max_order_size: 2000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPUSD"
    precision: int = 5
    min_margin: float = 10.0
    initial_margin: float = 20.0
    min_order_size: float = 6.0
    max_order_size: float = 2000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXRPUSD"

    def __str__(self):
        return "tXRPUSD"

    def __call__(self):
        return "tXRPUSD"


XRPUSD = XRPUSD()
"""
    name: tXRPUSD
    precision: 5
    min_margin: 10.0
    initial_margin: 20.0
    min_order_size: 6.0
    max_order_size: 2000000.0
    has_margin: True
    exchange: bitfinex
"""


class XRPUST(NamedTuple):
    """
        name: tXRPUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 2000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 2000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXRPUST"

    def __str__(self):
        return "tXRPUST"

    def __call__(self):
        return "tXRPUST"


XRPUST = XRPUST()
"""
    name: tXRPUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 2000000.0
    has_margin: True
    exchange: bitfinex
"""


class XTZBTC(NamedTuple):
    """
        name: tXTZBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXTZBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXTZBTC"

    def __str__(self):
        return "tXTZBTC"

    def __call__(self):
        return "tXTZBTC"


XTZBTC = XTZBTC()
"""
    name: tXTZBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class XTZF0_USTF0(NamedTuple):
    """
        name: tXTZF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXTZF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXTZF0:USTF0"

    def __str__(self):
        return "tXTZF0:USTF0"

    def __call__(self):
        return "tXTZF0:USTF0"


XTZF0_USTF0 = XTZF0_USTF0()
"""
    name: tXTZF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class XTZUSD(NamedTuple):
    """
        name: tXTZUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXTZUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXTZUSD"

    def __str__(self):
        return "tXTZUSD"

    def __call__(self):
        return "tXTZUSD"


XTZUSD = XTZUSD()
"""
    name: tXTZUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class XTZUST(NamedTuple):
    """
        name: tXTZUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXTZUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 100000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXTZUST"

    def __str__(self):
        return "tXTZUST"

    def __call__(self):
        return "tXTZUST"


XTZUST = XTZUST()
"""
    name: tXTZUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 100000.0
    has_margin: True
    exchange: bitfinex
"""


class XVGUSD(NamedTuple):
    """
        name: tXVGUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 432.0
        max_order_size: 1500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXVGUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 432.0
    max_order_size: float = 1500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tXVGUSD"

    def __str__(self):
        return "tXVGUSD"

    def __call__(self):
        return "tXVGUSD"


XVGUSD = XVGUSD()
"""
    name: tXVGUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 432.0
    max_order_size: 1500000.0
    has_margin: False
    exchange: bitfinex
"""


class YFIUSD(NamedTuple):
    """
        name: tYFIUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.0002
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tYFIUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.0002
    max_order_size: float = 100.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tYFIUSD"

    def __str__(self):
        return "tYFIUSD"

    def __call__(self):
        return "tYFIUSD"


YFIUSD = YFIUSD()
"""
    name: tYFIUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.0002
    max_order_size: 100.0
    has_margin: True
    exchange: bitfinex
"""


class YFIUST(NamedTuple):
    """
        name: tYFIUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.0002
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tYFIUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.0002
    max_order_size: float = 100.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tYFIUST"

    def __str__(self):
        return "tYFIUST"

    def __call__(self):
        return "tYFIUST"


YFIUST = YFIUST()
"""
    name: tYFIUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.0002
    max_order_size: 100.0
    has_margin: True
    exchange: bitfinex
"""


class ZECBTC(NamedTuple):
    """
        name: tZECBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 20000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tZECBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 20000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tZECBTC"

    def __str__(self):
        return "tZECBTC"

    def __call__(self):
        return "tZECBTC"


ZECBTC = ZECBTC()
"""
    name: tZECBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 20000.0
    has_margin: True
    exchange: bitfinex
"""


class ZECF0_USTF0(NamedTuple):
    """
        name: tZECF0:USTF0
        precision: 5
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.02
        max_order_size: 20000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tZECF0:USTF0"
    precision: int = 5
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.02
    max_order_size: float = 20000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tZECF0:USTF0"

    def __str__(self):
        return "tZECF0:USTF0"

    def __call__(self):
        return "tZECF0:USTF0"


ZECF0_USTF0 = ZECF0_USTF0()
"""
    name: tZECF0:USTF0
    precision: 5
    min_margin: 0.5
    initial_margin: 1.0
    min_order_size: 0.02
    max_order_size: 20000.0
    has_margin: True
    exchange: bitfinex
"""


class ZECUSD(NamedTuple):
    """
        name: tZECUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 20000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tZECUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.02
    max_order_size: float = 20000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tZECUSD"

    def __str__(self):
        return "tZECUSD"

    def __call__(self):
        return "tZECUSD"


ZECUSD = ZECUSD()
"""
    name: tZECUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 0.02
    max_order_size: 20000.0
    has_margin: True
    exchange: bitfinex
"""


class ZILBTC(NamedTuple):
    """
        name: tZILBTC
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 40.0
        max_order_size: 1500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tZILBTC"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 40.0
    max_order_size: float = 1500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tZILBTC"

    def __str__(self):
        return "tZILBTC"

    def __call__(self):
        return "tZILBTC"


ZILBTC = ZILBTC()
"""
    name: tZILBTC
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 40.0
    max_order_size: 1500000.0
    has_margin: False
    exchange: bitfinex
"""


class ZILUSD(NamedTuple):
    """
        name: tZILUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 40.0
        max_order_size: 1500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tZILUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 40.0
    max_order_size: float = 1500000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tZILUSD"

    def __str__(self):
        return "tZILUSD"

    def __call__(self):
        return "tZILUSD"


ZILUSD = ZILUSD()
"""
    name: tZILUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 40.0
    max_order_size: 1500000.0
    has_margin: False
    exchange: bitfinex
"""


class ZMTUSD(NamedTuple):
    """
        name: tZMTUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tZMTUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tZMTUSD"

    def __str__(self):
        return "tZMTUSD"

    def __call__(self):
        return "tZMTUSD"


ZMTUSD = ZMTUSD()
"""
    name: tZMTUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class ZMTUST(NamedTuple):
    """
        name: tZMTUST
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tZMTUST"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 2.0
    max_order_size: float = 50000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tZMTUST"

    def __str__(self):
        return "tZMTUST"

    def __call__(self):
        return "tZMTUST"


ZMTUST = ZMTUST()
"""
    name: tZMTUST
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 2.0
    max_order_size: 50000.0
    has_margin: False
    exchange: bitfinex
"""


class ZRXUSD(NamedTuple):
    """
        name: tZRXUSD
        precision: 5
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 200000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tZRXUSD"
    precision: int = 5
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 6.0
    max_order_size: float = 200000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tZRXUSD"

    def __str__(self):
        return "tZRXUSD"

    def __call__(self):
        return "tZRXUSD"


ZRXUSD = ZRXUSD()
"""
    name: tZRXUSD
    precision: 5
    min_margin: 15.0
    initial_margin: 30.0
    min_order_size: 6.0
    max_order_size: 200000.0
    has_margin: True
    exchange: bitfinex
"""
