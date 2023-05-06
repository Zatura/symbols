from ._model import Symbol


class ONEINCHEUR(Symbol):
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


ONEINCHEUR = ONEINCHEUR(*ONEINCHEUR._fields)


class ONEINCHUSD(Symbol):
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


ONEINCHUSD = ONEINCHUSD(*ONEINCHUSD._fields)


class AAVEETH(Symbol):
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


AAVEETH = AAVEETH(*AAVEETH._fields)


class AAVEEUR(Symbol):
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


AAVEEUR = AAVEEUR(*AAVEEUR._fields)


class AAVEGBP(Symbol):
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


AAVEGBP = AAVEGBP(*AAVEGBP._fields)


class AAVEUSD(Symbol):
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


AAVEUSD = AAVEUSD(*AAVEUSD._fields)


class AAVEXBT(Symbol):
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


AAVEXBT = AAVEXBT(*AAVEXBT._fields)


class ACAEUR(Symbol):
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


ACAEUR = ACAEUR(*ACAEUR._fields)


class ACAUSD(Symbol):
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


ACAUSD = ACAUSD(*ACAUSD._fields)


class ACHEUR(Symbol):
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


ACHEUR = ACHEUR(*ACHEUR._fields)


class ACHUSD(Symbol):
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


ACHUSD = ACHUSD(*ACHUSD._fields)


class ADAAUD(Symbol):
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


ADAAUD = ADAAUD(*ADAAUD._fields)


class ADAETH(Symbol):
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


ADAETH = ADAETH(*ADAETH._fields)


class ADAEUR(Symbol):
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


ADAEUR = ADAEUR(*ADAEUR._fields)


class ADAGBP(Symbol):
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


ADAGBP = ADAGBP(*ADAGBP._fields)


class ADAUSD(Symbol):
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


ADAUSD = ADAUSD(*ADAUSD._fields)


class ADAUSDT(Symbol):
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


ADAUSDT = ADAUSDT(*ADAUSDT._fields)


class ADAXBT(Symbol):
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


ADAXBT = ADAXBT(*ADAXBT._fields)


class ADXEUR(Symbol):
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


ADXEUR = ADXEUR(*ADXEUR._fields)


class ADXUSD(Symbol):
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


ADXUSD = ADXUSD(*ADXUSD._fields)


class AGLDEUR(Symbol):
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


AGLDEUR = AGLDEUR(*AGLDEUR._fields)


class AGLDUSD(Symbol):
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


AGLDUSD = AGLDUSD(*AGLDUSD._fields)


class AIREUR(Symbol):
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


AIREUR = AIREUR(*AIREUR._fields)


class AIRUSD(Symbol):
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


AIRUSD = AIRUSD(*AIRUSD._fields)


class AKTEUR(Symbol):
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


AKTEUR = AKTEUR(*AKTEUR._fields)


class AKTUSD(Symbol):
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


AKTUSD = AKTUSD(*AKTUSD._fields)


class ALCXEUR(Symbol):
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


ALCXEUR = ALCXEUR(*ALCXEUR._fields)


class ALCXUSD(Symbol):
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


ALCXUSD = ALCXUSD(*ALCXUSD._fields)


class ALGOETH(Symbol):
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


ALGOETH = ALGOETH(*ALGOETH._fields)


class ALGOEUR(Symbol):
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


ALGOEUR = ALGOEUR(*ALGOEUR._fields)


class ALGOGBP(Symbol):
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


ALGOGBP = ALGOGBP(*ALGOGBP._fields)


class ALGOUSD(Symbol):
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


ALGOUSD = ALGOUSD(*ALGOUSD._fields)


class ALGOUSDT(Symbol):
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


ALGOUSDT = ALGOUSDT(*ALGOUSDT._fields)


class ALGOXBT(Symbol):
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


ALGOXBT = ALGOXBT(*ALGOXBT._fields)


class ALICEEUR(Symbol):
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


ALICEEUR = ALICEEUR(*ALICEEUR._fields)


class ALICEUSD(Symbol):
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


ALICEUSD = ALICEUSD(*ALICEUSD._fields)


class ALPHAEUR(Symbol):
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


ALPHAEUR = ALPHAEUR(*ALPHAEUR._fields)


class ALPHAUSD(Symbol):
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


ALPHAUSD = ALPHAUSD(*ALPHAUSD._fields)


class ANKREUR(Symbol):
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


ANKREUR = ANKREUR(*ANKREUR._fields)


class ANKRUSD(Symbol):
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


ANKRUSD = ANKRUSD(*ANKRUSD._fields)


class ANKRXBT(Symbol):
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


ANKRXBT = ANKRXBT(*ANKRXBT._fields)


class ANTETH(Symbol):
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


ANTETH = ANTETH(*ANTETH._fields)


class ANTEUR(Symbol):
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


ANTEUR = ANTEUR(*ANTEUR._fields)


class ANTUSD(Symbol):
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


ANTUSD = ANTUSD(*ANTUSD._fields)


class ANTXBT(Symbol):
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


ANTXBT = ANTXBT(*ANTXBT._fields)


class APEEUR(Symbol):
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


APEEUR = APEEUR(*APEEUR._fields)


class APEUSD(Symbol):
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


APEUSD = APEUSD(*APEUSD._fields)


class APEUSDT(Symbol):
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


APEUSDT = APEUSDT(*APEUSDT._fields)


class API3EUR(Symbol):
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


API3EUR = API3EUR(*API3EUR._fields)


class API3USD(Symbol):
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


API3USD = API3USD(*API3USD._fields)


class APTEUR(Symbol):
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


APTEUR = APTEUR(*APTEUR._fields)


class APTUSD(Symbol):
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


APTUSD = APTUSD(*APTUSD._fields)


class ARBEUR(Symbol):
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


ARBEUR = ARBEUR(*ARBEUR._fields)


class ARBUSD(Symbol):
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


ARBUSD = ARBUSD(*ARBUSD._fields)


class ARPAEUR(Symbol):
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


ARPAEUR = ARPAEUR(*ARPAEUR._fields)


class ARPAUSD(Symbol):
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


ARPAUSD = ARPAUSD(*ARPAUSD._fields)


class ASTREUR(Symbol):
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


ASTREUR = ASTREUR(*ASTREUR._fields)


class ASTRUSD(Symbol):
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


ASTRUSD = ASTRUSD(*ASTRUSD._fields)


class ATLASEUR(Symbol):
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


ATLASEUR = ATLASEUR(*ATLASEUR._fields)


class ATLASUSD(Symbol):
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


ATLASUSD = ATLASUSD(*ATLASUSD._fields)


class ATOMETH(Symbol):
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


ATOMETH = ATOMETH(*ATOMETH._fields)


class ATOMEUR(Symbol):
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


ATOMEUR = ATOMEUR(*ATOMEUR._fields)


class ATOMGBP(Symbol):
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


ATOMGBP = ATOMGBP(*ATOMGBP._fields)


class ATOMUSD(Symbol):
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


ATOMUSD = ATOMUSD(*ATOMUSD._fields)


class ATOMUSDT(Symbol):
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


ATOMUSDT = ATOMUSDT(*ATOMUSDT._fields)


class ATOMXBT(Symbol):
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


ATOMXBT = ATOMXBT(*ATOMXBT._fields)


class AUDIOEUR(Symbol):
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


AUDIOEUR = AUDIOEUR(*AUDIOEUR._fields)


class AUDIOUSD(Symbol):
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


AUDIOUSD = AUDIOUSD(*AUDIOUSD._fields)


class AUDJPY(Symbol):
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


AUDJPY = AUDJPY(*AUDJPY._fields)


class AUDUSD(Symbol):
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


AUDUSD = AUDUSD(*AUDUSD._fields)


class AVAXEUR(Symbol):
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


AVAXEUR = AVAXEUR(*AVAXEUR._fields)


class AVAXUSD(Symbol):
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


AVAXUSD = AVAXUSD(*AVAXUSD._fields)


class AVAXUSDT(Symbol):
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


AVAXUSDT = AVAXUSDT(*AVAXUSDT._fields)


class AXSEUR(Symbol):
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


AXSEUR = AXSEUR(*AXSEUR._fields)


class AXSUSD(Symbol):
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


AXSUSD = AXSUSD(*AXSUSD._fields)


class BADGEREUR(Symbol):
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


BADGEREUR = BADGEREUR(*BADGEREUR._fields)


class BADGERUSD(Symbol):
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


BADGERUSD = BADGERUSD(*BADGERUSD._fields)


class BALEUR(Symbol):
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


BALEUR = BALEUR(*BALEUR._fields)


class BALUSD(Symbol):
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


BALUSD = BALUSD(*BALUSD._fields)


class BALXBT(Symbol):
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


BALXBT = BALXBT(*BALXBT._fields)


class BANDEUR(Symbol):
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


BANDEUR = BANDEUR(*BANDEUR._fields)


class BANDUSD(Symbol):
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


BANDUSD = BANDUSD(*BANDUSD._fields)


class BATETH(Symbol):
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


BATETH = BATETH(*BATETH._fields)


class BATEUR(Symbol):
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


BATEUR = BATEUR(*BATEUR._fields)


class BATJPY(Symbol):
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


BATJPY = BATJPY(*BATJPY._fields)


class BATUSD(Symbol):
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


BATUSD = BATUSD(*BATUSD._fields)


class BATXBT(Symbol):
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


BATXBT = BATXBT(*BATXBT._fields)


class BCHAUD(Symbol):
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


BCHAUD = BCHAUD(*BCHAUD._fields)


class BCHETH(Symbol):
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


BCHETH = BCHETH(*BCHETH._fields)


class BCHEUR(Symbol):
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


BCHEUR = BCHEUR(*BCHEUR._fields)


class BCHGBP(Symbol):
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


BCHGBP = BCHGBP(*BCHGBP._fields)


class BCHJPY(Symbol):
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


BCHJPY = BCHJPY(*BCHJPY._fields)


class BCHUSD(Symbol):
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


BCHUSD = BCHUSD(*BCHUSD._fields)


class BCHUSDT(Symbol):
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


BCHUSDT = BCHUSDT(*BCHUSDT._fields)


class BCHXBT(Symbol):
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


BCHXBT = BCHXBT(*BCHXBT._fields)


class BICOEUR(Symbol):
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


BICOEUR = BICOEUR(*BICOEUR._fields)


class BICOUSD(Symbol):
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


BICOUSD = BICOUSD(*BICOUSD._fields)


class BITEUR(Symbol):
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


BITEUR = BITEUR(*BITEUR._fields)


class BITUSD(Symbol):
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


BITUSD = BITUSD(*BITUSD._fields)


class BLUREUR(Symbol):
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


BLUREUR = BLUREUR(*BLUREUR._fields)


class BLURUSD(Symbol):
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


BLURUSD = BLURUSD(*BLURUSD._fields)


class BLZEUR(Symbol):
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


BLZEUR = BLZEUR(*BLZEUR._fields)


class BLZUSD(Symbol):
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


BLZUSD = BLZUSD(*BLZUSD._fields)


class BNCEUR(Symbol):
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


BNCEUR = BNCEUR(*BNCEUR._fields)


class BNCUSD(Symbol):
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


BNCUSD = BNCUSD(*BNCUSD._fields)


class BNTEUR(Symbol):
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


BNTEUR = BNTEUR(*BNTEUR._fields)


class BNTUSD(Symbol):
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


BNTUSD = BNTUSD(*BNTUSD._fields)


class BNTXBT(Symbol):
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


BNTXBT = BNTXBT(*BNTXBT._fields)


class BOBAEUR(Symbol):
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


BOBAEUR = BOBAEUR(*BOBAEUR._fields)


class BOBAUSD(Symbol):
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


BOBAUSD = BOBAUSD(*BOBAUSD._fields)


class BONDEUR(Symbol):
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


BONDEUR = BONDEUR(*BONDEUR._fields)


class BONDUSD(Symbol):
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


BONDUSD = BONDUSD(*BONDUSD._fields)


class BSXEUR(Symbol):
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


BSXEUR = BSXEUR(*BSXEUR._fields)


class BSXUSD(Symbol):
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


BSXUSD = BSXUSD(*BSXUSD._fields)


class BTTEUR(Symbol):
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


BTTEUR = BTTEUR(*BTTEUR._fields)


class BTTUSD(Symbol):
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


BTTUSD = BTTUSD(*BTTUSD._fields)


class C98EUR(Symbol):
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


C98EUR = C98EUR(*C98EUR._fields)


class C98USD(Symbol):
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


C98USD = C98USD(*C98USD._fields)


class CELREUR(Symbol):
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


CELREUR = CELREUR(*CELREUR._fields)


class CELRUSD(Symbol):
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


CELRUSD = CELRUSD(*CELRUSD._fields)


class CFGEUR(Symbol):
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


CFGEUR = CFGEUR(*CFGEUR._fields)


class CFGUSD(Symbol):
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


CFGUSD = CFGUSD(*CFGUSD._fields)


class CHREUR(Symbol):
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


CHREUR = CHREUR(*CHREUR._fields)


class CHRUSD(Symbol):
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


CHRUSD = CHRUSD(*CHRUSD._fields)


class CHZEUR(Symbol):
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


CHZEUR = CHZEUR(*CHZEUR._fields)


class CHZUSD(Symbol):
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


CHZUSD = CHZUSD(*CHZUSD._fields)


class COMPEUR(Symbol):
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


COMPEUR = COMPEUR(*COMPEUR._fields)


class COMPUSD(Symbol):
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


COMPUSD = COMPUSD(*COMPUSD._fields)


class COMPXBT(Symbol):
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


COMPXBT = COMPXBT(*COMPXBT._fields)


class COTIEUR(Symbol):
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


COTIEUR = COTIEUR(*COTIEUR._fields)


class COTIUSD(Symbol):
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


COTIUSD = COTIUSD(*COTIUSD._fields)


class CQTEUR(Symbol):
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


CQTEUR = CQTEUR(*CQTEUR._fields)


class CQTUSD(Symbol):
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


CQTUSD = CQTUSD(*CQTUSD._fields)


class CRVETH(Symbol):
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


CRVETH = CRVETH(*CRVETH._fields)


class CRVEUR(Symbol):
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


CRVEUR = CRVEUR(*CRVEUR._fields)


