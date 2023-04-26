from typing import NamedTuple


class ONEINCHEUR(NamedTuple):
    """
        name: 1INCHEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "1INCHEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "1INCHEUR"

    def __str__(self):
        return "1INCHEUR"

    def __call__(self):
        return "1INCHEUR"


ONEINCHEUR = ONEINCHEUR()
"""
    name: 1INCHEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ONEINCHUSD(NamedTuple):
    """
        name: 1INCHUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "1INCHUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "1INCHUSD"

    def __str__(self):
        return "1INCHUSD"

    def __call__(self):
        return "1INCHUSD"


ONEINCHUSD = ONEINCHUSD()
"""
    name: 1INCHUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AAVEETH(NamedTuple):
    """
        name: AAVEETH
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.07
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AAVEETH"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.07
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVEETH"

    def __str__(self):
        return "AAVEETH"

    def __call__(self):
        return "AAVEETH"


AAVEETH = AAVEETH()
"""
    name: AAVEETH
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.07
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AAVEEUR(NamedTuple):
    """
        name: AAVEEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.07
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "AAVEEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.07
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVEEUR"

    def __str__(self):
        return "AAVEEUR"

    def __call__(self):
        return "AAVEEUR"


AAVEEUR = AAVEEUR()
"""
    name: AAVEEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.07
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class AAVEGBP(NamedTuple):
    """
        name: AAVEGBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.07
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AAVEGBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.07
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVEGBP"

    def __str__(self):
        return "AAVEGBP"

    def __call__(self):
        return "AAVEGBP"


AAVEGBP = AAVEGBP()
"""
    name: AAVEGBP
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.07
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AAVEUSD(NamedTuple):
    """
        name: AAVEUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.07
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "AAVEUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.07
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVEUSD"

    def __str__(self):
        return "AAVEUSD"

    def __call__(self):
        return "AAVEUSD"


AAVEUSD = AAVEUSD()
"""
    name: AAVEUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.07
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class AAVEXBT(NamedTuple):
    """
        name: AAVEXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.07
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AAVEXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.07
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVEXBT"

    def __str__(self):
        return "AAVEXBT"

    def __call__(self):
        return "AAVEXBT"


AAVEXBT = AAVEXBT()
"""
    name: AAVEXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.07
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ACAEUR(NamedTuple):
    """
        name: ACAEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ACAEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ACAEUR"

    def __str__(self):
        return "ACAEUR"

    def __call__(self):
        return "ACAEUR"


ACAEUR = ACAEUR()
"""
    name: ACAEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ACAUSD(NamedTuple):
    """
        name: ACAUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ACAUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ACAUSD"

    def __str__(self):
        return "ACAUSD"

    def __call__(self):
        return "ACAUSD"


ACAUSD = ACAUSD()
"""
    name: ACAUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ACHEUR(NamedTuple):
    """
        name: ACHEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 325
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ACHEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 325
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ACHEUR"

    def __str__(self):
        return "ACHEUR"

    def __call__(self):
        return "ACHEUR"


ACHEUR = ACHEUR()
"""
    name: ACHEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 325
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ACHUSD(NamedTuple):
    """
        name: ACHUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 325
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ACHUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 325
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ACHUSD"

    def __str__(self):
        return "ACHUSD"

    def __call__(self):
        return "ACHUSD"


ACHUSD = ACHUSD()
"""
    name: ACHUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 325
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ADAAUD(NamedTuple):
    """
        name: ADAAUD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ADAAUD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADAAUD"

    def __str__(self):
        return "ADAAUD"

    def __call__(self):
        return "ADAAUD"


ADAAUD = ADAAUD()
"""
    name: ADAAUD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ADAETH(NamedTuple):
    """
        name: ADAETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ADAETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADAETH"

    def __str__(self):
        return "ADAETH"

    def __call__(self):
        return "ADAETH"


ADAETH = ADAETH()
"""
    name: ADAETH
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ADAEUR(NamedTuple):
    """
        name: ADAEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ADAEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADAEUR"

    def __str__(self):
        return "ADAEUR"

    def __call__(self):
        return "ADAEUR"


ADAEUR = ADAEUR()
"""
    name: ADAEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ADAGBP(NamedTuple):
    """
        name: ADAGBP
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ADAGBP"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADAGBP"

    def __str__(self):
        return "ADAGBP"

    def __call__(self):
        return "ADAGBP"


ADAGBP = ADAGBP()
"""
    name: ADAGBP
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ADAUSD(NamedTuple):
    """
        name: ADAUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ADAUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADAUSD"

    def __str__(self):
        return "ADAUSD"

    def __call__(self):
        return "ADAUSD"


ADAUSD = ADAUSD()
"""
    name: ADAUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ADAUSDT(NamedTuple):
    """
        name: ADAUSDT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ADAUSDT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADAUSDT"

    def __str__(self):
        return "ADAUSDT"

    def __call__(self):
        return "ADAUSDT"


ADAUSDT = ADAUSDT()
"""
    name: ADAUSDT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ADAXBT(NamedTuple):
    """
        name: ADAXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ADAXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADAXBT"

    def __str__(self):
        return "ADAXBT"

    def __call__(self):
        return "ADAXBT"


ADAXBT = ADAXBT()
"""
    name: ADAXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ADXEUR(NamedTuple):
    """
        name: ADXEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ADXEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADXEUR"

    def __str__(self):
        return "ADXEUR"

    def __call__(self):
        return "ADXEUR"


ADXEUR = ADXEUR()
"""
    name: ADXEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ADXUSD(NamedTuple):
    """
        name: ADXUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ADXUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADXUSD"

    def __str__(self):
        return "ADXUSD"

    def __call__(self):
        return "ADXUSD"


ADXUSD = ADXUSD()
"""
    name: ADXUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AGLDEUR(NamedTuple):
    """
        name: AGLDEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 11
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AGLDEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 11
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AGLDEUR"

    def __str__(self):
        return "AGLDEUR"

    def __call__(self):
        return "AGLDEUR"


AGLDEUR = AGLDEUR()
"""
    name: AGLDEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 11
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AGLDUSD(NamedTuple):
    """
        name: AGLDUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 11
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AGLDUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 11
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AGLDUSD"

    def __str__(self):
        return "AGLDUSD"

    def __call__(self):
        return "AGLDUSD"


AGLDUSD = AGLDUSD()
"""
    name: AGLDUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 11
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AIREUR(NamedTuple):
    """
        name: AIREUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AIREUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AIREUR"

    def __str__(self):
        return "AIREUR"

    def __call__(self):
        return "AIREUR"


AIREUR = AIREUR()
"""
    name: AIREUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AIRUSD(NamedTuple):
    """
        name: AIRUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AIRUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AIRUSD"

    def __str__(self):
        return "AIRUSD"

    def __call__(self):
        return "AIRUSD"


AIRUSD = AIRUSD()
"""
    name: AIRUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AKTEUR(NamedTuple):
    """
        name: AKTEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AKTEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AKTEUR"

    def __str__(self):
        return "AKTEUR"

    def __call__(self):
        return "AKTEUR"


AKTEUR = AKTEUR()
"""
    name: AKTEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AKTUSD(NamedTuple):
    """
        name: AKTUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AKTUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AKTUSD"

    def __str__(self):
        return "AKTUSD"

    def __call__(self):
        return "AKTUSD"


AKTUSD = AKTUSD()
"""
    name: AKTUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ALCXEUR(NamedTuple):
    """
        name: ALCXEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ALCXEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALCXEUR"

    def __str__(self):
        return "ALCXEUR"

    def __call__(self):
        return "ALCXEUR"


ALCXEUR = ALCXEUR()
"""
    name: ALCXEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ALCXUSD(NamedTuple):
    """
        name: ALCXUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ALCXUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALCXUSD"

    def __str__(self):
        return "ALCXUSD"

    def __call__(self):
        return "ALCXUSD"


ALCXUSD = ALCXUSD()
"""
    name: ALCXUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ALGOETH(NamedTuple):
    """
        name: ALGOETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ALGOETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGOETH"

    def __str__(self):
        return "ALGOETH"

    def __call__(self):
        return "ALGOETH"


ALGOETH = ALGOETH()
"""
    name: ALGOETH
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ALGOEUR(NamedTuple):
    """
        name: ALGOEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ALGOEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGOEUR"

    def __str__(self):
        return "ALGOEUR"

    def __call__(self):
        return "ALGOEUR"


ALGOEUR = ALGOEUR()
"""
    name: ALGOEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ALGOGBP(NamedTuple):
    """
        name: ALGOGBP
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ALGOGBP"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGOGBP"

    def __str__(self):
        return "ALGOGBP"

    def __call__(self):
        return "ALGOGBP"


ALGOGBP = ALGOGBP()
"""
    name: ALGOGBP
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ALGOUSD(NamedTuple):
    """
        name: ALGOUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ALGOUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGOUSD"

    def __str__(self):
        return "ALGOUSD"

    def __call__(self):
        return "ALGOUSD"


ALGOUSD = ALGOUSD()
"""
    name: ALGOUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ALGOUSDT(NamedTuple):
    """
        name: ALGOUSDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ALGOUSDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGOUSDT"

    def __str__(self):
        return "ALGOUSDT"

    def __call__(self):
        return "ALGOUSDT"


ALGOUSDT = ALGOUSDT()
"""
    name: ALGOUSDT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ALGOXBT(NamedTuple):
    """
        name: ALGOXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ALGOXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGOXBT"

    def __str__(self):
        return "ALGOXBT"

    def __call__(self):
        return "ALGOXBT"


ALGOXBT = ALGOXBT()
"""
    name: ALGOXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ALICEEUR(NamedTuple):
    """
        name: ALICEEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ALICEEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALICEEUR"

    def __str__(self):
        return "ALICEEUR"

    def __call__(self):
        return "ALICEEUR"


ALICEEUR = ALICEEUR()
"""
    name: ALICEEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ALICEUSD(NamedTuple):
    """
        name: ALICEUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ALICEUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALICEUSD"

    def __str__(self):
        return "ALICEUSD"

    def __call__(self):
        return "ALICEUSD"


ALICEUSD = ALICEUSD()
"""
    name: ALICEUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ALPHAEUR(NamedTuple):
    """
        name: ALPHAEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ALPHAEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALPHAEUR"

    def __str__(self):
        return "ALPHAEUR"

    def __call__(self):
        return "ALPHAEUR"


ALPHAEUR = ALPHAEUR()
"""
    name: ALPHAEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ALPHAUSD(NamedTuple):
    """
        name: ALPHAUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ALPHAUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALPHAUSD"

    def __str__(self):
        return "ALPHAUSD"

    def __call__(self):
        return "ALPHAUSD"


ALPHAUSD = ALPHAUSD()
"""
    name: ALPHAUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ANKREUR(NamedTuple):
    """
        name: ANKREUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 200
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ANKREUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 200
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANKREUR"

    def __str__(self):
        return "ANKREUR"

    def __call__(self):
        return "ANKREUR"


ANKREUR = ANKREUR()
"""
    name: ANKREUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 200
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ANKRUSD(NamedTuple):
    """
        name: ANKRUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 200
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ANKRUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 200
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANKRUSD"

    def __str__(self):
        return "ANKRUSD"

    def __call__(self):
        return "ANKRUSD"


ANKRUSD = ANKRUSD()
"""
    name: ANKRUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 200
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ANKRXBT(NamedTuple):
    """
        name: ANKRXBT
        significant_digits: None
        tick_size: 0.000000001
        min_margin: None
        initial_margin: None
        min_order_size: 200
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ANKRXBT"
    significant_digits: int = None
    tick_size: int = 0.000000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 200
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANKRXBT"

    def __str__(self):
        return "ANKRXBT"

    def __call__(self):
        return "ANKRXBT"


ANKRXBT = ANKRXBT()
"""
    name: ANKRXBT
    significant_digits: None
    tick_size: 0.000000001
    min_margin: None
    initial_margin: None
    min_order_size: 200
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ANTETH(NamedTuple):
    """
        name: ANTETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ANTETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANTETH"

    def __str__(self):
        return "ANTETH"

    def __call__(self):
        return "ANTETH"


ANTETH = ANTETH()
"""
    name: ANTETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ANTEUR(NamedTuple):
    """
        name: ANTEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ANTEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANTEUR"

    def __str__(self):
        return "ANTEUR"

    def __call__(self):
        return "ANTEUR"


ANTEUR = ANTEUR()
"""
    name: ANTEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ANTUSD(NamedTuple):
    """
        name: ANTUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ANTUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANTUSD"

    def __str__(self):
        return "ANTUSD"

    def __call__(self):
        return "ANTUSD"


ANTUSD = ANTUSD()
"""
    name: ANTUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ANTXBT(NamedTuple):
    """
        name: ANTXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ANTXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANTXBT"

    def __str__(self):
        return "ANTXBT"

    def __call__(self):
        return "ANTXBT"


ANTXBT = ANTXBT()
"""
    name: ANTXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class APEEUR(NamedTuple):
    """
        name: APEEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "APEEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APEEUR"

    def __str__(self):
        return "APEEUR"

    def __call__(self):
        return "APEEUR"


APEEUR = APEEUR()
"""
    name: APEEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class APEUSD(NamedTuple):
    """
        name: APEUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "APEUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APEUSD"

    def __str__(self):
        return "APEUSD"

    def __call__(self):
        return "APEUSD"


APEUSD = APEUSD()
"""
    name: APEUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class APEUSDT(NamedTuple):
    """
        name: APEUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "APEUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APEUSDT"

    def __str__(self):
        return "APEUSDT"

    def __call__(self):
        return "APEUSDT"


APEUSDT = APEUSDT()
"""
    name: APEUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class API3EUR(NamedTuple):
    """
        name: API3EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "API3EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "API3EUR"

    def __str__(self):
        return "API3EUR"

    def __call__(self):
        return "API3EUR"


API3EUR = API3EUR()
"""
    name: API3EUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class API3USD(NamedTuple):
    """
        name: API3USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "API3USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "API3USD"

    def __str__(self):
        return "API3USD"

    def __call__(self):
        return "API3USD"


API3USD = API3USD()
"""
    name: API3USD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class APTEUR(NamedTuple):
    """
        name: APTEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.35
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "APTEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.35
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APTEUR"

    def __str__(self):
        return "APTEUR"

    def __call__(self):
        return "APTEUR"


APTEUR = APTEUR()
"""
    name: APTEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.35
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class APTUSD(NamedTuple):
    """
        name: APTUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.35
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "APTUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.35
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APTUSD"

    def __str__(self):
        return "APTUSD"

    def __call__(self):
        return "APTUSD"


APTUSD = APTUSD()
"""
    name: APTUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.35
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ARBEUR(NamedTuple):
    """
        name: ARBEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ARBEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARBEUR"

    def __str__(self):
        return "ARBEUR"

    def __call__(self):
        return "ARBEUR"


ARBEUR = ARBEUR()
"""
    name: ARBEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ARBUSD(NamedTuple):
    """
        name: ARBUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ARBUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARBUSD"

    def __str__(self):
        return "ARBUSD"

    def __call__(self):
        return "ARBUSD"


ARBUSD = ARBUSD()
"""
    name: ARBUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ARPAEUR(NamedTuple):
    """
        name: ARPAEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 125
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ARPAEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 125
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARPAEUR"

    def __str__(self):
        return "ARPAEUR"

    def __call__(self):
        return "ARPAEUR"


ARPAEUR = ARPAEUR()
"""
    name: ARPAEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 125
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ARPAUSD(NamedTuple):
    """
        name: ARPAUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 125
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ARPAUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 125
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARPAUSD"

    def __str__(self):
        return "ARPAUSD"

    def __call__(self):
        return "ARPAUSD"


ARPAUSD = ARPAUSD()
"""
    name: ARPAUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 125
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ASTREUR(NamedTuple):
    """
        name: ASTREUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ASTREUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ASTREUR"

    def __str__(self):
        return "ASTREUR"

    def __call__(self):
        return "ASTREUR"


ASTREUR = ASTREUR()
"""
    name: ASTREUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ASTRUSD(NamedTuple):
    """
        name: ASTRUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ASTRUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ASTRUSD"

    def __str__(self):
        return "ASTRUSD"

    def __call__(self):
        return "ASTRUSD"


ASTRUSD = ASTRUSD()
"""
    name: ASTRUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ATLASEUR(NamedTuple):
    """
        name: ATLASEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1350
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ATLASEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1350
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATLASEUR"

    def __str__(self):
        return "ATLASEUR"

    def __call__(self):
        return "ATLASEUR"


ATLASEUR = ATLASEUR()
"""
    name: ATLASEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1350
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ATLASUSD(NamedTuple):
    """
        name: ATLASUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1350
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ATLASUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1350
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATLASUSD"

    def __str__(self):
        return "ATLASUSD"

    def __call__(self):
        return "ATLASUSD"


ATLASUSD = ATLASUSD()
"""
    name: ATLASUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1350
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ATOMETH(NamedTuple):
    """
        name: ATOMETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ATOMETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOMETH"

    def __str__(self):
        return "ATOMETH"

    def __call__(self):
        return "ATOMETH"


ATOMETH = ATOMETH()
"""
    name: ATOMETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ATOMEUR(NamedTuple):
    """
        name: ATOMEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ATOMEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOMEUR"

    def __str__(self):
        return "ATOMEUR"

    def __call__(self):
        return "ATOMEUR"


ATOMEUR = ATOMEUR()
"""
    name: ATOMEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ATOMGBP(NamedTuple):
    """
        name: ATOMGBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ATOMGBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOMGBP"

    def __str__(self):
        return "ATOMGBP"

    def __call__(self):
        return "ATOMGBP"


ATOMGBP = ATOMGBP()
"""
    name: ATOMGBP
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ATOMUSD(NamedTuple):
    """
        name: ATOMUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ATOMUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOMUSD"

    def __str__(self):
        return "ATOMUSD"

    def __call__(self):
        return "ATOMUSD"


ATOMUSD = ATOMUSD()
"""
    name: ATOMUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ATOMUSDT(NamedTuple):
    """
        name: ATOMUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ATOMUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOMUSDT"

    def __str__(self):
        return "ATOMUSDT"

    def __call__(self):
        return "ATOMUSDT"


ATOMUSDT = ATOMUSDT()
"""
    name: ATOMUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ATOMXBT(NamedTuple):
    """
        name: ATOMXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ATOMXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOMXBT"

    def __str__(self):
        return "ATOMXBT"

    def __call__(self):
        return "ATOMXBT"


ATOMXBT = ATOMXBT()
"""
    name: ATOMXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class AUDIOEUR(NamedTuple):
    """
        name: AUDIOEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AUDIOEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AUDIOEUR"

    def __str__(self):
        return "AUDIOEUR"

    def __call__(self):
        return "AUDIOEUR"


AUDIOEUR = AUDIOEUR()
"""
    name: AUDIOEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AUDIOUSD(NamedTuple):
    """
        name: AUDIOUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AUDIOUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AUDIOUSD"

    def __str__(self):
        return "AUDIOUSD"

    def __call__(self):
        return "AUDIOUSD"


AUDIOUSD = AUDIOUSD()
"""
    name: AUDIOUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AUDJPY(NamedTuple):
    """
        name: AUDJPY
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AUDJPY"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AUDJPY"

    def __str__(self):
        return "AUDJPY"

    def __call__(self):
        return "AUDJPY"


AUDJPY = AUDJPY()
"""
    name: AUDJPY
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AUDUSD(NamedTuple):
    """
        name: AUDUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AUDUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AUDUSD"

    def __str__(self):
        return "AUDUSD"

    def __call__(self):
        return "AUDUSD"


AUDUSD = AUDUSD()
"""
    name: AUDUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AVAXEUR(NamedTuple):
    """
        name: AVAXEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.3
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "AVAXEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.3
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AVAXEUR"

    def __str__(self):
        return "AVAXEUR"

    def __call__(self):
        return "AVAXEUR"


AVAXEUR = AVAXEUR()
"""
    name: AVAXEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.3
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class AVAXUSD(NamedTuple):
    """
        name: AVAXUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.3
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "AVAXUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.3
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AVAXUSD"

    def __str__(self):
        return "AVAXUSD"

    def __call__(self):
        return "AVAXUSD"


AVAXUSD = AVAXUSD()
"""
    name: AVAXUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.3
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class AVAXUSDT(NamedTuple):
    """
        name: AVAXUSDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "AVAXUSDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AVAXUSDT"

    def __str__(self):
        return "AVAXUSDT"

    def __call__(self):
        return "AVAXUSDT"


AVAXUSDT = AVAXUSDT()
"""
    name: AVAXUSDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class AXSEUR(NamedTuple):
    """
        name: AXSEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.65
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "AXSEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.65
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AXSEUR"

    def __str__(self):
        return "AXSEUR"

    def __call__(self):
        return "AXSEUR"


AXSEUR = AXSEUR()
"""
    name: AXSEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.65
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class AXSUSD(NamedTuple):
    """
        name: AXSUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.65
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "AXSUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.65
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AXSUSD"

    def __str__(self):
        return "AXSUSD"

    def __call__(self):
        return "AXSUSD"


AXSUSD = AXSUSD()
"""
    name: AXSUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.65
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class BADGEREUR(NamedTuple):
    """
        name: BADGEREUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BADGEREUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BADGEREUR"

    def __str__(self):
        return "BADGEREUR"

    def __call__(self):
        return "BADGEREUR"


BADGEREUR = BADGEREUR()
"""
    name: BADGEREUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BADGERUSD(NamedTuple):
    """
        name: BADGERUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BADGERUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BADGERUSD"

    def __str__(self):
        return "BADGERUSD"

    def __call__(self):
        return "BADGERUSD"


BADGERUSD = BADGERUSD()
"""
    name: BADGERUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BALEUR(NamedTuple):
    """
        name: BALEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BALEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BALEUR"

    def __str__(self):
        return "BALEUR"

    def __call__(self):
        return "BALEUR"


BALEUR = BALEUR()
"""
    name: BALEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BALUSD(NamedTuple):
    """
        name: BALUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BALUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BALUSD"

    def __str__(self):
        return "BALUSD"

    def __call__(self):
        return "BALUSD"


BALUSD = BALUSD()
"""
    name: BALUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BALXBT(NamedTuple):
    """
        name: BALXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BALXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BALXBT"

    def __str__(self):
        return "BALXBT"

    def __call__(self):
        return "BALXBT"


BALXBT = BALXBT()
"""
    name: BALXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BANDEUR(NamedTuple):
    """
        name: BANDEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BANDEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BANDEUR"

    def __str__(self):
        return "BANDEUR"

    def __call__(self):
        return "BANDEUR"


BANDEUR = BANDEUR()
"""
    name: BANDEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BANDUSD(NamedTuple):
    """
        name: BANDUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BANDUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BANDUSD"

    def __str__(self):
        return "BANDUSD"

    def __call__(self):
        return "BANDUSD"


BANDUSD = BANDUSD()
"""
    name: BANDUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BATETH(NamedTuple):
    """
        name: BATETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BATETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BATETH"

    def __str__(self):
        return "BATETH"

    def __call__(self):
        return "BATETH"


BATETH = BATETH()
"""
    name: BATETH
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BATEUR(NamedTuple):
    """
        name: BATEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "BATEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BATEUR"

    def __str__(self):
        return "BATEUR"

    def __call__(self):
        return "BATEUR"


BATEUR = BATEUR()
"""
    name: BATEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class BATJPY(NamedTuple):
    """
        name: BATJPY
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BATJPY"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BATJPY"

    def __str__(self):
        return "BATJPY"

    def __call__(self):
        return "BATJPY"


BATJPY = BATJPY()
"""
    name: BATJPY
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BATUSD(NamedTuple):
    """
        name: BATUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "BATUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BATUSD"

    def __str__(self):
        return "BATUSD"

    def __call__(self):
        return "BATUSD"


BATUSD = BATUSD()
"""
    name: BATUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class BATXBT(NamedTuple):
    """
        name: BATXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BATXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BATXBT"

    def __str__(self):
        return "BATXBT"

    def __call__(self):
        return "BATXBT"


BATXBT = BATXBT()
"""
    name: BATXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BCHAUD(NamedTuple):
    """
        name: BCHAUD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BCHAUD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCHAUD"

    def __str__(self):
        return "BCHAUD"

    def __call__(self):
        return "BCHAUD"


BCHAUD = BCHAUD()
"""
    name: BCHAUD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BCHETH(NamedTuple):
    """
        name: BCHETH
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BCHETH"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCHETH"

    def __str__(self):
        return "BCHETH"

    def __call__(self):
        return "BCHETH"


BCHETH = BCHETH()
"""
    name: BCHETH
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BCHEUR(NamedTuple):
    """
        name: BCHEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "BCHEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCHEUR"

    def __str__(self):
        return "BCHEUR"

    def __call__(self):
        return "BCHEUR"


BCHEUR = BCHEUR()
"""
    name: BCHEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class BCHGBP(NamedTuple):
    """
        name: BCHGBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BCHGBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCHGBP"

    def __str__(self):
        return "BCHGBP"

    def __call__(self):
        return "BCHGBP"


BCHGBP = BCHGBP()
"""
    name: BCHGBP
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BCHJPY(NamedTuple):
    """
        name: BCHJPY
        significant_digits: None
        tick_size: 1
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BCHJPY"
    significant_digits: int = None
    tick_size: int = 1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCHJPY"

    def __str__(self):
        return "BCHJPY"

    def __call__(self):
        return "BCHJPY"


BCHJPY = BCHJPY()
"""
    name: BCHJPY
    significant_digits: None
    tick_size: 1
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BCHUSD(NamedTuple):
    """
        name: BCHUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "BCHUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCHUSD"

    def __str__(self):
        return "BCHUSD"

    def __call__(self):
        return "BCHUSD"


BCHUSD = BCHUSD()
"""
    name: BCHUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class BCHUSDT(NamedTuple):
    """
        name: BCHUSDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BCHUSDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCHUSDT"

    def __str__(self):
        return "BCHUSDT"

    def __call__(self):
        return "BCHUSDT"


BCHUSDT = BCHUSDT()
"""
    name: BCHUSDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BCHXBT(NamedTuple):
    """
        name: BCHXBT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "BCHXBT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCHXBT"

    def __str__(self):
        return "BCHXBT"

    def __call__(self):
        return "BCHXBT"


BCHXBT = BCHXBT()
"""
    name: BCHXBT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class BICOEUR(NamedTuple):
    """
        name: BICOEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 17.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BICOEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 17.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BICOEUR"

    def __str__(self):
        return "BICOEUR"

    def __call__(self):
        return "BICOEUR"


BICOEUR = BICOEUR()
"""
    name: BICOEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 17.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BICOUSD(NamedTuple):
    """
        name: BICOUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 17.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BICOUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 17.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BICOUSD"

    def __str__(self):
        return "BICOUSD"

    def __call__(self):
        return "BICOUSD"


BICOUSD = BICOUSD()
"""
    name: BICOUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 17.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BITEUR(NamedTuple):
    """
        name: BITEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 9
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BITEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 9
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BITEUR"

    def __str__(self):
        return "BITEUR"

    def __call__(self):
        return "BITEUR"


BITEUR = BITEUR()
"""
    name: BITEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 9
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BITUSD(NamedTuple):
    """
        name: BITUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 9
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BITUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 9
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BITUSD"

    def __str__(self):
        return "BITUSD"

    def __call__(self):
        return "BITUSD"


BITUSD = BITUSD()
"""
    name: BITUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 9
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BLUREUR(NamedTuple):
    """
        name: BLUREUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 7.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "BLUREUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BLUREUR"

    def __str__(self):
        return "BLUREUR"

    def __call__(self):
        return "BLUREUR"


BLUREUR = BLUREUR()
"""
    name: BLUREUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 7.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class BLURUSD(NamedTuple):
    """
        name: BLURUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 7.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "BLURUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BLURUSD"

    def __str__(self):
        return "BLURUSD"

    def __call__(self):
        return "BLURUSD"


BLURUSD = BLURUSD()
"""
    name: BLURUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 7.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class BLZEUR(NamedTuple):
    """
        name: BLZEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 55
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BLZEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 55
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BLZEUR"

    def __str__(self):
        return "BLZEUR"

    def __call__(self):
        return "BLZEUR"


BLZEUR = BLZEUR()
"""
    name: BLZEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 55
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BLZUSD(NamedTuple):
    """
        name: BLZUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 55
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BLZUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 55
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BLZUSD"

    def __str__(self):
        return "BLZUSD"

    def __call__(self):
        return "BLZUSD"


BLZUSD = BLZUSD()
"""
    name: BLZUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 55
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BNCEUR(NamedTuple):
    """
        name: BNCEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 12.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BNCEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNCEUR"

    def __str__(self):
        return "BNCEUR"

    def __call__(self):
        return "BNCEUR"


BNCEUR = BNCEUR()
"""
    name: BNCEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 12.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BNCUSD(NamedTuple):
    """
        name: BNCUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 12.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BNCUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNCUSD"

    def __str__(self):
        return "BNCUSD"

    def __call__(self):
        return "BNCUSD"


BNCUSD = BNCUSD()
"""
    name: BNCUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 12.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BNTEUR(NamedTuple):
    """
        name: BNTEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BNTEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNTEUR"

    def __str__(self):
        return "BNTEUR"

    def __call__(self):
        return "BNTEUR"


BNTEUR = BNTEUR()
"""
    name: BNTEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BNTUSD(NamedTuple):
    """
        name: BNTUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BNTUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNTUSD"

    def __str__(self):
        return "BNTUSD"

    def __call__(self):
        return "BNTUSD"


BNTUSD = BNTUSD()
"""
    name: BNTUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BNTXBT(NamedTuple):
    """
        name: BNTXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BNTXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNTXBT"

    def __str__(self):
        return "BNTXBT"

    def __call__(self):
        return "BNTXBT"


BNTXBT = BNTXBT()
"""
    name: BNTXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BOBAEUR(NamedTuple):
    """
        name: BOBAEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BOBAEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BOBAEUR"

    def __str__(self):
        return "BOBAEUR"

    def __call__(self):
        return "BOBAEUR"


BOBAEUR = BOBAEUR()
"""
    name: BOBAEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BOBAUSD(NamedTuple):
    """
        name: BOBAUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BOBAUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BOBAUSD"

    def __str__(self):
        return "BOBAUSD"

    def __call__(self):
        return "BOBAUSD"


BOBAUSD = BOBAUSD()
"""
    name: BOBAUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BONDEUR(NamedTuple):
    """
        name: BONDEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BONDEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BONDEUR"

    def __str__(self):
        return "BONDEUR"

    def __call__(self):
        return "BONDEUR"


BONDEUR = BONDEUR()
"""
    name: BONDEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BONDUSD(NamedTuple):
    """
        name: BONDUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BONDUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BONDUSD"

    def __str__(self):
        return "BONDUSD"

    def __call__(self):
        return "BONDUSD"


BONDUSD = BONDUSD()
"""
    name: BONDUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BSXEUR(NamedTuple):
    """
        name: BSXEUR
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 35000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BSXEUR"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BSXEUR"

    def __str__(self):
        return "BSXEUR"

    def __call__(self):
        return "BSXEUR"


BSXEUR = BSXEUR()
"""
    name: BSXEUR
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 35000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BSXUSD(NamedTuple):
    """
        name: BSXUSD
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 35000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BSXUSD"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BSXUSD"

    def __str__(self):
        return "BSXUSD"

    def __call__(self):
        return "BSXUSD"


BSXUSD = BSXUSD()
"""
    name: BSXUSD
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 35000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BTTEUR(NamedTuple):
    """
        name: BTTEUR
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 7500000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BTTEUR"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7500000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTTEUR"

    def __str__(self):
        return "BTTEUR"

    def __call__(self):
        return "BTTEUR"


BTTEUR = BTTEUR()
"""
    name: BTTEUR
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 7500000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class BTTUSD(NamedTuple):
    """
        name: BTTUSD
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 7500000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "BTTUSD"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7500000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTTUSD"

    def __str__(self):
        return "BTTUSD"

    def __call__(self):
        return "BTTUSD"


BTTUSD = BTTUSD()
"""
    name: BTTUSD
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 7500000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class C98EUR(NamedTuple):
    """
        name: C98EUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "C98EUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "C98EUR"

    def __str__(self):
        return "C98EUR"

    def __call__(self):
        return "C98EUR"


C98EUR = C98EUR()
"""
    name: C98EUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class C98USD(NamedTuple):
    """
        name: C98USD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "C98USD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "C98USD"

    def __str__(self):
        return "C98USD"

    def __call__(self):
        return "C98USD"


C98USD = C98USD()
"""
    name: C98USD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CELREUR(NamedTuple):
    """
        name: CELREUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CELREUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CELREUR"

    def __str__(self):
        return "CELREUR"

    def __call__(self):
        return "CELREUR"


CELREUR = CELREUR()
"""
    name: CELREUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CELRUSD(NamedTuple):
    """
        name: CELRUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CELRUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CELRUSD"

    def __str__(self):
        return "CELRUSD"

    def __call__(self):
        return "CELRUSD"


CELRUSD = CELRUSD()
"""
    name: CELRUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CFGEUR(NamedTuple):
    """
        name: CFGEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CFGEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CFGEUR"

    def __str__(self):
        return "CFGEUR"

    def __call__(self):
        return "CFGEUR"


CFGEUR = CFGEUR()
"""
    name: CFGEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CFGUSD(NamedTuple):
    """
        name: CFGUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CFGUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CFGUSD"

    def __str__(self):
        return "CFGUSD"

    def __call__(self):
        return "CFGUSD"


CFGUSD = CFGUSD()
"""
    name: CFGUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CHREUR(NamedTuple):
    """
        name: CHREUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 28
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CHREUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 28
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CHREUR"

    def __str__(self):
        return "CHREUR"

    def __call__(self):
        return "CHREUR"


CHREUR = CHREUR()
"""
    name: CHREUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 28
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CHRUSD(NamedTuple):
    """
        name: CHRUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 28
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CHRUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 28
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CHRUSD"

    def __str__(self):
        return "CHRUSD"

    def __call__(self):
        return "CHRUSD"


CHRUSD = CHRUSD()
"""
    name: CHRUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 28
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CHZEUR(NamedTuple):
    """
        name: CHZEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 40
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CHZEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 40
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CHZEUR"

    def __str__(self):
        return "CHZEUR"

    def __call__(self):
        return "CHZEUR"


CHZEUR = CHZEUR()
"""
    name: CHZEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 40
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CHZUSD(NamedTuple):
    """
        name: CHZUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 40
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CHZUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 40
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CHZUSD"

    def __str__(self):
        return "CHZUSD"

    def __call__(self):
        return "CHZUSD"


CHZUSD = CHZUSD()
"""
    name: CHZUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 40
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class COMPEUR(NamedTuple):
    """
        name: COMPEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.11
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "COMPEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.11
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COMPEUR"

    def __str__(self):
        return "COMPEUR"

    def __call__(self):
        return "COMPEUR"


COMPEUR = COMPEUR()
"""
    name: COMPEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.11
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class COMPUSD(NamedTuple):
    """
        name: COMPUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.11
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "COMPUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.11
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COMPUSD"

    def __str__(self):
        return "COMPUSD"

    def __call__(self):
        return "COMPUSD"


COMPUSD = COMPUSD()
"""
    name: COMPUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.11
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class COMPXBT(NamedTuple):
    """
        name: COMPXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.11
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "COMPXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.11
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COMPXBT"

    def __str__(self):
        return "COMPXBT"

    def __call__(self):
        return "COMPXBT"


COMPXBT = COMPXBT()
"""
    name: COMPXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.11
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class COTIEUR(NamedTuple):
    """
        name: COTIEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 65
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "COTIEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 65
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COTIEUR"

    def __str__(self):
        return "COTIEUR"

    def __call__(self):
        return "COTIEUR"


COTIEUR = COTIEUR()
"""
    name: COTIEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 65
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class COTIUSD(NamedTuple):
    """
        name: COTIUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 65
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "COTIUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 65
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COTIUSD"

    def __str__(self):
        return "COTIUSD"

    def __call__(self):
        return "COTIUSD"


COTIUSD = COTIUSD()
"""
    name: COTIUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 65
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CQTEUR(NamedTuple):
    """
        name: CQTEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CQTEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CQTEUR"

    def __str__(self):
        return "CQTEUR"

    def __call__(self):
        return "CQTEUR"


CQTEUR = CQTEUR()
"""
    name: CQTEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CQTUSD(NamedTuple):
    """
        name: CQTUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CQTUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CQTUSD"

    def __str__(self):
        return "CQTUSD"

    def __call__(self):
        return "CQTUSD"


CQTUSD = CQTUSD()
"""
    name: CQTUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CRVETH(NamedTuple):
    """
        name: CRVETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CRVETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRVETH"

    def __str__(self):
        return "CRVETH"

    def __call__(self):
        return "CRVETH"


CRVETH = CRVETH()
"""
    name: CRVETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CRVEUR(NamedTuple):
    """
        name: CRVEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "CRVEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRVEUR"

    def __str__(self):
        return "CRVEUR"

    def __call__(self):
        return "CRVEUR"


CRVEUR = CRVEUR()
"""
    name: CRVEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class CRVUSD(NamedTuple):
    """
        name: CRVUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "CRVUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRVUSD"

    def __str__(self):
        return "CRVUSD"

    def __call__(self):
        return "CRVUSD"


CRVUSD = CRVUSD()
"""
    name: CRVUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class CRVXBT(NamedTuple):
    """
        name: CRVXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CRVXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRVXBT"

    def __str__(self):
        return "CRVXBT"

    def __call__(self):
        return "CRVXBT"


CRVXBT = CRVXBT()
"""
    name: CRVXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CSMEUR(NamedTuple):
    """
        name: CSMEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 300
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CSMEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 300
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CSMEUR"

    def __str__(self):
        return "CSMEUR"

    def __call__(self):
        return "CSMEUR"


CSMEUR = CSMEUR()
"""
    name: CSMEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 300
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CSMUSD(NamedTuple):
    """
        name: CSMUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 300
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CSMUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 300
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CSMUSD"

    def __str__(self):
        return "CSMUSD"

    def __call__(self):
        return "CSMUSD"


CSMUSD = CSMUSD()
"""
    name: CSMUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 300
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CTSIEUR(NamedTuple):
    """
        name: CTSIEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 33
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CTSIEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 33
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CTSIEUR"

    def __str__(self):
        return "CTSIEUR"

    def __call__(self):
        return "CTSIEUR"


CTSIEUR = CTSIEUR()
"""
    name: CTSIEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 33
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CTSIUSD(NamedTuple):
    """
        name: CTSIUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 33
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CTSIUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 33
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CTSIUSD"

    def __str__(self):
        return "CTSIUSD"

    def __call__(self):
        return "CTSIUSD"


CTSIUSD = CTSIUSD()
"""
    name: CTSIUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 33
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CVCEUR(NamedTuple):
    """
        name: CVCEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CVCEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CVCEUR"

    def __str__(self):
        return "CVCEUR"

    def __call__(self):
        return "CVCEUR"


CVCEUR = CVCEUR()
"""
    name: CVCEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CVCUSD(NamedTuple):
    """
        name: CVCUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CVCUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CVCUSD"

    def __str__(self):
        return "CVCUSD"

    def __call__(self):
        return "CVCUSD"


CVCUSD = CVCUSD()
"""
    name: CVCUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CVXEUR(NamedTuple):
    """
        name: CVXEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.9
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CVXEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.9
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CVXEUR"

    def __str__(self):
        return "CVXEUR"

    def __call__(self):
        return "CVXEUR"


CVXEUR = CVXEUR()
"""
    name: CVXEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.9
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class CVXUSD(NamedTuple):
    """
        name: CVXUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.9
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "CVXUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.9
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CVXUSD"

    def __str__(self):
        return "CVXUSD"

    def __call__(self):
        return "CVXUSD"


CVXUSD = CVXUSD()
"""
    name: CVXUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.9
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class DAIEUR(NamedTuple):
    """
        name: DAIEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DAIEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DAIEUR"

    def __str__(self):
        return "DAIEUR"

    def __call__(self):
        return "DAIEUR"


DAIEUR = DAIEUR()
"""
    name: DAIEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DAIUSD(NamedTuple):
    """
        name: DAIUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DAIUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DAIUSD"

    def __str__(self):
        return "DAIUSD"

    def __call__(self):
        return "DAIUSD"


DAIUSD = DAIUSD()
"""
    name: DAIUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DAIUSDT(NamedTuple):
    """
        name: DAIUSDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DAIUSDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DAIUSDT"

    def __str__(self):
        return "DAIUSDT"

    def __call__(self):
        return "DAIUSDT"


DAIUSDT = DAIUSDT()
"""
    name: DAIUSDT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DASHEUR(NamedTuple):
    """
        name: DASHEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.075
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DASHEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.075
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DASHEUR"

    def __str__(self):
        return "DASHEUR"

    def __call__(self):
        return "DASHEUR"


DASHEUR = DASHEUR()
"""
    name: DASHEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.075
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DASHUSD(NamedTuple):
    """
        name: DASHUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.075
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DASHUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.075
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DASHUSD"

    def __str__(self):
        return "DASHUSD"

    def __call__(self):
        return "DASHUSD"


DASHUSD = DASHUSD()
"""
    name: DASHUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.075
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DASHXBT(NamedTuple):
    """
        name: DASHXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.075
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DASHXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.075
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DASHXBT"

    def __str__(self):
        return "DASHXBT"

    def __call__(self):
        return "DASHXBT"


DASHXBT = DASHXBT()
"""
    name: DASHXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.075
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DENTEUR(NamedTuple):
    """
        name: DENTEUR
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 7000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "DENTEUR"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DENTEUR"

    def __str__(self):
        return "DENTEUR"

    def __call__(self):
        return "DENTEUR"


DENTEUR = DENTEUR()
"""
    name: DENTEUR
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 7000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class DENTUSD(NamedTuple):
    """
        name: DENTUSD
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 7000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "DENTUSD"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DENTUSD"

    def __str__(self):
        return "DENTUSD"

    def __call__(self):
        return "DENTUSD"


DENTUSD = DENTUSD()
"""
    name: DENTUSD
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 7000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class DOTETH(NamedTuple):
    """
        name: DOTETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DOTETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOTETH"

    def __str__(self):
        return "DOTETH"

    def __call__(self):
        return "DOTETH"


DOTETH = DOTETH()
"""
    name: DOTETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DOTEUR(NamedTuple):
    """
        name: DOTEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DOTEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOTEUR"

    def __str__(self):
        return "DOTEUR"

    def __call__(self):
        return "DOTEUR"


DOTEUR = DOTEUR()
"""
    name: DOTEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DOTGBP(NamedTuple):
    """
        name: DOTGBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "DOTGBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOTGBP"

    def __str__(self):
        return "DOTGBP"

    def __call__(self):
        return "DOTGBP"


DOTGBP = DOTGBP()
"""
    name: DOTGBP
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class DOTJPY(NamedTuple):
    """
        name: DOTJPY
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "DOTJPY"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOTJPY"

    def __str__(self):
        return "DOTJPY"

    def __call__(self):
        return "DOTJPY"


DOTJPY = DOTJPY()
"""
    name: DOTJPY
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class DOTUSD(NamedTuple):
    """
        name: DOTUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DOTUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOTUSD"

    def __str__(self):
        return "DOTUSD"

    def __call__(self):
        return "DOTUSD"


DOTUSD = DOTUSD()
"""
    name: DOTUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DOTUSDT(NamedTuple):
    """
        name: DOTUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DOTUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOTUSDT"

    def __str__(self):
        return "DOTUSDT"

    def __call__(self):
        return "DOTUSDT"


DOTUSDT = DOTUSDT()
"""
    name: DOTUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DOTXBT(NamedTuple):
    """
        name: DOTXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "DOTXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOTXBT"

    def __str__(self):
        return "DOTXBT"

    def __call__(self):
        return "DOTXBT"


DOTXBT = DOTXBT()
"""
    name: DOTXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class DYDXEUR(NamedTuple):
    """
        name: DYDXEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "DYDXEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DYDXEUR"

    def __str__(self):
        return "DYDXEUR"

    def __call__(self):
        return "DYDXEUR"


DYDXEUR = DYDXEUR()
"""
    name: DYDXEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class DYDXUSD(NamedTuple):
    """
        name: DYDXUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "DYDXUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DYDXUSD"

    def __str__(self):
        return "DYDXUSD"

    def __call__(self):
        return "DYDXUSD"


DYDXUSD = DYDXUSD()
"""
    name: DYDXUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EGLDEUR(NamedTuple):
    """
        name: EGLDEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EGLDEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EGLDEUR"

    def __str__(self):
        return "EGLDEUR"

    def __call__(self):
        return "EGLDEUR"


EGLDEUR = EGLDEUR()
"""
    name: EGLDEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EGLDUSD(NamedTuple):
    """
        name: EGLDUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EGLDUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EGLDUSD"

    def __str__(self):
        return "EGLDUSD"

    def __call__(self):
        return "EGLDUSD"


EGLDUSD = EGLDUSD()
"""
    name: EGLDUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ENJEUR(NamedTuple):
    """
        name: ENJEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ENJEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENJEUR"

    def __str__(self):
        return "ENJEUR"

    def __call__(self):
        return "ENJEUR"


ENJEUR = ENJEUR()
"""
    name: ENJEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ENJGBP(NamedTuple):
    """
        name: ENJGBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ENJGBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENJGBP"

    def __str__(self):
        return "ENJGBP"

    def __call__(self):
        return "ENJGBP"


ENJGBP = ENJGBP()
"""
    name: ENJGBP
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ENJJPY(NamedTuple):
    """
        name: ENJJPY
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ENJJPY"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENJJPY"

    def __str__(self):
        return "ENJJPY"

    def __call__(self):
        return "ENJJPY"


ENJJPY = ENJJPY()
"""
    name: ENJJPY
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ENJUSD(NamedTuple):
    """
        name: ENJUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ENJUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENJUSD"

    def __str__(self):
        return "ENJUSD"

    def __call__(self):
        return "ENJUSD"


ENJUSD = ENJUSD()
"""
    name: ENJUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ENJXBT(NamedTuple):
    """
        name: ENJXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ENJXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENJXBT"

    def __str__(self):
        return "ENJXBT"

    def __call__(self):
        return "ENJXBT"


ENJXBT = ENJXBT()
"""
    name: ENJXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ENSEUR(NamedTuple):
    """
        name: ENSEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.4
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ENSEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.4
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENSEUR"

    def __str__(self):
        return "ENSEUR"

    def __call__(self):
        return "ENSEUR"


ENSEUR = ENSEUR()
"""
    name: ENSEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.4
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ENSUSD(NamedTuple):
    """
        name: ENSUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.4
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ENSUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.4
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENSUSD"

    def __str__(self):
        return "ENSUSD"

    def __call__(self):
        return "ENSUSD"


ENSUSD = ENSUSD()
"""
    name: ENSUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.4
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EOSETH(NamedTuple):
    """
        name: EOSETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "EOSETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EOSETH"

    def __str__(self):
        return "EOSETH"

    def __call__(self):
        return "EOSETH"


EOSETH = EOSETH()
"""
    name: EOSETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class EOSEUR(NamedTuple):
    """
        name: EOSEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "EOSEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EOSEUR"

    def __str__(self):
        return "EOSEUR"

    def __call__(self):
        return "EOSEUR"


EOSEUR = EOSEUR()
"""
    name: EOSEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class EOSUSD(NamedTuple):
    """
        name: EOSUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "EOSUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EOSUSD"

    def __str__(self):
        return "EOSUSD"

    def __call__(self):
        return "EOSUSD"


EOSUSD = EOSUSD()
"""
    name: EOSUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class EOSUSDT(NamedTuple):
    """
        name: EOSUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EOSUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EOSUSDT"

    def __str__(self):
        return "EOSUSDT"

    def __call__(self):
        return "EOSUSDT"


EOSUSDT = EOSUSDT()
"""
    name: EOSUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EOSXBT(NamedTuple):
    """
        name: EOSXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "EOSXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EOSXBT"

    def __str__(self):
        return "EOSXBT"

    def __call__(self):
        return "EOSXBT"


EOSXBT = EOSXBT()
"""
    name: EOSXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ETH2_SETH(NamedTuple):
    """
        name: ETH2.SETH
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.001
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ETH2.SETH"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH2.SETH"

    def __str__(self):
        return "ETH2.SETH"

    def __call__(self):
        return "ETH2.SETH"


ETH2_SETH = ETH2_SETH()
"""
    name: ETH2.SETH
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.001
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ETHAED(NamedTuple):
    """
        name: ETHAED
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ETHAED"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHAED"

    def __str__(self):
        return "ETHAED"

    def __call__(self):
        return "ETHAED"


ETHAED = ETHAED()
"""
    name: ETHAED
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ETHAUD(NamedTuple):
    """
        name: ETHAUD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETHAUD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHAUD"

    def __str__(self):
        return "ETHAUD"

    def __call__(self):
        return "ETHAUD"


ETHAUD = ETHAUD()
"""
    name: ETHAUD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ETHCHF(NamedTuple):
    """
        name: ETHCHF
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ETHCHF"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHCHF"

    def __str__(self):
        return "ETHCHF"

    def __call__(self):
        return "ETHCHF"


ETHCHF = ETHCHF()
"""
    name: ETHCHF
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ETHDAI(NamedTuple):
    """
        name: ETHDAI
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ETHDAI"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHDAI"

    def __str__(self):
        return "ETHDAI"

    def __call__(self):
        return "ETHDAI"


ETHDAI = ETHDAI()
"""
    name: ETHDAI
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ETHUSDC(NamedTuple):
    """
        name: ETHUSDC
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETHUSDC"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHUSDC"

    def __str__(self):
        return "ETHUSDC"

    def __call__(self):
        return "ETHUSDC"


ETHUSDC = ETHUSDC()
"""
    name: ETHUSDC
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ETHUSDT(NamedTuple):
    """
        name: ETHUSDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETHUSDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHUSDT"

    def __str__(self):
        return "ETHUSDT"

    def __call__(self):
        return "ETHUSDT"


ETHUSDT = ETHUSDT()
"""
    name: ETHUSDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ETHWETH(NamedTuple):
    """
        name: ETHWETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ETHWETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHWETH"

    def __str__(self):
        return "ETHWETH"

    def __call__(self):
        return "ETHWETH"


ETHWETH = ETHWETH()
"""
    name: ETHWETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ETHWEUR(NamedTuple):
    """
        name: ETHWEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ETHWEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHWEUR"

    def __str__(self):
        return "ETHWEUR"

    def __call__(self):
        return "ETHWEUR"


ETHWEUR = ETHWEUR()
"""
    name: ETHWEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ETHWUSD(NamedTuple):
    """
        name: ETHWUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ETHWUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHWUSD"

    def __str__(self):
        return "ETHWUSD"

    def __call__(self):
        return "ETHWUSD"


ETHWUSD = ETHWUSD()
"""
    name: ETHWUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EULEUR(NamedTuple):
    """
        name: EULEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EULEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EULEUR"

    def __str__(self):
        return "EULEUR"

    def __call__(self):
        return "EULEUR"


EULEUR = EULEUR()
"""
    name: EULEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EULUSD(NamedTuple):
    """
        name: EULUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EULUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EULUSD"

    def __str__(self):
        return "EULUSD"

    def __call__(self):
        return "EULUSD"


EULUSD = EULUSD()
"""
    name: EULUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EURAUD(NamedTuple):
    """
        name: EURAUD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EURAUD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EURAUD"

    def __str__(self):
        return "EURAUD"

    def __call__(self):
        return "EURAUD"


EURAUD = EURAUD()
"""
    name: EURAUD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EURCAD(NamedTuple):
    """
        name: EURCAD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EURCAD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EURCAD"

    def __str__(self):
        return "EURCAD"

    def __call__(self):
        return "EURCAD"


EURCAD = EURCAD()
"""
    name: EURCAD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EURCHF(NamedTuple):
    """
        name: EURCHF
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EURCHF"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EURCHF"

    def __str__(self):
        return "EURCHF"

    def __call__(self):
        return "EURCHF"


EURCHF = EURCHF()
"""
    name: EURCHF
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EURGBP(NamedTuple):
    """
        name: EURGBP
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EURGBP"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EURGBP"

    def __str__(self):
        return "EURGBP"

    def __call__(self):
        return "EURGBP"


EURGBP = EURGBP()
"""
    name: EURGBP
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EURJPY(NamedTuple):
    """
        name: EURJPY
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EURJPY"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EURJPY"

    def __str__(self):
        return "EURJPY"

    def __call__(self):
        return "EURJPY"


EURJPY = EURJPY()
"""
    name: EURJPY
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EWTEUR(NamedTuple):
    """
        name: EWTEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EWTEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EWTEUR"

    def __str__(self):
        return "EWTEUR"

    def __call__(self):
        return "EWTEUR"


EWTEUR = EWTEUR()
"""
    name: EWTEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EWTGBP(NamedTuple):
    """
        name: EWTGBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EWTGBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EWTGBP"

    def __str__(self):
        return "EWTGBP"

    def __call__(self):
        return "EWTGBP"


EWTGBP = EWTGBP()
"""
    name: EWTGBP
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EWTUSD(NamedTuple):
    """
        name: EWTUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EWTUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EWTUSD"

    def __str__(self):
        return "EWTUSD"

    def __call__(self):
        return "EWTUSD"


EWTUSD = EWTUSD()
"""
    name: EWTUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class EWTXBT(NamedTuple):
    """
        name: EWTXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EWTXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EWTXBT"

    def __str__(self):
        return "EWTXBT"

    def __call__(self):
        return "EWTXBT"


EWTXBT = EWTXBT()
"""
    name: EWTXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FARMEUR(NamedTuple):
    """
        name: FARMEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FARMEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FARMEUR"

    def __str__(self):
        return "FARMEUR"

    def __call__(self):
        return "FARMEUR"


FARMEUR = FARMEUR()
"""
    name: FARMEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FARMUSD(NamedTuple):
    """
        name: FARMUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FARMUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FARMUSD"

    def __str__(self):
        return "FARMUSD"

    def __call__(self):
        return "FARMUSD"


FARMUSD = FARMUSD()
"""
    name: FARMUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FETEUR(NamedTuple):
    """
        name: FETEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 12.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FETEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FETEUR"

    def __str__(self):
        return "FETEUR"

    def __call__(self):
        return "FETEUR"


FETEUR = FETEUR()
"""
    name: FETEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 12.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FETUSD(NamedTuple):
    """
        name: FETUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 12.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FETUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FETUSD"

    def __str__(self):
        return "FETUSD"

    def __call__(self):
        return "FETUSD"


FETUSD = FETUSD()
"""
    name: FETUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 12.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FIDAEUR(NamedTuple):
    """
        name: FIDAEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 12
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FIDAEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIDAEUR"

    def __str__(self):
        return "FIDAEUR"

    def __call__(self):
        return "FIDAEUR"


FIDAEUR = FIDAEUR()
"""
    name: FIDAEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 12
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FIDAUSD(NamedTuple):
    """
        name: FIDAUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 12
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FIDAUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIDAUSD"

    def __str__(self):
        return "FIDAUSD"

    def __call__(self):
        return "FIDAUSD"


FIDAUSD = FIDAUSD()
"""
    name: FIDAUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 12
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FILETH(NamedTuple):
    """
        name: FILETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1.25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FILETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FILETH"

    def __str__(self):
        return "FILETH"

    def __call__(self):
        return "FILETH"


FILETH = FILETH()
"""
    name: FILETH
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1.25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FILEUR(NamedTuple):
    """
        name: FILEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "FILEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FILEUR"

    def __str__(self):
        return "FILEUR"

    def __call__(self):
        return "FILEUR"


FILEUR = FILEUR()
"""
    name: FILEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class FILGBP(NamedTuple):
    """
        name: FILGBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FILGBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FILGBP"

    def __str__(self):
        return "FILGBP"

    def __call__(self):
        return "FILGBP"


FILGBP = FILGBP()
"""
    name: FILGBP
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FILUSD(NamedTuple):
    """
        name: FILUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "FILUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FILUSD"

    def __str__(self):
        return "FILUSD"

    def __call__(self):
        return "FILUSD"


FILUSD = FILUSD()
"""
    name: FILUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class FILXBT(NamedTuple):
    """
        name: FILXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 1.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "FILXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FILXBT"

    def __str__(self):
        return "FILXBT"

    def __call__(self):
        return "FILXBT"


FILXBT = FILXBT()
"""
    name: FILXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 1.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class FISEUR(NamedTuple):
    """
        name: FISEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 9
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FISEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 9
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FISEUR"

    def __str__(self):
        return "FISEUR"

    def __call__(self):
        return "FISEUR"


FISEUR = FISEUR()
"""
    name: FISEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 9
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FISUSD(NamedTuple):
    """
        name: FISUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 9
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FISUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 9
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FISUSD"

    def __str__(self):
        return "FISUSD"

    def __call__(self):
        return "FISUSD"


FISUSD = FISUSD()
"""
    name: FISUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 9
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FLOWETH(NamedTuple):
    """
        name: FLOWETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FLOWETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLOWETH"

    def __str__(self):
        return "FLOWETH"

    def __call__(self):
        return "FLOWETH"


FLOWETH = FLOWETH()
"""
    name: FLOWETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FLOWEUR(NamedTuple):
    """
        name: FLOWEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "FLOWEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLOWEUR"

    def __str__(self):
        return "FLOWEUR"

    def __call__(self):
        return "FLOWEUR"


FLOWEUR = FLOWEUR()
"""
    name: FLOWEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class FLOWGBP(NamedTuple):
    """
        name: FLOWGBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FLOWGBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLOWGBP"

    def __str__(self):
        return "FLOWGBP"

    def __call__(self):
        return "FLOWGBP"


FLOWGBP = FLOWGBP()
"""
    name: FLOWGBP
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FLOWUSD(NamedTuple):
    """
        name: FLOWUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "FLOWUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLOWUSD"

    def __str__(self):
        return "FLOWUSD"

    def __call__(self):
        return "FLOWUSD"


FLOWUSD = FLOWUSD()
"""
    name: FLOWUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class FLOWXBT(NamedTuple):
    """
        name: FLOWXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FLOWXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLOWXBT"

    def __str__(self):
        return "FLOWXBT"

    def __call__(self):
        return "FLOWXBT"


FLOWXBT = FLOWXBT()
"""
    name: FLOWXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FLREUR(NamedTuple):
    """
        name: FLREUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 125
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "FLREUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 125
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLREUR"

    def __str__(self):
        return "FLREUR"

    def __call__(self):
        return "FLREUR"


FLREUR = FLREUR()
"""
    name: FLREUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 125
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class FLRUSD(NamedTuple):
    """
        name: FLRUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 125
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "FLRUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 125
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLRUSD"

    def __str__(self):
        return "FLRUSD"

    def __call__(self):
        return "FLRUSD"


FLRUSD = FLRUSD()
"""
    name: FLRUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 125
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class FORTHEUR(NamedTuple):
    """
        name: FORTHEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FORTHEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FORTHEUR"

    def __str__(self):
        return "FORTHEUR"

    def __call__(self):
        return "FORTHEUR"


FORTHEUR = FORTHEUR()
"""
    name: FORTHEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FORTHUSD(NamedTuple):
    """
        name: FORTHUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FORTHUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FORTHUSD"

    def __str__(self):
        return "FORTHUSD"

    def __call__(self):
        return "FORTHUSD"


FORTHUSD = FORTHUSD()
"""
    name: FORTHUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FTMEUR(NamedTuple):
    """
        name: FTMEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "FTMEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FTMEUR"

    def __str__(self):
        return "FTMEUR"

    def __call__(self):
        return "FTMEUR"


FTMEUR = FTMEUR()
"""
    name: FTMEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class FTMUSD(NamedTuple):
    """
        name: FTMUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "FTMUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FTMUSD"

    def __str__(self):
        return "FTMUSD"

    def __call__(self):
        return "FTMUSD"


FTMUSD = FTMUSD()
"""
    name: FTMUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class FXSEUR(NamedTuple):
    """
        name: FXSEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FXSEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FXSEUR"

    def __str__(self):
        return "FXSEUR"

    def __call__(self):
        return "FXSEUR"


FXSEUR = FXSEUR()
"""
    name: FXSEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class FXSUSD(NamedTuple):
    """
        name: FXSUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "FXSUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FXSUSD"

    def __str__(self):
        return "FXSUSD"

    def __call__(self):
        return "FXSUSD"


FXSUSD = FXSUSD()
"""
    name: FXSUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GALAEUR(NamedTuple):
    """
        name: GALAEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 120
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GALAEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 120
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALAEUR"

    def __str__(self):
        return "GALAEUR"

    def __call__(self):
        return "GALAEUR"


GALAEUR = GALAEUR()
"""
    name: GALAEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 120
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GALAUSD(NamedTuple):
    """
        name: GALAUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 120
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GALAUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 120
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALAUSD"

    def __str__(self):
        return "GALAUSD"

    def __call__(self):
        return "GALAUSD"


GALAUSD = GALAUSD()
"""
    name: GALAUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 120
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GALEUR(NamedTuple):
    """
        name: GALEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GALEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALEUR"

    def __str__(self):
        return "GALEUR"

    def __call__(self):
        return "GALEUR"


GALEUR = GALEUR()
"""
    name: GALEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GALUSD(NamedTuple):
    """
        name: GALUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GALUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALUSD"

    def __str__(self):
        return "GALUSD"

    def __call__(self):
        return "GALUSD"


GALUSD = GALUSD()
"""
    name: GALUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GARIEUR(NamedTuple):
    """
        name: GARIEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 85
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GARIEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 85
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GARIEUR"

    def __str__(self):
        return "GARIEUR"

    def __call__(self):
        return "GARIEUR"


GARIEUR = GARIEUR()
"""
    name: GARIEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 85
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GARIUSD(NamedTuple):
    """
        name: GARIUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 85
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GARIUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 85
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GARIUSD"

    def __str__(self):
        return "GARIUSD"

    def __call__(self):
        return "GARIUSD"


GARIUSD = GARIUSD()
"""
    name: GARIUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 85
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GHSTEUR(NamedTuple):
    """
        name: GHSTEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GHSTEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GHSTEUR"

    def __str__(self):
        return "GHSTEUR"

    def __call__(self):
        return "GHSTEUR"


GHSTEUR = GHSTEUR()
"""
    name: GHSTEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GHSTUSD(NamedTuple):
    """
        name: GHSTUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GHSTUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GHSTUSD"

    def __str__(self):
        return "GHSTUSD"

    def __call__(self):
        return "GHSTUSD"


GHSTUSD = GHSTUSD()
"""
    name: GHSTUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GHSTXBT(NamedTuple):
    """
        name: GHSTXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GHSTXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GHSTXBT"

    def __str__(self):
        return "GHSTXBT"

    def __call__(self):
        return "GHSTXBT"


GHSTXBT = GHSTXBT()
"""
    name: GHSTXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GLMREUR(NamedTuple):
    """
        name: GLMREUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GLMREUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GLMREUR"

    def __str__(self):
        return "GLMREUR"

    def __call__(self):
        return "GLMREUR"


GLMREUR = GLMREUR()
"""
    name: GLMREUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GLMRUSD(NamedTuple):
    """
        name: GLMRUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GLMRUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GLMRUSD"

    def __str__(self):
        return "GLMRUSD"

    def __call__(self):
        return "GLMRUSD"


GLMRUSD = GLMRUSD()
"""
    name: GLMRUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GMTEUR(NamedTuple):
    """
        name: GMTEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 12.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GMTEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GMTEUR"

    def __str__(self):
        return "GMTEUR"

    def __call__(self):
        return "GMTEUR"


GMTEUR = GMTEUR()
"""
    name: GMTEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 12.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GMTUSD(NamedTuple):
    """
        name: GMTUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 12.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GMTUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GMTUSD"

    def __str__(self):
        return "GMTUSD"

    def __call__(self):
        return "GMTUSD"


GMTUSD = GMTUSD()
"""
    name: GMTUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 12.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GMXEUR(NamedTuple):
    """
        name: GMXEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GMXEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GMXEUR"

    def __str__(self):
        return "GMXEUR"

    def __call__(self):
        return "GMXEUR"


GMXEUR = GMXEUR()
"""
    name: GMXEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GMXUSD(NamedTuple):
    """
        name: GMXUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GMXUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GMXUSD"

    def __str__(self):
        return "GMXUSD"

    def __call__(self):
        return "GMXUSD"


GMXUSD = GMXUSD()
"""
    name: GMXUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GNOEUR(NamedTuple):
    """
        name: GNOEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GNOEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GNOEUR"

    def __str__(self):
        return "GNOEUR"

    def __call__(self):
        return "GNOEUR"


GNOEUR = GNOEUR()
"""
    name: GNOEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GNOUSD(NamedTuple):
    """
        name: GNOUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GNOUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GNOUSD"

    def __str__(self):
        return "GNOUSD"

    def __call__(self):
        return "GNOUSD"


GNOUSD = GNOUSD()
"""
    name: GNOUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GNOXBT(NamedTuple):
    """
        name: GNOXBT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GNOXBT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GNOXBT"

    def __str__(self):
        return "GNOXBT"

    def __call__(self):
        return "GNOXBT"


GNOXBT = GNOXBT()
"""
    name: GNOXBT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GRTEUR(NamedTuple):
    """
        name: GRTEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "GRTEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRTEUR"

    def __str__(self):
        return "GRTEUR"

    def __call__(self):
        return "GRTEUR"


GRTEUR = GRTEUR()
"""
    name: GRTEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class GRTGBP(NamedTuple):
    """
        name: GRTGBP
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GRTGBP"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRTGBP"

    def __str__(self):
        return "GRTGBP"

    def __call__(self):
        return "GRTGBP"


GRTGBP = GRTGBP()
"""
    name: GRTGBP
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GRTUSD(NamedTuple):
    """
        name: GRTUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "GRTUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRTUSD"

    def __str__(self):
        return "GRTUSD"

    def __call__(self):
        return "GRTUSD"


GRTUSD = GRTUSD()
"""
    name: GRTUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class GRTXBT(NamedTuple):
    """
        name: GRTXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GRTXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRTXBT"

    def __str__(self):
        return "GRTXBT"

    def __call__(self):
        return "GRTXBT"


GRTXBT = GRTXBT()
"""
    name: GRTXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GSTEUR(NamedTuple):
    """
        name: GSTEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GSTEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GSTEUR"

    def __str__(self):
        return "GSTEUR"

    def __call__(self):
        return "GSTEUR"


GSTEUR = GSTEUR()
"""
    name: GSTEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GSTUSD(NamedTuple):
    """
        name: GSTUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GSTUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GSTUSD"

    def __str__(self):
        return "GSTUSD"

    def __call__(self):
        return "GSTUSD"


GSTUSD = GSTUSD()
"""
    name: GSTUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GTCEUR(NamedTuple):
    """
        name: GTCEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GTCEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GTCEUR"

    def __str__(self):
        return "GTCEUR"

    def __call__(self):
        return "GTCEUR"


GTCEUR = GTCEUR()
"""
    name: GTCEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class GTCUSD(NamedTuple):
    """
        name: GTCUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GTCUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GTCUSD"

    def __str__(self):
        return "GTCUSD"

    def __call__(self):
        return "GTCUSD"


GTCUSD = GTCUSD()
"""
    name: GTCUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class HDXEUR(NamedTuple):
    """
        name: HDXEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 700
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "HDXEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 700
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HDXEUR"

    def __str__(self):
        return "HDXEUR"

    def __call__(self):
        return "HDXEUR"


HDXEUR = HDXEUR()
"""
    name: HDXEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 700
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class HDXUSD(NamedTuple):
    """
        name: HDXUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 700
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "HDXUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 700
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HDXUSD"

    def __str__(self):
        return "HDXUSD"

    def __call__(self):
        return "HDXUSD"


HDXUSD = HDXUSD()
"""
    name: HDXUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 700
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class HFTEUR(NamedTuple):
    """
        name: HFTEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 8.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "HFTEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HFTEUR"

    def __str__(self):
        return "HFTEUR"

    def __call__(self):
        return "HFTEUR"


HFTEUR = HFTEUR()
"""
    name: HFTEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 8.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class HFTUSD(NamedTuple):
    """
        name: HFTUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 8.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "HFTUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HFTUSD"

    def __str__(self):
        return "HFTUSD"

    def __call__(self):
        return "HFTUSD"


HFTUSD = HFTUSD()
"""
    name: HFTUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 8.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ICPEUR(NamedTuple):
    """
        name: ICPEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ICPEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICPEUR"

    def __str__(self):
        return "ICPEUR"

    def __call__(self):
        return "ICPEUR"


ICPEUR = ICPEUR()
"""
    name: ICPEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ICPUSD(NamedTuple):
    """
        name: ICPUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ICPUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICPUSD"

    def __str__(self):
        return "ICPUSD"

    def __call__(self):
        return "ICPUSD"


ICPUSD = ICPUSD()
"""
    name: ICPUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ICXETH(NamedTuple):
    """
        name: ICXETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ICXETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICXETH"

    def __str__(self):
        return "ICXETH"

    def __call__(self):
        return "ICXETH"


ICXETH = ICXETH()
"""
    name: ICXETH
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ICXEUR(NamedTuple):
    """
        name: ICXEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ICXEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICXEUR"

    def __str__(self):
        return "ICXEUR"

    def __call__(self):
        return "ICXEUR"


ICXEUR = ICXEUR()
"""
    name: ICXEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ICXUSD(NamedTuple):
    """
        name: ICXUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ICXUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICXUSD"

    def __str__(self):
        return "ICXUSD"

    def __call__(self):
        return "ICXUSD"


ICXUSD = ICXUSD()
"""
    name: ICXUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ICXXBT(NamedTuple):
    """
        name: ICXXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ICXXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICXXBT"

    def __str__(self):
        return "ICXXBT"

    def __call__(self):
        return "ICXXBT"


ICXXBT = ICXXBT()
"""
    name: ICXXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class IDEXEUR(NamedTuple):
    """
        name: IDEXEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 100
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "IDEXEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 100
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IDEXEUR"

    def __str__(self):
        return "IDEXEUR"

    def __call__(self):
        return "IDEXEUR"


IDEXEUR = IDEXEUR()
"""
    name: IDEXEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 100
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class IDEXUSD(NamedTuple):
    """
        name: IDEXUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 100
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "IDEXUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 100
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IDEXUSD"

    def __str__(self):
        return "IDEXUSD"

    def __call__(self):
        return "IDEXUSD"


IDEXUSD = IDEXUSD()
"""
    name: IDEXUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 100
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class IMXEUR(NamedTuple):
    """
        name: IMXEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "IMXEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IMXEUR"

    def __str__(self):
        return "IMXEUR"

    def __call__(self):
        return "IMXEUR"


IMXEUR = IMXEUR()
"""
    name: IMXEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class IMXUSD(NamedTuple):
    """
        name: IMXUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "IMXUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IMXUSD"

    def __str__(self):
        return "IMXUSD"

    def __call__(self):
        return "IMXUSD"


IMXUSD = IMXUSD()
"""
    name: IMXUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class INJEUR(NamedTuple):
    """
        name: INJEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "INJEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "INJEUR"

    def __str__(self):
        return "INJEUR"

    def __call__(self):
        return "INJEUR"


INJEUR = INJEUR()
"""
    name: INJEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class INJUSD(NamedTuple):
    """
        name: INJUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "INJUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "INJUSD"

    def __str__(self):
        return "INJUSD"

    def __call__(self):
        return "INJUSD"


INJUSD = INJUSD()
"""
    name: INJUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class INTREUR(NamedTuple):
    """
        name: INTREUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "INTREUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "INTREUR"

    def __str__(self):
        return "INTREUR"

    def __call__(self):
        return "INTREUR"


INTREUR = INTREUR()
"""
    name: INTREUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class INTRUSD(NamedTuple):
    """
        name: INTRUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "INTRUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "INTRUSD"

    def __str__(self):
        return "INTRUSD"

    def __call__(self):
        return "INTRUSD"


INTRUSD = INTRUSD()
"""
    name: INTRUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class JASMYEUR(NamedTuple):
    """
        name: JASMYEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 800
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "JASMYEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 800
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "JASMYEUR"

    def __str__(self):
        return "JASMYEUR"

    def __call__(self):
        return "JASMYEUR"


JASMYEUR = JASMYEUR()
"""
    name: JASMYEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 800
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class JASMYUSD(NamedTuple):
    """
        name: JASMYUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 800
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "JASMYUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 800
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "JASMYUSD"

    def __str__(self):
        return "JASMYUSD"

    def __call__(self):
        return "JASMYUSD"


JASMYUSD = JASMYUSD()
"""
    name: JASMYUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 800
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class JUNOEUR(NamedTuple):
    """
        name: JUNOEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 4
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "JUNOEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 4
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "JUNOEUR"

    def __str__(self):
        return "JUNOEUR"

    def __call__(self):
        return "JUNOEUR"


JUNOEUR = JUNOEUR()
"""
    name: JUNOEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 4
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class JUNOUSD(NamedTuple):
    """
        name: JUNOUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 4
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "JUNOUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 4
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "JUNOUSD"

    def __str__(self):
        return "JUNOUSD"

    def __call__(self):
        return "JUNOUSD"


JUNOUSD = JUNOUSD()
"""
    name: JUNOUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 4
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KAREUR(NamedTuple):
    """
        name: KAREUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KAREUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KAREUR"

    def __str__(self):
        return "KAREUR"

    def __call__(self):
        return "KAREUR"


KAREUR = KAREUR()
"""
    name: KAREUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KARUSD(NamedTuple):
    """
        name: KARUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KARUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KARUSD"

    def __str__(self):
        return "KARUSD"

    def __call__(self):
        return "KARUSD"


KARUSD = KARUSD()
"""
    name: KARUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KAVAETH(NamedTuple):
    """
        name: KAVAETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 6
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KAVAETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KAVAETH"

    def __str__(self):
        return "KAVAETH"

    def __call__(self):
        return "KAVAETH"


KAVAETH = KAVAETH()
"""
    name: KAVAETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 6
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KAVAEUR(NamedTuple):
    """
        name: KAVAEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 6
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "KAVAEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KAVAEUR"

    def __str__(self):
        return "KAVAEUR"

    def __call__(self):
        return "KAVAEUR"


KAVAEUR = KAVAEUR()
"""
    name: KAVAEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 6
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class KAVAUSD(NamedTuple):
    """
        name: KAVAUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 6
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "KAVAUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KAVAUSD"

    def __str__(self):
        return "KAVAUSD"

    def __call__(self):
        return "KAVAUSD"


KAVAUSD = KAVAUSD()
"""
    name: KAVAUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 6
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class KAVAXBT(NamedTuple):
    """
        name: KAVAXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 6
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KAVAXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KAVAXBT"

    def __str__(self):
        return "KAVAXBT"

    def __call__(self):
        return "KAVAXBT"


KAVAXBT = KAVAXBT()
"""
    name: KAVAXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 6
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KEEPEUR(NamedTuple):
    """
        name: KEEPEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "KEEPEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KEEPEUR"

    def __str__(self):
        return "KEEPEUR"

    def __call__(self):
        return "KEEPEUR"


KEEPEUR = KEEPEUR()
"""
    name: KEEPEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class KEEPUSD(NamedTuple):
    """
        name: KEEPUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "KEEPUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KEEPUSD"

    def __str__(self):
        return "KEEPUSD"

    def __call__(self):
        return "KEEPUSD"


KEEPUSD = KEEPUSD()
"""
    name: KEEPUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class KEEPXBT(NamedTuple):
    """
        name: KEEPXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KEEPXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KEEPXBT"

    def __str__(self):
        return "KEEPXBT"

    def __call__(self):
        return "KEEPXBT"


KEEPXBT = KEEPXBT()
"""
    name: KEEPXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KEYEUR(NamedTuple):
    """
        name: KEYEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KEYEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KEYEUR"

    def __str__(self):
        return "KEYEUR"

    def __call__(self):
        return "KEYEUR"


KEYEUR = KEYEUR()
"""
    name: KEYEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KEYUSD(NamedTuple):
    """
        name: KEYUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KEYUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KEYUSD"

    def __str__(self):
        return "KEYUSD"

    def __call__(self):
        return "KEYUSD"


KEYUSD = KEYUSD()
"""
    name: KEYUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KILTEUR(NamedTuple):
    """
        name: KILTEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 12
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KILTEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KILTEUR"

    def __str__(self):
        return "KILTEUR"

    def __call__(self):
        return "KILTEUR"


KILTEUR = KILTEUR()
"""
    name: KILTEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 12
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KILTUSD(NamedTuple):
    """
        name: KILTUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 12
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KILTUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KILTUSD"

    def __str__(self):
        return "KILTUSD"

    def __call__(self):
        return "KILTUSD"


KILTUSD = KILTUSD()
"""
    name: KILTUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 12
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KINEUR(NamedTuple):
    """
        name: KINEUR
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 1200000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KINEUR"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1200000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KINEUR"

    def __str__(self):
        return "KINEUR"

    def __call__(self):
        return "KINEUR"


KINEUR = KINEUR()
"""
    name: KINEUR
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 1200000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KINTEUR(NamedTuple):
    """
        name: KINTEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 6.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KINTEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KINTEUR"

    def __str__(self):
        return "KINTEUR"

    def __call__(self):
        return "KINTEUR"


KINTEUR = KINTEUR()
"""
    name: KINTEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 6.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KINTUSD(NamedTuple):
    """
        name: KINTUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 6.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KINTUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KINTUSD"

    def __str__(self):
        return "KINTUSD"

    def __call__(self):
        return "KINTUSD"


KINTUSD = KINTUSD()
"""
    name: KINTUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 6.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KINUSD(NamedTuple):
    """
        name: KINUSD
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 1200000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KINUSD"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1200000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KINUSD"

    def __str__(self):
        return "KINUSD"

    def __call__(self):
        return "KINUSD"


KINUSD = KINUSD()
"""
    name: KINUSD
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 1200000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KNCETH(NamedTuple):
    """
        name: KNCETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 7
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KNCETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KNCETH"

    def __str__(self):
        return "KNCETH"

    def __call__(self):
        return "KNCETH"


KNCETH = KNCETH()
"""
    name: KNCETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 7
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KNCEUR(NamedTuple):
    """
        name: KNCEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 7
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KNCEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KNCEUR"

    def __str__(self):
        return "KNCEUR"

    def __call__(self):
        return "KNCEUR"


KNCEUR = KNCEUR()
"""
    name: KNCEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 7
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KNCUSD(NamedTuple):
    """
        name: KNCUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 7
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KNCUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KNCUSD"

    def __str__(self):
        return "KNCUSD"

    def __call__(self):
        return "KNCUSD"


KNCUSD = KNCUSD()
"""
    name: KNCUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 7
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KNCXBT(NamedTuple):
    """
        name: KNCXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 7
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KNCXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KNCXBT"

    def __str__(self):
        return "KNCXBT"

    def __call__(self):
        return "KNCXBT"


KNCXBT = KNCXBT()
"""
    name: KNCXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 7
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KP3REUR(NamedTuple):
    """
        name: KP3REUR
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.07
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KP3REUR"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.07
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KP3REUR"

    def __str__(self):
        return "KP3REUR"

    def __call__(self):
        return "KP3REUR"


KP3REUR = KP3REUR()
"""
    name: KP3REUR
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.07
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KP3RUSD(NamedTuple):
    """
        name: KP3RUSD
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.07
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KP3RUSD"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.07
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KP3RUSD"

    def __str__(self):
        return "KP3RUSD"

    def __call__(self):
        return "KP3RUSD"


KP3RUSD = KP3RUSD()
"""
    name: KP3RUSD
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.07
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KSMDOT(NamedTuple):
    """
        name: KSMDOT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KSMDOT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSMDOT"

    def __str__(self):
        return "KSMDOT"

    def __call__(self):
        return "KSMDOT"


KSMDOT = KSMDOT()
"""
    name: KSMDOT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KSMETH(NamedTuple):
    """
        name: KSMETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KSMETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSMETH"

    def __str__(self):
        return "KSMETH"

    def __call__(self):
        return "KSMETH"


KSMETH = KSMETH()
"""
    name: KSMETH
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KSMEUR(NamedTuple):
    """
        name: KSMEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.2
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "KSMEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.2
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSMEUR"

    def __str__(self):
        return "KSMEUR"

    def __call__(self):
        return "KSMEUR"


KSMEUR = KSMEUR()
"""
    name: KSMEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.2
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class KSMGBP(NamedTuple):
    """
        name: KSMGBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KSMGBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSMGBP"

    def __str__(self):
        return "KSMGBP"

    def __call__(self):
        return "KSMGBP"


KSMGBP = KSMGBP()
"""
    name: KSMGBP
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class KSMUSD(NamedTuple):
    """
        name: KSMUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.2
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "KSMUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.2
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSMUSD"

    def __str__(self):
        return "KSMUSD"

    def __call__(self):
        return "KSMUSD"


KSMUSD = KSMUSD()
"""
    name: KSMUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.2
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class KSMXBT(NamedTuple):
    """
        name: KSMXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "KSMXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSMXBT"

    def __str__(self):
        return "KSMXBT"

    def __call__(self):
        return "KSMXBT"


KSMXBT = KSMXBT()
"""
    name: KSMXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LCXEUR(NamedTuple):
    """
        name: LCXEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 45
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LCXEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 45
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LCXEUR"

    def __str__(self):
        return "LCXEUR"

    def __call__(self):
        return "LCXEUR"


LCXEUR = LCXEUR()
"""
    name: LCXEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 45
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LCXUSD(NamedTuple):
    """
        name: LCXUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 45
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LCXUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 45
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LCXUSD"

    def __str__(self):
        return "LCXUSD"

    def __call__(self):
        return "LCXUSD"


LCXUSD = LCXUSD()
"""
    name: LCXUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 45
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LDOEUR(NamedTuple):
    """
        name: LDOEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LDOEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LDOEUR"

    def __str__(self):
        return "LDOEUR"

    def __call__(self):
        return "LDOEUR"


LDOEUR = LDOEUR()
"""
    name: LDOEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class LDOUSD(NamedTuple):
    """
        name: LDOUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LDOUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LDOUSD"

    def __str__(self):
        return "LDOUSD"

    def __call__(self):
        return "LDOUSD"


LDOUSD = LDOUSD()
"""
    name: LDOUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class LINKAUD(NamedTuple):
    """
        name: LINKAUD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.8
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LINKAUD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.8
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINKAUD"

    def __str__(self):
        return "LINKAUD"

    def __call__(self):
        return "LINKAUD"


LINKAUD = LINKAUD()
"""
    name: LINKAUD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.8
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LINKETH(NamedTuple):
    """
        name: LINKETH
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LINKETH"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINKETH"

    def __str__(self):
        return "LINKETH"

    def __call__(self):
        return "LINKETH"


LINKETH = LINKETH()
"""
    name: LINKETH
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class LINKEUR(NamedTuple):
    """
        name: LINKEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LINKEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINKEUR"

    def __str__(self):
        return "LINKEUR"

    def __call__(self):
        return "LINKEUR"


LINKEUR = LINKEUR()
"""
    name: LINKEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class LINKGBP(NamedTuple):
    """
        name: LINKGBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.8
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LINKGBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.8
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINKGBP"

    def __str__(self):
        return "LINKGBP"

    def __call__(self):
        return "LINKGBP"


LINKGBP = LINKGBP()
"""
    name: LINKGBP
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.8
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LINKJPY(NamedTuple):
    """
        name: LINKJPY
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.8
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LINKJPY"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.8
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINKJPY"

    def __str__(self):
        return "LINKJPY"

    def __call__(self):
        return "LINKJPY"


LINKJPY = LINKJPY()
"""
    name: LINKJPY
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.8
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LINKUSD(NamedTuple):
    """
        name: LINKUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LINKUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINKUSD"

    def __str__(self):
        return "LINKUSD"

    def __call__(self):
        return "LINKUSD"


LINKUSD = LINKUSD()
"""
    name: LINKUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class LINKUSDT(NamedTuple):
    """
        name: LINKUSDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LINKUSDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINKUSDT"

    def __str__(self):
        return "LINKUSDT"

    def __call__(self):
        return "LINKUSDT"


LINKUSDT = LINKUSDT()
"""
    name: LINKUSDT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class LINKXBT(NamedTuple):
    """
        name: LINKXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LINKXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINKXBT"

    def __str__(self):
        return "LINKXBT"

    def __call__(self):
        return "LINKXBT"


LINKXBT = LINKXBT()
"""
    name: LINKXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class LPTEUR(NamedTuple):
    """
        name: LPTEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.65
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LPTEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.65
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LPTEUR"

    def __str__(self):
        return "LPTEUR"

    def __call__(self):
        return "LPTEUR"


LPTEUR = LPTEUR()
"""
    name: LPTEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.65
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LPTGBP(NamedTuple):
    """
        name: LPTGBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.65
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LPTGBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.65
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LPTGBP"

    def __str__(self):
        return "LPTGBP"

    def __call__(self):
        return "LPTGBP"


LPTGBP = LPTGBP()
"""
    name: LPTGBP
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.65
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LPTUSD(NamedTuple):
    """
        name: LPTUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.65
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LPTUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.65
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LPTUSD"

    def __str__(self):
        return "LPTUSD"

    def __call__(self):
        return "LPTUSD"


LPTUSD = LPTUSD()
"""
    name: LPTUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.65
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LPTXBT(NamedTuple):
    """
        name: LPTXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.65
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LPTXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.65
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LPTXBT"

    def __str__(self):
        return "LPTXBT"

    def __call__(self):
        return "LPTXBT"


LPTXBT = LPTXBT()
"""
    name: LPTXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.65
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LRCEUR(NamedTuple):
    """
        name: LRCEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 13
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LRCEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 13
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LRCEUR"

    def __str__(self):
        return "LRCEUR"

    def __call__(self):
        return "LRCEUR"


LRCEUR = LRCEUR()
"""
    name: LRCEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 13
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class LRCUSD(NamedTuple):
    """
        name: LRCUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 13
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LRCUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 13
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LRCUSD"

    def __str__(self):
        return "LRCUSD"

    def __call__(self):
        return "LRCUSD"


LRCUSD = LRCUSD()
"""
    name: LRCUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 13
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class LSKETH(NamedTuple):
    """
        name: LSKETH
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LSKETH"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LSKETH"

    def __str__(self):
        return "LSKETH"

    def __call__(self):
        return "LSKETH"


LSKETH = LSKETH()
"""
    name: LSKETH
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LSKEUR(NamedTuple):
    """
        name: LSKEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LSKEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LSKEUR"

    def __str__(self):
        return "LSKEUR"

    def __call__(self):
        return "LSKEUR"


LSKEUR = LSKEUR()
"""
    name: LSKEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LSKUSD(NamedTuple):
    """
        name: LSKUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LSKUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LSKUSD"

    def __str__(self):
        return "LSKUSD"

    def __call__(self):
        return "LSKUSD"


LSKUSD = LSKUSD()
"""
    name: LSKUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LSKXBT(NamedTuple):
    """
        name: LSKXBT
        significant_digits: None
        tick_size: 0.000000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LSKXBT"
    significant_digits: int = None
    tick_size: int = 0.000000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LSKXBT"

    def __str__(self):
        return "LSKXBT"

    def __call__(self):
        return "LSKXBT"


LSKXBT = LSKXBT()
"""
    name: LSKXBT
    significant_digits: None
    tick_size: 0.000000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LTCAUD(NamedTuple):
    """
        name: LTCAUD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LTCAUD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTCAUD"

    def __str__(self):
        return "LTCAUD"

    def __call__(self):
        return "LTCAUD"


LTCAUD = LTCAUD()
"""
    name: LTCAUD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LTCETH(NamedTuple):
    """
        name: LTCETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LTCETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTCETH"

    def __str__(self):
        return "LTCETH"

    def __call__(self):
        return "LTCETH"


LTCETH = LTCETH()
"""
    name: LTCETH
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LTCGBP(NamedTuple):
    """
        name: LTCGBP
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LTCGBP"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTCGBP"

    def __str__(self):
        return "LTCGBP"

    def __call__(self):
        return "LTCGBP"


LTCGBP = LTCGBP()
"""
    name: LTCGBP
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LTCUSDT(NamedTuple):
    """
        name: LTCUSDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LTCUSDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTCUSDT"

    def __str__(self):
        return "LTCUSDT"

    def __call__(self):
        return "LTCUSDT"


LTCUSDT = LTCUSDT()
"""
    name: LTCUSDT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LUNA2EUR(NamedTuple):
    """
        name: LUNA2EUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LUNA2EUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LUNA2EUR"

    def __str__(self):
        return "LUNA2EUR"

    def __call__(self):
        return "LUNA2EUR"


LUNA2EUR = LUNA2EUR()
"""
    name: LUNA2EUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LUNA2USD(NamedTuple):
    """
        name: LUNA2USD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LUNA2USD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LUNA2USD"

    def __str__(self):
        return "LUNA2USD"

    def __call__(self):
        return "LUNA2USD"


LUNA2USD = LUNA2USD()
"""
    name: LUNA2USD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LUNAEUR(NamedTuple):
    """
        name: LUNAEUR
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 30000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LUNAEUR"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LUNAEUR"

    def __str__(self):
        return "LUNAEUR"

    def __call__(self):
        return "LUNAEUR"


LUNAEUR = LUNAEUR()
"""
    name: LUNAEUR
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 30000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class LUNAUSD(NamedTuple):
    """
        name: LUNAUSD
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 30000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LUNAUSD"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LUNAUSD"

    def __str__(self):
        return "LUNAUSD"

    def __call__(self):
        return "LUNAUSD"


LUNAUSD = LUNAUSD()
"""
    name: LUNAUSD
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 30000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MANAETH(NamedTuple):
    """
        name: MANAETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 8
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MANAETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANAETH"

    def __str__(self):
        return "MANAETH"

    def __call__(self):
        return "MANAETH"


MANAETH = MANAETH()
"""
    name: MANAETH
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 8
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MANAEUR(NamedTuple):
    """
        name: MANAEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "MANAEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANAEUR"

    def __str__(self):
        return "MANAEUR"

    def __call__(self):
        return "MANAEUR"


MANAEUR = MANAEUR()
"""
    name: MANAEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class MANAUSD(NamedTuple):
    """
        name: MANAUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "MANAUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANAUSD"

    def __str__(self):
        return "MANAUSD"

    def __call__(self):
        return "MANAUSD"


MANAUSD = MANAUSD()
"""
    name: MANAUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class MANAUSDT(NamedTuple):
    """
        name: MANAUSDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 8
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MANAUSDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANAUSDT"

    def __str__(self):
        return "MANAUSDT"

    def __call__(self):
        return "MANAUSDT"


MANAUSDT = MANAUSDT()
"""
    name: MANAUSDT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 8
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MANAXBT(NamedTuple):
    """
        name: MANAXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "MANAXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANAXBT"

    def __str__(self):
        return "MANAXBT"

    def __call__(self):
        return "MANAXBT"


MANAXBT = MANAXBT()
"""
    name: MANAXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class MASKEUR(NamedTuple):
    """
        name: MASKEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MASKEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MASKEUR"

    def __str__(self):
        return "MASKEUR"

    def __call__(self):
        return "MASKEUR"


MASKEUR = MASKEUR()
"""
    name: MASKEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MASKUSD(NamedTuple):
    """
        name: MASKUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MASKUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MASKUSD"

    def __str__(self):
        return "MASKUSD"

    def __call__(self):
        return "MASKUSD"


MASKUSD = MASKUSD()
"""
    name: MASKUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MATICEUR(NamedTuple):
    """
        name: MATICEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 4
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "MATICEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 4
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATICEUR"

    def __str__(self):
        return "MATICEUR"

    def __call__(self):
        return "MATICEUR"


MATICEUR = MATICEUR()
"""
    name: MATICEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 4
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class MATICGBP(NamedTuple):
    """
        name: MATICGBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 4
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MATICGBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 4
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATICGBP"

    def __str__(self):
        return "MATICGBP"

    def __call__(self):
        return "MATICGBP"


MATICGBP = MATICGBP()
"""
    name: MATICGBP
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 4
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MATICUSD(NamedTuple):
    """
        name: MATICUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 4
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "MATICUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 4
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATICUSD"

    def __str__(self):
        return "MATICUSD"

    def __call__(self):
        return "MATICUSD"


MATICUSD = MATICUSD()
"""
    name: MATICUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 4
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class MATICUSDT(NamedTuple):
    """
        name: MATICUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 4
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MATICUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 4
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATICUSDT"

    def __str__(self):
        return "MATICUSDT"

    def __call__(self):
        return "MATICUSDT"


MATICUSDT = MATICUSDT()
"""
    name: MATICUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 4
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MATICXBT(NamedTuple):
    """
        name: MATICXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 4
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "MATICXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 4
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATICXBT"

    def __str__(self):
        return "MATICXBT"

    def __call__(self):
        return "MATICXBT"


MATICXBT = MATICXBT()
"""
    name: MATICXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 4
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class MCEUR(NamedTuple):
    """
        name: MCEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 17.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MCEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 17.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MCEUR"

    def __str__(self):
        return "MCEUR"

    def __call__(self):
        return "MCEUR"


MCEUR = MCEUR()
"""
    name: MCEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 17.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MCUSD(NamedTuple):
    """
        name: MCUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 17.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MCUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 17.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MCUSD"

    def __str__(self):
        return "MCUSD"

    def __call__(self):
        return "MCUSD"


MCUSD = MCUSD()
"""
    name: MCUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 17.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MINAEUR(NamedTuple):
    """
        name: MINAEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "MINAEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MINAEUR"

    def __str__(self):
        return "MINAEUR"

    def __call__(self):
        return "MINAEUR"


MINAEUR = MINAEUR()
"""
    name: MINAEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class MINAGBP(NamedTuple):
    """
        name: MINAGBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MINAGBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MINAGBP"

    def __str__(self):
        return "MINAGBP"

    def __call__(self):
        return "MINAGBP"


MINAGBP = MINAGBP()
"""
    name: MINAGBP
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MINAUSD(NamedTuple):
    """
        name: MINAUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "MINAUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MINAUSD"

    def __str__(self):
        return "MINAUSD"

    def __call__(self):
        return "MINAUSD"


MINAUSD = MINAUSD()
"""
    name: MINAUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class MINAXBT(NamedTuple):
    """
        name: MINAXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MINAXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MINAXBT"

    def __str__(self):
        return "MINAXBT"

    def __call__(self):
        return "MINAXBT"


MINAXBT = MINAXBT()
"""
    name: MINAXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MIREUR(NamedTuple):
    """
        name: MIREUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MIREUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MIREUR"

    def __str__(self):
        return "MIREUR"

    def __call__(self):
        return "MIREUR"


MIREUR = MIREUR()
"""
    name: MIREUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MIRUSD(NamedTuple):
    """
        name: MIRUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MIRUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MIRUSD"

    def __str__(self):
        return "MIRUSD"

    def __call__(self):
        return "MIRUSD"


MIRUSD = MIRUSD()
"""
    name: MIRUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MKREUR(NamedTuple):
    """
        name: MKREUR
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0075
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MKREUR"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0075
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MKREUR"

    def __str__(self):
        return "MKREUR"

    def __call__(self):
        return "MKREUR"


MKREUR = MKREUR()
"""
    name: MKREUR
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0075
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MKRUSD(NamedTuple):
    """
        name: MKRUSD
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0075
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MKRUSD"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0075
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MKRUSD"

    def __str__(self):
        return "MKRUSD"

    def __call__(self):
        return "MKRUSD"


MKRUSD = MKRUSD()
"""
    name: MKRUSD
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0075
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MKRXBT(NamedTuple):
    """
        name: MKRXBT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.0075
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MKRXBT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0075
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MKRXBT"

    def __str__(self):
        return "MKRXBT"

    def __call__(self):
        return "MKRXBT"


MKRXBT = MKRXBT()
"""
    name: MKRXBT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.0075
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MNGOEUR(NamedTuple):
    """
        name: MNGOEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 275
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MNGOEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 275
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MNGOEUR"

    def __str__(self):
        return "MNGOEUR"

    def __call__(self):
        return "MNGOEUR"


MNGOEUR = MNGOEUR()
"""
    name: MNGOEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 275
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MNGOUSD(NamedTuple):
    """
        name: MNGOUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 275
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MNGOUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 275
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MNGOUSD"

    def __str__(self):
        return "MNGOUSD"

    def __call__(self):
        return "MNGOUSD"


MNGOUSD = MNGOUSD()
"""
    name: MNGOUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 275
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MOVREUR(NamedTuple):
    """
        name: MOVREUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.65
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MOVREUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.65
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MOVREUR"

    def __str__(self):
        return "MOVREUR"

    def __call__(self):
        return "MOVREUR"


MOVREUR = MOVREUR()
"""
    name: MOVREUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.65
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MOVRUSD(NamedTuple):
    """
        name: MOVRUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.65
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MOVRUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.65
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MOVRUSD"

    def __str__(self):
        return "MOVRUSD"

    def __call__(self):
        return "MOVRUSD"


MOVRUSD = MOVRUSD()
"""
    name: MOVRUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.65
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MSOLEUR(NamedTuple):
    """
        name: MSOLEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.225
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MSOLEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.225
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MSOLEUR"

    def __str__(self):
        return "MSOLEUR"

    def __call__(self):
        return "MSOLEUR"


MSOLEUR = MSOLEUR()
"""
    name: MSOLEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.225
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MSOLUSD(NamedTuple):
    """
        name: MSOLUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.225
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MSOLUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.225
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MSOLUSD"

    def __str__(self):
        return "MSOLUSD"

    def __call__(self):
        return "MSOLUSD"


MSOLUSD = MSOLUSD()
"""
    name: MSOLUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.225
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MULTIEUR(NamedTuple):
    """
        name: MULTIEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.6
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MULTIEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.6
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MULTIEUR"

    def __str__(self):
        return "MULTIEUR"

    def __call__(self):
        return "MULTIEUR"


MULTIEUR = MULTIEUR()
"""
    name: MULTIEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.6
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MULTIUSD(NamedTuple):
    """
        name: MULTIUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.6
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MULTIUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.6
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MULTIUSD"

    def __str__(self):
        return "MULTIUSD"

    def __call__(self):
        return "MULTIUSD"


MULTIUSD = MULTIUSD()
"""
    name: MULTIUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.6
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MVEUR(NamedTuple):
    """
        name: MVEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MVEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MVEUR"

    def __str__(self):
        return "MVEUR"

    def __call__(self):
        return "MVEUR"


MVEUR = MVEUR()
"""
    name: MVEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MVUSD(NamedTuple):
    """
        name: MVUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MVUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MVUSD"

    def __str__(self):
        return "MVUSD"

    def __call__(self):
        return "MVUSD"


MVUSD = MVUSD()
"""
    name: MVUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MXCEUR(NamedTuple):
    """
        name: MXCEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 200
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MXCEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 200
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MXCEUR"

    def __str__(self):
        return "MXCEUR"

    def __call__(self):
        return "MXCEUR"


MXCEUR = MXCEUR()
"""
    name: MXCEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 200
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class MXCUSD(NamedTuple):
    """
        name: MXCUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 200
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MXCUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 200
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MXCUSD"

    def __str__(self):
        return "MXCUSD"

    def __call__(self):
        return "MXCUSD"


MXCUSD = MXCUSD()
"""
    name: MXCUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 200
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NANOETH(NamedTuple):
    """
        name: NANOETH
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 8
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NANOETH"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NANOETH"

    def __str__(self):
        return "NANOETH"

    def __call__(self):
        return "NANOETH"


NANOETH = NANOETH()
"""
    name: NANOETH
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 8
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NANOEUR(NamedTuple):
    """
        name: NANOEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "NANOEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NANOEUR"

    def __str__(self):
        return "NANOEUR"

    def __call__(self):
        return "NANOEUR"


NANOEUR = NANOEUR()
"""
    name: NANOEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class NANOUSD(NamedTuple):
    """
        name: NANOUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 8
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "NANOUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NANOUSD"

    def __str__(self):
        return "NANOUSD"

    def __call__(self):
        return "NANOUSD"


NANOUSD = NANOUSD()
"""
    name: NANOUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 8
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class NANOXBT(NamedTuple):
    """
        name: NANOXBT
        significant_digits: None
        tick_size: 0.000000001
        min_margin: None
        initial_margin: None
        min_order_size: 8
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NANOXBT"
    significant_digits: int = None
    tick_size: int = 0.000000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NANOXBT"

    def __str__(self):
        return "NANOXBT"

    def __call__(self):
        return "NANOXBT"


NANOXBT = NANOXBT()
"""
    name: NANOXBT
    significant_digits: None
    tick_size: 0.000000001
    min_margin: None
    initial_margin: None
    min_order_size: 8
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NEAREUR(NamedTuple):
    """
        name: NEAREUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NEAREUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NEAREUR"

    def __str__(self):
        return "NEAREUR"

    def __call__(self):
        return "NEAREUR"


NEAREUR = NEAREUR()
"""
    name: NEAREUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NEARUSD(NamedTuple):
    """
        name: NEARUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NEARUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NEARUSD"

    def __str__(self):
        return "NEARUSD"

    def __call__(self):
        return "NEARUSD"


NEARUSD = NEARUSD()
"""
    name: NEARUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NMREUR(NamedTuple):
    """
        name: NMREUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NMREUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NMREUR"

    def __str__(self):
        return "NMREUR"

    def __call__(self):
        return "NMREUR"


NMREUR = NMREUR()
"""
    name: NMREUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NMRUSD(NamedTuple):
    """
        name: NMRUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NMRUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NMRUSD"

    def __str__(self):
        return "NMRUSD"

    def __call__(self):
        return "NMRUSD"


NMRUSD = NMRUSD()
"""
    name: NMRUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NODLEUR(NamedTuple):
    """
        name: NODLEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 2000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NODLEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NODLEUR"

    def __str__(self):
        return "NODLEUR"

    def __call__(self):
        return "NODLEUR"


NODLEUR = NODLEUR()
"""
    name: NODLEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 2000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NODLUSD(NamedTuple):
    """
        name: NODLUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 2000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NODLUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NODLUSD"

    def __str__(self):
        return "NODLUSD"

    def __call__(self):
        return "NODLUSD"


NODLUSD = NODLUSD()
"""
    name: NODLUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 2000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NYMEUR(NamedTuple):
    """
        name: NYMEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NYMEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NYMEUR"

    def __str__(self):
        return "NYMEUR"

    def __call__(self):
        return "NYMEUR"


NYMEUR = NYMEUR()
"""
    name: NYMEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NYMUSD(NamedTuple):
    """
        name: NYMUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NYMUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NYMUSD"

    def __str__(self):
        return "NYMUSD"

    def __call__(self):
        return "NYMUSD"


NYMUSD = NYMUSD()
"""
    name: NYMUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class NYMXBT(NamedTuple):
    """
        name: NYMXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "NYMXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NYMXBT"

    def __str__(self):
        return "NYMXBT"

    def __call__(self):
        return "NYMXBT"


NYMXBT = NYMXBT()
"""
    name: NYMXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OCEANEUR(NamedTuple):
    """
        name: OCEANEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 12
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "OCEANEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OCEANEUR"

    def __str__(self):
        return "OCEANEUR"

    def __call__(self):
        return "OCEANEUR"


OCEANEUR = OCEANEUR()
"""
    name: OCEANEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 12
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class OCEANGBP(NamedTuple):
    """
        name: OCEANGBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 12
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OCEANGBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OCEANGBP"

    def __str__(self):
        return "OCEANGBP"

    def __call__(self):
        return "OCEANGBP"


OCEANGBP = OCEANGBP()
"""
    name: OCEANGBP
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 12
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OCEANUSD(NamedTuple):
    """
        name: OCEANUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 12
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "OCEANUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OCEANUSD"

    def __str__(self):
        return "OCEANUSD"

    def __call__(self):
        return "OCEANUSD"


OCEANUSD = OCEANUSD()
"""
    name: OCEANUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 12
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class OCEANXBT(NamedTuple):
    """
        name: OCEANXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 12
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OCEANXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 12
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OCEANXBT"

    def __str__(self):
        return "OCEANXBT"

    def __call__(self):
        return "OCEANXBT"


OCEANXBT = OCEANXBT()
"""
    name: OCEANXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 12
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OGNEUR(NamedTuple):
    """
        name: OGNEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OGNEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OGNEUR"

    def __str__(self):
        return "OGNEUR"

    def __call__(self):
        return "OGNEUR"


OGNEUR = OGNEUR()
"""
    name: OGNEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OGNUSD(NamedTuple):
    """
        name: OGNUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OGNUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OGNUSD"

    def __str__(self):
        return "OGNUSD"

    def __call__(self):
        return "OGNUSD"


OGNUSD = OGNUSD()
"""
    name: OGNUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OMGETH(NamedTuple):
    """
        name: OMGETH
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 3.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OMGETH"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMGETH"

    def __str__(self):
        return "OMGETH"

    def __call__(self):
        return "OMGETH"


OMGETH = OMGETH()
"""
    name: OMGETH
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 3.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OMGEUR(NamedTuple):
    """
        name: OMGEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 3.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "OMGEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMGEUR"

    def __str__(self):
        return "OMGEUR"

    def __call__(self):
        return "OMGEUR"


OMGEUR = OMGEUR()
"""
    name: OMGEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 3.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class OMGJPY(NamedTuple):
    """
        name: OMGJPY
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 3.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OMGJPY"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMGJPY"

    def __str__(self):
        return "OMGJPY"

    def __call__(self):
        return "OMGJPY"


OMGJPY = OMGJPY()
"""
    name: OMGJPY
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 3.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OMGUSD(NamedTuple):
    """
        name: OMGUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 3.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "OMGUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMGUSD"

    def __str__(self):
        return "OMGUSD"

    def __call__(self):
        return "OMGUSD"


OMGUSD = OMGUSD()
"""
    name: OMGUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 3.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class OMGXBT(NamedTuple):
    """
        name: OMGXBT
        significant_digits: None
        tick_size: 0.000000001
        min_margin: None
        initial_margin: None
        min_order_size: 3.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "OMGXBT"
    significant_digits: int = None
    tick_size: int = 0.000000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMGXBT"

    def __str__(self):
        return "OMGXBT"

    def __call__(self):
        return "OMGXBT"


OMGXBT = OMGXBT()
"""
    name: OMGXBT
    significant_digits: None
    tick_size: 0.000000001
    min_margin: None
    initial_margin: None
    min_order_size: 3.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class ORCAEUR(NamedTuple):
    """
        name: ORCAEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 6
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ORCAEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ORCAEUR"

    def __str__(self):
        return "ORCAEUR"

    def __call__(self):
        return "ORCAEUR"


ORCAEUR = ORCAEUR()
"""
    name: ORCAEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 6
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ORCAUSD(NamedTuple):
    """
        name: ORCAUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 6
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ORCAUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ORCAUSD"

    def __str__(self):
        return "ORCAUSD"

    def __call__(self):
        return "ORCAUSD"


ORCAUSD = ORCAUSD()
"""
    name: ORCAUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 6
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OXTEUR(NamedTuple):
    """
        name: OXTEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 55
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OXTEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 55
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OXTEUR"

    def __str__(self):
        return "OXTEUR"

    def __call__(self):
        return "OXTEUR"


OXTEUR = OXTEUR()
"""
    name: OXTEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 55
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OXTUSD(NamedTuple):
    """
        name: OXTUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 55
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OXTUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 55
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OXTUSD"

    def __str__(self):
        return "OXTUSD"

    def __call__(self):
        return "OXTUSD"


OXTUSD = OXTUSD()
"""
    name: OXTUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 55
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OXTXBT(NamedTuple):
    """
        name: OXTXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 55
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OXTXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 55
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OXTXBT"

    def __str__(self):
        return "OXTXBT"

    def __call__(self):
        return "OXTXBT"


OXTXBT = OXTXBT()
"""
    name: OXTXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 55
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OXYEUR(NamedTuple):
    """
        name: OXYEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OXYEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OXYEUR"

    def __str__(self):
        return "OXYEUR"

    def __call__(self):
        return "OXYEUR"


OXYEUR = OXYEUR()
"""
    name: OXYEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class OXYUSD(NamedTuple):
    """
        name: OXYUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "OXYUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OXYUSD"

    def __str__(self):
        return "OXYUSD"

    def __call__(self):
        return "OXYUSD"


OXYUSD = OXYUSD()
"""
    name: OXYUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PARAEUR(NamedTuple):
    """
        name: PARAEUR
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PARAEUR"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PARAEUR"

    def __str__(self):
        return "PARAEUR"

    def __call__(self):
        return "PARAEUR"


PARAEUR = PARAEUR()
"""
    name: PARAEUR
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PARAUSD(NamedTuple):
    """
        name: PARAUSD
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PARAUSD"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PARAUSD"

    def __str__(self):
        return "PARAUSD"

    def __call__(self):
        return "PARAUSD"


PARAUSD = PARAUSD()
"""
    name: PARAUSD
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PAXGETH(NamedTuple):
    """
        name: PAXGETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.003
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PAXGETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.003
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PAXGETH"

    def __str__(self):
        return "PAXGETH"

    def __call__(self):
        return "PAXGETH"


PAXGETH = PAXGETH()
"""
    name: PAXGETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.003
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PAXGEUR(NamedTuple):
    """
        name: PAXGEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.003
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "PAXGEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.003
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PAXGEUR"

    def __str__(self):
        return "PAXGEUR"

    def __call__(self):
        return "PAXGEUR"


PAXGEUR = PAXGEUR()
"""
    name: PAXGEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.003
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class PAXGUSD(NamedTuple):
    """
        name: PAXGUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.003
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "PAXGUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.003
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PAXGUSD"

    def __str__(self):
        return "PAXGUSD"

    def __call__(self):
        return "PAXGUSD"


PAXGUSD = PAXGUSD()
"""
    name: PAXGUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.003
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class PAXGXBT(NamedTuple):
    """
        name: PAXGXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.003
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "PAXGXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.003
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PAXGXBT"

    def __str__(self):
        return "PAXGXBT"

    def __call__(self):
        return "PAXGXBT"


PAXGXBT = PAXGXBT()
"""
    name: PAXGXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.003
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class PERPEUR(NamedTuple):
    """
        name: PERPEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 9
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PERPEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 9
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PERPEUR"

    def __str__(self):
        return "PERPEUR"

    def __call__(self):
        return "PERPEUR"


PERPEUR = PERPEUR()
"""
    name: PERPEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 9
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PERPUSD(NamedTuple):
    """
        name: PERPUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 9
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PERPUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 9
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PERPUSD"

    def __str__(self):
        return "PERPUSD"

    def __call__(self):
        return "PERPUSD"


PERPUSD = PERPUSD()
"""
    name: PERPUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 9
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PHAEUR(NamedTuple):
    """
        name: PHAEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PHAEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PHAEUR"

    def __str__(self):
        return "PHAEUR"

    def __call__(self):
        return "PHAEUR"


PHAEUR = PHAEUR()
"""
    name: PHAEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PHAUSD(NamedTuple):
    """
        name: PHAUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PHAUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PHAUSD"

    def __str__(self):
        return "PHAUSD"

    def __call__(self):
        return "PHAUSD"


PHAUSD = PHAUSD()
"""
    name: PHAUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PLAEUR(NamedTuple):
    """
        name: PLAEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PLAEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PLAEUR"

    def __str__(self):
        return "PLAEUR"

    def __call__(self):
        return "PLAEUR"


PLAEUR = PLAEUR()
"""
    name: PLAEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PLAUSD(NamedTuple):
    """
        name: PLAUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PLAUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PLAUSD"

    def __str__(self):
        return "PLAUSD"

    def __call__(self):
        return "PLAUSD"


PLAUSD = PLAUSD()
"""
    name: PLAUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class POLISEUR(NamedTuple):
    """
        name: POLISEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 17
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "POLISEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 17
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLISEUR"

    def __str__(self):
        return "POLISEUR"

    def __call__(self):
        return "POLISEUR"


POLISEUR = POLISEUR()
"""
    name: POLISEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 17
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class POLISUSD(NamedTuple):
    """
        name: POLISUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 17
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "POLISUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 17
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLISUSD"

    def __str__(self):
        return "POLISUSD"

    def __call__(self):
        return "POLISUSD"


POLISUSD = POLISUSD()
"""
    name: POLISUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 17
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class POLSEUR(NamedTuple):
    """
        name: POLSEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "POLSEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLSEUR"

    def __str__(self):
        return "POLSEUR"

    def __call__(self):
        return "POLSEUR"


POLSEUR = POLSEUR()
"""
    name: POLSEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class POLSUSD(NamedTuple):
    """
        name: POLSUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "POLSUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLSUSD"

    def __str__(self):
        return "POLSUSD"

    def __call__(self):
        return "POLSUSD"


POLSUSD = POLSUSD()
"""
    name: POLSUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PONDEUR(NamedTuple):
    """
        name: PONDEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 600
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PONDEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 600
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PONDEUR"

    def __str__(self):
        return "PONDEUR"

    def __call__(self):
        return "PONDEUR"


PONDEUR = PONDEUR()
"""
    name: PONDEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 600
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PONDUSD(NamedTuple):
    """
        name: PONDUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 600
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PONDUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 600
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PONDUSD"

    def __str__(self):
        return "PONDUSD"

    def __call__(self):
        return "PONDUSD"


PONDUSD = PONDUSD()
"""
    name: PONDUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 600
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class POWREUR(NamedTuple):
    """
        name: POWREUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "POWREUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POWREUR"

    def __str__(self):
        return "POWREUR"

    def __call__(self):
        return "POWREUR"


POWREUR = POWREUR()
"""
    name: POWREUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class POWRUSD(NamedTuple):
    """
        name: POWRUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 30
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "POWRUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 30
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POWRUSD"

    def __str__(self):
        return "POWRUSD"

    def __call__(self):
        return "POWRUSD"


POWRUSD = POWRUSD()
"""
    name: POWRUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 30
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PSTAKEEUR(NamedTuple):
    """
        name: PSTAKEEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 40
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PSTAKEEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 40
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PSTAKEEUR"

    def __str__(self):
        return "PSTAKEEUR"

    def __call__(self):
        return "PSTAKEEUR"


PSTAKEEUR = PSTAKEEUR()
"""
    name: PSTAKEEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 40
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class PSTAKEUSD(NamedTuple):
    """
        name: PSTAKEUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 40
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "PSTAKEUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 40
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PSTAKEUSD"

    def __str__(self):
        return "PSTAKEUSD"

    def __call__(self):
        return "PSTAKEUSD"


PSTAKEUSD = PSTAKEUSD()
"""
    name: PSTAKEUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 40
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class QNTEUR(NamedTuple):
    """
        name: QNTEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "QNTEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QNTEUR"

    def __str__(self):
        return "QNTEUR"

    def __call__(self):
        return "QNTEUR"


QNTEUR = QNTEUR()
"""
    name: QNTEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class QNTUSD(NamedTuple):
    """
        name: QNTUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.05
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "QNTUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.05
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QNTUSD"

    def __str__(self):
        return "QNTUSD"

    def __call__(self):
        return "QNTUSD"


QNTUSD = QNTUSD()
"""
    name: QNTUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.05
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class QTUMETH(NamedTuple):
    """
        name: QTUMETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "QTUMETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QTUMETH"

    def __str__(self):
        return "QTUMETH"

    def __call__(self):
        return "QTUMETH"


QTUMETH = QTUMETH()
"""
    name: QTUMETH
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class QTUMEUR(NamedTuple):
    """
        name: QTUMEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "QTUMEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QTUMEUR"

    def __str__(self):
        return "QTUMEUR"

    def __call__(self):
        return "QTUMEUR"


QTUMEUR = QTUMEUR()
"""
    name: QTUMEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class QTUMUSD(NamedTuple):
    """
        name: QTUMUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "QTUMUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QTUMUSD"

    def __str__(self):
        return "QTUMUSD"

    def __call__(self):
        return "QTUMUSD"


QTUMUSD = QTUMUSD()
"""
    name: QTUMUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class QTUMXBT(NamedTuple):
    """
        name: QTUMXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "QTUMXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QTUMXBT"

    def __str__(self):
        return "QTUMXBT"

    def __call__(self):
        return "QTUMXBT"


QTUMXBT = QTUMXBT()
"""
    name: QTUMXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RADEUR(NamedTuple):
    """
        name: RADEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RADEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RADEUR"

    def __str__(self):
        return "RADEUR"

    def __call__(self):
        return "RADEUR"


RADEUR = RADEUR()
"""
    name: RADEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RADUSD(NamedTuple):
    """
        name: RADUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RADUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RADUSD"

    def __str__(self):
        return "RADUSD"

    def __call__(self):
        return "RADUSD"


RADUSD = RADUSD()
"""
    name: RADUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RAREEUR(NamedTuple):
    """
        name: RAREEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RAREEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAREEUR"

    def __str__(self):
        return "RAREEUR"

    def __call__(self):
        return "RAREEUR"


RAREEUR = RAREEUR()
"""
    name: RAREEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RAREUSD(NamedTuple):
    """
        name: RAREUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RAREUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAREUSD"

    def __str__(self):
        return "RAREUSD"

    def __call__(self):
        return "RAREUSD"


RAREUSD = RAREUSD()
"""
    name: RAREUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RARIEUR(NamedTuple):
    """
        name: RARIEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RARIEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RARIEUR"

    def __str__(self):
        return "RARIEUR"

    def __call__(self):
        return "RARIEUR"


RARIEUR = RARIEUR()
"""
    name: RARIEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RARIUSD(NamedTuple):
    """
        name: RARIUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RARIUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RARIUSD"

    def __str__(self):
        return "RARIUSD"

    def __call__(self):
        return "RARIUSD"


RARIUSD = RARIUSD()
"""
    name: RARIUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RARIXBT(NamedTuple):
    """
        name: RARIXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RARIXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RARIXBT"

    def __str__(self):
        return "RARIXBT"

    def __call__(self):
        return "RARIXBT"


RARIXBT = RARIXBT()
"""
    name: RARIXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RAYEUR(NamedTuple):
    """
        name: RAYEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 18
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RAYEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 18
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAYEUR"

    def __str__(self):
        return "RAYEUR"

    def __call__(self):
        return "RAYEUR"


RAYEUR = RAYEUR()
"""
    name: RAYEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 18
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RAYUSD(NamedTuple):
    """
        name: RAYUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 18
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RAYUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 18
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAYUSD"

    def __str__(self):
        return "RAYUSD"

    def __call__(self):
        return "RAYUSD"


RAYUSD = RAYUSD()
"""
    name: RAYUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 18
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RBCEUR(NamedTuple):
    """
        name: RBCEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RBCEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RBCEUR"

    def __str__(self):
        return "RBCEUR"

    def __call__(self):
        return "RBCEUR"


RBCEUR = RBCEUR()
"""
    name: RBCEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RBCUSD(NamedTuple):
    """
        name: RBCUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RBCUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RBCUSD"

    def __str__(self):
        return "RBCUSD"

    def __call__(self):
        return "RBCUSD"


RBCUSD = RBCUSD()
"""
    name: RBCUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RENEUR(NamedTuple):
    """
        name: RENEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RENEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RENEUR"

    def __str__(self):
        return "RENEUR"

    def __call__(self):
        return "RENEUR"


RENEUR = RENEUR()
"""
    name: RENEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RENUSD(NamedTuple):
    """
        name: RENUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RENUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RENUSD"

    def __str__(self):
        return "RENUSD"

    def __call__(self):
        return "RENUSD"


RENUSD = RENUSD()
"""
    name: RENUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RENXBT(NamedTuple):
    """
        name: RENXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RENXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RENXBT"

    def __str__(self):
        return "RENXBT"

    def __call__(self):
        return "RENXBT"


RENXBT = RENXBT()
"""
    name: RENXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class REPV2ETH(NamedTuple):
    """
        name: REPV2ETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "REPV2ETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REPV2ETH"

    def __str__(self):
        return "REPV2ETH"

    def __call__(self):
        return "REPV2ETH"


REPV2ETH = REPV2ETH()
"""
    name: REPV2ETH
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class REPV2EUR(NamedTuple):
    """
        name: REPV2EUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "REPV2EUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REPV2EUR"

    def __str__(self):
        return "REPV2EUR"

    def __call__(self):
        return "REPV2EUR"


REPV2EUR = REPV2EUR()
"""
    name: REPV2EUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class REPV2USD(NamedTuple):
    """
        name: REPV2USD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "REPV2USD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REPV2USD"

    def __str__(self):
        return "REPV2USD"

    def __call__(self):
        return "REPV2USD"


REPV2USD = REPV2USD()
"""
    name: REPV2USD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class REPV2XBT(NamedTuple):
    """
        name: REPV2XBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "REPV2XBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REPV2XBT"

    def __str__(self):
        return "REPV2XBT"

    def __call__(self):
        return "REPV2XBT"


REPV2XBT = REPV2XBT()
"""
    name: REPV2XBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class REQEUR(NamedTuple):
    """
        name: REQEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "REQEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REQEUR"

    def __str__(self):
        return "REQEUR"

    def __call__(self):
        return "REQEUR"


REQEUR = REQEUR()
"""
    name: REQEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class REQUSD(NamedTuple):
    """
        name: REQUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "REQUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REQUSD"

    def __str__(self):
        return "REQUSD"

    def __call__(self):
        return "REQUSD"


REQUSD = REQUSD()
"""
    name: REQUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RLCEUR(NamedTuple):
    """
        name: RLCEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RLCEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RLCEUR"

    def __str__(self):
        return "RLCEUR"

    def __call__(self):
        return "RLCEUR"


RLCEUR = RLCEUR()
"""
    name: RLCEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RLCUSD(NamedTuple):
    """
        name: RLCUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RLCUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RLCUSD"

    def __str__(self):
        return "RLCUSD"

    def __call__(self):
        return "RLCUSD"


RLCUSD = RLCUSD()
"""
    name: RLCUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RNDREUR(NamedTuple):
    """
        name: RNDREUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RNDREUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RNDREUR"

    def __str__(self):
        return "RNDREUR"

    def __call__(self):
        return "RNDREUR"


RNDREUR = RNDREUR()
"""
    name: RNDREUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RNDRUSD(NamedTuple):
    """
        name: RNDRUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RNDRUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RNDRUSD"

    def __str__(self):
        return "RNDRUSD"

    def __call__(self):
        return "RNDRUSD"


RNDRUSD = RNDRUSD()
"""
    name: RNDRUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ROOKEUR(NamedTuple):
    """
        name: ROOKEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ROOKEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ROOKEUR"

    def __str__(self):
        return "ROOKEUR"

    def __call__(self):
        return "ROOKEUR"


ROOKEUR = ROOKEUR()
"""
    name: ROOKEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ROOKUSD(NamedTuple):
    """
        name: ROOKUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.35
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ROOKUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.35
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ROOKUSD"

    def __str__(self):
        return "ROOKUSD"

    def __call__(self):
        return "ROOKUSD"


ROOKUSD = ROOKUSD()
"""
    name: ROOKUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.35
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RPLEUR(NamedTuple):
    """
        name: RPLEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.125
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RPLEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.125
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RPLEUR"

    def __str__(self):
        return "RPLEUR"

    def __call__(self):
        return "RPLEUR"


RPLEUR = RPLEUR()
"""
    name: RPLEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.125
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RPLUSD(NamedTuple):
    """
        name: RPLUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.125
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RPLUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.125
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RPLUSD"

    def __str__(self):
        return "RPLUSD"

    def __call__(self):
        return "RPLUSD"


RPLUSD = RPLUSD()
"""
    name: RPLUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.125
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RUNEEUR(NamedTuple):
    """
        name: RUNEEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RUNEEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RUNEEUR"

    def __str__(self):
        return "RUNEEUR"

    def __call__(self):
        return "RUNEEUR"


RUNEEUR = RUNEEUR()
"""
    name: RUNEEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class RUNEUSD(NamedTuple):
    """
        name: RUNEUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "RUNEUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RUNEUSD"

    def __str__(self):
        return "RUNEUSD"

    def __call__(self):
        return "RUNEUSD"


RUNEUSD = RUNEUSD()
"""
    name: RUNEUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SAMOEUR(NamedTuple):
    """
        name: SAMOEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SAMOEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SAMOEUR"

    def __str__(self):
        return "SAMOEUR"

    def __call__(self):
        return "SAMOEUR"


SAMOEUR = SAMOEUR()
"""
    name: SAMOEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SAMOUSD(NamedTuple):
    """
        name: SAMOUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SAMOUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SAMOUSD"

    def __str__(self):
        return "SAMOUSD"

    def __call__(self):
        return "SAMOUSD"


SAMOUSD = SAMOUSD()
"""
    name: SAMOUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SANDEUR(NamedTuple):
    """
        name: SANDEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 8.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "SANDEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SANDEUR"

    def __str__(self):
        return "SANDEUR"

    def __call__(self):
        return "SANDEUR"


SANDEUR = SANDEUR()
"""
    name: SANDEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 8.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class SANDGBP(NamedTuple):
    """
        name: SANDGBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 8.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SANDGBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SANDGBP"

    def __str__(self):
        return "SANDGBP"

    def __call__(self):
        return "SANDGBP"


SANDGBP = SANDGBP()
"""
    name: SANDGBP
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 8.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SANDUSD(NamedTuple):
    """
        name: SANDUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 8.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "SANDUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SANDUSD"

    def __str__(self):
        return "SANDUSD"

    def __call__(self):
        return "SANDUSD"


SANDUSD = SANDUSD()
"""
    name: SANDUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 8.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class SANDXBT(NamedTuple):
    """
        name: SANDXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 8.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SANDXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 8.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SANDXBT"

    def __str__(self):
        return "SANDXBT"

    def __call__(self):
        return "SANDXBT"


SANDXBT = SANDXBT()
"""
    name: SANDXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 8.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SBREUR(NamedTuple):
    """
        name: SBREUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SBREUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SBREUR"

    def __str__(self):
        return "SBREUR"

    def __call__(self):
        return "SBREUR"


SBREUR = SBREUR()
"""
    name: SBREUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SBRUSD(NamedTuple):
    """
        name: SBRUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SBRUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SBRUSD"

    def __str__(self):
        return "SBRUSD"

    def __call__(self):
        return "SBRUSD"


SBRUSD = SBRUSD()
"""
    name: SBRUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SCETH(NamedTuple):
    """
        name: SCETH
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 1300
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SCETH"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1300
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SCETH"

    def __str__(self):
        return "SCETH"

    def __call__(self):
        return "SCETH"


SCETH = SCETH()
"""
    name: SCETH
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 1300
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SCEUR(NamedTuple):
    """
        name: SCEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1300
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "SCEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1300
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SCEUR"

    def __str__(self):
        return "SCEUR"

    def __call__(self):
        return "SCEUR"


SCEUR = SCEUR()
"""
    name: SCEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1300
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class SCRTEUR(NamedTuple):
    """
        name: SCRTEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 7
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SCRTEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SCRTEUR"

    def __str__(self):
        return "SCRTEUR"

    def __call__(self):
        return "SCRTEUR"


SCRTEUR = SCRTEUR()
"""
    name: SCRTEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 7
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SCRTUSD(NamedTuple):
    """
        name: SCRTUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 7
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SCRTUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SCRTUSD"

    def __str__(self):
        return "SCRTUSD"

    def __call__(self):
        return "SCRTUSD"


SCRTUSD = SCRTUSD()
"""
    name: SCRTUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 7
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SCUSD(NamedTuple):
    """
        name: SCUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1300
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "SCUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1300
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SCUSD"

    def __str__(self):
        return "SCUSD"

    def __call__(self):
        return "SCUSD"


SCUSD = SCUSD()
"""
    name: SCUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1300
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class SCXBT(NamedTuple):
    """
        name: SCXBT
        significant_digits: None
        tick_size: 0.0000000001
        min_margin: None
        initial_margin: None
        min_order_size: 1300
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SCXBT"
    significant_digits: int = None
    tick_size: int = 0.0000000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1300
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SCXBT"

    def __str__(self):
        return "SCXBT"

    def __call__(self):
        return "SCXBT"


SCXBT = SCXBT()
"""
    name: SCXBT
    significant_digits: None
    tick_size: 0.0000000001
    min_margin: None
    initial_margin: None
    min_order_size: 1300
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SDNEUR(NamedTuple):
    """
        name: SDNEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SDNEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SDNEUR"

    def __str__(self):
        return "SDNEUR"

    def __call__(self):
        return "SDNEUR"


SDNEUR = SDNEUR()
"""
    name: SDNEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SDNUSD(NamedTuple):
    """
        name: SDNUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 10
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SDNUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 10
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SDNUSD"

    def __str__(self):
        return "SDNUSD"

    def __call__(self):
        return "SDNUSD"


SDNUSD = SDNUSD()
"""
    name: SDNUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 10
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SGBEUR(NamedTuple):
    """
        name: SGBEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SGBEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SGBEUR"

    def __str__(self):
        return "SGBEUR"

    def __call__(self):
        return "SGBEUR"


SGBEUR = SGBEUR()
"""
    name: SGBEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SGBUSD(NamedTuple):
    """
        name: SGBUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SGBUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SGBUSD"

    def __str__(self):
        return "SGBUSD"

    def __call__(self):
        return "SGBUSD"


SGBUSD = SGBUSD()
"""
    name: SGBUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SHIBEUR(NamedTuple):
    """
        name: SHIBEUR
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 500000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SHIBEUR"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 500000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHIBEUR"

    def __str__(self):
        return "SHIBEUR"

    def __call__(self):
        return "SHIBEUR"


SHIBEUR = SHIBEUR()
"""
    name: SHIBEUR
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 500000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SHIBUSD(NamedTuple):
    """
        name: SHIBUSD
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 500000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SHIBUSD"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 500000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHIBUSD"

    def __str__(self):
        return "SHIBUSD"

    def __call__(self):
        return "SHIBUSD"


SHIBUSD = SHIBUSD()
"""
    name: SHIBUSD
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 500000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SHIBUSDT(NamedTuple):
    """
        name: SHIBUSDT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 500000
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SHIBUSDT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 500000
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHIBUSDT"

    def __str__(self):
        return "SHIBUSDT"

    def __call__(self):
        return "SHIBUSDT"


SHIBUSDT = SHIBUSDT()
"""
    name: SHIBUSDT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 500000
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SNXETH(NamedTuple):
    """
        name: SNXETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SNXETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNXETH"

    def __str__(self):
        return "SNXETH"

    def __call__(self):
        return "SNXETH"


SNXETH = SNXETH()
"""
    name: SNXETH
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SNXEUR(NamedTuple):
    """
        name: SNXEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SNXEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNXEUR"

    def __str__(self):
        return "SNXEUR"

    def __call__(self):
        return "SNXEUR"


SNXEUR = SNXEUR()
"""
    name: SNXEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SNXUSD(NamedTuple):
    """
        name: SNXUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SNXUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNXUSD"

    def __str__(self):
        return "SNXUSD"

    def __call__(self):
        return "SNXUSD"


SNXUSD = SNXUSD()
"""
    name: SNXUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SNXXBT(NamedTuple):
    """
        name: SNXXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 2
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SNXXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNXXBT"

    def __str__(self):
        return "SNXXBT"

    def __call__(self):
        return "SNXXBT"


SNXXBT = SNXXBT()
"""
    name: SNXXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 2
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SOLEUR(NamedTuple):
    """
        name: SOLEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "SOLEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOLEUR"

    def __str__(self):
        return "SOLEUR"

    def __call__(self):
        return "SOLEUR"


SOLEUR = SOLEUR()
"""
    name: SOLEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class SOLGBP(NamedTuple):
    """
        name: SOLGBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "SOLGBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOLGBP"

    def __str__(self):
        return "SOLGBP"

    def __call__(self):
        return "SOLGBP"


SOLGBP = SOLGBP()
"""
    name: SOLGBP
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class SOLUSD(NamedTuple):
    """
        name: SOLUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "SOLUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOLUSD"

    def __str__(self):
        return "SOLUSD"

    def __call__(self):
        return "SOLUSD"


SOLUSD = SOLUSD()
"""
    name: SOLUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class SOLUSDT(NamedTuple):
    """
        name: SOLUSDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SOLUSDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOLUSDT"

    def __str__(self):
        return "SOLUSDT"

    def __call__(self):
        return "SOLUSDT"


SOLUSDT = SOLUSDT()
"""
    name: SOLUSDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SOLXBT(NamedTuple):
    """
        name: SOLXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "SOLXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOLXBT"

    def __str__(self):
        return "SOLXBT"

    def __call__(self):
        return "SOLXBT"


SOLXBT = SOLXBT()
"""
    name: SOLXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class SPELLEUR(NamedTuple):
    """
        name: SPELLEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 7500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SPELLEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SPELLEUR"

    def __str__(self):
        return "SPELLEUR"

    def __call__(self):
        return "SPELLEUR"


SPELLEUR = SPELLEUR()
"""
    name: SPELLEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 7500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SPELLUSD(NamedTuple):
    """
        name: SPELLUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 7500
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SPELLUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7500
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SPELLUSD"

    def __str__(self):
        return "SPELLUSD"

    def __call__(self):
        return "SPELLUSD"


SPELLUSD = SPELLUSD()
"""
    name: SPELLUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 7500
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SRMEUR(NamedTuple):
    """
        name: SRMEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SRMEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SRMEUR"

    def __str__(self):
        return "SRMEUR"

    def __call__(self):
        return "SRMEUR"


SRMEUR = SRMEUR()
"""
    name: SRMEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SRMUSD(NamedTuple):
    """
        name: SRMUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SRMUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SRMUSD"

    def __str__(self):
        return "SRMUSD"

    def __call__(self):
        return "SRMUSD"


SRMUSD = SRMUSD()
"""
    name: SRMUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SRMXBT(NamedTuple):
    """
        name: SRMXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SRMXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SRMXBT"

    def __str__(self):
        return "SRMXBT"

    def __call__(self):
        return "SRMXBT"


SRMXBT = SRMXBT()
"""
    name: SRMXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class STEPEUR(NamedTuple):
    """
        name: STEPEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 325
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "STEPEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 325
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STEPEUR"

    def __str__(self):
        return "STEPEUR"

    def __call__(self):
        return "STEPEUR"


STEPEUR = STEPEUR()
"""
    name: STEPEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 325
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class STEPUSD(NamedTuple):
    """
        name: STEPUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 325
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "STEPUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 325
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STEPUSD"

    def __str__(self):
        return "STEPUSD"

    def __call__(self):
        return "STEPUSD"


STEPUSD = STEPUSD()
"""
    name: STEPUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 325
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class STGEUR(NamedTuple):
    """
        name: STGEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 6
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "STGEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STGEUR"

    def __str__(self):
        return "STGEUR"

    def __call__(self):
        return "STGEUR"


STGEUR = STGEUR()
"""
    name: STGEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 6
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class STGUSD(NamedTuple):
    """
        name: STGUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 6
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "STGUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 6
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STGUSD"

    def __str__(self):
        return "STGUSD"

    def __call__(self):
        return "STGUSD"


STGUSD = STGUSD()
"""
    name: STGUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 6
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class STORJEUR(NamedTuple):
    """
        name: STORJEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "STORJEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STORJEUR"

    def __str__(self):
        return "STORJEUR"

    def __call__(self):
        return "STORJEUR"


STORJEUR = STORJEUR()
"""
    name: STORJEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class STORJUSD(NamedTuple):
    """
        name: STORJUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "STORJUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STORJUSD"

    def __str__(self):
        return "STORJUSD"

    def __call__(self):
        return "STORJUSD"


STORJUSD = STORJUSD()
"""
    name: STORJUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class STORJXBT(NamedTuple):
    """
        name: STORJXBT
        significant_digits: None
        tick_size: 0.000000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "STORJXBT"
    significant_digits: int = None
    tick_size: int = 0.000000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STORJXBT"

    def __str__(self):
        return "STORJXBT"

    def __call__(self):
        return "STORJXBT"


STORJXBT = STORJXBT()
"""
    name: STORJXBT
    significant_digits: None
    tick_size: 0.000000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class STXEUR(NamedTuple):
    """
        name: STXEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "STXEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STXEUR"

    def __str__(self):
        return "STXEUR"

    def __call__(self):
        return "STXEUR"


STXEUR = STXEUR()
"""
    name: STXEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class STXUSD(NamedTuple):
    """
        name: STXUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 20
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "STXUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 20
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STXUSD"

    def __str__(self):
        return "STXUSD"

    def __call__(self):
        return "STXUSD"


STXUSD = STXUSD()
"""
    name: STXUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 20
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SUPEREUR(NamedTuple):
    """
        name: SUPEREUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SUPEREUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUPEREUR"

    def __str__(self):
        return "SUPEREUR"

    def __call__(self):
        return "SUPEREUR"


SUPEREUR = SUPEREUR()
"""
    name: SUPEREUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SUPERUSD(NamedTuple):
    """
        name: SUPERUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 50
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SUPERUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 50
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUPERUSD"

    def __str__(self):
        return "SUPERUSD"

    def __call__(self):
        return "SUPERUSD"


SUPERUSD = SUPERUSD()
"""
    name: SUPERUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 50
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SUSHIEUR(NamedTuple):
    """
        name: SUSHIEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SUSHIEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHIEUR"

    def __str__(self):
        return "SUSHIEUR"

    def __call__(self):
        return "SUSHIEUR"


SUSHIEUR = SUSHIEUR()
"""
    name: SUSHIEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SUSHIGBP(NamedTuple):
    """
        name: SUSHIGBP
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SUSHIGBP"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHIGBP"

    def __str__(self):
        return "SUSHIGBP"

    def __call__(self):
        return "SUSHIGBP"


SUSHIGBP = SUSHIGBP()
"""
    name: SUSHIGBP
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SUSHIUSD(NamedTuple):
    """
        name: SUSHIUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SUSHIUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHIUSD"

    def __str__(self):
        return "SUSHIUSD"

    def __call__(self):
        return "SUSHIUSD"


SUSHIUSD = SUSHIUSD()
"""
    name: SUSHIUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SUSHIXBT(NamedTuple):
    """
        name: SUSHIXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SUSHIXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHIXBT"

    def __str__(self):
        return "SUSHIXBT"

    def __call__(self):
        return "SUSHIXBT"


SUSHIXBT = SUSHIXBT()
"""
    name: SUSHIXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SYNEUR(NamedTuple):
    """
        name: SYNEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 3.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SYNEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SYNEUR"

    def __str__(self):
        return "SYNEUR"

    def __call__(self):
        return "SYNEUR"


SYNEUR = SYNEUR()
"""
    name: SYNEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 3.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class SYNUSD(NamedTuple):
    """
        name: SYNUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 3.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SYNUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SYNUSD"

    def __str__(self):
        return "SYNUSD"

    def __call__(self):
        return "SYNUSD"


SYNUSD = SYNUSD()
"""
    name: SYNUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 3.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TBTCEUR(NamedTuple):
    """
        name: TBTCEUR
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.00025
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TBTCEUR"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00025
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TBTCEUR"

    def __str__(self):
        return "TBTCEUR"

    def __call__(self):
        return "TBTCEUR"


TBTCEUR = TBTCEUR()
"""
    name: TBTCEUR
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.00025
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TBTCUSD(NamedTuple):
    """
        name: TBTCUSD
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.00025
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TBTCUSD"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00025
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TBTCUSD"

    def __str__(self):
        return "TBTCUSD"

    def __call__(self):
        return "TBTCUSD"


TBTCUSD = TBTCUSD()
"""
    name: TBTCUSD
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.00025
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TBTCXBT(NamedTuple):
    """
        name: TBTCXBT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00025
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TBTCXBT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00025
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TBTCXBT"

    def __str__(self):
        return "TBTCXBT"

    def __call__(self):
        return "TBTCXBT"


TBTCXBT = TBTCXBT()
"""
    name: TBTCXBT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00025
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TEEREUR(NamedTuple):
    """
        name: TEEREUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TEEREUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TEEREUR"

    def __str__(self):
        return "TEEREUR"

    def __call__(self):
        return "TEEREUR"


TEEREUR = TEEREUR()
"""
    name: TEEREUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TEERUSD(NamedTuple):
    """
        name: TEERUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TEERUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TEERUSD"

    def __str__(self):
        return "TEERUSD"

    def __call__(self):
        return "TEERUSD"


TEERUSD = TEERUSD()
"""
    name: TEERUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TEUR(NamedTuple):
    """
        name: TEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 130
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 130
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TEUR"

    def __str__(self):
        return "TEUR"

    def __call__(self):
        return "TEUR"


TEUR = TEUR()
"""
    name: TEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 130
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TLMEUR(NamedTuple):
    """
        name: TLMEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TLMEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TLMEUR"

    def __str__(self):
        return "TLMEUR"

    def __call__(self):
        return "TLMEUR"


TLMEUR = TLMEUR()
"""
    name: TLMEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TLMUSD(NamedTuple):
    """
        name: TLMUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 250
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TLMUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 250
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TLMUSD"

    def __str__(self):
        return "TLMUSD"

    def __call__(self):
        return "TLMUSD"


TLMUSD = TLMUSD()
"""
    name: TLMUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 250
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TOKEEUR(NamedTuple):
    """
        name: TOKEEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TOKEEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TOKEEUR"

    def __str__(self):
        return "TOKEEUR"

    def __call__(self):
        return "TOKEEUR"


TOKEEUR = TOKEEUR()
"""
    name: TOKEEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TOKEUSD(NamedTuple):
    """
        name: TOKEUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TOKEUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TOKEUSD"

    def __str__(self):
        return "TOKEUSD"

    def __call__(self):
        return "TOKEUSD"


TOKEUSD = TOKEUSD()
"""
    name: TOKEUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TRIBEEUR(NamedTuple):
    """
        name: TRIBEEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TRIBEEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRIBEEUR"

    def __str__(self):
        return "TRIBEEUR"

    def __call__(self):
        return "TRIBEEUR"


TRIBEEUR = TRIBEEUR()
"""
    name: TRIBEEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TRIBEUSD(NamedTuple):
    """
        name: TRIBEUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TRIBEUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRIBEUSD"

    def __str__(self):
        return "TRIBEUSD"

    def __call__(self):
        return "TRIBEUSD"


TRIBEUSD = TRIBEUSD()
"""
    name: TRIBEUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TRUEUR(NamedTuple):
    """
        name: TRUEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 125
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TRUEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 125
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRUEUR"

    def __str__(self):
        return "TRUEUR"

    def __call__(self):
        return "TRUEUR"


TRUEUR = TRUEUR()
"""
    name: TRUEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 125
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TRUUSD(NamedTuple):
    """
        name: TRUUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 125
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TRUUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 125
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRUUSD"

    def __str__(self):
        return "TRUUSD"

    def __call__(self):
        return "TRUUSD"


TRUUSD = TRUUSD()
"""
    name: TRUUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 125
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TRXETH(NamedTuple):
    """
        name: TRXETH
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 100
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "TRXETH"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 100
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRXETH"

    def __str__(self):
        return "TRXETH"

    def __call__(self):
        return "TRXETH"


TRXETH = TRXETH()
"""
    name: TRXETH
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 100
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class TRXEUR(NamedTuple):
    """
        name: TRXEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 100
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "TRXEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 100
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRXEUR"

    def __str__(self):
        return "TRXEUR"

    def __call__(self):
        return "TRXEUR"


TRXEUR = TRXEUR()
"""
    name: TRXEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 100
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class TRXUSD(NamedTuple):
    """
        name: TRXUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 100
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "TRXUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 100
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRXUSD"

    def __str__(self):
        return "TRXUSD"

    def __call__(self):
        return "TRXUSD"


TRXUSD = TRXUSD()
"""
    name: TRXUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 100
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class TRXXBT(NamedTuple):
    """
        name: TRXXBT
        significant_digits: None
        tick_size: 0.0000000001
        min_margin: None
        initial_margin: None
        min_order_size: 100
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "TRXXBT"
    significant_digits: int = None
    tick_size: int = 0.0000000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 100
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRXXBT"

    def __str__(self):
        return "TRXXBT"

    def __call__(self):
        return "TRXXBT"


TRXXBT = TRXXBT()
"""
    name: TRXXBT
    significant_digits: None
    tick_size: 0.0000000001
    min_margin: None
    initial_margin: None
    min_order_size: 100
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class TUSD(NamedTuple):
    """
        name: TUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 130
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 130
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TUSD"

    def __str__(self):
        return "TUSD"

    def __call__(self):
        return "TUSD"


TUSD = TUSD()
"""
    name: TUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 130
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TVKEUR(NamedTuple):
    """
        name: TVKEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 110
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TVKEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 110
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TVKEUR"

    def __str__(self):
        return "TVKEUR"

    def __call__(self):
        return "TVKEUR"


TVKEUR = TVKEUR()
"""
    name: TVKEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 110
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class TVKUSD(NamedTuple):
    """
        name: TVKUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 110
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "TVKUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 110
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TVKUSD"

    def __str__(self):
        return "TVKUSD"

    def __call__(self):
        return "TVKUSD"


TVKUSD = TVKUSD()
"""
    name: TVKUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 110
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class UMAEUR(NamedTuple):
    """
        name: UMAEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "UMAEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UMAEUR"

    def __str__(self):
        return "UMAEUR"

    def __call__(self):
        return "UMAEUR"


UMAEUR = UMAEUR()
"""
    name: UMAEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class UMAUSD(NamedTuple):
    """
        name: UMAUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 3
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "UMAUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 3
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UMAUSD"

    def __str__(self):
        return "UMAUSD"

    def __call__(self):
        return "UMAUSD"


UMAUSD = UMAUSD()
"""
    name: UMAUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 3
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class UNFIEUR(NamedTuple):
    """
        name: UNFIEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "UNFIEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNFIEUR"

    def __str__(self):
        return "UNFIEUR"

    def __call__(self):
        return "UNFIEUR"


UNFIEUR = UNFIEUR()
"""
    name: UNFIEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class UNFIUSD(NamedTuple):
    """
        name: UNFIUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "UNFIUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNFIUSD"

    def __str__(self):
        return "UNFIUSD"

    def __call__(self):
        return "UNFIUSD"


UNFIUSD = UNFIUSD()
"""
    name: UNFIUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class UNIETH(NamedTuple):
    """
        name: UNIETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "UNIETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNIETH"

    def __str__(self):
        return "UNIETH"

    def __call__(self):
        return "UNIETH"


UNIETH = UNIETH()
"""
    name: UNIETH
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class UNIEUR(NamedTuple):
    """
        name: UNIEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "UNIEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNIEUR"

    def __str__(self):
        return "UNIEUR"

    def __call__(self):
        return "UNIEUR"


UNIEUR = UNIEUR()
"""
    name: UNIEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class UNIUSD(NamedTuple):
    """
        name: UNIUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "UNIUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNIUSD"

    def __str__(self):
        return "UNIUSD"

    def __call__(self):
        return "UNIUSD"


UNIUSD = UNIUSD()
"""
    name: UNIUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class UNIXBT(NamedTuple):
    """
        name: UNIXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "UNIXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNIXBT"

    def __str__(self):
        return "UNIXBT"

    def __call__(self):
        return "UNIXBT"


UNIXBT = UNIXBT()
"""
    name: UNIXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class USDAED(NamedTuple):
    """
        name: USDAED
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USDAED"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDAED"

    def __str__(self):
        return "USDAED"

    def __call__(self):
        return "USDAED"


USDAED = USDAED()
"""
    name: USDAED
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class USDCAUD(NamedTuple):
    """
        name: USDCAUD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDCAUD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDCAUD"

    def __str__(self):
        return "USDCAUD"

    def __call__(self):
        return "USDCAUD"


USDCAUD = USDCAUD()
"""
    name: USDCAUD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDCCAD(NamedTuple):
    """
        name: USDCCAD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USDCCAD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDCCAD"

    def __str__(self):
        return "USDCCAD"

    def __call__(self):
        return "USDCCAD"


USDCCAD = USDCCAD()
"""
    name: USDCCAD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class USDCCHF(NamedTuple):
    """
        name: USDCCHF
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USDCCHF"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDCCHF"

    def __str__(self):
        return "USDCCHF"

    def __call__(self):
        return "USDCCHF"


USDCCHF = USDCCHF()
"""
    name: USDCCHF
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class USDCEUR(NamedTuple):
    """
        name: USDCEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDCEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDCEUR"

    def __str__(self):
        return "USDCEUR"

    def __call__(self):
        return "USDCEUR"


USDCEUR = USDCEUR()
"""
    name: USDCEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDCGBP(NamedTuple):
    """
        name: USDCGBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDCGBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDCGBP"

    def __str__(self):
        return "USDCGBP"

    def __call__(self):
        return "USDCGBP"


USDCGBP = USDCGBP()
"""
    name: USDCGBP
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDCHF(NamedTuple):
    """
        name: USDCHF
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USDCHF"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDCHF"

    def __str__(self):
        return "USDCHF"

    def __call__(self):
        return "USDCHF"


USDCHF = USDCHF()
"""
    name: USDCHF
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class USDCUSD(NamedTuple):
    """
        name: USDCUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDCUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDCUSD"

    def __str__(self):
        return "USDCUSD"

    def __call__(self):
        return "USDCUSD"


USDCUSD = USDCUSD()
"""
    name: USDCUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDCUSDT(NamedTuple):
    """
        name: USDCUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDCUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDCUSDT"

    def __str__(self):
        return "USDCUSDT"

    def __call__(self):
        return "USDCUSDT"


USDCUSDT = USDCUSDT()
"""
    name: USDCUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDTAUD(NamedTuple):
    """
        name: USDTAUD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDTAUD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDTAUD"

    def __str__(self):
        return "USDTAUD"

    def __call__(self):
        return "USDTAUD"


USDTAUD = USDTAUD()
"""
    name: USDTAUD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDTCAD(NamedTuple):
    """
        name: USDTCAD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDTCAD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDTCAD"

    def __str__(self):
        return "USDTCAD"

    def __call__(self):
        return "USDTCAD"


USDTCAD = USDTCAD()
"""
    name: USDTCAD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDTCHF(NamedTuple):
    """
        name: USDTCHF
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDTCHF"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDTCHF"

    def __str__(self):
        return "USDTCHF"

    def __call__(self):
        return "USDTCHF"


USDTCHF = USDTCHF()
"""
    name: USDTCHF
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDTEUR(NamedTuple):
    """
        name: USDTEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDTEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDTEUR"

    def __str__(self):
        return "USDTEUR"

    def __call__(self):
        return "USDTEUR"


USDTEUR = USDTEUR()
"""
    name: USDTEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDTGBP(NamedTuple):
    """
        name: USDTGBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDTGBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDTGBP"

    def __str__(self):
        return "USDTGBP"

    def __call__(self):
        return "USDTGBP"


USDTGBP = USDTGBP()
"""
    name: USDTGBP
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDTJPY(NamedTuple):
    """
        name: USDTJPY
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDTJPY"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDTJPY"

    def __str__(self):
        return "USDTJPY"

    def __call__(self):
        return "USDTJPY"


USDTJPY = USDTJPY()
"""
    name: USDTJPY
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USDTZUSD(NamedTuple):
    """
        name: USDTUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "USDTUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDTUSD"

    def __str__(self):
        return "USDTUSD"

    def __call__(self):
        return "USDTUSD"


USDTZUSD = USDTZUSD()
"""
    name: USDTUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class USTEUR(NamedTuple):
    """
        name: USTEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 175
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USTEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 175
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USTEUR"

    def __str__(self):
        return "USTEUR"

    def __call__(self):
        return "USTEUR"


USTEUR = USTEUR()
"""
    name: USTEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 175
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class USTUSD(NamedTuple):
    """
        name: USTUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 175
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USTUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 175
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USTUSD"

    def __str__(self):
        return "USTUSD"

    def __call__(self):
        return "USTUSD"


USTUSD = USTUSD()
"""
    name: USTUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 175
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class USTUSDC(NamedTuple):
    """
        name: USTUSDC
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 175
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USTUSDC"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 175
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USTUSDC"

    def __str__(self):
        return "USTUSDC"

    def __call__(self):
        return "USTUSDC"


USTUSDC = USTUSDC()
"""
    name: USTUSDC
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 175
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class USTUSDT(NamedTuple):
    """
        name: USTUSDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 175
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USTUSDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 175
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USTUSDT"

    def __str__(self):
        return "USTUSDT"

    def __call__(self):
        return "USTUSDT"


USTUSDT = USTUSDT()
"""
    name: USTUSDT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 175
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class WAVESETH(NamedTuple):
    """
        name: WAVESETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "WAVESETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WAVESETH"

    def __str__(self):
        return "WAVESETH"

    def __call__(self):
        return "WAVESETH"


WAVESETH = WAVESETH()
"""
    name: WAVESETH
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class WAVESEUR(NamedTuple):
    """
        name: WAVESEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "WAVESEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WAVESEUR"

    def __str__(self):
        return "WAVESEUR"

    def __call__(self):
        return "WAVESEUR"


WAVESEUR = WAVESEUR()
"""
    name: WAVESEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class WAVESUSD(NamedTuple):
    """
        name: WAVESUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "WAVESUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WAVESUSD"

    def __str__(self):
        return "WAVESUSD"

    def __call__(self):
        return "WAVESUSD"


WAVESUSD = WAVESUSD()
"""
    name: WAVESUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class WAVESXBT(NamedTuple):
    """
        name: WAVESXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 2.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "WAVESXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 2.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WAVESXBT"

    def __str__(self):
        return "WAVESXBT"

    def __call__(self):
        return "WAVESXBT"


WAVESXBT = WAVESXBT()
"""
    name: WAVESXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 2.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class WAXLEUR(NamedTuple):
    """
        name: WAXLEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 7
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "WAXLEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WAXLEUR"

    def __str__(self):
        return "WAXLEUR"

    def __call__(self):
        return "WAXLEUR"


WAXLEUR = WAXLEUR()
"""
    name: WAXLEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 7
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class WAXLUSD(NamedTuple):
    """
        name: WAXLUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 7
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "WAXLUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 7
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WAXLUSD"

    def __str__(self):
        return "WAXLUSD"

    def __call__(self):
        return "WAXLUSD"


WAXLUSD = WAXLUSD()
"""
    name: WAXLUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 7
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class WBTCEUR(NamedTuple):
    """
        name: WBTCEUR
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.00025
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "WBTCEUR"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00025
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WBTCEUR"

    def __str__(self):
        return "WBTCEUR"

    def __call__(self):
        return "WBTCEUR"


WBTCEUR = WBTCEUR()
"""
    name: WBTCEUR
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.00025
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class WBTCUSD(NamedTuple):
    """
        name: WBTCUSD
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.00025
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "WBTCUSD"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00025
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WBTCUSD"

    def __str__(self):
        return "WBTCUSD"

    def __call__(self):
        return "WBTCUSD"


WBTCUSD = WBTCUSD()
"""
    name: WBTCUSD
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.00025
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class WBTCXBT(NamedTuple):
    """
        name: WBTCXBT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.00025
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "WBTCXBT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.00025
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WBTCXBT"

    def __str__(self):
        return "WBTCXBT"

    def __call__(self):
        return "WBTCXBT"


WBTCXBT = WBTCXBT()
"""
    name: WBTCXBT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.00025
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class WOOEUR(NamedTuple):
    """
        name: WOOEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "WOOEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WOOEUR"

    def __str__(self):
        return "WOOEUR"

    def __call__(self):
        return "WOOEUR"


WOOEUR = WOOEUR()
"""
    name: WOOEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class WOOUSD(NamedTuple):
    """
        name: WOOUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "WOOUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WOOUSD"

    def __str__(self):
        return "WOOUSD"

    def __call__(self):
        return "WOOUSD"


WOOUSD = WOOUSD()
"""
    name: WOOUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XBTAED(NamedTuple):
    """
        name: XBTAED
        significant_digits: None
        tick_size: 1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XBTAED"
    significant_digits: int = None
    tick_size: int = 1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTAED"

    def __str__(self):
        return "XBTAED"

    def __call__(self):
        return "XBTAED"


XBTAED = XBTAED()
"""
    name: XBTAED
    significant_digits: None
    tick_size: 1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XBTAUD(NamedTuple):
    """
        name: XBTAUD
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XBTAUD"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTAUD"

    def __str__(self):
        return "XBTAUD"

    def __call__(self):
        return "XBTAUD"


XBTAUD = XBTAUD()
"""
    name: XBTAUD
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XBTCHF(NamedTuple):
    """
        name: XBTCHF
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XBTCHF"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTCHF"

    def __str__(self):
        return "XBTCHF"

    def __call__(self):
        return "XBTCHF"


XBTCHF = XBTCHF()
"""
    name: XBTCHF
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XBTDAI(NamedTuple):
    """
        name: XBTDAI
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XBTDAI"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTDAI"

    def __str__(self):
        return "XBTDAI"

    def __call__(self):
        return "XBTDAI"


XBTDAI = XBTDAI()
"""
    name: XBTDAI
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XBTUSDC(NamedTuple):
    """
        name: XBTUSDC
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XBTUSDC"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTUSDC"

    def __str__(self):
        return "XBTUSDC"

    def __call__(self):
        return "XBTUSDC"


XBTUSDC = XBTUSDC()
"""
    name: XBTUSDC
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XBTUSDT(NamedTuple):
    """
        name: XBTUSDT
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XBTUSDT"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTUSDT"

    def __str__(self):
        return "XBTUSDT"

    def __call__(self):
        return "XBTUSDT"


XBTUSDT = XBTUSDT()
"""
    name: XBTUSDT
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XCNEUR(NamedTuple):
    """
        name: XCNEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 300
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XCNEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 300
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XCNEUR"

    def __str__(self):
        return "XCNEUR"

    def __call__(self):
        return "XCNEUR"


XCNEUR = XCNEUR()
"""
    name: XCNEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 300
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XCNUSD(NamedTuple):
    """
        name: XCNUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 300
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XCNUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 300
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XCNUSD"

    def __str__(self):
        return "XCNUSD"

    def __call__(self):
        return "XCNUSD"


XCNUSD = XCNUSD()
"""
    name: XCNUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 300
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XDGEUR(NamedTuple):
    """
        name: XDGEUR
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XDGEUR"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XDGEUR"

    def __str__(self):
        return "XDGEUR"

    def __call__(self):
        return "XDGEUR"


XDGEUR = XDGEUR()
"""
    name: XDGEUR
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XDGUSD(NamedTuple):
    """
        name: XDGUSD
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XDGUSD"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XDGUSD"

    def __str__(self):
        return "XDGUSD"

    def __call__(self):
        return "XDGUSD"


XDGUSD = XDGUSD()
"""
    name: XDGUSD
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XDGUSDT(NamedTuple):
    """
        name: XDGUSDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XDGUSDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XDGUSDT"

    def __str__(self):
        return "XDGUSDT"

    def __call__(self):
        return "XDGUSDT"


XDGUSDT = XDGUSDT()
"""
    name: XDGUSDT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XETCXETH(NamedTuple):
    """
        name: ETCETH
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETCETH"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETCETH"

    def __str__(self):
        return "ETCETH"

    def __call__(self):
        return "ETCETH"


XETCXETH = XETCXETH()
"""
    name: ETCETH
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XETCXXBT(NamedTuple):
    """
        name: ETCXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETCXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETCXBT"

    def __str__(self):
        return "ETCXBT"

    def __call__(self):
        return "ETCXBT"


XETCXXBT = XETCXXBT()
"""
    name: ETCXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XETCZEUR(NamedTuple):
    """
        name: ETCEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETCEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETCEUR"

    def __str__(self):
        return "ETCEUR"

    def __call__(self):
        return "ETCEUR"


XETCZEUR = XETCZEUR()
"""
    name: ETCEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XETCZUSD(NamedTuple):
    """
        name: ETCUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETCUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETCUSD"

    def __str__(self):
        return "ETCUSD"

    def __call__(self):
        return "ETCUSD"


XETCZUSD = XETCZUSD()
"""
    name: ETCUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XETHXXBT(NamedTuple):
    """
        name: ETHXBT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETHXBT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHXBT"

    def __str__(self):
        return "ETHXBT"

    def __call__(self):
        return "ETHXBT"


XETHXXBT = XETHXXBT()
"""
    name: ETHXBT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XETHZCAD(NamedTuple):
    """
        name: ETHCAD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ETHCAD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHCAD"

    def __str__(self):
        return "ETHCAD"

    def __call__(self):
        return "ETHCAD"


XETHZCAD = XETHZCAD()
"""
    name: ETHCAD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XETHZEUR(NamedTuple):
    """
        name: ETHEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETHEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHEUR"

    def __str__(self):
        return "ETHEUR"

    def __call__(self):
        return "ETHEUR"


XETHZEUR = XETHZEUR()
"""
    name: ETHEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XETHZGBP(NamedTuple):
    """
        name: ETHGBP
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETHGBP"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHGBP"

    def __str__(self):
        return "ETHGBP"

    def __call__(self):
        return "ETHGBP"


XETHZGBP = XETHZGBP()
"""
    name: ETHGBP
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XETHZJPY(NamedTuple):
    """
        name: ETHJPY
        significant_digits: None
        tick_size: 1
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ETHJPY"
    significant_digits: int = None
    tick_size: int = 1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHJPY"

    def __str__(self):
        return "ETHJPY"

    def __call__(self):
        return "ETHJPY"


XETHZJPY = XETHZJPY()
"""
    name: ETHJPY
    significant_digits: None
    tick_size: 1
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XETHZUSD(NamedTuple):
    """
        name: ETHUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.01
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ETHUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.01
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHUSD"

    def __str__(self):
        return "ETHUSD"

    def __call__(self):
        return "ETHUSD"


XETHZUSD = XETHZUSD()
"""
    name: ETHUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.01
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XLTCXXBT(NamedTuple):
    """
        name: LTCXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LTCXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTCXBT"

    def __str__(self):
        return "LTCXBT"

    def __call__(self):
        return "LTCXBT"


XLTCXXBT = XLTCXXBT()
"""
    name: LTCXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XLTCZEUR(NamedTuple):
    """
        name: LTCEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LTCEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTCEUR"

    def __str__(self):
        return "LTCEUR"

    def __call__(self):
        return "LTCEUR"


XLTCZEUR = XLTCZEUR()
"""
    name: LTCEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XLTCZJPY(NamedTuple):
    """
        name: LTCJPY
        significant_digits: None
        tick_size: 1
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "LTCJPY"
    significant_digits: int = None
    tick_size: int = 1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTCJPY"

    def __str__(self):
        return "LTCJPY"

    def __call__(self):
        return "LTCJPY"


XLTCZJPY = XLTCZJPY()
"""
    name: LTCJPY
    significant_digits: None
    tick_size: 1
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XLTCZUSD(NamedTuple):
    """
        name: LTCUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.06
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "LTCUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.06
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTCUSD"

    def __str__(self):
        return "LTCUSD"

    def __call__(self):
        return "LTCUSD"


XLTCZUSD = XLTCZUSD()
"""
    name: LTCUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.06
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XMLNXETH(NamedTuple):
    """
        name: MLNETH
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MLNETH"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MLNETH"

    def __str__(self):
        return "MLNETH"

    def __call__(self):
        return "MLNETH"


XMLNXETH = XMLNXETH()
"""
    name: MLNETH
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XMLNXXBT(NamedTuple):
    """
        name: MLNXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MLNXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MLNXBT"

    def __str__(self):
        return "MLNXBT"

    def __call__(self):
        return "MLNXBT"


XMLNXXBT = XMLNXXBT()
"""
    name: MLNXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XMLNZEUR(NamedTuple):
    """
        name: MLNEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MLNEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MLNEUR"

    def __str__(self):
        return "MLNEUR"

    def __call__(self):
        return "MLNEUR"


XMLNZEUR = XMLNZEUR()
"""
    name: MLNEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XMLNZUSD(NamedTuple):
    """
        name: MLNUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "MLNUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MLNUSD"

    def __str__(self):
        return "MLNUSD"

    def __call__(self):
        return "MLNUSD"


XMLNZUSD = XMLNZUSD()
"""
    name: MLNUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XMRUSDT(NamedTuple):
    """
        name: XMRUSDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.035
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XMRUSDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.035
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XMRUSDT"

    def __str__(self):
        return "XMRUSDT"

    def __call__(self):
        return "XMRUSDT"


XMRUSDT = XMRUSDT()
"""
    name: XMRUSDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.035
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XREPXXBT(NamedTuple):
    """
        name: REPXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "REPXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REPXBT"

    def __str__(self):
        return "REPXBT"

    def __call__(self):
        return "REPXBT"


XREPXXBT = XREPXXBT()
"""
    name: REPXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XREPZEUR(NamedTuple):
    """
        name: REPEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "REPEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REPEUR"

    def __str__(self):
        return "REPEUR"

    def __call__(self):
        return "REPEUR"


XREPZEUR = XREPZEUR()
"""
    name: REPEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XREPZUSD(NamedTuple):
    """
        name: REPUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "REPUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REPUSD"

    def __str__(self):
        return "REPUSD"

    def __call__(self):
        return "REPUSD"


XREPZUSD = XREPZUSD()
"""
    name: REPUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XRPAUD(NamedTuple):
    """
        name: XRPAUD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XRPAUD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPAUD"

    def __str__(self):
        return "XRPAUD"

    def __call__(self):
        return "XRPAUD"


XRPAUD = XRPAUD()
"""
    name: XRPAUD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XRPETH(NamedTuple):
    """
        name: XRPETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XRPETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPETH"

    def __str__(self):
        return "XRPETH"

    def __call__(self):
        return "XRPETH"


XRPETH = XRPETH()
"""
    name: XRPETH
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XRPGBP(NamedTuple):
    """
        name: XRPGBP
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XRPGBP"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPGBP"

    def __str__(self):
        return "XRPGBP"

    def __call__(self):
        return "XRPGBP"


XRPGBP = XRPGBP()
"""
    name: XRPGBP
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XRPUSDT(NamedTuple):
    """
        name: XRPUSDT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XRPUSDT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPUSDT"

    def __str__(self):
        return "XRPUSDT"

    def __call__(self):
        return "XRPUSDT"


XRPUSDT = XRPUSDT()
"""
    name: XRPUSDT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XRTEUR(NamedTuple):
    """
        name: XRTEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XRTEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRTEUR"

    def __str__(self):
        return "XRTEUR"

    def __call__(self):
        return "XRTEUR"


XRTEUR = XRTEUR()
"""
    name: XRTEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XRTUSD(NamedTuple):
    """
        name: XRTUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 1
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XRTUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 1
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRTUSD"

    def __str__(self):
        return "XRTUSD"

    def __call__(self):
        return "XRTUSD"


XRTUSD = XRTUSD()
"""
    name: XRTUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 1
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XTZAUD(NamedTuple):
    """
        name: XTZAUD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XTZAUD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZAUD"

    def __str__(self):
        return "XTZAUD"

    def __call__(self):
        return "XTZAUD"


XTZAUD = XTZAUD()
"""
    name: XTZAUD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XTZETH(NamedTuple):
    """
        name: XTZETH
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XTZETH"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZETH"

    def __str__(self):
        return "XTZETH"

    def __call__(self):
        return "XTZETH"


XTZETH = XTZETH()
"""
    name: XTZETH
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XTZEUR(NamedTuple):
    """
        name: XTZEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XTZEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZEUR"

    def __str__(self):
        return "XTZEUR"

    def __call__(self):
        return "XTZEUR"


XTZEUR = XTZEUR()
"""
    name: XTZEUR
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XTZGBP(NamedTuple):
    """
        name: XTZGBP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XTZGBP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZGBP"

    def __str__(self):
        return "XTZGBP"

    def __call__(self):
        return "XTZGBP"


XTZGBP = XTZGBP()
"""
    name: XTZGBP
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XTZUSD(NamedTuple):
    """
        name: XTZUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XTZUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZUSD"

    def __str__(self):
        return "XTZUSD"

    def __call__(self):
        return "XTZUSD"


XTZUSD = XTZUSD()
"""
    name: XTZUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XTZUSDT(NamedTuple):
    """
        name: XTZUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XTZUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZUSDT"

    def __str__(self):
        return "XTZUSDT"

    def __call__(self):
        return "XTZUSDT"


XTZUSDT = XTZUSDT()
"""
    name: XTZUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XTZXBT(NamedTuple):
    """
        name: XTZXBT
        significant_digits: None
        tick_size: 0.0000001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XTZXBT"
    significant_digits: int = None
    tick_size: int = 0.0000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZXBT"

    def __str__(self):
        return "XTZXBT"

    def __call__(self):
        return "XTZXBT"


XTZXBT = XTZXBT()
"""
    name: XTZXBT
    significant_digits: None
    tick_size: 0.0000001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXBTZCAD(NamedTuple):
    """
        name: XBTCAD
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XBTCAD"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTCAD"

    def __str__(self):
        return "XBTCAD"

    def __call__(self):
        return "XBTCAD"


XXBTZCAD = XXBTZCAD()
"""
    name: XBTCAD
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXBTZEUR(NamedTuple):
    """
        name: XBTEUR
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XBTEUR"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTEUR"

    def __str__(self):
        return "XBTEUR"

    def __call__(self):
        return "XBTEUR"


XXBTZEUR = XXBTZEUR()
"""
    name: XBTEUR
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXBTZGBP(NamedTuple):
    """
        name: XBTGBP
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XBTGBP"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTGBP"

    def __str__(self):
        return "XBTGBP"

    def __call__(self):
        return "XBTGBP"


XXBTZGBP = XXBTZGBP()
"""
    name: XBTGBP
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXBTZJPY(NamedTuple):
    """
        name: XBTJPY
        significant_digits: None
        tick_size: 1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XBTJPY"
    significant_digits: int = None
    tick_size: int = 1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTJPY"

    def __str__(self):
        return "XBTJPY"

    def __call__(self):
        return "XBTJPY"


XXBTZJPY = XXBTZJPY()
"""
    name: XBTJPY
    significant_digits: None
    tick_size: 1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XXBTZUSD(NamedTuple):
    """
        name: XBTUSD
        significant_digits: None
        tick_size: 0.1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0001
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XBTUSD"
    significant_digits: int = None
    tick_size: int = 0.1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0001
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTUSD"

    def __str__(self):
        return "XBTUSD"

    def __call__(self):
        return "XBTUSD"


XXBTZUSD = XXBTZUSD()
"""
    name: XBTUSD
    significant_digits: None
    tick_size: 0.1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0001
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXDGXXBT(NamedTuple):
    """
        name: XDGXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XDGXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XDGXBT"

    def __str__(self):
        return "XDGXBT"

    def __call__(self):
        return "XDGXBT"


XXDGXXBT = XXDGXXBT()
"""
    name: XDGXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXLMXXBT(NamedTuple):
    """
        name: XLMXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XLMXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLMXBT"

    def __str__(self):
        return "XLMXBT"

    def __call__(self):
        return "XLMXBT"


XXLMXXBT = XXLMXXBT()
"""
    name: XLMXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXLMZEUR(NamedTuple):
    """
        name: XLMEUR
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XLMEUR"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLMEUR"

    def __str__(self):
        return "XLMEUR"

    def __call__(self):
        return "XLMEUR"


XXLMZEUR = XXLMZEUR()
"""
    name: XLMEUR
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXLMZGBP(NamedTuple):
    """
        name: XLMGBP
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XLMGBP"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLMGBP"

    def __str__(self):
        return "XLMGBP"

    def __call__(self):
        return "XLMGBP"


XXLMZGBP = XXLMZGBP()
"""
    name: XLMGBP
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XXLMZUSD(NamedTuple):
    """
        name: XLMUSD
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 60
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XLMUSD"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 60
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLMUSD"

    def __str__(self):
        return "XLMUSD"

    def __call__(self):
        return "XLMUSD"


XXLMZUSD = XXLMZUSD()
"""
    name: XLMUSD
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 60
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXMRXXBT(NamedTuple):
    """
        name: XMRXBT
        significant_digits: None
        tick_size: 0.000001
        min_margin: None
        initial_margin: None
        min_order_size: 0.035
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XMRXBT"
    significant_digits: int = None
    tick_size: int = 0.000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.035
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XMRXBT"

    def __str__(self):
        return "XMRXBT"

    def __call__(self):
        return "XMRXBT"


XXMRXXBT = XXMRXXBT()
"""
    name: XMRXBT
    significant_digits: None
    tick_size: 0.000001
    min_margin: None
    initial_margin: None
    min_order_size: 0.035
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXMRZEUR(NamedTuple):
    """
        name: XMREUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.035
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XMREUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.035
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XMREUR"

    def __str__(self):
        return "XMREUR"

    def __call__(self):
        return "XMREUR"


XXMRZEUR = XXMRZEUR()
"""
    name: XMREUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.035
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXMRZUSD(NamedTuple):
    """
        name: XMRUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.035
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XMRUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.035
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XMRUSD"

    def __str__(self):
        return "XMRUSD"

    def __call__(self):
        return "XMRUSD"


XXMRZUSD = XXMRZUSD()
"""
    name: XMRUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.035
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXRPXXBT(NamedTuple):
    """
        name: XRPXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XRPXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPXBT"

    def __str__(self):
        return "XRPXBT"

    def __call__(self):
        return "XRPXBT"


XXRPXXBT = XXRPXXBT()
"""
    name: XRPXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXRPZCAD(NamedTuple):
    """
        name: XRPCAD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XRPCAD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPCAD"

    def __str__(self):
        return "XRPCAD"

    def __call__(self):
        return "XRPCAD"


XXRPZCAD = XXRPZCAD()
"""
    name: XRPCAD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XXRPZEUR(NamedTuple):
    """
        name: XRPEUR
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XRPEUR"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPEUR"

    def __str__(self):
        return "XRPEUR"

    def __call__(self):
        return "XRPEUR"


XXRPZEUR = XXRPZEUR()
"""
    name: XRPEUR
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XXRPZJPY(NamedTuple):
    """
        name: XRPJPY
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "XRPJPY"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPJPY"

    def __str__(self):
        return "XRPJPY"

    def __call__(self):
        return "XRPJPY"


XXRPZJPY = XXRPZJPY()
"""
    name: XRPJPY
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class XXRPZUSD(NamedTuple):
    """
        name: XRPUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "XRPUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPUSD"

    def __str__(self):
        return "XRPUSD"

    def __call__(self):
        return "XRPUSD"


XXRPZUSD = XXRPZUSD()
"""
    name: XRPUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XZECXXBT(NamedTuple):
    """
        name: ZECXBT
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ZECXBT"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZECXBT"

    def __str__(self):
        return "ZECXBT"

    def __call__(self):
        return "ZECXBT"


XZECXXBT = XZECXXBT()
"""
    name: ZECXBT
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XZECZEUR(NamedTuple):
    """
        name: ZECEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 0.15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ZECEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZECEUR"

    def __str__(self):
        return "ZECEUR"

    def __call__(self):
        return "ZECEUR"


XZECZEUR = XZECZEUR()
"""
    name: ZECEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 0.15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class XZECZUSD(NamedTuple):
    """
        name: ZECUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: 0.15
        max_order_size: None
        has_margin: True
        exchange: kraken
    """
    name: str = "ZECUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.15
    max_order_size: float = None
    has_margin: bool = True
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZECUSD"

    def __str__(self):
        return "ZECUSD"

    def __call__(self):
        return "ZECUSD"


