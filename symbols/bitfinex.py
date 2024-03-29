from ._model import Symbol


class ONEINCH_USD(Symbol):
    """
        name: t1INCH:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "t1INCH:USD"
    significant_digits: int = 5
    tick_size: int = None
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


ONEINCH_USD = ONEINCH_USD(*ONEINCH_USD._fields)


class ONEINCH_UST(Symbol):
    """
        name: t1INCH:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "t1INCH:UST"
    significant_digits: int = 5
    tick_size: int = None
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


ONEINCH_UST = ONEINCH_UST(*ONEINCH_UST._fields)


class AAVE_USD(Symbol):
    """
        name: tAAVE:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAAVE:USD"
    significant_digits: int = 5
    tick_size: int = None
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


AAVE_USD = AAVE_USD(*AAVE_USD._fields)


class AAVE_UST(Symbol):
    """
        name: tAAVE:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAAVE:UST"
    significant_digits: int = 5
    tick_size: int = None
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


AAVE_UST = AAVE_UST(*AAVE_UST._fields)


class AAVEF0_USTF0(Symbol):
    """
        name: tAAVEF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAAVEF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


AAVEF0_USTF0 = AAVEF0_USTF0(*AAVEF0_USTF0._fields)


class ADABTC(Symbol):
    """
        name: tADABTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tADABTC"
    significant_digits: int = 5
    tick_size: int = None
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


ADABTC = ADABTC(*ADABTC._fields)


class ADAF0_USTF0(Symbol):
    """
        name: tADAF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tADAF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


ADAF0_USTF0 = ADAF0_USTF0(*ADAF0_USTF0._fields)


class ADAUSD(Symbol):
    """
        name: tADAUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tADAUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ADAUSD = ADAUSD(*ADAUSD._fields)


class ADAUST(Symbol):
    """
        name: tADAUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tADAUST"
    significant_digits: int = 5
    tick_size: int = None
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


ADAUST = ADAUST(*ADAUST._fields)


class AIXUSD(Symbol):
    """
        name: tAIXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 570.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAIXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


AIXUSD = AIXUSD(*AIXUSD._fields)


class AIXUST(Symbol):
    """
        name: tAIXUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 570.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAIXUST"
    significant_digits: int = 5
    tick_size: int = None
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


AIXUST = AIXUST(*AIXUST._fields)


class ALGBTC(Symbol):
    """
        name: tALGBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 150000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tALGBTC"
    significant_digits: int = 5
    tick_size: int = None
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


ALGBTC = ALGBTC(*ALGBTC._fields)


class ALGF0_USTF0(Symbol):
    """
        name: tALGF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tALGF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


ALGF0_USTF0 = ALGF0_USTF0(*ALGF0_USTF0._fields)


class ALGUSD(Symbol):
    """
        name: tALGUSD
        significant_digits: 5
        tick_size: None
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 6.0
        max_order_size: 150000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tALGUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ALGUSD = ALGUSD(*ALGUSD._fields)


class ALGUST(Symbol):
    """
        name: tALGUST
        significant_digits: 5
        tick_size: None
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 6.0
        max_order_size: 150000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tALGUST"
    significant_digits: int = 5
    tick_size: int = None
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


ALGUST = ALGUST(*ALGUST._fields)


class AMPBTC(Symbol):
    """
        name: tAMPBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAMPBTC"
    significant_digits: int = 5
    tick_size: int = None
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


AMPBTC = AMPBTC(*AMPBTC._fields)


class AMPF0_USTF0(Symbol):
    """
        name: tAMPF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 2.5
        initial_margin: 5.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAMPF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


AMPF0_USTF0 = AMPF0_USTF0(*AMPF0_USTF0._fields)


class AMPUSD(Symbol):
    """
        name: tAMPUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAMPUSD"
    significant_digits: int = 5
    tick_size: int = None
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


AMPUSD = AMPUSD(*AMPUSD._fields)


class AMPUST(Symbol):
    """
        name: tAMPUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAMPUST"
    significant_digits: int = 5
    tick_size: int = None
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


AMPUST = AMPUST(*AMPUST._fields)


class ANTBTC(Symbol):
    """
        name: tANTBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tANTBTC"
    significant_digits: int = 5
    tick_size: int = None
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


ANTBTC = ANTBTC(*ANTBTC._fields)


class ANTUSD(Symbol):
    """
        name: tANTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tANTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ANTUSD = ANTUSD(*ANTUSD._fields)


class APEF0_USTF0(Symbol):
    """
        name: tAPEF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPEF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


APEF0_USTF0 = APEF0_USTF0(*APEF0_USTF0._fields)


class APENFT_USD(Symbol):
    """
        name: tAPENFT:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 40000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAPENFT:USD"
    significant_digits: int = 5
    tick_size: int = None
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


APENFT_USD = APENFT_USD(*APENFT_USD._fields)


class APENFT_UST(Symbol):
    """
        name: tAPENFT:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 40000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tAPENFT:UST"
    significant_digits: int = 5
    tick_size: int = None
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


APENFT_UST = APENFT_UST(*APENFT_UST._fields)


class APEUSD(Symbol):
    """
        name: tAPEUSD
        significant_digits: 5
        tick_size: None
        min_margin: 30.0
        initial_margin: 60.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPEUSD"
    significant_digits: int = 5
    tick_size: int = None
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


APEUSD = APEUSD(*APEUSD._fields)


class APEUST(Symbol):
    """
        name: tAPEUST
        significant_digits: 5
        tick_size: None
        min_margin: 30.0
        initial_margin: 60.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPEUST"
    significant_digits: int = 5
    tick_size: int = None
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


APEUST = APEUST(*APEUST._fields)


class APTF0_USTF0(Symbol):
    """
        name: tAPTF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 30000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPTF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


APTF0_USTF0 = APTF0_USTF0(*APTF0_USTF0._fields)


class APTUSD(Symbol):
    """
        name: tAPTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 30000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


APTUSD = APTUSD(*APTUSD._fields)


class APTUST(Symbol):
    """
        name: tAPTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 30000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAPTUST"
    significant_digits: int = 5
    tick_size: int = None
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


APTUST = APTUST(*APTUST._fields)


class ARBF0_USTF0(Symbol):
    """
        name: tARBF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tARBF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


ARBF0_USTF0 = ARBF0_USTF0(*ARBF0_USTF0._fields)


class ARBUSD(Symbol):
    """
        name: tARBUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tARBUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ARBUSD = ARBUSD(*ARBUSD._fields)


class ARBUST(Symbol):
    """
        name: tARBUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tARBUST"
    significant_digits: int = 5
    tick_size: int = None
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


ARBUST = ARBUST(*ARBUST._fields)


class ATLAS_USD(Symbol):
    """
        name: tATLAS:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 232.0
        max_order_size: 25000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tATLAS:USD"
    significant_digits: int = 5
    tick_size: int = None
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


ATLAS_USD = ATLAS_USD(*ATLAS_USD._fields)


class ATLAS_UST(Symbol):
    """
        name: tATLAS:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 232.0
        max_order_size: 25000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tATLAS:UST"
    significant_digits: int = 5
    tick_size: int = None
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


ATLAS_UST = ATLAS_UST(*ATLAS_UST._fields)


class ATOBTC(Symbol):
    """
        name: tATOBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tATOBTC"
    significant_digits: int = 5
    tick_size: int = None
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


ATOBTC = ATOBTC(*ATOBTC._fields)


class ATOETH(Symbol):
    """
        name: tATOETH
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tATOETH"
    significant_digits: int = 5
    tick_size: int = None
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


ATOETH = ATOETH(*ATOETH._fields)


class ATOF0_USTF0(Symbol):
    """
        name: tATOF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tATOF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


ATOF0_USTF0 = ATOF0_USTF0(*ATOF0_USTF0._fields)


class ATOUSD(Symbol):
    """
        name: tATOUSD
        significant_digits: 5
        tick_size: None
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tATOUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ATOUSD = ATOUSD(*ATOUSD._fields)


class ATOUST(Symbol):
    """
        name: tATOUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tATOUST"
    significant_digits: int = 5
    tick_size: int = None
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


ATOUST = ATOUST(*ATOUST._fields)


class AUSTRALIA200IXF0_USTF0(Symbol):
    """
        name: tAUSTRALIA200IXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAUSTRALIA200IXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


AUSTRALIA200IXF0_USTF0 = AUSTRALIA200IXF0_USTF0(*AUSTRALIA200IXF0_USTF0._fields)


class AVAX_BTC(Symbol):
    """
        name: tAVAX:BTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.08
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAX:BTC"
    significant_digits: int = 5
    tick_size: int = None
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


AVAX_BTC = AVAX_BTC(*AVAX_BTC._fields)


class AVAX_USD(Symbol):
    """
        name: tAVAX:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.08
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAX:USD"
    significant_digits: int = 5
    tick_size: int = None
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


AVAX_USD = AVAX_USD(*AVAX_USD._fields)


class AVAX_UST(Symbol):
    """
        name: tAVAX:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.08
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAX:UST"
    significant_digits: int = 5
    tick_size: int = None
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


AVAX_UST = AVAX_UST(*AVAX_UST._fields)


class AVAXF0_BTCF0(Symbol):
    """
        name: tAVAXF0:BTCF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.08
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAXF0:BTCF0"
    significant_digits: int = 5
    tick_size: int = None
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


AVAXF0_BTCF0 = AVAXF0_BTCF0(*AVAXF0_BTCF0._fields)


class AVAXF0_USTF0(Symbol):
    """
        name: tAVAXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.08
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAVAXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


AVAXF0_USTF0 = AVAXF0_USTF0(*AVAXF0_USTF0._fields)


class AXSF0_USTF0(Symbol):
    """
        name: tAXSF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAXSF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


AXSF0_USTF0 = AXSF0_USTF0(*AXSF0_USTF0._fields)


class AXSUSD(Symbol):
    """
        name: tAXSUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAXSUSD"
    significant_digits: int = 5
    tick_size: int = None
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


AXSUSD = AXSUSD(*AXSUSD._fields)


class AXSUST(Symbol):
    """
        name: tAXSUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tAXSUST"
    significant_digits: int = 5
    tick_size: int = None
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


AXSUST = AXSUST(*AXSUST._fields)


class B2MUSD(Symbol):
    """
        name: tB2MUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 144.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tB2MUSD"
    significant_digits: int = 5
    tick_size: int = None
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


B2MUSD = B2MUSD(*B2MUSD._fields)


class B2MUST(Symbol):
    """
        name: tB2MUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 144.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tB2MUST"
    significant_digits: int = 5
    tick_size: int = None
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


B2MUST = B2MUST(*B2MUST._fields)


class BALUSD(Symbol):
    """
        name: tBALUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBALUSD"
    significant_digits: int = 5
    tick_size: int = None
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


BALUSD = BALUSD(*BALUSD._fields)


class BALUST(Symbol):
    """
        name: tBALUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBALUST"
    significant_digits: int = 5
    tick_size: int = None
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


BALUST = BALUST(*BALUST._fields)


class BAND_USD(Symbol):
    """
        name: tBAND:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBAND:USD"
    significant_digits: int = 5
    tick_size: int = None
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


BAND_USD = BAND_USD(*BAND_USD._fields)


class BAND_UST(Symbol):
    """
        name: tBAND:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBAND:UST"
    significant_digits: int = 5
    tick_size: int = None
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


BAND_UST = BAND_UST(*BAND_UST._fields)


class BATUSD(Symbol):
    """
        name: tBATUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBATUSD"
    significant_digits: int = 5
    tick_size: int = None
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


BATUSD = BATUSD(*BATUSD._fields)


class BATUST(Symbol):
    """
        name: tBATUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBATUST"
    significant_digits: int = 5
    tick_size: int = None
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


BATUST = BATUST(*BATUST._fields)


class BCHABC_USD(Symbol):
    """
        name: tBCHABC:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 40962.0
        max_order_size: 1000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBCHABC:USD"
    significant_digits: int = 5
    tick_size: int = None
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


BCHABC_USD = BCHABC_USD(*BCHABC_USD._fields)


class BCHN_USD(Symbol):
    """
        name: tBCHN:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBCHN:USD"
    significant_digits: int = 5
    tick_size: int = None
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


BCHN_USD = BCHN_USD(*BCHN_USD._fields)


class BEST_USD(Symbol):
    """
        name: tBEST:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBEST:USD"
    significant_digits: int = 5
    tick_size: int = None
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


BEST_USD = BEST_USD(*BEST_USD._fields)


class BGBUSD(Symbol):
    """
        name: tBGBUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBGBUSD"
    significant_digits: int = 5
    tick_size: int = None
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBGBUSD"

    def __str__(self):
        return "tBGBUSD"

    def __call__(self):
        return "tBGBUSD"


BGBUSD = BGBUSD(*BGBUSD._fields)


class BGBUST(Symbol):
    """
        name: tBGBUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBGBUST"
    significant_digits: int = 5
    tick_size: int = None
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 250000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tBGBUST"

    def __str__(self):
        return "tBGBUST"

    def __call__(self):
        return "tBGBUST"


BGBUST = BGBUST(*BGBUST._fields)


class BLUR_USD(Symbol):
    """
        name: tBLUR:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBLUR:USD"
    significant_digits: int = 5
    tick_size: int = None
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


BLUR_USD = BLUR_USD(*BLUR_USD._fields)


class BLUR_UST(Symbol):
    """
        name: tBLUR:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 75000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBLUR:UST"
    significant_digits: int = 5
    tick_size: int = None
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


BLUR_UST = BLUR_UST(*BLUR_UST._fields)


class BMNBTC(Symbol):
    """
        name: tBMNBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00002
        max_order_size: 1.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBMNBTC"
    significant_digits: int = 5
    tick_size: int = None
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


BMNBTC = BMNBTC(*BMNBTC._fields)


class BMNUSD(Symbol):
    """
        name: tBMNUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00002
        max_order_size: 1.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBMNUSD"
    significant_digits: int = 5
    tick_size: int = None
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


BMNUSD = BMNUSD(*BMNUSD._fields)


class BNTUSD(Symbol):
    """
        name: tBNTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBNTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


BNTUSD = BNTUSD(*BNTUSD._fields)


class BOBA_USD(Symbol):
    """
        name: tBOBA:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOBA:USD"
    significant_digits: int = 5
    tick_size: int = None
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


BOBA_USD = BOBA_USD(*BOBA_USD._fields)


class BOBA_UST(Symbol):
    """
        name: tBOBA:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOBA:UST"
    significant_digits: int = 5
    tick_size: int = None
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


BOBA_UST = BOBA_UST(*BOBA_UST._fields)


class BOOUSD(Symbol):
    """
        name: tBOOUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 45000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOOUSD"
    significant_digits: int = 5
    tick_size: int = None
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


BOOUSD = BOOUSD(*BOOUSD._fields)


class BOOUST(Symbol):
    """
        name: tBOOUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 45000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOOUST"
    significant_digits: int = 5
    tick_size: int = None
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


BOOUST = BOOUST(*BOOUST._fields)


class BOSON_USD(Symbol):
    """
        name: tBOSON:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOSON:USD"
    significant_digits: int = 5
    tick_size: int = None
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


BOSON_USD = BOSON_USD(*BOSON_USD._fields)


class BOSON_UST(Symbol):
    """
        name: tBOSON:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBOSON:UST"
    significant_digits: int = 5
    tick_size: int = None
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


BOSON_UST = BOSON_UST(*BOSON_UST._fields)


class BRISE_USD(Symbol):
    """
        name: tBRISE:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBRISE:USD"
    significant_digits: int = 5
    tick_size: int = None
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


BRISE_USD = BRISE_USD(*BRISE_USD._fields)


class BRISE_UST(Symbol):
    """
        name: tBRISE:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBRISE:UST"
    significant_digits: int = 5
    tick_size: int = None
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


BRISE_UST = BRISE_UST(*BRISE_UST._fields)


class BTC_CNHT(Symbol):
    """
        name: tBTC:CNHT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTC:CNHT"
    significant_digits: int = 5
    tick_size: int = None
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


BTC_CNHT = BTC_CNHT(*BTC_CNHT._fields)


class BTC_MXNT(Symbol):
    """
        name: tBTC:MXNT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTC:MXNT"
    significant_digits: int = 5
    tick_size: int = None
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


BTC_MXNT = BTC_MXNT(*BTC_MXNT._fields)


class BTC_XAUT(Symbol):
    """
        name: tBTC:XAUT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.0002
        max_order_size: 250.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTC:XAUT"
    significant_digits: int = 5
    tick_size: int = None
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


BTC_XAUT = BTC_XAUT(*BTC_XAUT._fields)


class BTCDOMF0_USTF0(Symbol):
    """
        name: tBTCDOMF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.01
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCDOMF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


BTCDOMF0_USTF0 = BTCDOMF0_USTF0(*BTCDOMF0_USTF0._fields)


class BTCEUR(Symbol):
    """
        name: tBTCEUR
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCEUR"
    significant_digits: int = 5
    tick_size: int = None
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


BTCEUR = BTCEUR(*BTCEUR._fields)


class BTCEUT(Symbol):
    """
        name: tBTCEUT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCEUT"
    significant_digits: int = 5
    tick_size: int = None
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


BTCEUT = BTCEUT(*BTCEUT._fields)


class BTCF0_EUTF0(Symbol):
    """
        name: tBTCF0:EUTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.0002
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCF0:EUTF0"
    significant_digits: int = 5
    tick_size: int = None
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


BTCF0_EUTF0 = BTCF0_EUTF0(*BTCF0_EUTF0._fields)


class BTCF0_USTF0(Symbol):
    """
        name: tBTCF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.00006
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


BTCF0_USTF0 = BTCF0_USTF0(*BTCF0_USTF0._fields)


class BTCGBP(Symbol):
    """
        name: tBTCGBP
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCGBP"
    significant_digits: int = 5
    tick_size: int = None
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


BTCGBP = BTCGBP(*BTCGBP._fields)


class BTCJPY(Symbol):
    """
        name: tBTCJPY
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCJPY"
    significant_digits: int = 5
    tick_size: int = None
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


BTCJPY = BTCJPY(*BTCJPY._fields)


class BTCMIM(Symbol):
    """
        name: tBTCMIM
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.0002
        max_order_size: 2500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTCMIM"
    significant_digits: int = 5
    tick_size: int = None
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


BTCMIM = BTCMIM(*BTCMIM._fields)


class BTCTRY(Symbol):
    """
        name: tBTCTRY
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTCTRY"
    significant_digits: int = 5
    tick_size: int = None
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