class CRVUSD(Symbol):
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


CRVUSD = CRVUSD(*CRVUSD._fields)


class CRVXBT(Symbol):
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


CRVXBT = CRVXBT(*CRVXBT._fields)


class CSMEUR(Symbol):
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


CSMEUR = CSMEUR(*CSMEUR._fields)


class CSMUSD(Symbol):
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


CSMUSD = CSMUSD(*CSMUSD._fields)


class CTSIEUR(Symbol):
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


CTSIEUR = CTSIEUR(*CTSIEUR._fields)


class CTSIUSD(Symbol):
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


CTSIUSD = CTSIUSD(*CTSIUSD._fields)


class CVCEUR(Symbol):
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


CVCEUR = CVCEUR(*CVCEUR._fields)


class CVCUSD(Symbol):
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


CVCUSD = CVCUSD(*CVCUSD._fields)


class CVXEUR(Symbol):
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


CVXEUR = CVXEUR(*CVXEUR._fields)


class CVXUSD(Symbol):
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


CVXUSD = CVXUSD(*CVXUSD._fields)


class DAIEUR(Symbol):
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


DAIEUR = DAIEUR(*DAIEUR._fields)


class DAIUSD(Symbol):
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


DAIUSD = DAIUSD(*DAIUSD._fields)


class DAIUSDT(Symbol):
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


DAIUSDT = DAIUSDT(*DAIUSDT._fields)


class DASHEUR(Symbol):
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


DASHEUR = DASHEUR(*DASHEUR._fields)


class DASHUSD(Symbol):
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


DASHUSD = DASHUSD(*DASHUSD._fields)


class DASHXBT(Symbol):
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


DASHXBT = DASHXBT(*DASHXBT._fields)


class DENTEUR(Symbol):
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


DENTEUR = DENTEUR(*DENTEUR._fields)


class DENTUSD(Symbol):
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


DENTUSD = DENTUSD(*DENTUSD._fields)


class DOTETH(Symbol):
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


DOTETH = DOTETH(*DOTETH._fields)


class DOTEUR(Symbol):
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


DOTEUR = DOTEUR(*DOTEUR._fields)


class DOTGBP(Symbol):
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


DOTGBP = DOTGBP(*DOTGBP._fields)


class DOTJPY(Symbol):
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


DOTJPY = DOTJPY(*DOTJPY._fields)


class DOTUSD(Symbol):
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


DOTUSD = DOTUSD(*DOTUSD._fields)


class DOTUSDT(Symbol):
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


DOTUSDT = DOTUSDT(*DOTUSDT._fields)


class DOTXBT(Symbol):
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


DOTXBT = DOTXBT(*DOTXBT._fields)


class DYDXEUR(Symbol):
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


DYDXEUR = DYDXEUR(*DYDXEUR._fields)


class DYDXUSD(Symbol):
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


DYDXUSD = DYDXUSD(*DYDXUSD._fields)


class EGLDEUR(Symbol):
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


EGLDEUR = EGLDEUR(*EGLDEUR._fields)


class EGLDUSD(Symbol):
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


EGLDUSD = EGLDUSD(*EGLDUSD._fields)


class ENJEUR(Symbol):
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


ENJEUR = ENJEUR(*ENJEUR._fields)


class ENJGBP(Symbol):
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


ENJGBP = ENJGBP(*ENJGBP._fields)


class ENJJPY(Symbol):
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


ENJJPY = ENJJPY(*ENJJPY._fields)


class ENJUSD(Symbol):
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


ENJUSD = ENJUSD(*ENJUSD._fields)


class ENJXBT(Symbol):
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


ENJXBT = ENJXBT(*ENJXBT._fields)


class ENSEUR(Symbol):
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


ENSEUR = ENSEUR(*ENSEUR._fields)


class ENSUSD(Symbol):
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


ENSUSD = ENSUSD(*ENSUSD._fields)


class EOSETH(Symbol):
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


EOSETH = EOSETH(*EOSETH._fields)


class EOSEUR(Symbol):
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


EOSEUR = EOSEUR(*EOSEUR._fields)


class EOSUSD(Symbol):
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


EOSUSD = EOSUSD(*EOSUSD._fields)


class EOSUSDT(Symbol):
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


EOSUSDT = EOSUSDT(*EOSUSDT._fields)


class EOSXBT(Symbol):
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


EOSXBT = EOSXBT(*EOSXBT._fields)


class ETH2_SETH(Symbol):
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


ETH2_SETH = ETH2_SETH(*ETH2_SETH._fields)


class ETHAED(Symbol):
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


ETHAED = ETHAED(*ETHAED._fields)


class ETHAUD(Symbol):
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


ETHAUD = ETHAUD(*ETHAUD._fields)


class ETHCHF(Symbol):
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


ETHCHF = ETHCHF(*ETHCHF._fields)


class ETHDAI(Symbol):
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


ETHDAI = ETHDAI(*ETHDAI._fields)


class ETHUSDC(Symbol):
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


ETHUSDC = ETHUSDC(*ETHUSDC._fields)


class ETHUSDT(Symbol):
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


ETHUSDT = ETHUSDT(*ETHUSDT._fields)


class ETHWETH(Symbol):
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


ETHWETH = ETHWETH(*ETHWETH._fields)


class ETHWEUR(Symbol):
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


ETHWEUR = ETHWEUR(*ETHWEUR._fields)


class ETHWUSD(Symbol):
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


ETHWUSD = ETHWUSD(*ETHWUSD._fields)


class EULEUR(Symbol):
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


EULEUR = EULEUR(*EULEUR._fields)


class EULUSD(Symbol):
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


EULUSD = EULUSD(*EULUSD._fields)


class EURAUD(Symbol):
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


EURAUD = EURAUD(*EURAUD._fields)


class EURCAD(Symbol):
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


EURCAD = EURCAD(*EURCAD._fields)


class EURCHF(Symbol):
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


EURCHF = EURCHF(*EURCHF._fields)


class EURGBP(Symbol):
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


EURGBP = EURGBP(*EURGBP._fields)


class EURJPY(Symbol):
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


EURJPY = EURJPY(*EURJPY._fields)


class EURTEUR(Symbol):
    """
        name: EURTEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EURTEUR"
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
        return "EURTEUR"

    def __str__(self):
        return "EURTEUR"

    def __call__(self):
        return "EURTEUR"


EURTEUR = EURTEUR(*EURTEUR._fields)


class EURTUSD(Symbol):
    """
        name: EURTUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EURTUSD"
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
        return "EURTUSD"

    def __str__(self):
        return "EURTUSD"

    def __call__(self):
        return "EURTUSD"


EURTUSD = EURTUSD(*EURTUSD._fields)


