from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ONEINCHEUR:
    """
        name: 1INCHEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "1INCHEUR"
    precision: int = 0.001
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
        return "1INCHEUR"

    def __str__(self):
        return "1INCHEUR"

    def __call__(self):
        return "1INCHEUR"


ONEINCHEUR = ONEINCHEUR()
"""
    name: 1INCHEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ONEINCHUSD:
    """
        name: 1INCHUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "1INCHUSD"
    precision: int = 0.001
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
        return "1INCHUSD"

    def __str__(self):
        return "1INCHUSD"

    def __call__(self):
        return "1INCHUSD"


ONEINCHUSD = ONEINCHUSD()
"""
    name: 1INCHUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AAVEAUD:
    """
        name: AAVEAUD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: False
    """
    name: str = "AAVEAUD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVEAUD"

    def __str__(self):
        return "AAVEAUD"

    def __call__(self):
        return "AAVEAUD"


AAVEAUD = AAVEAUD()
"""
    name: AAVEAUD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AAVEETH:
    """
        name: AAVEETH
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: False
    """
    name: str = "AAVEETH"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AAVEEUR:
    """
        name: AAVEEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: True
    """
    name: str = "AAVEEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AAVEGBP:
    """
        name: AAVEGBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: False
    """
    name: str = "AAVEGBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AAVEUSD:
    """
        name: AAVEUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: True
    """
    name: str = "AAVEUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AAVEXBT:
    """
        name: AAVEXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: False
    """
    name: str = "AAVEXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ACAEUR:
    """
        name: ACAEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "ACAEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ACAUSD:
    """
        name: ACAUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "ACAUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ACHEUR:
    """
        name: ACHEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500
        maximum_order_size: None
        margin: False
    """
    name: str = "ACHEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ACHUSD:
    """
        name: ACHUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500
        maximum_order_size: None
        margin: False
    """
    name: str = "ACHUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ADAAUD:
    """
        name: ADAAUD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "ADAAUD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ADAETH:
    """
        name: ADAETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: True
    """
    name: str = "ADAETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ADAEUR:
    """
        name: ADAEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: True
    """
    name: str = "ADAEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ADAGBP:
    """
        name: ADAGBP
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "ADAGBP"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ADAUSD:
    """
        name: ADAUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: True
    """
    name: str = "ADAUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ADAUSDT:
    """
        name: ADAUSDT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: True
    """
    name: str = "ADAUSDT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ADAXBT:
    """
        name: ADAXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: True
    """
    name: str = "ADAXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ADXEUR:
    """
        name: ADXEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 40
        maximum_order_size: None
        margin: False
    """
    name: str = "ADXEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 40
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 40
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ADXUSD:
    """
        name: ADXUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 40
        maximum_order_size: None
        margin: False
    """
    name: str = "ADXUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 40
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 40
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AGLDEUR:
    """
        name: AGLDEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "AGLDEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AGLDUSD:
    """
        name: AGLDUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "AGLDUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AIREUR:
    """
        name: AIREUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 700
        maximum_order_size: None
        margin: False
    """
    name: str = "AIREUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 700
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 700
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AIRUSD:
    """
        name: AIRUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 700
        maximum_order_size: None
        margin: False
    """
    name: str = "AIRUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 700
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 700
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AKTEUR:
    """
        name: AKTEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "AKTEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AKTUSD:
    """
        name: AKTUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "AKTUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ALCXEUR:
    """
        name: ALCXEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.3
        maximum_order_size: None
        margin: False
    """
    name: str = "ALCXEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ALCXUSD:
    """
        name: ALCXUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.3
        maximum_order_size: None
        margin: False
    """
    name: str = "ALCXUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ALGOETH:
    """
        name: ALGOETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "ALGOETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ALGOEUR:
    """
        name: ALGOEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: True
    """
    name: str = "ALGOEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ALGOGBP:
    """
        name: ALGOGBP
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "ALGOGBP"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ALGOUSD:
    """
        name: ALGOUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: True
    """
    name: str = "ALGOUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ALGOUSDT:
    """
        name: ALGOUSDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "ALGOUSDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ALGOXBT:
    """
        name: ALGOXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: True
    """
    name: str = "ALGOXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ALICEEUR:
    """
        name: ALICEEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "ALICEEUR"
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
        return "ALICEEUR"

    def __str__(self):
        return "ALICEEUR"

    def __call__(self):
        return "ALICEEUR"


ALICEEUR = ALICEEUR()
"""
    name: ALICEEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ALICEUSD:
    """
        name: ALICEUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "ALICEUSD"
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
        return "ALICEUSD"

    def __str__(self):
        return "ALICEUSD"

    def __call__(self):
        return "ALICEUSD"


ALICEUSD = ALICEUSD()
"""
    name: ALICEUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ALPHAEUR:
    """
        name: ALPHAEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "ALPHAEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ALPHAUSD:
    """
        name: ALPHAUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "ALPHAUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ANKREUR:
    """
        name: ANKREUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "ANKREUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ANKRGBP:
    """
        name: ANKRGBP
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "ANKRGBP"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANKRGBP"

    def __str__(self):
        return "ANKRGBP"

    def __call__(self):
        return "ANKRGBP"


ANKRGBP = ANKRGBP()
"""
    name: ANKRGBP
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ANKRUSD:
    """
        name: ANKRUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "ANKRUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ANKRXBT:
    """
        name: ANKRXBT
        precision: 0.000000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "ANKRXBT"
    precision: int = 0.000000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ANTETH:
    """
        name: ANTETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ANTETH"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ANTEUR:
    """
        name: ANTEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ANTEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ANTUSD:
    """
        name: ANTUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ANTUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ANTXBT:
    """
        name: ANTXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ANTXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class APEEUR:
    """
        name: APEEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: True
    """
    name: str = "APEEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class APEUSD:
    """
        name: APEUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: True
    """
    name: str = "APEUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class APEUSDT:
    """
        name: APEUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "APEUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class API3EUR:
    """
        name: API3EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3.5
        maximum_order_size: None
        margin: False
    """
    name: str = "API3EUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class API3USD:
    """
        name: API3USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3.5
        maximum_order_size: None
        margin: False
    """
    name: str = "API3USD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class APTEUR:
    """
        name: APTEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: False
    """
    name: str = "APTEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class APTUSD:
    """
        name: APTUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: False
    """
    name: str = "APTUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ARPAEUR:
    """
        name: ARPAEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "ARPAEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ARPAUSD:
    """
        name: ARPAUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "ARPAUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ASTREUR:
    """
        name: ASTREUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 125
        maximum_order_size: None
        margin: False
    """
    name: str = "ASTREUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 125
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 125
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ASTRUSD:
    """
        name: ASTRUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 125
        maximum_order_size: None
        margin: False
    """
    name: str = "ASTRUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 125
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 125
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ATLASEUR:
    """
        name: ATLASEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: False
    """
    name: str = "ATLASEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ATLASUSD:
    """
        name: ATLASUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: False
    """
    name: str = "ATLASUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ATOMAUD:
    """
        name: ATOMAUD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOMAUD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.5
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOMAUD"

    def __str__(self):
        return "ATOMAUD"

    def __call__(self):
        return "ATOMAUD"


ATOMAUD = ATOMAUD()
"""
    name: ATOMAUD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ATOMETH:
    """
        name: ATOMETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOMETH"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ATOMEUR:
    """
        name: ATOMEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.5
        maximum_order_size: None
        margin: True
    """
    name: str = "ATOMEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ATOMGBP:
    """
        name: ATOMGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOMGBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ATOMUSD:
    """
        name: ATOMUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.5
        maximum_order_size: None
        margin: True
    """
    name: str = "ATOMUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ATOMUSDT:
    """
        name: ATOMUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOMUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ATOMXBT:
    """
        name: ATOMXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.5
        maximum_order_size: None
        margin: True
    """
    name: str = "ATOMXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AUDIOEUR:
    """
        name: AUDIOEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "AUDIOEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AUDIOUSD:
    """
        name: AUDIOUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "AUDIOUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AUDJPY:
    """
        name: AUDJPY
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "AUDJPY"
    precision: int = 0.001
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
        return "AUDJPY"

    def __str__(self):
        return "AUDJPY"

    def __call__(self):
        return "AUDJPY"


AUDJPY = AUDJPY()
"""
    name: AUDJPY
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AUDUSD:
    """
        name: AUDUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "AUDUSD"
    precision: int = 0.00001
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
        return "AUDUSD"

    def __str__(self):
        return "AUDUSD"

    def __call__(self):
        return "AUDUSD"


AUDUSD = AUDUSD()
"""
    name: AUDUSD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AVAXEUR:
    """
        name: AVAXEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.4
        maximum_order_size: None
        margin: True
    """
    name: str = "AVAXEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.4
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.4
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AVAXUSD:
    """
        name: AVAXUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.4
        maximum_order_size: None
        margin: True
    """
    name: str = "AVAXUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.4
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.4
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AVAXUSDT:
    """
        name: AVAXUSDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.4
        maximum_order_size: None
        margin: False
    """
    name: str = "AVAXUSDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.4
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.4
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class AXSEUR:
    """
        name: AXSEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.65
        maximum_order_size: None
        margin: True
    """
    name: str = "AXSEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.65
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.65
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AXSUSD:
    """
        name: AXSUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.65
        maximum_order_size: None
        margin: True
    """
    name: str = "AXSUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.65
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.65
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BADGEREUR:
    """
        name: BADGEREUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "BADGEREUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BADGERUSD:
    """
        name: BADGERUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "BADGERUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BALETH:
    """
        name: BALETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BALETH"
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
        return "BALETH"

    def __str__(self):
        return "BALETH"

    def __call__(self):
        return "BALETH"


BALETH = BALETH()
"""
    name: BALETH
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BALEUR:
    """
        name: BALEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BALEUR"
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
        return "BALEUR"

    def __str__(self):
        return "BALEUR"

    def __call__(self):
        return "BALEUR"


BALEUR = BALEUR()
"""
    name: BALEUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BALUSD:
    """
        name: BALUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BALUSD"
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
        return "BALUSD"

    def __str__(self):
        return "BALUSD"

    def __call__(self):
        return "BALUSD"


BALUSD = BALUSD()
"""
    name: BALUSD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BALXBT:
    """
        name: BALXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "BALXBT"
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
        return "BALXBT"

    def __str__(self):
        return "BALXBT"

    def __call__(self):
        return "BALXBT"