BTCTRY = BTCTRY(*BTCTRY._fields)


class BTCUSD(Symbol):
    """
        name: tBTCUSD
        significant_digits: 5
        tick_size: None
        min_margin: 5.0
        initial_margin: 10.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCUSD"
    significant_digits: int = 5
    tick_size: int = None
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


BTCUSD = BTCUSD(*BTCUSD._fields)


class BTCUST(Symbol):
    """
        name: tBTCUST
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.00006
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tBTCUST"
    significant_digits: int = 5
    tick_size: int = None
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


BTCUST = BTCUST(*BTCUST._fields)


class BTGBTC(Symbol):
    """
        name: tBTGBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTGBTC"
    significant_digits: int = 5
    tick_size: int = None
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


BTGBTC = BTGBTC(*BTGBTC._fields)


class BTGUSD(Symbol):
    """
        name: tBTGUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTGUSD"
    significant_digits: int = 5
    tick_size: int = None
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


BTGUSD = BTGUSD(*BTGUSD._fields)


class BTSE_USD(Symbol):
    """
        name: tBTSE:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTSE:USD"
    significant_digits: int = 5
    tick_size: int = None
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


BTSE_USD = BTSE_USD(*BTSE_USD._fields)


class BTTUSD(Symbol):
    """
        name: tBTTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1970444.0
        max_order_size: 25000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tBTTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


BTTUSD = BTTUSD(*BTTUSD._fields)


class CCDBTC(Symbol):
    """
        name: tCCDBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 100.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCCDBTC"
    significant_digits: int = 5
    tick_size: int = None
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


CCDBTC = CCDBTC(*CCDBTC._fields)


class CCDUSD(Symbol):
    """
        name: tCCDUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 100.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCCDUSD"
    significant_digits: int = 5
    tick_size: int = None
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


CCDUSD = CCDUSD(*CCDUSD._fields)


class CCDUST(Symbol):
    """
        name: tCCDUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 100.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCCDUST"
    significant_digits: int = 5
    tick_size: int = None
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


CCDUST = CCDUST(*CCDUST._fields)


class CHEX_USD(Symbol):
    """
        name: tCHEX:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 88.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHEX:USD"
    significant_digits: int = 5
    tick_size: int = None
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


CHEX_USD = CHEX_USD(*CHEX_USD._fields)


class CHSB_BTC(Symbol):
    """
        name: tCHSB:BTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHSB:BTC"
    significant_digits: int = 5
    tick_size: int = None
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


CHSB_BTC = CHSB_BTC(*CHSB_BTC._fields)


class CHSB_USD(Symbol):
    """
        name: tCHSB:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHSB:USD"
    significant_digits: int = 5
    tick_size: int = None
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


CHSB_USD = CHSB_USD(*CHSB_USD._fields)


class CHSB_UST(Symbol):
    """
        name: tCHSB:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHSB:UST"
    significant_digits: int = 5
    tick_size: int = None
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


CHSB_UST = CHSB_UST(*CHSB_UST._fields)


class CHZUSD(Symbol):
    """
        name: tCHZUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 16.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHZUSD"
    significant_digits: int = 5
    tick_size: int = None
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


CHZUSD = CHZUSD(*CHZUSD._fields)


class CHZUST(Symbol):
    """
        name: tCHZUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 16.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCHZUST"
    significant_digits: int = 5
    tick_size: int = None
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


CHZUST = CHZUST(*CHZUST._fields)


class CLOUSD(Symbol):
    """
        name: tCLOUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 624.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCLOUSD"
    significant_digits: int = 5
    tick_size: int = None
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


CLOUSD = CLOUSD(*CLOUSD._fields)


class CNH_CNHT(Symbol):
    """
        name: tCNH:CNHT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCNH:CNHT"
    significant_digits: int = 5
    tick_size: int = None
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


CNH_CNHT = CNH_CNHT(*CNH_CNHT._fields)


class COMP_USD(Symbol):
    """
        name: tCOMP:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tCOMP:USD"
    significant_digits: int = 5
    tick_size: int = None
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


COMP_USD = COMP_USD(*COMP_USD._fields)


class COMP_UST(Symbol):
    """
        name: tCOMP:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tCOMP:UST"
    significant_digits: int = 5
    tick_size: int = None
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


COMP_UST = COMP_UST(*COMP_UST._fields)


class COMPF0_USTF0(Symbol):
    """
        name: tCOMPF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tCOMPF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


COMPF0_USTF0 = COMPF0_USTF0(*COMPF0_USTF0._fields)


class CONV_USD(Symbol):
    """
        name: tCONV:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCONV:USD"
    significant_digits: int = 5
    tick_size: int = None
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


CONV_USD = CONV_USD(*CONV_USD._fields)


class CONV_UST(Symbol):
    """
        name: tCONV:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCONV:UST"
    significant_digits: int = 5
    tick_size: int = None
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


CONV_UST = CONV_UST(*CONV_UST._fields)


class CRVF0_USTF0(Symbol):
    """
        name: tCRVF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tCRVF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


CRVF0_USTF0 = CRVF0_USTF0(*CRVF0_USTF0._fields)


class CRVUSD(Symbol):
    """
        name: tCRVUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCRVUSD"
    significant_digits: int = 5
    tick_size: int = None
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


CRVUSD = CRVUSD(*CRVUSD._fields)


class CRVUST(Symbol):
    """
        name: tCRVUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tCRVUST"
    significant_digits: int = 5
    tick_size: int = None
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


CRVUST = CRVUST(*CRVUST._fields)


class DAIBTC(Symbol):
    """
        name: tDAIBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDAIBTC"
    significant_digits: int = 5
    tick_size: int = None
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


DAIBTC = DAIBTC(*DAIBTC._fields)


class DAIUSD(Symbol):
    """
        name: tDAIUSD
        significant_digits: 5
        tick_size: None
        min_margin: 33.0
        initial_margin: 66.0
        min_order_size: 2.0
        max_order_size: 200000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDAIUSD"
    significant_digits: int = 5
    tick_size: int = None
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


DAIUSD = DAIUSD(*DAIUSD._fields)


class DGBUSD(Symbol):
    """
        name: tDGBUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 184.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDGBUSD"
    significant_digits: int = 5
    tick_size: int = None
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


DGBUSD = DGBUSD(*DGBUSD._fields)


class DOGE_BTC(Symbol):
    """
        name: tDOGE:BTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 1500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOGE:BTC"
    significant_digits: int = 5
    tick_size: int = None
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


DOGE_BTC = DOGE_BTC(*DOGE_BTC._fields)


class DOGE_USD(Symbol):
    """
        name: tDOGE:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 1500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOGE:USD"
    significant_digits: int = 5
    tick_size: int = None
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


DOGE_USD = DOGE_USD(*DOGE_USD._fields)


class DOGE_UST(Symbol):
    """
        name: tDOGE:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 1500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOGE:UST"
    significant_digits: int = 5
    tick_size: int = None
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


DOGE_UST = DOGE_UST(*DOGE_UST._fields)


class DOGEF0_USTF0(Symbol):
    """
        name: tDOGEF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 26.0
        max_order_size: 1500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOGEF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


DOGEF0_USTF0 = DOGEF0_USTF0(*DOGEF0_USTF0._fields)


class DORA_USD(Symbol):
    """
        name: tDORA:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDORA:USD"
    significant_digits: int = 5
    tick_size: int = None
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


DORA_USD = DORA_USD(*DORA_USD._fields)


class DORA_UST(Symbol):
    """
        name: tDORA:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDORA:UST"
    significant_digits: int = 5
    tick_size: int = None
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


DORA_UST = DORA_UST(*DORA_UST._fields)


class DOTBTC(Symbol):
    """
        name: tDOTBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTBTC"
    significant_digits: int = 5
    tick_size: int = None
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


DOTBTC = DOTBTC(*DOTBTC._fields)


class DOTF0_BTCF0(Symbol):
    """
        name: tDOTF0:BTCF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTF0:BTCF0"
    significant_digits: int = 5
    tick_size: int = None
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


DOTF0_BTCF0 = DOTF0_BTCF0(*DOTF0_BTCF0._fields)


class DOTF0_USTF0(Symbol):
    """
        name: tDOTF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


DOTF0_USTF0 = DOTF0_USTF0(*DOTF0_USTF0._fields)


class DOTUSD(Symbol):
    """
        name: tDOTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


DOTUSD = DOTUSD(*DOTUSD._fields)


class DOTUST(Symbol):
    """
        name: tDOTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDOTUST"
    significant_digits: int = 5
    tick_size: int = None
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


DOTUST = DOTUST(*DOTUST._fields)


class DSHBTC(Symbol):
    """
        name: tDSHBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDSHBTC"
    significant_digits: int = 5
    tick_size: int = None
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


DSHBTC = DSHBTC(*DSHBTC._fields)


class DSHUSD(Symbol):
    """
        name: tDSHUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tDSHUSD"
    significant_digits: int = 5
    tick_size: int = None
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


DSHUSD = DSHUSD(*DSHUSD._fields)


class DUSK_BTC(Symbol):
    """
        name: tDUSK:BTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDUSK:BTC"
    significant_digits: int = 5
    tick_size: int = None
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


DUSK_BTC = DUSK_BTC(*DUSK_BTC._fields)


class DUSK_USD(Symbol):
    """
        name: tDUSK:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDUSK:USD"
    significant_digits: int = 5
    tick_size: int = None
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


DUSK_USD = DUSK_USD(*DUSK_USD._fields)


class DVFUSD(Symbol):
    """
        name: tDVFUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tDVFUSD"
    significant_digits: int = 5
    tick_size: int = None
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


DVFUSD = DVFUSD(*DVFUSD._fields)


class EDOUSD(Symbol):
    """
        name: tEDOUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEDOUSD"
    significant_digits: int = 5
    tick_size: int = None
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


EDOUSD = EDOUSD(*EDOUSD._fields)


class EGLD_USD(Symbol):
    """
        name: tEGLD:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEGLD:USD"
    significant_digits: int = 5
    tick_size: int = None
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


EGLD_USD = EGLD_USD(*EGLD_USD._fields)


class EGLD_UST(Symbol):
    """
        name: tEGLD:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEGLD:UST"
    significant_digits: int = 5
    tick_size: int = None
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


EGLD_UST = EGLD_UST(*EGLD_UST._fields)


class EGLDF0_USTF0(Symbol):
    """
        name: tEGLDF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEGLDF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


EGLDF0_USTF0 = EGLDF0_USTF0(*EGLDF0_USTF0._fields)


class ENJUSD(Symbol):
    """
        name: tENJUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tENJUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ENJUSD = ENJUSD(*ENJUSD._fields)


class EOSBTC(Symbol):
    """
        name: tEOSBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSBTC"
    significant_digits: int = 5
    tick_size: int = None
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


EOSBTC = EOSBTC(*EOSBTC._fields)


class EOSETH(Symbol):
    """
        name: tEOSETH
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSETH"
    significant_digits: int = 5
    tick_size: int = None
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


EOSETH = EOSETH(*EOSETH._fields)


class EOSEUR(Symbol):
    """
        name: tEOSEUR
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSEUR"
    significant_digits: int = 5
    tick_size: int = None
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


EOSEUR = EOSEUR(*EOSEUR._fields)


class EOSF0_USTF0(Symbol):
    """
        name: tEOSF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


EOSF0_USTF0 = EOSF0_USTF0(*EOSF0_USTF0._fields)


class EOSUSD(Symbol):
    """
        name: tEOSUSD
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSUSD"
    significant_digits: int = 5
    tick_size: int = None
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


EOSUSD = EOSUSD(*EOSUSD._fields)


class EOSUST(Symbol):
    """
        name: tEOSUST
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEOSUST"
    significant_digits: int = 5
    tick_size: int = None
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


EOSUST = EOSUST(*EOSUST._fields)


class ETCBTC(Symbol):
    """
        name: tETCBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETCBTC"
    significant_digits: int = 5
    tick_size: int = None
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


ETCBTC = ETCBTC(*ETCBTC._fields)


class ETCF0_USTF0(Symbol):
    """
        name: tETCF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.1
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETCF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


ETCF0_USTF0 = ETCF0_USTF0(*ETCF0_USTF0._fields)


class ETCUSD(Symbol):
    """
        name: tETCUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETCUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ETCUSD = ETCUSD(*ETCUSD._fields)


class ETCUST(Symbol):
    """
        name: tETCUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.1
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETCUST"
    significant_digits: int = 5
    tick_size: int = None
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


ETCUST = ETCUST(*ETCUST._fields)


class ETH2X_ETH(Symbol):
    """
        name: tETH2X:ETH
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH2X:ETH"
    significant_digits: int = 5
    tick_size: int = None
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


ETH2X_ETH = ETH2X_ETH(*ETH2X_ETH._fields)


class ETH2X_USD(Symbol):
    """
        name: tETH2X:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH2X:USD"
    significant_digits: int = 5
    tick_size: int = None
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


ETH2X_USD = ETH2X_USD(*ETH2X_USD._fields)


class ETH2X_UST(Symbol):
    """
        name: tETH2X:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH2X:UST"
    significant_digits: int = 5
    tick_size: int = None
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


ETH2X_UST = ETH2X_UST(*ETH2X_UST._fields)


class ETH_MXNT(Symbol):
    """
        name: tETH:MXNT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 2000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH:MXNT"
    significant_digits: int = 5
    tick_size: int = None
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


ETH_MXNT = ETH_MXNT(*ETH_MXNT._fields)


class ETH_XAUT(Symbol):
    """
        name: tETH:XAUT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 2500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETH:XAUT"
    significant_digits: int = 5
    tick_size: int = None
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


ETH_XAUT = ETH_XAUT(*ETH_XAUT._fields)


class ETHBTC(Symbol):
    """
        name: tETHBTC
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHBTC"
    significant_digits: int = 5
    tick_size: int = None
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


ETHBTC = ETHBTC(*ETHBTC._fields)


class ETHEUR(Symbol):
    """
        name: tETHEUR
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHEUR"
    significant_digits: int = 5
    tick_size: int = None
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


ETHEUR = ETHEUR(*ETHEUR._fields)


class ETHEUT(Symbol):
    """
        name: tETHEUT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHEUT"
    significant_digits: int = 5
    tick_size: int = None
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


ETHEUT = ETHEUT(*ETHEUT._fields)


class ETHF0_BTCF0(Symbol):
    """
        name: tETHF0:BTCF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHF0:BTCF0"
    significant_digits: int = 5
    tick_size: int = None
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


ETHF0_BTCF0 = ETHF0_BTCF0(*ETHF0_BTCF0._fields)


class ETHF0_EUTF0(Symbol):
    """
        name: tETHF0:EUTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHF0:EUTF0"
    significant_digits: int = 5
    tick_size: int = None
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


ETHF0_EUTF0 = ETHF0_EUTF0(*ETHF0_EUTF0._fields)


class ETHF0_USTF0(Symbol):
    """
        name: tETHF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


ETHF0_USTF0 = ETHF0_USTF0(*ETHF0_USTF0._fields)


class ETHGBP(Symbol):
    """
        name: tETHGBP
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHGBP"
    significant_digits: int = 5
    tick_size: int = None
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


ETHGBP = ETHGBP(*ETHGBP._fields)


class ETHJPY(Symbol):
    """
        name: tETHJPY
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHJPY"
    significant_digits: int = 5
    tick_size: int = None
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


ETHJPY = ETHJPY(*ETHJPY._fields)


class ETHUSD(Symbol):
    """
        name: tETHUSD
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ETHUSD = ETHUSD(*ETHUSD._fields)


class ETHUST(Symbol):
    """
        name: tETHUST
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHUST"
    significant_digits: int = 5
    tick_size: int = None
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


ETHUST = ETHUST(*ETHUST._fields)


class ETHW_USD(Symbol):
    """
        name: tETHW:USD
        significant_digits: 5
        tick_size: None
        min_margin: 30.0
        initial_margin: 60.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHW:USD"
    significant_digits: int = 5
    tick_size: int = None
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


ETHW_USD = ETHW_USD(*ETHW_USD._fields)


class ETHW_UST(Symbol):
    """
        name: tETHW:UST
        significant_digits: 5
        tick_size: None
        min_margin: 30.0
        initial_margin: 60.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tETHW:UST"
    significant_digits: int = 5
    tick_size: int = None
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


ETHW_UST = ETHW_UST(*ETHW_UST._fields)


class ETPUSD(Symbol):
    """
        name: tETPUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 42.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tETPUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ETPUSD = ETPUSD(*ETPUSD._fields)


class EURF0_USTF0(Symbol):
    """
        name: tEURF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEURF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


EURF0_USTF0 = EURF0_USTF0(*EURF0_USTF0._fields)


class EUROPE50IXF0_USTF0(Symbol):
    """
        name: tEUROPE50IXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.0006
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tEUROPE50IXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


EUROPE50IXF0_USTF0 = EUROPE50IXF0_USTF0(*EUROPE50IXF0_USTF0._fields)


class EURUST(Symbol):
    """
        name: tEURUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEURUST"
    significant_digits: int = 5
    tick_size: int = None
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


EURUST = EURUST(*EURUST._fields)


class EUSUSD(Symbol):
    """
        name: tEUSUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUSUSD"
    significant_digits: int = 5
    tick_size: int = None
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


EUSUSD = EUSUSD(*EUSUSD._fields)


class EUT_MXNT(Symbol):
    """
        name: tEUT:MXNT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUT:MXNT"
    significant_digits: int = 5
    tick_size: int = None
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


EUT_MXNT = EUT_MXNT(*EUT_MXNT._fields)


class EUTEUR(Symbol):
    """
        name: tEUTEUR
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUTEUR"
    significant_digits: int = 5
    tick_size: int = None
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


EUTEUR = EUTEUR(*EUTEUR._fields)


class EUTUSD(Symbol):
    """
        name: tEUTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


EUTUSD = EUTUSD(*EUTUSD._fields)


class EUTUST(Symbol):
    """
        name: tEUTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tEUTUST"
    significant_digits: int = 5
    tick_size: int = None
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


EUTUST = EUTUST(*EUTUST._fields)


class FBTUSD(Symbol):
    """
        name: tFBTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFBTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


FBTUSD = FBTUSD(*FBTUSD._fields)