class EURTUSDT(Symbol):
    """
        name: EURTUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 5
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "EURTUSDT"
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
        return "EURTUSDT"

    def __str__(self):
        return "EURTUSDT"

    def __call__(self):
        return "EURTUSDT"


EURTUSDT = EURTUSDT(*EURTUSDT._fields)


class EWTEUR(Symbol):
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


EWTEUR = EWTEUR(*EWTEUR._fields)


class EWTGBP(Symbol):
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


EWTGBP = EWTGBP(*EWTGBP._fields)


class EWTUSD(Symbol):
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


EWTUSD = EWTUSD(*EWTUSD._fields)


class EWTXBT(Symbol):
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


EWTXBT = EWTXBT(*EWTXBT._fields)


class FARMEUR(Symbol):
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


FARMEUR = FARMEUR(*FARMEUR._fields)


class FARMUSD(Symbol):
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


FARMUSD = FARMUSD(*FARMUSD._fields)


class FETEUR(Symbol):
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


FETEUR = FETEUR(*FETEUR._fields)


class FETUSD(Symbol):
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


FETUSD = FETUSD(*FETUSD._fields)


class FIDAEUR(Symbol):
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


FIDAEUR = FIDAEUR(*FIDAEUR._fields)


class FIDAUSD(Symbol):
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


FIDAUSD = FIDAUSD(*FIDAUSD._fields)


class FILETH(Symbol):
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


FILETH = FILETH(*FILETH._fields)


class FILEUR(Symbol):
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


FILEUR = FILEUR(*FILEUR._fields)


class FILGBP(Symbol):
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


FILGBP = FILGBP(*FILGBP._fields)


class FILUSD(Symbol):
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


FILUSD = FILUSD(*FILUSD._fields)


class FILXBT(Symbol):
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


FILXBT = FILXBT(*FILXBT._fields)


class FISEUR(Symbol):
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


FISEUR = FISEUR(*FISEUR._fields)


class FISUSD(Symbol):
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


FISUSD = FISUSD(*FISUSD._fields)


class FLOWETH(Symbol):
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


FLOWETH = FLOWETH(*FLOWETH._fields)


class FLOWEUR(Symbol):
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


FLOWEUR = FLOWEUR(*FLOWEUR._fields)


class FLOWGBP(Symbol):
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


FLOWGBP = FLOWGBP(*FLOWGBP._fields)


class FLOWUSD(Symbol):
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


FLOWUSD = FLOWUSD(*FLOWUSD._fields)


class FLOWXBT(Symbol):
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


FLOWXBT = FLOWXBT(*FLOWXBT._fields)


class FLREUR(Symbol):
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


FLREUR = FLREUR(*FLREUR._fields)


class FLRUSD(Symbol):
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


FLRUSD = FLRUSD(*FLRUSD._fields)


class FORTHEUR(Symbol):
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


FORTHEUR = FORTHEUR(*FORTHEUR._fields)


class FORTHUSD(Symbol):
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


FORTHUSD = FORTHUSD(*FORTHUSD._fields)


class FTMEUR(Symbol):
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


FTMEUR = FTMEUR(*FTMEUR._fields)


class FTMUSD(Symbol):
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


FTMUSD = FTMUSD(*FTMUSD._fields)


class FXSEUR(Symbol):
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


FXSEUR = FXSEUR(*FXSEUR._fields)


class FXSUSD(Symbol):
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


FXSUSD = FXSUSD(*FXSUSD._fields)


class GALAEUR(Symbol):
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


GALAEUR = GALAEUR(*GALAEUR._fields)


class GALAUSD(Symbol):
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


GALAUSD = GALAUSD(*GALAUSD._fields)


class GALEUR(Symbol):
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


GALEUR = GALEUR(*GALEUR._fields)


class GALUSD(Symbol):
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


GALUSD = GALUSD(*GALUSD._fields)


class GARIEUR(Symbol):
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


GARIEUR = GARIEUR(*GARIEUR._fields)


class GARIUSD(Symbol):
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


GARIUSD = GARIUSD(*GARIUSD._fields)


class GHSTEUR(Symbol):
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


GHSTEUR = GHSTEUR(*GHSTEUR._fields)


class GHSTUSD(Symbol):
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


GHSTUSD = GHSTUSD(*GHSTUSD._fields)


class GHSTXBT(Symbol):
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


GHSTXBT = GHSTXBT(*GHSTXBT._fields)


class GLMREUR(Symbol):
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


GLMREUR = GLMREUR(*GLMREUR._fields)


class GLMRUSD(Symbol):
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


GLMRUSD = GLMRUSD(*GLMRUSD._fields)


class GMTEUR(Symbol):
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


GMTEUR = GMTEUR(*GMTEUR._fields)


class GMTUSD(Symbol):
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


GMTUSD = GMTUSD(*GMTUSD._fields)


class GMXEUR(Symbol):
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


GMXEUR = GMXEUR(*GMXEUR._fields)


class GMXUSD(Symbol):
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


GMXUSD = GMXUSD(*GMXUSD._fields)


class GNOEUR(Symbol):
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


GNOEUR = GNOEUR(*GNOEUR._fields)


class GNOUSD(Symbol):
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


GNOUSD = GNOUSD(*GNOUSD._fields)


class GNOXBT(Symbol):
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


GNOXBT = GNOXBT(*GNOXBT._fields)


class GRTEUR(Symbol):
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


GRTEUR = GRTEUR(*GRTEUR._fields)


class GRTGBP(Symbol):
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


GRTGBP = GRTGBP(*GRTGBP._fields)


class GRTUSD(Symbol):
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


GRTUSD = GRTUSD(*GRTUSD._fields)


class GRTXBT(Symbol):
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


GRTXBT = GRTXBT(*GRTXBT._fields)


class GSTEUR(Symbol):
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


GSTEUR = GSTEUR(*GSTEUR._fields)


class GSTUSD(Symbol):
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


GSTUSD = GSTUSD(*GSTUSD._fields)


class GTCEUR(Symbol):
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


GTCEUR = GTCEUR(*GTCEUR._fields)


class GTCUSD(Symbol):
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


GTCUSD = GTCUSD(*GTCUSD._fields)


class HDXEUR(Symbol):
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


HDXEUR = HDXEUR(*HDXEUR._fields)


class HDXUSD(Symbol):
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


HDXUSD = HDXUSD(*HDXUSD._fields)


class HFTEUR(Symbol):
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


HFTEUR = HFTEUR(*HFTEUR._fields)


class HFTUSD(Symbol):
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


HFTUSD = HFTUSD(*HFTUSD._fields)


class ICPEUR(Symbol):
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


ICPEUR = ICPEUR(*ICPEUR._fields)


class ICPUSD(Symbol):
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


ICPUSD = ICPUSD(*ICPUSD._fields)


class ICXETH(Symbol):
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


ICXETH = ICXETH(*ICXETH._fields)


class ICXEUR(Symbol):
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


ICXEUR = ICXEUR(*ICXEUR._fields)


class ICXUSD(Symbol):
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


ICXUSD = ICXUSD(*ICXUSD._fields)


class ICXXBT(Symbol):
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


ICXXBT = ICXXBT(*ICXXBT._fields)


class IDEXEUR(Symbol):
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


IDEXEUR = IDEXEUR(*IDEXEUR._fields)


class IDEXUSD(Symbol):
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


IDEXUSD = IDEXUSD(*IDEXUSD._fields)


class IMXEUR(Symbol):
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


IMXEUR = IMXEUR(*IMXEUR._fields)


class IMXUSD(Symbol):
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


IMXUSD = IMXUSD(*IMXUSD._fields)


class INJEUR(Symbol):
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


INJEUR = INJEUR(*INJEUR._fields)


class INJUSD(Symbol):
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


INJUSD = INJUSD(*INJUSD._fields)


class INTREUR(Symbol):
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


INTREUR = INTREUR(*INTREUR._fields)


class INTRUSD(Symbol):
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


INTRUSD = INTRUSD(*INTRUSD._fields)


class JASMYEUR(Symbol):
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


JASMYEUR = JASMYEUR(*JASMYEUR._fields)


class JASMYUSD(Symbol):
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


JASMYUSD = JASMYUSD(*JASMYUSD._fields)


class JUNOEUR(Symbol):
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


JUNOEUR = JUNOEUR(*JUNOEUR._fields)


class JUNOUSD(Symbol):
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


JUNOUSD = JUNOUSD(*JUNOUSD._fields)


class KAREUR(Symbol):
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


KAREUR = KAREUR(*KAREUR._fields)


class KARUSD(Symbol):
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


KARUSD = KARUSD(*KARUSD._fields)


class KAVAETH(Symbol):
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


KAVAETH = KAVAETH(*KAVAETH._fields)


class KAVAEUR(Symbol):
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


KAVAEUR = KAVAEUR(*KAVAEUR._fields)


class KAVAUSD(Symbol):
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


KAVAUSD = KAVAUSD(*KAVAUSD._fields)


class KAVAXBT(Symbol):
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


KAVAXBT = KAVAXBT(*KAVAXBT._fields)


class KEEPEUR(Symbol):
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


KEEPEUR = KEEPEUR(*KEEPEUR._fields)


class KEEPUSD(Symbol):
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


KEEPUSD = KEEPUSD(*KEEPUSD._fields)


class KEEPXBT(Symbol):
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


KEEPXBT = KEEPXBT(*KEEPXBT._fields)


class KEYEUR(Symbol):
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


KEYEUR = KEYEUR(*KEYEUR._fields)


class KEYUSD(Symbol):
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


KEYUSD = KEYUSD(*KEYUSD._fields)


class KILTEUR(Symbol):
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


KILTEUR = KILTEUR(*KILTEUR._fields)


class KILTUSD(Symbol):
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


KILTUSD = KILTUSD(*KILTUSD._fields)


class KINEUR(Symbol):
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


KINEUR = KINEUR(*KINEUR._fields)


class KINTEUR(Symbol):
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


KINTEUR = KINTEUR(*KINTEUR._fields)


class KINTUSD(Symbol):
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


KINTUSD = KINTUSD(*KINTUSD._fields)


class KINUSD(Symbol):
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


KINUSD = KINUSD(*KINUSD._fields)


class KNCETH(Symbol):
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


KNCETH = KNCETH(*KNCETH._fields)


class KNCEUR(Symbol):
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


KNCEUR = KNCEUR(*KNCEUR._fields)


class KNCUSD(Symbol):
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


KNCUSD = KNCUSD(*KNCUSD._fields)


class KNCXBT(Symbol):
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


KNCXBT = KNCXBT(*KNCXBT._fields)


class KP3REUR(Symbol):
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


KP3REUR = KP3REUR(*KP3REUR._fields)


class KP3RUSD(Symbol):
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


KP3RUSD = KP3RUSD(*KP3RUSD._fields)


class KSMDOT(Symbol):
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


KSMDOT = KSMDOT(*KSMDOT._fields)


class KSMETH(Symbol):
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


KSMETH = KSMETH(*KSMETH._fields)


class KSMEUR(Symbol):
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


KSMEUR = KSMEUR(*KSMEUR._fields)


class KSMGBP(Symbol):
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


KSMGBP = KSMGBP(*KSMGBP._fields)


class KSMUSD(Symbol):
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


KSMUSD = KSMUSD(*KSMUSD._fields)


class KSMXBT(Symbol):
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


KSMXBT = KSMXBT(*KSMXBT._fields)


class LCXEUR(Symbol):
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


LCXEUR = LCXEUR(*LCXEUR._fields)


class LCXUSD(Symbol):
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


LCXUSD = LCXUSD(*LCXUSD._fields)


class LDOEUR(Symbol):
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


LDOEUR = LDOEUR(*LDOEUR._fields)


class LDOUSD(Symbol):
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


LDOUSD = LDOUSD(*LDOUSD._fields)


class LINKAUD(Symbol):
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


LINKAUD = LINKAUD(*LINKAUD._fields)


class LINKETH(Symbol):
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


LINKETH = LINKETH(*LINKETH._fields)


class LINKEUR(Symbol):
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


LINKEUR = LINKEUR(*LINKEUR._fields)


class LINKGBP(Symbol):
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


LINKGBP = LINKGBP(*LINKGBP._fields)


class LINKJPY(Symbol):
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


LINKJPY = LINKJPY(*LINKJPY._fields)


class LINKUSD(Symbol):
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


LINKUSD = LINKUSD(*LINKUSD._fields)


class LINKUSDT(Symbol):
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


LINKUSDT = LINKUSDT(*LINKUSDT._fields)


class LINKXBT(Symbol):
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


LINKXBT = LINKXBT(*LINKXBT._fields)


class LPTEUR(Symbol):
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


LPTEUR = LPTEUR(*LPTEUR._fields)


class LPTGBP(Symbol):
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


LPTGBP = LPTGBP(*LPTGBP._fields)


class LPTUSD(Symbol):
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


LPTUSD = LPTUSD(*LPTUSD._fields)


class LPTXBT(Symbol):
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


LPTXBT = LPTXBT(*LPTXBT._fields)


class LRCEUR(Symbol):
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


LRCEUR = LRCEUR(*LRCEUR._fields)


class LRCUSD(Symbol):
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


LRCUSD = LRCUSD(*LRCUSD._fields)


class LSKETH(Symbol):
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


LSKETH = LSKETH(*LSKETH._fields)


class LSKEUR(Symbol):
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


LSKEUR = LSKEUR(*LSKEUR._fields)


class LSKUSD(Symbol):
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


LSKUSD = LSKUSD(*LSKUSD._fields)


class LSKXBT(Symbol):
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


LSKXBT = LSKXBT(*LSKXBT._fields)


class LTCAUD(Symbol):
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


LTCAUD = LTCAUD(*LTCAUD._fields)


class LTCETH(Symbol):
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


LTCETH = LTCETH(*LTCETH._fields)


class LTCGBP(Symbol):
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


LTCGBP = LTCGBP(*LTCGBP._fields)


class LTCUSDT(Symbol):
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


LTCUSDT = LTCUSDT(*LTCUSDT._fields)


class LUNA2EUR(Symbol):
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


LUNA2EUR = LUNA2EUR(*LUNA2EUR._fields)


class LUNA2USD(Symbol):
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


LUNA2USD = LUNA2USD(*LUNA2USD._fields)


class LUNAEUR(Symbol):
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


LUNAEUR = LUNAEUR(*LUNAEUR._fields)


class LUNAUSD(Symbol):
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


LUNAUSD = LUNAUSD(*LUNAUSD._fields)


class MANAETH(Symbol):
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


MANAETH = MANAETH(*MANAETH._fields)


class MANAEUR(Symbol):
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


MANAEUR = MANAEUR(*MANAEUR._fields)


class MANAUSD(Symbol):
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


MANAUSD = MANAUSD(*MANAUSD._fields)


class MANAUSDT(Symbol):
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


MANAUSDT = MANAUSDT(*MANAUSDT._fields)


class MANAXBT(Symbol):
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


MANAXBT = MANAXBT(*MANAXBT._fields)


class MASKEUR(Symbol):
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


MASKEUR = MASKEUR(*MASKEUR._fields)


class MASKUSD(Symbol):
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


MASKUSD = MASKUSD(*MASKUSD._fields)


class MATICEUR(Symbol):
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


MATICEUR = MATICEUR(*MATICEUR._fields)


class MATICGBP(Symbol):
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


MATICGBP = MATICGBP(*MATICGBP._fields)


class MATICUSD(Symbol):
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


MATICUSD = MATICUSD(*MATICUSD._fields)


class MATICUSDT(Symbol):
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


MATICUSDT = MATICUSDT(*MATICUSDT._fields)


class MATICXBT(Symbol):
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


MATICXBT = MATICXBT(*MATICXBT._fields)


class MCEUR(Symbol):
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


MCEUR = MCEUR(*MCEUR._fields)


class MCUSD(Symbol):
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


MCUSD = MCUSD(*MCUSD._fields)


class MINAEUR(Symbol):
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


MINAEUR = MINAEUR(*MINAEUR._fields)


class MINAGBP(Symbol):
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


MINAGBP = MINAGBP(*MINAGBP._fields)


class MINAUSD(Symbol):
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


MINAUSD = MINAUSD(*MINAUSD._fields)


class MINAXBT(Symbol):
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


MINAXBT = MINAXBT(*MINAXBT._fields)


class MIREUR(Symbol):
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


MIREUR = MIREUR(*MIREUR._fields)


class MIRUSD(Symbol):
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


MIRUSD = MIRUSD(*MIRUSD._fields)


class MKREUR(Symbol):
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


MKREUR = MKREUR(*MKREUR._fields)


class MKRUSD(Symbol):
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


MKRUSD = MKRUSD(*MKRUSD._fields)


class MKRXBT(Symbol):
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


MKRXBT = MKRXBT(*MKRXBT._fields)


class MNGOEUR(Symbol):
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


MNGOEUR = MNGOEUR(*MNGOEUR._fields)


class MNGOUSD(Symbol):
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


MNGOUSD = MNGOUSD(*MNGOUSD._fields)


class MOVREUR(Symbol):
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


MOVREUR = MOVREUR(*MOVREUR._fields)


class MOVRUSD(Symbol):
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


MOVRUSD = MOVRUSD(*MOVRUSD._fields)


class MSOLEUR(Symbol):
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


MSOLEUR = MSOLEUR(*MSOLEUR._fields)


class MSOLUSD(Symbol):
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


MSOLUSD = MSOLUSD(*MSOLUSD._fields)


class MULTIEUR(Symbol):
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


MULTIEUR = MULTIEUR(*MULTIEUR._fields)


class MULTIUSD(Symbol):
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


MULTIUSD = MULTIUSD(*MULTIUSD._fields)


class MVEUR(Symbol):
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


MVEUR = MVEUR(*MVEUR._fields)


class MVUSD(Symbol):
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


MVUSD = MVUSD(*MVUSD._fields)


class MXCEUR(Symbol):
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


MXCEUR = MXCEUR(*MXCEUR._fields)


class MXCUSD(Symbol):
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


MXCUSD = MXCUSD(*MXCUSD._fields)


class NANOETH(Symbol):
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


NANOETH = NANOETH(*NANOETH._fields)


class NANOEUR(Symbol):
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


NANOEUR = NANOEUR(*NANOEUR._fields)


class NANOUSD(Symbol):
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


NANOUSD = NANOUSD(*NANOUSD._fields)


class NANOXBT(Symbol):
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


NANOXBT = NANOXBT(*NANOXBT._fields)


class NEAREUR(Symbol):
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


NEAREUR = NEAREUR(*NEAREUR._fields)


class NEARUSD(Symbol):
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


NEARUSD = NEARUSD(*NEARUSD._fields)


class NMREUR(Symbol):
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


NMREUR = NMREUR(*NMREUR._fields)


class NMRUSD(Symbol):
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


NMRUSD = NMRUSD(*NMRUSD._fields)


class NODLEUR(Symbol):
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


NODLEUR = NODLEUR(*NODLEUR._fields)


class NODLUSD(Symbol):
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


NODLUSD = NODLUSD(*NODLUSD._fields)


class NYMEUR(Symbol):
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


NYMEUR = NYMEUR(*NYMEUR._fields)


class NYMUSD(Symbol):
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


NYMUSD = NYMUSD(*NYMUSD._fields)


class NYMXBT(Symbol):
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


NYMXBT = NYMXBT(*NYMXBT._fields)


class OCEANEUR(Symbol):
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


OCEANEUR = OCEANEUR(*OCEANEUR._fields)


class OCEANGBP(Symbol):
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


OCEANGBP = OCEANGBP(*OCEANGBP._fields)


class OCEANUSD(Symbol):
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


OCEANUSD = OCEANUSD(*OCEANUSD._fields)


class OCEANXBT(Symbol):
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


OCEANXBT = OCEANXBT(*OCEANXBT._fields)


class OGNEUR(Symbol):
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


OGNEUR = OGNEUR(*OGNEUR._fields)


class OGNUSD(Symbol):
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


OGNUSD = OGNUSD(*OGNUSD._fields)


class OMGETH(Symbol):
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


OMGETH = OMGETH(*OMGETH._fields)


class OMGEUR(Symbol):
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


OMGEUR = OMGEUR(*OMGEUR._fields)


class OMGJPY(Symbol):
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


OMGJPY = OMGJPY(*OMGJPY._fields)


class OMGUSD(Symbol):
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


OMGUSD = OMGUSD(*OMGUSD._fields)


class OMGXBT(Symbol):
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


OMGXBT = OMGXBT(*OMGXBT._fields)


class ORCAEUR(Symbol):
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


ORCAEUR = ORCAEUR(*ORCAEUR._fields)


class ORCAUSD(Symbol):
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


ORCAUSD = ORCAUSD(*ORCAUSD._fields)


class OXTEUR(Symbol):
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


OXTEUR = OXTEUR(*OXTEUR._fields)


class OXTUSD(Symbol):
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


OXTUSD = OXTUSD(*OXTUSD._fields)


class OXTXBT(Symbol):
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


OXTXBT = OXTXBT(*OXTXBT._fields)


class OXYEUR(Symbol):
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


OXYEUR = OXYEUR(*OXYEUR._fields)


class OXYUSD(Symbol):
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


OXYUSD = OXYUSD(*OXYUSD._fields)


class PARAEUR(Symbol):
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


PARAEUR = PARAEUR(*PARAEUR._fields)


class PARAUSD(Symbol):
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


PARAUSD = PARAUSD(*PARAUSD._fields)


class PAXGETH(Symbol):
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


PAXGETH = PAXGETH(*PAXGETH._fields)


class PAXGEUR(Symbol):
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


PAXGEUR = PAXGEUR(*PAXGEUR._fields)


class PAXGUSD(Symbol):
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


PAXGUSD = PAXGUSD(*PAXGUSD._fields)


class PAXGXBT(Symbol):
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


PAXGXBT = PAXGXBT(*PAXGXBT._fields)


class PERPEUR(Symbol):
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


PERPEUR = PERPEUR(*PERPEUR._fields)


class PERPUSD(Symbol):
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


PERPUSD = PERPUSD(*PERPUSD._fields)


class PHAEUR(Symbol):
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


PHAEUR = PHAEUR(*PHAEUR._fields)


class PHAUSD(Symbol):
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


PHAUSD = PHAUSD(*PHAUSD._fields)


class PLAEUR(Symbol):
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


PLAEUR = PLAEUR(*PLAEUR._fields)


class PLAUSD(Symbol):
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


PLAUSD = PLAUSD(*PLAUSD._fields)


class POLISEUR(Symbol):
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


POLISEUR = POLISEUR(*POLISEUR._fields)


class POLISUSD(Symbol):
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


POLISUSD = POLISUSD(*POLISUSD._fields)


class POLSEUR(Symbol):
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


POLSEUR = POLSEUR(*POLSEUR._fields)


class POLSUSD(Symbol):
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


POLSUSD = POLSUSD(*POLSUSD._fields)


class PONDEUR(Symbol):
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


PONDEUR = PONDEUR(*PONDEUR._fields)


class PONDUSD(Symbol):
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


PONDUSD = PONDUSD(*PONDUSD._fields)


class POWREUR(Symbol):
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


POWREUR = POWREUR(*POWREUR._fields)


class POWRUSD(Symbol):
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


POWRUSD = POWRUSD(*POWRUSD._fields)


class PSTAKEEUR(Symbol):
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


PSTAKEEUR = PSTAKEEUR(*PSTAKEEUR._fields)


class PSTAKEUSD(Symbol):
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


PSTAKEUSD = PSTAKEUSD(*PSTAKEUSD._fields)


class QNTEUR(Symbol):
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


QNTEUR = QNTEUR(*QNTEUR._fields)


class QNTUSD(Symbol):
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


QNTUSD = QNTUSD(*QNTUSD._fields)


class QTUMETH(Symbol):
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


QTUMETH = QTUMETH(*QTUMETH._fields)


class QTUMEUR(Symbol):
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


QTUMEUR = QTUMEUR(*QTUMEUR._fields)


class QTUMUSD(Symbol):
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


QTUMUSD = QTUMUSD(*QTUMUSD._fields)


class QTUMXBT(Symbol):
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


QTUMXBT = QTUMXBT(*QTUMXBT._fields)


class RADEUR(Symbol):
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


RADEUR = RADEUR(*RADEUR._fields)


class RADUSD(Symbol):
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


RADUSD = RADUSD(*RADUSD._fields)


class RAREEUR(Symbol):
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


RAREEUR = RAREEUR(*RAREEUR._fields)


class RAREUSD(Symbol):
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


RAREUSD = RAREUSD(*RAREUSD._fields)


class RARIEUR(Symbol):
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


RARIEUR = RARIEUR(*RARIEUR._fields)


class RARIUSD(Symbol):
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


RARIUSD = RARIUSD(*RARIUSD._fields)


class RARIXBT(Symbol):
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


RARIXBT = RARIXBT(*RARIXBT._fields)


class RAYEUR(Symbol):
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


RAYEUR = RAYEUR(*RAYEUR._fields)


class RAYUSD(Symbol):
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


RAYUSD = RAYUSD(*RAYUSD._fields)


class RBCEUR(Symbol):
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


RBCEUR = RBCEUR(*RBCEUR._fields)


class RBCUSD(Symbol):
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


RBCUSD = RBCUSD(*RBCUSD._fields)


class RENEUR(Symbol):
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


RENEUR = RENEUR(*RENEUR._fields)


class RENUSD(Symbol):
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


RENUSD = RENUSD(*RENUSD._fields)


class RENXBT(Symbol):
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


RENXBT = RENXBT(*RENXBT._fields)


class REPV2ETH(Symbol):
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


REPV2ETH = REPV2ETH(*REPV2ETH._fields)


class REPV2EUR(Symbol):
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


REPV2EUR = REPV2EUR(*REPV2EUR._fields)


class REPV2USD(Symbol):
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


REPV2USD = REPV2USD(*REPV2USD._fields)


class REPV2XBT(Symbol):
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


REPV2XBT = REPV2XBT(*REPV2XBT._fields)


class REQEUR(Symbol):
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


REQEUR = REQEUR(*REQEUR._fields)


class REQUSD(Symbol):
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


REQUSD = REQUSD(*REQUSD._fields)


class RLCEUR(Symbol):
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


RLCEUR = RLCEUR(*RLCEUR._fields)


class RLCUSD(Symbol):
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


RLCUSD = RLCUSD(*RLCUSD._fields)


class RNDREUR(Symbol):
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


RNDREUR = RNDREUR(*RNDREUR._fields)


class RNDRUSD(Symbol):
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


RNDRUSD = RNDRUSD(*RNDRUSD._fields)


class ROOKEUR(Symbol):
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


ROOKEUR = ROOKEUR(*ROOKEUR._fields)


class ROOKUSD(Symbol):
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


ROOKUSD = ROOKUSD(*ROOKUSD._fields)


class RPLEUR(Symbol):
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


RPLEUR = RPLEUR(*RPLEUR._fields)


class RPLUSD(Symbol):
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


RPLUSD = RPLUSD(*RPLUSD._fields)


class RUNEEUR(Symbol):
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


RUNEEUR = RUNEEUR(*RUNEEUR._fields)


class RUNEUSD(Symbol):
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


RUNEUSD = RUNEUSD(*RUNEUSD._fields)


class SAMOEUR(Symbol):
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


SAMOEUR = SAMOEUR(*SAMOEUR._fields)


class SAMOUSD(Symbol):
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


SAMOUSD = SAMOUSD(*SAMOUSD._fields)


class SANDEUR(Symbol):
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


SANDEUR = SANDEUR(*SANDEUR._fields)


class SANDGBP(Symbol):
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


SANDGBP = SANDGBP(*SANDGBP._fields)


class SANDUSD(Symbol):
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


SANDUSD = SANDUSD(*SANDUSD._fields)


class SANDXBT(Symbol):
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


SANDXBT = SANDXBT(*SANDXBT._fields)


class SBREUR(Symbol):
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


SBREUR = SBREUR(*SBREUR._fields)


class SBRUSD(Symbol):
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


SBRUSD = SBRUSD(*SBRUSD._fields)


class SCETH(Symbol):
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


SCETH = SCETH(*SCETH._fields)


class SCEUR(Symbol):
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


SCEUR = SCEUR(*SCEUR._fields)


class SCRTEUR(Symbol):
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


SCRTEUR = SCRTEUR(*SCRTEUR._fields)


class SCRTUSD(Symbol):
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


SCRTUSD = SCRTUSD(*SCRTUSD._fields)


class SCUSD(Symbol):
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


SCUSD = SCUSD(*SCUSD._fields)


class SCXBT(Symbol):
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


SCXBT = SCXBT(*SCXBT._fields)


class SDNEUR(Symbol):
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


SDNEUR = SDNEUR(*SDNEUR._fields)


class SDNUSD(Symbol):
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


SDNUSD = SDNUSD(*SDNUSD._fields)


class SGBEUR(Symbol):
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


SGBEUR = SGBEUR(*SGBEUR._fields)


class SGBUSD(Symbol):
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


SGBUSD = SGBUSD(*SGBUSD._fields)


class SHIBEUR(Symbol):
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


SHIBEUR = SHIBEUR(*SHIBEUR._fields)


class SHIBUSD(Symbol):
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


SHIBUSD = SHIBUSD(*SHIBUSD._fields)


class SHIBUSDT(Symbol):
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


SHIBUSDT = SHIBUSDT(*SHIBUSDT._fields)


class SNXETH(Symbol):
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


SNXETH = SNXETH(*SNXETH._fields)


class SNXEUR(Symbol):
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


SNXEUR = SNXEUR(*SNXEUR._fields)


class SNXUSD(Symbol):
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


SNXUSD = SNXUSD(*SNXUSD._fields)


class SNXXBT(Symbol):
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


SNXXBT = SNXXBT(*SNXXBT._fields)


class SOLEUR(Symbol):
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


SOLEUR = SOLEUR(*SOLEUR._fields)


class SOLGBP(Symbol):
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


SOLGBP = SOLGBP(*SOLGBP._fields)


class SOLUSD(Symbol):
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


SOLUSD = SOLUSD(*SOLUSD._fields)


class SOLUSDT(Symbol):
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


SOLUSDT = SOLUSDT(*SOLUSDT._fields)


class SOLXBT(Symbol):
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


SOLXBT = SOLXBT(*SOLXBT._fields)


class SPELLEUR(Symbol):
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


SPELLEUR = SPELLEUR(*SPELLEUR._fields)


class SPELLUSD(Symbol):
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


SPELLUSD = SPELLUSD(*SPELLUSD._fields)


class SRMEUR(Symbol):
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


SRMEUR = SRMEUR(*SRMEUR._fields)


class SRMUSD(Symbol):
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


SRMUSD = SRMUSD(*SRMUSD._fields)


class SRMXBT(Symbol):
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


SRMXBT = SRMXBT(*SRMXBT._fields)


class STEPEUR(Symbol):
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


STEPEUR = STEPEUR(*STEPEUR._fields)


class STEPUSD(Symbol):
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


STEPUSD = STEPUSD(*STEPUSD._fields)


class STGEUR(Symbol):
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


STGEUR = STGEUR(*STGEUR._fields)


class STGUSD(Symbol):
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


STGUSD = STGUSD(*STGUSD._fields)


class STORJEUR(Symbol):
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


STORJEUR = STORJEUR(*STORJEUR._fields)


class STORJUSD(Symbol):
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


STORJUSD = STORJUSD(*STORJUSD._fields)


class STORJXBT(Symbol):
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


STORJXBT = STORJXBT(*STORJXBT._fields)


class STXEUR(Symbol):
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


STXEUR = STXEUR(*STXEUR._fields)


class STXUSD(Symbol):
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


STXUSD = STXUSD(*STXUSD._fields)


class SUIEUR(Symbol):
    """
        name: SUIEUR
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.005
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SUIEUR"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.005
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUIEUR"

    def __str__(self):
        return "SUIEUR"

    def __call__(self):
        return "SUIEUR"