BALXBT = BALXBT()
"""
    name: BALXBT
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BANDEUR:
    """
        name: BANDEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "BANDEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BANDUSD:
    """
        name: BANDUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "BANDUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BATETH:
    """
        name: BATETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "BATETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BATEUR:
    """
        name: BATEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: True
    """
    name: str = "BATEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BATJPY:
    """
        name: BATJPY
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "BATJPY"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BATUSD:
    """
        name: BATUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: True
    """
    name: str = "BATUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BATXBT:
    """
        name: BATXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "BATXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BCHAUD:
    """
        name: BCHAUD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: False
    """
    name: str = "BCHAUD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BCHETH:
    """
        name: BCHETH
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: False
    """
    name: str = "BCHETH"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BCHEUR:
    """
        name: BCHEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: True
    """
    name: str = "BCHEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BCHGBP:
    """
        name: BCHGBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: False
    """
    name: str = "BCHGBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BCHJPY:
    """
        name: BCHJPY
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: False
    """
    name: str = "BCHJPY"
    precision: int = 1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BCHUSD:
    """
        name: BCHUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: True
    """
    name: str = "BCHUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BCHUSDT:
    """
        name: BCHUSDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: False
    """
    name: str = "BCHUSDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BCHXBT:
    """
        name: BCHXBT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: True
    """
    name: str = "BCHXBT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BICOEUR:
    """
        name: BICOEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 17.5
        maximum_order_size: None
        margin: False
    """
    name: str = "BICOEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 17.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 17.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BICOUSD:
    """
        name: BICOUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 17.5
        maximum_order_size: None
        margin: False
    """
    name: str = "BICOUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 17.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 17.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BITEUR:
    """
        name: BITEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 17.5
        maximum_order_size: None
        margin: False
    """
    name: str = "BITEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 17.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 17.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BITUSD:
    """
        name: BITUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 17.5
        maximum_order_size: None
        margin: False
    """
    name: str = "BITUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 17.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 17.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BLZEUR:
    """
        name: BLZEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 85
        maximum_order_size: None
        margin: False
    """
    name: str = "BLZEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 85
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 85
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BLZUSD:
    """
        name: BLZUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 85
        maximum_order_size: None
        margin: False
    """
    name: str = "BLZUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 85
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 85
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BNCEUR:
    """
        name: BNCEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "BNCEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BNCUSD:
    """
        name: BNCUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "BNCUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BNTEUR:
    """
        name: BNTEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "BNTEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BNTGBP:
    """
        name: BNTGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "BNTGBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNTGBP"

    def __str__(self):
        return "BNTGBP"

    def __call__(self):
        return "BNTGBP"


BNTGBP = BNTGBP()
"""
    name: BNTGBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BNTUSD:
    """
        name: BNTUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "BNTUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BNTXBT:
    """
        name: BNTXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "BNTXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BOBAEUR:
    """
        name: BOBAEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "BOBAEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BOBAUSD:
    """
        name: BOBAUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "BOBAUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BONDEUR:
    """
        name: BONDEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "BONDEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BONDUSD:
    """
        name: BONDUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "BONDUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BSXEUR:
    """
        name: BSXEUR
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60000
        maximum_order_size: None
        margin: False
    """
    name: str = "BSXEUR"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BSXUSD:
    """
        name: BSXUSD
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60000
        maximum_order_size: None
        margin: False
    """
    name: str = "BSXUSD"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BTTEUR:
    """
        name: BTTEUR
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7500000
        maximum_order_size: None
        margin: False
    """
    name: str = "BTTEUR"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7500000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7500000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class BTTUSD:
    """
        name: BTTUSD
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7500000
        maximum_order_size: None
        margin: False
    """
    name: str = "BTTUSD"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7500000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7500000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class C98EUR:
    """
        name: C98EUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "C98EUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class C98USD:
    """
        name: C98USD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "C98USD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CELREUR:
    """
        name: CELREUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500
        maximum_order_size: None
        margin: False
    """
    name: str = "CELREUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CELRUSD:
    """
        name: CELRUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500
        maximum_order_size: None
        margin: False
    """
    name: str = "CELRUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CFGEUR:
    """
        name: CFGEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "CFGEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CFGUSD:
    """
        name: CFGUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "CFGUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CHREUR:
    """
        name: CHREUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 40
        maximum_order_size: None
        margin: False
    """
    name: str = "CHREUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 40
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 40
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CHRUSD:
    """
        name: CHRUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 40
        maximum_order_size: None
        margin: False
    """
    name: str = "CHRUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 40
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 40
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CHZEUR:
    """
        name: CHZEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "CHZEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CHZUSD:
    """
        name: CHZUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "CHZUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class COMPETH:
    """
        name: COMPETH
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: False
    """
    name: str = "COMPETH"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COMPETH"

    def __str__(self):
        return "COMPETH"

    def __call__(self):
        return "COMPETH"


COMPETH = COMPETH()
"""
    name: COMPETH
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class COMPEUR:
    """
        name: COMPEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: True
    """
    name: str = "COMPEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class COMPUSD:
    """
        name: COMPUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: True
    """
    name: str = "COMPUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class COMPXBT:
    """
        name: COMPXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: False
    """
    name: str = "COMPXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class COTIEUR:
    """
        name: COTIEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 65
        maximum_order_size: None
        margin: False
    """
    name: str = "COTIEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class COTIUSD:
    """
        name: COTIUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 65
        maximum_order_size: None
        margin: False
    """
    name: str = "COTIUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CQTEUR:
    """
        name: CQTEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "CQTEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CQTUSD:
    """
        name: CQTUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "CQTUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CRVETH:
    """
        name: CRVETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "CRVETH"
    precision: int = 0.000001
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
        return "CRVETH"

    def __str__(self):
        return "CRVETH"

    def __call__(self):
        return "CRVETH"


CRVETH = CRVETH()
"""
    name: CRVETH
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CRVEUR:
    """
        name: CRVEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: True
    """
    name: str = "CRVEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 10
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class CRVUSD:
    """
        name: CRVUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: True
    """
    name: str = "CRVUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 10
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class CRVXBT:
    """
        name: CRVXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "CRVXBT"
    precision: int = 0.0000001
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
        return "CRVXBT"

    def __str__(self):
        return "CRVXBT"

    def __call__(self):
        return "CRVXBT"


CRVXBT = CRVXBT()
"""
    name: CRVXBT
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CSMEUR:
    """
        name: CSMEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1250
        maximum_order_size: None
        margin: False
    """
    name: str = "CSMEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CSMUSD:
    """
        name: CSMUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1250
        maximum_order_size: None
        margin: False
    """
    name: str = "CSMUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CTSIEUR:
    """
        name: CTSIEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "CTSIEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CTSIUSD:
    """
        name: CTSIUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "CTSIUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CVCEUR:
    """
        name: CVCEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "CVCEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CVCUSD:
    """
        name: CVCUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "CVCUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CVXEUR:
    """
        name: CVXEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.2
        maximum_order_size: None
        margin: False
    """
    name: str = "CVXEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class CVXUSD:
    """
        name: CVXUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.2
        maximum_order_size: None
        margin: False
    """
    name: str = "CVXUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class DAIEUR:
    """
        name: DAIEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "DAIEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DAIUSD:
    """
        name: DAIUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "DAIUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DAIUSDT:
    """
        name: DAIUSDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "DAIUSDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DASHEUR:
    """
        name: DASHEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.13
        maximum_order_size: None
        margin: True
    """
    name: str = "DASHEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.13
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.13
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DASHUSD:
    """
        name: DASHUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.13
        maximum_order_size: None
        margin: True
    """
    name: str = "DASHUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.13
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.13
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DASHXBT:
    """
        name: DASHXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.13
        maximum_order_size: None
        margin: True
    """
    name: str = "DASHXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.13
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.13
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DENTEUR:
    """
        name: DENTEUR
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7000
        maximum_order_size: None
        margin: False
    """
    name: str = "DENTEUR"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class DENTUSD:
    """
        name: DENTUSD
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7000
        maximum_order_size: None
        margin: False
    """
    name: str = "DENTUSD"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class DOTAUD:
    """
        name: DOTAUD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DOTAUD"
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
        return "DOTAUD"

    def __str__(self):
        return "DOTAUD"

    def __call__(self):
        return "DOTAUD"


DOTAUD = DOTAUD()
"""
    name: DOTAUD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class DOTETH:
    """
        name: DOTETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: True
    """
    name: str = "DOTETH"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DOTEUR:
    """
        name: DOTEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: True
    """
    name: str = "DOTEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DOTGBP:
    """
        name: DOTGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DOTGBP"
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
        return "DOTGBP"

    def __str__(self):
        return "DOTGBP"

    def __call__(self):
        return "DOTGBP"


DOTGBP = DOTGBP()
"""
    name: DOTGBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class DOTJPY:
    """
        name: DOTJPY
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "DOTJPY"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class DOTUSD:
    """
        name: DOTUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: True
    """
    name: str = "DOTUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DOTUSDT:
    """
        name: DOTUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: True
    """
    name: str = "DOTUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DOTXBT:
    """
        name: DOTXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: True
    """
    name: str = "DOTXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DYDXEUR:
    """
        name: DYDXEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "DYDXEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class DYDXUSD:
    """
        name: DYDXUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "DYDXUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EGLDEUR:
    """
        name: EGLDEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: False
    """
    name: str = "EGLDEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EGLDUSD:
    """
        name: EGLDUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: False
    """
    name: str = "EGLDUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ENJEUR:
    """
        name: ENJEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "ENJEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ENJGBP:
    """
        name: ENJGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "ENJGBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ENJJPY:
    """
        name: ENJJPY
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "ENJJPY"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ENJUSD:
    """
        name: ENJUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "ENJUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ENJXBT:
    """
        name: ENJXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "ENJXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ENSEUR:
    """
        name: ENSEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.4
        maximum_order_size: None
        margin: False
    """
    name: str = "ENSEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.4
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.4
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ENSUSD:
    """
        name: ENSUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.4
        maximum_order_size: None
        margin: False
    """
    name: str = "ENSUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.4
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.4
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EOSETH:
    """
        name: EOSETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "EOSETH"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class EOSEUR:
    """
        name: EOSEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "EOSEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class EOSUSD:
    """
        name: EOSUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "EOSUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class EOSUSDT:
    """
        name: EOSUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "EOSUSDT"
    precision: int = 0.0001
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
        return "EOSUSDT"

    def __str__(self):
        return "EOSUSDT"

    def __call__(self):
        return "EOSUSDT"


EOSUSDT = EOSUSDT()
"""
    name: EOSUSDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EOSXBT:
    """
        name: EOSXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "EOSXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETH2_SETH:
    """
        name: ETH2.SETH
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.001
        maximum_order_size: None
        margin: False
    """
    name: str = "ETH2.SETH"
    precision: int = 0.0001
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
        return "ETH2.SETH"

    def __str__(self):
        return "ETH2.SETH"

    def __call__(self):
        return "ETH2.SETH"


ETH2_SETH = ETH2_SETH()
"""
    name: ETH2.SETH
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ETHAED:
    """
        name: ETHAED
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: False
    """
    name: str = "ETHAED"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ETHAUD:
    """
        name: ETHAUD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: True
    """
    name: str = "ETHAUD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHCHF:
    """
        name: ETHCHF
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: False
    """
    name: str = "ETHCHF"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ETHDAI:
    """
        name: ETHDAI
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: False
    """
    name: str = "ETHDAI"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ETHUSDC:
    """
        name: ETHUSDC
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: True
    """
    name: str = "ETHUSDC"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHUSDT:
    """
        name: ETHUSDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: True
    """
    name: str = "ETHUSDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHWETH:
    """
        name: ETHWETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ETHWETH"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ETHWEUR:
    """
        name: ETHWEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ETHWEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ETHWUSD:
    """
        name: ETHWUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ETHWUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EULEUR:
    """
        name: EULEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "EULEUR"
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
        return "EULEUR"

    def __str__(self):
        return "EULEUR"

    def __call__(self):
        return "EULEUR"


EULEUR = EULEUR()
"""
    name: EULEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EULUSD:
    """
        name: EULUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "EULUSD"
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
        return "EULUSD"

    def __str__(self):
        return "EULUSD"

    def __call__(self):
        return "EULUSD"


EULUSD = EULUSD()
"""
    name: EULUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EURAUD:
    """
        name: EURAUD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "EURAUD"
    precision: int = 0.00001
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
        return "EURAUD"

    def __str__(self):
        return "EURAUD"

    def __call__(self):
        return "EURAUD"