class FBTUST(Symbol):
    """
        name: tFBTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFBTUST"
    significant_digits: int = 5
    tick_size: int = None
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


FBTUST = FBTUST(*FBTUST._fields)


class FCLUSD(Symbol):
    """
        name: tFCLUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 62.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFCLUSD"
    significant_digits: int = 5
    tick_size: int = None
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


FCLUSD = FCLUSD(*FCLUSD._fields)


class FCLUST(Symbol):
    """
        name: tFCLUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 62.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFCLUST"
    significant_digits: int = 5
    tick_size: int = None
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


FCLUST = FCLUST(*FCLUST._fields)


class FETUSD(Symbol):
    """
        name: tFETUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFETUSD"
    significant_digits: int = 5
    tick_size: int = None
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


FETUSD = FETUSD(*FETUSD._fields)


class FETUST(Symbol):
    """
        name: tFETUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFETUST"
    significant_digits: int = 5
    tick_size: int = None
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


FETUST = FETUST(*FETUST._fields)


class FILF0_USTF0(Symbol):
    """
        name: tFILF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFILF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


FILF0_USTF0 = FILF0_USTF0(*FILF0_USTF0._fields)


class FILUSD(Symbol):
    """
        name: tFILUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFILUSD"
    significant_digits: int = 5
    tick_size: int = None
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


FILUSD = FILUSD(*FILUSD._fields)


class FILUST(Symbol):
    """
        name: tFILUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFILUST"
    significant_digits: int = 5
    tick_size: int = None
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


FILUST = FILUST(*FILUST._fields)


class FLOKI_USD(Symbol):
    """
        name: tFLOKI:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 2500000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFLOKI:USD"
    significant_digits: int = 5
    tick_size: int = None
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 2500000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFLOKI:USD"

    def __str__(self):
        return "tFLOKI:USD"

    def __call__(self):
        return "tFLOKI:USD"


FLOKI_USD = FLOKI_USD(*FLOKI_USD._fields)


class FLOKI_UST(Symbol):
    """
        name: tFLOKI:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 2500000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFLOKI:UST"
    significant_digits: int = 5
    tick_size: int = None
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 2500000000.0
    has_margin: bool = False
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tFLOKI:UST"

    def __str__(self):
        return "tFLOKI:UST"

    def __call__(self):
        return "tFLOKI:UST"


FLOKI_UST = FLOKI_UST(*FLOKI_UST._fields)


class FLRUSD(Symbol):
    """
        name: tFLRUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFLRUSD"
    significant_digits: int = 5
    tick_size: int = None
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


FLRUSD = FLRUSD(*FLRUSD._fields)


class FLRUST(Symbol):
    """
        name: tFLRUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFLRUST"
    significant_digits: int = 5
    tick_size: int = None
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


FLRUST = FLRUST(*FLRUST._fields)


class FORTH_USD(Symbol):
    """
        name: tFORTH:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFORTH:USD"
    significant_digits: int = 5
    tick_size: int = None
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


FORTH_USD = FORTH_USD(*FORTH_USD._fields)


class FORTH_UST(Symbol):
    """
        name: tFORTH:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFORTH:UST"
    significant_digits: int = 5
    tick_size: int = None
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


FORTH_UST = FORTH_UST(*FORTH_UST._fields)


class FRANCE40IXF0_USTF0(Symbol):
    """
        name: tFRANCE40IXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFRANCE40IXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


FRANCE40IXF0_USTF0 = FRANCE40IXF0_USTF0(*FRANCE40IXF0_USTF0._fields)


class FTMF0_USTF0(Symbol):
    """
        name: tFTMF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFTMF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


FTMF0_USTF0 = FTMF0_USTF0(*FTMF0_USTF0._fields)


class FTMUSD(Symbol):
    """
        name: tFTMUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFTMUSD"
    significant_digits: int = 5
    tick_size: int = None
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


FTMUSD = FTMUSD(*FTMUSD._fields)


class FTMUST(Symbol):
    """
        name: tFTMUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tFTMUST"
    significant_digits: int = 5
    tick_size: int = None
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


FTMUST = FTMUST(*FTMUST._fields)


class FUNUSD(Symbol):
    """
        name: tFUNUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 226.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tFUNUSD"
    significant_digits: int = 5
    tick_size: int = None
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


FUNUSD = FUNUSD(*FUNUSD._fields)


class GALA_USD(Symbol):
    """
        name: tGALA:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGALA:USD"
    significant_digits: int = 5
    tick_size: int = None
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


GALA_USD = GALA_USD(*GALA_USD._fields)


class GALA_UST(Symbol):
    """
        name: tGALA:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGALA:UST"
    significant_digits: int = 5
    tick_size: int = None
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


GALA_UST = GALA_UST(*GALA_UST._fields)


class GALAF0_USTF0(Symbol):
    """
        name: tGALAF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tGALAF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


GALAF0_USTF0 = GALAF0_USTF0(*GALAF0_USTF0._fields)


class GBPEUT(Symbol):
    """
        name: tGBPEUT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGBPEUT"
    significant_digits: int = 5
    tick_size: int = None
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


GBPEUT = GBPEUT(*GBPEUT._fields)


class GBPF0_USTF0(Symbol):
    """
        name: tGBPF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tGBPF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


GBPF0_USTF0 = GBPF0_USTF0(*GBPF0_USTF0._fields)


class GBPUST(Symbol):
    """
        name: tGBPUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGBPUST"
    significant_digits: int = 5
    tick_size: int = None
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


GBPUST = GBPUST(*GBPUST._fields)


class GERMANY40IXF0_USTF0(Symbol):
    """
        name: tGERMANY40IXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.0004
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tGERMANY40IXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


GERMANY40IXF0_USTF0 = GERMANY40IXF0_USTF0(*GERMANY40IXF0_USTF0._fields)


class GNOUSD(Symbol):
    """
        name: tGNOUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 1000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGNOUSD"
    significant_digits: int = 5
    tick_size: int = None
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


GNOUSD = GNOUSD(*GNOUSD._fields)


class GNTUSD(Symbol):
    """
        name: tGNTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGNTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


GNTUSD = GNTUSD(*GNTUSD._fields)


class GPTUSD(Symbol):
    """
        name: tGPTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 400000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGPTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


GPTUSD = GPTUSD(*GPTUSD._fields)


class GPTUST(Symbol):
    """
        name: tGPTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 400000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGPTUST"
    significant_digits: int = 5
    tick_size: int = None
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


GPTUST = GPTUST(*GPTUST._fields)


class GRTUSD(Symbol):
    """
        name: tGRTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGRTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


GRTUSD = GRTUSD(*GRTUSD._fields)


class GRTUST(Symbol):
    """
        name: tGRTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGRTUST"
    significant_digits: int = 5
    tick_size: int = None
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


GRTUST = GRTUST(*GRTUST._fields)


class GTXUSD(Symbol):
    """
        name: tGTXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGTXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


GTXUSD = GTXUSD(*GTXUSD._fields)


class GTXUST(Symbol):
    """
        name: tGTXUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGTXUST"
    significant_digits: int = 5
    tick_size: int = None
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


GTXUST = GTXUST(*GTXUST._fields)


class GXTUSD(Symbol):
    """
        name: tGXTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGXTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


GXTUSD = GXTUSD(*GXTUSD._fields)


class GXTUST(Symbol):
    """
        name: tGXTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tGXTUST"
    significant_digits: int = 5
    tick_size: int = None
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


GXTUST = GXTUST(*GXTUST._fields)


class HECUSD(Symbol):
    """
        name: tHECUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHECUSD"
    significant_digits: int = 5
    tick_size: int = None
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


HECUSD = HECUSD(*HECUSD._fields)


class HECUST(Symbol):
    """
        name: tHECUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHECUST"
    significant_digits: int = 5
    tick_size: int = None
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


HECUST = HECUST(*HECUST._fields)


class HIXUSD(Symbol):
    """
        name: tHIXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHIXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


HIXUSD = HIXUSD(*HIXUSD._fields)


class HIXUST(Symbol):
    """
        name: tHIXUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHIXUST"
    significant_digits: int = 5
    tick_size: int = None
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


HIXUST = HIXUST(*HIXUST._fields)


class HMTUSD(Symbol):
    """
        name: tHMTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHMTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


HMTUSD = HMTUSD(*HMTUSD._fields)


class HMTUST(Symbol):
    """
        name: tHMTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHMTUST"
    significant_digits: int = 5
    tick_size: int = None
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


HMTUST = HMTUST(*HMTUST._fields)


class HONGKONG50IXF0_USTF0(Symbol):
    """
        name: tHONGKONG50IXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tHONGKONG50IXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


HONGKONG50IXF0_USTF0 = HONGKONG50IXF0_USTF0(*HONGKONG50IXF0_USTF0._fields)


class HTXUSD(Symbol):
    """
        name: tHTXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHTXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


HTXUSD = HTXUSD(*HTXUSD._fields)


class HTXUST(Symbol):
    """
        name: tHTXUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tHTXUST"
    significant_digits: int = 5
    tick_size: int = None
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


HTXUST = HTXUST(*HTXUST._fields)


class ICEUSD(Symbol):
    """
        name: tICEUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tICEUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ICEUSD = ICEUSD(*ICEUSD._fields)


class ICPBTC(Symbol):
    """
        name: tICPBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tICPBTC"
    significant_digits: int = 5
    tick_size: int = None
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


ICPBTC = ICPBTC(*ICPBTC._fields)


class ICPF0_USTF0(Symbol):
    """
        name: tICPF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tICPF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


ICPF0_USTF0 = ICPF0_USTF0(*ICPF0_USTF0._fields)


class ICPUSD(Symbol):
    """
        name: tICPUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tICPUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ICPUSD = ICPUSD(*ICPUSD._fields)


class ICPUST(Symbol):
    """
        name: tICPUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tICPUST"
    significant_digits: int = 5
    tick_size: int = None
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


ICPUST = ICPUST(*ICPUST._fields)


class IDXUSD(Symbol):
    """
        name: tIDXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tIDXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


IDXUSD = IDXUSD(*IDXUSD._fields)


class IDXUST(Symbol):
    """
        name: tIDXUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tIDXUST"
    significant_digits: int = 5
    tick_size: int = None
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


IDXUST = IDXUST(*IDXUST._fields)


class IOTBTC(Symbol):
    """
        name: tIOTBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tIOTBTC"
    significant_digits: int = 5
    tick_size: int = None
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


IOTBTC = IOTBTC(*IOTBTC._fields)


class IOTF0_USTF0(Symbol):
    """
        name: tIOTF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tIOTF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


IOTF0_USTF0 = IOTF0_USTF0(*IOTF0_USTF0._fields)


class IOTUSD(Symbol):
    """
        name: tIOTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tIOTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


IOTUSD = IOTUSD(*IOTUSD._fields)


class JAPAN225IXF0_USTF0(Symbol):
    """
        name: tJAPAN225IXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tJAPAN225IXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


JAPAN225IXF0_USTF0 = JAPAN225IXF0_USTF0(*JAPAN225IXF0_USTF0._fields)


class JASMY_USD(Symbol):
    """
        name: tJASMY:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 168.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJASMY:USD"
    significant_digits: int = 5
    tick_size: int = None
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


JASMY_USD = JASMY_USD(*JASMY_USD._fields)


class JASMY_UST(Symbol):
    """
        name: tJASMY:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 168.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJASMY:UST"
    significant_digits: int = 5
    tick_size: int = None
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


JASMY_UST = JASMY_UST(*JASMY_UST._fields)


class JASMYF0_USTF0(Symbol):
    """
        name: tJASMYF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 168.0
        max_order_size: 2500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tJASMYF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


JASMYF0_USTF0 = JASMYF0_USTF0(*JASMYF0_USTF0._fields)


class JPYF0_USTF0(Symbol):
    """
        name: tJPYF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 262.0
        max_order_size: 100000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tJPYF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


JPYF0_USTF0 = JPYF0_USTF0(*JPYF0_USTF0._fields)


class JPYUST(Symbol):
    """
        name: tJPYUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 262.0
        max_order_size: 100000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJPYUST"
    significant_digits: int = 5
    tick_size: int = None
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


JPYUST = JPYUST(*JPYUST._fields)


class JSTBTC(Symbol):
    """
        name: tJSTBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 48.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJSTBTC"
    significant_digits: int = 5
    tick_size: int = None
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


JSTBTC = JSTBTC(*JSTBTC._fields)


class JSTUSD(Symbol):
    """
        name: tJSTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 48.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJSTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


JSTUSD = JSTUSD(*JSTUSD._fields)


class JSTUST(Symbol):
    """
        name: tJSTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 48.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tJSTUST"
    significant_digits: int = 5
    tick_size: int = None
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


JSTUST = JSTUST(*JSTUST._fields)


class KANUSD(Symbol):
    """
        name: tKANUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1542.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKANUSD"
    significant_digits: int = 5
    tick_size: int = None
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


KANUSD = KANUSD(*KANUSD._fields)


class KANUST(Symbol):
    """
        name: tKANUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1542.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKANUST"
    significant_digits: int = 5
    tick_size: int = None
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


KANUST = KANUST(*KANUST._fields)


class KNCBTC(Symbol):
    """
        name: tKNCBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKNCBTC"
    significant_digits: int = 5
    tick_size: int = None
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


KNCBTC = KNCBTC(*KNCBTC._fields)


class KNCF0_USTF0(Symbol):
    """
        name: tKNCF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tKNCF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


KNCF0_USTF0 = KNCF0_USTF0(*KNCF0_USTF0._fields)


class KNCUSD(Symbol):
    """
        name: tKNCUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKNCUSD"
    significant_digits: int = 5
    tick_size: int = None
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


KNCUSD = KNCUSD(*KNCUSD._fields)


class KSMUSD(Symbol):
    """
        name: tKSMUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKSMUSD"
    significant_digits: int = 5
    tick_size: int = None
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


KSMUSD = KSMUSD(*KSMUSD._fields)


class KSMUST(Symbol):
    """
        name: tKSMUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tKSMUST"
    significant_digits: int = 5
    tick_size: int = None
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


KSMUST = KSMUST(*KSMUST._fields)


class LDOUSD(Symbol):
    """
        name: tLDOUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLDOUSD"
    significant_digits: int = 5
    tick_size: int = None
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


LDOUSD = LDOUSD(*LDOUSD._fields)


class LDOUST(Symbol):
    """
        name: tLDOUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLDOUST"
    significant_digits: int = 5
    tick_size: int = None
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


LDOUST = LDOUST(*LDOUST._fields)


class LEOBTC(Symbol):
    """
        name: tLEOBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLEOBTC"
    significant_digits: int = 5
    tick_size: int = None
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


LEOBTC = LEOBTC(*LEOBTC._fields)


class LEOETH(Symbol):
    """
        name: tLEOETH
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLEOETH"
    significant_digits: int = 5
    tick_size: int = None
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


LEOETH = LEOETH(*LEOETH._fields)


class LEOUSD(Symbol):
    """
        name: tLEOUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLEOUSD"
    significant_digits: int = 5
    tick_size: int = None
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


LEOUSD = LEOUSD(*LEOUSD._fields)


class LEOUST(Symbol):
    """
        name: tLEOUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLEOUST"
    significant_digits: int = 5
    tick_size: int = None
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


LEOUST = LEOUST(*LEOUST._fields)


class LINK_USD(Symbol):
    """
        name: tLINK:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLINK:USD"
    significant_digits: int = 5
    tick_size: int = None
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


LINK_USD = LINK_USD(*LINK_USD._fields)


class LINK_UST(Symbol):
    """
        name: tLINK:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLINK:UST"
    significant_digits: int = 5
    tick_size: int = None
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


LINK_UST = LINK_UST(*LINK_UST._fields)


class LINKF0_USTF0(Symbol):
    """
        name: tLINKF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLINKF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


LINKF0_USTF0 = LINKF0_USTF0(*LINKF0_USTF0._fields)


class LRCUSD(Symbol):
    """
        name: tLRCUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLRCUSD"
    significant_digits: int = 5
    tick_size: int = None
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


LRCUSD = LRCUSD(*LRCUSD._fields)


class LTCBTC(Symbol):
    """
        name: tLTCBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCBTC"
    significant_digits: int = 5
    tick_size: int = None
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


LTCBTC = LTCBTC(*LTCBTC._fields)


class LTCF0_BTCF0(Symbol):
    """
        name: tLTCF0:BTCF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.04
        max_order_size: 7500.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCF0:BTCF0"
    significant_digits: int = 5
    tick_size: int = None
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


LTCF0_BTCF0 = LTCF0_BTCF0(*LTCF0_BTCF0._fields)


class LTCF0_USTF0(Symbol):
    """
        name: tLTCF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.04
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


LTCF0_USTF0 = LTCF0_USTF0(*LTCF0_USTF0._fields)


class LTCUSD(Symbol):
    """
        name: tLTCUSD
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.04
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCUSD"
    significant_digits: int = 5
    tick_size: int = None
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


LTCUSD = LTCUSD(*LTCUSD._fields)


class LTCUST(Symbol):
    """
        name: tLTCUST
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.04
        max_order_size: 2000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tLTCUST"
    significant_digits: int = 5
    tick_size: int = None
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


LTCUST = LTCUST(*LTCUST._fields)


class LUNA2_USD(Symbol):
    """
        name: tLUNA2:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUNA2:USD"
    significant_digits: int = 5
    tick_size: int = None
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


LUNA2_USD = LUNA2_USD(*LUNA2_USD._fields)


class LUNA2_UST(Symbol):
    """
        name: tLUNA2:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUNA2:UST"
    significant_digits: int = 5
    tick_size: int = None
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


LUNA2_UST = LUNA2_UST(*LUNA2_UST._fields)


class LUNA_USD(Symbol):
    """
        name: tLUNA:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20814.0
        max_order_size: 100000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUNA:USD"
    significant_digits: int = 5
    tick_size: int = None
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


LUNA_USD = LUNA_USD(*LUNA_USD._fields)


class LUNA_UST(Symbol):
    """
        name: tLUNA:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20814.0
        max_order_size: 100000000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUNA:UST"
    significant_digits: int = 5
    tick_size: int = None
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


LUNA_UST = LUNA_UST(*LUNA_UST._fields)


class LUXO_USD(Symbol):
    """
        name: tLUXO:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLUXO:USD"
    significant_digits: int = 5
    tick_size: int = None
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


LUXO_USD = LUXO_USD(*LUXO_USD._fields)


class LYMUSD(Symbol):
    """
        name: tLYMUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 740.0
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tLYMUSD"
    significant_digits: int = 5
    tick_size: int = None
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


LYMUSD = LYMUSD(*LYMUSD._fields)