SUIEUR = SUIEUR(*SUIEUR._fields)


class SUIUSD(Symbol):
    """
        name: SUIUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: 0.005
        max_order_size: None
        has_margin: False
        exchange: kraken
    """
    name: str = "SUIUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = 0.005
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "kraken"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUIUSD"

    def __str__(self):
        return "SUIUSD"

    def __call__(self):
        return "SUIUSD"


SUIUSD = SUIUSD(*SUIUSD._fields)


class SUPEREUR(Symbol):
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


SUPEREUR = SUPEREUR(*SUPEREUR._fields)


class SUPERUSD(Symbol):
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


SUPERUSD = SUPERUSD(*SUPERUSD._fields)


class SUSHIEUR(Symbol):
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


SUSHIEUR = SUSHIEUR(*SUSHIEUR._fields)


class SUSHIGBP(Symbol):
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


SUSHIGBP = SUSHIGBP(*SUSHIGBP._fields)


class SUSHIUSD(Symbol):
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


SUSHIUSD = SUSHIUSD(*SUSHIUSD._fields)


class SUSHIXBT(Symbol):
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


SUSHIXBT = SUSHIXBT(*SUSHIXBT._fields)


class SYNEUR(Symbol):
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


SYNEUR = SYNEUR(*SYNEUR._fields)


class SYNUSD(Symbol):
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


SYNUSD = SYNUSD(*SYNUSD._fields)


class TBTCEUR(Symbol):
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


TBTCEUR = TBTCEUR(*TBTCEUR._fields)


class TBTCUSD(Symbol):
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


TBTCUSD = TBTCUSD(*TBTCUSD._fields)


class TBTCXBT(Symbol):
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


TBTCXBT = TBTCXBT(*TBTCXBT._fields)


class TEEREUR(Symbol):
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


TEEREUR = TEEREUR(*TEEREUR._fields)


class TEERUSD(Symbol):
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


TEERUSD = TEERUSD(*TEERUSD._fields)


class TEUR(Symbol):
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


TEUR = TEUR(*TEUR._fields)


class TLMEUR(Symbol):
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


TLMEUR = TLMEUR(*TLMEUR._fields)


class TLMUSD(Symbol):
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


TLMUSD = TLMUSD(*TLMUSD._fields)


class TOKEEUR(Symbol):
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


TOKEEUR = TOKEEUR(*TOKEEUR._fields)


class TOKEUSD(Symbol):
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


TOKEUSD = TOKEUSD(*TOKEUSD._fields)


class TRIBEEUR(Symbol):
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


TRIBEEUR = TRIBEEUR(*TRIBEEUR._fields)


class TRIBEUSD(Symbol):
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


TRIBEUSD = TRIBEUSD(*TRIBEUSD._fields)


class TRUEUR(Symbol):
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


TRUEUR = TRUEUR(*TRUEUR._fields)


class TRUUSD(Symbol):
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


TRUUSD = TRUUSD(*TRUUSD._fields)


class TRXETH(Symbol):
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


TRXETH = TRXETH(*TRXETH._fields)


class TRXEUR(Symbol):
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


TRXEUR = TRXEUR(*TRXEUR._fields)


class TRXUSD(Symbol):
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


TRXUSD = TRXUSD(*TRXUSD._fields)


class TRXXBT(Symbol):
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


TRXXBT = TRXXBT(*TRXXBT._fields)


class TUSD(Symbol):
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


TUSD = TUSD(*TUSD._fields)


class TVKEUR(Symbol):
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


TVKEUR = TVKEUR(*TVKEUR._fields)


class TVKUSD(Symbol):
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


TVKUSD = TVKUSD(*TVKUSD._fields)


class UMAEUR(Symbol):
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


UMAEUR = UMAEUR(*UMAEUR._fields)


class UMAUSD(Symbol):
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


UMAUSD = UMAUSD(*UMAUSD._fields)


class UNFIEUR(Symbol):
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


UNFIEUR = UNFIEUR(*UNFIEUR._fields)


class UNFIUSD(Symbol):
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