EURAUD = EURAUD()
"""
    name: EURAUD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EURCAD:
    """
        name: EURCAD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "EURCAD"
    precision: int = 0.00001
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
        return "EURCAD"

    def __str__(self):
        return "EURCAD"

    def __call__(self):
        return "EURCAD"


EURCAD = EURCAD()
"""
    name: EURCAD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EURCHF:
    """
        name: EURCHF
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "EURCHF"
    precision: int = 0.00001
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
        return "EURCHF"

    def __str__(self):
        return "EURCHF"

    def __call__(self):
        return "EURCHF"


EURCHF = EURCHF()
"""
    name: EURCHF
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EURGBP:
    """
        name: EURGBP
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "EURGBP"
    precision: int = 0.00001
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
        return "EURGBP"

    def __str__(self):
        return "EURGBP"

    def __call__(self):
        return "EURGBP"


EURGBP = EURGBP()
"""
    name: EURGBP
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EURJPY:
    """
        name: EURJPY
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "EURJPY"
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
        return "EURJPY"

    def __str__(self):
        return "EURJPY"

    def __call__(self):
        return "EURJPY"


EURJPY = EURJPY()
"""
    name: EURJPY
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EWTEUR:
    """
        name: EWTEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: False
    """
    name: str = "EWTEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EWTGBP:
    """
        name: EWTGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: False
    """
    name: str = "EWTGBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EWTUSD:
    """
        name: EWTUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: False
    """
    name: str = "EWTUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class EWTXBT:
    """
        name: EWTXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: False
    """
    name: str = "EWTXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FARMEUR:
    """
        name: FARMEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: False
    """
    name: str = "FARMEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FARMUSD:
    """
        name: FARMUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: False
    """
    name: str = "FARMUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FETEUR:
    """
        name: FETEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: False
    """
    name: str = "FETEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FETUSD:
    """
        name: FETUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: False
    """
    name: str = "FETUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FIDAEUR:
    """
        name: FIDAEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "FIDAEUR"
    precision: int = 0.001
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
        return "FIDAEUR"

    def __str__(self):
        return "FIDAEUR"

    def __call__(self):
        return "FIDAEUR"


FIDAEUR = FIDAEUR()
"""
    name: FIDAEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FIDAUSD:
    """
        name: FIDAUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "FIDAUSD"
    precision: int = 0.001
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
        return "FIDAUSD"

    def __str__(self):
        return "FIDAUSD"

    def __call__(self):
        return "FIDAUSD"


FIDAUSD = FIDAUSD()
"""
    name: FIDAUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FILAUD:
    """
        name: FILAUD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: False
    """
    name: str = "FILAUD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FILAUD"

    def __str__(self):
        return "FILAUD"

    def __call__(self):
        return "FILAUD"


FILAUD = FILAUD()
"""
    name: FILAUD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FILETH:
    """
        name: FILETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: False
    """
    name: str = "FILETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FILEUR:
    """
        name: FILEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: True
    """
    name: str = "FILEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class FILGBP:
    """
        name: FILGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: False
    """
    name: str = "FILGBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FILUSD:
    """
        name: FILUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: True
    """
    name: str = "FILUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class FILXBT:
    """
        name: FILXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.25
        maximum_order_size: None
        margin: True
    """
    name: str = "FILXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.25
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.25
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class FISEUR:
    """
        name: FISEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "FISEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FISUSD:
    """
        name: FISUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "FISUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FLOWETH:
    """
        name: FLOWETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "FLOWETH"
    precision: int = 0.000001
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
        return "FLOWETH"

    def __str__(self):
        return "FLOWETH"

    def __call__(self):
        return "FLOWETH"


FLOWETH = FLOWETH()
"""
    name: FLOWETH
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FLOWEUR:
    """
        name: FLOWEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "FLOWEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class FLOWGBP:
    """
        name: FLOWGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "FLOWGBP"
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
        return "FLOWGBP"

    def __str__(self):
        return "FLOWGBP"

    def __call__(self):
        return "FLOWGBP"


FLOWGBP = FLOWGBP()
"""
    name: FLOWGBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FLOWUSD:
    """
        name: FLOWUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "FLOWUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class FLOWXBT:
    """
        name: FLOWXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "FLOWXBT"
    precision: int = 0.0000001
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
        return "FLOWXBT"

    def __str__(self):
        return "FLOWXBT"

    def __call__(self):
        return "FLOWXBT"


FLOWXBT = FLOWXBT()
"""
    name: FLOWXBT
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FLREUR:
    """
        name: FLREUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "FLREUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FLRUSD:
    """
        name: FLRUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "FLRUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FORTHEUR:
    """
        name: FORTHEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "FORTHEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FORTHUSD:
    """
        name: FORTHUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "FORTHUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FTMEUR:
    """
        name: FTMEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "FTMEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FTMUSD:
    """
        name: FTMUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "FTMUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FXSEUR:
    """
        name: FXSEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FXSEUR"
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
        return "FXSEUR"

    def __str__(self):
        return "FXSEUR"

    def __call__(self):
        return "FXSEUR"


FXSEUR = FXSEUR()
"""
    name: FXSEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class FXSUSD:
    """
        name: FXSUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "FXSUSD"
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
        return "FXSUSD"

    def __str__(self):
        return "FXSUSD"

    def __call__(self):
        return "FXSUSD"


FXSUSD = FXSUSD()
"""
    name: FXSUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GALAEUR:
    """
        name: GALAEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "GALAEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GALAUSD:
    """
        name: GALAUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "GALAUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GALEUR:
    """
        name: GALEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "GALEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GALUSD:
    """
        name: GALUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "GALUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GARIEUR:
    """
        name: GARIEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 150
        maximum_order_size: None
        margin: False
    """
    name: str = "GARIEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 150
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 150
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GARIUSD:
    """
        name: GARIUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 150
        maximum_order_size: None
        margin: False
    """
    name: str = "GARIUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 150
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 150
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GHSTEUR:
    """
        name: GHSTEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "GHSTEUR"
    precision: int = 0.0001
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
        return "GHSTEUR"

    def __str__(self):
        return "GHSTEUR"

    def __call__(self):
        return "GHSTEUR"


GHSTEUR = GHSTEUR()
"""
    name: GHSTEUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GHSTGBP:
    """
        name: GHSTGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "GHSTGBP"
    precision: int = 0.0001
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
        return "GHSTGBP"

    def __str__(self):
        return "GHSTGBP"

    def __call__(self):
        return "GHSTGBP"


GHSTGBP = GHSTGBP()
"""
    name: GHSTGBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GHSTUSD:
    """
        name: GHSTUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "GHSTUSD"
    precision: int = 0.0001
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
        return "GHSTUSD"

    def __str__(self):
        return "GHSTUSD"

    def __call__(self):
        return "GHSTUSD"


GHSTUSD = GHSTUSD()
"""
    name: GHSTUSD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GHSTXBT:
    """
        name: GHSTXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "GHSTXBT"
    precision: int = 0.00000001
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
        return "GHSTXBT"

    def __str__(self):
        return "GHSTXBT"

    def __call__(self):
        return "GHSTXBT"


GHSTXBT = GHSTXBT()
"""
    name: GHSTXBT
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GLMREUR:
    """
        name: GLMREUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "GLMREUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GLMRUSD:
    """
        name: GLMRUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "GLMRUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GMTEUR:
    """
        name: GMTEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "GMTEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GMTUSD:
    """
        name: GMTUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "GMTUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GNOETH:
    """
        name: GNOETH
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: False
    """
    name: str = "GNOETH"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GNOETH"

    def __str__(self):
        return "GNOETH"

    def __call__(self):
        return "GNOETH"


GNOETH = GNOETH()
"""
    name: GNOETH
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GNOEUR:
    """
        name: GNOEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: False
    """
    name: str = "GNOEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GNOUSD:
    """
        name: GNOUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: False
    """
    name: str = "GNOUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GNOXBT:
    """
        name: GNOXBT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: False
    """
    name: str = "GNOXBT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GRTAUD:
    """
        name: GRTAUD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 80
        maximum_order_size: None
        margin: False
    """
    name: str = "GRTAUD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 80
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRTAUD"

    def __str__(self):
        return "GRTAUD"

    def __call__(self):
        return "GRTAUD"


GRTAUD = GRTAUD()
"""
    name: GRTAUD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 80
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GRTETH:
    """
        name: GRTETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 80
        maximum_order_size: None
        margin: False
    """
    name: str = "GRTETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 80
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRTETH"

    def __str__(self):
        return "GRTETH"

    def __call__(self):
        return "GRTETH"


GRTETH = GRTETH()
"""
    name: GRTETH
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 80
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GRTEUR:
    """
        name: GRTEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 80
        maximum_order_size: None
        margin: True
    """
    name: str = "GRTEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 80
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 80
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class GRTGBP:
    """
        name: GRTGBP
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 80
        maximum_order_size: None
        margin: False
    """
    name: str = "GRTGBP"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 80
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 80
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GRTUSD:
    """
        name: GRTUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 80
        maximum_order_size: None
        margin: True
    """
    name: str = "GRTUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 80
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 80
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class GRTXBT:
    """
        name: GRTXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 80
        maximum_order_size: None
        margin: False
    """
    name: str = "GRTXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 80
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 80
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GSTEUR:
    """
        name: GSTEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "GSTEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GSTUSD:
    """
        name: GSTUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 200
        maximum_order_size: None
        margin: False
    """
    name: str = "GSTUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 200
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 200
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GTCEUR:
    """
        name: GTCEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "GTCEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class GTCUSD:
    """
        name: GTCUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "GTCUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class HFTEUR:
    """
        name: HFTEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8.5
        maximum_order_size: None
        margin: False
    """
    name: str = "HFTEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class HFTUSD:
    """
        name: HFTUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8.5
        maximum_order_size: None
        margin: False
    """
    name: str = "HFTUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ICPEUR:
    """
        name: ICPEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ICPEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ICPUSD:
    """
        name: ICPUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "ICPUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ICXETH:
    """
        name: ICXETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "ICXETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ICXEUR:
    """
        name: ICXEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "ICXEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ICXUSD:
    """
        name: ICXUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "ICXUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ICXXBT:
    """
        name: ICXXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "ICXXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class IDEXEUR:
    """
        name: IDEXEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: False
    """
    name: str = "IDEXEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class IDEXUSD:
    """
        name: IDEXUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: False
    """
    name: str = "IDEXUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class IMXEUR:
    """
        name: IMXEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12
        maximum_order_size: None
        margin: False
    """
    name: str = "IMXEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class IMXUSD:
    """
        name: IMXUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12
        maximum_order_size: None
        margin: False
    """
    name: str = "IMXUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class INJEUR:
    """
        name: INJEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "INJEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class INJUSD:
    """
        name: INJUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "INJUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class INTREUR:
    """
        name: INTREUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "INTREUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class INTRUSD:
    """
        name: INTRUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "INTRUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class JASMYEUR:
    """
        name: JASMYEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1250
        maximum_order_size: None
        margin: False
    """
    name: str = "JASMYEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class JASMYUSD:
    """
        name: JASMYUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1250
        maximum_order_size: None
        margin: False
    """
    name: str = "JASMYUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class JUNOEUR:
    """
        name: JUNOEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "JUNOEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class JUNOUSD:
    """
        name: JUNOUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "JUNOUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KAREUR:
    """
        name: KAREUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 22.5
        maximum_order_size: None
        margin: False
    """
    name: str = "KAREUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 22.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 22.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KARUSD:
    """
        name: KARUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 22.5
        maximum_order_size: None
        margin: False
    """
    name: str = "KARUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 22.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 22.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KAVAETH:
    """
        name: KAVAETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "KAVAETH"
    precision: int = 0.000001
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
        return "KAVAETH"

    def __str__(self):
        return "KAVAETH"

    def __call__(self):
        return "KAVAETH"


KAVAETH = KAVAETH()
"""
    name: KAVAETH
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KAVAEUR:
    """
        name: KAVAEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "KAVAEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class KAVAUSD:
    """
        name: KAVAUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "KAVAUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class KAVAXBT:
    """
        name: KAVAXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "KAVAXBT"
    precision: int = 0.00000001
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
        return "KAVAXBT"

    def __str__(self):
        return "KAVAXBT"

    def __call__(self):
        return "KAVAXBT"


KAVAXBT = KAVAXBT()
"""
    name: KAVAXBT
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KEEPETH:
    """
        name: KEEPETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: False
    """
    name: str = "KEEPETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KEEPETH"

    def __str__(self):
        return "KEEPETH"

    def __call__(self):
        return "KEEPETH"