XZECZUSD = XZECZUSD()
"""
    name: ZECUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: 0.15
    max_order_size: None
    has_margin: True
    exchange: kraken
"""


class YFIEUR(NamedTuple):
    """
        name: YFIEUR
        significant_digits: None
        tick_size: 1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0007
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "YFIEUR"
    significant_digits: int = None
    tick_size: int = 1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0007
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YFIEUR"

    def __str__(self):
        return "YFIEUR"

    def __call__(self):
        return "YFIEUR"


YFIEUR = YFIEUR()
"""
    name: YFIEUR
    significant_digits: None
    tick_size: 1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0007
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class YFIUSD(NamedTuple):
    """
        name: YFIUSD
        significant_digits: None
        tick_size: 1
        min_margin: None
        initial_margin: None
        min_order_size: 0.0007
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "YFIUSD"
    significant_digits: int = None
    tick_size: int = 1
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0007
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YFIUSD"

    def __str__(self):
        return "YFIUSD"

    def __call__(self):
        return "YFIUSD"


YFIUSD = YFIUSD()
"""
    name: YFIUSD
    significant_digits: None
    tick_size: 1
    min_margin: None
    initial_margin: None
    min_order_size: 0.0007
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class YFIXBT(NamedTuple):
    """
        name: YFIXBT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.0007
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "YFIXBT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.0007
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YFIXBT"

    def __str__(self):
        return "YFIXBT"

    def __call__(self):
        return "YFIXBT"


YFIXBT = YFIXBT()
"""
    name: YFIXBT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: 0.0007
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class YGGEUR(NamedTuple):
    """
        name: YGGEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 17.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "YGGEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 17.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YGGEUR"

    def __str__(self):
        return "YGGEUR"

    def __call__(self):
        return "YGGEUR"


YGGEUR = YGGEUR()
"""
    name: YGGEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 17.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class YGGUSD(NamedTuple):
    """
        name: YGGUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 17.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "YGGUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 17.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YGGUSD"

    def __str__(self):
        return "YGGUSD"

    def __call__(self):
        return "YGGUSD"


YGGUSD = YGGUSD()
"""
    name: YGGUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 17.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ZEURZUSD(NamedTuple):
    """
        name: EURUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 0.5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EURUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "EURUSD"

    def __str__(self):
        return "EURUSD"

    def __call__(self):
        return "EURUSD"


ZEURZUSD = ZEURZUSD()
"""
    name: EURUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 0.5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ZGBPZUSD(NamedTuple):
    """
        name: GBPUSD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "GBPUSD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GBPUSD"

    def __str__(self):
        return "GBPUSD"

    def __call__(self):
        return "GBPUSD"


ZGBPZUSD = ZGBPZUSD()
"""
    name: GBPUSD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ZRXEUR(NamedTuple):
    """
        name: ZRXEUR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ZRXEUR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZRXEUR"

    def __str__(self):
        return "ZRXEUR"

    def __call__(self):
        return "ZRXEUR"


ZRXEUR = ZRXEUR()
"""
    name: ZRXEUR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ZRXUSD(NamedTuple):
    """
        name: ZRXUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ZRXUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZRXUSD"

    def __str__(self):
        return "ZRXUSD"

    def __call__(self):
        return "ZRXUSD"


ZRXUSD = ZRXUSD()
"""
    name: ZRXUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ZRXXBT(NamedTuple):
    """
        name: ZRXXBT
        significant_digits: None
        tick_size: 0.00000001
        min_margin: None
        initial_margin: None
        min_order_size: 25
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "ZRXXBT"
    significant_digits: int = None
    tick_size: int = 0.00000001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 25
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZRXXBT"

    def __str__(self):
        return "ZRXXBT"

    def __call__(self):
        return "ZRXXBT"


ZRXXBT = ZRXXBT()
"""
    name: ZRXXBT
    significant_digits: None
    tick_size: 0.00000001
    min_margin: None
    initial_margin: None
    min_order_size: 25
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ZUSDZCAD(NamedTuple):
    """
        name: USDCAD
        significant_digits: None
        tick_size: 0.00001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USDCAD"
    significant_digits: int = None
    tick_size: int = 0.00001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDCAD"

    def __str__(self):
        return "USDCAD"

    def __call__(self):
        return "USDCAD"


ZUSDZCAD = ZUSDZCAD()
"""
    name: USDCAD
    significant_digits: None
    tick_size: 0.00001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""


class ZUSDZJPY(NamedTuple):
    """
        name: USDJPY
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "USDJPY"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 5
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDJPY"

    def __str__(self):
        return "USDJPY"

    def __call__(self):
        return "USDJPY"


ZUSDZJPY = ZUSDZJPY()
"""
    name: USDJPY
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: 5
    max_order_size: None
    has_margin: False
    exchange: kraken
"""