UNFIUSD = UNFIUSD(*UNFIUSD._fields)


class UNIETH(Symbol):
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


UNIETH = UNIETH(*UNIETH._fields)


class UNIEUR(Symbol):
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


UNIEUR = UNIEUR(*UNIEUR._fields)


class UNIUSD(Symbol):
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


UNIUSD = UNIUSD(*UNIUSD._fields)


class UNIXBT(Symbol):
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


UNIXBT = UNIXBT(*UNIXBT._fields)


class USDAED(Symbol):
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


USDAED = USDAED(*USDAED._fields)


class USDCAUD(Symbol):
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


USDCAUD = USDCAUD(*USDCAUD._fields)


class USDCCAD(Symbol):
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


USDCCAD = USDCCAD(*USDCCAD._fields)


class USDCCHF(Symbol):
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


USDCCHF = USDCCHF(*USDCCHF._fields)


class USDCEUR(Symbol):
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


USDCEUR = USDCEUR(*USDCEUR._fields)


class USDCGBP(Symbol):
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


USDCGBP = USDCGBP(*USDCGBP._fields)


class USDCHF(Symbol):
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


USDCHF = USDCHF(*USDCHF._fields)


class USDCUSD(Symbol):
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


USDCUSD = USDCUSD(*USDCUSD._fields)


class USDCUSDT(Symbol):
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


USDCUSDT = USDCUSDT(*USDCUSDT._fields)


class USDTAUD(Symbol):
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


USDTAUD = USDTAUD(*USDTAUD._fields)


class USDTCAD(Symbol):
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


USDTCAD = USDTCAD(*USDTCAD._fields)


class USDTCHF(Symbol):
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


USDTCHF = USDTCHF(*USDTCHF._fields)


class USDTEUR(Symbol):
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


USDTEUR = USDTEUR(*USDTEUR._fields)


class USDTGBP(Symbol):
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


USDTGBP = USDTGBP(*USDTGBP._fields)


class USDTJPY(Symbol):
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


USDTJPY = USDTJPY(*USDTJPY._fields)


class USDTZUSD(Symbol):
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


USDTZUSD = USDTZUSD(*USDTZUSD._fields)


class USTEUR(Symbol):
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


USTEUR = USTEUR(*USTEUR._fields)


class USTUSD(Symbol):
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


USTUSD = USTUSD(*USTUSD._fields)


class USTUSDC(Symbol):
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


USTUSDC = USTUSDC(*USTUSDC._fields)


class USTUSDT(Symbol):
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


USTUSDT = USTUSDT(*USTUSDT._fields)


class WAVESETH(Symbol):
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


WAVESETH = WAVESETH(*WAVESETH._fields)


class WAVESEUR(Symbol):
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


WAVESEUR = WAVESEUR(*WAVESEUR._fields)


class WAVESUSD(Symbol):
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


WAVESUSD = WAVESUSD(*WAVESUSD._fields)


class WAVESXBT(Symbol):
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


WAVESXBT = WAVESXBT(*WAVESXBT._fields)


class WAXLEUR(Symbol):
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


WAXLEUR = WAXLEUR(*WAXLEUR._fields)


class WAXLUSD(Symbol):
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


WAXLUSD = WAXLUSD(*WAXLUSD._fields)


class WBTCEUR(Symbol):
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


WBTCEUR = WBTCEUR(*WBTCEUR._fields)


class WBTCUSD(Symbol):
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


WBTCUSD = WBTCUSD(*WBTCUSD._fields)


class WBTCXBT(Symbol):
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


WBTCXBT = WBTCXBT(*WBTCXBT._fields)


class WOOEUR(Symbol):
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


WOOEUR = WOOEUR(*WOOEUR._fields)


class WOOUSD(Symbol):
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


WOOUSD = WOOUSD(*WOOUSD._fields)


class XBTAED(Symbol):
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


XBTAED = XBTAED(*XBTAED._fields)


class XBTAUD(Symbol):
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


XBTAUD = XBTAUD(*XBTAUD._fields)


class XBTCHF(Symbol):
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


XBTCHF = XBTCHF(*XBTCHF._fields)


class XBTDAI(Symbol):
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


XBTDAI = XBTDAI(*XBTDAI._fields)


class XBTUSDC(Symbol):
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


XBTUSDC = XBTUSDC(*XBTUSDC._fields)


class XBTUSDT(Symbol):
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


XBTUSDT = XBTUSDT(*XBTUSDT._fields)


class XCNEUR(Symbol):
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


XCNEUR = XCNEUR(*XCNEUR._fields)


class XCNUSD(Symbol):
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


XCNUSD = XCNUSD(*XCNUSD._fields)


class XDGEUR(Symbol):
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


XDGEUR = XDGEUR(*XDGEUR._fields)


class XDGUSD(Symbol):
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


XDGUSD = XDGUSD(*XDGUSD._fields)


class XDGUSDT(Symbol):
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


XDGUSDT = XDGUSDT(*XDGUSDT._fields)


class XETCXETH(Symbol):
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


XETCXETH = XETCXETH(*XETCXETH._fields)


class XETCXXBT(Symbol):
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


XETCXXBT = XETCXXBT(*XETCXXBT._fields)


class XETCZEUR(Symbol):
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


XETCZEUR = XETCZEUR(*XETCZEUR._fields)


class XETCZUSD(Symbol):
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


XETCZUSD = XETCZUSD(*XETCZUSD._fields)


class XETHXXBT(Symbol):
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


XETHXXBT = XETHXXBT(*XETHXXBT._fields)


class XETHZCAD(Symbol):
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


XETHZCAD = XETHZCAD(*XETHZCAD._fields)


class XETHZEUR(Symbol):
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


XETHZEUR = XETHZEUR(*XETHZEUR._fields)


class XETHZGBP(Symbol):
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


XETHZGBP = XETHZGBP(*XETHZGBP._fields)


class XETHZJPY(Symbol):
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


XETHZJPY = XETHZJPY(*XETHZJPY._fields)


class XETHZUSD(Symbol):
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


XETHZUSD = XETHZUSD(*XETHZUSD._fields)


class XLTCXXBT(Symbol):
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


XLTCXXBT = XLTCXXBT(*XLTCXXBT._fields)


class XLTCZEUR(Symbol):
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


XLTCZEUR = XLTCZEUR(*XLTCZEUR._fields)


class XLTCZJPY(Symbol):
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


XLTCZJPY = XLTCZJPY(*XLTCZJPY._fields)


class XLTCZUSD(Symbol):
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


XLTCZUSD = XLTCZUSD(*XLTCZUSD._fields)


class XMLNXETH(Symbol):
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


XMLNXETH = XMLNXETH(*XMLNXETH._fields)


class XMLNXXBT(Symbol):
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


XMLNXXBT = XMLNXXBT(*XMLNXXBT._fields)


class XMLNZEUR(Symbol):
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


XMLNZEUR = XMLNZEUR(*XMLNZEUR._fields)


class XMLNZUSD(Symbol):
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


XMLNZUSD = XMLNZUSD(*XMLNZUSD._fields)


class XMRUSDT(Symbol):
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


XMRUSDT = XMRUSDT(*XMRUSDT._fields)


class XREPXXBT(Symbol):
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


XREPXXBT = XREPXXBT(*XREPXXBT._fields)


class XREPZEUR(Symbol):
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


XREPZEUR = XREPZEUR(*XREPZEUR._fields)


class XREPZUSD(Symbol):
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


XREPZUSD = XREPZUSD(*XREPZUSD._fields)


class XRPAUD(Symbol):
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


XRPAUD = XRPAUD(*XRPAUD._fields)


class XRPETH(Symbol):
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


XRPETH = XRPETH(*XRPETH._fields)


class XRPGBP(Symbol):
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


XRPGBP = XRPGBP(*XRPGBP._fields)


class XRPUSDT(Symbol):
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


XRPUSDT = XRPUSDT(*XRPUSDT._fields)


class XRTEUR(Symbol):
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


XRTEUR = XRTEUR(*XRTEUR._fields)


class XRTUSD(Symbol):
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


XRTUSD = XRTUSD(*XRTUSD._fields)


class XTZAUD(Symbol):
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


XTZAUD = XTZAUD(*XTZAUD._fields)


class XTZETH(Symbol):
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


XTZETH = XTZETH(*XTZETH._fields)


class XTZEUR(Symbol):
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


XTZEUR = XTZEUR(*XTZEUR._fields)


class XTZGBP(Symbol):
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


XTZGBP = XTZGBP(*XTZGBP._fields)


class XTZUSD(Symbol):
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


XTZUSD = XTZUSD(*XTZUSD._fields)


class XTZUSDT(Symbol):
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


XTZUSDT = XTZUSDT(*XTZUSDT._fields)


class XTZXBT(Symbol):
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


XTZXBT = XTZXBT(*XTZXBT._fields)


class XXBTZCAD(Symbol):
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


XXBTZCAD = XXBTZCAD(*XXBTZCAD._fields)


class XXBTZEUR(Symbol):
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


XXBTZEUR = XXBTZEUR(*XXBTZEUR._fields)


class XXBTZGBP(Symbol):
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


XXBTZGBP = XXBTZGBP(*XXBTZGBP._fields)


class XXBTZJPY(Symbol):
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


XXBTZJPY = XXBTZJPY(*XXBTZJPY._fields)


class XXBTZUSD(Symbol):
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


XXBTZUSD = XXBTZUSD(*XXBTZUSD._fields)


class XXDGXXBT(Symbol):
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


XXDGXXBT = XXDGXXBT(*XXDGXXBT._fields)


class XXLMXXBT(Symbol):
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


XXLMXXBT = XXLMXXBT(*XXLMXXBT._fields)


class XXLMZEUR(Symbol):
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


XXLMZEUR = XXLMZEUR(*XXLMZEUR._fields)


class XXLMZGBP(Symbol):
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


XXLMZGBP = XXLMZGBP(*XXLMZGBP._fields)


class XXLMZUSD(Symbol):
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


XXLMZUSD = XXLMZUSD(*XXLMZUSD._fields)


class XXMRXXBT(Symbol):
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


XXMRXXBT = XXMRXXBT(*XXMRXXBT._fields)


class XXMRZEUR(Symbol):
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


XXMRZEUR = XXMRZEUR(*XXMRZEUR._fields)


class XXMRZUSD(Symbol):
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


XXMRZUSD = XXMRZUSD(*XXMRZUSD._fields)


class XXRPXXBT(Symbol):
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


XXRPXXBT = XXRPXXBT(*XXRPXXBT._fields)


class XXRPZCAD(Symbol):
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


XXRPZCAD = XXRPZCAD(*XXRPZCAD._fields)


class XXRPZEUR(Symbol):
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


XXRPZEUR = XXRPZEUR(*XXRPZEUR._fields)


class XXRPZJPY(Symbol):
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


XXRPZJPY = XXRPZJPY(*XXRPZJPY._fields)


class XXRPZUSD(Symbol):
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


XXRPZUSD = XXRPZUSD(*XXRPZUSD._fields)


class XZECXXBT(Symbol):
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


XZECXXBT = XZECXXBT(*XZECXXBT._fields)


class XZECZEUR(Symbol):
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


XZECZEUR = XZECZEUR(*XZECZEUR._fields)


class XZECZUSD(Symbol):
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


XZECZUSD = XZECZUSD(*XZECZUSD._fields)


class YFIEUR(Symbol):
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


YFIEUR = YFIEUR(*YFIEUR._fields)


class YFIUSD(Symbol):
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


YFIUSD = YFIUSD(*YFIUSD._fields)


class YFIXBT(Symbol):
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


YFIXBT = YFIXBT(*YFIXBT._fields)


class YGGEUR(Symbol):
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


YGGEUR = YGGEUR(*YGGEUR._fields)


class YGGUSD(Symbol):
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


YGGUSD = YGGUSD(*YGGUSD._fields)


class ZEURZUSD(Symbol):
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


ZEURZUSD = ZEURZUSD(*ZEURZUSD._fields)


class ZGBPZUSD(Symbol):
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


ZGBPZUSD = ZGBPZUSD(*ZGBPZUSD._fields)


class ZRXEUR(Symbol):
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


ZRXEUR = ZRXEUR(*ZRXEUR._fields)


class ZRXUSD(Symbol):
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


ZRXUSD = ZRXUSD(*ZRXUSD._fields)


class ZRXXBT(Symbol):
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


ZRXXBT = ZRXXBT(*ZRXXBT._fields)


class ZUSDZCAD(Symbol):
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


ZUSDZCAD = ZUSDZCAD(*ZUSDZCAD._fields)


class ZUSDZJPY(Symbol):
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


ZUSDZJPY = ZUSDZJPY(*ZUSDZJPY._fields)