KEEPETH = KEEPETH()
"""
    name: KEEPETH
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KEEPEUR:
    """
        name: KEEPEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: True
    """
    name: str = "KEEPEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class KEEPUSD:
    """
        name: KEEPUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: True
    """
    name: str = "KEEPUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class KEEPXBT:
    """
        name: KEEPXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: False
    """
    name: str = "KEEPXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KEYEUR:
    """
        name: KEYEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1500
        maximum_order_size: None
        margin: False
    """
    name: str = "KEYEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KEYUSD:
    """
        name: KEYUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1500
        maximum_order_size: None
        margin: False
    """
    name: str = "KEYUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KILTEUR:
    """
        name: KILTEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12
        maximum_order_size: None
        margin: False
    """
    name: str = "KILTEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KILTUSD:
    """
        name: KILTUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12
        maximum_order_size: None
        margin: False
    """
    name: str = "KILTUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KINEUR:
    """
        name: KINEUR
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500000
        maximum_order_size: None
        margin: False
    """
    name: str = "KINEUR"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KINTEUR:
    """
        name: KINTEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 6.5
        maximum_order_size: None
        margin: False
    """
    name: str = "KINTEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 6.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 6.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KINTUSD:
    """
        name: KINTUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 6.5
        maximum_order_size: None
        margin: False
    """
    name: str = "KINTUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 6.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 6.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KINUSD:
    """
        name: KINUSD
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500000
        maximum_order_size: None
        margin: False
    """
    name: str = "KINUSD"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KNCETH:
    """
        name: KNCETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "KNCETH"
    precision: int = 0.000001
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
        return "KNCETH"

    def __str__(self):
        return "KNCETH"

    def __call__(self):
        return "KNCETH"


KNCETH = KNCETH()
"""
    name: KNCETH
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KNCEUR:
    """
        name: KNCEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "KNCEUR"
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
        return "KNCEUR"

    def __str__(self):
        return "KNCEUR"

    def __call__(self):
        return "KNCEUR"


KNCEUR = KNCEUR()
"""
    name: KNCEUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KNCUSD:
    """
        name: KNCUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "KNCUSD"
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
        return "KNCUSD"

    def __str__(self):
        return "KNCUSD"

    def __call__(self):
        return "KNCUSD"


KNCUSD = KNCUSD()
"""
    name: KNCUSD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KNCXBT:
    """
        name: KNCXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "KNCXBT"
    precision: int = 0.00000001
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
        return "KNCXBT"

    def __str__(self):
        return "KNCXBT"

    def __call__(self):
        return "KNCXBT"


KNCXBT = KNCXBT()
"""
    name: KNCXBT
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KP3REUR:
    """
        name: KP3REUR
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.065
        maximum_order_size: None
        margin: False
    """
    name: str = "KP3REUR"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.065
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.065
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KP3RUSD:
    """
        name: KP3RUSD
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.065
        maximum_order_size: None
        margin: False
    """
    name: str = "KP3RUSD"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.065
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.065
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KSMAUD:
    """
        name: KSMAUD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: False
    """
    name: str = "KSMAUD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSMAUD"

    def __str__(self):
        return "KSMAUD"

    def __call__(self):
        return "KSMAUD"


KSMAUD = KSMAUD()
"""
    name: KSMAUD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KSMDOT:
    """
        name: KSMDOT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: False
    """
    name: str = "KSMDOT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KSMETH:
    """
        name: KSMETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: False
    """
    name: str = "KSMETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KSMEUR:
    """
        name: KSMEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: True
    """
    name: str = "KSMEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class KSMGBP:
    """
        name: KSMGBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: False
    """
    name: str = "KSMGBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class KSMUSD:
    """
        name: KSMUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: True
    """
    name: str = "KSMUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class KSMXBT:
    """
        name: KSMXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.2
        maximum_order_size: None
        margin: False
    """
    name: str = "KSMXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LCXEUR:
    """
        name: LCXEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 125
        maximum_order_size: None
        margin: False
    """
    name: str = "LCXEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 125
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 125
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LCXUSD:
    """
        name: LCXUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 125
        maximum_order_size: None
        margin: False
    """
    name: str = "LCXUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 125
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 125
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LDOEUR:
    """
        name: LDOEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "LDOEUR"
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
        return "LDOEUR"

    def __str__(self):
        return "LDOEUR"

    def __call__(self):
        return "LDOEUR"


LDOEUR = LDOEUR()
"""
    name: LDOEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LDOUSD:
    """
        name: LDOUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "LDOUSD"
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
        return "LDOUSD"

    def __str__(self):
        return "LDOUSD"

    def __call__(self):
        return "LDOUSD"


LDOUSD = LDOUSD()
"""
    name: LDOUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LINKAUD:
    """
        name: LINKAUD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.8
        maximum_order_size: None
        margin: False
    """
    name: str = "LINKAUD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.8
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.8
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LINKETH:
    """
        name: LINKETH
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.8
        maximum_order_size: None
        margin: True
    """
    name: str = "LINKETH"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.8
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.8
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LINKEUR:
    """
        name: LINKEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.8
        maximum_order_size: None
        margin: True
    """
    name: str = "LINKEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.8
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.8
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LINKGBP:
    """
        name: LINKGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.8
        maximum_order_size: None
        margin: False
    """
    name: str = "LINKGBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.8
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.8
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LINKJPY:
    """
        name: LINKJPY
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.8
        maximum_order_size: None
        margin: False
    """
    name: str = "LINKJPY"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.8
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.8
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LINKUSD:
    """
        name: LINKUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.8
        maximum_order_size: None
        margin: True
    """
    name: str = "LINKUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.8
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.8
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LINKUSDT:
    """
        name: LINKUSDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.8
        maximum_order_size: None
        margin: True
    """
    name: str = "LINKUSDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.8
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.8
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LINKXBT:
    """
        name: LINKXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.8
        maximum_order_size: None
        margin: True
    """
    name: str = "LINKXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.8
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.8
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LPTEUR:
    """
        name: LPTEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.65
        maximum_order_size: None
        margin: False
    """
    name: str = "LPTEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LPTGBP:
    """
        name: LPTGBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.65
        maximum_order_size: None
        margin: False
    """
    name: str = "LPTGBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LPTUSD:
    """
        name: LPTUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.65
        maximum_order_size: None
        margin: False
    """
    name: str = "LPTUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LPTXBT:
    """
        name: LPTXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.65
        maximum_order_size: None
        margin: False
    """
    name: str = "LPTXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LRCEUR:
    """
        name: LRCEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: True
    """
    name: str = "LRCEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LRCUSD:
    """
        name: LRCUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: True
    """
    name: str = "LRCUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LSKETH:
    """
        name: LSKETH
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7.5
        maximum_order_size: None
        margin: False
    """
    name: str = "LSKETH"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LSKEUR:
    """
        name: LSKEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7.5
        maximum_order_size: None
        margin: False
    """
    name: str = "LSKEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LSKUSD:
    """
        name: LSKUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7.5
        maximum_order_size: None
        margin: False
    """
    name: str = "LSKUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LSKXBT:
    """
        name: LSKXBT
        precision: 0.000000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7.5
        maximum_order_size: None
        margin: False
    """
    name: str = "LSKXBT"
    precision: int = 0.000000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LTCAUD:
    """
        name: LTCAUD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: False
    """
    name: str = "LTCAUD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LTCETH:
    """
        name: LTCETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: False
    """
    name: str = "LTCETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LTCGBP:
    """
        name: LTCGBP
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: False
    """
    name: str = "LTCGBP"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LTCUSDT:
    """
        name: LTCUSDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: False
    """
    name: str = "LTCUSDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LUNA2EUR:
    """
        name: LUNA2EUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "LUNA2EUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LUNA2USD:
    """
        name: LUNA2USD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "LUNA2USD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LUNAEUR:
    """
        name: LUNAEUR
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30000
        maximum_order_size: None
        margin: False
    """
    name: str = "LUNAEUR"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class LUNAUSD:
    """
        name: LUNAUSD
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30000
        maximum_order_size: None
        margin: False
    """
    name: str = "LUNAUSD"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MANAETH:
    """
        name: MANAETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "MANAETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MANAEUR:
    """
        name: MANAEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: True
    """
    name: str = "MANAEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class MANAUSD:
    """
        name: MANAUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: True
    """
    name: str = "MANAUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class MANAUSDT:
    """
        name: MANAUSDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "MANAUSDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MANAXBT:
    """
        name: MANAXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: True
    """
    name: str = "MANAXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class MASKEUR:
    """
        name: MASKEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "MASKEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MASKUSD:
    """
        name: MASKUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "MASKUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MATICEUR:
    """
        name: MATICEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 6
        maximum_order_size: None
        margin: True
    """
    name: str = "MATICEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 6
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 6
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class MATICGBP:
    """
        name: MATICGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 6
        maximum_order_size: None
        margin: False
    """
    name: str = "MATICGBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 6
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 6
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MATICUSD:
    """
        name: MATICUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 6
        maximum_order_size: None
        margin: True
    """
    name: str = "MATICUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 6
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 6
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class MATICUSDT:
    """
        name: MATICUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 6
        maximum_order_size: None
        margin: False
    """
    name: str = "MATICUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 6
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 6
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MATICXBT:
    """
        name: MATICXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 6
        maximum_order_size: None
        margin: True
    """
    name: str = "MATICXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 6
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 6
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class MCEUR:
    """
        name: MCEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12
        maximum_order_size: None
        margin: False
    """
    name: str = "MCEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MCUSD:
    """
        name: MCUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12
        maximum_order_size: None
        margin: False
    """
    name: str = "MCUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MINAEUR:
    """
        name: MINAEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "MINAEUR"
    precision: int = 0.001
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
        return "MINAEUR"

    def __str__(self):
        return "MINAEUR"

    def __call__(self):
        return "MINAEUR"


MINAEUR = MINAEUR()
"""
    name: MINAEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MINAGBP:
    """
        name: MINAGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "MINAGBP"
    precision: int = 0.001
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
        return "MINAGBP"

    def __str__(self):
        return "MINAGBP"

    def __call__(self):
        return "MINAGBP"


MINAGBP = MINAGBP()
"""
    name: MINAGBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MINAUSD:
    """
        name: MINAUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "MINAUSD"
    precision: int = 0.001
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
        return "MINAUSD"

    def __str__(self):
        return "MINAUSD"

    def __call__(self):
        return "MINAUSD"


MINAUSD = MINAUSD()
"""
    name: MINAUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MINAXBT:
    """
        name: MINAXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "MINAXBT"
    precision: int = 0.0000001
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
        return "MINAXBT"

    def __str__(self):
        return "MINAXBT"

    def __call__(self):
        return "MINAXBT"


MINAXBT = MINAXBT()
"""
    name: MINAXBT
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MIREUR:
    """
        name: MIREUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "MIREUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MIRUSD:
    """
        name: MIRUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "MIRUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MKREUR:
    """
        name: MKREUR
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0075
        maximum_order_size: None
        margin: False
    """
    name: str = "MKREUR"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0075
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0075
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MKRGBP:
    """
        name: MKRGBP
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0075
        maximum_order_size: None
        margin: False
    """
    name: str = "MKRGBP"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0075
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MKRGBP"

    def __str__(self):
        return "MKRGBP"

    def __call__(self):
        return "MKRGBP"