class MATIC_BTC(Symbol):
    """
        name: tMATIC:BTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMATIC:BTC"
    significant_digits: int = 5
    tick_size: int = None
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


MATIC_BTC = MATIC_BTC(*MATIC_BTC._fields)


class MATIC_USD(Symbol):
    """
        name: tMATIC:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMATIC:USD"
    significant_digits: int = 5
    tick_size: int = None
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


MATIC_USD = MATIC_USD(*MATIC_USD._fields)


class MATIC_UST(Symbol):
    """
        name: tMATIC:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMATIC:UST"
    significant_digits: int = 5
    tick_size: int = None
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


MATIC_UST = MATIC_UST(*MATIC_UST._fields)


class MATICF0_USTF0(Symbol):
    """
        name: tMATICF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMATICF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


MATICF0_USTF0 = MATICF0_USTF0(*MATICF0_USTF0._fields)


class MIMUSD(Symbol):
    """
        name: tMIMUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMIMUSD"
    significant_digits: int = 5
    tick_size: int = None
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


MIMUSD = MIMUSD(*MIMUSD._fields)


class MIMUST(Symbol):
    """
        name: tMIMUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMIMUST"
    significant_digits: int = 5
    tick_size: int = None
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


MIMUST = MIMUST(*MIMUST._fields)


class MKRF0_USTF0(Symbol):
    """
        name: tMKRF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 2500.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMKRF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


MKRF0_USTF0 = MKRF0_USTF0(*MKRF0_USTF0._fields)


class MKRUSD(Symbol):
    """
        name: tMKRUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 2500.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tMKRUSD"
    significant_digits: int = 5
    tick_size: int = None
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


MKRUSD = MKRUSD(*MKRUSD._fields)


class MKRUST(Symbol):
    """
        name: tMKRUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.002
        max_order_size: 2500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMKRUST"
    significant_digits: int = 5
    tick_size: int = None
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


MKRUST = MKRUST(*MKRUST._fields)


class MLNUSD(Symbol):
    """
        name: tMLNUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.08
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMLNUSD"
    significant_digits: int = 5
    tick_size: int = None
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


MLNUSD = MLNUSD(*MLNUSD._fields)


class MNABTC(Symbol):
    """
        name: tMNABTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMNABTC"
    significant_digits: int = 5
    tick_size: int = None
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


MNABTC = MNABTC(*MNABTC._fields)


class MNAUSD(Symbol):
    """
        name: tMNAUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMNAUSD"
    significant_digits: int = 5
    tick_size: int = None
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


MNAUSD = MNAUSD(*MNAUSD._fields)


class MOBUSD(Symbol):
    """
        name: tMOBUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMOBUSD"
    significant_digits: int = 5
    tick_size: int = None
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


MOBUSD = MOBUSD(*MOBUSD._fields)


class MOBUST(Symbol):
    """
        name: tMOBUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMOBUST"
    significant_digits: int = 5
    tick_size: int = None
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


MOBUST = MOBUST(*MOBUST._fields)


class MXNT_USD(Symbol):
    """
        name: tMXNT:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tMXNT:USD"
    significant_digits: int = 5
    tick_size: int = None
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


MXNT_USD = MXNT_USD(*MXNT_USD._fields)


class NEAR_USD(Symbol):
    """
        name: tNEAR:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEAR:USD"
    significant_digits: int = 5
    tick_size: int = None
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


NEAR_USD = NEAR_USD(*NEAR_USD._fields)


class NEAR_UST(Symbol):
    """
        name: tNEAR:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 25000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEAR:UST"
    significant_digits: int = 5
    tick_size: int = None
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


NEAR_UST = NEAR_UST(*NEAR_UST._fields)


class NEARF0_USTF0(Symbol):
    """
        name: tNEARF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.4
        max_order_size: 25000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEARF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


NEARF0_USTF0 = NEARF0_USTF0(*NEARF0_USTF0._fields)


class NEOBTC(Symbol):
    """
        name: tNEOBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEOBTC"
    significant_digits: int = 5
    tick_size: int = None
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


NEOBTC = NEOBTC(*NEOBTC._fields)


class NEOF0_USTF0(Symbol):
    """
        name: tNEOF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEOF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


NEOF0_USTF0 = NEOF0_USTF0(*NEOF0_USTF0._fields)


class NEOUSD(Symbol):
    """
        name: tNEOUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEOUSD"
    significant_digits: int = 5
    tick_size: int = None
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


NEOUSD = NEOUSD(*NEOUSD._fields)


class NEOUST(Symbol):
    """
        name: tNEOUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tNEOUST"
    significant_digits: int = 5
    tick_size: int = None
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


NEOUST = NEOUST(*NEOUST._fields)


class NEXO_BTC(Symbol):
    """
        name: tNEXO:BTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEXO:BTC"
    significant_digits: int = 5
    tick_size: int = None
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


NEXO_BTC = NEXO_BTC(*NEXO_BTC._fields)


class NEXO_USD(Symbol):
    """
        name: tNEXO:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEXO:USD"
    significant_digits: int = 5
    tick_size: int = None
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


NEXO_USD = NEXO_USD(*NEXO_USD._fields)


class NEXO_UST(Symbol):
    """
        name: tNEXO:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNEXO:UST"
    significant_digits: int = 5
    tick_size: int = None
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


NEXO_UST = NEXO_UST(*NEXO_UST._fields)


class NOMUSD(Symbol):
    """
        name: tNOMUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNOMUSD"
    significant_digits: int = 5
    tick_size: int = None
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


NOMUSD = NOMUSD(*NOMUSD._fields)


class NOMUST(Symbol):
    """
        name: tNOMUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNOMUST"
    significant_digits: int = 5
    tick_size: int = None
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


NOMUST = NOMUST(*NOMUST._fields)


class NXRA_USD(Symbol):
    """
        name: tNXRA:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 200000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tNXRA:USD"
    significant_digits: int = 5
    tick_size: int = None
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


NXRA_USD = NXRA_USD(*NXRA_USD._fields)


class OCEAN_USD(Symbol):
    """
        name: tOCEAN:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOCEAN:USD"
    significant_digits: int = 5
    tick_size: int = None
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


OCEAN_USD = OCEAN_USD(*OCEAN_USD._fields)


class OCEAN_UST(Symbol):
    """
        name: tOCEAN:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOCEAN:UST"
    significant_digits: int = 5
    tick_size: int = None
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


OCEAN_UST = OCEAN_UST(*OCEAN_UST._fields)


class OGNUSD(Symbol):
    """
        name: tOGNUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOGNUSD"
    significant_digits: int = 5
    tick_size: int = None
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


OGNUSD = OGNUSD(*OGNUSD._fields)


class OGNUST(Symbol):
    """
        name: tOGNUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOGNUST"
    significant_digits: int = 5
    tick_size: int = None
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


OGNUST = OGNUST(*OGNUST._fields)


class OMGBTC(Symbol):
    """
        name: tOMGBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tOMGBTC"
    significant_digits: int = 5
    tick_size: int = None
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


OMGBTC = OMGBTC(*OMGBTC._fields)


class OMGETH(Symbol):
    """
        name: tOMGETH
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tOMGETH"
    significant_digits: int = 5
    tick_size: int = None
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


OMGETH = OMGETH(*OMGETH._fields)


class OMGF0_USTF0(Symbol):
    """
        name: tOMGF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.8
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tOMGF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


OMGF0_USTF0 = OMGF0_USTF0(*OMGF0_USTF0._fields)


class OMGUSD(Symbol):
    """
        name: tOMGUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tOMGUSD"
    significant_digits: int = 5
    tick_size: int = None
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


OMGUSD = OMGUSD(*OMGUSD._fields)


class OMNUSD(Symbol):
    """
        name: tOMNUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 20000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tOMNUSD"
    significant_digits: int = 5
    tick_size: int = None
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


OMNUSD = OMNUSD(*OMNUSD._fields)


class ONEUSD(Symbol):
    """
        name: tONEUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tONEUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ONEUSD = ONEUSD(*ONEUSD._fields)


class ONEUST(Symbol):
    """
        name: tONEUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tONEUST"
    significant_digits: int = 5
    tick_size: int = None
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


ONEUST = ONEUST(*ONEUST._fields)


class PASUSD(Symbol):
    """
        name: tPASUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1588.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPASUSD"
    significant_digits: int = 5
    tick_size: int = None
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


PASUSD = PASUSD(*PASUSD._fields)


class PAXUSD(Symbol):
    """
        name: tPAXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPAXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


PAXUSD = PAXUSD(*PAXUSD._fields)


class PAXUST(Symbol):
    """
        name: tPAXUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPAXUST"
    significant_digits: int = 5
    tick_size: int = None
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


PAXUST = PAXUST(*PAXUST._fields)


class PLANETS_USD(Symbol):
    """
        name: tPLANETS:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 124.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPLANETS:USD"
    significant_digits: int = 5
    tick_size: int = None
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


PLANETS_USD = PLANETS_USD(*PLANETS_USD._fields)


class PLANETS_UST(Symbol):
    """
        name: tPLANETS:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 124.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPLANETS:UST"
    significant_digits: int = 5
    tick_size: int = None
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


PLANETS_UST = PLANETS_UST(*PLANETS_UST._fields)


class PLUUSD(Symbol):
    """
        name: tPLUUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 10000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPLUUSD"
    significant_digits: int = 5
    tick_size: int = None
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


PLUUSD = PLUUSD(*PLUUSD._fields)


class PNKUSD(Symbol):
    """
        name: tPNKUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPNKUSD"
    significant_digits: int = 5
    tick_size: int = None
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


PNKUSD = PNKUSD(*PNKUSD._fields)


class POLC_USD(Symbol):
    """
        name: tPOLC:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPOLC:USD"
    significant_digits: int = 5
    tick_size: int = None
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


POLC_USD = POLC_USD(*POLC_USD._fields)


class POLC_UST(Symbol):
    """
        name: tPOLC:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 26.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPOLC:UST"
    significant_digits: int = 5
    tick_size: int = None
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


POLC_UST = POLC_UST(*POLC_UST._fields)


class POLIS_USD(Symbol):
    """
        name: tPOLIS:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPOLIS:USD"
    significant_digits: int = 5
    tick_size: int = None
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


POLIS_USD = POLIS_USD(*POLIS_USD._fields)


class POLIS_UST(Symbol):
    """
        name: tPOLIS:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPOLIS:UST"
    significant_digits: int = 5
    tick_size: int = None
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


POLIS_UST = POLIS_UST(*POLIS_UST._fields)


class PRMX_USD(Symbol):
    """
        name: tPRMX:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 4000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPRMX:USD"
    significant_digits: int = 5
    tick_size: int = None
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


PRMX_USD = PRMX_USD(*PRMX_USD._fields)


class PRMX_UST(Symbol):
    """
        name: tPRMX:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 4000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tPRMX:UST"
    significant_digits: int = 5
    tick_size: int = None
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


PRMX_UST = PRMX_UST(*PRMX_UST._fields)


class QRDO_USD(Symbol):
    """
        name: tQRDO:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQRDO:USD"
    significant_digits: int = 5
    tick_size: int = None
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


QRDO_USD = QRDO_USD(*QRDO_USD._fields)


class QRDO_UST(Symbol):
    """
        name: tQRDO:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQRDO:UST"
    significant_digits: int = 5
    tick_size: int = None
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


QRDO_UST = QRDO_UST(*QRDO_UST._fields)


class QTFBTC(Symbol):
    """
        name: tQTFBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQTFBTC"
    significant_digits: int = 5
    tick_size: int = None
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


QTFBTC = QTFBTC(*QTFBTC._fields)


class QTFUSD(Symbol):
    """
        name: tQTFUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQTFUSD"
    significant_digits: int = 5
    tick_size: int = None
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


QTFUSD = QTFUSD(*QTFUSD._fields)


class QTMUSD(Symbol):
    """
        name: tQTMUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.6
        max_order_size: 5000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tQTMUSD"
    significant_digits: int = 5
    tick_size: int = None
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


QTMUSD = QTMUSD(*QTMUSD._fields)


class RBTUSD(Symbol):
    """
        name: tRBTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 500.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tRBTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


RBTUSD = RBTUSD(*RBTUSD._fields)


class REEF_USD(Symbol):
    """
        name: tREEF:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 466.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tREEF:USD"
    significant_digits: int = 5
    tick_size: int = None
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


REEF_USD = REEF_USD(*REEF_USD._fields)


class REEF_UST(Symbol):
    """
        name: tREEF:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 466.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tREEF:UST"
    significant_digits: int = 5
    tick_size: int = None
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


REEF_UST = REEF_UST(*REEF_UST._fields)


class REPUSD(Symbol):
    """
        name: tREPUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 1000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tREPUSD"
    significant_digits: int = 5
    tick_size: int = None
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


REPUSD = REPUSD(*REPUSD._fields)


class REQUSD(Symbol):
    """
        name: tREQUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 16.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tREQUSD"
    significant_digits: int = 5
    tick_size: int = None
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


REQUSD = REQUSD(*REQUSD._fields)


class RLYUSD(Symbol):
    """
        name: tRLYUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tRLYUSD"
    significant_digits: int = 5
    tick_size: int = None
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


RLYUSD = RLYUSD(*RLYUSD._fields)


class RLYUST(Symbol):
    """
        name: tRLYUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tRLYUST"
    significant_digits: int = 5
    tick_size: int = None
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


RLYUST = RLYUST(*RLYUST._fields)


class RRTUSD(Symbol):
    """
        name: tRRTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tRRTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


RRTUSD = RRTUSD(*RRTUSD._fields)


class SAND_USD(Symbol):
    """
        name: tSAND:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSAND:USD"
    significant_digits: int = 5
    tick_size: int = None
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


SAND_USD = SAND_USD(*SAND_USD._fields)


class SAND_UST(Symbol):
    """
        name: tSAND:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSAND:UST"
    significant_digits: int = 5
    tick_size: int = None
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


SAND_UST = SAND_UST(*SAND_UST._fields)


class SANDF0_USTF0(Symbol):
    """
        name: tSANDF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSANDF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


SANDF0_USTF0 = SANDF0_USTF0(*SANDF0_USTF0._fields)


class SENATE_USD(Symbol):
    """
        name: tSENATE:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 20.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSENATE:USD"
    significant_digits: int = 5
    tick_size: int = None
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


SENATE_USD = SENATE_USD(*SENATE_USD._fields)


class SGBUSD(Symbol):
    """
        name: tSGBUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSGBUSD"
    significant_digits: int = 5
    tick_size: int = None
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


SGBUSD = SGBUSD(*SGBUSD._fields)


class SGBUST(Symbol):
    """
        name: tSGBUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSGBUST"
    significant_digits: int = 5
    tick_size: int = None
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


SGBUST = SGBUST(*SGBUST._fields)


class SHFT_USD(Symbol):
    """
        name: tSHFT:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSHFT:USD"
    significant_digits: int = 5
    tick_size: int = None
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


SHFT_USD = SHFT_USD(*SHFT_USD._fields)


class SHFT_UST(Symbol):
    """
        name: tSHFT:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 52.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSHFT:UST"
    significant_digits: int = 5
    tick_size: int = None
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


SHFT_UST = SHFT_UST(*SHFT_UST._fields)


class SHIB_USD(Symbol):
    """
        name: tSHIB:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 187004.0
        max_order_size: 5000000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSHIB:USD"
    significant_digits: int = 5
    tick_size: int = None
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


SHIB_USD = SHIB_USD(*SHIB_USD._fields)


class SHIB_UST(Symbol):
    """
        name: tSHIB:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 187004.0
        max_order_size: 5000000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSHIB:UST"
    significant_digits: int = 5
    tick_size: int = None
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


SHIB_UST = SHIB_UST(*SHIB_UST._fields)


class SHIBF0_USTF0(Symbol):
    """
        name: tSHIBF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 187004.0
        max_order_size: 5000000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSHIBF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


SHIBF0_USTF0 = SHIBF0_USTF0(*SHIBF0_USTF0._fields)


class SIDUS_USD(Symbol):
    """
        name: tSIDUS:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 664.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSIDUS:USD"
    significant_digits: int = 5
    tick_size: int = None
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


SIDUS_USD = SIDUS_USD(*SIDUS_USD._fields)


class SMRUSD(Symbol):
    """
        name: tSMRUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 700000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSMRUSD"
    significant_digits: int = 5
    tick_size: int = None
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


SMRUSD = SMRUSD(*SMRUSD._fields)


class SMRUST(Symbol):
    """
        name: tSMRUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 700000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSMRUST"
    significant_digits: int = 5
    tick_size: int = None
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


SMRUST = SMRUST(*SMRUST._fields)


class SNTUSD(Symbol):
    """
        name: tSNTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 48.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSNTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


SNTUSD = SNTUSD(*SNTUSD._fields)


class SNXUSD(Symbol):
    """
        name: tSNXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSNXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


SNXUSD = SNXUSD(*SNXUSD._fields)


class SNXUST(Symbol):
    """
        name: tSNXUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.8
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSNXUST"
    significant_digits: int = 5
    tick_size: int = None
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


SNXUST = SNXUST(*SNXUST._fields)


class SOLBTC(Symbol):
    """
        name: tSOLBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.06
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLBTC"
    significant_digits: int = 5
    tick_size: int = None
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


SOLBTC = SOLBTC(*SOLBTC._fields)


class SOLF0_BTCF0(Symbol):
    """
        name: tSOLF0:BTCF0
        significant_digits: 5
        tick_size: None
        min_margin: 2.5
        initial_margin: 5.0
        min_order_size: 0.06
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLF0:BTCF0"
    significant_digits: int = 5
    tick_size: int = None
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


SOLF0_BTCF0 = SOLF0_BTCF0(*SOLF0_BTCF0._fields)


class SOLF0_USTF0(Symbol):
    """
        name: tSOLF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 2.5
        initial_margin: 5.0
        min_order_size: 0.06
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


SOLF0_USTF0 = SOLF0_USTF0(*SOLF0_USTF0._fields)


class SOLUSD(Symbol):
    """
        name: tSOLUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.06
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLUSD"
    significant_digits: int = 5
    tick_size: int = None
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


SOLUSD = SOLUSD(*SOLUSD._fields)


class SOLUST(Symbol):
    """
        name: tSOLUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.06
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSOLUST"
    significant_digits: int = 5
    tick_size: int = None
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


SOLUST = SOLUST(*SOLUST._fields)


class SPAIN35IXF0_USTF0(Symbol):
    """
        name: tSPAIN35IXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSPAIN35IXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