class Kraken:

    ONEINCHEUR: Symbol = ONEINCHEUR
    ONEINCHUSD: Symbol = ONEINCHUSD
    AAVEETH: Symbol = AAVEETH
    AAVEEUR: Symbol = AAVEEUR
    AAVEGBP: Symbol = AAVEGBP
    AAVEUSD: Symbol = AAVEUSD
    AAVEXBT: Symbol = AAVEXBT
    ACAEUR: Symbol = ACAEUR
    ACAUSD: Symbol = ACAUSD
    ACHEUR: Symbol = ACHEUR
    ACHUSD: Symbol = ACHUSD
    ADAAUD: Symbol = ADAAUD
    ADAETH: Symbol = ADAETH
    ADAEUR: Symbol = ADAEUR
    ADAGBP: Symbol = ADAGBP
    ADAUSD: Symbol = ADAUSD
    ADAUSDT: Symbol = ADAUSDT
    ADAXBT: Symbol = ADAXBT
    ADXEUR: Symbol = ADXEUR
    ADXUSD: Symbol = ADXUSD
    AGLDEUR: Symbol = AGLDEUR
    AGLDUSD: Symbol = AGLDUSD
    AIREUR: Symbol = AIREUR
    AIRUSD: Symbol = AIRUSD
    AKTEUR: Symbol = AKTEUR
    AKTUSD: Symbol = AKTUSD
    ALCXEUR: Symbol = ALCXEUR
    ALCXUSD: Symbol = ALCXUSD
    ALGOETH: Symbol = ALGOETH
    ALGOEUR: Symbol = ALGOEUR
    ALGOGBP: Symbol = ALGOGBP
    ALGOUSD: Symbol = ALGOUSD
    ALGOUSDT: Symbol = ALGOUSDT
    ALGOXBT: Symbol = ALGOXBT
    ALICEEUR: Symbol = ALICEEUR
    ALICEUSD: Symbol = ALICEUSD
    ALPHAEUR: Symbol = ALPHAEUR
    ALPHAUSD: Symbol = ALPHAUSD
    ANKREUR: Symbol = ANKREUR
    ANKRUSD: Symbol = ANKRUSD
    ANKRXBT: Symbol = ANKRXBT
    ANTETH: Symbol = ANTETH
    ANTEUR: Symbol = ANTEUR
    ANTUSD: Symbol = ANTUSD
    ANTXBT: Symbol = ANTXBT
    APEEUR: Symbol = APEEUR
    APEUSD: Symbol = APEUSD
    APEUSDT: Symbol = APEUSDT
    API3EUR: Symbol = API3EUR
    API3USD: Symbol = API3USD
    APTEUR: Symbol = APTEUR
    APTUSD: Symbol = APTUSD
    ARBEUR: Symbol = ARBEUR
    ARBUSD: Symbol = ARBUSD
    ARPAEUR: Symbol = ARPAEUR
    ARPAUSD: Symbol = ARPAUSD
    ASTREUR: Symbol = ASTREUR
    ASTRUSD: Symbol = ASTRUSD
    ATLASEUR: Symbol = ATLASEUR
    ATLASUSD: Symbol = ATLASUSD
    ATOMETH: Symbol = ATOMETH
    ATOMEUR: Symbol = ATOMEUR
    ATOMGBP: Symbol = ATOMGBP
    ATOMUSD: Symbol = ATOMUSD
    ATOMUSDT: Symbol = ATOMUSDT
    ATOMXBT: Symbol = ATOMXBT
    AUDIOEUR: Symbol = AUDIOEUR
    AUDIOUSD: Symbol = AUDIOUSD
    AUDJPY: Symbol = AUDJPY
    AUDUSD: Symbol = AUDUSD
    AVAXEUR: Symbol = AVAXEUR
    AVAXUSD: Symbol = AVAXUSD
    AVAXUSDT: Symbol = AVAXUSDT
    AXSEUR: Symbol = AXSEUR
    AXSUSD: Symbol = AXSUSD
    BADGEREUR: Symbol = BADGEREUR
    BADGERUSD: Symbol = BADGERUSD
    BALEUR: Symbol = BALEUR
    BALUSD: Symbol = BALUSD
    BALXBT: Symbol = BALXBT
    BANDEUR: Symbol = BANDEUR
    BANDUSD: Symbol = BANDUSD
    BATETH: Symbol = BATETH
    BATEUR: Symbol = BATEUR
    BATJPY: Symbol = BATJPY
    BATUSD: Symbol = BATUSD
    BATXBT: Symbol = BATXBT
    BCHAUD: Symbol = BCHAUD
    BCHETH: Symbol = BCHETH
    BCHEUR: Symbol = BCHEUR
    BCHGBP: Symbol = BCHGBP
    BCHJPY: Symbol = BCHJPY
    BCHUSD: Symbol = BCHUSD
    BCHUSDT: Symbol = BCHUSDT
    BCHXBT: Symbol = BCHXBT
    BICOEUR: Symbol = BICOEUR
    BICOUSD: Symbol = BICOUSD
    BITEUR: Symbol = BITEUR
    BITUSD: Symbol = BITUSD
    BLUREUR: Symbol = BLUREUR
    BLURUSD: Symbol = BLURUSD
    BLZEUR: Symbol = BLZEUR
    BLZUSD: Symbol = BLZUSD
    BNCEUR: Symbol = BNCEUR
    BNCUSD: Symbol = BNCUSD
    BNTEUR: Symbol = BNTEUR
    BNTUSD: Symbol = BNTUSD
    BNTXBT: Symbol = BNTXBT
    BOBAEUR: Symbol = BOBAEUR
    BOBAUSD: Symbol = BOBAUSD
    BONDEUR: Symbol = BONDEUR
    BONDUSD: Symbol = BONDUSD
    BSXEUR: Symbol = BSXEUR
    BSXUSD: Symbol = BSXUSD
    BTTEUR: Symbol = BTTEUR
    BTTUSD: Symbol = BTTUSD
    C98EUR: Symbol = C98EUR
    C98USD: Symbol = C98USD
    CELREUR: Symbol = CELREUR
    CELRUSD: Symbol = CELRUSD
    CFGEUR: Symbol = CFGEUR
    CFGUSD: Symbol = CFGUSD
    CHREUR: Symbol = CHREUR
    CHRUSD: Symbol = CHRUSD
    CHZEUR: Symbol = CHZEUR
    CHZUSD: Symbol = CHZUSD
    COMPEUR: Symbol = COMPEUR
    COMPUSD: Symbol = COMPUSD
    COMPXBT: Symbol = COMPXBT
    COTIEUR: Symbol = COTIEUR
    COTIUSD: Symbol = COTIUSD
    CQTEUR: Symbol = CQTEUR
    CQTUSD: Symbol = CQTUSD
    CRVETH: Symbol = CRVETH
    CRVEUR: Symbol = CRVEUR
    CRVUSD: Symbol = CRVUSD
    CRVXBT: Symbol = CRVXBT
    CSMEUR: Symbol = CSMEUR
    CSMUSD: Symbol = CSMUSD
    CTSIEUR: Symbol = CTSIEUR
    CTSIUSD: Symbol = CTSIUSD
    CVCEUR: Symbol = CVCEUR
    CVCUSD: Symbol = CVCUSD
    CVXEUR: Symbol = CVXEUR
    CVXUSD: Symbol = CVXUSD
    DAIEUR: Symbol = DAIEUR
    DAIUSD: Symbol = DAIUSD
    DAIUSDT: Symbol = DAIUSDT
    DASHEUR: Symbol = DASHEUR
    DASHUSD: Symbol = DASHUSD
    DASHXBT: Symbol = DASHXBT
    DENTEUR: Symbol = DENTEUR
    DENTUSD: Symbol = DENTUSD
    DOTETH: Symbol = DOTETH
    DOTEUR: Symbol = DOTEUR
    DOTGBP: Symbol = DOTGBP
    DOTJPY: Symbol = DOTJPY
    DOTUSD: Symbol = DOTUSD
    DOTUSDT: Symbol = DOTUSDT
    DOTXBT: Symbol = DOTXBT
    DYDXEUR: Symbol = DYDXEUR
    DYDXUSD: Symbol = DYDXUSD
    EGLDEUR: Symbol = EGLDEUR
    EGLDUSD: Symbol = EGLDUSD
    ENJEUR: Symbol = ENJEUR
    ENJGBP: Symbol = ENJGBP
    ENJJPY: Symbol = ENJJPY
    ENJUSD: Symbol = ENJUSD
    ENJXBT: Symbol = ENJXBT
    ENSEUR: Symbol = ENSEUR
    ENSUSD: Symbol = ENSUSD
    EOSETH: Symbol = EOSETH
    EOSEUR: Symbol = EOSEUR
    EOSUSD: Symbol = EOSUSD
    EOSUSDT: Symbol = EOSUSDT
    EOSXBT: Symbol = EOSXBT
    ETH2_SETH: Symbol = ETH2_SETH
    ETHAED: Symbol = ETHAED
    ETHAUD: Symbol = ETHAUD
    ETHCHF: Symbol = ETHCHF
    ETHDAI: Symbol = ETHDAI
    ETHUSDC: Symbol = ETHUSDC
    ETHUSDT: Symbol = ETHUSDT
    ETHWETH: Symbol = ETHWETH
    ETHWEUR: Symbol = ETHWEUR
    ETHWUSD: Symbol = ETHWUSD
    EULEUR: Symbol = EULEUR
    EULUSD: Symbol = EULUSD
    EURAUD: Symbol = EURAUD
    EURCAD: Symbol = EURCAD
    EURCHF: Symbol = EURCHF
    EURGBP: Symbol = EURGBP
    EURJPY: Symbol = EURJPY
    EURTEUR: Symbol = EURTEUR
    EURTUSD: Symbol = EURTUSD
    EURTUSDT: Symbol = EURTUSDT
    EWTEUR: Symbol = EWTEUR
    EWTGBP: Symbol = EWTGBP
    EWTUSD: Symbol = EWTUSD
    EWTXBT: Symbol = EWTXBT
    FARMEUR: Symbol = FARMEUR
    FARMUSD: Symbol = FARMUSD
    FETEUR: Symbol = FETEUR
    FETUSD: Symbol = FETUSD
    FIDAEUR: Symbol = FIDAEUR
    FIDAUSD: Symbol = FIDAUSD
    FILETH: Symbol = FILETH
    FILEUR: Symbol = FILEUR
    FILGBP: Symbol = FILGBP
    FILUSD: Symbol = FILUSD
    FILXBT: Symbol = FILXBT
    FISEUR: Symbol = FISEUR
    FISUSD: Symbol = FISUSD
    FLOWETH: Symbol = FLOWETH
    FLOWEUR: Symbol = FLOWEUR
    FLOWGBP: Symbol = FLOWGBP
    FLOWUSD: Symbol = FLOWUSD
    FLOWXBT: Symbol = FLOWXBT
    FLREUR: Symbol = FLREUR
    FLRUSD: Symbol = FLRUSD
    FORTHEUR: Symbol = FORTHEUR
    FORTHUSD: Symbol = FORTHUSD
    FTMEUR: Symbol = FTMEUR
    FTMUSD: Symbol = FTMUSD
    FXSEUR: Symbol = FXSEUR
    FXSUSD: Symbol = FXSUSD
    GALAEUR: Symbol = GALAEUR
    GALAUSD: Symbol = GALAUSD
    GALEUR: Symbol = GALEUR
    GALUSD: Symbol = GALUSD
    GARIEUR: Symbol = GARIEUR
    GARIUSD: Symbol = GARIUSD
    GHSTEUR: Symbol = GHSTEUR
    GHSTUSD: Symbol = GHSTUSD
    GHSTXBT: Symbol = GHSTXBT
    GLMREUR: Symbol = GLMREUR
    GLMRUSD: Symbol = GLMRUSD
    GMTEUR: Symbol = GMTEUR
    GMTUSD: Symbol = GMTUSD
    GMXEUR: Symbol = GMXEUR
    GMXUSD: Symbol = GMXUSD
    GNOEUR: Symbol = GNOEUR
    GNOUSD: Symbol = GNOUSD
    GNOXBT: Symbol = GNOXBT
    GRTEUR: Symbol = GRTEUR
    GRTGBP: Symbol = GRTGBP
    GRTUSD: Symbol = GRTUSD
    GRTXBT: Symbol = GRTXBT
    GSTEUR: Symbol = GSTEUR
    GSTUSD: Symbol = GSTUSD
    GTCEUR: Symbol = GTCEUR
    GTCUSD: Symbol = GTCUSD
    HDXEUR: Symbol = HDXEUR
    HDXUSD: Symbol = HDXUSD
    HFTEUR: Symbol = HFTEUR
    HFTUSD: Symbol = HFTUSD
    ICPEUR: Symbol = ICPEUR
    ICPUSD: Symbol = ICPUSD
    ICXETH: Symbol = ICXETH
    ICXEUR: Symbol = ICXEUR
    ICXUSD: Symbol = ICXUSD
    ICXXBT: Symbol = ICXXBT
    IDEXEUR: Symbol = IDEXEUR
    IDEXUSD: Symbol = IDEXUSD
    IMXEUR: Symbol = IMXEUR
    IMXUSD: Symbol = IMXUSD
    INJEUR: Symbol = INJEUR
    INJUSD: Symbol = INJUSD
    INTREUR: Symbol = INTREUR
    INTRUSD: Symbol = INTRUSD
    JASMYEUR: Symbol = JASMYEUR
    JASMYUSD: Symbol = JASMYUSD
    JUNOEUR: Symbol = JUNOEUR
    JUNOUSD: Symbol = JUNOUSD
    KAREUR: Symbol = KAREUR
    KARUSD: Symbol = KARUSD
    KAVAETH: Symbol = KAVAETH
    KAVAEUR: Symbol = KAVAEUR
    KAVAUSD: Symbol = KAVAUSD
    KAVAXBT: Symbol = KAVAXBT
    KEEPEUR: Symbol = KEEPEUR
    KEEPUSD: Symbol = KEEPUSD
    KEEPXBT: Symbol = KEEPXBT
    KEYEUR: Symbol = KEYEUR
    KEYUSD: Symbol = KEYUSD
    KILTEUR: Symbol = KILTEUR
    KILTUSD: Symbol = KILTUSD
    KINEUR: Symbol = KINEUR
    KINTEUR: Symbol = KINTEUR
    KINTUSD: Symbol = KINTUSD
    KINUSD: Symbol = KINUSD
    KNCETH: Symbol = KNCETH
    KNCEUR: Symbol = KNCEUR
    KNCUSD: Symbol = KNCUSD
    KNCXBT: Symbol = KNCXBT
    KP3REUR: Symbol = KP3REUR
    KP3RUSD: Symbol = KP3RUSD
    KSMDOT: Symbol = KSMDOT
    KSMETH: Symbol = KSMETH
    KSMEUR: Symbol = KSMEUR
    KSMGBP: Symbol = KSMGBP
    KSMUSD: Symbol = KSMUSD
    KSMXBT: Symbol = KSMXBT
    LCXEUR: Symbol = LCXEUR
    LCXUSD: Symbol = LCXUSD
    LDOEUR: Symbol = LDOEUR
    LDOUSD: Symbol = LDOUSD
    LINKAUD: Symbol = LINKAUD
    LINKETH: Symbol = LINKETH
    LINKEUR: Symbol = LINKEUR
    LINKGBP: Symbol = LINKGBP
    LINKJPY: Symbol = LINKJPY
    LINKUSD: Symbol = LINKUSD
    LINKUSDT: Symbol = LINKUSDT
    LINKXBT: Symbol = LINKXBT
    LPTEUR: Symbol = LPTEUR
    LPTGBP: Symbol = LPTGBP
    LPTUSD: Symbol = LPTUSD
    LPTXBT: Symbol = LPTXBT
    LRCEUR: Symbol = LRCEUR
    LRCUSD: Symbol = LRCUSD
    LSKETH: Symbol = LSKETH
    LSKEUR: Symbol = LSKEUR
    LSKUSD: Symbol = LSKUSD
    LSKXBT: Symbol = LSKXBT
    LTCAUD: Symbol = LTCAUD
    LTCETH: Symbol = LTCETH
    LTCGBP: Symbol = LTCGBP
    LTCUSDT: Symbol = LTCUSDT
    LUNA2EUR: Symbol = LUNA2EUR
    LUNA2USD: Symbol = LUNA2USD
    LUNAEUR: Symbol = LUNAEUR
    LUNAUSD: Symbol = LUNAUSD
    MANAETH: Symbol = MANAETH
    MANAEUR: Symbol = MANAEUR
    MANAUSD: Symbol = MANAUSD
    MANAUSDT: Symbol = MANAUSDT
    MANAXBT: Symbol = MANAXBT
    MASKEUR: Symbol = MASKEUR
    MASKUSD: Symbol = MASKUSD
    MATICEUR: Symbol = MATICEUR
    MATICGBP: Symbol = MATICGBP
    MATICUSD: Symbol = MATICUSD
    MATICUSDT: Symbol = MATICUSDT
    MATICXBT: Symbol = MATICXBT
    MCEUR: Symbol = MCEUR
    MCUSD: Symbol = MCUSD
    MINAEUR: Symbol = MINAEUR
    MINAGBP: Symbol = MINAGBP
    MINAUSD: Symbol = MINAUSD
    MINAXBT: Symbol = MINAXBT
    MIREUR: Symbol = MIREUR
    MIRUSD: Symbol = MIRUSD
    MKREUR: Symbol = MKREUR
    MKRUSD: Symbol = MKRUSD
    MKRXBT: Symbol = MKRXBT
    MNGOEUR: Symbol = MNGOEUR
    MNGOUSD: Symbol = MNGOUSD
    MOVREUR: Symbol = MOVREUR
    MOVRUSD: Symbol = MOVRUSD
    MSOLEUR: Symbol = MSOLEUR
    MSOLUSD: Symbol = MSOLUSD
    MULTIEUR: Symbol = MULTIEUR
    MULTIUSD: Symbol = MULTIUSD
    MVEUR: Symbol = MVEUR
    MVUSD: Symbol = MVUSD
    MXCEUR: Symbol = MXCEUR
    MXCUSD: Symbol = MXCUSD
    NANOETH: Symbol = NANOETH
    NANOEUR: Symbol = NANOEUR
    NANOUSD: Symbol = NANOUSD
    NANOXBT: Symbol = NANOXBT
    NEAREUR: Symbol = NEAREUR
    NEARUSD: Symbol = NEARUSD
    NMREUR: Symbol = NMREUR
    NMRUSD: Symbol = NMRUSD
    NODLEUR: Symbol = NODLEUR
    NODLUSD: Symbol = NODLUSD
    NYMEUR: Symbol = NYMEUR
    NYMUSD: Symbol = NYMUSD
    NYMXBT: Symbol = NYMXBT
    OCEANEUR: Symbol = OCEANEUR
    OCEANGBP: Symbol = OCEANGBP
    OCEANUSD: Symbol = OCEANUSD
    OCEANXBT: Symbol = OCEANXBT
    OGNEUR: Symbol = OGNEUR
    OGNUSD: Symbol = OGNUSD
    OMGETH: Symbol = OMGETH
    OMGEUR: Symbol = OMGEUR
    OMGJPY: Symbol = OMGJPY
    OMGUSD: Symbol = OMGUSD
    OMGXBT: Symbol = OMGXBT
    ORCAEUR: Symbol = ORCAEUR
    ORCAUSD: Symbol = ORCAUSD
    OXTEUR: Symbol = OXTEUR
    OXTUSD: Symbol = OXTUSD
    OXTXBT: Symbol = OXTXBT
    OXYEUR: Symbol = OXYEUR
    OXYUSD: Symbol = OXYUSD
    PARAEUR: Symbol = PARAEUR
    PARAUSD: Symbol = PARAUSD
    PAXGETH: Symbol = PAXGETH
    PAXGEUR: Symbol = PAXGEUR
    PAXGUSD: Symbol = PAXGUSD
    PAXGXBT: Symbol = PAXGXBT
    PERPEUR: Symbol = PERPEUR
    PERPUSD: Symbol = PERPUSD
    PHAEUR: Symbol = PHAEUR
    PHAUSD: Symbol = PHAUSD
    PLAEUR: Symbol = PLAEUR
    PLAUSD: Symbol = PLAUSD
    POLISEUR: Symbol = POLISEUR
    POLISUSD: Symbol = POLISUSD
    POLSEUR: Symbol = POLSEUR
    POLSUSD: Symbol = POLSUSD
    PONDEUR: Symbol = PONDEUR
    PONDUSD: Symbol = PONDUSD
    POWREUR: Symbol = POWREUR
    POWRUSD: Symbol = POWRUSD
    PSTAKEEUR: Symbol = PSTAKEEUR
    PSTAKEUSD: Symbol = PSTAKEUSD
    QNTEUR: Symbol = QNTEUR
    QNTUSD: Symbol = QNTUSD
    QTUMETH: Symbol = QTUMETH
    QTUMEUR: Symbol = QTUMEUR
    QTUMUSD: Symbol = QTUMUSD
    QTUMXBT: Symbol = QTUMXBT
    RADEUR: Symbol = RADEUR
    RADUSD: Symbol = RADUSD
    RAREEUR: Symbol = RAREEUR
    RAREUSD: Symbol = RAREUSD
    RARIEUR: Symbol = RARIEUR
    RARIUSD: Symbol = RARIUSD
    RARIXBT: Symbol = RARIXBT
    RAYEUR: Symbol = RAYEUR
    RAYUSD: Symbol = RAYUSD
    RBCEUR: Symbol = RBCEUR
    RBCUSD: Symbol = RBCUSD
    RENEUR: Symbol = RENEUR
    RENUSD: Symbol = RENUSD
    RENXBT: Symbol = RENXBT
    REPV2ETH: Symbol = REPV2ETH
    REPV2EUR: Symbol = REPV2EUR
    REPV2USD: Symbol = REPV2USD
    REPV2XBT: Symbol = REPV2XBT
    REQEUR: Symbol = REQEUR
    REQUSD: Symbol = REQUSD
    RLCEUR: Symbol = RLCEUR
    RLCUSD: Symbol = RLCUSD
    RNDREUR: Symbol = RNDREUR
    RNDRUSD: Symbol = RNDRUSD
    ROOKEUR: Symbol = ROOKEUR
    ROOKUSD: Symbol = ROOKUSD
    RPLEUR: Symbol = RPLEUR
    RPLUSD: Symbol = RPLUSD
    RUNEEUR: Symbol = RUNEEUR
    RUNEUSD: Symbol = RUNEUSD
    SAMOEUR: Symbol = SAMOEUR
    SAMOUSD: Symbol = SAMOUSD
    SANDEUR: Symbol = SANDEUR
    SANDGBP: Symbol = SANDGBP
    SANDUSD: Symbol = SANDUSD
    SANDXBT: Symbol = SANDXBT
    SBREUR: Symbol = SBREUR
    SBRUSD: Symbol = SBRUSD
    SCETH: Symbol = SCETH
    SCEUR: Symbol = SCEUR
    SCRTEUR: Symbol = SCRTEUR
    SCRTUSD: Symbol = SCRTUSD
    SCUSD: Symbol = SCUSD
    SCXBT: Symbol = SCXBT
    SDNEUR: Symbol = SDNEUR
    SDNUSD: Symbol = SDNUSD
    SGBEUR: Symbol = SGBEUR
    SGBUSD: Symbol = SGBUSD
    SHIBEUR: Symbol = SHIBEUR
    SHIBUSD: Symbol = SHIBUSD
    SHIBUSDT: Symbol = SHIBUSDT
    SNXETH: Symbol = SNXETH
    SNXEUR: Symbol = SNXEUR
    SNXUSD: Symbol = SNXUSD
    SNXXBT: Symbol = SNXXBT
    SOLEUR: Symbol = SOLEUR
    SOLGBP: Symbol = SOLGBP
    SOLUSD: Symbol = SOLUSD
    SOLUSDT: Symbol = SOLUSDT
    SOLXBT: Symbol = SOLXBT
    SPELLEUR: Symbol = SPELLEUR
    SPELLUSD: Symbol = SPELLUSD
    SRMEUR: Symbol = SRMEUR
    SRMUSD: Symbol = SRMUSD
    SRMXBT: Symbol = SRMXBT
    STEPEUR: Symbol = STEPEUR
    STEPUSD: Symbol = STEPUSD
    STGEUR: Symbol = STGEUR
    STGUSD: Symbol = STGUSD
    STORJEUR: Symbol = STORJEUR
    STORJUSD: Symbol = STORJUSD
    STORJXBT: Symbol = STORJXBT
    STXEUR: Symbol = STXEUR
    STXUSD: Symbol = STXUSD
    SUIEUR: Symbol = SUIEUR
    SUIUSD: Symbol = SUIUSD
    SUPEREUR: Symbol = SUPEREUR
    SUPERUSD: Symbol = SUPERUSD
    SUSHIEUR: Symbol = SUSHIEUR
    SUSHIGBP: Symbol = SUSHIGBP
    SUSHIUSD: Symbol = SUSHIUSD
    SUSHIXBT: Symbol = SUSHIXBT
    SYNEUR: Symbol = SYNEUR
    SYNUSD: Symbol = SYNUSD
    TBTCEUR: Symbol = TBTCEUR
    TBTCUSD: Symbol = TBTCUSD
    TBTCXBT: Symbol = TBTCXBT
    TEEREUR: Symbol = TEEREUR
    TEERUSD: Symbol = TEERUSD
    TEUR: Symbol = TEUR
    TLMEUR: Symbol = TLMEUR
    TLMUSD: Symbol = TLMUSD
    TOKEEUR: Symbol = TOKEEUR
    TOKEUSD: Symbol = TOKEUSD
    TRIBEEUR: Symbol = TRIBEEUR
    TRIBEUSD: Symbol = TRIBEUSD
    TRUEUR: Symbol = TRUEUR
    TRUUSD: Symbol = TRUUSD
    TRXETH: Symbol = TRXETH
    TRXEUR: Symbol = TRXEUR
    TRXUSD: Symbol = TRXUSD
    TRXXBT: Symbol = TRXXBT
    TUSD: Symbol = TUSD
    TVKEUR: Symbol = TVKEUR
    TVKUSD: Symbol = TVKUSD
    UMAEUR: Symbol = UMAEUR
    UMAUSD: Symbol = UMAUSD
    UNFIEUR: Symbol = UNFIEUR
    UNFIUSD: Symbol = UNFIUSD
    UNIETH: Symbol = UNIETH
    UNIEUR: Symbol = UNIEUR
    UNIUSD: Symbol = UNIUSD
    UNIXBT: Symbol = UNIXBT
    USDAED: Symbol = USDAED
    USDCAUD: Symbol = USDCAUD
    USDCCAD: Symbol = USDCCAD
    USDCCHF: Symbol = USDCCHF
    USDCEUR: Symbol = USDCEUR
    USDCGBP: Symbol = USDCGBP
    USDCHF: Symbol = USDCHF
    USDCUSD: Symbol = USDCUSD
    USDCUSDT: Symbol = USDCUSDT
    USDTAUD: Symbol = USDTAUD
    USDTCAD: Symbol = USDTCAD
    USDTCHF: Symbol = USDTCHF
    USDTEUR: Symbol = USDTEUR
    USDTGBP: Symbol = USDTGBP
    USDTJPY: Symbol = USDTJPY
    USDTZUSD: Symbol = USDTZUSD
    USTEUR: Symbol = USTEUR
    USTUSD: Symbol = USTUSD
    USTUSDC: Symbol = USTUSDC
    USTUSDT: Symbol = USTUSDT
    WAVESETH: Symbol = WAVESETH
    WAVESEUR: Symbol = WAVESEUR
    WAVESUSD: Symbol = WAVESUSD
    WAVESXBT: Symbol = WAVESXBT
    WAXLEUR: Symbol = WAXLEUR
    WAXLUSD: Symbol = WAXLUSD
    WBTCEUR: Symbol = WBTCEUR
    WBTCUSD: Symbol = WBTCUSD
    WBTCXBT: Symbol = WBTCXBT
    WOOEUR: Symbol = WOOEUR
    WOOUSD: Symbol = WOOUSD
    XBTAED: Symbol = XBTAED
    XBTAUD: Symbol = XBTAUD
    XBTCHF: Symbol = XBTCHF
    XBTDAI: Symbol = XBTDAI
    XBTUSDC: Symbol = XBTUSDC
    XBTUSDT: Symbol = XBTUSDT
    XCNEUR: Symbol = XCNEUR
    XCNUSD: Symbol = XCNUSD
    XDGEUR: Symbol = XDGEUR
    XDGUSD: Symbol = XDGUSD
    XDGUSDT: Symbol = XDGUSDT
    XETCXETH: Symbol = XETCXETH
    XETCXXBT: Symbol = XETCXXBT
    XETCZEUR: Symbol = XETCZEUR
    XETCZUSD: Symbol = XETCZUSD
    XETHXXBT: Symbol = XETHXXBT
    XETHZCAD: Symbol = XETHZCAD
    XETHZEUR: Symbol = XETHZEUR
    XETHZGBP: Symbol = XETHZGBP
    XETHZJPY: Symbol = XETHZJPY
    XETHZUSD: Symbol = XETHZUSD
    XLTCXXBT: Symbol = XLTCXXBT
    XLTCZEUR: Symbol = XLTCZEUR
    XLTCZJPY: Symbol = XLTCZJPY
    XLTCZUSD: Symbol = XLTCZUSD
    XMLNXETH: Symbol = XMLNXETH
    XMLNXXBT: Symbol = XMLNXXBT
    XMLNZEUR: Symbol = XMLNZEUR
    XMLNZUSD: Symbol = XMLNZUSD
    XMRUSDT: Symbol = XMRUSDT
    XREPXXBT: Symbol = XREPXXBT
    XREPZEUR: Symbol = XREPZEUR
    XREPZUSD: Symbol = XREPZUSD
    XRPAUD: Symbol = XRPAUD
    XRPETH: Symbol = XRPETH
    XRPGBP: Symbol = XRPGBP
    XRPUSDT: Symbol = XRPUSDT
    XRTEUR: Symbol = XRTEUR
    XRTUSD: Symbol = XRTUSD
    XTZAUD: Symbol = XTZAUD
    XTZETH: Symbol = XTZETH
    XTZEUR: Symbol = XTZEUR
    XTZGBP: Symbol = XTZGBP
    XTZUSD: Symbol = XTZUSD
    XTZUSDT: Symbol = XTZUSDT
    XTZXBT: Symbol = XTZXBT
    XXBTZCAD: Symbol = XXBTZCAD
    XXBTZEUR: Symbol = XXBTZEUR
    XXBTZGBP: Symbol = XXBTZGBP
    XXBTZJPY: Symbol = XXBTZJPY
    XXBTZUSD: Symbol = XXBTZUSD
    XXDGXXBT: Symbol = XXDGXXBT
    XXLMXXBT: Symbol = XXLMXXBT
    XXLMZEUR: Symbol = XXLMZEUR
    XXLMZGBP: Symbol = XXLMZGBP
    XXLMZUSD: Symbol = XXLMZUSD
    XXMRXXBT: Symbol = XXMRXXBT
    XXMRZEUR: Symbol = XXMRZEUR
    XXMRZUSD: Symbol = XXMRZUSD
    XXRPXXBT: Symbol = XXRPXXBT
    XXRPZCAD: Symbol = XXRPZCAD
    XXRPZEUR: Symbol = XXRPZEUR
    XXRPZJPY: Symbol = XXRPZJPY
    XXRPZUSD: Symbol = XXRPZUSD
    XZECXXBT: Symbol = XZECXXBT
    XZECZEUR: Symbol = XZECZEUR
    XZECZUSD: Symbol = XZECZUSD
    YFIEUR: Symbol = YFIEUR
    YFIUSD: Symbol = YFIUSD
    YFIXBT: Symbol = YFIXBT
    YGGEUR: Symbol = YGGEUR
    YGGUSD: Symbol = YGGUSD
    ZEURZUSD: Symbol = ZEURZUSD
    ZGBPZUSD: Symbol = ZGBPZUSD
    ZRXEUR: Symbol = ZRXEUR
    ZRXUSD: Symbol = ZRXUSD
    ZRXXBT: Symbol = ZRXXBT
    ZUSDZCAD: Symbol = ZUSDZCAD
    ZUSDZJPY: Symbol = ZUSDZJPY

    def __iter__(self) -> list[Symbol]:
        return iter([ONEINCHEUR, ONEINCHUSD, AAVEETH, AAVEEUR, AAVEGBP, AAVEUSD, AAVEXBT, ACAEUR, ACAUSD, ACHEUR, ACHUSD, ADAAUD, ADAETH, ADAEUR, ADAGBP, ADAUSD, ADAUSDT, ADAXBT, ADXEUR, ADXUSD, AGLDEUR, AGLDUSD, AIREUR, AIRUSD, AKTEUR, AKTUSD, ALCXEUR, ALCXUSD, ALGOETH, ALGOEUR, ALGOGBP, ALGOUSD, ALGOUSDT, ALGOXBT, ALICEEUR, ALICEUSD, ALPHAEUR, ALPHAUSD, ANKREUR, ANKRUSD, ANKRXBT, ANTETH, ANTEUR, ANTUSD, ANTXBT, APEEUR, APEUSD, APEUSDT, API3EUR, API3USD, APTEUR, APTUSD, ARBEUR, ARBUSD, ARPAEUR, ARPAUSD, ASTREUR, ASTRUSD, ATLASEUR, ATLASUSD, ATOMETH, ATOMEUR, ATOMGBP, ATOMUSD, ATOMUSDT, ATOMXBT, AUDIOEUR, AUDIOUSD, AUDJPY, AUDUSD, AVAXEUR, AVAXUSD, AVAXUSDT, AXSEUR, AXSUSD, BADGEREUR, BADGERUSD, BALEUR, BALUSD, BALXBT, BANDEUR, BANDUSD, BATETH, BATEUR, BATJPY, BATUSD, BATXBT, BCHAUD, BCHETH, BCHEUR, BCHGBP, BCHJPY, BCHUSD, BCHUSDT, BCHXBT, BICOEUR, BICOUSD, BITEUR, BITUSD, BLUREUR, BLURUSD, BLZEUR, BLZUSD, BNCEUR, BNCUSD, BNTEUR, BNTUSD, BNTXBT, BOBAEUR, BOBAUSD, BONDEUR, BONDUSD, BSXEUR, BSXUSD, BTTEUR, BTTUSD, C98EUR, C98USD, CELREUR, CELRUSD, CFGEUR, CFGUSD, CHREUR, CHRUSD, CHZEUR, CHZUSD, COMPEUR, COMPUSD, COMPXBT, COTIEUR, COTIUSD, CQTEUR, CQTUSD, CRVETH, CRVEUR, CRVUSD, CRVXBT, CSMEUR, CSMUSD, CTSIEUR, CTSIUSD, CVCEUR, CVCUSD, CVXEUR, CVXUSD, DAIEUR, DAIUSD, DAIUSDT, DASHEUR, DASHUSD, DASHXBT, DENTEUR, DENTUSD, DOTETH, DOTEUR, DOTGBP, DOTJPY, DOTUSD, DOTUSDT, DOTXBT, DYDXEUR, DYDXUSD, EGLDEUR, EGLDUSD, ENJEUR, ENJGBP, ENJJPY, ENJUSD, ENJXBT, ENSEUR, ENSUSD, EOSETH, EOSEUR, EOSUSD, EOSUSDT, EOSXBT, ETH2_SETH, ETHAED, ETHAUD, ETHCHF, ETHDAI, ETHUSDC, ETHUSDT, ETHWETH, ETHWEUR, ETHWUSD, EULEUR, EULUSD, EURAUD, EURCAD, EURCHF, EURGBP, EURJPY, EURTEUR, EURTUSD, EURTUSDT, EWTEUR, EWTGBP, EWTUSD, EWTXBT, FARMEUR, FARMUSD, FETEUR, FETUSD, FIDAEUR, FIDAUSD, FILETH, FILEUR, FILGBP, FILUSD, FILXBT, FISEUR, FISUSD, FLOWETH, FLOWEUR, FLOWGBP, FLOWUSD, FLOWXBT, FLREUR, FLRUSD, FORTHEUR, FORTHUSD, FTMEUR, FTMUSD, FXSEUR, FXSUSD, GALAEUR, GALAUSD, GALEUR, GALUSD, GARIEUR, GARIUSD, GHSTEUR, GHSTUSD, GHSTXBT, GLMREUR, GLMRUSD, GMTEUR, GMTUSD, GMXEUR, GMXUSD, GNOEUR, GNOUSD, GNOXBT, GRTEUR, GRTGBP, GRTUSD, GRTXBT, GSTEUR, GSTUSD, GTCEUR, GTCUSD, HDXEUR, HDXUSD, HFTEUR, HFTUSD, ICPEUR, ICPUSD, ICXETH, ICXEUR, ICXUSD, ICXXBT, IDEXEUR, IDEXUSD, IMXEUR, IMXUSD, INJEUR, INJUSD, INTREUR, INTRUSD, JASMYEUR, JASMYUSD, JUNOEUR, JUNOUSD, KAREUR, KARUSD, KAVAETH, KAVAEUR, KAVAUSD, KAVAXBT, KEEPEUR, KEEPUSD, KEEPXBT, KEYEUR, KEYUSD, KILTEUR, KILTUSD, KINEUR, KINTEUR, KINTUSD, KINUSD, KNCETH, KNCEUR, KNCUSD, KNCXBT, KP3REUR, KP3RUSD, KSMDOT, KSMETH, KSMEUR, KSMGBP, KSMUSD, KSMXBT, LCXEUR, LCXUSD, LDOEUR, LDOUSD, LINKAUD, LINKETH, LINKEUR, LINKGBP, LINKJPY, LINKUSD, LINKUSDT, LINKXBT, LPTEUR, LPTGBP, LPTUSD, LPTXBT, LRCEUR, LRCUSD, LSKETH, LSKEUR, LSKUSD, LSKXBT, LTCAUD, LTCETH, LTCGBP, LTCUSDT, LUNA2EUR, LUNA2USD, LUNAEUR, LUNAUSD, MANAETH, MANAEUR, MANAUSD, MANAUSDT, MANAXBT, MASKEUR, MASKUSD, MATICEUR, MATICGBP, MATICUSD, MATICUSDT, MATICXBT, MCEUR, MCUSD, MINAEUR, MINAGBP, MINAUSD, MINAXBT, MIREUR, MIRUSD, MKREUR, MKRUSD, MKRXBT, MNGOEUR, MNGOUSD, MOVREUR, MOVRUSD, MSOLEUR, MSOLUSD, MULTIEUR, MULTIUSD, MVEUR, MVUSD, MXCEUR, MXCUSD, NANOETH, NANOEUR, NANOUSD, NANOXBT, NEAREUR, NEARUSD, NMREUR, NMRUSD, NODLEUR, NODLUSD, NYMEUR, NYMUSD, NYMXBT, OCEANEUR, OCEANGBP, OCEANUSD, OCEANXBT, OGNEUR, OGNUSD, OMGETH, OMGEUR, OMGJPY, OMGUSD, OMGXBT, ORCAEUR, ORCAUSD, OXTEUR, OXTUSD, OXTXBT, OXYEUR, OXYUSD, PARAEUR, PARAUSD, PAXGETH, PAXGEUR, PAXGUSD, PAXGXBT, PERPEUR, PERPUSD, PHAEUR, PHAUSD, PLAEUR, PLAUSD, POLISEUR, POLISUSD, POLSEUR, POLSUSD, PONDEUR, PONDUSD, POWREUR, POWRUSD, PSTAKEEUR, PSTAKEUSD, QNTEUR, QNTUSD, QTUMETH, QTUMEUR, QTUMUSD, QTUMXBT, RADEUR, RADUSD, RAREEUR, RAREUSD, RARIEUR, RARIUSD, RARIXBT, RAYEUR, RAYUSD, RBCEUR, RBCUSD, RENEUR, RENUSD, RENXBT, REPV2ETH, REPV2EUR, REPV2USD, REPV2XBT, REQEUR, REQUSD, RLCEUR, RLCUSD, RNDREUR, RNDRUSD, ROOKEUR, ROOKUSD, RPLEUR, RPLUSD, RUNEEUR, RUNEUSD, SAMOEUR, SAMOUSD, SANDEUR, SANDGBP, SANDUSD, SANDXBT, SBREUR, SBRUSD, SCETH, SCEUR, SCRTEUR, SCRTUSD, SCUSD, SCXBT, SDNEUR, SDNUSD, SGBEUR, SGBUSD, SHIBEUR, SHIBUSD, SHIBUSDT, SNXETH, SNXEUR, SNXUSD, SNXXBT, SOLEUR, SOLGBP, SOLUSD, SOLUSDT, SOLXBT, SPELLEUR, SPELLUSD, SRMEUR, SRMUSD, SRMXBT, STEPEUR, STEPUSD, STGEUR, STGUSD, STORJEUR, STORJUSD, STORJXBT, STXEUR, STXUSD, SUIEUR, SUIUSD, SUPEREUR, SUPERUSD, SUSHIEUR, SUSHIGBP, SUSHIUSD, SUSHIXBT, SYNEUR, SYNUSD, TBTCEUR, TBTCUSD, TBTCXBT, TEEREUR, TEERUSD, TEUR, TLMEUR, TLMUSD, TOKEEUR, TOKEUSD, TRIBEEUR, TRIBEUSD, TRUEUR, TRUUSD, TRXETH, TRXEUR, TRXUSD, TRXXBT, TUSD, TVKEUR, TVKUSD, UMAEUR, UMAUSD, UNFIEUR, UNFIUSD, UNIETH, UNIEUR, UNIUSD, UNIXBT, USDAED, USDCAUD, USDCCAD, USDCCHF, USDCEUR, USDCGBP, USDCHF, USDCUSD, USDCUSDT, USDTAUD, USDTCAD, USDTCHF, USDTEUR, USDTGBP, USDTJPY, USDTZUSD, USTEUR, USTUSD, USTUSDC, USTUSDT, WAVESETH, WAVESEUR, WAVESUSD, WAVESXBT, WAXLEUR, WAXLUSD, WBTCEUR, WBTCUSD, WBTCXBT, WOOEUR, WOOUSD, XBTAED, XBTAUD, XBTCHF, XBTDAI, XBTUSDC, XBTUSDT, XCNEUR, XCNUSD, XDGEUR, XDGUSD, XDGUSDT, XETCXETH, XETCXXBT, XETCZEUR, XETCZUSD, XETHXXBT, XETHZCAD, XETHZEUR, XETHZGBP, XETHZJPY, XETHZUSD, XLTCXXBT, XLTCZEUR, XLTCZJPY, XLTCZUSD, XMLNXETH, XMLNXXBT, XMLNZEUR, XMLNZUSD, XMRUSDT, XREPXXBT, XREPZEUR, XREPZUSD, XRPAUD, XRPETH, XRPGBP, XRPUSDT, XRTEUR, XRTUSD, XTZAUD, XTZETH, XTZEUR, XTZGBP, XTZUSD, XTZUSDT, XTZXBT, XXBTZCAD, XXBTZEUR, XXBTZGBP, XXBTZJPY, XXBTZUSD, XXDGXXBT, XXLMXXBT, XXLMZEUR, XXLMZGBP, XXLMZUSD, XXMRXXBT, XXMRZEUR, XXMRZUSD, XXRPXXBT, XXRPZCAD, XXRPZEUR, XXRPZJPY, XXRPZUSD, XZECXXBT, XZECZEUR, XZECZUSD, YFIEUR, YFIUSD, YFIXBT, YGGEUR, YGGUSD, ZEURZUSD, ZGBPZUSD, ZRXEUR, ZRXUSD, ZRXXBT, ZUSDZCAD, ZUSDZJPY])

kraken = Kraken()