MKRGBP = MKRGBP()
"""
    name: MKRGBP
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0075
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MKRUSD:
    """
        name: MKRUSD
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0075
        maximum_order_size: None
        margin: False
    """
    name: str = "MKRUSD"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0075
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0075
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MKRXBT:
    """
        name: MKRXBT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0075
        maximum_order_size: None
        margin: False
    """
    name: str = "MKRXBT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0075
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0075
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MNGOEUR:
    """
        name: MNGOEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "MNGOEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MNGOUSD:
    """
        name: MNGOUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "MNGOUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MOVREUR:
    """
        name: MOVREUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.65
        maximum_order_size: None
        margin: False
    """
    name: str = "MOVREUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MOVRUSD:
    """
        name: MOVRUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.65
        maximum_order_size: None
        margin: False
    """
    name: str = "MOVRUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MSOLEUR:
    """
        name: MSOLEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.35
        maximum_order_size: None
        margin: False
    """
    name: str = "MSOLEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MSOLUSD:
    """
        name: MSOLUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.35
        maximum_order_size: None
        margin: False
    """
    name: str = "MSOLUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MULTIEUR:
    """
        name: MULTIEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "MULTIEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MULTIUSD:
    """
        name: MULTIUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "MULTIUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MVEUR:
    """
        name: MVEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "MVEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MVUSD:
    """
        name: MVUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "MVUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MXCEUR:
    """
        name: MXCEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 150
        maximum_order_size: None
        margin: False
    """
    name: str = "MXCEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 150
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 150
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class MXCUSD:
    """
        name: MXCUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 150
        maximum_order_size: None
        margin: False
    """
    name: str = "MXCUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 150
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 150
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NANOETH:
    """
        name: NANOETH
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8
        maximum_order_size: None
        margin: False
    """
    name: str = "NANOETH"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NANOEUR:
    """
        name: NANOEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8
        maximum_order_size: None
        margin: True
    """
    name: str = "NANOEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class NANOUSD:
    """
        name: NANOUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8
        maximum_order_size: None
        margin: True
    """
    name: str = "NANOUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class NANOXBT:
    """
        name: NANOXBT
        precision: 0.000000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8
        maximum_order_size: None
        margin: False
    """
    name: str = "NANOXBT"
    precision: int = 0.000000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NEAREUR:
    """
        name: NEAREUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "NEAREUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NEARUSD:
    """
        name: NEARUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "NEARUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NMREUR:
    """
        name: NMREUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.5
        maximum_order_size: None
        margin: False
    """
    name: str = "NMREUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NMRUSD:
    """
        name: NMRUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.5
        maximum_order_size: None
        margin: False
    """
    name: str = "NMRUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NODLEUR:
    """
        name: NODLEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: False
    """
    name: str = "NODLEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NODLUSD:
    """
        name: NODLUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: False
    """
    name: str = "NODLUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NYMEUR:
    """
        name: NYMEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "NYMEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NYMUSD:
    """
        name: NYMUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "NYMUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class NYMXBT:
    """
        name: NYMXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "NYMXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OCEANEUR:
    """
        name: OCEANEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "OCEANEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OCEANGBP:
    """
        name: OCEANGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "OCEANGBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OCEANUSD:
    """
        name: OCEANUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "OCEANUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OCEANXBT:
    """
        name: OCEANXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "OCEANXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OGNEUR:
    """
        name: OGNEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "OGNEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OGNUSD:
    """
        name: OGNUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "OGNUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OMGETH:
    """
        name: OMGETH
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "OMGETH"
    precision: int = 0.00000001
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
        return "OMGETH"

    def __str__(self):
        return "OMGETH"

    def __call__(self):
        return "OMGETH"


OMGETH = OMGETH()
"""
    name: OMGETH
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OMGEUR:
    """
        name: OMGEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "OMGEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class OMGJPY:
    """
        name: OMGJPY
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "OMGJPY"
    precision: int = 0.1
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
        return "OMGJPY"

    def __str__(self):
        return "OMGJPY"

    def __call__(self):
        return "OMGJPY"


OMGJPY = OMGJPY()
"""
    name: OMGJPY
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OMGUSD:
    """
        name: OMGUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "OMGUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class OMGXBT:
    """
        name: OMGXBT
        precision: 0.000000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "OMGXBT"
    precision: int = 0.000000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ORCAEUR:
    """
        name: ORCAEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "ORCAEUR"
    precision: int = 0.001
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
        return "ORCAEUR"

    def __str__(self):
        return "ORCAEUR"

    def __call__(self):
        return "ORCAEUR"


ORCAEUR = ORCAEUR()
"""
    name: ORCAEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ORCAUSD:
    """
        name: ORCAUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "ORCAUSD"
    precision: int = 0.001
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
        return "ORCAUSD"

    def __str__(self):
        return "ORCAUSD"

    def __call__(self):
        return "ORCAUSD"


ORCAUSD = ORCAUSD()
"""
    name: ORCAUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OXTETH:
    """
        name: OXTETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: False
    """
    name: str = "OXTETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OXTETH"

    def __str__(self):
        return "OXTETH"

    def __call__(self):
        return "OXTETH"


OXTETH = OXTETH()
"""
    name: OXTETH
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OXTEUR:
    """
        name: OXTEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: False
    """
    name: str = "OXTEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OXTUSD:
    """
        name: OXTUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: False
    """
    name: str = "OXTUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OXTXBT:
    """
        name: OXTXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 75
        maximum_order_size: None
        margin: False
    """
    name: str = "OXTXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 75
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 75
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OXYEUR:
    """
        name: OXYEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 600
        maximum_order_size: None
        margin: False
    """
    name: str = "OXYEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 600
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 600
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class OXYUSD:
    """
        name: OXYUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 600
        maximum_order_size: None
        margin: False
    """
    name: str = "OXYUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 600
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 600
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PARAEUR:
    """
        name: PARAEUR
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 350
        maximum_order_size: None
        margin: False
    """
    name: str = "PARAEUR"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 350
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 350
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PARAUSD:
    """
        name: PARAUSD
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 350
        maximum_order_size: None
        margin: False
    """
    name: str = "PARAUSD"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 350
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 350
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PAXGETH:
    """
        name: PAXGETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.003
        maximum_order_size: None
        margin: False
    """
    name: str = "PAXGETH"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.003
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.003
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PAXGEUR:
    """
        name: PAXGEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.003
        maximum_order_size: None
        margin: True
    """
    name: str = "PAXGEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.003
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.003
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class PAXGUSD:
    """
        name: PAXGUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.003
        maximum_order_size: None
        margin: True
    """
    name: str = "PAXGUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.003
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.003
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class PAXGXBT:
    """
        name: PAXGXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.003
        maximum_order_size: None
        margin: False
    """
    name: str = "PAXGXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.003
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.003
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PERPEUR:
    """
        name: PERPEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "PERPEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PERPUSD:
    """
        name: PERPUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "PERPUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PHAEUR:
    """
        name: PHAEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "PHAEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PHAUSD:
    """
        name: PHAUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "PHAUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PLAEUR:
    """
        name: PLAEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "PLAEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PLAUSD:
    """
        name: PLAUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "PLAUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class POLISEUR:
    """
        name: POLISEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "POLISEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class POLISUSD:
    """
        name: POLISUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "POLISUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class POLSEUR:
    """
        name: POLSEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "POLSEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class POLSUSD:
    """
        name: POLSUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "POLSUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PONDEUR:
    """
        name: PONDEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 600
        maximum_order_size: None
        margin: False
    """
    name: str = "PONDEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 600
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 600
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PONDUSD:
    """
        name: PONDUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 600
        maximum_order_size: None
        margin: False
    """
    name: str = "PONDUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 600
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 600
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class POWREUR:
    """
        name: POWREUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "POWREUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class POWRUSD:
    """
        name: POWRUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 30
        maximum_order_size: None
        margin: False
    """
    name: str = "POWRUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 30
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 30
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PSTAKEEUR:
    """
        name: PSTAKEEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 65
        maximum_order_size: None
        margin: False
    """
    name: str = "PSTAKEEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class PSTAKEUSD:
    """
        name: PSTAKEUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 65
        maximum_order_size: None
        margin: False
    """
    name: str = "PSTAKEUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 65
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 65
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class QNTEUR:
    """
        name: QNTEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: False
    """
    name: str = "QNTEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class QNTUSD:
    """
        name: QNTUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: False
    """
    name: str = "QNTUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class QTUMETH:
    """
        name: QTUMETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "QTUMETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class QTUMEUR:
    """
        name: QTUMEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "QTUMEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class QTUMUSD:
    """
        name: QTUMUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "QTUMUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class QTUMXBT:
    """
        name: QTUMXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "QTUMXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RADEUR:
    """
        name: RADEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "RADEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RADUSD:
    """
        name: RADUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "RADUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RAREEUR:
    """
        name: RAREEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "RAREEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RAREUSD:
    """
        name: RAREUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 35
        maximum_order_size: None
        margin: False
    """
    name: str = "RAREUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RARIEUR:
    """
        name: RARIEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "RARIEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RARIGBP:
    """
        name: RARIGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "RARIGBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RARIGBP"

    def __str__(self):
        return "RARIGBP"

    def __call__(self):
        return "RARIGBP"