SPAIN35IXF0_USTF0 = SPAIN35IXF0_USTF0(*SPAIN35IXF0_USTF0._fields)


class SPELL_USD(Symbol):
    """
        name: tSPELL:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 1640.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSPELL:USD"
    significant_digits: int = 5
    tick_size: int = None
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


SPELL_USD = SPELL_USD(*SPELL_USD._fields)


class STGF0_USTF0(Symbol):
    """
        name: tSTGF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSTGF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


STGF0_USTF0 = STGF0_USTF0(*STGF0_USTF0._fields)


class STGUSD(Symbol):
    """
        name: tSTGUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSTGUSD"
    significant_digits: int = 5
    tick_size: int = None
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


STGUSD = STGUSD(*STGUSD._fields)


class STGUST(Symbol):
    """
        name: tSTGUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSTGUST"
    significant_digits: int = 5
    tick_size: int = None
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


STGUST = STGUST(*STGUST._fields)


class STJUSD(Symbol):
    """
        name: tSTJUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 30000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSTJUSD"
    significant_digits: int = 5
    tick_size: int = None
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


STJUSD = STJUSD(*STJUSD._fields)


class SUIUSD(Symbol):
    """
        name: tSUIUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUIUSD"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tSUIUSD"

    def __str__(self):
        return "tSUIUSD"

    def __call__(self):
        return "tSUIUSD"


SUIUSD = SUIUSD(*SUIUSD._fields)


class SUIUST(Symbol):
    """
        name: tSUIUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUIUST"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tSUIUST"

    def __str__(self):
        return "tSUIUST"

    def __call__(self):
        return "tSUIUST"


SUIUST = SUIUST(*SUIUST._fields)


class SUKU_USD(Symbol):
    """
        name: tSUKU:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUKU:USD"
    significant_digits: int = 5
    tick_size: int = None
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


SUKU_USD = SUKU_USD(*SUKU_USD._fields)


class SUKU_UST(Symbol):
    """
        name: tSUKU:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 18.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUKU:UST"
    significant_digits: int = 5
    tick_size: int = None
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


SUKU_UST = SUKU_UST(*SUKU_UST._fields)


class SUNUSD(Symbol):
    """
        name: tSUNUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 216.0
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUNUSD"
    significant_digits: int = 5
    tick_size: int = None
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


SUNUSD = SUNUSD(*SUNUSD._fields)


class SUNUST(Symbol):
    """
        name: tSUNUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 216.0
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSUNUST"
    significant_digits: int = 5
    tick_size: int = None
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


SUNUST = SUNUST(*SUNUST._fields)


class SUSHI_USD(Symbol):
    """
        name: tSUSHI:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSUSHI:USD"
    significant_digits: int = 5
    tick_size: int = None
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


SUSHI_USD = SUSHI_USD(*SUSHI_USD._fields)


class SUSHI_UST(Symbol):
    """
        name: tSUSHI:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSUSHI:UST"
    significant_digits: int = 5
    tick_size: int = None
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


SUSHI_UST = SUSHI_UST(*SUSHI_UST._fields)


class SUSHIF0_USTF0(Symbol):
    """
        name: tSUSHIF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tSUSHIF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


SUSHIF0_USTF0 = SUSHIF0_USTF0(*SUSHIF0_USTF0._fields)


class SWEAT_USD(Symbol):
    """
        name: tSWEAT:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 7000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSWEAT:USD"
    significant_digits: int = 5
    tick_size: int = None
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


SWEAT_USD = SWEAT_USD(*SWEAT_USD._fields)


class SWEAT_UST(Symbol):
    """
        name: tSWEAT:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 7000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSWEAT:UST"
    significant_digits: int = 5
    tick_size: int = None
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


SWEAT_UST = SWEAT_UST(*SWEAT_UST._fields)


class SXXUSD(Symbol):
    """
        name: tSXXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tSXXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


SXXUSD = SXXUSD(*SXXUSD._fields)


class TERRAUST_USD(Symbol):
    """
        name: tTERRAUST:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 100.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTERRAUST:USD"
    significant_digits: int = 5
    tick_size: int = None
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


TERRAUST_USD = TERRAUST_USD(*TERRAUST_USD._fields)


class TESTADA_TESTUSD(Symbol):
    """
        name: tTESTADA:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTADA:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTADA:TESTUSD"

    def __str__(self):
        return "tTESTADA:TESTUSD"

    def __call__(self):
        return "tTESTADA:TESTUSD"


TESTADA_TESTUSD = TESTADA_TESTUSD(*TESTADA_TESTUSD._fields)


class TESTADAF0_TESTUSDTF0(Symbol):
    """
        name: tTESTADAF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTADAF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTADAF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTADAF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTADAF0:TESTUSDTF0"


TESTADAF0_TESTUSDTF0 = TESTADAF0_TESTUSDTF0(*TESTADAF0_TESTUSDTF0._fields)


class TESTALGO_TESTUSD(Symbol):
    """
        name: tTESTALGO:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTALGO:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTALGO:TESTUSD"

    def __str__(self):
        return "tTESTALGO:TESTUSD"

    def __call__(self):
        return "tTESTALGO:TESTUSD"


TESTALGO_TESTUSD = TESTALGO_TESTUSD(*TESTALGO_TESTUSD._fields)


class TESTALGOF0_TESTUSDTF0(Symbol):
    """
        name: tTESTALGOF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTALGOF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTALGOF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTALGOF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTALGOF0:TESTUSDTF0"


TESTALGOF0_TESTUSDTF0 = TESTALGOF0_TESTUSDTF0(*TESTALGOF0_TESTUSDTF0._fields)


class TESTAPT_TESTUSD(Symbol):
    """
        name: tTESTAPT:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTAPT:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTAPT_TESTUSD = TESTAPT_TESTUSD(*TESTAPT_TESTUSD._fields)


class TESTAPTF0_TESTUSDTF0(Symbol):
    """
        name: tTESTAPTF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTAPTF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTAPTF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTAPTF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTAPTF0:TESTUSDTF0"


TESTAPTF0_TESTUSDTF0 = TESTAPTF0_TESTUSDTF0(*TESTAPTF0_TESTUSDTF0._fields)


class TESTAVAX_TESTUSD(Symbol):
    """
        name: tTESTAVAX:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTAVAX:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTAVAX_TESTUSD = TESTAVAX_TESTUSD(*TESTAVAX_TESTUSD._fields)


class TESTAVAXF0_TESTUSDTF0(Symbol):
    """
        name: tTESTAVAXF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTAVAXF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTAVAXF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTAVAXF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTAVAXF0:TESTUSDTF0"


TESTAVAXF0_TESTUSDTF0 = TESTAVAXF0_TESTUSDTF0(*TESTAVAXF0_TESTUSDTF0._fields)


class TESTBTC_TESTUSD(Symbol):
    """
        name: tTESTBTC:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTBTC:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTBTC_TESTUSD = TESTBTC_TESTUSD(*TESTBTC_TESTUSD._fields)


class TESTBTC_TESTUSDT(Symbol):
    """
        name: tTESTBTC:TESTUSDT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTBTC:TESTUSDT"
    significant_digits: int = 5
    tick_size: int = None
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


TESTBTC_TESTUSDT = TESTBTC_TESTUSDT(*TESTBTC_TESTUSDT._fields)


class TESTBTCF0_TESTUSDTF0(Symbol):
    """
        name: tTESTBTCF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.00006
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTBTCF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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


TESTBTCF0_TESTUSDTF0 = TESTBTCF0_TESTUSDTF0(*TESTBTCF0_TESTUSDTF0._fields)


class TESTDOGE_TESTUSD(Symbol):
    """
        name: tTESTDOGE:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTDOGE:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
    min_margin: float = 15.0
    initial_margin: float = 30.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
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


TESTDOGE_TESTUSD = TESTDOGE_TESTUSD(*TESTDOGE_TESTUSD._fields)


class TESTDOGEF0_TESTUSDTF0(Symbol):
    """
        name: tTESTDOGEF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTDOGEF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
    min_margin: float = 0.5
    initial_margin: float = 1.0
    min_order_size: float = 0.001
    max_order_size: float = 1000000.0
    has_margin: bool = True
    exchange: str = "bitfinex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "tTESTDOGEF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTDOGEF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTDOGEF0:TESTUSDTF0"


TESTDOGEF0_TESTUSDTF0 = TESTDOGEF0_TESTUSDTF0(*TESTDOGEF0_TESTUSDTF0._fields)


class TESTDOT_TESTUSD(Symbol):
    """
        name: tTESTDOT:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTDOT:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTDOT_TESTUSD = TESTDOT_TESTUSD(*TESTDOT_TESTUSD._fields)


class TESTDOTF0_TESTUSDTF0(Symbol):
    """
        name: tTESTDOTF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTDOTF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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


TESTDOTF0_TESTUSDTF0 = TESTDOTF0_TESTUSDTF0(*TESTDOTF0_TESTUSDTF0._fields)


class TESTEOS_TESTUSD(Symbol):
    """
        name: tTESTEOS:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTEOS:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTEOS_TESTUSD = TESTEOS_TESTUSD(*TESTEOS_TESTUSD._fields)


class TESTEOSF0_TESTUSDTF0(Symbol):
    """
        name: tTESTEOSF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTEOSF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTEOSF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTEOSF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTEOSF0:TESTUSDTF0"


TESTEOSF0_TESTUSDTF0 = TESTEOSF0_TESTUSDTF0(*TESTEOSF0_TESTUSDTF0._fields)


class TESTETH_TESTUSD(Symbol):
    """
        name: tTESTETH:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTETH:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTETH_TESTUSD = TESTETH_TESTUSD(*TESTETH_TESTUSD._fields)


class TESTETHF0_TESTUSDTF0(Symbol):
    """
        name: tTESTETHF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTETHF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTETHF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTETHF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTETHF0:TESTUSDTF0"


TESTETHF0_TESTUSDTF0 = TESTETHF0_TESTUSDTF0(*TESTETHF0_TESTUSDTF0._fields)


class TESTFIL_TESTUSD(Symbol):
    """
        name: tTESTFIL:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTFIL:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTFIL_TESTUSD = TESTFIL_TESTUSD(*TESTFIL_TESTUSD._fields)


class TESTFILF0_TESTUSDTF0(Symbol):
    """
        name: tTESTFILF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTFILF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTFILF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTFILF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTFILF0:TESTUSDTF0"


TESTFILF0_TESTUSDTF0 = TESTFILF0_TESTUSDTF0(*TESTFILF0_TESTUSDTF0._fields)


class TESTLTC_TESTUSD(Symbol):
    """
        name: tTESTLTC:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTLTC:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTLTC_TESTUSD = TESTLTC_TESTUSD(*TESTLTC_TESTUSD._fields)


class TESTLTCF0_TESTUSDTF0(Symbol):
    """
        name: tTESTLTCF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTLTCF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTLTCF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTLTCF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTLTCF0:TESTUSDTF0"


TESTLTCF0_TESTUSDTF0 = TESTLTCF0_TESTUSDTF0(*TESTLTCF0_TESTUSDTF0._fields)


class TESTMATIC_TESTUSD(Symbol):
    """
        name: tTESTMATIC:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTMATIC:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTMATIC_TESTUSD = TESTMATIC_TESTUSD(*TESTMATIC_TESTUSD._fields)


class TESTMATIC_TESTUSDT(Symbol):
    """
        name: tTESTMATIC:TESTUSDT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTESTMATIC:TESTUSDT"
    significant_digits: int = 5
    tick_size: int = None
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


TESTMATIC_TESTUSDT = TESTMATIC_TESTUSDT(*TESTMATIC_TESTUSDT._fields)


class TESTMATICF0_TESTUSDTF0(Symbol):
    """
        name: tTESTMATICF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTMATICF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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


TESTMATICF0_TESTUSDTF0 = TESTMATICF0_TESTUSDTF0(*TESTMATICF0_TESTUSDTF0._fields)


class TESTNEAR_TESTUSD(Symbol):
    """
        name: tTESTNEAR:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTNEAR:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTNEAR_TESTUSD = TESTNEAR_TESTUSD(*TESTNEAR_TESTUSD._fields)


class TESTNEARF0_TESTUSDTF0(Symbol):
    """
        name: tTESTNEARF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTNEARF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTNEARF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTNEARF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTNEARF0:TESTUSDTF0"


TESTNEARF0_TESTUSDTF0 = TESTNEARF0_TESTUSDTF0(*TESTNEARF0_TESTUSDTF0._fields)


class TESTSOL_TESTUSD(Symbol):
    """
        name: tTESTSOL:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTSOL:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTSOL_TESTUSD = TESTSOL_TESTUSD(*TESTSOL_TESTUSD._fields)


class TESTSOLF0_TESTUSDTF0(Symbol):
    """
        name: tTESTSOLF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTSOLF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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


TESTSOLF0_TESTUSDTF0 = TESTSOLF0_TESTUSDTF0(*TESTSOLF0_TESTUSDTF0._fields)


class TESTXAUT_TESTUSD(Symbol):
    """
        name: tTESTXAUT:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTXAUT:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTXAUT_TESTUSD = TESTXAUT_TESTUSD(*TESTXAUT_TESTUSD._fields)


class TESTXAUTF0_TESTUSDTF0(Symbol):
    """
        name: tTESTXAUTF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTXAUTF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTXAUTF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTXAUTF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTXAUTF0:TESTUSDTF0"


TESTXAUTF0_TESTUSDTF0 = TESTXAUTF0_TESTUSDTF0(*TESTXAUTF0_TESTUSDTF0._fields)


class TESTXTZ_TESTUSD(Symbol):
    """
        name: tTESTXTZ:TESTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTXTZ:TESTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TESTXTZ_TESTUSD = TESTXTZ_TESTUSD(*TESTXTZ_TESTUSD._fields)


class TESTXTZF0_TESTUSDTF0(Symbol):
    """
        name: tTESTXTZF0:TESTUSDTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTESTXTZF0:TESTUSDTF0"
    significant_digits: int = 5
    tick_size: int = None
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
        return "tTESTXTZF0:TESTUSDTF0"

    def __str__(self):
        return "tTESTXTZF0:TESTUSDTF0"

    def __call__(self):
        return "tTESTXTZF0:TESTUSDTF0"


TESTXTZF0_TESTUSDTF0 = TESTXTZF0_TESTUSDTF0(*TESTXTZF0_TESTUSDTF0._fields)


class THETA_USD(Symbol):
    """
        name: tTHETA:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTHETA:USD"
    significant_digits: int = 5
    tick_size: int = None
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


THETA_USD = THETA_USD(*THETA_USD._fields)


class THETA_UST(Symbol):
    """
        name: tTHETA:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTHETA:UST"
    significant_digits: int = 5
    tick_size: int = None
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


THETA_UST = THETA_UST(*THETA_UST._fields)


class TLOS_USD(Symbol):
    """
        name: tTLOS:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 8.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTLOS:USD"
    significant_digits: int = 5
    tick_size: int = None
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


TLOS_USD = TLOS_USD(*TLOS_USD._fields)


class TONUSD(Symbol):
    """
        name: tTONUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTONUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TONUSD = TONUSD(*TONUSD._fields)


class TONUST(Symbol):
    """
        name: tTONUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTONUST"
    significant_digits: int = 5
    tick_size: int = None
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


TONUST = TONUST(*TONUST._fields)


class TRADE_USD(Symbol):
    """
        name: tTRADE:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 28.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRADE:USD"
    significant_digits: int = 5
    tick_size: int = None
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


TRADE_USD = TRADE_USD(*TRADE_USD._fields)


class TRADE_UST(Symbol):
    """
        name: tTRADE:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 28.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRADE:UST"
    significant_digits: int = 5
    tick_size: int = None
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


TRADE_UST = TRADE_UST(*TRADE_UST._fields)


class TREEB_USD(Symbol):
    """
        name: tTREEB:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 3000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTREEB:USD"
    significant_digits: int = 5
    tick_size: int = None
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


TREEB_USD = TREEB_USD(*TREEB_USD._fields)


class TREEB_UST(Symbol):
    """
        name: tTREEB:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 3000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTREEB:UST"
    significant_digits: int = 5
    tick_size: int = None
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


TREEB_UST = TREEB_UST(*TREEB_UST._fields)


class TRXBTC(Symbol):
    """
        name: tTRXBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 34.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRXBTC"
    significant_digits: int = 5
    tick_size: int = None
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


TRXBTC = TRXBTC(*TRXBTC._fields)


class TRXETH(Symbol):
    """
        name: tTRXETH
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 34.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRXETH"
    significant_digits: int = 5
    tick_size: int = None
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


TRXETH = TRXETH(*TRXETH._fields)


class TRXEUR(Symbol):
    """
        name: tTRXEUR
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 34.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRXEUR"
    significant_digits: int = 5
    tick_size: int = None
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


TRXEUR = TRXEUR(*TRXEUR._fields)


class TRXF0_USTF0(Symbol):
    """
        name: tTRXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 24.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTRXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


TRXF0_USTF0 = TRXF0_USTF0(*TRXF0_USTF0._fields)


class TRXUSD(Symbol):
    """
        name: tTRXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 34.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTRXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TRXUSD = TRXUSD(*TRXUSD._fields)


class TRXUST(Symbol):
    """
        name: tTRXUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 24.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tTRXUST"
    significant_digits: int = 5
    tick_size: int = None
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


TRXUST = TRXUST(*TRXUST._fields)


class TRYUST(Symbol):
    """
        name: tTRYUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTRYUST"
    significant_digits: int = 5
    tick_size: int = None
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


TRYUST = TRYUST(*TRYUST._fields)


class TSDUSD(Symbol):
    """
        name: tTSDUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTSDUSD"
    significant_digits: int = 5
    tick_size: int = None
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


TSDUSD = TSDUSD(*TSDUSD._fields)


class TSDUST(Symbol):
    """
        name: tTSDUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tTSDUST"
    significant_digits: int = 5
    tick_size: int = None
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


TSDUST = TSDUST(*TSDUST._fields)


class UDCUSD(Symbol):
    """
        name: tUDCUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUDCUSD"
    significant_digits: int = 5
    tick_size: int = None
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


UDCUSD = UDCUSD(*UDCUSD._fields)


class UDCUST(Symbol):
    """
        name: tUDCUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUDCUST"
    significant_digits: int = 5
    tick_size: int = None
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


UDCUST = UDCUST(*UDCUST._fields)