RARIGBP = RARIGBP()
"""
    name: RARIGBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RARIUSD:
    """
        name: RARIUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "RARIUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RARIXBT:
    """
        name: RARIXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "RARIXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RAYEUR:
    """
        name: RAYEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "RAYEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RAYUSD:
    """
        name: RAYUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "RAYUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RBCEUR:
    """
        name: RBCEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 150
        maximum_order_size: None
        margin: False
    """
    name: str = "RBCEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 150
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 150
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RBCUSD:
    """
        name: RBCUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 150
        maximum_order_size: None
        margin: False
    """
    name: str = "RBCUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 150
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 150
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RENEUR:
    """
        name: RENEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: False
    """
    name: str = "RENEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RENGBP:
    """
        name: RENGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: False
    """
    name: str = "RENGBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RENGBP"

    def __str__(self):
        return "RENGBP"

    def __call__(self):
        return "RENGBP"


RENGBP = RENGBP()
"""
    name: RENGBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RENUSD:
    """
        name: RENUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: False
    """
    name: str = "RENUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RENXBT:
    """
        name: RENXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: False
    """
    name: str = "RENXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class REPV2ETH:
    """
        name: REPV2ETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "REPV2ETH"
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
        return "REPV2ETH"

    def __str__(self):
        return "REPV2ETH"

    def __call__(self):
        return "REPV2ETH"


REPV2ETH = REPV2ETH()
"""
    name: REPV2ETH
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class REPV2EUR:
    """
        name: REPV2EUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "REPV2EUR"
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
        return "REPV2EUR"

    def __str__(self):
        return "REPV2EUR"

    def __call__(self):
        return "REPV2EUR"


REPV2EUR = REPV2EUR()
"""
    name: REPV2EUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class REPV2USD:
    """
        name: REPV2USD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "REPV2USD"
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
        return "REPV2USD"

    def __str__(self):
        return "REPV2USD"

    def __call__(self):
        return "REPV2USD"


REPV2USD = REPV2USD()
"""
    name: REPV2USD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class REPV2XBT:
    """
        name: REPV2XBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "REPV2XBT"
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
        return "REPV2XBT"

    def __str__(self):
        return "REPV2XBT"

    def __call__(self):
        return "REPV2XBT"


REPV2XBT = REPV2XBT()
"""
    name: REPV2XBT
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class REQEUR:
    """
        name: REQEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "REQEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class REQUSD:
    """
        name: REQUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "REQUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RLCEUR:
    """
        name: RLCEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 6.5
        maximum_order_size: None
        margin: False
    """
    name: str = "RLCEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 6.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 6.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RLCUSD:
    """
        name: RLCUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 6.5
        maximum_order_size: None
        margin: False
    """
    name: str = "RLCUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 6.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 6.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RNDREUR:
    """
        name: RNDREUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "RNDREUR"
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
        return "RNDREUR"

    def __str__(self):
        return "RNDREUR"

    def __call__(self):
        return "RNDREUR"


RNDREUR = RNDREUR()
"""
    name: RNDREUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RNDRUSD:
    """
        name: RNDRUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "RNDRUSD"
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
        return "RNDRUSD"

    def __str__(self):
        return "RNDRUSD"

    def __call__(self):
        return "RNDRUSD"


RNDRUSD = RNDRUSD()
"""
    name: RNDRUSD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ROOKEUR:
    """
        name: ROOKEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.35
        maximum_order_size: None
        margin: False
    """
    name: str = "ROOKEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ROOKUSD:
    """
        name: ROOKUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.35
        maximum_order_size: None
        margin: False
    """
    name: str = "ROOKUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RPLEUR:
    """
        name: RPLEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: False
    """
    name: str = "RPLEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RPLUSD:
    """
        name: RPLUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: False
    """
    name: str = "RPLUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RUNEEUR:
    """
        name: RUNEEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "RUNEEUR"
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
        return "RUNEEUR"

    def __str__(self):
        return "RUNEEUR"

    def __call__(self):
        return "RUNEEUR"


RUNEEUR = RUNEEUR()
"""
    name: RUNEEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class RUNEUSD:
    """
        name: RUNEUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "RUNEUSD"
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
        return "RUNEUSD"

    def __str__(self):
        return "RUNEUSD"

    def __call__(self):
        return "RUNEUSD"


RUNEUSD = RUNEUSD()
"""
    name: RUNEUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SAMOEUR:
    """
        name: SAMOEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: False
    """
    name: str = "SAMOEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SAMOUSD:
    """
        name: SAMOUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: False
    """
    name: str = "SAMOUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SANDEUR:
    """
        name: SANDEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8.5
        maximum_order_size: None
        margin: True
    """
    name: str = "SANDEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SANDGBP:
    """
        name: SANDGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8.5
        maximum_order_size: None
        margin: False
    """
    name: str = "SANDGBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SANDUSD:
    """
        name: SANDUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8.5
        maximum_order_size: None
        margin: True
    """
    name: str = "SANDUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SANDXBT:
    """
        name: SANDXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8.5
        maximum_order_size: None
        margin: False
    """
    name: str = "SANDXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SBREUR:
    """
        name: SBREUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5000
        maximum_order_size: None
        margin: False
    """
    name: str = "SBREUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SBRUSD:
    """
        name: SBRUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5000
        maximum_order_size: None
        margin: False
    """
    name: str = "SBRUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SCETH:
    """
        name: SCETH
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: False
    """
    name: str = "SCETH"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SCEUR:
    """
        name: SCEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: True
    """
    name: str = "SCEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SCRTEUR:
    """
        name: SCRTEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "SCRTEUR"
    precision: int = 0.001
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
        return "SCRTEUR"

    def __str__(self):
        return "SCRTEUR"

    def __call__(self):
        return "SCRTEUR"


SCRTEUR = SCRTEUR()
"""
    name: SCRTEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SCRTUSD:
    """
        name: SCRTUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 10
        maximum_order_size: None
        margin: False
    """
    name: str = "SCRTUSD"
    precision: int = 0.001
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
        return "SCRTUSD"

    def __str__(self):
        return "SCRTUSD"

    def __call__(self):
        return "SCRTUSD"


SCRTUSD = SCRTUSD()
"""
    name: SCRTUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 10
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SCUSD:
    """
        name: SCUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: True
    """
    name: str = "SCUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SCXBT:
    """
        name: SCXBT
        precision: 0.0000000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2000
        maximum_order_size: None
        margin: False
    """
    name: str = "SCXBT"
    precision: int = 0.0000000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SDNEUR:
    """
        name: SDNEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 17.5
        maximum_order_size: None
        margin: False
    """
    name: str = "SDNEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 17.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 17.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SDNUSD:
    """
        name: SDNUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 17.5
        maximum_order_size: None
        margin: False
    """
    name: str = "SDNUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 17.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 17.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SGBEUR:
    """
        name: SGBEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 400
        maximum_order_size: None
        margin: False
    """
    name: str = "SGBEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 400
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 400
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SGBUSD:
    """
        name: SGBUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 400
        maximum_order_size: None
        margin: False
    """
    name: str = "SGBUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 400
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 400
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SHIBEUR:
    """
        name: SHIBEUR
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500000
        maximum_order_size: None
        margin: False
    """
    name: str = "SHIBEUR"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SHIBUSD:
    """
        name: SHIBUSD
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500000
        maximum_order_size: None
        margin: False
    """
    name: str = "SHIBUSD"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SHIBUSDT:
    """
        name: SHIBUSDT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500000
        maximum_order_size: None
        margin: False
    """
    name: str = "SHIBUSDT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500000
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500000
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SNXAUD:
    """
        name: SNXAUD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "SNXAUD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNXAUD"

    def __str__(self):
        return "SNXAUD"

    def __call__(self):
        return "SNXAUD"


SNXAUD = SNXAUD()
"""
    name: SNXAUD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SNXETH:
    """
        name: SNXETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "SNXETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SNXEUR:
    """
        name: SNXEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "SNXEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SNXGBP:
    """
        name: SNXGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "SNXGBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNXGBP"

    def __str__(self):
        return "SNXGBP"

    def __call__(self):
        return "SNXGBP"


SNXGBP = SNXGBP()
"""
    name: SNXGBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SNXUSD:
    """
        name: SNXUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "SNXUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SNXXBT:
    """
        name: SNXXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "SNXXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SOLEUR:
    """
        name: SOLEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.35
        maximum_order_size: None
        margin: True
    """
    name: str = "SOLEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.35
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.35
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SOLGBP:
    """
        name: SOLGBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.35
        maximum_order_size: None
        margin: True
    """
    name: str = "SOLGBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.35
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.35
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SOLUSD:
    """
        name: SOLUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.35
        maximum_order_size: None
        margin: True
    """
    name: str = "SOLUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.35
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.35
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SOLUSDT:
    """
        name: SOLUSDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.35
        maximum_order_size: None
        margin: False
    """
    name: str = "SOLUSDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.35
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.35
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SOLXBT:
    """
        name: SOLXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.35
        maximum_order_size: None
        margin: True
    """
    name: str = "SOLXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.35
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.35
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SPELLEUR:
    """
        name: SPELLEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7500
        maximum_order_size: None
        margin: False
    """
    name: str = "SPELLEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SPELLUSD:
    """
        name: SPELLUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 7500
        maximum_order_size: None
        margin: False
    """
    name: str = "SPELLUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 7500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 7500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SRMEUR:
    """
        name: SRMEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "SRMEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SRMGBP:
    """
        name: SRMGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "SRMGBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SRMGBP"

    def __str__(self):
        return "SRMGBP"

    def __call__(self):
        return "SRMGBP"


SRMGBP = SRMGBP()
"""
    name: SRMGBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SRMUSD:
    """
        name: SRMUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "SRMUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SRMXBT:
    """
        name: SRMXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "SRMXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STEPEUR:
    """
        name: STEPEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500
        maximum_order_size: None
        margin: False
    """
    name: str = "STEPEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STEPUSD:
    """
        name: STEPUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 500
        maximum_order_size: None
        margin: False
    """
    name: str = "STEPUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 500
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 500
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STGEUR:
    """
        name: STGEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12
        maximum_order_size: None
        margin: False
    """
    name: str = "STGEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STGUSD:
    """
        name: STGUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12
        maximum_order_size: None
        margin: False
    """
    name: str = "STGUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STORJETH:
    """
        name: STORJETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "STORJETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STORJETH"

    def __str__(self):
        return "STORJETH"

    def __call__(self):
        return "STORJETH"


STORJETH = STORJETH()
"""
    name: STORJETH
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STORJEUR:
    """
        name: STORJEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "STORJEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STORJUSD:
    """
        name: STORJUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "STORJUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STORJXBT:
    """
        name: STORJXBT
        precision: 0.000000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "STORJXBT"
    precision: int = 0.000000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STXEUR:
    """
        name: STXEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "STXEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class STXUSD:
    """
        name: STXUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 20
        maximum_order_size: None
        margin: False
    """
    name: str = "STXUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 20
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 20
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SUPEREUR:
    """
        name: SUPEREUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "SUPEREUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SUPERUSD:
    """
        name: SUPERUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "SUPERUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SUSHIEUR:
    """
        name: SUSHIEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHIEUR"
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
        return "SUSHIEUR"

    def __str__(self):
        return "SUSHIEUR"

    def __call__(self):
        return "SUSHIEUR"


SUSHIEUR = SUSHIEUR()
"""
    name: SUSHIEUR
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SUSHIGBP:
    """
        name: SUSHIGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHIGBP"
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
        return "SUSHIGBP"

    def __str__(self):
        return "SUSHIGBP"

    def __call__(self):
        return "SUSHIGBP"


SUSHIGBP = SUSHIGBP()
"""
    name: SUSHIGBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SUSHIUSD:
    """
        name: SUSHIUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHIUSD"
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
        return "SUSHIUSD"

    def __str__(self):
        return "SUSHIUSD"

    def __call__(self):
        return "SUSHIUSD"


SUSHIUSD = SUSHIUSD()
"""
    name: SUSHIUSD
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SUSHIXBT:
    """
        name: SUSHIXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHIXBT"
    precision: int = 0.0000001
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
        return "SUSHIXBT"

    def __str__(self):
        return "SUSHIXBT"

    def __call__(self):
        return "SUSHIXBT"


SUSHIXBT = SUSHIXBT()
"""
    name: SUSHIXBT
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SYNEUR:
    """
        name: SYNEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8
        maximum_order_size: None
        margin: False
    """
    name: str = "SYNEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class SYNUSD:
    """
        name: SYNUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 8
        maximum_order_size: None
        margin: False
    """
    name: str = "SYNUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 8
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 8
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TBTCETH:
    """
        name: TBTCETH
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "TBTCETH"
    precision: int = 0.001
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
        return "TBTCETH"

    def __str__(self):
        return "TBTCETH"

    def __call__(self):
        return "TBTCETH"


TBTCETH = TBTCETH()
"""
    name: TBTCETH
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TBTCEUR:
    """
        name: TBTCEUR
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "TBTCEUR"
    precision: int = 0.1
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
        return "TBTCEUR"

    def __str__(self):
        return "TBTCEUR"

    def __call__(self):
        return "TBTCEUR"


TBTCEUR = TBTCEUR()
"""
    name: TBTCEUR
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TBTCUSD:
    """
        name: TBTCUSD
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "TBTCUSD"
    precision: int = 0.1
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
        return "TBTCUSD"

    def __str__(self):
        return "TBTCUSD"

    def __call__(self):
        return "TBTCUSD"


TBTCUSD = TBTCUSD()
"""
    name: TBTCUSD
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TBTCXBT:
    """
        name: TBTCXBT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "TBTCXBT"
    precision: int = 0.00001
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
        return "TBTCXBT"

    def __str__(self):
        return "TBTCXBT"

    def __call__(self):
        return "TBTCXBT"


TBTCXBT = TBTCXBT()
"""
    name: TBTCXBT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TEEREUR:
    """
        name: TEEREUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "TEEREUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TEERUSD:
    """
        name: TEERUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 15
        maximum_order_size: None
        margin: False
    """
    name: str = "TEERUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 15
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 15
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TEUR:
    """
        name: TEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "TEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TLMEUR:
    """
        name: TLMEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 350
        maximum_order_size: None
        margin: False
    """
    name: str = "TLMEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 350
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 350
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TLMUSD:
    """
        name: TLMUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 350
        maximum_order_size: None
        margin: False
    """
    name: str = "TLMUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 350
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 350
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TOKEEUR:
    """
        name: TOKEEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "TOKEEUR"
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
        return "TOKEEUR"

    def __str__(self):
        return "TOKEEUR"

    def __call__(self):
        return "TOKEEUR"


TOKEEUR = TOKEEUR()
"""
    name: TOKEEUR
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TOKEUSD:
    """
        name: TOKEUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "TOKEUSD"
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
        return "TOKEUSD"

    def __str__(self):
        return "TOKEUSD"

    def __call__(self):
        return "TOKEUSD"


TOKEUSD = TOKEUSD()
"""
    name: TOKEUSD
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TRIBEEUR:
    """
        name: TRIBEEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "TRIBEEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TRIBEUSD:
    """
        name: TRIBEUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "TRIBEUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TRUEUR:
    """
        name: TRUEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: False
    """
    name: str = "TRUEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TRUUSD:
    """
        name: TRUUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: False
    """
    name: str = "TRUUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TRXETH:
    """
        name: TRXETH
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: True
    """
    name: str = "TRXETH"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class TRXEUR:
    """
        name: TRXEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: True
    """
    name: str = "TRXEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class TRXUSD:
    """
        name: TRXUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: True
    """
    name: str = "TRXUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class TRXXBT:
    """
        name: TRXXBT
        precision: 0.0000000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: True
    """
    name: str = "TRXXBT"
    precision: int = 0.0000000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class TUSD:
    """
        name: TUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "TUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TVKEUR:
    """
        name: TVKEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 175
        maximum_order_size: None
        margin: False
    """
    name: str = "TVKEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 175
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 175
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class TVKUSD:
    """
        name: TVKUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 175
        maximum_order_size: None
        margin: False
    """
    name: str = "TVKUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 175
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 175
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class UMAEUR:
    """
        name: UMAEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "UMAEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class UMAUSD:
    """
        name: UMAUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 3
        maximum_order_size: None
        margin: False
    """
    name: str = "UMAUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 3
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 3
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class UNFIEUR:
    """
        name: UNFIEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "UNFIEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class UNFIUSD:
    """
        name: UNFIUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "UNFIUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class UNIETH:
    """
        name: UNIETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "UNIETH"
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
        return "UNIETH"

    def __str__(self):
        return "UNIETH"

    def __call__(self):
        return "UNIETH"


UNIETH = UNIETH()
"""
    name: UNIETH
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class UNIEUR:
    """
        name: UNIEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: True
    """
    name: str = "UNIEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class UNIUSD:
    """
        name: UNIUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: True
    """
    name: str = "UNIUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class UNIXBT:
    """
        name: UNIXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1
        maximum_order_size: None
        margin: False
    """
    name: str = "UNIXBT"
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
        return "UNIXBT"

    def __str__(self):
        return "UNIXBT"

    def __call__(self):
        return "UNIXBT"


UNIXBT = UNIXBT()
"""
    name: UNIXBT
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class USDAED:
    """
        name: USDAED
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "USDAED"
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
        return "USDAED"

    def __str__(self):
        return "USDAED"

    def __call__(self):
        return "USDAED"


USDAED = USDAED()
"""
    name: USDAED
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class USDCAUD:
    """
        name: USDCAUD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDCAUD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDCCAD:
    """
        name: USDCCAD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "USDCCAD"
    precision: int = 0.0001
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
        return "USDCCAD"

    def __str__(self):
        return "USDCCAD"

    def __call__(self):
        return "USDCCAD"


USDCCAD = USDCCAD()
"""
    name: USDCCAD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class USDCCHF:
    """
        name: USDCCHF
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "USDCCHF"
    precision: int = 0.0001
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
        return "USDCCHF"

    def __str__(self):
        return "USDCCHF"

    def __call__(self):
        return "USDCCHF"


USDCCHF = USDCCHF()
"""
    name: USDCCHF
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class USDCEUR:
    """
        name: USDCEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDCEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDCGBP:
    """
        name: USDCGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDCGBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDCHF:
    """
        name: USDCHF
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "USDCHF"
    precision: int = 0.00001
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
        return "USDCHF"

    def __str__(self):
        return "USDCHF"

    def __call__(self):
        return "USDCHF"


USDCHF = USDCHF()
"""
    name: USDCHF
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class USDCUSD:
    """
        name: USDCUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDCUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDCUSDT:
    """
        name: USDCUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDCUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDTAUD:
    """
        name: USDTAUD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDTAUD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDTCAD:
    """
        name: USDTCAD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDTCAD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDTCHF:
    """
        name: USDTCHF
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDTCHF"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDTEUR:
    """
        name: USDTEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDTEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDTGBP:
    """
        name: USDTGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDTGBP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDTJPY:
    """
        name: USDTJPY
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDTJPY"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USDTZUSD:
    """
        name: USDTUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "USDTUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class USTEUR:
    """
        name: USTEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "USTEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class USTUSD:
    """
        name: USTUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "USTUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class USTUSDC:
    """
        name: USTUSDC
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "USTUSDC"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class USTUSDT:
    """
        name: USTUSDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 250
        maximum_order_size: None
        margin: False
    """
    name: str = "USTUSDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 250
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 250
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class WAVESETH:
    """
        name: WAVESETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "WAVESETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class WAVESEUR:
    """
        name: WAVESEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: True
    """
    name: str = "WAVESEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class WAVESUSD:
    """
        name: WAVESUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: True
    """
    name: str = "WAVESUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class WAVESXBT:
    """
        name: WAVESXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2.5
        maximum_order_size: None
        margin: False
    """
    name: str = "WAVESXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class WAXLEUR:
    """
        name: WAXLEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "WAXLEUR"
    precision: int = 0.0001
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
        return "WAXLEUR"

    def __str__(self):
        return "WAXLEUR"

    def __call__(self):
        return "WAXLEUR"


WAXLEUR = WAXLEUR()
"""
    name: WAXLEUR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class WAXLUSD:
    """
        name: WAXLUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "WAXLUSD"
    precision: int = 0.0001
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
        return "WAXLUSD"

    def __str__(self):
        return "WAXLUSD"

    def __call__(self):
        return "WAXLUSD"


WAXLUSD = WAXLUSD()
"""
    name: WAXLUSD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class WBTCEUR:
    """
        name: WBTCEUR
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "WBTCEUR"
    precision: int = 0.1
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
        return "WBTCEUR"

    def __str__(self):
        return "WBTCEUR"

    def __call__(self):
        return "WBTCEUR"


WBTCEUR = WBTCEUR()
"""
    name: WBTCEUR
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class WBTCUSD:
    """
        name: WBTCUSD
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "WBTCUSD"
    precision: int = 0.1
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
        return "WBTCUSD"

    def __str__(self):
        return "WBTCUSD"

    def __call__(self):
        return "WBTCUSD"


WBTCUSD = WBTCUSD()
"""
    name: WBTCUSD
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class WBTCXBT:
    """
        name: WBTCXBT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "WBTCXBT"
    precision: int = 0.00001
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
        return "WBTCXBT"

    def __str__(self):
        return "WBTCXBT"

    def __call__(self):
        return "WBTCXBT"


WBTCXBT = WBTCXBT()
"""
    name: WBTCXBT
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class WOOEUR:
    """
        name: WOOEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "WOOEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class WOOUSD:
    """
        name: WOOUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 50
        maximum_order_size: None
        margin: False
    """
    name: str = "WOOUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 50
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 50
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XBTAED:
    """
        name: XBTAED
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "XBTAED"
    precision: int = 1
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
        return "XBTAED"

    def __str__(self):
        return "XBTAED"

    def __call__(self):
        return "XBTAED"


XBTAED = XBTAED()
"""
    name: XBTAED
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XBTAUD:
    """
        name: XBTAUD
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: True
    """
    name: str = "XBTAUD"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTCHF:
    """
        name: XBTCHF
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: True
    """
    name: str = "XBTCHF"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTDAI:
    """
        name: XBTDAI
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "XBTDAI"
    precision: int = 0.1
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
        return "XBTDAI"

    def __str__(self):
        return "XBTDAI"

    def __call__(self):
        return "XBTDAI"


XBTDAI = XBTDAI()
"""
    name: XBTDAI
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XBTUSDC:
    """
        name: XBTUSDC
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: True
    """
    name: str = "XBTUSDC"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTUSDT:
    """
        name: XBTUSDT
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: True
    """
    name: str = "XBTUSDT"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XCNEUR:
    """
        name: XCNEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: False
    """
    name: str = "XCNEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XCNUSD:
    """
        name: XCNUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 100
        maximum_order_size: None
        margin: False
    """
    name: str = "XCNUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 100
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 100
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XDGEUR:
    """
        name: XDGEUR
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: True
    """
    name: str = "XDGEUR"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XDGUSD:
    """
        name: XDGUSD
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: True
    """
    name: str = "XDGUSD"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XDGUSDT:
    """
        name: XDGUSDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: False
    """
    name: str = "XDGUSDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XETCXETH:
    """
        name: ETCETH
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: True
    """
    name: str = "ETCETH"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XETCXXBT:
    """
        name: ETCXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: True
    """
    name: str = "ETCXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XETCZEUR:
    """
        name: ETCEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: True
    """
    name: str = "ETCEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XETCZUSD:
    """
        name: ETCUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: True
    """
    name: str = "ETCUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XETHXXBT:
    """
        name: ETHXBT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: True
    """
    name: str = "ETHXBT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XETHZCAD:
    """
        name: ETHCAD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: False
    """
    name: str = "ETHCAD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XETHZEUR:
    """
        name: ETHEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: True
    """
    name: str = "ETHEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XETHZGBP:
    """
        name: ETHGBP
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: True
    """
    name: str = "ETHGBP"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XETHZJPY:
    """
        name: ETHJPY
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: False
    """
    name: str = "ETHJPY"
    precision: int = 1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XETHZUSD:
    """
        name: ETHUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.01
        maximum_order_size: None
        margin: True
    """
    name: str = "ETHUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.01
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.01
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XLTCXXBT:
    """
        name: LTCXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: True
    """
    name: str = "LTCXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XLTCZEUR:
    """
        name: LTCEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: True
    """
    name: str = "LTCEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XLTCZJPY:
    """
        name: LTCJPY
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: False
    """
    name: str = "LTCJPY"
    precision: int = 1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XLTCZUSD:
    """
        name: LTCUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.06
        maximum_order_size: None
        margin: True
    """
    name: str = "LTCUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.06
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.06
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XMLNXETH:
    """
        name: MLNETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: False
    """
    name: str = "MLNETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XMLNXXBT:
    """
        name: MLNXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: False
    """
    name: str = "MLNXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XMLNZEUR:
    """
        name: MLNEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: False
    """
    name: str = "MLNEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XMLNZUSD:
    """
        name: MLNUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.25
        maximum_order_size: None
        margin: False
    """
    name: str = "MLNUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XMRUSDT:
    """
        name: XMRUSDT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: False
    """
    name: str = "XMRUSDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XREPXETH:
    """
        name: REPETH
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: True
    """
    name: str = "REPETH"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REPETH"

    def __str__(self):
        return "REPETH"

    def __call__(self):
        return "REPETH"