class UK100IXF0_USTF0(Symbol):
    """
        name: tUK100IXF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUK100IXF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


UK100IXF0_USTF0 = UK100IXF0_USTF0(*UK100IXF0_USTF0._fields)


class UKOILF0_USTF0(Symbol):
    """
        name: tUKOILF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUKOILF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


UKOILF0_USTF0 = UKOILF0_USTF0(*UKOILF0_USTF0._fields)


class UNIF0_USTF0(Symbol):
    """
        name: tUNIF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.4
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUNIF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


UNIF0_USTF0 = UNIF0_USTF0(*UNIF0_USTF0._fields)


class UNIUSD(Symbol):
    """
        name: tUNIUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUNIUSD"
    significant_digits: int = 5
    tick_size: int = None
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


UNIUSD = UNIUSD(*UNIUSD._fields)


class UNIUST(Symbol):
    """
        name: tUNIUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.4
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUNIUST"
    significant_digits: int = 5
    tick_size: int = None
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


UNIUST = UNIUST(*UNIUST._fields)


class UOSBTC(Symbol):
    """
        name: tUOSBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 400000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUOSBTC"
    significant_digits: int = 5
    tick_size: int = None
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


UOSBTC = UOSBTC(*UOSBTC._fields)


class UOSUSD(Symbol):
    """
        name: tUOSUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 4.0
        max_order_size: 400000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUOSUSD"
    significant_digits: int = 5
    tick_size: int = None
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


UOSUSD = UOSUSD(*UOSUSD._fields)


class UST_CNHT(Symbol):
    """
        name: tUST:CNHT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUST:CNHT"
    significant_digits: int = 5
    tick_size: int = None
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


UST_CNHT = UST_CNHT(*UST_CNHT._fields)


class UST_MXNT(Symbol):
    """
        name: tUST:MXNT
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUST:MXNT"
    significant_digits: int = 5
    tick_size: int = None
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


UST_MXNT = UST_MXNT(*UST_MXNT._fields)


class USTUSD(Symbol):
    """
        name: tUSTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 5.0
        initial_margin: 10.0
        min_order_size: 2.0
        max_order_size: 5000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tUSTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


USTUSD = USTUSD(*USTUSD._fields)


class UTKUSD(Symbol):
    """
        name: tUTKUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 300000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tUTKUSD"
    significant_digits: int = 5
    tick_size: int = None
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


UTKUSD = UTKUSD(*UTKUSD._fields)


class VELO_USD(Symbol):
    """
        name: tVELO:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 1750000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVELO:USD"
    significant_digits: int = 5
    tick_size: int = None
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


VELO_USD = VELO_USD(*VELO_USD._fields)


class VELO_UST(Symbol):
    """
        name: tVELO:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 1750000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVELO:UST"
    significant_digits: int = 5
    tick_size: int = None
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


VELO_UST = VELO_UST(*VELO_UST._fields)


class VETBTC(Symbol):
    """
        name: tVETBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVETBTC"
    significant_digits: int = 5
    tick_size: int = None
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


VETBTC = VETBTC(*VETBTC._fields)


class VETUSD(Symbol):
    """
        name: tVETUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVETUSD"
    significant_digits: int = 5
    tick_size: int = None
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


VETUSD = VETUSD(*VETUSD._fields)


class VETUST(Symbol):
    """
        name: tVETUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 66.0
        max_order_size: 5000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVETUST"
    significant_digits: int = 5
    tick_size: int = None
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


VETUST = VETUST(*VETUST._fields)


class VRAUSD(Symbol):
    """
        name: tVRAUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 286.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVRAUSD"
    significant_digits: int = 5
    tick_size: int = None
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


VRAUSD = VRAUSD(*VRAUSD._fields)


class VRAUST(Symbol):
    """
        name: tVRAUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 286.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVRAUST"
    significant_digits: int = 5
    tick_size: int = None
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


VRAUST = VRAUST(*VRAUST._fields)


class VSYUSD(Symbol):
    """
        name: tVSYUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 432.0
        max_order_size: 250000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tVSYUSD"
    significant_digits: int = 5
    tick_size: int = None
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


VSYUSD = VSYUSD(*VSYUSD._fields)


class WAVES_USD(Symbol):
    """
        name: tWAVES:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWAVES:USD"
    significant_digits: int = 5
    tick_size: int = None
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


WAVES_USD = WAVES_USD(*WAVES_USD._fields)


class WAVES_UST(Symbol):
    """
        name: tWAVES:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWAVES:UST"
    significant_digits: int = 5
    tick_size: int = None
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


WAVES_UST = WAVES_UST(*WAVES_UST._fields)


class WAVESF0_USTF0(Symbol):
    """
        name: tWAVESF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.2
        max_order_size: 50000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tWAVESF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


WAVESF0_USTF0 = WAVESF0_USTF0(*WAVESF0_USTF0._fields)


class WAXUSD(Symbol):
    """
        name: tWAXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 16.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWAXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


WAXUSD = WAXUSD(*WAXUSD._fields)


class WBTBTC(Symbol):
    """
        name: tWBTBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 10.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWBTBTC"
    significant_digits: int = 5
    tick_size: int = None
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


WBTBTC = WBTBTC(*WBTBTC._fields)


class WBTUSD(Symbol):
    """
        name: tWBTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.00006
        max_order_size: 10.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWBTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


WBTUSD = WBTUSD(*WBTUSD._fields)


class WILD_USD(Symbol):
    """
        name: tWILD:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWILD:USD"
    significant_digits: int = 5
    tick_size: int = None
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


WILD_USD = WILD_USD(*WILD_USD._fields)


class WILD_UST(Symbol):
    """
        name: tWILD:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWILD:UST"
    significant_digits: int = 5
    tick_size: int = None
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


WILD_UST = WILD_UST(*WILD_UST._fields)


class WMINIMA_USD(Symbol):
    """
        name: tWMINIMA:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 150000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWMINIMA:USD"
    significant_digits: int = 5
    tick_size: int = None
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


WMINIMA_USD = WMINIMA_USD(*WMINIMA_USD._fields)


class WMINIMA_UST(Symbol):
    """
        name: tWMINIMA:UST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 150000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWMINIMA:UST"
    significant_digits: int = 5
    tick_size: int = None
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


WMINIMA_UST = WMINIMA_UST(*WMINIMA_UST._fields)


class WNCG_USD(Symbol):
    """
        name: tWNCG:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 12.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWNCG:USD"
    significant_digits: int = 5
    tick_size: int = None
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


WNCG_USD = WNCG_USD(*WNCG_USD._fields)


class WOOUSD(Symbol):
    """
        name: tWOOUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWOOUSD"
    significant_digits: int = 5
    tick_size: int = None
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


WOOUSD = WOOUSD(*WOOUSD._fields)


class WOOUST(Symbol):
    """
        name: tWOOUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 10.0
        max_order_size: 2500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tWOOUST"
    significant_digits: int = 5
    tick_size: int = None
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


WOOUST = WOOUST(*WOOUST._fields)


class XAGF0_USTF0(Symbol):
    """
        name: tXAGF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.1
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAGF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


XAGF0_USTF0 = XAGF0_USTF0(*XAGF0_USTF0._fields)


class XAUT_BTC(Symbol):
    """
        name: tXAUT:BTC
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 400.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUT:BTC"
    significant_digits: int = 5
    tick_size: int = None
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


XAUT_BTC = XAUT_BTC(*XAUT_BTC._fields)


class XAUT_USD(Symbol):
    """
        name: tXAUT:USD
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 400.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUT:USD"
    significant_digits: int = 5
    tick_size: int = None
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


XAUT_USD = XAUT_USD(*XAUT_USD._fields)


class XAUT_UST(Symbol):
    """
        name: tXAUT:UST
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 0.002
        max_order_size: 400.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUT:UST"
    significant_digits: int = 5
    tick_size: int = None
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


XAUT_UST = XAUT_UST(*XAUT_UST._fields)


class XAUTF0_BTCF0(Symbol):
    """
        name: tXAUTF0:BTCF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 500.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUTF0:BTCF0"
    significant_digits: int = 5
    tick_size: int = None
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


XAUTF0_BTCF0 = XAUTF0_BTCF0(*XAUTF0_BTCF0._fields)


class XAUTF0_USTF0(Symbol):
    """
        name: tXAUTF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.002
        max_order_size: 400.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXAUTF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


XAUTF0_USTF0 = XAUTF0_USTF0(*XAUTF0_USTF0._fields)


class XCAD_USD(Symbol):
    """
        name: tXCAD:USD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 15000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXCAD:USD"
    significant_digits: int = 5
    tick_size: int = None
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


XCAD_USD = XCAD_USD(*XCAD_USD._fields)


class XCNUSD(Symbol):
    """
        name: tXCNUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXCNUSD"
    significant_digits: int = 5
    tick_size: int = None
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


XCNUSD = XCNUSD(*XCNUSD._fields)


class XCNUST(Symbol):
    """
        name: tXCNUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.001
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXCNUST"
    significant_digits: int = 5
    tick_size: int = None
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


XCNUST = XCNUST(*XCNUST._fields)


class XDCUSD(Symbol):
    """
        name: tXDCUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 54.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXDCUSD"
    significant_digits: int = 5
    tick_size: int = None
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


XDCUSD = XDCUSD(*XDCUSD._fields)


class XDCUST(Symbol):
    """
        name: tXDCUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 54.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXDCUST"
    significant_digits: int = 5
    tick_size: int = None
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


XDCUST = XDCUST(*XDCUST._fields)


class XLMBTC(Symbol):
    """
        name: tXLMBTC
        significant_digits: 5
        tick_size: None
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 14.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXLMBTC"
    significant_digits: int = 5
    tick_size: int = None
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


XLMBTC = XLMBTC(*XLMBTC._fields)


class XLMF0_USTF0(Symbol):
    """
        name: tXLMF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 14.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXLMF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


XLMF0_USTF0 = XLMF0_USTF0(*XLMF0_USTF0._fields)


class XLMUSD(Symbol):
    """
        name: tXLMUSD
        significant_digits: 5
        tick_size: None
        min_margin: 25.0
        initial_margin: 50.0
        min_order_size: 14.0
        max_order_size: 1000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXLMUSD"
    significant_digits: int = 5
    tick_size: int = None
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


XLMUSD = XLMUSD(*XLMUSD._fields)


class XLMUST(Symbol):
    """
        name: tXLMUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 14.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXLMUST"
    significant_digits: int = 5
    tick_size: int = None
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


XLMUST = XLMUST(*XLMUST._fields)


class XMRBTC(Symbol):
    """
        name: tXMRBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXMRBTC"
    significant_digits: int = 5
    tick_size: int = None
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


XMRBTC = XMRBTC(*XMRBTC._fields)


class XMRF0_USTF0(Symbol):
    """
        name: tXMRF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.02
        max_order_size: 10000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXMRF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


XMRF0_USTF0 = XMRF0_USTF0(*XMRF0_USTF0._fields)


class XMRUSD(Symbol):
    """
        name: tXMRUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXMRUSD"
    significant_digits: int = 5
    tick_size: int = None
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


XMRUSD = XMRUSD(*XMRUSD._fields)


class XMRUST(Symbol):
    """
        name: tXMRUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 5000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXMRUST"
    significant_digits: int = 5
    tick_size: int = None
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


XMRUST = XMRUST(*XMRUST._fields)


class XPDF0_USTF0(Symbol):
    """
        name: tXPDF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXPDF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


XPDF0_USTF0 = XPDF0_USTF0(*XPDF0_USTF0._fields)


class XPTF0_USTF0(Symbol):
    """
        name: tXPTF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.001
        max_order_size: 1000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXPTF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


XPTF0_USTF0 = XPTF0_USTF0(*XPTF0_USTF0._fields)


class XRDBTC(Symbol):
    """
        name: tXRDBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 24.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXRDBTC"
    significant_digits: int = 5
    tick_size: int = None
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


XRDBTC = XRDBTC(*XRDBTC._fields)


class XRDUSD(Symbol):
    """
        name: tXRDUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 24.0
        max_order_size: 1000000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXRDUSD"
    significant_digits: int = 5
    tick_size: int = None
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


XRDUSD = XRDUSD(*XRDUSD._fields)


class XRPBTC(Symbol):
    """
        name: tXRPBTC
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 6.0
        max_order_size: 2000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPBTC"
    significant_digits: int = 5
    tick_size: int = None
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


XRPBTC = XRPBTC(*XRPBTC._fields)


class XRPF0_BTCF0(Symbol):
    """
        name: tXRPF0:BTCF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 250000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPF0:BTCF0"
    significant_digits: int = 5
    tick_size: int = None
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


XRPF0_BTCF0 = XRPF0_BTCF0(*XRPF0_BTCF0._fields)


class XRPF0_USTF0(Symbol):
    """
        name: tXRPF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 6.0
        max_order_size: 500000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


XRPF0_USTF0 = XRPF0_USTF0(*XRPF0_USTF0._fields)


class XRPUSD(Symbol):
    """
        name: tXRPUSD
        significant_digits: 5
        tick_size: None
        min_margin: 10.0
        initial_margin: 20.0
        min_order_size: 6.0
        max_order_size: 2000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPUSD"
    significant_digits: int = 5
    tick_size: int = None
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


XRPUSD = XRPUSD(*XRPUSD._fields)


class XRPUST(Symbol):
    """
        name: tXRPUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 2000000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXRPUST"
    significant_digits: int = 5
    tick_size: int = None
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


XRPUST = XRPUST(*XRPUST._fields)


class XTZBTC(Symbol):
    """
        name: tXTZBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXTZBTC"
    significant_digits: int = 5
    tick_size: int = None
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


XTZBTC = XTZBTC(*XTZBTC._fields)


class XTZF0_USTF0(Symbol):
    """
        name: tXTZF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXTZF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


XTZF0_USTF0 = XTZF0_USTF0(*XTZF0_USTF0._fields)


class XTZUSD(Symbol):
    """
        name: tXTZUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXTZUSD"
    significant_digits: int = 5
    tick_size: int = None
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


XTZUSD = XTZUSD(*XTZUSD._fields)


class XTZUST(Symbol):
    """
        name: tXTZUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 100000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tXTZUST"
    significant_digits: int = 5
    tick_size: int = None
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


XTZUST = XTZUST(*XTZUST._fields)


class XVGUSD(Symbol):
    """
        name: tXVGUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 432.0
        max_order_size: 1500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tXVGUSD"
    significant_digits: int = 5
    tick_size: int = None
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


XVGUSD = XVGUSD(*XVGUSD._fields)


class YFIUSD(Symbol):
    """
        name: tYFIUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.0002
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tYFIUSD"
    significant_digits: int = 5
    tick_size: int = None
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


YFIUSD = YFIUSD(*YFIUSD._fields)


class YFIUST(Symbol):
    """
        name: tYFIUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.0002
        max_order_size: 100.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tYFIUST"
    significant_digits: int = 5
    tick_size: int = None
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


YFIUST = YFIUST(*YFIUST._fields)


class ZECBTC(Symbol):
    """
        name: tZECBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 20000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tZECBTC"
    significant_digits: int = 5
    tick_size: int = None
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


ZECBTC = ZECBTC(*ZECBTC._fields)


class ZECF0_USTF0(Symbol):
    """
        name: tZECF0:USTF0
        significant_digits: 5
        tick_size: None
        min_margin: 0.5
        initial_margin: 1.0
        min_order_size: 0.02
        max_order_size: 20000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tZECF0:USTF0"
    significant_digits: int = 5
    tick_size: int = None
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


ZECF0_USTF0 = ZECF0_USTF0(*ZECF0_USTF0._fields)


class ZECUSD(Symbol):
    """
        name: tZECUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 0.02
        max_order_size: 20000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tZECUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ZECUSD = ZECUSD(*ZECUSD._fields)


class ZILBTC(Symbol):
    """
        name: tZILBTC
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 40.0
        max_order_size: 1500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tZILBTC"
    significant_digits: int = 5
    tick_size: int = None
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


ZILBTC = ZILBTC(*ZILBTC._fields)


class ZILUSD(Symbol):
    """
        name: tZILUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 40.0
        max_order_size: 1500000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tZILUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ZILUSD = ZILUSD(*ZILUSD._fields)