XREPXETH = XREPXETH()
"""
    name: REPETH
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XREPXXBT:
    """
        name: REPXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: True
    """
    name: str = "REPXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XREPZEUR:
    """
        name: REPEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: True
    """
    name: str = "REPEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XREPZUSD:
    """
        name: REPUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 1.5
        maximum_order_size: None
        margin: False
    """
    name: str = "REPUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 1.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 1.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XRPAUD:
    """
        name: XRPAUD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "XRPAUD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XRPETH:
    """
        name: XRPETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "XRPETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XRPGBP:
    """
        name: XRPGBP
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "XRPGBP"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XRPUSDT:
    """
        name: XRPUSDT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: True
    """
    name: str = "XRPUSDT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XRTEUR:
    """
        name: XRTEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "XRTEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XRTUSD:
    """
        name: XRTUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 2
        maximum_order_size: None
        margin: False
    """
    name: str = "XRTUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 2
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 2
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XTZAUD:
    """
        name: XTZAUD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "XTZAUD"
    precision: int = 0.0001
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
        return "XTZAUD"

    def __str__(self):
        return "XTZAUD"

    def __call__(self):
        return "XTZAUD"


XTZAUD = XTZAUD()
"""
    name: XTZAUD
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XTZETH:
    """
        name: XTZETH
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "XTZETH"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XTZEUR:
    """
        name: XTZEUR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "XTZEUR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XTZGBP:
    """
        name: XTZGBP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "XTZGBP"
    precision: int = 0.0001
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
        return "XTZGBP"

    def __str__(self):
        return "XTZGBP"

    def __call__(self):
        return "XTZGBP"


XTZGBP = XTZGBP()
"""
    name: XTZGBP
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XTZUSD:
    """
        name: XTZUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "XTZUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XTZUSDT:
    """
        name: XTZUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "XTZUSDT"
    precision: int = 0.0001
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
        return "XTZUSDT"

    def __str__(self):
        return "XTZUSDT"

    def __call__(self):
        return "XTZUSDT"


XTZUSDT = XTZUSDT()
"""
    name: XTZUSDT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XTZXBT:
    """
        name: XTZXBT
        precision: 0.0000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: True
    """
    name: str = "XTZXBT"
    precision: int = 0.0000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.0000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXBTZCAD:
    """
        name: XBTCAD
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: True
    """
    name: str = "XBTCAD"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXBTZEUR:
    """
        name: XBTEUR
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: True
    """
    name: str = "XBTEUR"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXBTZGBP:
    """
        name: XBTGBP
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: True
    """
    name: str = "XBTGBP"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXBTZJPY:
    """
        name: XBTJPY
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: False
    """
    name: str = "XBTJPY"
    precision: int = 1
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
        return "XBTJPY"

    def __str__(self):
        return "XBTJPY"

    def __call__(self):
        return "XBTJPY"


XXBTZJPY = XXBTZJPY()
"""
    name: XBTJPY
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XXBTZUSD:
    """
        name: XBTUSD
        precision: 0.1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.0001
        maximum_order_size: None
        margin: True
    """
    name: str = "XBTUSD"
    precision: int = 0.1
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.0001
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.0001
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXDGXXBT:
    """
        name: XDGXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: True
    """
    name: str = "XDGXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXLMXXBT:
    """
        name: XLMXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: True
    """
    name: str = "XLMXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXLMZAUD:
    """
        name: XLMAUD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: False
    """
    name: str = "XLMAUD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLMAUD"

    def __str__(self):
        return "XLMAUD"

    def __call__(self):
        return "XLMAUD"


XXLMZAUD = XXLMZAUD()
"""
    name: XLMAUD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XXLMZEUR:
    """
        name: XLMEUR
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: True
    """
    name: str = "XLMEUR"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXLMZGBP:
    """
        name: XLMGBP
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: False
    """
    name: str = "XLMGBP"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XXLMZUSD:
    """
        name: XLMUSD
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 60
        maximum_order_size: None
        margin: True
    """
    name: str = "XLMUSD"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 60
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 60
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXMRXXBT:
    """
        name: XMRXBT
        precision: 0.000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: True
    """
    name: str = "XMRXBT"
    precision: int = 0.000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXMRZEUR:
    """
        name: XMREUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: True
    """
    name: str = "XMREUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXMRZUSD:
    """
        name: XMRUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.05
        maximum_order_size: None
        margin: True
    """
    name: str = "XMRUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.05
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.05
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXRPXXBT:
    """
        name: XRPXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: True
    """
    name: str = "XRPXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXRPZCAD:
    """
        name: XRPCAD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "XRPCAD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XXRPZEUR:
    """
        name: XRPEUR
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: True
    """
    name: str = "XRPEUR"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XXRPZJPY:
    """
        name: XRPJPY
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: False
    """
    name: str = "XRPJPY"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XXRPZUSD:
    """
        name: XRPUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 12.5
        maximum_order_size: None
        margin: True
    """
    name: str = "XRPUSD"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 12.5
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 12.5
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XZECXXBT:
    """
        name: ZECXBT
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: True
    """
    name: str = "ZECXBT"
    precision: int = 0.00001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XZECZEUR:
    """
        name: ZECEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: True
    """
    name: str = "ZECEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XZECZUSD:
    """
        name: ZECUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.15
        maximum_order_size: None
        margin: True
    """
    name: str = "ZECUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 0.15
    maximum_order_size: float = None
    margin: bool = True

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
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.15
    maximum_order_size: None
    margin: True
"""


@dataclass(slots=True, frozen=True)
class YFIAUD:
    """
        name: YFIAUD
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.002
        maximum_order_size: None
        margin: False
    """
    name: str = "YFIAUD"
    precision: int = 1
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
        return "YFIAUD"

    def __str__(self):
        return "YFIAUD"

    def __call__(self):
        return "YFIAUD"


YFIAUD = YFIAUD()
"""
    name: YFIAUD
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.002
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class YFIETH:
    """
        name: YFIETH
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.002
        maximum_order_size: None
        margin: False
    """
    name: str = "YFIETH"
    precision: int = 0.01
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
        return "YFIETH"

    def __str__(self):
        return "YFIETH"

    def __call__(self):
        return "YFIETH"


YFIETH = YFIETH()
"""
    name: YFIETH
    precision: 0.01
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.002
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class YFIEUR:
    """
        name: YFIEUR
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.002
        maximum_order_size: None
        margin: False
    """
    name: str = "YFIEUR"
    precision: int = 1
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
        return "YFIEUR"

    def __str__(self):
        return "YFIEUR"

    def __call__(self):
        return "YFIEUR"


YFIEUR = YFIEUR()
"""
    name: YFIEUR
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.002
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class YFIGBP:
    """
        name: YFIGBP
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.002
        maximum_order_size: None
        margin: False
    """
    name: str = "YFIGBP"
    precision: int = 1
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
        return "YFIGBP"

    def __str__(self):
        return "YFIGBP"

    def __call__(self):
        return "YFIGBP"


YFIGBP = YFIGBP()
"""
    name: YFIGBP
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.002
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class YFIUSD:
    """
        name: YFIUSD
        precision: 1
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.002
        maximum_order_size: None
        margin: False
    """
    name: str = "YFIUSD"
    precision: int = 1
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
        return "YFIUSD"

    def __str__(self):
        return "YFIUSD"

    def __call__(self):
        return "YFIUSD"


YFIUSD = YFIUSD()
"""
    name: YFIUSD
    precision: 1
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.002
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class YFIXBT:
    """
        name: YFIXBT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 0.002
        maximum_order_size: None
        margin: False
    """
    name: str = "YFIXBT"
    precision: int = 0.0001
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
        return "YFIXBT"

    def __str__(self):
        return "YFIXBT"

    def __call__(self):
        return "YFIXBT"


YFIXBT = YFIXBT()
"""
    name: YFIXBT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 0.002
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class YGGEUR:
    """
        name: YGGEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "YGGEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class YGGUSD:
    """
        name: YGGUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "YGGUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ZEURZUSD:
    """
        name: EURUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "EURUSD"
    precision: int = 0.00001
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
        return "EURUSD"

    def __str__(self):
        return "EURUSD"

    def __call__(self):
        return "EURUSD"


ZEURZUSD = ZEURZUSD()
"""
    name: EURUSD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ZGBPZUSD:
    """
        name: GBPUSD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "GBPUSD"
    precision: int = 0.00001
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
        return "GBPUSD"

    def __str__(self):
        return "GBPUSD"

    def __call__(self):
        return "GBPUSD"


ZGBPZUSD = ZGBPZUSD()
"""
    name: GBPUSD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ZRXEUR:
    """
        name: ZRXEUR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "ZRXEUR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ZRXGBP:
    """
        name: ZRXGBP
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "ZRXGBP"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZRXGBP"

    def __str__(self):
        return "ZRXGBP"

    def __call__(self):
        return "ZRXGBP"


ZRXGBP = ZRXGBP()
"""
    name: ZRXGBP
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ZRXUSD:
    """
        name: ZRXUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "ZRXUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ZRXXBT:
    """
        name: ZRXXBT
        precision: 0.00000001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 25
        maximum_order_size: None
        margin: False
    """
    name: str = "ZRXXBT"
    precision: int = 0.00000001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = 25
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.00000001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 25
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ZUSDZCAD:
    """
        name: USDCAD
        precision: 0.00001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "USDCAD"
    precision: int = 0.00001
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
        return "USDCAD"

    def __str__(self):
        return "USDCAD"

    def __call__(self):
        return "USDCAD"


ZUSDZCAD = ZUSDZCAD()
"""
    name: USDCAD
    precision: 0.00001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ZUSDZJPY:
    """
        name: USDJPY
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: 5
        maximum_order_size: None
        margin: False
    """
    name: str = "USDJPY"
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
        return "USDJPY"

    def __str__(self):
        return "USDJPY"

    def __call__(self):
        return "USDJPY"


ZUSDZJPY = ZUSDZJPY()
"""
    name: USDJPY
    precision: 0.001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: 5
    maximum_order_size: None
    margin: False
"""