class ZMTUSD(Symbol):
    """
        name: tZMTUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tZMTUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ZMTUSD = ZMTUSD(*ZMTUSD._fields)


class ZMTUST(Symbol):
    """
        name: tZMTUST
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 2.0
        max_order_size: 50000.0
        has_margin: False
        exchange: bitfinex
    """
    name: str = "tZMTUST"
    significant_digits: int = 5
    tick_size: int = None
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


ZMTUST = ZMTUST(*ZMTUST._fields)


class ZRXUSD(Symbol):
    """
        name: tZRXUSD
        significant_digits: 5
        tick_size: None
        min_margin: 15.0
        initial_margin: 30.0
        min_order_size: 6.0
        max_order_size: 200000.0
        has_margin: True
        exchange: bitfinex
    """
    name: str = "tZRXUSD"
    significant_digits: int = 5
    tick_size: int = None
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


ZRXUSD = ZRXUSD(*ZRXUSD._fields)


class Bitfinex:

    ONEINCH_USD: Symbol = ONEINCH_USD
    ONEINCH_UST: Symbol = ONEINCH_UST
    AAVE_USD: Symbol = AAVE_USD
    AAVE_UST: Symbol = AAVE_UST
    AAVEF0_USTF0: Symbol = AAVEF0_USTF0
    ADABTC: Symbol = ADABTC
    ADAF0_USTF0: Symbol = ADAF0_USTF0
    ADAUSD: Symbol = ADAUSD
    ADAUST: Symbol = ADAUST
    AIXUSD: Symbol = AIXUSD
    AIXUST: Symbol = AIXUST
    ALGBTC: Symbol = ALGBTC
    ALGF0_USTF0: Symbol = ALGF0_USTF0
    ALGUSD: Symbol = ALGUSD
    ALGUST: Symbol = ALGUST
    AMPBTC: Symbol = AMPBTC
    AMPF0_USTF0: Symbol = AMPF0_USTF0
    AMPUSD: Symbol = AMPUSD
    AMPUST: Symbol = AMPUST
    ANTBTC: Symbol = ANTBTC
    ANTUSD: Symbol = ANTUSD
    APEF0_USTF0: Symbol = APEF0_USTF0
    APENFT_USD: Symbol = APENFT_USD
    APENFT_UST: Symbol = APENFT_UST
    APEUSD: Symbol = APEUSD
    APEUST: Symbol = APEUST
    APTF0_USTF0: Symbol = APTF0_USTF0
    APTUSD: Symbol = APTUSD
    APTUST: Symbol = APTUST
    ARBF0_USTF0: Symbol = ARBF0_USTF0
    ARBUSD: Symbol = ARBUSD
    ARBUST: Symbol = ARBUST
    ATLAS_USD: Symbol = ATLAS_USD
    ATLAS_UST: Symbol = ATLAS_UST
    ATOBTC: Symbol = ATOBTC
    ATOETH: Symbol = ATOETH
    ATOF0_USTF0: Symbol = ATOF0_USTF0
    ATOUSD: Symbol = ATOUSD
    ATOUST: Symbol = ATOUST
    AUSTRALIA200IXF0_USTF0: Symbol = AUSTRALIA200IXF0_USTF0
    AVAX_BTC: Symbol = AVAX_BTC
    AVAX_USD: Symbol = AVAX_USD
    AVAX_UST: Symbol = AVAX_UST
    AVAXF0_BTCF0: Symbol = AVAXF0_BTCF0
    AVAXF0_USTF0: Symbol = AVAXF0_USTF0
    AXSF0_USTF0: Symbol = AXSF0_USTF0
    AXSUSD: Symbol = AXSUSD
    AXSUST: Symbol = AXSUST
    B2MUSD: Symbol = B2MUSD
    B2MUST: Symbol = B2MUST
    BALUSD: Symbol = BALUSD
    BALUST: Symbol = BALUST
    BAND_USD: Symbol = BAND_USD
    BAND_UST: Symbol = BAND_UST
    BATUSD: Symbol = BATUSD
    BATUST: Symbol = BATUST
    BCHABC_USD: Symbol = BCHABC_USD
    BCHN_USD: Symbol = BCHN_USD
    BEST_USD: Symbol = BEST_USD
    BGBUSD: Symbol = BGBUSD
    BGBUST: Symbol = BGBUST
    BLUR_USD: Symbol = BLUR_USD
    BLUR_UST: Symbol = BLUR_UST
    BMNBTC: Symbol = BMNBTC
    BMNUSD: Symbol = BMNUSD
    BNTUSD: Symbol = BNTUSD
    BOBA_USD: Symbol = BOBA_USD
    BOBA_UST: Symbol = BOBA_UST
    BOOUSD: Symbol = BOOUSD
    BOOUST: Symbol = BOOUST
    BOSON_USD: Symbol = BOSON_USD
    BOSON_UST: Symbol = BOSON_UST
    BRISE_USD: Symbol = BRISE_USD
    BRISE_UST: Symbol = BRISE_UST
    BTC_CNHT: Symbol = BTC_CNHT
    BTC_MXNT: Symbol = BTC_MXNT
    BTC_XAUT: Symbol = BTC_XAUT
    BTCDOMF0_USTF0: Symbol = BTCDOMF0_USTF0
    BTCEUR: Symbol = BTCEUR
    BTCEUT: Symbol = BTCEUT
    BTCF0_EUTF0: Symbol = BTCF0_EUTF0
    BTCF0_USTF0: Symbol = BTCF0_USTF0
    BTCGBP: Symbol = BTCGBP
    BTCJPY: Symbol = BTCJPY
    BTCMIM: Symbol = BTCMIM
    BTCTRY: Symbol = BTCTRY
    BTCUSD: Symbol = BTCUSD
    BTCUST: Symbol = BTCUST
    BTGBTC: Symbol = BTGBTC
    BTGUSD: Symbol = BTGUSD
    BTSE_USD: Symbol = BTSE_USD
    BTTUSD: Symbol = BTTUSD
    CCDBTC: Symbol = CCDBTC
    CCDUSD: Symbol = CCDUSD
    CCDUST: Symbol = CCDUST
    CHEX_USD: Symbol = CHEX_USD
    CHSB_BTC: Symbol = CHSB_BTC
    CHSB_USD: Symbol = CHSB_USD
    CHSB_UST: Symbol = CHSB_UST
    CHZUSD: Symbol = CHZUSD
    CHZUST: Symbol = CHZUST
    CLOUSD: Symbol = CLOUSD
    CNH_CNHT: Symbol = CNH_CNHT
    COMP_USD: Symbol = COMP_USD
    COMP_UST: Symbol = COMP_UST
    COMPF0_USTF0: Symbol = COMPF0_USTF0
    CONV_USD: Symbol = CONV_USD
    CONV_UST: Symbol = CONV_UST
    CRVF0_USTF0: Symbol = CRVF0_USTF0
    CRVUSD: Symbol = CRVUSD
    CRVUST: Symbol = CRVUST
    DAIBTC: Symbol = DAIBTC
    DAIUSD: Symbol = DAIUSD
    DGBUSD: Symbol = DGBUSD
    DOGE_BTC: Symbol = DOGE_BTC
    DOGE_USD: Symbol = DOGE_USD
    DOGE_UST: Symbol = DOGE_UST
    DOGEF0_USTF0: Symbol = DOGEF0_USTF0
    DORA_USD: Symbol = DORA_USD
    DORA_UST: Symbol = DORA_UST
    DOTBTC: Symbol = DOTBTC
    DOTF0_BTCF0: Symbol = DOTF0_BTCF0
    DOTF0_USTF0: Symbol = DOTF0_USTF0
    DOTUSD: Symbol = DOTUSD
    DOTUST: Symbol = DOTUST
    DSHBTC: Symbol = DSHBTC
    DSHUSD: Symbol = DSHUSD
    DUSK_BTC: Symbol = DUSK_BTC
    DUSK_USD: Symbol = DUSK_USD
    DVFUSD: Symbol = DVFUSD
    EDOUSD: Symbol = EDOUSD
    EGLD_USD: Symbol = EGLD_USD
    EGLD_UST: Symbol = EGLD_UST
    EGLDF0_USTF0: Symbol = EGLDF0_USTF0
    ENJUSD: Symbol = ENJUSD
    EOSBTC: Symbol = EOSBTC
    EOSETH: Symbol = EOSETH
    EOSEUR: Symbol = EOSEUR
    EOSF0_USTF0: Symbol = EOSF0_USTF0
    EOSUSD: Symbol = EOSUSD
    EOSUST: Symbol = EOSUST
    ETCBTC: Symbol = ETCBTC
    ETCF0_USTF0: Symbol = ETCF0_USTF0
    ETCUSD: Symbol = ETCUSD
    ETCUST: Symbol = ETCUST
    ETH2X_ETH: Symbol = ETH2X_ETH
    ETH2X_USD: Symbol = ETH2X_USD
    ETH2X_UST: Symbol = ETH2X_UST
    ETH_MXNT: Symbol = ETH_MXNT
    ETH_XAUT: Symbol = ETH_XAUT
    ETHBTC: Symbol = ETHBTC
    ETHEUR: Symbol = ETHEUR
    ETHEUT: Symbol = ETHEUT
    ETHF0_BTCF0: Symbol = ETHF0_BTCF0
    ETHF0_EUTF0: Symbol = ETHF0_EUTF0
    ETHF0_USTF0: Symbol = ETHF0_USTF0
    ETHGBP: Symbol = ETHGBP
    ETHJPY: Symbol = ETHJPY
    ETHUSD: Symbol = ETHUSD
    ETHUST: Symbol = ETHUST
    ETHW_USD: Symbol = ETHW_USD
    ETHW_UST: Symbol = ETHW_UST
    ETPUSD: Symbol = ETPUSD
    EURF0_USTF0: Symbol = EURF0_USTF0
    EUROPE50IXF0_USTF0: Symbol = EUROPE50IXF0_USTF0
    EURUST: Symbol = EURUST
    EUSUSD: Symbol = EUSUSD
    EUT_MXNT: Symbol = EUT_MXNT
    EUTEUR: Symbol = EUTEUR
    EUTUSD: Symbol = EUTUSD
    EUTUST: Symbol = EUTUST
    FBTUSD: Symbol = FBTUSD
    FBTUST: Symbol = FBTUST
    FCLUSD: Symbol = FCLUSD
    FCLUST: Symbol = FCLUST
    FETUSD: Symbol = FETUSD
    FETUST: Symbol = FETUST
    FILF0_USTF0: Symbol = FILF0_USTF0
    FILUSD: Symbol = FILUSD
    FILUST: Symbol = FILUST
    FLOKI_USD: Symbol = FLOKI_USD
    FLOKI_UST: Symbol = FLOKI_UST
    FLRUSD: Symbol = FLRUSD
    FLRUST: Symbol = FLRUST
    FORTH_USD: Symbol = FORTH_USD
    FORTH_UST: Symbol = FORTH_UST
    FRANCE40IXF0_USTF0: Symbol = FRANCE40IXF0_USTF0
    FTMF0_USTF0: Symbol = FTMF0_USTF0
    FTMUSD: Symbol = FTMUSD
    FTMUST: Symbol = FTMUST
    FUNUSD: Symbol = FUNUSD
    GALA_USD: Symbol = GALA_USD
    GALA_UST: Symbol = GALA_UST
    GALAF0_USTF0: Symbol = GALAF0_USTF0
    GBPEUT: Symbol = GBPEUT
    GBPF0_USTF0: Symbol = GBPF0_USTF0
    GBPUST: Symbol = GBPUST
    GERMANY40IXF0_USTF0: Symbol = GERMANY40IXF0_USTF0
    GNOUSD: Symbol = GNOUSD
    GNTUSD: Symbol = GNTUSD
    GPTUSD: Symbol = GPTUSD
    GPTUST: Symbol = GPTUST
    GRTUSD: Symbol = GRTUSD
    GRTUST: Symbol = GRTUST
    GTXUSD: Symbol = GTXUSD
    GTXUST: Symbol = GTXUST
    GXTUSD: Symbol = GXTUSD
    GXTUST: Symbol = GXTUST
    HECUSD: Symbol = HECUSD
    HECUST: Symbol = HECUST
    HIXUSD: Symbol = HIXUSD
    HIXUST: Symbol = HIXUST
    HMTUSD: Symbol = HMTUSD
    HMTUST: Symbol = HMTUST
    HONGKONG50IXF0_USTF0: Symbol = HONGKONG50IXF0_USTF0
    HTXUSD: Symbol = HTXUSD
    HTXUST: Symbol = HTXUST
    ICEUSD: Symbol = ICEUSD
    ICPBTC: Symbol = ICPBTC
    ICPF0_USTF0: Symbol = ICPF0_USTF0
    ICPUSD: Symbol = ICPUSD
    ICPUST: Symbol = ICPUST
    IDXUSD: Symbol = IDXUSD
    IDXUST: Symbol = IDXUST
    IOTBTC: Symbol = IOTBTC
    IOTF0_USTF0: Symbol = IOTF0_USTF0
    IOTUSD: Symbol = IOTUSD
    JAPAN225IXF0_USTF0: Symbol = JAPAN225IXF0_USTF0
    JASMY_USD: Symbol = JASMY_USD
    JASMY_UST: Symbol = JASMY_UST
    JASMYF0_USTF0: Symbol = JASMYF0_USTF0
    JPYF0_USTF0: Symbol = JPYF0_USTF0
    JPYUST: Symbol = JPYUST
    JSTBTC: Symbol = JSTBTC
    JSTUSD: Symbol = JSTUSD
    JSTUST: Symbol = JSTUST
    KANUSD: Symbol = KANUSD
    KANUST: Symbol = KANUST
    KNCBTC: Symbol = KNCBTC
    KNCF0_USTF0: Symbol = KNCF0_USTF0
    KNCUSD: Symbol = KNCUSD
    KSMUSD: Symbol = KSMUSD
    KSMUST: Symbol = KSMUST
    LDOUSD: Symbol = LDOUSD
    LDOUST: Symbol = LDOUST
    LEOBTC: Symbol = LEOBTC
    LEOETH: Symbol = LEOETH
    LEOUSD: Symbol = LEOUSD
    LEOUST: Symbol = LEOUST
    LINK_USD: Symbol = LINK_USD
    LINK_UST: Symbol = LINK_UST
    LINKF0_USTF0: Symbol = LINKF0_USTF0
    LRCUSD: Symbol = LRCUSD
    LTCBTC: Symbol = LTCBTC
    LTCF0_BTCF0: Symbol = LTCF0_BTCF0
    LTCF0_USTF0: Symbol = LTCF0_USTF0
    LTCUSD: Symbol = LTCUSD
    LTCUST: Symbol = LTCUST
    LUNA2_USD: Symbol = LUNA2_USD
    LUNA2_UST: Symbol = LUNA2_UST
    LUNA_USD: Symbol = LUNA_USD
    LUNA_UST: Symbol = LUNA_UST
    LUXO_USD: Symbol = LUXO_USD
    LYMUSD: Symbol = LYMUSD
    MATIC_BTC: Symbol = MATIC_BTC
    MATIC_USD: Symbol = MATIC_USD
    MATIC_UST: Symbol = MATIC_UST
    MATICF0_USTF0: Symbol = MATICF0_USTF0
    MIMUSD: Symbol = MIMUSD
    MIMUST: Symbol = MIMUST
    MKRF0_USTF0: Symbol = MKRF0_USTF0
    MKRUSD: Symbol = MKRUSD
    MKRUST: Symbol = MKRUST
    MLNUSD: Symbol = MLNUSD
    MNABTC: Symbol = MNABTC
    MNAUSD: Symbol = MNAUSD
    MOBUSD: Symbol = MOBUSD
    MOBUST: Symbol = MOBUST
    MXNT_USD: Symbol = MXNT_USD
    NEAR_USD: Symbol = NEAR_USD
    NEAR_UST: Symbol = NEAR_UST
    NEARF0_USTF0: Symbol = NEARF0_USTF0
    NEOBTC: Symbol = NEOBTC
    NEOF0_USTF0: Symbol = NEOF0_USTF0
    NEOUSD: Symbol = NEOUSD
    NEOUST: Symbol = NEOUST
    NEXO_BTC: Symbol = NEXO_BTC
    NEXO_USD: Symbol = NEXO_USD
    NEXO_UST: Symbol = NEXO_UST
    NOMUSD: Symbol = NOMUSD
    NOMUST: Symbol = NOMUST
    NXRA_USD: Symbol = NXRA_USD
    OCEAN_USD: Symbol = OCEAN_USD
    OCEAN_UST: Symbol = OCEAN_UST
    OGNUSD: Symbol = OGNUSD
    OGNUST: Symbol = OGNUST
    OMGBTC: Symbol = OMGBTC
    OMGETH: Symbol = OMGETH
    OMGF0_USTF0: Symbol = OMGF0_USTF0
    OMGUSD: Symbol = OMGUSD
    OMNUSD: Symbol = OMNUSD
    ONEUSD: Symbol = ONEUSD
    ONEUST: Symbol = ONEUST
    PASUSD: Symbol = PASUSD
    PAXUSD: Symbol = PAXUSD
    PAXUST: Symbol = PAXUST
    PLANETS_USD: Symbol = PLANETS_USD
    PLANETS_UST: Symbol = PLANETS_UST
    PLUUSD: Symbol = PLUUSD
    PNKUSD: Symbol = PNKUSD
    POLC_USD: Symbol = POLC_USD
    POLC_UST: Symbol = POLC_UST
    POLIS_USD: Symbol = POLIS_USD
    POLIS_UST: Symbol = POLIS_UST
    PRMX_USD: Symbol = PRMX_USD
    PRMX_UST: Symbol = PRMX_UST
    QRDO_USD: Symbol = QRDO_USD
    QRDO_UST: Symbol = QRDO_UST
    QTFBTC: Symbol = QTFBTC
    QTFUSD: Symbol = QTFUSD
    QTMUSD: Symbol = QTMUSD
    RBTUSD: Symbol = RBTUSD
    REEF_USD: Symbol = REEF_USD
    REEF_UST: Symbol = REEF_UST
    REPUSD: Symbol = REPUSD
    REQUSD: Symbol = REQUSD
    RLYUSD: Symbol = RLYUSD
    RLYUST: Symbol = RLYUST
    RRTUSD: Symbol = RRTUSD
    SAND_USD: Symbol = SAND_USD
    SAND_UST: Symbol = SAND_UST
    SANDF0_USTF0: Symbol = SANDF0_USTF0
    SENATE_USD: Symbol = SENATE_USD
    SGBUSD: Symbol = SGBUSD
    SGBUST: Symbol = SGBUST
    SHFT_USD: Symbol = SHFT_USD
    SHFT_UST: Symbol = SHFT_UST
    SHIB_USD: Symbol = SHIB_USD
    SHIB_UST: Symbol = SHIB_UST
    SHIBF0_USTF0: Symbol = SHIBF0_USTF0
    SIDUS_USD: Symbol = SIDUS_USD
    SMRUSD: Symbol = SMRUSD
    SMRUST: Symbol = SMRUST
    SNTUSD: Symbol = SNTUSD
    SNXUSD: Symbol = SNXUSD
    SNXUST: Symbol = SNXUST
    SOLBTC: Symbol = SOLBTC
    SOLF0_BTCF0: Symbol = SOLF0_BTCF0
    SOLF0_USTF0: Symbol = SOLF0_USTF0
    SOLUSD: Symbol = SOLUSD
    SOLUST: Symbol = SOLUST
    SPAIN35IXF0_USTF0: Symbol = SPAIN35IXF0_USTF0
    SPELL_USD: Symbol = SPELL_USD
    STGF0_USTF0: Symbol = STGF0_USTF0
    STGUSD: Symbol = STGUSD
    STGUST: Symbol = STGUST
    STJUSD: Symbol = STJUSD
    SUIUSD: Symbol = SUIUSD
    SUIUST: Symbol = SUIUST
    SUKU_USD: Symbol = SUKU_USD
    SUKU_UST: Symbol = SUKU_UST
    SUNUSD: Symbol = SUNUSD
    SUNUST: Symbol = SUNUST
    SUSHI_USD: Symbol = SUSHI_USD
    SUSHI_UST: Symbol = SUSHI_UST
    SUSHIF0_USTF0: Symbol = SUSHIF0_USTF0
    SWEAT_USD: Symbol = SWEAT_USD
    SWEAT_UST: Symbol = SWEAT_UST
    SXXUSD: Symbol = SXXUSD
    TERRAUST_USD: Symbol = TERRAUST_USD
    TESTADA_TESTUSD: Symbol = TESTADA_TESTUSD
    TESTADAF0_TESTUSDTF0: Symbol = TESTADAF0_TESTUSDTF0
    TESTALGO_TESTUSD: Symbol = TESTALGO_TESTUSD
    TESTALGOF0_TESTUSDTF0: Symbol = TESTALGOF0_TESTUSDTF0
    TESTAPT_TESTUSD: Symbol = TESTAPT_TESTUSD
    TESTAPTF0_TESTUSDTF0: Symbol = TESTAPTF0_TESTUSDTF0
    TESTAVAX_TESTUSD: Symbol = TESTAVAX_TESTUSD
    TESTAVAXF0_TESTUSDTF0: Symbol = TESTAVAXF0_TESTUSDTF0
    TESTBTC_TESTUSD: Symbol = TESTBTC_TESTUSD
    TESTBTC_TESTUSDT: Symbol = TESTBTC_TESTUSDT
    TESTBTCF0_TESTUSDTF0: Symbol = TESTBTCF0_TESTUSDTF0
    TESTDOGE_TESTUSD: Symbol = TESTDOGE_TESTUSD
    TESTDOGEF0_TESTUSDTF0: Symbol = TESTDOGEF0_TESTUSDTF0
    TESTDOT_TESTUSD: Symbol = TESTDOT_TESTUSD
    TESTDOTF0_TESTUSDTF0: Symbol = TESTDOTF0_TESTUSDTF0
    TESTEOS_TESTUSD: Symbol = TESTEOS_TESTUSD
    TESTEOSF0_TESTUSDTF0: Symbol = TESTEOSF0_TESTUSDTF0
    TESTETH_TESTUSD: Symbol = TESTETH_TESTUSD
    TESTETHF0_TESTUSDTF0: Symbol = TESTETHF0_TESTUSDTF0
    TESTFIL_TESTUSD: Symbol = TESTFIL_TESTUSD
    TESTFILF0_TESTUSDTF0: Symbol = TESTFILF0_TESTUSDTF0
    TESTLTC_TESTUSD: Symbol = TESTLTC_TESTUSD
    TESTLTCF0_TESTUSDTF0: Symbol = TESTLTCF0_TESTUSDTF0
    TESTMATIC_TESTUSD: Symbol = TESTMATIC_TESTUSD
    TESTMATIC_TESTUSDT: Symbol = TESTMATIC_TESTUSDT
    TESTMATICF0_TESTUSDTF0: Symbol = TESTMATICF0_TESTUSDTF0
    TESTNEAR_TESTUSD: Symbol = TESTNEAR_TESTUSD
    TESTNEARF0_TESTUSDTF0: Symbol = TESTNEARF0_TESTUSDTF0
    TESTSOL_TESTUSD: Symbol = TESTSOL_TESTUSD
    TESTSOLF0_TESTUSDTF0: Symbol = TESTSOLF0_TESTUSDTF0
    TESTXAUT_TESTUSD: Symbol = TESTXAUT_TESTUSD
    TESTXAUTF0_TESTUSDTF0: Symbol = TESTXAUTF0_TESTUSDTF0
    TESTXTZ_TESTUSD: Symbol = TESTXTZ_TESTUSD
    TESTXTZF0_TESTUSDTF0: Symbol = TESTXTZF0_TESTUSDTF0
    THETA_USD: Symbol = THETA_USD
    THETA_UST: Symbol = THETA_UST
    TLOS_USD: Symbol = TLOS_USD
    TONUSD: Symbol = TONUSD
    TONUST: Symbol = TONUST
    TRADE_USD: Symbol = TRADE_USD
    TRADE_UST: Symbol = TRADE_UST
    TREEB_USD: Symbol = TREEB_USD
    TREEB_UST: Symbol = TREEB_UST
    TRXBTC: Symbol = TRXBTC
    TRXETH: Symbol = TRXETH
    TRXEUR: Symbol = TRXEUR
    TRXF0_USTF0: Symbol = TRXF0_USTF0
    TRXUSD: Symbol = TRXUSD
    TRXUST: Symbol = TRXUST
    TRYUST: Symbol = TRYUST
    TSDUSD: Symbol = TSDUSD
    TSDUST: Symbol = TSDUST
    UDCUSD: Symbol = UDCUSD
    UDCUST: Symbol = UDCUST
    UK100IXF0_USTF0: Symbol = UK100IXF0_USTF0
    UKOILF0_USTF0: Symbol = UKOILF0_USTF0
    UNIF0_USTF0: Symbol = UNIF0_USTF0
    UNIUSD: Symbol = UNIUSD
    UNIUST: Symbol = UNIUST
    UOSBTC: Symbol = UOSBTC
    UOSUSD: Symbol = UOSUSD
    UST_CNHT: Symbol = UST_CNHT
    UST_MXNT: Symbol = UST_MXNT
    USTUSD: Symbol = USTUSD
    UTKUSD: Symbol = UTKUSD
    VELO_USD: Symbol = VELO_USD
    VELO_UST: Symbol = VELO_UST
    VETBTC: Symbol = VETBTC
    VETUSD: Symbol = VETUSD
    VETUST: Symbol = VETUST
    VRAUSD: Symbol = VRAUSD
    VRAUST: Symbol = VRAUST
    VSYUSD: Symbol = VSYUSD
    WAVES_USD: Symbol = WAVES_USD
    WAVES_UST: Symbol = WAVES_UST
    WAVESF0_USTF0: Symbol = WAVESF0_USTF0
    WAXUSD: Symbol = WAXUSD
    WBTBTC: Symbol = WBTBTC
    WBTUSD: Symbol = WBTUSD
    WILD_USD: Symbol = WILD_USD
    WILD_UST: Symbol = WILD_UST
    WMINIMA_USD: Symbol = WMINIMA_USD
    WMINIMA_UST: Symbol = WMINIMA_UST
    WNCG_USD: Symbol = WNCG_USD
    WOOUSD: Symbol = WOOUSD
    WOOUST: Symbol = WOOUST
    XAGF0_USTF0: Symbol = XAGF0_USTF0
    XAUT_BTC: Symbol = XAUT_BTC
    XAUT_USD: Symbol = XAUT_USD
    XAUT_UST: Symbol = XAUT_UST
    XAUTF0_BTCF0: Symbol = XAUTF0_BTCF0
    XAUTF0_USTF0: Symbol = XAUTF0_USTF0
    XCAD_USD: Symbol = XCAD_USD
    XCNUSD: Symbol = XCNUSD
    XCNUST: Symbol = XCNUST
    XDCUSD: Symbol = XDCUSD
    XDCUST: Symbol = XDCUST
    XLMBTC: Symbol = XLMBTC
    XLMF0_USTF0: Symbol = XLMF0_USTF0
    XLMUSD: Symbol = XLMUSD
    XLMUST: Symbol = XLMUST
    XMRBTC: Symbol = XMRBTC
    XMRF0_USTF0: Symbol = XMRF0_USTF0
    XMRUSD: Symbol = XMRUSD
    XMRUST: Symbol = XMRUST
    XPDF0_USTF0: Symbol = XPDF0_USTF0
    XPTF0_USTF0: Symbol = XPTF0_USTF0
    XRDBTC: Symbol = XRDBTC
    XRDUSD: Symbol = XRDUSD
    XRPBTC: Symbol = XRPBTC
    XRPF0_BTCF0: Symbol = XRPF0_BTCF0
    XRPF0_USTF0: Symbol = XRPF0_USTF0
    XRPUSD: Symbol = XRPUSD
    XRPUST: Symbol = XRPUST
    XTZBTC: Symbol = XTZBTC
    XTZF0_USTF0: Symbol = XTZF0_USTF0
    XTZUSD: Symbol = XTZUSD
    XTZUST: Symbol = XTZUST
    XVGUSD: Symbol = XVGUSD
    YFIUSD: Symbol = YFIUSD
    YFIUST: Symbol = YFIUST
    ZECBTC: Symbol = ZECBTC
    ZECF0_USTF0: Symbol = ZECF0_USTF0
    ZECUSD: Symbol = ZECUSD
    ZILBTC: Symbol = ZILBTC
    ZILUSD: Symbol = ZILUSD
    ZMTUSD: Symbol = ZMTUSD
    ZMTUST: Symbol = ZMTUST
    ZRXUSD: Symbol = ZRXUSD

    def __iter__(self) -> list[Symbol]:
        return iter([ONEINCH_USD, ONEINCH_UST, AAVE_USD, AAVE_UST, AAVEF0_USTF0, ADABTC, ADAF0_USTF0, ADAUSD, ADAUST, AIXUSD, AIXUST, ALGBTC, ALGF0_USTF0, ALGUSD, ALGUST, AMPBTC, AMPF0_USTF0, AMPUSD, AMPUST, ANTBTC, ANTUSD, APEF0_USTF0, APENFT_USD, APENFT_UST, APEUSD, APEUST, APTF0_USTF0, APTUSD, APTUST, ARBF0_USTF0, ARBUSD, ARBUST, ATLAS_USD, ATLAS_UST, ATOBTC, ATOETH, ATOF0_USTF0, ATOUSD, ATOUST, AUSTRALIA200IXF0_USTF0, AVAX_BTC, AVAX_USD, AVAX_UST, AVAXF0_BTCF0, AVAXF0_USTF0, AXSF0_USTF0, AXSUSD, AXSUST, B2MUSD, B2MUST, BALUSD, BALUST, BAND_USD, BAND_UST, BATUSD, BATUST, BCHABC_USD, BCHN_USD, BEST_USD, BGBUSD, BGBUST, BLUR_USD, BLUR_UST, BMNBTC, BMNUSD, BNTUSD, BOBA_USD, BOBA_UST, BOOUSD, BOOUST, BOSON_USD, BOSON_UST, BRISE_USD, BRISE_UST, BTC_CNHT, BTC_MXNT, BTC_XAUT, BTCDOMF0_USTF0, BTCEUR, BTCEUT, BTCF0_EUTF0, BTCF0_USTF0, BTCGBP, BTCJPY, BTCMIM, BTCTRY, BTCUSD, BTCUST, BTGBTC, BTGUSD, BTSE_USD, BTTUSD, CCDBTC, CCDUSD, CCDUST, CHEX_USD, CHSB_BTC, CHSB_USD, CHSB_UST, CHZUSD, CHZUST, CLOUSD, CNH_CNHT, COMP_USD, COMP_UST, COMPF0_USTF0, CONV_USD, CONV_UST, CRVF0_USTF0, CRVUSD, CRVUST, DAIBTC, DAIUSD, DGBUSD, DOGE_BTC, DOGE_USD, DOGE_UST, DOGEF0_USTF0, DORA_USD, DORA_UST, DOTBTC, DOTF0_BTCF0, DOTF0_USTF0, DOTUSD, DOTUST, DSHBTC, DSHUSD, DUSK_BTC, DUSK_USD, DVFUSD, EDOUSD, EGLD_USD, EGLD_UST, EGLDF0_USTF0, ENJUSD, EOSBTC, EOSETH, EOSEUR, EOSF0_USTF0, EOSUSD, EOSUST, ETCBTC, ETCF0_USTF0, ETCUSD, ETCUST, ETH2X_ETH, ETH2X_USD, ETH2X_UST, ETH_MXNT, ETH_XAUT, ETHBTC, ETHEUR, ETHEUT, ETHF0_BTCF0, ETHF0_EUTF0, ETHF0_USTF0, ETHGBP, ETHJPY, ETHUSD, ETHUST, ETHW_USD, ETHW_UST, ETPUSD, EURF0_USTF0, EUROPE50IXF0_USTF0, EURUST, EUSUSD, EUT_MXNT, EUTEUR, EUTUSD, EUTUST, FBTUSD, FBTUST, FCLUSD, FCLUST, FETUSD, FETUST, FILF0_USTF0, FILUSD, FILUST, FLOKI_USD, FLOKI_UST, FLRUSD, FLRUST, FORTH_USD, FORTH_UST, FRANCE40IXF0_USTF0, FTMF0_USTF0, FTMUSD, FTMUST, FUNUSD, GALA_USD, GALA_UST, GALAF0_USTF0, GBPEUT, GBPF0_USTF0, GBPUST, GERMANY40IXF0_USTF0, GNOUSD, GNTUSD, GPTUSD, GPTUST, GRTUSD, GRTUST, GTXUSD, GTXUST, GXTUSD, GXTUST, HECUSD, HECUST, HIXUSD, HIXUST, HMTUSD, HMTUST, HONGKONG50IXF0_USTF0, HTXUSD, HTXUST, ICEUSD, ICPBTC, ICPF0_USTF0, ICPUSD, ICPUST, IDXUSD, IDXUST, IOTBTC, IOTF0_USTF0, IOTUSD, JAPAN225IXF0_USTF0, JASMY_USD, JASMY_UST, JASMYF0_USTF0, JPYF0_USTF0, JPYUST, JSTBTC, JSTUSD, JSTUST, KANUSD, KANUST, KNCBTC, KNCF0_USTF0, KNCUSD, KSMUSD, KSMUST, LDOUSD, LDOUST, LEOBTC, LEOETH, LEOUSD, LEOUST, LINK_USD, LINK_UST, LINKF0_USTF0, LRCUSD, LTCBTC, LTCF0_BTCF0, LTCF0_USTF0, LTCUSD, LTCUST, LUNA2_USD, LUNA2_UST, LUNA_USD, LUNA_UST, LUXO_USD, LYMUSD, MATIC_BTC, MATIC_USD, MATIC_UST, MATICF0_USTF0, MIMUSD, MIMUST, MKRF0_USTF0, MKRUSD, MKRUST, MLNUSD, MNABTC, MNAUSD, MOBUSD, MOBUST, MXNT_USD, NEAR_USD, NEAR_UST, NEARF0_USTF0, NEOBTC, NEOF0_USTF0, NEOUSD, NEOUST, NEXO_BTC, NEXO_USD, NEXO_UST, NOMUSD, NOMUST, NXRA_USD, OCEAN_USD, OCEAN_UST, OGNUSD, OGNUST, OMGBTC, OMGETH, OMGF0_USTF0, OMGUSD, OMNUSD, ONEUSD, ONEUST, PASUSD, PAXUSD, PAXUST, PLANETS_USD, PLANETS_UST, PLUUSD, PNKUSD, POLC_USD, POLC_UST, POLIS_USD, POLIS_UST, PRMX_USD, PRMX_UST, QRDO_USD, QRDO_UST, QTFBTC, QTFUSD, QTMUSD, RBTUSD, REEF_USD, REEF_UST, REPUSD, REQUSD, RLYUSD, RLYUST, RRTUSD, SAND_USD, SAND_UST, SANDF0_USTF0, SENATE_USD, SGBUSD, SGBUST, SHFT_USD, SHFT_UST, SHIB_USD, SHIB_UST, SHIBF0_USTF0, SIDUS_USD, SMRUSD, SMRUST, SNTUSD, SNXUSD, SNXUST, SOLBTC, SOLF0_BTCF0, SOLF0_USTF0, SOLUSD, SOLUST, SPAIN35IXF0_USTF0, SPELL_USD, STGF0_USTF0, STGUSD, STGUST, STJUSD, SUIUSD, SUIUST, SUKU_USD, SUKU_UST, SUNUSD, SUNUST, SUSHI_USD, SUSHI_UST, SUSHIF0_USTF0, SWEAT_USD, SWEAT_UST, SXXUSD, TERRAUST_USD, TESTADA_TESTUSD, TESTADAF0_TESTUSDTF0, TESTALGO_TESTUSD, TESTALGOF0_TESTUSDTF0, TESTAPT_TESTUSD, TESTAPTF0_TESTUSDTF0, TESTAVAX_TESTUSD, TESTAVAXF0_TESTUSDTF0, TESTBTC_TESTUSD, TESTBTC_TESTUSDT, TESTBTCF0_TESTUSDTF0, TESTDOGE_TESTUSD, TESTDOGEF0_TESTUSDTF0, TESTDOT_TESTUSD, TESTDOTF0_TESTUSDTF0, TESTEOS_TESTUSD, TESTEOSF0_TESTUSDTF0, TESTETH_TESTUSD, TESTETHF0_TESTUSDTF0, TESTFIL_TESTUSD, TESTFILF0_TESTUSDTF0, TESTLTC_TESTUSD, TESTLTCF0_TESTUSDTF0, TESTMATIC_TESTUSD, TESTMATIC_TESTUSDT, TESTMATICF0_TESTUSDTF0, TESTNEAR_TESTUSD, TESTNEARF0_TESTUSDTF0, TESTSOL_TESTUSD, TESTSOLF0_TESTUSDTF0, TESTXAUT_TESTUSD, TESTXAUTF0_TESTUSDTF0, TESTXTZ_TESTUSD, TESTXTZF0_TESTUSDTF0, THETA_USD, THETA_UST, TLOS_USD, TONUSD, TONUST, TRADE_USD, TRADE_UST, TREEB_USD, TREEB_UST, TRXBTC, TRXETH, TRXEUR, TRXF0_USTF0, TRXUSD, TRXUST, TRYUST, TSDUSD, TSDUST, UDCUSD, UDCUST, UK100IXF0_USTF0, UKOILF0_USTF0, UNIF0_USTF0, UNIUSD, UNIUST, UOSBTC, UOSUSD, UST_CNHT, UST_MXNT, USTUSD, UTKUSD, VELO_USD, VELO_UST, VETBTC, VETUSD, VETUST, VRAUSD, VRAUST, VSYUSD, WAVES_USD, WAVES_UST, WAVESF0_USTF0, WAXUSD, WBTBTC, WBTUSD, WILD_USD, WILD_UST, WMINIMA_USD, WMINIMA_UST, WNCG_USD, WOOUSD, WOOUST, XAGF0_USTF0, XAUT_BTC, XAUT_USD, XAUT_UST, XAUTF0_BTCF0, XAUTF0_USTF0, XCAD_USD, XCNUSD, XCNUST, XDCUSD, XDCUST, XLMBTC, XLMF0_USTF0, XLMUSD, XLMUST, XMRBTC, XMRF0_USTF0, XMRUSD, XMRUST, XPDF0_USTF0, XPTF0_USTF0, XRDBTC, XRDUSD, XRPBTC, XRPF0_BTCF0, XRPF0_USTF0, XRPUSD, XRPUST, XTZBTC, XTZF0_USTF0, XTZUSD, XTZUST, XVGUSD, YFIUSD, YFIUST, ZECBTC, ZECF0_USTF0, ZECUSD, ZILBTC, ZILUSD, ZMTUSD, ZMTUST, ZRXUSD])

bitfinex = Bitfinex()
