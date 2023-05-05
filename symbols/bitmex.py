from ._model import Symbol


class _EVOL7D(Symbol):
    """
        name: .EVOL7D
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EVOL7D"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EVOL7D"

    def __str__(self):
        return ".EVOL7D"

    def __call__(self):
        return ".EVOL7D"


_EVOL7D = _EVOL7D(*_EVOL7D._fields)
"""
    name: .EVOL7D
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BADAXBT(Symbol):
    """
        name: .BADAXBT
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAXBT"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BADAXBT"

    def __str__(self):
        return ".BADAXBT"

    def __call__(self):
        return ".BADAXBT"


_BADAXBT = _BADAXBT(*_BADAXBT._fields)
"""
    name: .BADAXBT
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BADAXBT30M(Symbol):
    """
        name: .BADAXBT30M
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAXBT30M"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BADAXBT30M"

    def __str__(self):
        return ".BADAXBT30M"

    def __call__(self):
        return ".BADAXBT30M"


_BADAXBT30M = _BADAXBT30M(*_BADAXBT30M._fields)
"""
    name: .BADAXBT30M
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBCHXBT(Symbol):
    """
        name: .BBCHXBT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHXBT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBCHXBT"

    def __str__(self):
        return ".BBCHXBT"

    def __call__(self):
        return ".BBCHXBT"


_BBCHXBT = _BBCHXBT(*_BBCHXBT._fields)
"""
    name: .BBCHXBT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBCHXBT30M(Symbol):
    """
        name: .BBCHXBT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHXBT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBCHXBT30M"

    def __str__(self):
        return ".BBCHXBT30M"

    def __call__(self):
        return ".BBCHXBT30M"


_BBCHXBT30M = _BBCHXBT30M(*_BBCHXBT30M._fields)
"""
    name: .BBCHXBT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEOSXBT(Symbol):
    """
        name: .BEOSXBT
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOSXBT"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEOSXBT"

    def __str__(self):
        return ".BEOSXBT"

    def __call__(self):
        return ".BEOSXBT"


_BEOSXBT = _BEOSXBT(*_BEOSXBT._fields)
"""
    name: .BEOSXBT
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEOSXBT30M(Symbol):
    """
        name: .BEOSXBT30M
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOSXBT30M"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEOSXBT30M"

    def __str__(self):
        return ".BEOSXBT30M"

    def __call__(self):
        return ".BEOSXBT30M"


_BEOSXBT30M = _BEOSXBT30M(*_BEOSXBT30M._fields)
"""
    name: .BEOSXBT30M
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXRPXBT(Symbol):
    """
        name: .BXRPXBT
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPXBT"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXRPXBT"

    def __str__(self):
        return ".BXRPXBT"

    def __call__(self):
        return ".BXRPXBT"


_BXRPXBT = _BXRPXBT(*_BXRPXBT._fields)
"""
    name: .BXRPXBT
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXRPXBT30M(Symbol):
    """
        name: .BXRPXBT30M
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPXBT30M"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXRPXBT30M"

    def __str__(self):
        return ".BXRPXBT30M"

    def __call__(self):
        return ".BXRPXBT30M"


_BXRPXBT30M = _BXRPXBT30M(*_BXRPXBT30M._fields)
"""
    name: .BXRPXBT30M
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTRXXBT(Symbol):
    """
        name: .BTRXXBT
        significant_digits: None
        tick_size: 1e-10
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXXBT"
    significant_digits: int = None
    tick_size: int = 1e-10
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTRXXBT"

    def __str__(self):
        return ".BTRXXBT"

    def __call__(self):
        return ".BTRXXBT"


_BTRXXBT = _BTRXXBT(*_BTRXXBT._fields)
"""
    name: .BTRXXBT
    significant_digits: None
    tick_size: 1e-10
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTRXXBT30M(Symbol):
    """
        name: .BTRXXBT30M
        significant_digits: None
        tick_size: 1e-10
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXXBT30M"
    significant_digits: int = None
    tick_size: int = 1e-10
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTRXXBT30M"

    def __str__(self):
        return ".BTRXXBT30M"

    def __call__(self):
        return ".BTRXXBT30M"


_BTRXXBT30M = _BTRXXBT30M(*_BTRXXBT30M._fields)
"""
    name: .BTRXXBT30M
    significant_digits: None
    tick_size: 1e-10
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BADAXBT_NEXT(Symbol):
    """
        name: .BADAXBT_NEXT
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAXBT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BADAXBT_NEXT"

    def __str__(self):
        return ".BADAXBT_NEXT"

    def __call__(self):
        return ".BADAXBT_NEXT"


_BADAXBT_NEXT = _BADAXBT_NEXT(*_BADAXBT_NEXT._fields)
"""
    name: .BADAXBT_NEXT
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBCHXBT_NEXT(Symbol):
    """
        name: .BBCHXBT_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHXBT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBCHXBT_NEXT"

    def __str__(self):
        return ".BBCHXBT_NEXT"

    def __call__(self):
        return ".BBCHXBT_NEXT"


_BBCHXBT_NEXT = _BBCHXBT_NEXT(*_BBCHXBT_NEXT._fields)
"""
    name: .BBCHXBT_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEOSXBT_NEXT(Symbol):
    """
        name: .BEOSXBT_NEXT
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOSXBT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEOSXBT_NEXT"

    def __str__(self):
        return ".BEOSXBT_NEXT"

    def __call__(self):
        return ".BEOSXBT_NEXT"


_BEOSXBT_NEXT = _BEOSXBT_NEXT(*_BEOSXBT_NEXT._fields)
"""
    name: .BEOSXBT_NEXT
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTRXXBT_NEXT(Symbol):
    """
        name: .BTRXXBT_NEXT
        significant_digits: None
        tick_size: 1e-10
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXXBT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-10
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTRXXBT_NEXT"

    def __str__(self):
        return ".BTRXXBT_NEXT"

    def __call__(self):
        return ".BTRXXBT_NEXT"


_BTRXXBT_NEXT = _BTRXXBT_NEXT(*_BTRXXBT_NEXT._fields)
"""
    name: .BTRXXBT_NEXT
    significant_digits: None
    tick_size: 1e-10
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXRPXBT_NEXT(Symbol):
    """
        name: .BXRPXBT_NEXT
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPXBT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXRPXBT_NEXT"

    def __str__(self):
        return ".BXRPXBT_NEXT"

    def __call__(self):
        return ".BXRPXBT_NEXT"


_BXRPXBT_NEXT = _BXRPXBT_NEXT(*_BXRPXBT_NEXT._fields)
"""
    name: .BXRPXBT_NEXT
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXRP_NEXT(Symbol):
    """
        name: .BXRP_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRP_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXRP_NEXT"

    def __str__(self):
        return ".BXRP_NEXT"

    def __call__(self):
        return ".BXRP_NEXT"


_BXRP_NEXT = _BXRP_NEXT(*_BXRP_NEXT._fields)
"""
    name: .BXRP_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXRP(Symbol):
    """
        name: .BXRP
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRP"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXRP"

    def __str__(self):
        return ".BXRP"

    def __call__(self):
        return ".BXRP"


_BXRP = _BXRP(*_BXRP._fields)
"""
    name: .BXRP
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XRPBON(Symbol):
    """
        name: .XRPBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XRPBON"

    def __str__(self):
        return ".XRPBON"

    def __call__(self):
        return ".XRPBON"


_XRPBON = _XRPBON(*_XRPBON._fields)
"""
    name: .XRPBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XRPBON8H(Symbol):
    """
        name: .XRPBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XRPBON8H"

    def __str__(self):
        return ".XRPBON8H"

    def __call__(self):
        return ".XRPBON8H"


_XRPBON8H = _XRPBON8H(*_XRPBON8H._fields)
"""
    name: .XRPBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XRPUSDPI(Symbol):
    """
        name: .XRPUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XRPUSDPI"

    def __str__(self):
        return ".XRPUSDPI"

    def __call__(self):
        return ".XRPUSDPI"


_XRPUSDPI = _XRPUSDPI(*_XRPUSDPI._fields)
"""
    name: .XRPUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XRPUSDPI8H(Symbol):
    """
        name: .XRPUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XRPUSDPI8H"

    def __str__(self):
        return ".XRPUSDPI8H"

    def __call__(self):
        return ".XRPUSDPI8H"


_XRPUSDPI8H = _XRPUSDPI8H(*_XRPUSDPI8H._fields)
"""
    name: .XRPUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBCH(Symbol):
    """
        name: .BBCH
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCH"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBCH"

    def __str__(self):
        return ".BBCH"

    def __call__(self):
        return ".BBCH"


_BBCH = _BBCH(*_BBCH._fields)
"""
    name: .BBCH
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCHBON(Symbol):
    """
        name: .BCHBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCHBON"

    def __str__(self):
        return ".BCHBON"

    def __call__(self):
        return ".BCHBON"


_BCHBON = _BCHBON(*_BCHBON._fields)
"""
    name: .BCHBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCHBON8H(Symbol):
    """
        name: .BCHBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCHBON8H"

    def __str__(self):
        return ".BCHBON8H"

    def __call__(self):
        return ".BCHBON8H"


_BCHBON8H = _BCHBON8H(*_BCHBON8H._fields)
"""
    name: .BCHBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCHUSDPI(Symbol):
    """
        name: .BCHUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCHUSDPI"

    def __str__(self):
        return ".BCHUSDPI"

    def __call__(self):
        return ".BCHUSDPI"


_BCHUSDPI = _BCHUSDPI(*_BCHUSDPI._fields)
"""
    name: .BCHUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCHUSDPI8H(Symbol):
    """
        name: .BCHUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCHUSDPI8H"

    def __str__(self):
        return ".BCHUSDPI8H"

    def __call__(self):
        return ".BCHUSDPI8H"


_BCHUSDPI8H = _BCHUSDPI8H(*_BCHUSDPI8H._fields)
"""
    name: .BCHUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBCH_NEXT(Symbol):
    """
        name: .BBCH_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCH_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBCH_NEXT"

    def __str__(self):
        return ".BBCH_NEXT"

    def __call__(self):
        return ".BBCH_NEXT"


_BBCH_NEXT = _BBCH_NEXT(*_BBCH_NEXT._fields)
"""
    name: .BBCH_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUSDT(Symbol):
    """
        name: .BUSDT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDT"

    def __str__(self):
        return ".BUSDT"

    def __call__(self):
        return ".BUSDT"


_BUSDT = _BUSDT(*_BUSDT._fields)
"""
    name: .BUSDT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUSDT_NEXT(Symbol):
    """
        name: .BUSDT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDT_NEXT"

    def __str__(self):
        return ".BUSDT_NEXT"

    def __call__(self):
        return ".BUSDT_NEXT"


_BUSDT_NEXT = _BUSDT_NEXT(*_BUSDT_NEXT._fields)
"""
    name: .BUSDT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEOST(Symbol):
    """
        name: .BEOST
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOST"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEOST"

    def __str__(self):
        return ".BEOST"

    def __call__(self):
        return ".BEOST"


_BEOST = _BEOST(*_BEOST._fields)
"""
    name: .BEOST
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEOST_NEXT(Symbol):
    """
        name: .BEOST_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOST_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEOST_NEXT"

    def __str__(self):
        return ".BEOST_NEXT"

    def __call__(self):
        return ".BEOST_NEXT"


_BEOST_NEXT = _BEOST_NEXT(*_BEOST_NEXT._fields)
"""
    name: .BEOST_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEOST30M(Symbol):
    """
        name: .BEOST30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOST30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEOST30M"

    def __str__(self):
        return ".BEOST30M"

    def __call__(self):
        return ".BEOST30M"


_BEOST30M = _BEOST30M(*_BEOST30M._fields)
"""
    name: .BEOST30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLINKT(Symbol):
    """
        name: .BLINKT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINKT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLINKT"

    def __str__(self):
        return ".BLINKT"

    def __call__(self):
        return ".BLINKT"


_BLINKT = _BLINKT(*_BLINKT._fields)
"""
    name: .BLINKT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLINKT_NEXT(Symbol):
    """
        name: .BLINKT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINKT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLINKT_NEXT"

    def __str__(self):
        return ".BLINKT_NEXT"

    def __call__(self):
        return ".BLINKT_NEXT"


_BLINKT_NEXT = _BLINKT_NEXT(*_BLINKT_NEXT._fields)
"""
    name: .BLINKT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLINKT30M(Symbol):
    """
        name: .BLINKT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINKT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLINKT30M"

    def __str__(self):
        return ".BLINKT30M"

    def __call__(self):
        return ".BLINKT30M"


_BLINKT30M = _BLINKT30M(*_BLINKT30M._fields)
"""
    name: .BLINKT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BADAT(Symbol):
    """
        name: .BADAT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BADAT"

    def __str__(self):
        return ".BADAT"

    def __call__(self):
        return ".BADAT"


_BADAT = _BADAT(*_BADAT._fields)
"""
    name: .BADAT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BADAT_NEXT(Symbol):
    """
        name: .BADAT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BADAT_NEXT"

    def __str__(self):
        return ".BADAT_NEXT"

    def __call__(self):
        return ".BADAT_NEXT"


_BADAT_NEXT = _BADAT_NEXT(*_BADAT_NEXT._fields)
"""
    name: .BADAT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BADAT30M(Symbol):
    """
        name: .BADAT30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAT30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BADAT30M"

    def __str__(self):
        return ".BADAT30M"

    def __call__(self):
        return ".BADAT30M"


_BADAT30M = _BADAT30M(*_BADAT30M._fields)
"""
    name: .BADAT30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXTZT(Symbol):
    """
        name: .BXTZT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXTZT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXTZT"

    def __str__(self):
        return ".BXTZT"

    def __call__(self):
        return ".BXTZT"


_BXTZT = _BXTZT(*_BXTZT._fields)
"""
    name: .BXTZT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXTZT_NEXT(Symbol):
    """
        name: .BXTZT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXTZT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXTZT_NEXT"

    def __str__(self):
        return ".BXTZT_NEXT"

    def __call__(self):
        return ".BXTZT_NEXT"


_BXTZT_NEXT = _BXTZT_NEXT(*_BXTZT_NEXT._fields)
"""
    name: .BXTZT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXTZT30M(Symbol):
    """
        name: .BXTZT30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXTZT30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXTZT30M"

    def __str__(self):
        return ".BXTZT30M"

    def __call__(self):
        return ".BXTZT30M"


_BXTZT30M = _BXTZT30M(*_BXTZT30M._fields)
"""
    name: .BXTZT30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LINKBON(Symbol):
    """
        name: .LINKBON
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKBON"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LINKBON"

    def __str__(self):
        return ".LINKBON"

    def __call__(self):
        return ".LINKBON"


_LINKBON = _LINKBON(*_LINKBON._fields)
"""
    name: .LINKBON
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LINKBON8H(Symbol):
    """
        name: .LINKBON8H
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKBON8H"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LINKBON8H"

    def __str__(self):
        return ".LINKBON8H"

    def __call__(self):
        return ".LINKBON8H"


_LINKBON8H = _LINKBON8H(*_LINKBON8H._fields)
"""
    name: .LINKBON8H
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LINKUSDTPI(Symbol):
    """
        name: .LINKUSDTPI
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LINKUSDTPI"

    def __str__(self):
        return ".LINKUSDTPI"

    def __call__(self):
        return ".LINKUSDTPI"


_LINKUSDTPI = _LINKUSDTPI(*_LINKUSDTPI._fields)
"""
    name: .LINKUSDTPI
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LINKUSDTPI8H(Symbol):
    """
        name: .LINKUSDTPI8H
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LINKUSDTPI8H"

    def __str__(self):
        return ".LINKUSDTPI8H"

    def __call__(self):
        return ".LINKUSDTPI8H"


_LINKUSDTPI8H = _LINKUSDTPI8H(*_LINKUSDTPI8H._fields)
"""
    name: .LINKUSDTPI8H
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTBON(Symbol):
    """
        name: .USDTBON
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTBON"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTBON"

    def __str__(self):
        return ".USDTBON"

    def __call__(self):
        return ".USDTBON"


_USDTBON = _USDTBON(*_USDTBON._fields)
"""
    name: .USDTBON
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTBON8H(Symbol):
    """
        name: .USDTBON8H
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTBON8H"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTBON8H"

    def __str__(self):
        return ".USDTBON8H"

    def __call__(self):
        return ".USDTBON8H"


_USDTBON8H = _USDTBON8H(*_USDTBON8H._fields)
"""
    name: .USDTBON8H
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBNBT(Symbol):
    """
        name: .BBNBT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNBT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBNBT"

    def __str__(self):
        return ".BBNBT"

    def __call__(self):
        return ".BBNBT"


_BBNBT = _BBNBT(*_BBNBT._fields)
"""
    name: .BBNBT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBNBT_NEXT(Symbol):
    """
        name: .BBNBT_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNBT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBNBT_NEXT"

    def __str__(self):
        return ".BBNBT_NEXT"

    def __call__(self):
        return ".BBNBT_NEXT"


_BBNBT_NEXT = _BBNBT_NEXT(*_BBNBT_NEXT._fields)
"""
    name: .BBNBT_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBNBT30M(Symbol):
    """
        name: .BBNBT30M
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNBT30M"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBNBT30M"

    def __str__(self):
        return ".BBNBT30M"

    def __call__(self):
        return ".BBNBT30M"


_BBNBT30M = _BBNBT30M(*_BBNBT30M._fields)
"""
    name: .BBNBT30M
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOTT(Symbol):
    """
        name: .BDOTT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOTT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOTT"

    def __str__(self):
        return ".BDOTT"

    def __call__(self):
        return ".BDOTT"


_BDOTT = _BDOTT(*_BDOTT._fields)
"""
    name: .BDOTT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOTT_NEXT(Symbol):
    """
        name: .BDOTT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOTT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOTT_NEXT"

    def __str__(self):
        return ".BDOTT_NEXT"

    def __call__(self):
        return ".BDOTT_NEXT"


_BDOTT_NEXT = _BDOTT_NEXT(*_BDOTT_NEXT._fields)
"""
    name: .BDOTT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOTT30M(Symbol):
    """
        name: .BDOTT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOTT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOTT30M"

    def __str__(self):
        return ".BDOTT30M"

    def __call__(self):
        return ".BDOTT30M"


_BDOTT30M = _BDOTT30M(*_BDOTT30M._fields)
"""
    name: .BDOTT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BYFIT(Symbol):
    """
        name: .BYFIT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BYFIT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BYFIT"

    def __str__(self):
        return ".BYFIT"

    def __call__(self):
        return ".BYFIT"


_BYFIT = _BYFIT(*_BYFIT._fields)
"""
    name: .BYFIT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BYFIT_NEXT(Symbol):
    """
        name: .BYFIT_NEXT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BYFIT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BYFIT_NEXT"

    def __str__(self):
        return ".BYFIT_NEXT"

    def __call__(self):
        return ".BYFIT_NEXT"


_BYFIT_NEXT = _BYFIT_NEXT(*_BYFIT_NEXT._fields)
"""
    name: .BYFIT_NEXT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BYFIT30M(Symbol):
    """
        name: .BYFIT30M
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BYFIT30M"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BYFIT30M"

    def __str__(self):
        return ".BYFIT30M"

    def __call__(self):
        return ".BYFIT30M"


_BYFIT30M = _BYFIT30M(*_BYFIT30M._fields)
"""
    name: .BYFIT30M
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOGET(Symbol):
    """
        name: .BDOGET
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGET"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOGET"

    def __str__(self):
        return ".BDOGET"

    def __call__(self):
        return ".BDOGET"


_BDOGET = _BDOGET(*_BDOGET._fields)
"""
    name: .BDOGET
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOGET_NEXT(Symbol):
    """
        name: .BDOGET_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGET_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOGET_NEXT"

    def __str__(self):
        return ".BDOGET_NEXT"

    def __call__(self):
        return ".BDOGET_NEXT"


_BDOGET_NEXT = _BDOGET_NEXT(*_BDOGET_NEXT._fields)
"""
    name: .BDOGET_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOGEBON(Symbol):
    """
        name: .DOGEBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOGEBON"

    def __str__(self):
        return ".DOGEBON"

    def __call__(self):
        return ".DOGEBON"


_DOGEBON = _DOGEBON(*_DOGEBON._fields)
"""
    name: .DOGEBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOGEBON8H(Symbol):
    """
        name: .DOGEBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOGEBON8H"

    def __str__(self):
        return ".DOGEBON8H"

    def __call__(self):
        return ".DOGEBON8H"


_DOGEBON8H = _DOGEBON8H(*_DOGEBON8H._fields)
"""
    name: .DOGEBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOGEUSDTPI(Symbol):
    """
        name: .DOGEUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOGEUSDTPI"

    def __str__(self):
        return ".DOGEUSDTPI"

    def __call__(self):
        return ".DOGEUSDTPI"


_DOGEUSDTPI = _DOGEUSDTPI(*_DOGEUSDTPI._fields)
"""
    name: .DOGEUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOGEUSDTPI8H(Symbol):
    """
        name: .DOGEUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOGEUSDTPI8H"

    def __str__(self):
        return ".DOGEUSDTPI8H"

    def __call__(self):
        return ".DOGEUSDTPI8H"


_DOGEUSDTPI8H = _DOGEUSDTPI8H(*_DOGEUSDTPI8H._fields)
"""
    name: .DOGEUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNBBON(Symbol):
    """
        name: .BNBBON
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBBON"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNBBON"

    def __str__(self):
        return ".BNBBON"

    def __call__(self):
        return ".BNBBON"


_BNBBON = _BNBBON(*_BNBBON._fields)
"""
    name: .BNBBON
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNBBON8H(Symbol):
    """
        name: .BNBBON8H
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBBON8H"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNBBON8H"

    def __str__(self):
        return ".BNBBON8H"

    def __call__(self):
        return ".BNBBON8H"


_BNBBON8H = _BNBBON8H(*_BNBBON8H._fields)
"""
    name: .BNBBON8H
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNBUSDTPI(Symbol):
    """
        name: .BNBUSDTPI
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNBUSDTPI"

    def __str__(self):
        return ".BNBUSDTPI"

    def __call__(self):
        return ".BNBUSDTPI"


_BNBUSDTPI = _BNBUSDTPI(*_BNBUSDTPI._fields)
"""
    name: .BNBUSDTPI
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNBUSDTPI8H(Symbol):
    """
        name: .BNBUSDTPI8H
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNBUSDTPI8H"

    def __str__(self):
        return ".BNBUSDTPI8H"

    def __call__(self):
        return ".BNBUSDTPI8H"


_BNBUSDTPI8H = _BNBUSDTPI8H(*_BNBUSDTPI8H._fields)
"""
    name: .BNBUSDTPI8H
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ADABON(Symbol):
    """
        name: .ADABON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADABON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ADABON"

    def __str__(self):
        return ".ADABON"

    def __call__(self):
        return ".ADABON"


_ADABON = _ADABON(*_ADABON._fields)
"""
    name: .ADABON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ADABON8H(Symbol):
    """
        name: .ADABON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADABON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ADABON8H"

    def __str__(self):
        return ".ADABON8H"

    def __call__(self):
        return ".ADABON8H"


_ADABON8H = _ADABON8H(*_ADABON8H._fields)
"""
    name: .ADABON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ADAUSDTPI(Symbol):
    """
        name: .ADAUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADAUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ADAUSDTPI"

    def __str__(self):
        return ".ADAUSDTPI"

    def __call__(self):
        return ".ADAUSDTPI"


_ADAUSDTPI = _ADAUSDTPI(*_ADAUSDTPI._fields)
"""
    name: .ADAUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ADAUSDTPI8H(Symbol):
    """
        name: .ADAUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADAUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ADAUSDTPI8H"

    def __str__(self):
        return ".ADAUSDTPI8H"

    def __call__(self):
        return ".ADAUSDTPI8H"


_ADAUSDTPI8H = _ADAUSDTPI8H(*_ADAUSDTPI8H._fields)
"""
    name: .ADAUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOTBON(Symbol):
    """
        name: .DOTBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOTBON"

    def __str__(self):
        return ".DOTBON"

    def __call__(self):
        return ".DOTBON"


_DOTBON = _DOTBON(*_DOTBON._fields)
"""
    name: .DOTBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOTBON8H(Symbol):
    """
        name: .DOTBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOTBON8H"

    def __str__(self):
        return ".DOTBON8H"

    def __call__(self):
        return ".DOTBON8H"


_DOTBON8H = _DOTBON8H(*_DOTBON8H._fields)
"""
    name: .DOTBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOTUSDTPI(Symbol):
    """
        name: .DOTUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOTUSDTPI"

    def __str__(self):
        return ".DOTUSDTPI"

    def __call__(self):
        return ".DOTUSDTPI"


_DOTUSDTPI = _DOTUSDTPI(*_DOTUSDTPI._fields)
"""
    name: .DOTUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOTUSDTPI8H(Symbol):
    """
        name: .DOTUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOTUSDTPI8H"

    def __str__(self):
        return ".DOTUSDTPI8H"

    def __call__(self):
        return ".DOTUSDTPI8H"


_DOTUSDTPI8H = _DOTUSDTPI8H(*_DOTUSDTPI8H._fields)
"""
    name: .DOTUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EOSBON(Symbol):
    """
        name: .EOSBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EOSBON"

    def __str__(self):
        return ".EOSBON"

    def __call__(self):
        return ".EOSBON"


_EOSBON = _EOSBON(*_EOSBON._fields)
"""
    name: .EOSBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EOSBON8H(Symbol):
    """
        name: .EOSBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EOSBON8H"

    def __str__(self):
        return ".EOSBON8H"

    def __call__(self):
        return ".EOSBON8H"


_EOSBON8H = _EOSBON8H(*_EOSBON8H._fields)
"""
    name: .EOSBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EOSUSDTPI(Symbol):
    """
        name: .EOSUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EOSUSDTPI"

    def __str__(self):
        return ".EOSUSDTPI"

    def __call__(self):
        return ".EOSUSDTPI"


_EOSUSDTPI = _EOSUSDTPI(*_EOSUSDTPI._fields)
"""
    name: .EOSUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EOSUSDTPI8H(Symbol):
    """
        name: .EOSUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EOSUSDTPI8H"

    def __str__(self):
        return ".EOSUSDTPI8H"

    def __call__(self):
        return ".EOSUSDTPI8H"


_EOSUSDTPI8H = _EOSUSDTPI8H(*_EOSUSDTPI8H._fields)
"""
    name: .EOSUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XTZBON(Symbol):
    """
        name: .XTZBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XTZBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XTZBON"

    def __str__(self):
        return ".XTZBON"

    def __call__(self):
        return ".XTZBON"


_XTZBON = _XTZBON(*_XTZBON._fields)
"""
    name: .XTZBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XTZBON8H(Symbol):
    """
        name: .XTZBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XTZBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XTZBON8H"

    def __str__(self):
        return ".XTZBON8H"

    def __call__(self):
        return ".XTZBON8H"


_XTZBON8H = _XTZBON8H(*_XTZBON8H._fields)
"""
    name: .XTZBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XTZUSDTPI(Symbol):
    """
        name: .XTZUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XTZUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XTZUSDTPI"

    def __str__(self):
        return ".XTZUSDTPI"

    def __call__(self):
        return ".XTZUSDTPI"


_XTZUSDTPI = _XTZUSDTPI(*_XTZUSDTPI._fields)
"""
    name: .XTZUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _YFIBON(Symbol):
    """
        name: .YFIBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".YFIBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".YFIBON"

    def __str__(self):
        return ".YFIBON"

    def __call__(self):
        return ".YFIBON"


_YFIBON = _YFIBON(*_YFIBON._fields)
"""
    name: .YFIBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _YFIBON8H(Symbol):
    """
        name: .YFIBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".YFIBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".YFIBON8H"

    def __str__(self):
        return ".YFIBON8H"

    def __call__(self):
        return ".YFIBON8H"


_YFIBON8H = _YFIBON8H(*_YFIBON8H._fields)
"""
    name: .YFIBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _YFIUSDTPI(Symbol):
    """
        name: .YFIUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".YFIUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".YFIUSDTPI"

    def __str__(self):
        return ".YFIUSDTPI"

    def __call__(self):
        return ".YFIUSDTPI"


_YFIUSDTPI = _YFIUSDTPI(*_YFIUSDTPI._fields)
"""
    name: .YFIUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAAVET(Symbol):
    """
        name: .BAAVET
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAAVET"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAAVET"

    def __str__(self):
        return ".BAAVET"

    def __call__(self):
        return ".BAAVET"


_BAAVET = _BAAVET(*_BAAVET._fields)
"""
    name: .BAAVET
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAAVET_NEXT(Symbol):
    """
        name: .BAAVET_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAAVET_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAAVET_NEXT"

    def __str__(self):
        return ".BAAVET_NEXT"

    def __call__(self):
        return ".BAAVET_NEXT"


_BAAVET_NEXT = _BAAVET_NEXT(*_BAAVET_NEXT._fields)
"""
    name: .BAAVET_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AAVEBON(Symbol):
    """
        name: .AAVEBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AAVEBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AAVEBON"

    def __str__(self):
        return ".AAVEBON"

    def __call__(self):
        return ".AAVEBON"


_AAVEBON = _AAVEBON(*_AAVEBON._fields)
"""
    name: .AAVEBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AAVEBON8H(Symbol):
    """
        name: .AAVEBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AAVEBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AAVEBON8H"

    def __str__(self):
        return ".AAVEBON8H"

    def __call__(self):
        return ".AAVEBON8H"


_AAVEBON8H = _AAVEBON8H(*_AAVEBON8H._fields)
"""
    name: .AAVEBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AAVEUSDTPI(Symbol):
    """
        name: .AAVEUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AAVEUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AAVEUSDTPI"

    def __str__(self):
        return ".AAVEUSDTPI"

    def __call__(self):
        return ".AAVEUSDTPI"


_AAVEUSDTPI = _AAVEUSDTPI(*_AAVEUSDTPI._fields)
"""
    name: .AAVEUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AAVEUSDTPI8H(Symbol):
    """
        name: .AAVEUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AAVEUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AAVEUSDTPI8H"

    def __str__(self):
        return ".AAVEUSDTPI8H"

    def __call__(self):
        return ".AAVEUSDTPI8H"


_AAVEUSDTPI8H = _AAVEUSDTPI8H(*_AAVEUSDTPI8H._fields)
"""
    name: .AAVEUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUNIT(Symbol):
    """
        name: .BUNIT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUNIT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUNIT"

    def __str__(self):
        return ".BUNIT"

    def __call__(self):
        return ".BUNIT"


_BUNIT = _BUNIT(*_BUNIT._fields)
"""
    name: .BUNIT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUNIT_NEXT(Symbol):
    """
        name: .BUNIT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUNIT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUNIT_NEXT"

    def __str__(self):
        return ".BUNIT_NEXT"

    def __call__(self):
        return ".BUNIT_NEXT"


_BUNIT_NEXT = _BUNIT_NEXT(*_BUNIT_NEXT._fields)
"""
    name: .BUNIT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _UNIBON(Symbol):
    """
        name: .UNIBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".UNIBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".UNIBON"

    def __str__(self):
        return ".UNIBON"

    def __call__(self):
        return ".UNIBON"


_UNIBON = _UNIBON(*_UNIBON._fields)
"""
    name: .UNIBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _UNIBON8H(Symbol):
    """
        name: .UNIBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".UNIBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".UNIBON8H"

    def __str__(self):
        return ".UNIBON8H"

    def __call__(self):
        return ".UNIBON8H"


_UNIBON8H = _UNIBON8H(*_UNIBON8H._fields)
"""
    name: .UNIBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _UNIUSDTPI(Symbol):
    """
        name: .UNIUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".UNIUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".UNIUSDTPI"

    def __str__(self):
        return ".UNIUSDTPI"

    def __call__(self):
        return ".UNIUSDTPI"


_UNIUSDTPI = _UNIUSDTPI(*_UNIUSDTPI._fields)
"""
    name: .UNIUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _UNIUSDTPI8H(Symbol):
    """
        name: .UNIUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".UNIUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".UNIUSDTPI8H"

    def __str__(self):
        return ".UNIUSDTPI8H"

    def __call__(self):
        return ".UNIUSDTPI8H"


_UNIUSDTPI8H = _UNIUSDTPI8H(*_UNIUSDTPI8H._fields)
"""
    name: .UNIUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXLMT(Symbol):
    """
        name: .BXLMT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXLMT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXLMT"

    def __str__(self):
        return ".BXLMT"

    def __call__(self):
        return ".BXLMT"


_BXLMT = _BXLMT(*_BXLMT._fields)
"""
    name: .BXLMT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXLMT_NEXT(Symbol):
    """
        name: .BXLMT_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXLMT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXLMT_NEXT"

    def __str__(self):
        return ".BXLMT_NEXT"

    def __call__(self):
        return ".BXLMT_NEXT"


_BXLMT_NEXT = _BXLMT_NEXT(*_BXLMT_NEXT._fields)
"""
    name: .BXLMT_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XLMBON(Symbol):
    """
        name: .XLMBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XLMBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XLMBON"

    def __str__(self):
        return ".XLMBON"

    def __call__(self):
        return ".XLMBON"


_XLMBON = _XLMBON(*_XLMBON._fields)
"""
    name: .XLMBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XLMBON8H(Symbol):
    """
        name: .XLMBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XLMBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XLMBON8H"

    def __str__(self):
        return ".XLMBON8H"

    def __call__(self):
        return ".XLMBON8H"


_XLMBON8H = _XLMBON8H(*_XLMBON8H._fields)
"""
    name: .XLMBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XLMUSDTPI(Symbol):
    """
        name: .XLMUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XLMUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XLMUSDTPI"

    def __str__(self):
        return ".XLMUSDTPI"

    def __call__(self):
        return ".XLMUSDTPI"


_XLMUSDTPI = _XLMUSDTPI(*_XLMUSDTPI._fields)
"""
    name: .XLMUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XLMUSDTPI8H(Symbol):
    """
        name: .XLMUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XLMUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XLMUSDTPI8H"

    def __str__(self):
        return ".XLMUSDTPI8H"

    def __call__(self):
        return ".XLMUSDTPI8H"


_XLMUSDTPI8H = _XLMUSDTPI8H(*_XLMUSDTPI8H._fields)
"""
    name: .XLMUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTRXT(Symbol):
    """
        name: .BTRXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTRXT"

    def __str__(self):
        return ".BTRXT"

    def __call__(self):
        return ".BTRXT"


_BTRXT = _BTRXT(*_BTRXT._fields)
"""
    name: .BTRXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTRXT_NEXT(Symbol):
    """
        name: .BTRXT_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTRXT_NEXT"

    def __str__(self):
        return ".BTRXT_NEXT"

    def __call__(self):
        return ".BTRXT_NEXT"


_BTRXT_NEXT = _BTRXT_NEXT(*_BTRXT_NEXT._fields)
"""
    name: .BTRXT_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _TRXBON(Symbol):
    """
        name: .TRXBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".TRXBON"

    def __str__(self):
        return ".TRXBON"

    def __call__(self):
        return ".TRXBON"


_TRXBON = _TRXBON(*_TRXBON._fields)
"""
    name: .TRXBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _TRXBON8H(Symbol):
    """
        name: .TRXBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".TRXBON8H"

    def __str__(self):
        return ".TRXBON8H"

    def __call__(self):
        return ".TRXBON8H"


_TRXBON8H = _TRXBON8H(*_TRXBON8H._fields)
"""
    name: .TRXBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _TRXUSDTPI(Symbol):
    """
        name: .TRXUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".TRXUSDTPI"

    def __str__(self):
        return ".TRXUSDTPI"

    def __call__(self):
        return ".TRXUSDTPI"


_TRXUSDTPI = _TRXUSDTPI(*_TRXUSDTPI._fields)
"""
    name: .TRXUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _TRXUSDTPI8H(Symbol):
    """
        name: .TRXUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".TRXUSDTPI8H"

    def __str__(self):
        return ".TRXUSDTPI8H"

    def __call__(self):
        return ".TRXUSDTPI8H"


_TRXUSDTPI8H = _TRXUSDTPI8H(*_TRXUSDTPI8H._fields)
"""
    name: .TRXUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTRXT30M(Symbol):
    """
        name: .BTRXT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTRXT30M"

    def __str__(self):
        return ".BTRXT30M"

    def __call__(self):
        return ".BTRXT30M"


_BTRXT30M = _BTRXT30M(*_BTRXT30M._fields)
"""
    name: .BTRXT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSOLT(Symbol):
    """
        name: .BSOLT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOLT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSOLT"

    def __str__(self):
        return ".BSOLT"

    def __call__(self):
        return ".BSOLT"


_BSOLT = _BSOLT(*_BSOLT._fields)
"""
    name: .BSOLT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSOLT_NEXT(Symbol):
    """
        name: .BSOLT_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOLT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSOLT_NEXT"

    def __str__(self):
        return ".BSOLT_NEXT"

    def __call__(self):
        return ".BSOLT_NEXT"


_BSOLT_NEXT = _BSOLT_NEXT(*_BSOLT_NEXT._fields)
"""
    name: .BSOLT_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SOLBON(Symbol):
    """
        name: .SOLBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SOLBON"

    def __str__(self):
        return ".SOLBON"

    def __call__(self):
        return ".SOLBON"


_SOLBON = _SOLBON(*_SOLBON._fields)
"""
    name: .SOLBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SOLBON8H(Symbol):
    """
        name: .SOLBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SOLBON8H"

    def __str__(self):
        return ".SOLBON8H"

    def __call__(self):
        return ".SOLBON8H"


_SOLBON8H = _SOLBON8H(*_SOLBON8H._fields)
"""
    name: .SOLBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SOLUSDTPI(Symbol):
    """
        name: .SOLUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SOLUSDTPI"

    def __str__(self):
        return ".SOLUSDTPI"

    def __call__(self):
        return ".SOLUSDTPI"


_SOLUSDTPI = _SOLUSDTPI(*_SOLUSDTPI._fields)
"""
    name: .SOLUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SOLUSDTPI8H(Symbol):
    """
        name: .SOLUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SOLUSDTPI8H"

    def __str__(self):
        return ".SOLUSDTPI8H"

    def __call__(self):
        return ".SOLUSDTPI8H"


_SOLUSDTPI8H = _SOLUSDTPI8H(*_SOLUSDTPI8H._fields)
"""
    name: .SOLUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFILT(Symbol):
    """
        name: .BFILT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFILT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFILT"

    def __str__(self):
        return ".BFILT"

    def __call__(self):
        return ".BFILT"


_BFILT = _BFILT(*_BFILT._fields)
"""
    name: .BFILT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFILT_NEXT(Symbol):
    """
        name: .BFILT_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFILT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFILT_NEXT"

    def __str__(self):
        return ".BFILT_NEXT"

    def __call__(self):
        return ".BFILT_NEXT"


_BFILT_NEXT = _BFILT_NEXT(*_BFILT_NEXT._fields)
"""
    name: .BFILT_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FILBON(Symbol):
    """
        name: .FILBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FILBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FILBON"

    def __str__(self):
        return ".FILBON"

    def __call__(self):
        return ".FILBON"


_FILBON = _FILBON(*_FILBON._fields)
"""
    name: .FILBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FILBON8H(Symbol):
    """
        name: .FILBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FILBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FILBON8H"

    def __str__(self):
        return ".FILBON8H"

    def __call__(self):
        return ".FILBON8H"


_FILBON8H = _FILBON8H(*_FILBON8H._fields)
"""
    name: .FILBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FILUSDTPI(Symbol):
    """
        name: .FILUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FILUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FILUSDTPI"

    def __str__(self):
        return ".FILUSDTPI"

    def __call__(self):
        return ".FILUSDTPI"


_FILUSDTPI = _FILUSDTPI(*_FILUSDTPI._fields)
"""
    name: .FILUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FILUSDTPI8H(Symbol):
    """
        name: .FILUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FILUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FILUSDTPI8H"

    def __str__(self):
        return ".FILUSDTPI8H"

    def __call__(self):
        return ".FILUSDTPI8H"


_FILUSDTPI8H = _FILUSDTPI8H(*_FILUSDTPI8H._fields)
"""
    name: .FILUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURBON(Symbol):
    """
        name: .EURBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURBON"

    def __str__(self):
        return ".EURBON"

    def __call__(self):
        return ".EURBON"


_EURBON = _EURBON(*_EURBON._fields)
"""
    name: .EURBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURBON8H(Symbol):
    """
        name: .EURBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURBON8H"

    def __str__(self):
        return ".EURBON8H"

    def __call__(self):
        return ".EURBON8H"


_EURBON8H = _EURBON8H(*_EURBON8H._fields)
"""
    name: .EURBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BVETT(Symbol):
    """
        name: .BVETT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVETT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BVETT"

    def __str__(self):
        return ".BVETT"

    def __call__(self):
        return ".BVETT"


_BVETT = _BVETT(*_BVETT._fields)
"""
    name: .BVETT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BVETT_NEXT(Symbol):
    """
        name: .BVETT_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVETT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BVETT_NEXT"

    def __str__(self):
        return ".BVETT_NEXT"

    def __call__(self):
        return ".BVETT_NEXT"


_BVETT_NEXT = _BVETT_NEXT(*_BVETT_NEXT._fields)
"""
    name: .BVETT_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _VETBON(Symbol):
    """
        name: .VETBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".VETBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".VETBON"

    def __str__(self):
        return ".VETBON"

    def __call__(self):
        return ".VETBON"


_VETBON = _VETBON(*_VETBON._fields)
"""
    name: .VETBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _VETBON8H(Symbol):
    """
        name: .VETBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".VETBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".VETBON8H"

    def __str__(self):
        return ".VETBON8H"

    def __call__(self):
        return ".VETBON8H"


_VETBON8H = _VETBON8H(*_VETBON8H._fields)
"""
    name: .VETBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _VETUSDTPI(Symbol):
    """
        name: .VETUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".VETUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".VETUSDTPI"

    def __str__(self):
        return ".VETUSDTPI"

    def __call__(self):
        return ".VETUSDTPI"


_VETUSDTPI = _VETUSDTPI(*_VETUSDTPI._fields)
"""
    name: .VETUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _VETUSDTPI8H(Symbol):
    """
        name: .VETUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".VETUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".VETUSDTPI8H"

    def __str__(self):
        return ".VETUSDTPI8H"

    def __call__(self):
        return ".VETUSDTPI8H"


_VETUSDTPI8H = _VETUSDTPI8H(*_VETUSDTPI8H._fields)
"""
    name: .VETUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMATICT(Symbol):
    """
        name: .BMATICT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMATICT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMATICT"

    def __str__(self):
        return ".BMATICT"

    def __call__(self):
        return ".BMATICT"


_BMATICT = _BMATICT(*_BMATICT._fields)
"""
    name: .BMATICT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMATICT_NEXT(Symbol):
    """
        name: .BMATICT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMATICT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMATICT_NEXT"

    def __str__(self):
        return ".BMATICT_NEXT"

    def __call__(self):
        return ".BMATICT_NEXT"


_BMATICT_NEXT = _BMATICT_NEXT(*_BMATICT_NEXT._fields)
"""
    name: .BMATICT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MATICBON(Symbol):
    """
        name: .MATICBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MATICBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MATICBON"

    def __str__(self):
        return ".MATICBON"

    def __call__(self):
        return ".MATICBON"


_MATICBON = _MATICBON(*_MATICBON._fields)
"""
    name: .MATICBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MATICBON8H(Symbol):
    """
        name: .MATICBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MATICBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MATICBON8H"

    def __str__(self):
        return ".MATICBON8H"

    def __call__(self):
        return ".MATICBON8H"


_MATICBON8H = _MATICBON8H(*_MATICBON8H._fields)
"""
    name: .MATICBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MATICUSDTPI(Symbol):
    """
        name: .MATICUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MATICUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MATICUSDTPI"

    def __str__(self):
        return ".MATICUSDTPI"

    def __call__(self):
        return ".MATICUSDTPI"


_MATICUSDTPI = _MATICUSDTPI(*_MATICUSDTPI._fields)
"""
    name: .MATICUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MATICUSDTPI8H(Symbol):
    """
        name: .MATICUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MATICUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MATICUSDTPI8H"

    def __str__(self):
        return ".MATICUSDTPI8H"

    def __call__(self):
        return ".MATICUSDTPI8H"


_MATICUSDTPI8H = _MATICUSDTPI8H(*_MATICUSDTPI8H._fields)
"""
    name: .MATICUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMKRT(Symbol):
    """
        name: .BMKRT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMKRT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMKRT"

    def __str__(self):
        return ".BMKRT"

    def __call__(self):
        return ".BMKRT"


_BMKRT = _BMKRT(*_BMKRT._fields)
"""
    name: .BMKRT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMKRT_NEXT(Symbol):
    """
        name: .BMKRT_NEXT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMKRT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMKRT_NEXT"

    def __str__(self):
        return ".BMKRT_NEXT"

    def __call__(self):
        return ".BMKRT_NEXT"


_BMKRT_NEXT = _BMKRT_NEXT(*_BMKRT_NEXT._fields)
"""
    name: .BMKRT_NEXT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAVAXT(Symbol):
    """
        name: .BAVAXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAVAXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAVAXT"

    def __str__(self):
        return ".BAVAXT"

    def __call__(self):
        return ".BAVAXT"


_BAVAXT = _BAVAXT(*_BAVAXT._fields)
"""
    name: .BAVAXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAVAXT_NEXT(Symbol):
    """
        name: .BAVAXT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAVAXT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAVAXT_NEXT"

    def __str__(self):
        return ".BAVAXT_NEXT"

    def __call__(self):
        return ".BAVAXT_NEXT"


_BAVAXT_NEXT = _BAVAXT_NEXT(*_BAVAXT_NEXT._fields)
"""
    name: .BAVAXT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNAT(Symbol):
    """
        name: .BLUNAT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNAT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNAT"

    def __str__(self):
        return ".BLUNAT"

    def __call__(self):
        return ".BLUNAT"


_BLUNAT = _BLUNAT(*_BLUNAT._fields)
"""
    name: .BLUNAT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNAT_NEXT(Symbol):
    """
        name: .BLUNAT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNAT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNAT_NEXT"

    def __str__(self):
        return ".BLUNAT_NEXT"

    def __call__(self):
        return ".BLUNAT_NEXT"


_BLUNAT_NEXT = _BLUNAT_NEXT(*_BLUNAT_NEXT._fields)
"""
    name: .BLUNAT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCOMPT(Symbol):
    """
        name: .BCOMPT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCOMPT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCOMPT"

    def __str__(self):
        return ".BCOMPT"

    def __call__(self):
        return ".BCOMPT"


_BCOMPT = _BCOMPT(*_BCOMPT._fields)
"""
    name: .BCOMPT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCOMPT_NEXT(Symbol):
    """
        name: .BCOMPT_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCOMPT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCOMPT_NEXT"

    def __str__(self):
        return ".BCOMPT_NEXT"

    def __call__(self):
        return ".BCOMPT_NEXT"


_BCOMPT_NEXT = _BCOMPT_NEXT(*_BCOMPT_NEXT._fields)
"""
    name: .BCOMPT_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSUSHIT(Symbol):
    """
        name: .BSUSHIT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUSHIT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSUSHIT"

    def __str__(self):
        return ".BSUSHIT"

    def __call__(self):
        return ".BSUSHIT"


_BSUSHIT = _BSUSHIT(*_BSUSHIT._fields)
"""
    name: .BSUSHIT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSUSHIT_NEXT(Symbol):
    """
        name: .BSUSHIT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUSHIT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSUSHIT_NEXT"

    def __str__(self):
        return ".BSUSHIT_NEXT"

    def __call__(self):
        return ".BSUSHIT_NEXT"


_BSUSHIT_NEXT = _BSUSHIT_NEXT(*_BSUSHIT_NEXT._fields)
"""
    name: .BSUSHIT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGRTT(Symbol):
    """
        name: .BGRTT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGRTT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGRTT"

    def __str__(self):
        return ".BGRTT"

    def __call__(self):
        return ".BGRTT"


_BGRTT = _BGRTT(*_BGRTT._fields)
"""
    name: .BGRTT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGRTT_NEXT(Symbol):
    """
        name: .BGRTT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGRTT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGRTT_NEXT"

    def __str__(self):
        return ".BGRTT_NEXT"

    def __call__(self):
        return ".BGRTT_NEXT"


_BGRTT_NEXT = _BGRTT_NEXT(*_BGRTT_NEXT._fields)
"""
    name: .BGRTT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BALTMEX(Symbol):
    """
        name: .BALTMEX
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BALTMEX"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BALTMEX"

    def __str__(self):
        return ".BALTMEX"

    def __call__(self):
        return ".BALTMEX"


_BALTMEX = _BALTMEX(*_BALTMEX._fields)
"""
    name: .BALTMEX
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDEFIMEX(Symbol):
    """
        name: .BDEFIMEX
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDEFIMEX"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDEFIMEX"

    def __str__(self):
        return ".BDEFIMEX"

    def __call__(self):
        return ".BDEFIMEX"


_BDEFIMEX = _BDEFIMEX(*_BDEFIMEX._fields)
"""
    name: .BDEFIMEX
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ALTMEXBON(Symbol):
    """
        name: .ALTMEXBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ALTMEXBON"

    def __str__(self):
        return ".ALTMEXBON"

    def __call__(self):
        return ".ALTMEXBON"


_ALTMEXBON = _ALTMEXBON(*_ALTMEXBON._fields)
"""
    name: .ALTMEXBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ALTMEXBON8H(Symbol):
    """
        name: .ALTMEXBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ALTMEXBON8H"

    def __str__(self):
        return ".ALTMEXBON8H"

    def __call__(self):
        return ".ALTMEXBON8H"


_ALTMEXBON8H = _ALTMEXBON8H(*_ALTMEXBON8H._fields)
"""
    name: .ALTMEXBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ALTMEXUSDPI(Symbol):
    """
        name: .ALTMEXUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ALTMEXUSDPI"

    def __str__(self):
        return ".ALTMEXUSDPI"

    def __call__(self):
        return ".ALTMEXUSDPI"


_ALTMEXUSDPI = _ALTMEXUSDPI(*_ALTMEXUSDPI._fields)
"""
    name: .ALTMEXUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ALTMEXUSDPI8H(Symbol):
    """
        name: .ALTMEXUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ALTMEXUSDPI8H"

    def __str__(self):
        return ".ALTMEXUSDPI8H"

    def __call__(self):
        return ".ALTMEXUSDPI8H"


_ALTMEXUSDPI8H = _ALTMEXUSDPI8H(*_ALTMEXUSDPI8H._fields)
"""
    name: .ALTMEXUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DEFIMEXBON(Symbol):
    """
        name: .DEFIMEXBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DEFIMEXBON"

    def __str__(self):
        return ".DEFIMEXBON"

    def __call__(self):
        return ".DEFIMEXBON"


_DEFIMEXBON = _DEFIMEXBON(*_DEFIMEXBON._fields)
"""
    name: .DEFIMEXBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DEFIMEXBON8H(Symbol):
    """
        name: .DEFIMEXBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DEFIMEXBON8H"

    def __str__(self):
        return ".DEFIMEXBON8H"

    def __call__(self):
        return ".DEFIMEXBON8H"


_DEFIMEXBON8H = _DEFIMEXBON8H(*_DEFIMEXBON8H._fields)
"""
    name: .DEFIMEXBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DEFIMEXUSDPI(Symbol):
    """
        name: .DEFIMEXUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DEFIMEXUSDPI"

    def __str__(self):
        return ".DEFIMEXUSDPI"

    def __call__(self):
        return ".DEFIMEXUSDPI"


_DEFIMEXUSDPI = _DEFIMEXUSDPI(*_DEFIMEXUSDPI._fields)
"""
    name: .DEFIMEXUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DEFIMEXUSDPI8H(Symbol):
    """
        name: .DEFIMEXUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DEFIMEXUSDPI8H"

    def __str__(self):
        return ".DEFIMEXUSDPI8H"

    def __call__(self):
        return ".DEFIMEXUSDPI8H"


_DEFIMEXUSDPI8H = _DEFIMEXUSDPI8H(*_DEFIMEXUSDPI8H._fields)
"""
    name: .DEFIMEXUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUSHIBON(Symbol):
    """
        name: .SUSHIBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUSHIBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUSHIBON"

    def __str__(self):
        return ".SUSHIBON"

    def __call__(self):
        return ".SUSHIBON"


_SUSHIBON = _SUSHIBON(*_SUSHIBON._fields)
"""
    name: .SUSHIBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUSHIBON8H(Symbol):
    """
        name: .SUSHIBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUSHIBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUSHIBON8H"

    def __str__(self):
        return ".SUSHIBON8H"

    def __call__(self):
        return ".SUSHIBON8H"


_SUSHIBON8H = _SUSHIBON8H(*_SUSHIBON8H._fields)
"""
    name: .SUSHIBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUSHIUSDTPI(Symbol):
    """
        name: .SUSHIUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUSHIUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUSHIUSDTPI"

    def __str__(self):
        return ".SUSHIUSDTPI"

    def __call__(self):
        return ".SUSHIUSDTPI"


_SUSHIUSDTPI = _SUSHIUSDTPI(*_SUSHIUSDTPI._fields)
"""
    name: .SUSHIUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUSHIUSDTPI8H(Symbol):
    """
        name: .SUSHIUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUSHIUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUSHIUSDTPI8H"

    def __str__(self):
        return ".SUSHIUSDTPI8H"

    def __call__(self):
        return ".SUSHIUSDTPI8H"


_SUSHIUSDTPI8H = _SUSHIUSDTPI8H(*_SUSHIUSDTPI8H._fields)
"""
    name: .SUSHIUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAXST(Symbol):
    """
        name: .BAXST
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXST"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAXST"

    def __str__(self):
        return ".BAXST"

    def __call__(self):
        return ".BAXST"


_BAXST = _BAXST(*_BAXST._fields)
"""
    name: .BAXST
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAXST_NEXT(Symbol):
    """
        name: .BAXST_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXST_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAXST_NEXT"

    def __str__(self):
        return ".BAXST_NEXT"

    def __call__(self):
        return ".BAXST_NEXT"


_BAXST_NEXT = _BAXST_NEXT(*_BAXST_NEXT._fields)
"""
    name: .BAXST_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AXSBON(Symbol):
    """
        name: .AXSBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AXSBON"

    def __str__(self):
        return ".AXSBON"

    def __call__(self):
        return ".AXSBON"


_AXSBON = _AXSBON(*_AXSBON._fields)
"""
    name: .AXSBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AXSBON8H(Symbol):
    """
        name: .AXSBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AXSBON8H"

    def __str__(self):
        return ".AXSBON8H"

    def __call__(self):
        return ".AXSBON8H"


_AXSBON8H = _AXSBON8H(*_AXSBON8H._fields)
"""
    name: .AXSBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AXSUSDTPI(Symbol):
    """
        name: .AXSUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AXSUSDTPI"

    def __str__(self):
        return ".AXSUSDTPI"

    def __call__(self):
        return ".AXSUSDTPI"


_AXSUSDTPI = _AXSUSDTPI(*_AXSUSDTPI._fields)
"""
    name: .AXSUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AXSUSDTPI8H(Symbol):
    """
        name: .AXSUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AXSUSDTPI8H"

    def __str__(self):
        return ".AXSUSDTPI8H"

    def __call__(self):
        return ".AXSUSDTPI8H"


_AXSUSDTPI8H = _AXSUSDTPI8H(*_AXSUSDTPI8H._fields)
"""
    name: .AXSUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSRMT(Symbol):
    """
        name: .BSRMT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSRMT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSRMT"

    def __str__(self):
        return ".BSRMT"

    def __call__(self):
        return ".BSRMT"


_BSRMT = _BSRMT(*_BSRMT._fields)
"""
    name: .BSRMT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSRMT_NEXT(Symbol):
    """
        name: .BSRMT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSRMT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSRMT_NEXT"

    def __str__(self):
        return ".BSRMT_NEXT"

    def __call__(self):
        return ".BSRMT_NEXT"


_BSRMT_NEXT = _BSRMT_NEXT(*_BSRMT_NEXT._fields)
"""
    name: .BSRMT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SRMBON(Symbol):
    """
        name: .SRMBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SRMBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SRMBON"

    def __str__(self):
        return ".SRMBON"

    def __call__(self):
        return ".SRMBON"


_SRMBON = _SRMBON(*_SRMBON._fields)
"""
    name: .SRMBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SRMBON8H(Symbol):
    """
        name: .SRMBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SRMBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SRMBON8H"

    def __str__(self):
        return ".SRMBON8H"

    def __call__(self):
        return ".SRMBON8H"


_SRMBON8H = _SRMBON8H(*_SRMBON8H._fields)
"""
    name: .SRMBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SRMUSDTPI(Symbol):
    """
        name: .SRMUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SRMUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SRMUSDTPI"

    def __str__(self):
        return ".SRMUSDTPI"

    def __call__(self):
        return ".SRMUSDTPI"


_SRMUSDTPI = _SRMUSDTPI(*_SRMUSDTPI._fields)
"""
    name: .SRMUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SRMUSDTPI8H(Symbol):
    """
        name: .SRMUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SRMUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SRMUSDTPI8H"

    def __str__(self):
        return ".SRMUSDTPI8H"

    def __call__(self):
        return ".SRMUSDTPI8H"


_SRMUSDTPI8H = _SRMUSDTPI8H(*_SRMUSDTPI8H._fields)
"""
    name: .SRMUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNA(Symbol):
    """
        name: .BLUNA
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNA"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNA"

    def __str__(self):
        return ".BLUNA"

    def __call__(self):
        return ".BLUNA"


_BLUNA = _BLUNA(*_BLUNA._fields)
"""
    name: .BLUNA
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNA_NEXT(Symbol):
    """
        name: .BLUNA_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNA_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNA_NEXT"

    def __str__(self):
        return ".BLUNA_NEXT"

    def __call__(self):
        return ".BLUNA_NEXT"


_BLUNA_NEXT = _BLUNA_NEXT(*_BLUNA_NEXT._fields)
"""
    name: .BLUNA_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LUNABON(Symbol):
    """
        name: .LUNABON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNABON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LUNABON"

    def __str__(self):
        return ".LUNABON"

    def __call__(self):
        return ".LUNABON"


_LUNABON = _LUNABON(*_LUNABON._fields)
"""
    name: .LUNABON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LUNABON8H(Symbol):
    """
        name: .LUNABON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNABON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LUNABON8H"

    def __str__(self):
        return ".LUNABON8H"

    def __call__(self):
        return ".LUNABON8H"


_LUNABON8H = _LUNABON8H(*_LUNABON8H._fields)
"""
    name: .LUNABON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LUNAUSDPI(Symbol):
    """
        name: .LUNAUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNAUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LUNAUSDPI"

    def __str__(self):
        return ".LUNAUSDPI"

    def __call__(self):
        return ".LUNAUSDPI"


_LUNAUSDPI = _LUNAUSDPI(*_LUNAUSDPI._fields)
"""
    name: .LUNAUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LUNAUSDPI8H(Symbol):
    """
        name: .LUNAUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNAUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LUNAUSDPI8H"

    def __str__(self):
        return ".LUNAUSDPI8H"

    def __call__(self):
        return ".LUNAUSDPI8H"


_LUNAUSDPI8H = _LUNAUSDPI8H(*_LUNAUSDPI8H._fields)
"""
    name: .LUNAUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AVAXBON(Symbol):
    """
        name: .AVAXBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AVAXBON"

    def __str__(self):
        return ".AVAXBON"

    def __call__(self):
        return ".AVAXBON"


_AVAXBON = _AVAXBON(*_AVAXBON._fields)
"""
    name: .AVAXBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AVAXBON8H(Symbol):
    """
        name: .AVAXBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AVAXBON8H"

    def __str__(self):
        return ".AVAXBON8H"

    def __call__(self):
        return ".AVAXBON8H"


_AVAXBON8H = _AVAXBON8H(*_AVAXBON8H._fields)
"""
    name: .AVAXBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAVAX(Symbol):
    """
        name: .BAVAX
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAVAX"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAVAX"

    def __str__(self):
        return ".BAVAX"

    def __call__(self):
        return ".BAVAX"


_BAVAX = _BAVAX(*_BAVAX._fields)
"""
    name: .BAVAX
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAVAX_NEXT(Symbol):
    """
        name: .BAVAX_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAVAX_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAVAX_NEXT"

    def __str__(self):
        return ".BAVAX_NEXT"

    def __call__(self):
        return ".BAVAX_NEXT"


_BAVAX_NEXT = _BAVAX_NEXT(*_BAVAX_NEXT._fields)
"""
    name: .BAVAX_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AVAXUSDPI(Symbol):
    """
        name: .AVAXUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AVAXUSDPI"

    def __str__(self):
        return ".AVAXUSDPI"

    def __call__(self):
        return ".AVAXUSDPI"


_AVAXUSDPI = _AVAXUSDPI(*_AVAXUSDPI._fields)
"""
    name: .AVAXUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AVAXUSDPI8H(Symbol):
    """
        name: .AVAXUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AVAXUSDPI8H"

    def __str__(self):
        return ".AVAXUSDPI8H"

    def __call__(self):
        return ".AVAXUSDPI8H"


_AVAXUSDPI8H = _AVAXUSDPI8H(*_AVAXUSDPI8H._fields)
"""
    name: .AVAXUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BADA(Symbol):
    """
        name: .BADA
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADA"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BADA"

    def __str__(self):
        return ".BADA"

    def __call__(self):
        return ".BADA"


_BADA = _BADA(*_BADA._fields)
"""
    name: .BADA
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BADA_NEXT(Symbol):
    """
        name: .BADA_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADA_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BADA_NEXT"

    def __str__(self):
        return ".BADA_NEXT"

    def __call__(self):
        return ".BADA_NEXT"


_BADA_NEXT = _BADA_NEXT(*_BADA_NEXT._fields)
"""
    name: .BADA_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ADAUSDPI(Symbol):
    """
        name: .ADAUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADAUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ADAUSDPI"

    def __str__(self):
        return ".ADAUSDPI"

    def __call__(self):
        return ".ADAUSDPI"


_ADAUSDPI = _ADAUSDPI(*_ADAUSDPI._fields)
"""
    name: .ADAUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ADAUSDPI8H(Symbol):
    """
        name: .ADAUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADAUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ADAUSDPI8H"

    def __str__(self):
        return ".ADAUSDPI8H"

    def __call__(self):
        return ".ADAUSDPI8H"


_ADAUSDPI8H = _ADAUSDPI8H(*_ADAUSDPI8H._fields)
"""
    name: .ADAUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOGE(Symbol):
    """
        name: .BDOGE
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGE"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOGE"

    def __str__(self):
        return ".BDOGE"

    def __call__(self):
        return ".BDOGE"


_BDOGE = _BDOGE(*_BDOGE._fields)
"""
    name: .BDOGE
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOGE_NEXT(Symbol):
    """
        name: .BDOGE_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGE_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOGE_NEXT"

    def __str__(self):
        return ".BDOGE_NEXT"

    def __call__(self):
        return ".BDOGE_NEXT"


_BDOGE_NEXT = _BDOGE_NEXT(*_BDOGE_NEXT._fields)
"""
    name: .BDOGE_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOGEUSDPI(Symbol):
    """
        name: .DOGEUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOGEUSDPI"

    def __str__(self):
        return ".DOGEUSDPI"

    def __call__(self):
        return ".DOGEUSDPI"


_DOGEUSDPI = _DOGEUSDPI(*_DOGEUSDPI._fields)
"""
    name: .DOGEUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOGEUSDPI8H(Symbol):
    """
        name: .DOGEUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOGEUSDPI8H"

    def __str__(self):
        return ".DOGEUSDPI8H"

    def __call__(self):
        return ".DOGEUSDPI8H"


_DOGEUSDPI8H = _DOGEUSDPI8H(*_DOGEUSDPI8H._fields)
"""
    name: .DOGEUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBNB(Symbol):
    """
        name: .BBNB
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNB"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBNB"

    def __str__(self):
        return ".BBNB"

    def __call__(self):
        return ".BBNB"


_BBNB = _BBNB(*_BBNB._fields)
"""
    name: .BBNB
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBNB_NEXT(Symbol):
    """
        name: .BBNB_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNB_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBNB_NEXT"

    def __str__(self):
        return ".BBNB_NEXT"

    def __call__(self):
        return ".BBNB_NEXT"


_BBNB_NEXT = _BBNB_NEXT(*_BBNB_NEXT._fields)
"""
    name: .BBNB_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNBUSDPI(Symbol):
    """
        name: .BNBUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNBUSDPI"

    def __str__(self):
        return ".BNBUSDPI"

    def __call__(self):
        return ".BNBUSDPI"


_BNBUSDPI = _BNBUSDPI(*_BNBUSDPI._fields)
"""
    name: .BNBUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNBUSDPI8H(Symbol):
    """
        name: .BNBUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNBUSDPI8H"

    def __str__(self):
        return ".BNBUSDPI8H"

    def __call__(self):
        return ".BNBUSDPI8H"


_BNBUSDPI8H = _BNBUSDPI8H(*_BNBUSDPI8H._fields)
"""
    name: .BNBUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOT(Symbol):
    """
        name: .BDOT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOT"

    def __str__(self):
        return ".BDOT"

    def __call__(self):
        return ".BDOT"


_BDOT = _BDOT(*_BDOT._fields)
"""
    name: .BDOT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOT_NEXT(Symbol):
    """
        name: .BDOT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOT_NEXT"

    def __str__(self):
        return ".BDOT_NEXT"

    def __call__(self):
        return ".BDOT_NEXT"


_BDOT_NEXT = _BDOT_NEXT(*_BDOT_NEXT._fields)
"""
    name: .BDOT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOTUSDPI(Symbol):
    """
        name: .DOTUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOTUSDPI"

    def __str__(self):
        return ".DOTUSDPI"

    def __call__(self):
        return ".DOTUSDPI"


_DOTUSDPI = _DOTUSDPI(*_DOTUSDPI._fields)
"""
    name: .DOTUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DOTUSDPI8H(Symbol):
    """
        name: .DOTUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DOTUSDPI8H"

    def __str__(self):
        return ".DOTUSDPI8H"

    def __call__(self):
        return ".DOTUSDPI8H"


_DOTUSDPI8H = _DOTUSDPI8H(*_DOTUSDPI8H._fields)
"""
    name: .DOTUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDOGET30M(Symbol):
    """
        name: .BDOGET30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGET30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDOGET30M"

    def __str__(self):
        return ".BDOGET30M"

    def __call__(self):
        return ".BDOGET30M"


_BDOGET30M = _BDOGET30M(*_BDOGET30M._fields)
"""
    name: .BDOGET30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFILT30M(Symbol):
    """
        name: .BFILT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFILT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFILT30M"

    def __str__(self):
        return ".BFILT30M"

    def __call__(self):
        return ".BFILT30M"


_BFILT30M = _BFILT30M(*_BFILT30M._fields)
"""
    name: .BFILT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUNIT30M(Symbol):
    """
        name: .BUNIT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUNIT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUNIT30M"

    def __str__(self):
        return ".BUNIT30M"

    def __call__(self):
        return ".BUNIT30M"


_BUNIT30M = _BUNIT30M(*_BUNIT30M._fields)
"""
    name: .BUNIT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXLMT30M(Symbol):
    """
        name: .BXLMT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXLMT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXLMT30M"

    def __str__(self):
        return ".BXLMT30M"

    def __call__(self):
        return ".BXLMT30M"


_BXLMT30M = _BXLMT30M(*_BXLMT30M._fields)
"""
    name: .BXLMT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAXS(Symbol):
    """
        name: .BAXS
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXS"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAXS"

    def __str__(self):
        return ".BAXS"

    def __call__(self):
        return ".BAXS"


_BAXS = _BAXS(*_BAXS._fields)
"""
    name: .BAXS
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAXS_NEXT(Symbol):
    """
        name: .BAXS_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXS_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAXS_NEXT"

    def __str__(self):
        return ".BAXS_NEXT"

    def __call__(self):
        return ".BAXS_NEXT"


_BAXS_NEXT = _BAXS_NEXT(*_BAXS_NEXT._fields)
"""
    name: .BAXS_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AXSUSDPI(Symbol):
    """
        name: .AXSUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AXSUSDPI"

    def __str__(self):
        return ".AXSUSDPI"

    def __call__(self):
        return ".AXSUSDPI"


_AXSUSDPI = _AXSUSDPI(*_AXSUSDPI._fields)
"""
    name: .AXSUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AXSUSDPI8H(Symbol):
    """
        name: .AXSUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AXSUSDPI8H"

    def __str__(self):
        return ".AXSUSDPI8H"

    def __call__(self):
        return ".AXSUSDPI8H"


_AXSUSDPI8H = _AXSUSDPI8H(*_AXSUSDPI8H._fields)
"""
    name: .AXSUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEOS(Symbol):
    """
        name: .BEOS
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOS"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEOS"

    def __str__(self):
        return ".BEOS"

    def __call__(self):
        return ".BEOS"


_BEOS = _BEOS(*_BEOS._fields)
"""
    name: .BEOS
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEOS_NEXT(Symbol):
    """
        name: .BEOS_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOS_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEOS_NEXT"

    def __str__(self):
        return ".BEOS_NEXT"

    def __call__(self):
        return ".BEOS_NEXT"


_BEOS_NEXT = _BEOS_NEXT(*_BEOS_NEXT._fields)
"""
    name: .BEOS_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EOSUSDPI(Symbol):
    """
        name: .EOSUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EOSUSDPI"

    def __str__(self):
        return ".EOSUSDPI"

    def __call__(self):
        return ".EOSUSDPI"


_EOSUSDPI = _EOSUSDPI(*_EOSUSDPI._fields)
"""
    name: .EOSUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EOSUSDPI8H(Symbol):
    """
        name: .EOSUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EOSUSDPI8H"

    def __str__(self):
        return ".EOSUSDPI8H"

    def __call__(self):
        return ".EOSUSDPI8H"


_EOSUSDPI8H = _EOSUSDPI8H(*_EOSUSDPI8H._fields)
"""
    name: .EOSUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLINK(Symbol):
    """
        name: .BLINK
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINK"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLINK"

    def __str__(self):
        return ".BLINK"

    def __call__(self):
        return ".BLINK"


_BLINK = _BLINK(*_BLINK._fields)
"""
    name: .BLINK
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLINK_NEXT(Symbol):
    """
        name: .BLINK_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINK_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLINK_NEXT"

    def __str__(self):
        return ".BLINK_NEXT"

    def __call__(self):
        return ".BLINK_NEXT"


_BLINK_NEXT = _BLINK_NEXT(*_BLINK_NEXT._fields)
"""
    name: .BLINK_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LINKUSDPI(Symbol):
    """
        name: .LINKUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LINKUSDPI"

    def __str__(self):
        return ".LINKUSDPI"

    def __call__(self):
        return ".LINKUSDPI"


_LINKUSDPI = _LINKUSDPI(*_LINKUSDPI._fields)
"""
    name: .LINKUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LINKUSDPI8H(Symbol):
    """
        name: .LINKUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LINKUSDPI8H"

    def __str__(self):
        return ".LINKUSDPI8H"

    def __call__(self):
        return ".LINKUSDPI8H"


_LINKUSDPI8H = _LINKUSDPI8H(*_LINKUSDPI8H._fields)
"""
    name: .LINKUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSOL(Symbol):
    """
        name: .BSOL
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOL"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSOL"

    def __str__(self):
        return ".BSOL"

    def __call__(self):
        return ".BSOL"


_BSOL = _BSOL(*_BSOL._fields)
"""
    name: .BSOL
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSOL_NEXT(Symbol):
    """
        name: .BSOL_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOL_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSOL_NEXT"

    def __str__(self):
        return ".BSOL_NEXT"

    def __call__(self):
        return ".BSOL_NEXT"


_BSOL_NEXT = _BSOL_NEXT(*_BSOL_NEXT._fields)
"""
    name: .BSOL_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SOLUSDPI(Symbol):
    """
        name: .SOLUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SOLUSDPI"

    def __str__(self):
        return ".SOLUSDPI"

    def __call__(self):
        return ".SOLUSDPI"


_SOLUSDPI = _SOLUSDPI(*_SOLUSDPI._fields)
"""
    name: .SOLUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SOLUSDPI8H(Symbol):
    """
        name: .SOLUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SOLUSDPI8H"

    def __str__(self):
        return ".SOLUSDPI8H"

    def __call__(self):
        return ".SOLUSDPI8H"


_SOLUSDPI8H = _SOLUSDPI8H(*_SOLUSDPI8H._fields)
"""
    name: .SOLUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAXST30M(Symbol):
    """
        name: .BAXST30M
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXST30M"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAXST30M"

    def __str__(self):
        return ".BAXST30M"

    def __call__(self):
        return ".BAXST30M"


_BAXST30M = _BAXST30M(*_BAXST30M._fields)
"""
    name: .BAXST30M
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSOLT30M(Symbol):
    """
        name: .BSOLT30M
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOLT30M"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSOLT30M"

    def __str__(self):
        return ".BSOLT30M"

    def __call__(self):
        return ".BSOLT30M"


_BSOLT30M = _BSOLT30M(*_BSOLT30M._fields)
"""
    name: .BSOLT30M
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BVETT30M(Symbol):
    """
        name: .BVETT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVETT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BVETT30M"

    def __str__(self):
        return ".BVETT30M"

    def __call__(self):
        return ".BVETT30M"


_BVETT30M = _BVETT30M(*_BVETT30M._fields)
"""
    name: .BVETT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMATICT30M(Symbol):
    """
        name: .BMATICT30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMATICT30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMATICT30M"

    def __str__(self):
        return ".BMATICT30M"

    def __call__(self):
        return ".BMATICT30M"


_BMATICT30M = _BMATICT30M(*_BMATICT30M._fields)
"""
    name: .BMATICT30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAAVET30M(Symbol):
    """
        name: .BAAVET30M
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAAVET30M"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAAVET30M"

    def __str__(self):
        return ".BAAVET30M"

    def __call__(self):
        return ".BAAVET30M"


_BAAVET30M = _BAAVET30M(*_BAAVET30M._fields)
"""
    name: .BAAVET30M
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSUSHIT30M(Symbol):
    """
        name: .BSUSHIT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUSHIT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSUSHIT30M"

    def __str__(self):
        return ".BSUSHIT30M"

    def __call__(self):
        return ".BSUSHIT30M"


_BSUSHIT30M = _BSUSHIT30M(*_BSUSHIT30M._fields)
"""
    name: .BSUSHIT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSRMT30M(Symbol):
    """
        name: .BSRMT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSRMT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSRMT30M"

    def __str__(self):
        return ".BSRMT30M"

    def __call__(self):
        return ".BSRMT30M"


_BSRMT30M = _BSRMT30M(*_BSRMT30M._fields)
"""
    name: .BSRMT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXRPT(Symbol):
    """
        name: .BXRPT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXRPT"

    def __str__(self):
        return ".BXRPT"

    def __call__(self):
        return ".BXRPT"


_BXRPT = _BXRPT(*_BXRPT._fields)
"""
    name: .BXRPT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXRPT_NEXT(Symbol):
    """
        name: .BXRPT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXRPT_NEXT"

    def __str__(self):
        return ".BXRPT_NEXT"

    def __call__(self):
        return ".BXRPT_NEXT"


_BXRPT_NEXT = _BXRPT_NEXT(*_BXRPT_NEXT._fields)
"""
    name: .BXRPT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBCHT(Symbol):
    """
        name: .BBCHT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBCHT"

    def __str__(self):
        return ".BBCHT"

    def __call__(self):
        return ".BBCHT"


_BBCHT = _BBCHT(*_BBCHT._fields)
"""
    name: .BBCHT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBCHT_NEXT(Symbol):
    """
        name: .BBCHT_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBCHT_NEXT"

    def __str__(self):
        return ".BBCHT_NEXT"

    def __call__(self):
        return ".BBCHT_NEXT"


_BBCHT_NEXT = _BBCHT_NEXT(*_BBCHT_NEXT._fields)
"""
    name: .BBCHT_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XRPUSDTPI(Symbol):
    """
        name: .XRPUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XRPUSDTPI"

    def __str__(self):
        return ".XRPUSDTPI"

    def __call__(self):
        return ".XRPUSDTPI"


_XRPUSDTPI = _XRPUSDTPI(*_XRPUSDTPI._fields)
"""
    name: .XRPUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XRPUSDTPI8H(Symbol):
    """
        name: .XRPUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XRPUSDTPI8H"

    def __str__(self):
        return ".XRPUSDTPI8H"

    def __call__(self):
        return ".XRPUSDTPI8H"


_XRPUSDTPI8H = _XRPUSDTPI8H(*_XRPUSDTPI8H._fields)
"""
    name: .XRPUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCHUSDTPI(Symbol):
    """
        name: .BCHUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCHUSDTPI"

    def __str__(self):
        return ".BCHUSDTPI"

    def __call__(self):
        return ".BCHUSDTPI"


_BCHUSDTPI = _BCHUSDTPI(*_BCHUSDTPI._fields)
"""
    name: .BCHUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCHUSDTPI8H(Symbol):
    """
        name: .BCHUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCHUSDTPI8H"

    def __str__(self):
        return ".BCHUSDTPI8H"

    def __call__(self):
        return ".BCHUSDTPI8H"


_BCHUSDTPI8H = _BCHUSDTPI8H(*_BCHUSDTPI8H._fields)
"""
    name: .BCHUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDEFIMEX30M(Symbol):
    """
        name: .BDEFIMEX30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDEFIMEX30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDEFIMEX30M"

    def __str__(self):
        return ".BDEFIMEX30M"

    def __call__(self):
        return ".BDEFIMEX30M"


_BDEFIMEX30M = _BDEFIMEX30M(*_BDEFIMEX30M._fields)
"""
    name: .BDEFIMEX30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BALTMEX30M(Symbol):
    """
        name: .BALTMEX30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BALTMEX30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BALTMEX30M"

    def __str__(self):
        return ".BALTMEX30M"

    def __call__(self):
        return ".BALTMEX30M"


_BALTMEX30M = _BALTMEX30M(*_BALTMEX30M._fields)
"""
    name: .BALTMEX30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFTMT(Symbol):
    """
        name: .BFTMT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTMT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFTMT"

    def __str__(self):
        return ".BFTMT"

    def __call__(self):
        return ".BFTMT"


_BFTMT = _BFTMT(*_BFTMT._fields)
"""
    name: .BFTMT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFTMT_NEXT(Symbol):
    """
        name: .BFTMT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTMT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFTMT_NEXT"

    def __str__(self):
        return ".BFTMT_NEXT"

    def __call__(self):
        return ".BFTMT_NEXT"


_BFTMT_NEXT = _BFTMT_NEXT(*_BFTMT_NEXT._fields)
"""
    name: .BFTMT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTMBON(Symbol):
    """
        name: .FTMBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTMBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTMBON"

    def __str__(self):
        return ".FTMBON"

    def __call__(self):
        return ".FTMBON"


_FTMBON = _FTMBON(*_FTMBON._fields)
"""
    name: .FTMBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTMBON8H(Symbol):
    """
        name: .FTMBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTMBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTMBON8H"

    def __str__(self):
        return ".FTMBON8H"

    def __call__(self):
        return ".FTMBON8H"


_FTMBON8H = _FTMBON8H(*_FTMBON8H._fields)
"""
    name: .FTMBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTMUSDTPI(Symbol):
    """
        name: .FTMUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTMUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTMUSDTPI"

    def __str__(self):
        return ".FTMUSDTPI"

    def __call__(self):
        return ".FTMUSDTPI"


_FTMUSDTPI = _FTMUSDTPI(*_FTMUSDTPI._fields)
"""
    name: .FTMUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTMUSDTPI8H(Symbol):
    """
        name: .FTMUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTMUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTMUSDTPI8H"

    def __str__(self):
        return ".FTMUSDTPI8H"

    def __call__(self):
        return ".FTMUSDTPI8H"


_FTMUSDTPI8H = _FTMUSDTPI8H(*_FTMUSDTPI8H._fields)
"""
    name: .FTMUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSHIBT(Symbol):
    """
        name: .BSHIBT
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSHIBT"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSHIBT"

    def __str__(self):
        return ".BSHIBT"

    def __call__(self):
        return ".BSHIBT"


_BSHIBT = _BSHIBT(*_BSHIBT._fields)
"""
    name: .BSHIBT
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSHIBT_NEXT(Symbol):
    """
        name: .BSHIBT_NEXT
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSHIBT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSHIBT_NEXT"

    def __str__(self):
        return ".BSHIBT_NEXT"

    def __call__(self):
        return ".BSHIBT_NEXT"


_BSHIBT_NEXT = _BSHIBT_NEXT(*_BSHIBT_NEXT._fields)
"""
    name: .BSHIBT_NEXT
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SHIBBON(Symbol):
    """
        name: .SHIBBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SHIBBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SHIBBON"

    def __str__(self):
        return ".SHIBBON"

    def __call__(self):
        return ".SHIBBON"


_SHIBBON = _SHIBBON(*_SHIBBON._fields)
"""
    name: .SHIBBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SHIBBON8H(Symbol):
    """
        name: .SHIBBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SHIBBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SHIBBON8H"

    def __str__(self):
        return ".SHIBBON8H"

    def __call__(self):
        return ".SHIBBON8H"


_SHIBBON8H = _SHIBBON8H(*_SHIBBON8H._fields)
"""
    name: .SHIBBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SHIBUSDTPI(Symbol):
    """
        name: .SHIBUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SHIBUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SHIBUSDTPI"

    def __str__(self):
        return ".SHIBUSDTPI"

    def __call__(self):
        return ".SHIBUSDTPI"


_SHIBUSDTPI = _SHIBUSDTPI(*_SHIBUSDTPI._fields)
"""
    name: .SHIBUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SHIBUSDTPI8H(Symbol):
    """
        name: .SHIBUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SHIBUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SHIBUSDTPI8H"

    def __str__(self):
        return ".SHIBUSDTPI8H"

    def __call__(self):
        return ".SHIBUSDTPI8H"


_SHIBUSDTPI8H = _SHIBUSDTPI8H(*_SHIBUSDTPI8H._fields)
"""
    name: .SHIBUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLRCT(Symbol):
    """
        name: .BLRCT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLRCT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLRCT"

    def __str__(self):
        return ".BLRCT"

    def __call__(self):
        return ".BLRCT"


_BLRCT = _BLRCT(*_BLRCT._fields)
"""
    name: .BLRCT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLRCT_NEXT(Symbol):
    """
        name: .BLRCT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLRCT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLRCT_NEXT"

    def __str__(self):
        return ".BLRCT_NEXT"

    def __call__(self):
        return ".BLRCT_NEXT"


_BLRCT_NEXT = _BLRCT_NEXT(*_BLRCT_NEXT._fields)
"""
    name: .BLRCT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMANAT(Symbol):
    """
        name: .BMANAT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMANAT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMANAT"

    def __str__(self):
        return ".BMANAT"

    def __call__(self):
        return ".BMANAT"


_BMANAT = _BMANAT(*_BMANAT._fields)
"""
    name: .BMANAT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMANAT_NEXT(Symbol):
    """
        name: .BMANAT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMANAT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMANAT_NEXT"

    def __str__(self):
        return ".BMANAT_NEXT"

    def __call__(self):
        return ".BMANAT_NEXT"


_BMANAT_NEXT = _BMANAT_NEXT(*_BMANAT_NEXT._fields)
"""
    name: .BMANAT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MANABON(Symbol):
    """
        name: .MANABON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MANABON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MANABON"

    def __str__(self):
        return ".MANABON"

    def __call__(self):
        return ".MANABON"


_MANABON = _MANABON(*_MANABON._fields)
"""
    name: .MANABON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MANABON8H(Symbol):
    """
        name: .MANABON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MANABON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MANABON8H"

    def __str__(self):
        return ".MANABON8H"

    def __call__(self):
        return ".MANABON8H"


_MANABON8H = _MANABON8H(*_MANABON8H._fields)
"""
    name: .MANABON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MANAUSDTPI(Symbol):
    """
        name: .MANAUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MANAUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MANAUSDTPI"

    def __str__(self):
        return ".MANAUSDTPI"

    def __call__(self):
        return ".MANAUSDTPI"


_MANAUSDTPI = _MANAUSDTPI(*_MANAUSDTPI._fields)
"""
    name: .MANAUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MANAUSDTPI8H(Symbol):
    """
        name: .MANAUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MANAUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MANAUSDTPI8H"

    def __str__(self):
        return ".MANAUSDTPI8H"

    def __call__(self):
        return ".MANAUSDTPI8H"


_MANAUSDTPI8H = _MANAUSDTPI8H(*_MANAUSDTPI8H._fields)
"""
    name: .MANAUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSANDT(Symbol):
    """
        name: .BSANDT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSANDT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSANDT"

    def __str__(self):
        return ".BSANDT"

    def __call__(self):
        return ".BSANDT"


_BSANDT = _BSANDT(*_BSANDT._fields)
"""
    name: .BSANDT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSANDT_NEXT(Symbol):
    """
        name: .BSANDT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSANDT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSANDT_NEXT"

    def __str__(self):
        return ".BSANDT_NEXT"

    def __call__(self):
        return ".BSANDT_NEXT"


_BSANDT_NEXT = _BSANDT_NEXT(*_BSANDT_NEXT._fields)
"""
    name: .BSANDT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SANDBON(Symbol):
    """
        name: .SANDBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SANDBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SANDBON"

    def __str__(self):
        return ".SANDBON"

    def __call__(self):
        return ".SANDBON"


_SANDBON = _SANDBON(*_SANDBON._fields)
"""
    name: .SANDBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SANDBON8H(Symbol):
    """
        name: .SANDBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SANDBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SANDBON8H"

    def __str__(self):
        return ".SANDBON8H"

    def __call__(self):
        return ".SANDBON8H"


_SANDBON8H = _SANDBON8H(*_SANDBON8H._fields)
"""
    name: .SANDBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SANDUSDTPI(Symbol):
    """
        name: .SANDUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SANDUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SANDUSDTPI"

    def __str__(self):
        return ".SANDUSDTPI"

    def __call__(self):
        return ".SANDUSDTPI"


_SANDUSDTPI = _SANDUSDTPI(*_SANDUSDTPI._fields)
"""
    name: .SANDUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SANDUSDTPI8H(Symbol):
    """
        name: .SANDUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SANDUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SANDUSDTPI8H"

    def __str__(self):
        return ".SANDUSDTPI8H"

    def __call__(self):
        return ".SANDUSDTPI8H"


_SANDUSDTPI8H = _SANDUSDTPI8H(*_SANDUSDTPI8H._fields)
"""
    name: .SANDUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTHETAT(Symbol):
    """
        name: .BTHETAT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTHETAT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTHETAT"

    def __str__(self):
        return ".BTHETAT"

    def __call__(self):
        return ".BTHETAT"


_BTHETAT = _BTHETAT(*_BTHETAT._fields)
"""
    name: .BTHETAT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTHETAT_NEXT(Symbol):
    """
        name: .BTHETAT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTHETAT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTHETAT_NEXT"

    def __str__(self):
        return ".BTHETAT_NEXT"

    def __call__(self):
        return ".BTHETAT_NEXT"


_BTHETAT_NEXT = _BTHETAT_NEXT(*_BTHETAT_NEXT._fields)
"""
    name: .BTHETAT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BENJT(Symbol):
    """
        name: .BENJT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BENJT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BENJT"

    def __str__(self):
        return ".BENJT"

    def __call__(self):
        return ".BENJT"


_BENJT = _BENJT(*_BENJT._fields)
"""
    name: .BENJT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BENJT_NEXT(Symbol):
    """
        name: .BENJT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BENJT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BENJT_NEXT"

    def __str__(self):
        return ".BENJT_NEXT"

    def __call__(self):
        return ".BENJT_NEXT"


_BENJT_NEXT = _BENJT_NEXT(*_BENJT_NEXT._fields)
"""
    name: .BENJT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDEFIMEXT(Symbol):
    """
        name: .BDEFIMEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDEFIMEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDEFIMEXT"

    def __str__(self):
        return ".BDEFIMEXT"

    def __call__(self):
        return ".BDEFIMEXT"


_BDEFIMEXT = _BDEFIMEXT(*_BDEFIMEXT._fields)
"""
    name: .BDEFIMEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DEFIMEXTBON(Symbol):
    """
        name: .DEFIMEXTBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXTBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DEFIMEXTBON"

    def __str__(self):
        return ".DEFIMEXTBON"

    def __call__(self):
        return ".DEFIMEXTBON"


_DEFIMEXTBON = _DEFIMEXTBON(*_DEFIMEXTBON._fields)
"""
    name: .DEFIMEXTBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DEFIMEXTBON8H(Symbol):
    """
        name: .DEFIMEXTBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXTBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DEFIMEXTBON8H"

    def __str__(self):
        return ".DEFIMEXTBON8H"

    def __call__(self):
        return ".DEFIMEXTBON8H"


_DEFIMEXTBON8H = _DEFIMEXTBON8H(*_DEFIMEXTBON8H._fields)
"""
    name: .DEFIMEXTBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DEFIMEXTUSDTPI(Symbol):
    """
        name: .DEFIMEXTUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXTUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DEFIMEXTUSDTPI"

    def __str__(self):
        return ".DEFIMEXTUSDTPI"

    def __call__(self):
        return ".DEFIMEXTUSDTPI"


_DEFIMEXTUSDTPI = _DEFIMEXTUSDTPI(*_DEFIMEXTUSDTPI._fields)
"""
    name: .DEFIMEXTUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _DEFIMEXTUSDTPI8H(Symbol):
    """
        name: .DEFIMEXTUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXTUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".DEFIMEXTUSDTPI8H"

    def __str__(self):
        return ".DEFIMEXTUSDTPI8H"

    def __call__(self):
        return ".DEFIMEXTUSDTPI8H"


_DEFIMEXTUSDTPI8H = _DEFIMEXTUSDTPI8H(*_DEFIMEXTUSDTPI8H._fields)
"""
    name: .DEFIMEXTUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BALTMEXT(Symbol):
    """
        name: .BALTMEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BALTMEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BALTMEXT"

    def __str__(self):
        return ".BALTMEXT"

    def __call__(self):
        return ".BALTMEXT"


_BALTMEXT = _BALTMEXT(*_BALTMEXT._fields)
"""
    name: .BALTMEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ALTMEXTBON(Symbol):
    """
        name: .ALTMEXTBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXTBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ALTMEXTBON"

    def __str__(self):
        return ".ALTMEXTBON"

    def __call__(self):
        return ".ALTMEXTBON"


_ALTMEXTBON = _ALTMEXTBON(*_ALTMEXTBON._fields)
"""
    name: .ALTMEXTBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ALTMEXTBON8H(Symbol):
    """
        name: .ALTMEXTBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXTBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ALTMEXTBON8H"

    def __str__(self):
        return ".ALTMEXTBON8H"

    def __call__(self):
        return ".ALTMEXTBON8H"


_ALTMEXTBON8H = _ALTMEXTBON8H(*_ALTMEXTBON8H._fields)
"""
    name: .ALTMEXTBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ALTMEXTUSDTPI(Symbol):
    """
        name: .ALTMEXTUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXTUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ALTMEXTUSDTPI"

    def __str__(self):
        return ".ALTMEXTUSDTPI"

    def __call__(self):
        return ".ALTMEXTUSDTPI"


_ALTMEXTUSDTPI = _ALTMEXTUSDTPI(*_ALTMEXTUSDTPI._fields)
"""
    name: .ALTMEXTUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ALTMEXTUSDTPI8H(Symbol):
    """
        name: .ALTMEXTUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXTUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ALTMEXTUSDTPI8H"

    def __str__(self):
        return ".ALTMEXTUSDTPI8H"

    def __call__(self):
        return ".ALTMEXTUSDTPI8H"


_ALTMEXTUSDTPI8H = _ALTMEXTUSDTPI8H(*_ALTMEXTUSDTPI8H._fields)
"""
    name: .ALTMEXTUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMETAMEXT(Symbol):
    """
        name: .BMETAMEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMETAMEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMETAMEXT"

    def __str__(self):
        return ".BMETAMEXT"

    def __call__(self):
        return ".BMETAMEXT"


_BMETAMEXT = _BMETAMEXT(*_BMETAMEXT._fields)
"""
    name: .BMETAMEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _METAMEXTBON(Symbol):
    """
        name: .METAMEXTBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".METAMEXTBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".METAMEXTBON"

    def __str__(self):
        return ".METAMEXTBON"

    def __call__(self):
        return ".METAMEXTBON"


_METAMEXTBON = _METAMEXTBON(*_METAMEXTBON._fields)
"""
    name: .METAMEXTBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _METAMEXTBON8H(Symbol):
    """
        name: .METAMEXTBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".METAMEXTBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".METAMEXTBON8H"

    def __str__(self):
        return ".METAMEXTBON8H"

    def __call__(self):
        return ".METAMEXTBON8H"


_METAMEXTBON8H = _METAMEXTBON8H(*_METAMEXTBON8H._fields)
"""
    name: .METAMEXTBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _METAMEXTUSDTPI(Symbol):
    """
        name: .METAMEXTUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".METAMEXTUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".METAMEXTUSDTPI"

    def __str__(self):
        return ".METAMEXTUSDTPI"

    def __call__(self):
        return ".METAMEXTUSDTPI"


_METAMEXTUSDTPI = _METAMEXTUSDTPI(*_METAMEXTUSDTPI._fields)
"""
    name: .METAMEXTUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _METAMEXTUSDTPI8H(Symbol):
    """
        name: .METAMEXTUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".METAMEXTUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".METAMEXTUSDTPI8H"

    def __str__(self):
        return ".METAMEXTUSDTPI8H"

    def __call__(self):
        return ".METAMEXTUSDTPI8H"


_METAMEXTUSDTPI8H = _METAMEXTUSDTPI8H(*_METAMEXTUSDTPI8H._fields)
"""
    name: .METAMEXTUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AVAXUSDTPI(Symbol):
    """
        name: .AVAXUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AVAXUSDTPI"

    def __str__(self):
        return ".AVAXUSDTPI"

    def __call__(self):
        return ".AVAXUSDTPI"


_AVAXUSDTPI = _AVAXUSDTPI(*_AVAXUSDTPI._fields)
"""
    name: .AVAXUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _AVAXUSDTPI8H(Symbol):
    """
        name: .AVAXUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".AVAXUSDTPI8H"

    def __str__(self):
        return ".AVAXUSDTPI8H"

    def __call__(self):
        return ".AVAXUSDTPI8H"


_AVAXUSDTPI8H = _AVAXUSDTPI8H(*_AVAXUSDTPI8H._fields)
"""
    name: .AVAXUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LUNAUSDTPI(Symbol):
    """
        name: .LUNAUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNAUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LUNAUSDTPI"

    def __str__(self):
        return ".LUNAUSDTPI"

    def __call__(self):
        return ".LUNAUSDTPI"


_LUNAUSDTPI = _LUNAUSDTPI(*_LUNAUSDTPI._fields)
"""
    name: .LUNAUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LUNAUSDTPI8H(Symbol):
    """
        name: .LUNAUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNAUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LUNAUSDTPI8H"

    def __str__(self):
        return ".LUNAUSDTPI8H"

    def __call__(self):
        return ".LUNAUSDTPI8H"


_LUNAUSDTPI8H = _LUNAUSDTPI8H(*_LUNAUSDTPI8H._fields)
"""
    name: .LUNAUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPET(Symbol):
    """
        name: .BAPET
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPET"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPET"

    def __str__(self):
        return ".BAPET"

    def __call__(self):
        return ".BAPET"


_BAPET = _BAPET(*_BAPET._fields)
"""
    name: .BAPET
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPET_NEXT(Symbol):
    """
        name: .BAPET_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPET_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPET_NEXT"

    def __str__(self):
        return ".BAPET_NEXT"

    def __call__(self):
        return ".BAPET_NEXT"


_BAPET_NEXT = _BAPET_NEXT(*_BAPET_NEXT._fields)
"""
    name: .BAPET_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APEBON(Symbol):
    """
        name: .APEBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APEBON"

    def __str__(self):
        return ".APEBON"

    def __call__(self):
        return ".APEBON"


_APEBON = _APEBON(*_APEBON._fields)
"""
    name: .APEBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APEBON8H(Symbol):
    """
        name: .APEBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APEBON8H"

    def __str__(self):
        return ".APEBON8H"

    def __call__(self):
        return ".APEBON8H"


_APEBON8H = _APEBON8H(*_APEBON8H._fields)
"""
    name: .APEBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APEUSDTPI(Symbol):
    """
        name: .APEUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APEUSDTPI"

    def __str__(self):
        return ".APEUSDTPI"

    def __call__(self):
        return ".APEUSDTPI"


_APEUSDTPI = _APEUSDTPI(*_APEUSDTPI._fields)
"""
    name: .APEUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APEUSDTPI8H(Symbol):
    """
        name: .APEUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APEUSDTPI8H"

    def __str__(self):
        return ".APEUSDTPI8H"

    def __call__(self):
        return ".APEUSDTPI8H"


_APEUSDTPI8H = _APEUSDTPI8H(*_APEUSDTPI8H._fields)
"""
    name: .APEUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMTBON(Symbol):
    """
        name: .GMTBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMTBON"

    def __str__(self):
        return ".GMTBON"

    def __call__(self):
        return ".GMTBON"


_GMTBON = _GMTBON(*_GMTBON._fields)
"""
    name: .GMTBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMTBON8H(Symbol):
    """
        name: .GMTBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMTBON8H"

    def __str__(self):
        return ".GMTBON8H"

    def __call__(self):
        return ".GMTBON8H"


_GMTBON8H = _GMTBON8H(*_GMTBON8H._fields)
"""
    name: .GMTBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMTUSDTPI(Symbol):
    """
        name: .GMTUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMTUSDTPI"

    def __str__(self):
        return ".GMTUSDTPI"

    def __call__(self):
        return ".GMTUSDTPI"


_GMTUSDTPI = _GMTUSDTPI(*_GMTUSDTPI._fields)
"""
    name: .GMTUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMTUSDTPI8H(Symbol):
    """
        name: .GMTUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMTUSDTPI8H"

    def __str__(self):
        return ".GMTUSDTPI8H"

    def __call__(self):
        return ".GMTUSDTPI8H"


_GMTUSDTPI8H = _GMTUSDTPI8H(*_GMTUSDTPI8H._fields)
"""
    name: .GMTUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMTUSDPI(Symbol):
    """
        name: .GMTUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMTUSDPI"

    def __str__(self):
        return ".GMTUSDPI"

    def __call__(self):
        return ".GMTUSDPI"


_GMTUSDPI = _GMTUSDPI(*_GMTUSDPI._fields)
"""
    name: .GMTUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMTUSDPI8H(Symbol):
    """
        name: .GMTUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMTUSDPI8H"

    def __str__(self):
        return ".GMTUSDPI8H"

    def __call__(self):
        return ".GMTUSDPI8H"


_GMTUSDPI8H = _GMTUSDPI8H(*_GMTUSDPI8H._fields)
"""
    name: .GMTUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGMT(Symbol):
    """
        name: .BGMT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGMT"

    def __str__(self):
        return ".BGMT"

    def __call__(self):
        return ".BGMT"


_BGMT = _BGMT(*_BGMT._fields)
"""
    name: .BGMT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGMT_NEXT(Symbol):
    """
        name: .BGMT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGMT_NEXT"

    def __str__(self):
        return ".BGMT_NEXT"

    def __call__(self):
        return ".BGMT_NEXT"


_BGMT_NEXT = _BGMT_NEXT(*_BGMT_NEXT._fields)
"""
    name: .BGMT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGMTT(Symbol):
    """
        name: .BGMTT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMTT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGMTT"

    def __str__(self):
        return ".BGMTT"

    def __call__(self):
        return ".BGMTT"


_BGMTT = _BGMTT(*_BGMTT._fields)
"""
    name: .BGMTT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGMTT_NEXT(Symbol):
    """
        name: .BGMTT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMTT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGMTT_NEXT"

    def __str__(self):
        return ".BGMTT_NEXT"

    def __call__(self):
        return ".BGMTT_NEXT"


_BGMTT_NEXT = _BGMTT_NEXT(*_BGMTT_NEXT._fields)
"""
    name: .BGMTT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NEARBON(Symbol):
    """
        name: .NEARBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NEARBON"

    def __str__(self):
        return ".NEARBON"

    def __call__(self):
        return ".NEARBON"


_NEARBON = _NEARBON(*_NEARBON._fields)
"""
    name: .NEARBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NEARBON8H(Symbol):
    """
        name: .NEARBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NEARBON8H"

    def __str__(self):
        return ".NEARBON8H"

    def __call__(self):
        return ".NEARBON8H"


_NEARBON8H = _NEARBON8H(*_NEARBON8H._fields)
"""
    name: .NEARBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NEARUSDTPI(Symbol):
    """
        name: .NEARUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NEARUSDTPI"

    def __str__(self):
        return ".NEARUSDTPI"

    def __call__(self):
        return ".NEARUSDTPI"


_NEARUSDTPI = _NEARUSDTPI(*_NEARUSDTPI._fields)
"""
    name: .NEARUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NEARUSDTPI8H(Symbol):
    """
        name: .NEARUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NEARUSDTPI8H"

    def __str__(self):
        return ".NEARUSDTPI8H"

    def __call__(self):
        return ".NEARUSDTPI8H"


_NEARUSDTPI8H = _NEARUSDTPI8H(*_NEARUSDTPI8H._fields)
"""
    name: .NEARUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NEARUSDPI(Symbol):
    """
        name: .NEARUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NEARUSDPI"

    def __str__(self):
        return ".NEARUSDPI"

    def __call__(self):
        return ".NEARUSDPI"


_NEARUSDPI = _NEARUSDPI(*_NEARUSDPI._fields)
"""
    name: .NEARUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NEARUSDPI8H(Symbol):
    """
        name: .NEARUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NEARUSDPI8H"

    def __str__(self):
        return ".NEARUSDPI8H"

    def __call__(self):
        return ".NEARUSDPI8H"


_NEARUSDPI8H = _NEARUSDPI8H(*_NEARUSDPI8H._fields)
"""
    name: .NEARUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNEAR(Symbol):
    """
        name: .BNEAR
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEAR"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNEAR"

    def __str__(self):
        return ".BNEAR"

    def __call__(self):
        return ".BNEAR"


_BNEAR = _BNEAR(*_BNEAR._fields)
"""
    name: .BNEAR
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNEAR_NEXT(Symbol):
    """
        name: .BNEAR_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEAR_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNEAR_NEXT"

    def __str__(self):
        return ".BNEAR_NEXT"

    def __call__(self):
        return ".BNEAR_NEXT"


_BNEAR_NEXT = _BNEAR_NEXT(*_BNEAR_NEXT._fields)
"""
    name: .BNEAR_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNEART(Symbol):
    """
        name: .BNEART
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEART"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNEART"

    def __str__(self):
        return ".BNEART"

    def __call__(self):
        return ".BNEART"


_BNEART = _BNEART(*_BNEART._fields)
"""
    name: .BNEART
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNEART_NEXT(Symbol):
    """
        name: .BNEART_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEART_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNEART_NEXT"

    def __str__(self):
        return ".BNEART_NEXT"

    def __call__(self):
        return ".BNEART_NEXT"


_BNEART_NEXT = _BNEART_NEXT(*_BNEART_NEXT._fields)
"""
    name: .BNEART_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNA30M(Symbol):
    """
        name: .BLUNA30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNA30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNA30M"

    def __str__(self):
        return ".BLUNA30M"

    def __call__(self):
        return ".BLUNA30M"


_BLUNA30M = _BLUNA30M(*_BLUNA30M._fields)
"""
    name: .BLUNA30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNAT30M(Symbol):
    """
        name: .BLUNAT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNAT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNAT30M"

    def __str__(self):
        return ".BLUNAT30M"

    def __call__(self):
        return ".BLUNAT30M"


_BLUNAT30M = _BLUNAT30M(*_BLUNAT30M._fields)
"""
    name: .BLUNAT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPE(Symbol):
    """
        name: .BAPE
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPE"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPE"

    def __str__(self):
        return ".BAPE"

    def __call__(self):
        return ".BAPE"


_BAPE = _BAPE(*_BAPE._fields)
"""
    name: .BAPE
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPE_NEXT(Symbol):
    """
        name: .BAPE_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPE_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPE_NEXT"

    def __str__(self):
        return ".BAPE_NEXT"

    def __call__(self):
        return ".BAPE_NEXT"


_BAPE_NEXT = _BAPE_NEXT(*_BAPE_NEXT._fields)
"""
    name: .BAPE_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTRX(Symbol):
    """
        name: .BTRX
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRX"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTRX"

    def __str__(self):
        return ".BTRX"

    def __call__(self):
        return ".BTRX"


_BTRX = _BTRX(*_BTRX._fields)
"""
    name: .BTRX
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTRX_NEXT(Symbol):
    """
        name: .BTRX_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRX_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTRX_NEXT"

    def __str__(self):
        return ".BTRX_NEXT"

    def __call__(self):
        return ".BTRX_NEXT"


_BTRX_NEXT = _BTRX_NEXT(*_BTRX_NEXT._fields)
"""
    name: .BTRX_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGAL(Symbol):
    """
        name: .BGAL
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGAL"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGAL"

    def __str__(self):
        return ".BGAL"

    def __call__(self):
        return ".BGAL"


_BGAL = _BGAL(*_BGAL._fields)
"""
    name: .BGAL
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGAL_NEXT(Symbol):
    """
        name: .BGAL_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGAL_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGAL_NEXT"

    def __str__(self):
        return ".BGAL_NEXT"

    def __call__(self):
        return ".BGAL_NEXT"


_BGAL_NEXT = _BGAL_NEXT(*_BGAL_NEXT._fields)
"""
    name: .BGAL_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGALT(Symbol):
    """
        name: .BGALT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGALT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGALT"

    def __str__(self):
        return ".BGALT"

    def __call__(self):
        return ".BGALT"


_BGALT = _BGALT(*_BGALT._fields)
"""
    name: .BGALT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGALT_NEXT(Symbol):
    """
        name: .BGALT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGALT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGALT_NEXT"

    def __str__(self):
        return ".BGALT_NEXT"

    def __call__(self):
        return ".BGALT_NEXT"


_BGALT_NEXT = _BGALT_NEXT(*_BGALT_NEXT._fields)
"""
    name: .BGALT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GALBON(Symbol):
    """
        name: .GALBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GALBON"

    def __str__(self):
        return ".GALBON"

    def __call__(self):
        return ".GALBON"


_GALBON = _GALBON(*_GALBON._fields)
"""
    name: .GALBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GALBON8H(Symbol):
    """
        name: .GALBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GALBON8H"

    def __str__(self):
        return ".GALBON8H"

    def __call__(self):
        return ".GALBON8H"


_GALBON8H = _GALBON8H(*_GALBON8H._fields)
"""
    name: .GALBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APEUSDPI(Symbol):
    """
        name: .APEUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APEUSDPI"

    def __str__(self):
        return ".APEUSDPI"

    def __call__(self):
        return ".APEUSDPI"


_APEUSDPI = _APEUSDPI(*_APEUSDPI._fields)
"""
    name: .APEUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APEUSDPI8H(Symbol):
    """
        name: .APEUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APEUSDPI8H"

    def __str__(self):
        return ".APEUSDPI8H"

    def __call__(self):
        return ".APEUSDPI8H"


_APEUSDPI8H = _APEUSDPI8H(*_APEUSDPI8H._fields)
"""
    name: .APEUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _TRXUSDPI(Symbol):
    """
        name: .TRXUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".TRXUSDPI"

    def __str__(self):
        return ".TRXUSDPI"

    def __call__(self):
        return ".TRXUSDPI"


_TRXUSDPI = _TRXUSDPI(*_TRXUSDPI._fields)
"""
    name: .TRXUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _TRXUSDPI8H(Symbol):
    """
        name: .TRXUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".TRXUSDPI8H"

    def __str__(self):
        return ".TRXUSDPI8H"

    def __call__(self):
        return ".TRXUSDPI8H"


_TRXUSDPI8H = _TRXUSDPI8H(*_TRXUSDPI8H._fields)
"""
    name: .TRXUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GALUSDTPI(Symbol):
    """
        name: .GALUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GALUSDTPI"

    def __str__(self):
        return ".GALUSDTPI"

    def __call__(self):
        return ".GALUSDTPI"


_GALUSDTPI = _GALUSDTPI(*_GALUSDTPI._fields)
"""
    name: .GALUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GALUSDTPI8H(Symbol):
    """
        name: .GALUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GALUSDTPI8H"

    def __str__(self):
        return ".GALUSDTPI8H"

    def __call__(self):
        return ".GALUSDTPI8H"


_GALUSDTPI8H = _GALUSDTPI8H(*_GALUSDTPI8H._fields)
"""
    name: .GALUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GALUSDPI(Symbol):
    """
        name: .GALUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GALUSDPI"

    def __str__(self):
        return ".GALUSDPI"

    def __call__(self):
        return ".GALUSDPI"


_GALUSDPI = _GALUSDPI(*_GALUSDPI._fields)
"""
    name: .GALUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GALUSDPI8H(Symbol):
    """
        name: .GALUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GALUSDPI8H"

    def __str__(self):
        return ".GALUSDPI8H"

    def __call__(self):
        return ".GALUSDPI8H"


_GALUSDPI8H = _GALUSDPI8H(*_GALUSDPI8H._fields)
"""
    name: .GALUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNC(Symbol):
    """
        name: .BLUNC
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNC"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNC"

    def __str__(self):
        return ".BLUNC"

    def __call__(self):
        return ".BLUNC"


_BLUNC = _BLUNC(*_BLUNC._fields)
"""
    name: .BLUNC
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNC_NEXT(Symbol):
    """
        name: .BLUNC_NEXT
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNC_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNC_NEXT"

    def __str__(self):
        return ".BLUNC_NEXT"

    def __call__(self):
        return ".BLUNC_NEXT"


_BLUNC_NEXT = _BLUNC_NEXT(*_BLUNC_NEXT._fields)
"""
    name: .BLUNC_NEXT
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNCT(Symbol):
    """
        name: .BLUNCT
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNCT"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNCT"

    def __str__(self):
        return ".BLUNCT"

    def __call__(self):
        return ".BLUNCT"


_BLUNCT = _BLUNCT(*_BLUNCT._fields)
"""
    name: .BLUNCT
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLUNCT_NEXT(Symbol):
    """
        name: .BLUNCT_NEXT
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNCT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLUNCT_NEXT"

    def __str__(self):
        return ".BLUNCT_NEXT"

    def __call__(self):
        return ".BLUNCT_NEXT"


_BLUNCT_NEXT = _BLUNCT_NEXT(*_BLUNCT_NEXT._fields)
"""
    name: .BLUNCT_NEXT
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDFI(Symbol):
    """
        name: .BDFI
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDFI"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDFI"

    def __str__(self):
        return ".BDFI"

    def __call__(self):
        return ".BDFI"


_BDFI = _BDFI(*_BDFI._fields)
"""
    name: .BDFI
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDFIT(Symbol):
    """
        name: .BDFIT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDFIT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDFIT"

    def __str__(self):
        return ".BDFIT"

    def __call__(self):
        return ".BDFIT"


_BDFIT = _BDFIT(*_BDFIT._fields)
"""
    name: .BDFIT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGRT(Symbol):
    """
        name: .BGRT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGRT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGRT"

    def __str__(self):
        return ".BGRT"

    def __call__(self):
        return ".BGRT"


_BGRT = _BGRT(*_BGRT._fields)
"""
    name: .BGRT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURUSDPI(Symbol):
    """
        name: .EURUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURUSDPI"

    def __str__(self):
        return ".EURUSDPI"

    def __call__(self):
        return ".EURUSDPI"


_EURUSDPI = _EURUSDPI(*_EURUSDPI._fields)
"""
    name: .EURUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDCHFPI(Symbol):
    """
        name: .USDCHFPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCHFPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDCHFPI"

    def __str__(self):
        return ".USDCHFPI"

    def __call__(self):
        return ".USDCHFPI"


_USDCHFPI = _USDCHFPI(*_USDCHFPI._fields)
"""
    name: .USDCHFPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURCHFPI(Symbol):
    """
        name: .EURCHFPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURCHFPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURCHFPI"

    def __str__(self):
        return ".EURCHFPI"

    def __call__(self):
        return ".EURCHFPI"


_EURCHFPI = _EURCHFPI(*_EURCHFPI._fields)
"""
    name: .EURCHFPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURTRYPI(Symbol):
    """
        name: .EURTRYPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURTRYPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURTRYPI"

    def __str__(self):
        return ".EURTRYPI"

    def __call__(self):
        return ".EURTRYPI"


_EURTRYPI = _EURTRYPI(*_EURTRYPI._fields)
"""
    name: .EURTRYPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTRYPI(Symbol):
    """
        name: .USDTRYPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTRYPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTRYPI"

    def __str__(self):
        return ".USDTRYPI"

    def __call__(self):
        return ".USDTRYPI"


_USDTRYPI = _USDTRYPI(*_USDTRYPI._fields)
"""
    name: .USDTRYPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDINRPI(Symbol):
    """
        name: .USDINRPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDINRPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDINRPI"

    def __str__(self):
        return ".USDINRPI"

    def __call__(self):
        return ".USDINRPI"


_USDINRPI = _USDINRPI(*_USDINRPI._fields)
"""
    name: .USDINRPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDZARPI(Symbol):
    """
        name: .USDZARPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDZARPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDZARPI"

    def __str__(self):
        return ".USDZARPI"

    def __call__(self):
        return ".USDZARPI"


_USDZARPI = _USDZARPI(*_USDZARPI._fields)
"""
    name: .USDZARPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDBRLPI(Symbol):
    """
        name: .USDBRLPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDBRLPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDBRLPI"

    def __str__(self):
        return ".USDBRLPI"

    def __call__(self):
        return ".USDBRLPI"


_USDBRLPI = _USDBRLPI(*_USDBRLPI._fields)
"""
    name: .USDBRLPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDMXNPI(Symbol):
    """
        name: .USDMXNPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDMXNPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDMXNPI"

    def __str__(self):
        return ".USDMXNPI"

    def __call__(self):
        return ".USDMXNPI"


_USDMXNPI = _USDMXNPI(*_USDMXNPI._fields)
"""
    name: .USDMXNPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NZDUSDPI(Symbol):
    """
        name: .NZDUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NZDUSDPI"

    def __str__(self):
        return ".NZDUSDPI"

    def __call__(self):
        return ".NZDUSDPI"


_NZDUSDPI = _NZDUSDPI(*_NZDUSDPI._fields)
"""
    name: .NZDUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDCNHPI(Symbol):
    """
        name: .USDCNHPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCNHPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDCNHPI"

    def __str__(self):
        return ".USDCNHPI"

    def __call__(self):
        return ".USDCNHPI"


_USDCNHPI = _USDCNHPI(*_USDCNHPI._fields)
"""
    name: .USDCNHPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDSEKPI(Symbol):
    """
        name: .USDSEKPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDSEKPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDSEKPI"

    def __str__(self):
        return ".USDSEKPI"

    def __call__(self):
        return ".USDSEKPI"


_USDSEKPI = _USDSEKPI(*_USDSEKPI._fields)
"""
    name: .USDSEKPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURUSDPI8H(Symbol):
    """
        name: .EURUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURUSDPI8H"

    def __str__(self):
        return ".EURUSDPI8H"

    def __call__(self):
        return ".EURUSDPI8H"


_EURUSDPI8H = _EURUSDPI8H(*_EURUSDPI8H._fields)
"""
    name: .EURUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDCHFPI8H(Symbol):
    """
        name: .USDCHFPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCHFPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDCHFPI8H"

    def __str__(self):
        return ".USDCHFPI8H"

    def __call__(self):
        return ".USDCHFPI8H"


_USDCHFPI8H = _USDCHFPI8H(*_USDCHFPI8H._fields)
"""
    name: .USDCHFPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURCHFPI8H(Symbol):
    """
        name: .EURCHFPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURCHFPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURCHFPI8H"

    def __str__(self):
        return ".EURCHFPI8H"

    def __call__(self):
        return ".EURCHFPI8H"


_EURCHFPI8H = _EURCHFPI8H(*_EURCHFPI8H._fields)
"""
    name: .EURCHFPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURTRYPI8H(Symbol):
    """
        name: .EURTRYPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURTRYPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURTRYPI8H"

    def __str__(self):
        return ".EURTRYPI8H"

    def __call__(self):
        return ".EURTRYPI8H"


_EURTRYPI8H = _EURTRYPI8H(*_EURTRYPI8H._fields)
"""
    name: .EURTRYPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTRYPI8H(Symbol):
    """
        name: .USDTRYPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTRYPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTRYPI8H"

    def __str__(self):
        return ".USDTRYPI8H"

    def __call__(self):
        return ".USDTRYPI8H"


_USDTRYPI8H = _USDTRYPI8H(*_USDTRYPI8H._fields)
"""
    name: .USDTRYPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDINRPI8H(Symbol):
    """
        name: .USDINRPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDINRPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDINRPI8H"

    def __str__(self):
        return ".USDINRPI8H"

    def __call__(self):
        return ".USDINRPI8H"


_USDINRPI8H = _USDINRPI8H(*_USDINRPI8H._fields)
"""
    name: .USDINRPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDZARPI8H(Symbol):
    """
        name: .USDZARPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDZARPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDZARPI8H"

    def __str__(self):
        return ".USDZARPI8H"

    def __call__(self):
        return ".USDZARPI8H"


_USDZARPI8H = _USDZARPI8H(*_USDZARPI8H._fields)
"""
    name: .USDZARPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDBRLPI8H(Symbol):
    """
        name: .USDBRLPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDBRLPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDBRLPI8H"

    def __str__(self):
        return ".USDBRLPI8H"

    def __call__(self):
        return ".USDBRLPI8H"


_USDBRLPI8H = _USDBRLPI8H(*_USDBRLPI8H._fields)
"""
    name: .USDBRLPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDMXNPI8H(Symbol):
    """
        name: .USDMXNPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDMXNPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDMXNPI8H"

    def __str__(self):
        return ".USDMXNPI8H"

    def __call__(self):
        return ".USDMXNPI8H"


_USDMXNPI8H = _USDMXNPI8H(*_USDMXNPI8H._fields)
"""
    name: .USDMXNPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NZDUSDPI8H(Symbol):
    """
        name: .NZDUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NZDUSDPI8H"

    def __str__(self):
        return ".NZDUSDPI8H"

    def __call__(self):
        return ".NZDUSDPI8H"


_NZDUSDPI8H = _NZDUSDPI8H(*_NZDUSDPI8H._fields)
"""
    name: .NZDUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDCNHPI8H(Symbol):
    """
        name: .USDCNHPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCNHPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDCNHPI8H"

    def __str__(self):
        return ".USDCNHPI8H"

    def __call__(self):
        return ".USDCNHPI8H"


_USDCNHPI8H = _USDCNHPI8H(*_USDCNHPI8H._fields)
"""
    name: .USDCNHPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDSEKPI8H(Symbol):
    """
        name: .USDSEKPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDSEKPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDSEKPI8H"

    def __str__(self):
        return ".USDSEKPI8H"

    def __call__(self):
        return ".USDSEKPI8H"


_USDSEKPI8H = _USDSEKPI8H(*_USDSEKPI8H._fields)
"""
    name: .USDSEKPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURUSDTPI(Symbol):
    """
        name: .EURUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURUSDTPI"

    def __str__(self):
        return ".EURUSDTPI"

    def __call__(self):
        return ".EURUSDTPI"


_EURUSDTPI = _EURUSDTPI(*_EURUSDTPI._fields)
"""
    name: .EURUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTCHFPI(Symbol):
    """
        name: .USDTCHFPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTCHFPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTCHFPI"

    def __str__(self):
        return ".USDTCHFPI"

    def __call__(self):
        return ".USDTCHFPI"


_USDTCHFPI = _USDTCHFPI(*_USDTCHFPI._fields)
"""
    name: .USDTCHFPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTTRYPI(Symbol):
    """
        name: .USDTTRYPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTTRYPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTTRYPI"

    def __str__(self):
        return ".USDTTRYPI"

    def __call__(self):
        return ".USDTTRYPI"


_USDTTRYPI = _USDTTRYPI(*_USDTTRYPI._fields)
"""
    name: .USDTTRYPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTINRPI(Symbol):
    """
        name: .USDTINRPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTINRPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTINRPI"

    def __str__(self):
        return ".USDTINRPI"

    def __call__(self):
        return ".USDTINRPI"


_USDTINRPI = _USDTINRPI(*_USDTINRPI._fields)
"""
    name: .USDTINRPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTZARPI(Symbol):
    """
        name: .USDTZARPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTZARPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTZARPI"

    def __str__(self):
        return ".USDTZARPI"

    def __call__(self):
        return ".USDTZARPI"


_USDTZARPI = _USDTZARPI(*_USDTZARPI._fields)
"""
    name: .USDTZARPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTBRLPI(Symbol):
    """
        name: .USDTBRLPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTBRLPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTBRLPI"

    def __str__(self):
        return ".USDTBRLPI"

    def __call__(self):
        return ".USDTBRLPI"


_USDTBRLPI = _USDTBRLPI(*_USDTBRLPI._fields)
"""
    name: .USDTBRLPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTMXNPI(Symbol):
    """
        name: .USDTMXNPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTMXNPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTMXNPI"

    def __str__(self):
        return ".USDTMXNPI"

    def __call__(self):
        return ".USDTMXNPI"


_USDTMXNPI = _USDTMXNPI(*_USDTMXNPI._fields)
"""
    name: .USDTMXNPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NZDUSDTPI(Symbol):
    """
        name: .NZDUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NZDUSDTPI"

    def __str__(self):
        return ".NZDUSDTPI"

    def __call__(self):
        return ".NZDUSDTPI"


_NZDUSDTPI = _NZDUSDTPI(*_NZDUSDTPI._fields)
"""
    name: .NZDUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTCNHPI(Symbol):
    """
        name: .USDTCNHPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTCNHPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTCNHPI"

    def __str__(self):
        return ".USDTCNHPI"

    def __call__(self):
        return ".USDTCNHPI"


_USDTCNHPI = _USDTCNHPI(*_USDTCNHPI._fields)
"""
    name: .USDTCNHPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTSEKPI(Symbol):
    """
        name: .USDTSEKPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTSEKPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTSEKPI"

    def __str__(self):
        return ".USDTSEKPI"

    def __call__(self):
        return ".USDTSEKPI"


_USDTSEKPI = _USDTSEKPI(*_USDTSEKPI._fields)
"""
    name: .USDTSEKPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _EURUSDTPI8H(Symbol):
    """
        name: .EURUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".EURUSDTPI8H"

    def __str__(self):
        return ".EURUSDTPI8H"

    def __call__(self):
        return ".EURUSDTPI8H"


_EURUSDTPI8H = _EURUSDTPI8H(*_EURUSDTPI8H._fields)
"""
    name: .EURUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTCHFPI8H(Symbol):
    """
        name: .USDTCHFPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTCHFPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTCHFPI8H"

    def __str__(self):
        return ".USDTCHFPI8H"

    def __call__(self):
        return ".USDTCHFPI8H"


_USDTCHFPI8H = _USDTCHFPI8H(*_USDTCHFPI8H._fields)
"""
    name: .USDTCHFPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTTRYPI8H(Symbol):
    """
        name: .USDTTRYPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTTRYPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTTRYPI8H"

    def __str__(self):
        return ".USDTTRYPI8H"

    def __call__(self):
        return ".USDTTRYPI8H"


_USDTTRYPI8H = _USDTTRYPI8H(*_USDTTRYPI8H._fields)
"""
    name: .USDTTRYPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTINRPI8H(Symbol):
    """
        name: .USDTINRPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTINRPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTINRPI8H"

    def __str__(self):
        return ".USDTINRPI8H"

    def __call__(self):
        return ".USDTINRPI8H"


_USDTINRPI8H = _USDTINRPI8H(*_USDTINRPI8H._fields)
"""
    name: .USDTINRPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTZARPI8H(Symbol):
    """
        name: .USDTZARPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTZARPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTZARPI8H"

    def __str__(self):
        return ".USDTZARPI8H"

    def __call__(self):
        return ".USDTZARPI8H"


_USDTZARPI8H = _USDTZARPI8H(*_USDTZARPI8H._fields)
"""
    name: .USDTZARPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTBRLPI8H(Symbol):
    """
        name: .USDTBRLPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTBRLPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTBRLPI8H"

    def __str__(self):
        return ".USDTBRLPI8H"

    def __call__(self):
        return ".USDTBRLPI8H"


_USDTBRLPI8H = _USDTBRLPI8H(*_USDTBRLPI8H._fields)
"""
    name: .USDTBRLPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTMXNPI8H(Symbol):
    """
        name: .USDTMXNPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTMXNPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTMXNPI8H"

    def __str__(self):
        return ".USDTMXNPI8H"

    def __call__(self):
        return ".USDTMXNPI8H"


_USDTMXNPI8H = _USDTMXNPI8H(*_USDTMXNPI8H._fields)
"""
    name: .USDTMXNPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NZDUSDTPI8H(Symbol):
    """
        name: .NZDUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NZDUSDTPI8H"

    def __str__(self):
        return ".NZDUSDTPI8H"

    def __call__(self):
        return ".NZDUSDTPI8H"


_NZDUSDTPI8H = _NZDUSDTPI8H(*_NZDUSDTPI8H._fields)
"""
    name: .NZDUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTCNHPI8H(Symbol):
    """
        name: .USDTCNHPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTCNHPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTCNHPI8H"

    def __str__(self):
        return ".USDTCNHPI8H"

    def __call__(self):
        return ".USDTCNHPI8H"


_USDTCNHPI8H = _USDTCNHPI8H(*_USDTCNHPI8H._fields)
"""
    name: .USDTCNHPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTSEKPI8H(Symbol):
    """
        name: .USDTSEKPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTSEKPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTSEKPI8H"

    def __str__(self):
        return ".USDTSEKPI8H"

    def __call__(self):
        return ".USDTSEKPI8H"


_USDTSEKPI8H = _USDTSEKPI8H(*_USDTSEKPI8H._fields)
"""
    name: .USDTSEKPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CHFBON(Symbol):
    """
        name: .CHFBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CHFBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CHFBON"

    def __str__(self):
        return ".CHFBON"

    def __call__(self):
        return ".CHFBON"


_CHFBON = _CHFBON(*_CHFBON._fields)
"""
    name: .CHFBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _TRYBON(Symbol):
    """
        name: .TRYBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRYBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".TRYBON"

    def __str__(self):
        return ".TRYBON"

    def __call__(self):
        return ".TRYBON"


_TRYBON = _TRYBON(*_TRYBON._fields)
"""
    name: .TRYBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _INRBON(Symbol):
    """
        name: .INRBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".INRBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".INRBON"

    def __str__(self):
        return ".INRBON"

    def __call__(self):
        return ".INRBON"


_INRBON = _INRBON(*_INRBON._fields)
"""
    name: .INRBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ZARBON(Symbol):
    """
        name: .ZARBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ZARBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ZARBON"

    def __str__(self):
        return ".ZARBON"

    def __call__(self):
        return ".ZARBON"


_ZARBON = _ZARBON(*_ZARBON._fields)
"""
    name: .ZARBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BRLBON(Symbol):
    """
        name: .BRLBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BRLBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BRLBON"

    def __str__(self):
        return ".BRLBON"

    def __call__(self):
        return ".BRLBON"


_BRLBON = _BRLBON(*_BRLBON._fields)
"""
    name: .BRLBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MXNBON(Symbol):
    """
        name: .MXNBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MXNBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MXNBON"

    def __str__(self):
        return ".MXNBON"

    def __call__(self):
        return ".MXNBON"


_MXNBON = _MXNBON(*_MXNBON._fields)
"""
    name: .MXNBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NZDBON(Symbol):
    """
        name: .NZDBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NZDBON"

    def __str__(self):
        return ".NZDBON"

    def __call__(self):
        return ".NZDBON"


_NZDBON = _NZDBON(*_NZDBON._fields)
"""
    name: .NZDBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CNHBON(Symbol):
    """
        name: .CNHBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CNHBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CNHBON"

    def __str__(self):
        return ".CNHBON"

    def __call__(self):
        return ".CNHBON"


_CNHBON = _CNHBON(*_CNHBON._fields)
"""
    name: .CNHBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SEKBON(Symbol):
    """
        name: .SEKBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SEKBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SEKBON"

    def __str__(self):
        return ".SEKBON"

    def __call__(self):
        return ".SEKBON"


_SEKBON = _SEKBON(*_SEKBON._fields)
"""
    name: .SEKBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CHFBON8H(Symbol):
    """
        name: .CHFBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CHFBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CHFBON8H"

    def __str__(self):
        return ".CHFBON8H"

    def __call__(self):
        return ".CHFBON8H"


_CHFBON8H = _CHFBON8H(*_CHFBON8H._fields)
"""
    name: .CHFBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _TRYBON8H(Symbol):
    """
        name: .TRYBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRYBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".TRYBON8H"

    def __str__(self):
        return ".TRYBON8H"

    def __call__(self):
        return ".TRYBON8H"


_TRYBON8H = _TRYBON8H(*_TRYBON8H._fields)
"""
    name: .TRYBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _INRBON8H(Symbol):
    """
        name: .INRBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".INRBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".INRBON8H"

    def __str__(self):
        return ".INRBON8H"

    def __call__(self):
        return ".INRBON8H"


_INRBON8H = _INRBON8H(*_INRBON8H._fields)
"""
    name: .INRBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ZARBON8H(Symbol):
    """
        name: .ZARBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ZARBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ZARBON8H"

    def __str__(self):
        return ".ZARBON8H"

    def __call__(self):
        return ".ZARBON8H"


_ZARBON8H = _ZARBON8H(*_ZARBON8H._fields)
"""
    name: .ZARBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BRLBON8H(Symbol):
    """
        name: .BRLBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BRLBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BRLBON8H"

    def __str__(self):
        return ".BRLBON8H"

    def __call__(self):
        return ".BRLBON8H"


_BRLBON8H = _BRLBON8H(*_BRLBON8H._fields)
"""
    name: .BRLBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _MXNBON8H(Symbol):
    """
        name: .MXNBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MXNBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".MXNBON8H"

    def __str__(self):
        return ".MXNBON8H"

    def __call__(self):
        return ".MXNBON8H"


_MXNBON8H = _MXNBON8H(*_MXNBON8H._fields)
"""
    name: .MXNBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _NZDBON8H(Symbol):
    """
        name: .NZDBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".NZDBON8H"

    def __str__(self):
        return ".NZDBON8H"

    def __call__(self):
        return ".NZDBON8H"


_NZDBON8H = _NZDBON8H(*_NZDBON8H._fields)
"""
    name: .NZDBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CNHBON8H(Symbol):
    """
        name: .CNHBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CNHBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CNHBON8H"

    def __str__(self):
        return ".CNHBON8H"

    def __call__(self):
        return ".CNHBON8H"


_CNHBON8H = _CNHBON8H(*_CNHBON8H._fields)
"""
    name: .CNHBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SEKBON8H(Symbol):
    """
        name: .SEKBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SEKBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SEKBON8H"

    def __str__(self):
        return ".SEKBON8H"

    def __call__(self):
        return ".SEKBON8H"


_SEKBON8H = _SEKBON8H(*_SEKBON8H._fields)
"""
    name: .SEKBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BOP(Symbol):
    """
        name: .BOP
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOP"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BOP"

    def __str__(self):
        return ".BOP"

    def __call__(self):
        return ".BOP"


_BOP = _BOP(*_BOP._fields)
"""
    name: .BOP
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BOP_NEXT(Symbol):
    """
        name: .BOP_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOP_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BOP_NEXT"

    def __str__(self):
        return ".BOP_NEXT"

    def __call__(self):
        return ".BOP_NEXT"


_BOP_NEXT = _BOP_NEXT(*_BOP_NEXT._fields)
"""
    name: .BOP_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BOPT(Symbol):
    """
        name: .BOPT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOPT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BOPT"

    def __str__(self):
        return ".BOPT"

    def __call__(self):
        return ".BOPT"


_BOPT = _BOPT(*_BOPT._fields)
"""
    name: .BOPT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BOPT_NEXT(Symbol):
    """
        name: .BOPT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOPT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BOPT_NEXT"

    def __str__(self):
        return ".BOPT_NEXT"

    def __call__(self):
        return ".BOPT_NEXT"


_BOPT_NEXT = _BOPT_NEXT(*_BOPT_NEXT._fields)
"""
    name: .BOPT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _OPBON(Symbol):
    """
        name: .OPBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".OPBON"

    def __str__(self):
        return ".OPBON"

    def __call__(self):
        return ".OPBON"


_OPBON = _OPBON(*_OPBON._fields)
"""
    name: .OPBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _OPBON8H(Symbol):
    """
        name: .OPBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".OPBON8H"

    def __str__(self):
        return ".OPBON8H"

    def __call__(self):
        return ".OPBON8H"


_OPBON8H = _OPBON8H(*_OPBON8H._fields)
"""
    name: .OPBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _OPUSDTPI(Symbol):
    """
        name: .OPUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".OPUSDTPI"

    def __str__(self):
        return ".OPUSDTPI"

    def __call__(self):
        return ".OPUSDTPI"


_OPUSDTPI = _OPUSDTPI(*_OPUSDTPI._fields)
"""
    name: .OPUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _OPUSDTPI8H(Symbol):
    """
        name: .OPUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".OPUSDTPI8H"

    def __str__(self):
        return ".OPUSDTPI8H"

    def __call__(self):
        return ".OPUSDTPI8H"


_OPUSDTPI8H = _OPUSDTPI8H(*_OPUSDTPI8H._fields)
"""
    name: .OPUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _OPUSDPI(Symbol):
    """
        name: .OPUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".OPUSDPI"

    def __str__(self):
        return ".OPUSDPI"

    def __call__(self):
        return ".OPUSDPI"


_OPUSDPI = _OPUSDPI(*_OPUSDPI._fields)
"""
    name: .OPUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _OPUSDPI8H(Symbol):
    """
        name: .OPUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".OPUSDPI8H"

    def __str__(self):
        return ".OPUSDPI8H"

    def __call__(self):
        return ".OPUSDPI8H"


_OPUSDPI8H = _OPUSDPI8H(*_OPUSDPI8H._fields)
"""
    name: .OPUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUSDC(Symbol):
    """
        name: .BUSDC
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDC"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDC"

    def __str__(self):
        return ".BUSDC"

    def __call__(self):
        return ".BUSDC"


_BUSDC = _BUSDC(*_BUSDC._fields)
"""
    name: .BUSDC
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUSDCT(Symbol):
    """
        name: .BUSDCT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDCT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDCT"

    def __str__(self):
        return ".BUSDCT"

    def __call__(self):
        return ".BUSDCT"


_BUSDCT = _BUSDCT(*_BUSDCT._fields)
"""
    name: .BUSDCT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHPOWT(Symbol):
    """
        name: .BETHPOWT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHPOWT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHPOWT"

    def __str__(self):
        return ".BETHPOWT"

    def __call__(self):
        return ".BETHPOWT"


_BETHPOWT = _BETHPOWT(*_BETHPOWT._fields)
"""
    name: .BETHPOWT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHPOWT_NEXT(Symbol):
    """
        name: .BETHPOWT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHPOWT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHPOWT_NEXT"

    def __str__(self):
        return ".BETHPOWT_NEXT"

    def __call__(self):
        return ".BETHPOWT_NEXT"


_BETHPOWT_NEXT = _BETHPOWT_NEXT(*_BETHPOWT_NEXT._fields)
"""
    name: .BETHPOWT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHPOWT30M(Symbol):
    """
        name: .BETHPOWT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHPOWT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHPOWT30M"

    def __str__(self):
        return ".BETHPOWT30M"

    def __call__(self):
        return ".BETHPOWT30M"


_BETHPOWT30M = _BETHPOWT30M(*_BETHPOWT30M._fields)
"""
    name: .BETHPOWT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BALTMEXT30M(Symbol):
    """
        name: .BALTMEXT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BALTMEXT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BALTMEXT30M"

    def __str__(self):
        return ".BALTMEXT30M"

    def __call__(self):
        return ".BALTMEXT30M"


_BALTMEXT30M = _BALTMEXT30M(*_BALTMEXT30M._fields)
"""
    name: .BALTMEXT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDEFIMEXT30M(Symbol):
    """
        name: .BDEFIMEXT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDEFIMEXT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDEFIMEXT30M"

    def __str__(self):
        return ".BDEFIMEXT30M"

    def __call__(self):
        return ".BDEFIMEXT30M"


_BDEFIMEXT30M = _BDEFIMEXT30M(*_BDEFIMEXT30M._fields)
"""
    name: .BDEFIMEXT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMETAMEXT30M(Symbol):
    """
        name: .BMETAMEXT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMETAMEXT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMETAMEXT30M"

    def __str__(self):
        return ".BMETAMEXT30M"

    def __call__(self):
        return ".BMETAMEXT30M"


_BMETAMEXT30M = _BMETAMEXT30M(*_BMETAMEXT30M._fields)
"""
    name: .BMETAMEXT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUSDC_NEXT(Symbol):
    """
        name: .BUSDC_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDC_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDC_NEXT"

    def __str__(self):
        return ".BUSDC_NEXT"

    def __call__(self):
        return ".BUSDC_NEXT"


_BUSDC_NEXT = _BUSDC_NEXT(*_BUSDC_NEXT._fields)
"""
    name: .BUSDC_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUSDCT_NEXT(Symbol):
    """
        name: .BUSDCT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDCT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDCT_NEXT"

    def __str__(self):
        return ".BUSDCT_NEXT"

    def __call__(self):
        return ".BUSDCT_NEXT"


_BUSDCT_NEXT = _BUSDCT_NEXT(*_BUSDCT_NEXT._fields)
"""
    name: .BUSDCT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BKLAY(Symbol):
    """
        name: .BKLAY
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BKLAY"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BKLAY"

    def __str__(self):
        return ".BKLAY"

    def __call__(self):
        return ".BKLAY"


_BKLAY = _BKLAY(*_BKLAY._fields)
"""
    name: .BKLAY
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BKLAY_NEXT(Symbol):
    """
        name: .BKLAY_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BKLAY_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BKLAY_NEXT"

    def __str__(self):
        return ".BKLAY_NEXT"

    def __call__(self):
        return ".BKLAY_NEXT"


_BKLAY_NEXT = _BKLAY_NEXT(*_BKLAY_NEXT._fields)
"""
    name: .BKLAY_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BKLAYT(Symbol):
    """
        name: .BKLAYT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BKLAYT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BKLAYT"

    def __str__(self):
        return ".BKLAYT"

    def __call__(self):
        return ".BKLAYT"


_BKLAYT = _BKLAYT(*_BKLAYT._fields)
"""
    name: .BKLAYT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BKLAYT_NEXT(Symbol):
    """
        name: .BKLAYT_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BKLAYT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BKLAYT_NEXT"

    def __str__(self):
        return ".BKLAYT_NEXT"

    def __call__(self):
        return ".BKLAYT_NEXT"


_BKLAYT_NEXT = _BKLAYT_NEXT(*_BKLAYT_NEXT._fields)
"""
    name: .BKLAYT_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _KLAYUSDTPI(Symbol):
    """
        name: .KLAYUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".KLAYUSDTPI"

    def __str__(self):
        return ".KLAYUSDTPI"

    def __call__(self):
        return ".KLAYUSDTPI"


_KLAYUSDTPI = _KLAYUSDTPI(*_KLAYUSDTPI._fields)
"""
    name: .KLAYUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _KLAYUSDTPI8H(Symbol):
    """
        name: .KLAYUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".KLAYUSDTPI8H"

    def __str__(self):
        return ".KLAYUSDTPI8H"

    def __call__(self):
        return ".KLAYUSDTPI8H"


_KLAYUSDTPI8H = _KLAYUSDTPI8H(*_KLAYUSDTPI8H._fields)
"""
    name: .KLAYUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _KLAYUSDPI(Symbol):
    """
        name: .KLAYUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".KLAYUSDPI"

    def __str__(self):
        return ".KLAYUSDPI"

    def __call__(self):
        return ".KLAYUSDPI"


_KLAYUSDPI = _KLAYUSDPI(*_KLAYUSDPI._fields)
"""
    name: .KLAYUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _KLAYUSDPI8H(Symbol):
    """
        name: .KLAYUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".KLAYUSDPI8H"

    def __str__(self):
        return ".KLAYUSDPI8H"

    def __call__(self):
        return ".KLAYUSDPI8H"


_KLAYUSDPI8H = _KLAYUSDPI8H(*_KLAYUSDPI8H._fields)
"""
    name: .KLAYUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _KLAYBON(Symbol):
    """
        name: .KLAYBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".KLAYBON"

    def __str__(self):
        return ".KLAYBON"

    def __call__(self):
        return ".KLAYBON"


_KLAYBON = _KLAYBON(*_KLAYBON._fields)
"""
    name: .KLAYBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _KLAYBON8H(Symbol):
    """
        name: .KLAYBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".KLAYBON8H"

    def __str__(self):
        return ".KLAYBON8H"

    def __call__(self):
        return ".KLAYBON8H"


_KLAYBON8H = _KLAYBON8H(*_KLAYBON8H._fields)
"""
    name: .KLAYBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSTETH(Symbol):
    """
        name: .BSTETH
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSTETH"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSTETH"

    def __str__(self):
        return ".BSTETH"

    def __call__(self):
        return ".BSTETH"


_BSTETH = _BSTETH(*_BSTETH._fields)
"""
    name: .BSTETH
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSTETHT(Symbol):
    """
        name: .BSTETHT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSTETHT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSTETHT"

    def __str__(self):
        return ".BSTETHT"

    def __call__(self):
        return ".BSTETHT"


_BSTETHT = _BSTETHT(*_BSTETHT._fields)
"""
    name: .BSTETHT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDAI(Symbol):
    """
        name: .BDAI
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDAI"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDAI"

    def __str__(self):
        return ".BDAI"

    def __call__(self):
        return ".BDAI"


_BDAI = _BDAI(*_BDAI._fields)
"""
    name: .BDAI
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BDAIT(Symbol):
    """
        name: .BDAIT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDAIT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BDAIT"

    def __str__(self):
        return ".BDAIT"

    def __call__(self):
        return ".BDAIT"


_BDAIT = _BDAIT(*_BDAIT._fields)
"""
    name: .BDAIT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBUSD(Symbol):
    """
        name: .BBUSD
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBUSD"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBUSD"

    def __str__(self):
        return ".BBUSD"

    def __call__(self):
        return ".BBUSD"


_BBUSD = _BBUSD(*_BBUSD._fields)
"""
    name: .BBUSD
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBUSDT(Symbol):
    """
        name: .BBUSDT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBUSDT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBUSDT"

    def __str__(self):
        return ".BBUSDT"

    def __call__(self):
        return ".BBUSDT"


_BBUSDT = _BBUSDT(*_BBUSDT._fields)
"""
    name: .BBUSDT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BWBTC(Symbol):
    """
        name: .BWBTC
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BWBTC"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BWBTC"

    def __str__(self):
        return ".BWBTC"

    def __call__(self):
        return ".BWBTC"


_BWBTC = _BWBTC(*_BWBTC._fields)
"""
    name: .BWBTC
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BWBTCT(Symbol):
    """
        name: .BWBTCT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BWBTCT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BWBTCT"

    def __str__(self):
        return ".BWBTCT"

    def __call__(self):
        return ".BWBTCT"


_BWBTCT = _BWBTCT(*_BWBTCT._fields)
"""
    name: .BWBTCT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCRO(Symbol):
    """
        name: .BCRO
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCRO"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCRO"

    def __str__(self):
        return ".BCRO"

    def __call__(self):
        return ".BCRO"


_BCRO = _BCRO(*_BCRO._fields)
"""
    name: .BCRO
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCROT(Symbol):
    """
        name: .BCROT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCROT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCROT"

    def __str__(self):
        return ".BCROT"

    def __call__(self):
        return ".BCROT"


_BCROT = _BCROT(*_BCROT._fields)
"""
    name: .BCROT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BQNT(Symbol):
    """
        name: .BQNT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BQNT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BQNT"

    def __str__(self):
        return ".BQNT"

    def __call__(self):
        return ".BQNT"


_BQNT = _BQNT(*_BQNT._fields)
"""
    name: .BQNT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BQNTT(Symbol):
    """
        name: .BQNTT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BQNTT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BQNTT"

    def __str__(self):
        return ".BQNTT"

    def __call__(self):
        return ".BQNTT"


_BQNTT = _BQNTT(*_BQNTT._fields)
"""
    name: .BQNTT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BOKB(Symbol):
    """
        name: .BOKB
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOKB"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BOKB"

    def __str__(self):
        return ".BOKB"

    def __call__(self):
        return ".BOKB"


_BOKB = _BOKB(*_BOKB._fields)
"""
    name: .BOKB
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BOKBT(Symbol):
    """
        name: .BOKBT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOKBT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BOKBT"

    def __str__(self):
        return ".BOKBT"

    def __call__(self):
        return ".BOKBT"


_BOKBT = _BOKBT(*_BOKBT._fields)
"""
    name: .BOKBT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLEO(Symbol):
    """
        name: .BLEO
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLEO"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLEO"

    def __str__(self):
        return ".BLEO"

    def __call__(self):
        return ".BLEO"


_BLEO = _BLEO(*_BLEO._fields)
"""
    name: .BLEO
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLEOT(Symbol):
    """
        name: .BLEOT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLEOT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLEOT"

    def __str__(self):
        return ".BLEOT"

    def __call__(self):
        return ".BLEOT"


_BLEOT = _BLEOT(*_BLEOT._fields)
"""
    name: .BLEOT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAAVE(Symbol):
    """
        name: .BAAVE
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAAVE"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAAVE"

    def __str__(self):
        return ".BAAVE"

    def __call__(self):
        return ".BAAVE"


_BAAVE = _BAAVE(*_BAAVE._fields)
"""
    name: .BAAVE
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMANA(Symbol):
    """
        name: .BMANA
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMANA"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMANA"

    def __str__(self):
        return ".BMANA"

    def __call__(self):
        return ".BMANA"


_BMANA = _BMANA(*_BMANA._fields)
"""
    name: .BMANA
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXLM(Symbol):
    """
        name: .BXLM
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXLM"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXLM"

    def __str__(self):
        return ".BXLM"

    def __call__(self):
        return ".BXLM"


_BXLM = _BXLM(*_BXLM._fields)
"""
    name: .BXLM
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BVET(Symbol):
    """
        name: .BVET
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVET"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BVET"

    def __str__(self):
        return ".BVET"

    def __call__(self):
        return ".BVET"


_BVET = _BVET(*_BVET._fields)
"""
    name: .BVET
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFIL(Symbol):
    """
        name: .BFIL
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFIL"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFIL"

    def __str__(self):
        return ".BFIL"

    def __call__(self):
        return ".BFIL"


_BFIL = _BFIL(*_BFIL._fields)
"""
    name: .BFIL
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXTZ(Symbol):
    """
        name: .BXTZ
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXTZ"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXTZ"

    def __str__(self):
        return ".BXTZ"

    def __call__(self):
        return ".BXTZ"


_BXTZ = _BXTZ(*_BXTZ._fields)
"""
    name: .BXTZ
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMKR(Symbol):
    """
        name: .BMKR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMKR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMKR"

    def __str__(self):
        return ".BMKR"

    def __call__(self):
        return ".BMKR"


_BMKR = _BMKR(*_BMKR._fields)
"""
    name: .BMKR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFLOW(Symbol):
    """
        name: .BFLOW
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLOW"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFLOW"

    def __str__(self):
        return ".BFLOW"

    def __call__(self):
        return ".BFLOW"


_BFLOW = _BFLOW(*_BFLOW._fields)
"""
    name: .BFLOW
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFLOWT(Symbol):
    """
        name: .BFLOWT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLOWT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFLOWT"

    def __str__(self):
        return ".BFLOWT"

    def __call__(self):
        return ".BFLOWT"


_BFLOWT = _BFLOWT(*_BFLOWT._fields)
"""
    name: .BFLOWT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BHBAR(Symbol):
    """
        name: .BHBAR
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BHBAR"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BHBAR"

    def __str__(self):
        return ".BHBAR"

    def __call__(self):
        return ".BHBAR"


_BHBAR = _BHBAR(*_BHBAR._fields)
"""
    name: .BHBAR
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BHBART(Symbol):
    """
        name: .BHBART
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BHBART"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BHBART"

    def __str__(self):
        return ".BHBART"

    def __call__(self):
        return ".BHBART"


_BHBART = _BHBART(*_BHBART._fields)
"""
    name: .BHBART
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEGLD(Symbol):
    """
        name: .BEGLD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEGLD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEGLD"

    def __str__(self):
        return ".BEGLD"

    def __call__(self):
        return ".BEGLD"


_BEGLD = _BEGLD(*_BEGLD._fields)
"""
    name: .BEGLD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BEGLDT(Symbol):
    """
        name: .BEGLDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEGLDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEGLDT"

    def __str__(self):
        return ".BEGLDT"

    def __call__(self):
        return ".BEGLDT"


_BEGLDT = _BEGLDT(*_BEGLDT._fields)
"""
    name: .BEGLDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTUSD(Symbol):
    """
        name: .BTUSD
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTUSD"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTUSD"

    def __str__(self):
        return ".BTUSD"

    def __call__(self):
        return ".BTUSD"


_BTUSD = _BTUSD(*_BTUSD._fields)
"""
    name: .BTUSD
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTUSDT(Symbol):
    """
        name: .BTUSDT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTUSDT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTUSDT"

    def __str__(self):
        return ".BTUSDT"

    def __call__(self):
        return ".BTUSDT"


_BTUSDT = _BTUSDT(*_BTUSDT._fields)
"""
    name: .BTUSDT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUSDP(Symbol):
    """
        name: .BUSDP
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDP"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDP"

    def __str__(self):
        return ".BUSDP"

    def __call__(self):
        return ".BUSDP"


_BUSDP = _BUSDP(*_BUSDP._fields)
"""
    name: .BUSDP
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BHNT(Symbol):
    """
        name: .BHNT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BHNT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BHNT"

    def __str__(self):
        return ".BHNT"

    def __call__(self):
        return ".BHNT"


_BHNT = _BHNT(*_BHNT._fields)
"""
    name: .BHNT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BHNTT(Symbol):
    """
        name: .BHNTT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BHNTT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BHNTT"

    def __str__(self):
        return ".BHNTT"

    def __call__(self):
        return ".BHNTT"


_BHNTT = _BHNTT(*_BHNTT._fields)
"""
    name: .BHNTT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BIOTA(Symbol):
    """
        name: .BIOTA
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BIOTA"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BIOTA"

    def __str__(self):
        return ".BIOTA"

    def __call__(self):
        return ".BIOTA"


_BIOTA = _BIOTA(*_BIOTA._fields)
"""
    name: .BIOTA
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BIOTAT(Symbol):
    """
        name: .BIOTAT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BIOTAT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BIOTAT"

    def __str__(self):
        return ".BIOTAT"

    def __call__(self):
        return ".BIOTAT"


_BIOTAT = _BIOTAT(*_BIOTAT._fields)
"""
    name: .BIOTAT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXEC(Symbol):
    """
        name: .BXEC
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXEC"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXEC"

    def __str__(self):
        return ".BXEC"

    def __call__(self):
        return ".BXEC"


_BXEC = _BXEC(*_BXEC._fields)
"""
    name: .BXEC
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXECT(Symbol):
    """
        name: .BXECT
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXECT"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXECT"

    def __str__(self):
        return ".BXECT"

    def __call__(self):
        return ".BXECT"


_BXECT = _BXECT(*_BXECT._fields)
"""
    name: .BXECT
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFTTT(Symbol):
    """
        name: .BFTTT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTTT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFTTT"

    def __str__(self):
        return ".BFTTT"

    def __call__(self):
        return ".BFTTT"


_BFTTT = _BFTTT(*_BFTTT._fields)
"""
    name: .BFTTT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSANDT30M(Symbol):
    """
        name: .BSANDT30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSANDT30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSANDT30M"

    def __str__(self):
        return ".BSANDT30M"

    def __call__(self):
        return ".BSANDT30M"


_BSANDT30M = _BSANDT30M(*_BSANDT30M._fields)
"""
    name: .BSANDT30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BNEART30M(Symbol):
    """
        name: .BNEART30M
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEART30M"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNEART30M"

    def __str__(self):
        return ".BNEART30M"

    def __call__(self):
        return ".BNEART30M"


_BNEART30M = _BNEART30M(*_BNEART30M._fields)
"""
    name: .BNEART30M
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMANAT30M(Symbol):
    """
        name: .BMANAT30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMANAT30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMANAT30M"

    def __str__(self):
        return ".BMANAT30M"

    def __call__(self):
        return ".BMANAT30M"


_BMANAT30M = _BMANAT30M(*_BMANAT30M._fields)
"""
    name: .BMANAT30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSHIBT30M(Symbol):
    """
        name: .BSHIBT30M
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSHIBT30M"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSHIBT30M"

    def __str__(self):
        return ".BSHIBT30M"

    def __call__(self):
        return ".BSHIBT30M"


_BSHIBT30M = _BSHIBT30M(*_BSHIBT30M._fields)
"""
    name: .BSHIBT30M
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BOPT30M(Symbol):
    """
        name: .BOPT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOPT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BOPT30M"

    def __str__(self):
        return ".BOPT30M"

    def __call__(self):
        return ".BOPT30M"


_BOPT30M = _BOPT30M(*_BOPT30M._fields)
"""
    name: .BOPT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGALT30M(Symbol):
    """
        name: .BGALT30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGALT30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGALT30M"

    def __str__(self):
        return ".BGALT30M"

    def __call__(self):
        return ".BGALT30M"


_BGALT30M = _BGALT30M(*_BGALT30M._fields)
"""
    name: .BGALT30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGAL30M(Symbol):
    """
        name: .BGAL30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGAL30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGAL30M"

    def __str__(self):
        return ".BGAL30M"

    def __call__(self):
        return ".BGAL30M"


_BGAL30M = _BGAL30M(*_BGAL30M._fields)
"""
    name: .BGAL30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BTRX30M(Symbol):
    """
        name: .BTRX30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRX30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BTRX30M"

    def __str__(self):
        return ".BTRX30M"

    def __call__(self):
        return ".BTRX30M"


_BTRX30M = _BTRX30M(*_BTRX30M._fields)
"""
    name: .BTRX30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BOP30M(Symbol):
    """
        name: .BOP30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOP30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BOP30M"

    def __str__(self):
        return ".BOP30M"

    def __call__(self):
        return ".BOP30M"


_BOP30M = _BOP30M(*_BOP30M._fields)
"""
    name: .BOP30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPE30M(Symbol):
    """
        name: .BAPE30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPE30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPE30M"

    def __str__(self):
        return ".BAPE30M"

    def __call__(self):
        return ".BAPE30M"


_BAPE30M = _BAPE30M(*_BAPE30M._fields)
"""
    name: .BAPE30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFTMT30M(Symbol):
    """
        name: .BFTMT30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTMT30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFTMT30M"

    def __str__(self):
        return ".BFTMT30M"

    def __call__(self):
        return ".BFTMT30M"


_BFTMT30M = _BFTMT30M(*_BFTMT30M._fields)
"""
    name: .BFTMT30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPT(Symbol):
    """
        name: .BAPT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPT"

    def __str__(self):
        return ".BAPT"

    def __call__(self):
        return ".BAPT"


_BAPT = _BAPT(*_BAPT._fields)
"""
    name: .BAPT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPT_NEXT(Symbol):
    """
        name: .BAPT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPT_NEXT"

    def __str__(self):
        return ".BAPT_NEXT"

    def __call__(self):
        return ".BAPT_NEXT"


_BAPT_NEXT = _BAPT_NEXT(*_BAPT_NEXT._fields)
"""
    name: .BAPT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPT30M(Symbol):
    """
        name: .BAPT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPT30M"

    def __str__(self):
        return ".BAPT30M"

    def __call__(self):
        return ".BAPT30M"


_BAPT30M = _BAPT30M(*_BAPT30M._fields)
"""
    name: .BAPT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPTT(Symbol):
    """
        name: .BAPTT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPTT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPTT"

    def __str__(self):
        return ".BAPTT"

    def __call__(self):
        return ".BAPTT"


_BAPTT = _BAPTT(*_BAPTT._fields)
"""
    name: .BAPTT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPTT_NEXT(Symbol):
    """
        name: .BAPTT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPTT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPTT_NEXT"

    def __str__(self):
        return ".BAPTT_NEXT"

    def __call__(self):
        return ".BAPTT_NEXT"


_BAPTT_NEXT = _BAPTT_NEXT(*_BAPTT_NEXT._fields)
"""
    name: .BAPTT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BAPTT30M(Symbol):
    """
        name: .BAPTT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPTT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BAPTT30M"

    def __str__(self):
        return ".BAPTT30M"

    def __call__(self):
        return ".BAPTT30M"


_BAPTT30M = _BAPTT30M(*_BAPTT30M._fields)
"""
    name: .BAPTT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APTBON(Symbol):
    """
        name: .APTBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APTBON"

    def __str__(self):
        return ".APTBON"

    def __call__(self):
        return ".APTBON"


_APTBON = _APTBON(*_APTBON._fields)
"""
    name: .APTBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APTBON8H(Symbol):
    """
        name: .APTBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APTBON8H"

    def __str__(self):
        return ".APTBON8H"

    def __call__(self):
        return ".APTBON8H"


_APTBON8H = _APTBON8H(*_APTBON8H._fields)
"""
    name: .APTBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APTUSDTPI(Symbol):
    """
        name: .APTUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APTUSDTPI"

    def __str__(self):
        return ".APTUSDTPI"

    def __call__(self):
        return ".APTUSDTPI"


_APTUSDTPI = _APTUSDTPI(*_APTUSDTPI._fields)
"""
    name: .APTUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APTUSDTPI8H(Symbol):
    """
        name: .APTUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APTUSDTPI8H"

    def __str__(self):
        return ".APTUSDTPI8H"

    def __call__(self):
        return ".APTUSDTPI8H"


_APTUSDTPI8H = _APTUSDTPI8H(*_APTUSDTPI8H._fields)
"""
    name: .APTUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APTUSDPI(Symbol):
    """
        name: .APTUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APTUSDPI"

    def __str__(self):
        return ".APTUSDPI"

    def __call__(self):
        return ".APTUSDPI"


_APTUSDPI = _APTUSDPI(*_APTUSDPI._fields)
"""
    name: .APTUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _APTUSDPI8H(Symbol):
    """
        name: .APTUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".APTUSDPI8H"

    def __str__(self):
        return ".APTUSDPI8H"

    def __call__(self):
        return ".APTUSDPI8H"


_APTUSDPI8H = _APTUSDPI8H(*_APTUSDPI8H._fields)
"""
    name: .APTUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFTT(Symbol):
    """
        name: .BFTT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFTT"

    def __str__(self):
        return ".BFTT"

    def __call__(self):
        return ".BFTT"


_BFTT = _BFTT(*_BFTT._fields)
"""
    name: .BFTT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFTT_NEXT(Symbol):
    """
        name: .BFTT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFTT_NEXT"

    def __str__(self):
        return ".BFTT_NEXT"

    def __call__(self):
        return ".BFTT_NEXT"


_BFTT_NEXT = _BFTT_NEXT(*_BFTT_NEXT._fields)
"""
    name: .BFTT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFTTT_NEXT(Symbol):
    """
        name: .BFTTT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTTT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFTTT_NEXT"

    def __str__(self):
        return ".BFTTT_NEXT"

    def __call__(self):
        return ".BFTTT_NEXT"


_BFTTT_NEXT = _BFTTT_NEXT(*_BFTTT_NEXT._fields)
"""
    name: .BFTTT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTTBON(Symbol):
    """
        name: .FTTBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTTBON"

    def __str__(self):
        return ".FTTBON"

    def __call__(self):
        return ".FTTBON"


_FTTBON = _FTTBON(*_FTTBON._fields)
"""
    name: .FTTBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTTBON8H(Symbol):
    """
        name: .FTTBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTTBON8H"

    def __str__(self):
        return ".FTTBON8H"

    def __call__(self):
        return ".FTTBON8H"


_FTTBON8H = _FTTBON8H(*_FTTBON8H._fields)
"""
    name: .FTTBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTTUSDTPI(Symbol):
    """
        name: .FTTUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTTUSDTPI"

    def __str__(self):
        return ".FTTUSDTPI"

    def __call__(self):
        return ".FTTUSDTPI"


_FTTUSDTPI = _FTTUSDTPI(*_FTTUSDTPI._fields)
"""
    name: .FTTUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTTUSDTPI8H(Symbol):
    """
        name: .FTTUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTTUSDTPI8H"

    def __str__(self):
        return ".FTTUSDTPI8H"

    def __call__(self):
        return ".FTTUSDTPI8H"


_FTTUSDTPI8H = _FTTUSDTPI8H(*_FTTUSDTPI8H._fields)
"""
    name: .FTTUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTTUSDPI(Symbol):
    """
        name: .FTTUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTTUSDPI"

    def __str__(self):
        return ".FTTUSDPI"

    def __call__(self):
        return ".FTTUSDPI"


_FTTUSDPI = _FTTUSDPI(*_FTTUSDPI._fields)
"""
    name: .FTTUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FTTUSDPI8H(Symbol):
    """
        name: .FTTUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FTTUSDPI8H"

    def __str__(self):
        return ".FTTUSDPI8H"

    def __call__(self):
        return ".FTTUSDPI8H"


_FTTUSDPI8H = _FTTUSDPI8H(*_FTTUSDPI8H._fields)
"""
    name: .FTTUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMEXBON(Symbol):
    """
        name: .BMEXBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMEXBON"

    def __str__(self):
        return ".BMEXBON"

    def __call__(self):
        return ".BMEXBON"


_BMEXBON = _BMEXBON(*_BMEXBON._fields)
"""
    name: .BMEXBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMEXBON8H(Symbol):
    """
        name: .BMEXBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMEXBON8H"

    def __str__(self):
        return ".BMEXBON8H"

    def __call__(self):
        return ".BMEXBON8H"


_BMEXBON8H = _BMEXBON8H(*_BMEXBON8H._fields)
"""
    name: .BMEXBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMEXUSDTPI(Symbol):
    """
        name: .BMEXUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMEXUSDTPI"

    def __str__(self):
        return ".BMEXUSDTPI"

    def __call__(self):
        return ".BMEXUSDTPI"


_BMEXUSDTPI = _BMEXUSDTPI(*_BMEXUSDTPI._fields)
"""
    name: .BMEXUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMEXUSDTPI8H(Symbol):
    """
        name: .BMEXUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMEXUSDTPI8H"

    def __str__(self):
        return ".BMEXUSDTPI8H"

    def __call__(self):
        return ".BMEXUSDTPI8H"


_BMEXUSDTPI8H = _BMEXUSDTPI8H(*_BMEXUSDTPI8H._fields)
"""
    name: .BMEXUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMEXUSDPI(Symbol):
    """
        name: .BMEXUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMEXUSDPI"

    def __str__(self):
        return ".BMEXUSDPI"

    def __call__(self):
        return ".BMEXUSDPI"


_BMEXUSDPI = _BMEXUSDPI(*_BMEXUSDPI._fields)
"""
    name: .BMEXUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BMEXUSDPI8H(Symbol):
    """
        name: .BMEXUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BMEXUSDPI8H"

    def __str__(self):
        return ".BMEXUSDPI8H"

    def __call__(self):
        return ".BMEXUSDPI8H"


_BMEXUSDPI8H = _BMEXUSDPI8H(*_BMEXUSDPI8H._fields)
"""
    name: .BMEXUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBMEXT(Symbol):
    """
        name: .BBMEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBMEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBMEXT"

    def __str__(self):
        return ".BBMEXT"

    def __call__(self):
        return ".BBMEXT"


_BBMEXT = _BBMEXT(*_BBMEXT._fields)
"""
    name: .BBMEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBMEXT_NEXT(Symbol):
    """
        name: .BBMEXT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBMEXT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBMEXT_NEXT"

    def __str__(self):
        return ".BBMEXT_NEXT"

    def __call__(self):
        return ".BBMEXT_NEXT"


_BBMEXT_NEXT = _BBMEXT_NEXT(*_BBMEXT_NEXT._fields)
"""
    name: .BBMEXT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBMEX(Symbol):
    """
        name: .BBMEX
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBMEX"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBMEX"

    def __str__(self):
        return ".BBMEX"

    def __call__(self):
        return ".BBMEX"


_BBMEX = _BBMEX(*_BBMEX._fields)
"""
    name: .BBMEX
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBMEX_NEXT(Symbol):
    """
        name: .BBMEX_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBMEX_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBMEX_NEXT"

    def __str__(self):
        return ".BBMEX_NEXT"

    def __call__(self):
        return ".BBMEX_NEXT"


_BBMEX_NEXT = _BBMEX_NEXT(*_BBMEX_NEXT._fields)
"""
    name: .BBMEX_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CROBON(Symbol):
    """
        name: .CROBON
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROBON"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CROBON"

    def __str__(self):
        return ".CROBON"

    def __call__(self):
        return ".CROBON"


_CROBON = _CROBON(*_CROBON._fields)
"""
    name: .CROBON
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CROBON8H(Symbol):
    """
        name: .CROBON8H
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROBON8H"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CROBON8H"

    def __str__(self):
        return ".CROBON8H"

    def __call__(self):
        return ".CROBON8H"


_CROBON8H = _CROBON8H(*_CROBON8H._fields)
"""
    name: .CROBON8H
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CROUSDTPI(Symbol):
    """
        name: .CROUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CROUSDTPI"

    def __str__(self):
        return ".CROUSDTPI"

    def __call__(self):
        return ".CROUSDTPI"


_CROUSDTPI = _CROUSDTPI(*_CROUSDTPI._fields)
"""
    name: .CROUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CROUSDTPI8H(Symbol):
    """
        name: .CROUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CROUSDTPI8H"

    def __str__(self):
        return ".CROUSDTPI8H"

    def __call__(self):
        return ".CROUSDTPI8H"


_CROUSDTPI8H = _CROUSDTPI8H(*_CROUSDTPI8H._fields)
"""
    name: .CROUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CROUSDPI(Symbol):
    """
        name: .CROUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CROUSDPI"

    def __str__(self):
        return ".CROUSDPI"

    def __call__(self):
        return ".CROUSDPI"


_CROUSDPI = _CROUSDPI(*_CROUSDPI._fields)
"""
    name: .CROUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _CROUSDPI8H(Symbol):
    """
        name: .CROUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".CROUSDPI8H"

    def __str__(self):
        return ".CROUSDPI8H"

    def __call__(self):
        return ".CROUSDPI8H"


_CROUSDPI8H = _CROUSDPI8H(*_CROUSDPI8H._fields)
"""
    name: .CROUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFTT30M(Symbol):
    """
        name: .BFTT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFTT30M"

    def __str__(self):
        return ".BFTT30M"

    def __call__(self):
        return ".BFTT30M"


_BFTT30M = _BFTT30M(*_BFTT30M._fields)
"""
    name: .BFTT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFTTT30M(Symbol):
    """
        name: .BFTTT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTTT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFTTT30M"

    def __str__(self):
        return ".BFTTT30M"

    def __call__(self):
        return ".BFTTT30M"


_BFTTT30M = _BFTTT30M(*_BFTTT30M._fields)
"""
    name: .BFTTT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHYLD(Symbol):
    """
        name: .BETHYLD
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHYLD"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHYLD"

    def __str__(self):
        return ".BETHYLD"

    def __call__(self):
        return ".BETHYLD"


_BETHYLD = _BETHYLD(*_BETHYLD._fields)
"""
    name: .BETHYLD
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFLRT(Symbol):
    """
        name: .BFLRT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLRT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFLRT"

    def __str__(self):
        return ".BFLRT"

    def __call__(self):
        return ".BFLRT"


_BFLRT = _BFLRT(*_BFLRT._fields)
"""
    name: .BFLRT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFLRT_NEXT(Symbol):
    """
        name: .BFLRT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLRT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFLRT_NEXT"

    def __str__(self):
        return ".BFLRT_NEXT"

    def __call__(self):
        return ".BFLRT_NEXT"


_BFLRT_NEXT = _BFLRT_NEXT(*_BFLRT_NEXT._fields)
"""
    name: .BFLRT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFLRT30M(Symbol):
    """
        name: .BFLRT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLRT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFLRT30M"

    def __str__(self):
        return ".BFLRT30M"

    def __call__(self):
        return ".BFLRT30M"


_BFLRT30M = _BFLRT30M(*_BFLRT30M._fields)
"""
    name: .BFLRT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FLRBON(Symbol):
    """
        name: .FLRBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FLRBON"

    def __str__(self):
        return ".FLRBON"

    def __call__(self):
        return ".FLRBON"


_FLRBON = _FLRBON(*_FLRBON._fields)
"""
    name: .FLRBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FLRBON8H(Symbol):
    """
        name: .FLRBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FLRBON8H"

    def __str__(self):
        return ".FLRBON8H"

    def __call__(self):
        return ".FLRBON8H"


_FLRBON8H = _FLRBON8H(*_FLRBON8H._fields)
"""
    name: .FLRBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FLRUSDTPI(Symbol):
    """
        name: .FLRUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FLRUSDTPI"

    def __str__(self):
        return ".FLRUSDTPI"

    def __call__(self):
        return ".FLRUSDTPI"


_FLRUSDTPI = _FLRUSDTPI(*_FLRUSDTPI._fields)
"""
    name: .FLRUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FLRUSDTPI8H(Symbol):
    """
        name: .FLRUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FLRUSDTPI8H"

    def __str__(self):
        return ".FLRUSDTPI8H"

    def __call__(self):
        return ".FLRUSDTPI8H"


_FLRUSDTPI8H = _FLRUSDTPI8H(*_FLRUSDTPI8H._fields)
"""
    name: .FLRUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FLRUSDPI(Symbol):
    """
        name: .FLRUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FLRUSDPI"

    def __str__(self):
        return ".FLRUSDPI"

    def __call__(self):
        return ".FLRUSDPI"


_FLRUSDPI = _FLRUSDPI(*_FLRUSDPI._fields)
"""
    name: .FLRUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _FLRUSDPI8H(Symbol):
    """
        name: .FLRUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".FLRUSDPI8H"

    def __str__(self):
        return ".FLRUSDPI8H"

    def __call__(self):
        return ".FLRUSDPI8H"


_FLRUSDPI8H = _FLRUSDPI8H(*_FLRUSDPI8H._fields)
"""
    name: .FLRUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFLR(Symbol):
    """
        name: .BFLR
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLR"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFLR"

    def __str__(self):
        return ".BFLR"

    def __call__(self):
        return ".BFLR"


_BFLR = _BFLR(*_BFLR._fields)
"""
    name: .BFLR
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BFLR_NEXT(Symbol):
    """
        name: .BFLR_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLR_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BFLR_NEXT"

    def __str__(self):
        return ".BFLR_NEXT"

    def __call__(self):
        return ".BFLR_NEXT"


_BFLR_NEXT = _BFLR_NEXT(*_BFLR_NEXT._fields)
"""
    name: .BFLR_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLURBON(Symbol):
    """
        name: .BLURBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLURBON"

    def __str__(self):
        return ".BLURBON"

    def __call__(self):
        return ".BLURBON"


_BLURBON = _BLURBON(*_BLURBON._fields)
"""
    name: .BLURBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLURBON8H(Symbol):
    """
        name: .BLURBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLURBON8H"

    def __str__(self):
        return ".BLURBON8H"

    def __call__(self):
        return ".BLURBON8H"


_BLURBON8H = _BLURBON8H(*_BLURBON8H._fields)
"""
    name: .BLURBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLURUSDTPI(Symbol):
    """
        name: .BLURUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLURUSDTPI"

    def __str__(self):
        return ".BLURUSDTPI"

    def __call__(self):
        return ".BLURUSDTPI"


_BLURUSDTPI = _BLURUSDTPI(*_BLURUSDTPI._fields)
"""
    name: .BLURUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLURUSDTPI8H(Symbol):
    """
        name: .BLURUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLURUSDTPI8H"

    def __str__(self):
        return ".BLURUSDTPI8H"

    def __call__(self):
        return ".BLURUSDTPI8H"


_BLURUSDTPI8H = _BLURUSDTPI8H(*_BLURUSDTPI8H._fields)
"""
    name: .BLURUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLURUSDPI(Symbol):
    """
        name: .BLURUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLURUSDPI"

    def __str__(self):
        return ".BLURUSDPI"

    def __call__(self):
        return ".BLURUSDPI"


_BLURUSDPI = _BLURUSDPI(*_BLURUSDPI._fields)
"""
    name: .BLURUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLURUSDPI8H(Symbol):
    """
        name: .BLURUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLURUSDPI8H"

    def __str__(self):
        return ".BLURUSDPI8H"

    def __call__(self):
        return ".BLURUSDPI8H"


_BLURUSDPI8H = _BLURUSDPI8H(*_BLURUSDPI8H._fields)
"""
    name: .BLURUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBLUR(Symbol):
    """
        name: .BBLUR
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBLUR"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBLUR"

    def __str__(self):
        return ".BBLUR"

    def __call__(self):
        return ".BBLUR"


_BBLUR = _BBLUR(*_BBLUR._fields)
"""
    name: .BBLUR
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBLUR_NEXT(Symbol):
    """
        name: .BBLUR_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBLUR_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBLUR_NEXT"

    def __str__(self):
        return ".BBLUR_NEXT"

    def __call__(self):
        return ".BBLUR_NEXT"


_BBLUR_NEXT = _BBLUR_NEXT(*_BBLUR_NEXT._fields)
"""
    name: .BBLUR_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBLURT(Symbol):
    """
        name: .BBLURT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBLURT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBLURT"

    def __str__(self):
        return ".BBLURT"

    def __call__(self):
        return ".BBLURT"


_BBLURT = _BBLURT(*_BBLURT._fields)
"""
    name: .BBLURT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BBLURT_NEXT(Symbol):
    """
        name: .BBLURT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBLURT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BBLURT_NEXT"

    def __str__(self):
        return ".BBLURT_NEXT"

    def __call__(self):
        return ".BBLURT_NEXT"


_BBLURT_NEXT = _BBLURT_NEXT(*_BBLURT_NEXT._fields)
"""
    name: .BBLURT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGMXT(Symbol):
    """
        name: .BGMXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGMXT"

    def __str__(self):
        return ".BGMXT"

    def __call__(self):
        return ".BGMXT"


_BGMXT = _BGMXT(*_BGMXT._fields)
"""
    name: .BGMXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGMXT_NEXT(Symbol):
    """
        name: .BGMXT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMXT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGMXT_NEXT"

    def __str__(self):
        return ".BGMXT_NEXT"

    def __call__(self):
        return ".BGMXT_NEXT"


_BGMXT_NEXT = _BGMXT_NEXT(*_BGMXT_NEXT._fields)
"""
    name: .BGMXT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGMX(Symbol):
    """
        name: .BGMX
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMX"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGMX"

    def __str__(self):
        return ".BGMX"

    def __call__(self):
        return ".BGMX"


_BGMX = _BGMX(*_BGMX._fields)
"""
    name: .BGMX
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BGMX_NEXT(Symbol):
    """
        name: .BGMX_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMX_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BGMX_NEXT"

    def __str__(self):
        return ".BGMX_NEXT"

    def __call__(self):
        return ".BGMX_NEXT"


_BGMX_NEXT = _BGMX_NEXT(*_BGMX_NEXT._fields)
"""
    name: .BGMX_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMXBON(Symbol):
    """
        name: .GMXBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMXBON"

    def __str__(self):
        return ".GMXBON"

    def __call__(self):
        return ".GMXBON"


_GMXBON = _GMXBON(*_GMXBON._fields)
"""
    name: .GMXBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMXBON8H(Symbol):
    """
        name: .GMXBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMXBON8H"

    def __str__(self):
        return ".GMXBON8H"

    def __call__(self):
        return ".GMXBON8H"


_GMXBON8H = _GMXBON8H(*_GMXBON8H._fields)
"""
    name: .GMXBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMXUSDTPI(Symbol):
    """
        name: .GMXUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMXUSDTPI"

    def __str__(self):
        return ".GMXUSDTPI"

    def __call__(self):
        return ".GMXUSDTPI"


_GMXUSDTPI = _GMXUSDTPI(*_GMXUSDTPI._fields)
"""
    name: .GMXUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMXUSDTPI8H(Symbol):
    """
        name: .GMXUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMXUSDTPI8H"

    def __str__(self):
        return ".GMXUSDTPI8H"

    def __call__(self):
        return ".GMXUSDTPI8H"


_GMXUSDTPI8H = _GMXUSDTPI8H(*_GMXUSDTPI8H._fields)
"""
    name: .GMXUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMXUSDPI(Symbol):
    """
        name: .GMXUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMXUSDPI"

    def __str__(self):
        return ".GMXUSDPI"

    def __call__(self):
        return ".GMXUSDPI"


_GMXUSDPI = _GMXUSDPI(*_GMXUSDPI._fields)
"""
    name: .GMXUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _GMXUSDPI8H(Symbol):
    """
        name: .GMXUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".GMXUSDPI8H"

    def __str__(self):
        return ".GMXUSDPI8H"

    def __call__(self):
        return ".GMXUSDPI8H"


_GMXUSDPI8H = _GMXUSDPI8H(*_GMXUSDPI8H._fields)
"""
    name: .GMXUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDCBON(Symbol):
    """
        name: .USDCBON
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCBON"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDCBON"

    def __str__(self):
        return ".USDCBON"

    def __call__(self):
        return ".USDCBON"


_USDCBON = _USDCBON(*_USDCBON._fields)
"""
    name: .USDCBON
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDCBON8H(Symbol):
    """
        name: .USDCBON8H
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCBON8H"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDCBON8H"

    def __str__(self):
        return ".USDCBON8H"

    def __call__(self):
        return ".USDCBON8H"


_USDCBON8H = _USDCBON8H(*_USDCBON8H._fields)
"""
    name: .USDCBON8H
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTUSDCPI(Symbol):
    """
        name: .USDTUSDCPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTUSDCPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTUSDCPI"

    def __str__(self):
        return ".USDTUSDCPI"

    def __call__(self):
        return ".USDTUSDCPI"


_USDTUSDCPI = _USDTUSDCPI(*_USDTUSDCPI._fields)
"""
    name: .USDTUSDCPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDTUSDCPI8H(Symbol):
    """
        name: .USDTUSDCPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTUSDCPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDTUSDCPI8H"

    def __str__(self):
        return ".USDTUSDCPI8H"

    def __call__(self):
        return ".USDTUSDCPI8H"


_USDTUSDCPI8H = _USDTUSDCPI8H(*_USDTUSDCPI8H._fields)
"""
    name: .USDTUSDCPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BUSDTUSDC(Symbol):
    """
        name: .BUSDTUSDC
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDTUSDC"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTUSDC"

    def __str__(self):
        return ".BUSDTUSDC"

    def __call__(self):
        return ".BUSDTUSDC"


_BUSDTUSDC = _BUSDTUSDC(*_BUSDTUSDC._fields)
"""
    name: .BUSDTUSDC
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BARBT(Symbol):
    """
        name: .BARBT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARBT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BARBT"

    def __str__(self):
        return ".BARBT"

    def __call__(self):
        return ".BARBT"


_BARBT = _BARBT(*_BARBT._fields)
"""
    name: .BARBT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BARBT_NEXT(Symbol):
    """
        name: .BARBT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARBT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BARBT_NEXT"

    def __str__(self):
        return ".BARBT_NEXT"

    def __call__(self):
        return ".BARBT_NEXT"


_BARBT_NEXT = _BARBT_NEXT(*_BARBT_NEXT._fields)
"""
    name: .BARBT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BARBT30M(Symbol):
    """
        name: .BARBT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARBT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BARBT30M"

    def __str__(self):
        return ".BARBT30M"

    def __call__(self):
        return ".BARBT30M"


_BARBT30M = _BARBT30M(*_BARBT30M._fields)
"""
    name: .BARBT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BARB(Symbol):
    """
        name: .BARB
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARB"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BARB"

    def __str__(self):
        return ".BARB"

    def __call__(self):
        return ".BARB"


_BARB = _BARB(*_BARB._fields)
"""
    name: .BARB
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BARB_NEXT(Symbol):
    """
        name: .BARB_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARB_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BARB_NEXT"

    def __str__(self):
        return ".BARB_NEXT"

    def __call__(self):
        return ".BARB_NEXT"


_BARB_NEXT = _BARB_NEXT(*_BARB_NEXT._fields)
"""
    name: .BARB_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ARBBON(Symbol):
    """
        name: .ARBBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ARBBON"

    def __str__(self):
        return ".ARBBON"

    def __call__(self):
        return ".ARBBON"


_ARBBON = _ARBBON(*_ARBBON._fields)
"""
    name: .ARBBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ARBBON8H(Symbol):
    """
        name: .ARBBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ARBBON8H"

    def __str__(self):
        return ".ARBBON8H"

    def __call__(self):
        return ".ARBBON8H"


_ARBBON8H = _ARBBON8H(*_ARBBON8H._fields)
"""
    name: .ARBBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ARBUSDTPI(Symbol):
    """
        name: .ARBUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ARBUSDTPI"

    def __str__(self):
        return ".ARBUSDTPI"

    def __call__(self):
        return ".ARBUSDTPI"


_ARBUSDTPI = _ARBUSDTPI(*_ARBUSDTPI._fields)
"""
    name: .ARBUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ARBUSDTPI8H(Symbol):
    """
        name: .ARBUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ARBUSDTPI8H"

    def __str__(self):
        return ".ARBUSDTPI8H"

    def __call__(self):
        return ".ARBUSDTPI8H"


_ARBUSDTPI8H = _ARBUSDTPI8H(*_ARBUSDTPI8H._fields)
"""
    name: .ARBUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ARBUSDPI(Symbol):
    """
        name: .ARBUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ARBUSDPI"

    def __str__(self):
        return ".ARBUSDPI"

    def __call__(self):
        return ".ARBUSDPI"


_ARBUSDPI = _ARBUSDPI(*_ARBUSDPI._fields)
"""
    name: .ARBUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ARBUSDPI8H(Symbol):
    """
        name: .ARBUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ARBUSDPI8H"

    def __str__(self):
        return ".ARBUSDPI8H"

    def __call__(self):
        return ".ARBUSDPI8H"


_ARBUSDPI8H = _ARBUSDPI8H(*_ARBUSDPI8H._fields)
"""
    name: .ARBUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BPEPET(Symbol):
    """
        name: .BPEPET
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BPEPET"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BPEPET"

    def __str__(self):
        return ".BPEPET"

    def __call__(self):
        return ".BPEPET"


_BPEPET = _BPEPET(*_BPEPET._fields)
"""
    name: .BPEPET
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BPEPET_NEXT(Symbol):
    """
        name: .BPEPET_NEXT
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BPEPET_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BPEPET_NEXT"

    def __str__(self):
        return ".BPEPET_NEXT"

    def __call__(self):
        return ".BPEPET_NEXT"


_BPEPET_NEXT = _BPEPET_NEXT(*_BPEPET_NEXT._fields)
"""
    name: .BPEPET_NEXT
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BPEPE(Symbol):
    """
        name: .BPEPE
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BPEPE"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BPEPE"

    def __str__(self):
        return ".BPEPE"

    def __call__(self):
        return ".BPEPE"


_BPEPE = _BPEPE(*_BPEPE._fields)
"""
    name: .BPEPE
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BPEPE_NEXT(Symbol):
    """
        name: .BPEPE_NEXT
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BPEPE_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BPEPE_NEXT"

    def __str__(self):
        return ".BPEPE_NEXT"

    def __call__(self):
        return ".BPEPE_NEXT"


_BPEPE_NEXT = _BPEPE_NEXT(*_BPEPE_NEXT._fields)
"""
    name: .BPEPE_NEXT
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _PEPEBON(Symbol):
    """
        name: .PEPEBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".PEPEBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".PEPEBON"

    def __str__(self):
        return ".PEPEBON"

    def __call__(self):
        return ".PEPEBON"


_PEPEBON = _PEPEBON(*_PEPEBON._fields)
"""
    name: .PEPEBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _PEPEBON8H(Symbol):
    """
        name: .PEPEBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".PEPEBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".PEPEBON8H"

    def __str__(self):
        return ".PEPEBON8H"

    def __call__(self):
        return ".PEPEBON8H"


_PEPEBON8H = _PEPEBON8H(*_PEPEBON8H._fields)
"""
    name: .PEPEBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _PEPEUSDTPI(Symbol):
    """
        name: .PEPEUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".PEPEUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".PEPEUSDTPI"

    def __str__(self):
        return ".PEPEUSDTPI"

    def __call__(self):
        return ".PEPEUSDTPI"


_PEPEUSDTPI = _PEPEUSDTPI(*_PEPEUSDTPI._fields)
"""
    name: .PEPEUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _PEPEUSDTPI8H(Symbol):
    """
        name: .PEPEUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".PEPEUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".PEPEUSDTPI8H"

    def __str__(self):
        return ".PEPEUSDTPI8H"

    def __call__(self):
        return ".PEPEUSDTPI8H"


_PEPEUSDTPI8H = _PEPEUSDTPI8H(*_PEPEUSDTPI8H._fields)
"""
    name: .PEPEUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _PEPEUSDPI(Symbol):
    """
        name: .PEPEUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".PEPEUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".PEPEUSDPI"

    def __str__(self):
        return ".PEPEUSDPI"

    def __call__(self):
        return ".PEPEUSDPI"


_PEPEUSDPI = _PEPEUSDPI(*_PEPEUSDPI._fields)
"""
    name: .PEPEUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _PEPEUSDPI8H(Symbol):
    """
        name: .PEPEUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".PEPEUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".PEPEUSDPI8H"

    def __str__(self):
        return ".PEPEUSDPI8H"

    def __call__(self):
        return ".PEPEUSDPI8H"


_PEPEUSDPI8H = _PEPEUSDPI8H(*_PEPEUSDPI8H._fields)
"""
    name: .PEPEUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSUIT(Symbol):
    """
        name: .BSUIT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUIT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSUIT"

    def __str__(self):
        return ".BSUIT"

    def __call__(self):
        return ".BSUIT"


_BSUIT = _BSUIT(*_BSUIT._fields)
"""
    name: .BSUIT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSUIT_NEXT(Symbol):
    """
        name: .BSUIT_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUIT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSUIT_NEXT"

    def __str__(self):
        return ".BSUIT_NEXT"

    def __call__(self):
        return ".BSUIT_NEXT"


_BSUIT_NEXT = _BSUIT_NEXT(*_BSUIT_NEXT._fields)
"""
    name: .BSUIT_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSUI(Symbol):
    """
        name: .BSUI
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUI"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSUI"

    def __str__(self):
        return ".BSUI"

    def __call__(self):
        return ".BSUI"


_BSUI = _BSUI(*_BSUI._fields)
"""
    name: .BSUI
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSUI_NEXT(Symbol):
    """
        name: .BSUI_NEXT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUI_NEXT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSUI_NEXT"

    def __str__(self):
        return ".BSUI_NEXT"

    def __call__(self):
        return ".BSUI_NEXT"


_BSUI_NEXT = _BSUI_NEXT(*_BSUI_NEXT._fields)
"""
    name: .BSUI_NEXT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BSUIT30M(Symbol):
    """
        name: .BSUIT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUIT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BSUIT30M"

    def __str__(self):
        return ".BSUIT30M"

    def __call__(self):
        return ".BSUIT30M"


_BSUIT30M = _BSUIT30M(*_BSUIT30M._fields)
"""
    name: .BSUIT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUIUSDTPI(Symbol):
    """
        name: .SUIUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUIUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUIUSDTPI"

    def __str__(self):
        return ".SUIUSDTPI"

    def __call__(self):
        return ".SUIUSDTPI"


_SUIUSDTPI = _SUIUSDTPI(*_SUIUSDTPI._fields)
"""
    name: .SUIUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUIUSDTPI8H(Symbol):
    """
        name: .SUIUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUIUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUIUSDTPI8H"

    def __str__(self):
        return ".SUIUSDTPI8H"

    def __call__(self):
        return ".SUIUSDTPI8H"


_SUIUSDTPI8H = _SUIUSDTPI8H(*_SUIUSDTPI8H._fields)
"""
    name: .SUIUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUIUSDPI(Symbol):
    """
        name: .SUIUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUIUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUIUSDPI"

    def __str__(self):
        return ".SUIUSDPI"

    def __call__(self):
        return ".SUIUSDPI"


_SUIUSDPI = _SUIUSDPI(*_SUIUSDPI._fields)
"""
    name: .SUIUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUIUSDPI8H(Symbol):
    """
        name: .SUIUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUIUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUIUSDPI8H"

    def __str__(self):
        return ".SUIUSDPI8H"

    def __call__(self):
        return ".SUIUSDPI8H"


_SUIUSDPI8H = _SUIUSDPI8H(*_SUIUSDPI8H._fields)
"""
    name: .SUIUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUIBON(Symbol):
    """
        name: .SUIBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUIBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUIBON"

    def __str__(self):
        return ".SUIBON"

    def __call__(self):
        return ".SUIBON"


_SUIBON = _SUIBON(*_SUIBON._fields)
"""
    name: .SUIBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _SUIBON8H(Symbol):
    """
        name: .SUIBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUIBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".SUIBON8H"

    def __str__(self):
        return ".SUIBON8H"

    def __call__(self):
        return ".SUIBON8H"


_SUIBON8H = _SUIBON8H(*_SUIBON8H._fields)
"""
    name: .SUIBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BKLAYT30M(Symbol):
    """
        name: .BKLAYT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BKLAYT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BKLAYT30M"

    def __str__(self):
        return ".BKLAYT30M"

    def __call__(self):
        return ".BKLAYT30M"


_BKLAYT30M = _BKLAYT30M(*_BKLAYT30M._fields)
"""
    name: .BKLAYT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BCROT30M(Symbol):
    """
        name: .BCROT30M
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCROT30M"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BCROT30M"

    def __str__(self):
        return ".BCROT30M"

    def __call__(self):
        return ".BCROT30M"


_BCROT30M = _BCROT30M(*_BCROT30M._fields)
"""
    name: .BCROT30M
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class ADAM23(Symbol):
    """
        name: ADAM23
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ADAM23"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = 0.05
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADAM23"

    def __str__(self):
        return "ADAM23"

    def __call__(self):
        return "ADAM23"


ADAM23 = ADAM23(*ADAM23._fields)
"""
    name: ADAM23
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: 0.05
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class XRPM23(Symbol):
    """
        name: XRPM23
        significant_digits: None
        tick_size: 1e-08
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XRPM23"
    significant_digits: int = None
    tick_size: int = 1e-08
    min_margin: float = None
    initial_margin: float = 0.05
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPM23"

    def __str__(self):
        return "XRPM23"

    def __call__(self):
        return "XRPM23"


XRPM23 = XRPM23(*XRPM23._fields)
"""
    name: XRPM23
    significant_digits: None
    tick_size: 1e-08
    min_margin: None
    initial_margin: 0.05
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class ARBUSDTM23(Symbol):
    """
        name: ARBUSDTM23
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ARBUSDTM23"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.05
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARBUSDTM23"

    def __str__(self):
        return "ARBUSDTM23"

    def __call__(self):
        return "ARBUSDTM23"


ARBUSDTM23 = ARBUSDTM23(*ARBUSDTM23._fields)
"""
    name: ARBUSDTM23
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.05
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class KLAYUSD(Symbol):
    """
        name: KLAYUSD
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "KLAYUSD"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KLAYUSD"

    def __str__(self):
        return "KLAYUSD"

    def __call__(self):
        return "KLAYUSD"


KLAYUSD = KLAYUSD(*KLAYUSD._fields)
"""
    name: KLAYUSD
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: 0.01
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class KLAYUSDT(Symbol):
    """
        name: KLAYUSDT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "KLAYUSDT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KLAYUSDT"

    def __str__(self):
        return "KLAYUSDT"

    def __call__(self):
        return "KLAYUSDT"


KLAYUSDT = KLAYUSDT(*KLAYUSDT._fields)
"""
    name: KLAYUSDT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: 0.01
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class XRPUSD(Symbol):
    """
        name: XRPUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XRPUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 100000000
    has_margin: bool = True
    exchange: str = "bitmex"

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


XRPUSD = XRPUSD(*XRPUSD._fields)
"""
    name: XRPUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 100000000
    has_margin: True
    exchange: bitmex
"""


class BCHUSD(Symbol):
    """
        name: BCHUSD
        significant_digits: None
        tick_size: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BCHUSD"
    significant_digits: int = None
    tick_size: int = 0.05
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 100000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: BCHUSD
    significant_digits: None
    tick_size: 0.05
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 100000000
    has_margin: True
    exchange: bitmex
"""


class DOGEUSD(Symbol):
    """
        name: DOGEUSD
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 5000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "DOGEUSD"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 5000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOGEUSD"

    def __str__(self):
        return "DOGEUSD"

    def __call__(self):
        return "DOGEUSD"


DOGEUSD = DOGEUSD(*DOGEUSD._fields)
"""
    name: DOGEUSD
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 5000000
    has_margin: True
    exchange: bitmex
"""


class BNBUSD(Symbol):
    """
        name: BNBUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BNBUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 1000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNBUSD"

    def __str__(self):
        return "BNBUSD"

    def __call__(self):
        return "BNBUSD"


BNBUSD = BNBUSD(*BNBUSD._fields)
"""
    name: BNBUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 1000000
    has_margin: True
    exchange: bitmex
"""


class LINKUSD(Symbol):
    """
        name: LINKUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LINKUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 1000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: LINKUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 1000000
    has_margin: True
    exchange: bitmex
"""


class SOLUSD(Symbol):
    """
        name: SOLUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "SOLUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 1000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: SOLUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 1000000
    has_margin: True
    exchange: bitmex
"""


class APTUSD(Symbol):
    """
        name: APTUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "APTUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 1000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: APTUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 1000000
    has_margin: True
    exchange: bitmex
"""


class BMEXUSD(Symbol):
    """
        name: BMEXUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BMEXUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 1000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BMEXUSD"

    def __str__(self):
        return "BMEXUSD"

    def __call__(self):
        return "BMEXUSD"


BMEXUSD = BMEXUSD(*BMEXUSD._fields)
"""
    name: BMEXUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 1000000
    has_margin: True
    exchange: bitmex
"""


class CROUSD(Symbol):
    """
        name: CROUSD
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 5000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "CROUSD"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 5000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CROUSD"

    def __str__(self):
        return "CROUSD"

    def __call__(self):
        return "CROUSD"


CROUSD = CROUSD(*CROUSD._fields)
"""
    name: CROUSD
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 5000000
    has_margin: True
    exchange: bitmex
"""


class FLRUSD(Symbol):
    """
        name: FLRUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "FLRUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: FLRUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class BLURUSD(Symbol):
    """
        name: BLURUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BLURUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: BLURUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class GMXUSD(Symbol):
    """
        name: GMXUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "GMXUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 1000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: GMXUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 1000000
    has_margin: True
    exchange: bitmex
"""


class ARBUSD(Symbol):
    """
        name: ARBUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ARBUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: ARBUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class PEPEUSDT(Symbol):
    """
        name: PEPEUSDT
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: 0.02
        min_order_size: 10000
        max_order_size: 100000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "PEPEUSDT"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 10000
    max_order_size: float = 100000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PEPEUSDT"

    def __str__(self):
        return "PEPEUSDT"

    def __call__(self):
        return "PEPEUSDT"


PEPEUSDT = PEPEUSDT(*PEPEUSDT._fields)
"""
    name: PEPEUSDT
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: 0.02
    min_order_size: 10000
    max_order_size: 100000000000
    has_margin: True
    exchange: bitmex
"""


class PEPEUSD(Symbol):
    """
        name: PEPEUSD
        significant_digits: None
        tick_size: 1e-09
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "PEPEUSD"
    significant_digits: int = None
    tick_size: int = 1e-09
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PEPEUSD"

    def __str__(self):
        return "PEPEUSD"

    def __call__(self):
        return "PEPEUSD"


PEPEUSD = PEPEUSD(*PEPEUSD._fields)
"""
    name: PEPEUSD
    significant_digits: None
    tick_size: 1e-09
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class SUIUSD(Symbol):
    """
        name: SUIUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "SUIUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: SUIUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class DOGEUSDT(Symbol):
    """
        name: DOGEUSDT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 10000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "DOGEUSDT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 10000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOGEUSDT"

    def __str__(self):
        return "DOGEUSDT"

    def __call__(self):
        return "DOGEUSDT"


DOGEUSDT = DOGEUSDT(*DOGEUSDT._fields)
"""
    name: DOGEUSDT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 10000000000
    has_margin: True
    exchange: bitmex
"""


class DOTUSDT(Symbol):
    """
        name: DOTUSDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "DOTUSDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: DOTUSDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class ADAUSDT(Symbol):
    """
        name: ADAUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ADAUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: ADAUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class BNBUSDT(Symbol):
    """
        name: BNBUSDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BNBUSDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNBUSDT"

    def __str__(self):
        return "BNBUSDT"

    def __call__(self):
        return "BNBUSDT"


BNBUSDT = BNBUSDT(*BNBUSDT._fields)
"""
    name: BNBUSDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class SOLUSDT(Symbol):
    """
        name: SOLUSDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "SOLUSDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: SOLUSDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class ADAUSD(Symbol):
    """
        name: ADAUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ADAUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: ADAUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class EOSUSD(Symbol):
    """
        name: EOSUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "EOSUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: EOSUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class XRPUSDT(Symbol):
    """
        name: XRPUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XRPUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: XRPUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class BCHUSDT(Symbol):
    """
        name: BCHUSDT
        significant_digits: None
        tick_size: 0.05
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BCHUSDT"
    significant_digits: int = None
    tick_size: int = 0.05
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: BCHUSDT
    significant_digits: None
    tick_size: 0.05
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class APEUSDT(Symbol):
    """
        name: APEUSDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "APEUSDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: APEUSDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class GMTUSDT(Symbol):
    """
        name: GMTUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "GMTUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GMTUSDT"

    def __str__(self):
        return "GMTUSDT"

    def __call__(self):
        return "GMTUSDT"


GMTUSDT = GMTUSDT(*GMTUSDT._fields)
"""
    name: GMTUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class GMTUSD(Symbol):
    """
        name: GMTUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "GMTUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: GMTUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class NEARUSD(Symbol):
    """
        name: NEARUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "NEARUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: NEARUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class APTUSDT(Symbol):
    """
        name: APTUSDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "APTUSDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APTUSDT"

    def __str__(self):
        return "APTUSDT"

    def __call__(self):
        return "APTUSDT"


APTUSDT = APTUSDT(*APTUSDT._fields)
"""
    name: APTUSDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class BMEXUSDT(Symbol):
    """
        name: BMEXUSDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BMEXUSDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BMEXUSDT"

    def __str__(self):
        return "BMEXUSDT"

    def __call__(self):
        return "BMEXUSDT"


BMEXUSDT = BMEXUSDT(*BMEXUSDT._fields)
"""
    name: BMEXUSDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class CROUSDT(Symbol):
    """
        name: CROUSDT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 10000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "CROUSDT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 10000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CROUSDT"

    def __str__(self):
        return "CROUSDT"

    def __call__(self):
        return "CROUSDT"


CROUSDT = CROUSDT(*CROUSDT._fields)
"""
    name: CROUSDT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 10000000000
    has_margin: True
    exchange: bitmex
"""


class FLRUSDT(Symbol):
    """
        name: FLRUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "FLRUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLRUSDT"

    def __str__(self):
        return "FLRUSDT"

    def __call__(self):
        return "FLRUSDT"


FLRUSDT = FLRUSDT(*FLRUSDT._fields)
"""
    name: FLRUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class BLURUSDT(Symbol):
    """
        name: BLURUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BLURUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BLURUSDT"

    def __str__(self):
        return "BLURUSDT"

    def __call__(self):
        return "BLURUSDT"


BLURUSDT = BLURUSDT(*BLURUSDT._fields)
"""
    name: BLURUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class GMXUSDT(Symbol):
    """
        name: GMXUSDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "GMXUSDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GMXUSDT"

    def __str__(self):
        return "GMXUSDT"

    def __call__(self):
        return "GMXUSDT"


GMXUSDT = GMXUSDT(*GMXUSDT._fields)
"""
    name: GMXUSDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class ARBUSDT(Symbol):
    """
        name: ARBUSDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 100
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ARBUSDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 100
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARBUSDT"

    def __str__(self):
        return "ARBUSDT"

    def __call__(self):
        return "ARBUSDT"


ARBUSDT = ARBUSDT(*ARBUSDT._fields)
"""
    name: ARBUSDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 100
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class SUIUSDT(Symbol):
    """
        name: SUIUSDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 100
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "SUIUSDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 100
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUIUSDT"

    def __str__(self):
        return "SUIUSDT"

    def __call__(self):
        return "SUIUSDT"


SUIUSDT = SUIUSDT(*SUIUSDT._fields)
"""
    name: SUIUSDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.03
    min_order_size: 100
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class LUNAUSD(Symbol):
    """
        name: LUNAUSD
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.04
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LUNAUSD"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.04
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: LUNAUSD
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.04
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class DOTUSD(Symbol):
    """
        name: DOTUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.04
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "DOTUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.04
    min_order_size: float = 1
    max_order_size: float = 1000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: DOTUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.04
    min_order_size: 1
    max_order_size: 1000000
    has_margin: True
    exchange: bitmex
"""


class MATICUSDT(Symbol):
    """
        name: MATICUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "MATICUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.05
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: MATICUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.05
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class AVAXUSD(Symbol):
    """
        name: AVAXUSD
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "AVAXUSD"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.05
    min_order_size: float = 1
    max_order_size: float = 500000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: AVAXUSD
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.05
    min_order_size: 1
    max_order_size: 500000
    has_margin: True
    exchange: bitmex
"""


class AXSUSD(Symbol):
    """
        name: AXSUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "AXSUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 0.05
    min_order_size: float = 1
    max_order_size: float = 1000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: AXSUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 0.05
    min_order_size: 1
    max_order_size: 1000000
    has_margin: True
    exchange: bitmex
"""


class AVAXUSDT(Symbol):
    """
        name: AVAXUSDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "AVAXUSDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 0.05
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: AVAXUSDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 0.05
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class LUNAUSDT(Symbol):
    """
        name: LUNAUSDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LUNAUSDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.05
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LUNAUSDT"

    def __str__(self):
        return "LUNAUSDT"

    def __call__(self):
        return "LUNAUSDT"


LUNAUSDT = LUNAUSDT(*LUNAUSDT._fields)
"""
    name: LUNAUSDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.05
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class USDTUSDC(Symbol):
    """
        name: USDTUSDC
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 0.1
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "USDTUSDC"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 0.1
    min_order_size: float = 1
    max_order_size: float = 100000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDTUSDC"

    def __str__(self):
        return "USDTUSDC"

    def __call__(self):
        return "USDTUSDC"


USDTUSDC = USDTUSDC(*USDTUSDC._fields)
"""
    name: USDTUSDC
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 0.1
    min_order_size: 1
    max_order_size: 100000000
    has_margin: True
    exchange: bitmex
"""


class UNI_USDT(Symbol):
    """
        name: UNI_USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 1
        min_order_size: 10000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "UNI_USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 10000000
    max_order_size: float = 10000000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNI_USDT"

    def __str__(self):
        return "UNI_USDT"

    def __call__(self):
        return "UNI_USDT"


UNI_USDT = UNI_USDT(*UNI_USDT._fields)
"""
    name: UNI_USDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 1
    min_order_size: 10000000
    max_order_size: 10000000000000
    has_margin: True
    exchange: bitmex
"""


class LINK_USDT(Symbol):
    """
        name: LINK_USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 1
        min_order_size: 10000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LINK_USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 10000000
    max_order_size: float = 10000000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINK_USDT"

    def __str__(self):
        return "LINK_USDT"

    def __call__(self):
        return "LINK_USDT"


LINK_USDT = LINK_USDT(*LINK_USDT._fields)
"""
    name: LINK_USDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 1
    min_order_size: 10000000
    max_order_size: 10000000000000
    has_margin: True
    exchange: bitmex
"""


class MATIC_USDT(Symbol):
    """
        name: MATIC_USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 1
        min_order_size: 100000000
        max_order_size: 100000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "MATIC_USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 100000000
    max_order_size: float = 100000000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATIC_USDT"

    def __str__(self):
        return "MATIC_USDT"

    def __call__(self):
        return "MATIC_USDT"


MATIC_USDT = MATIC_USDT(*MATIC_USDT._fields)
"""
    name: MATIC_USDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 1
    min_order_size: 100000000
    max_order_size: 100000000000000
    has_margin: True
    exchange: bitmex
"""


class AXS_USDT(Symbol):
    """
        name: AXS_USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 1000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "AXS_USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 1000000
    max_order_size: float = 1000000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AXS_USDT"

    def __str__(self):
        return "AXS_USDT"

    def __call__(self):
        return "AXS_USDT"


AXS_USDT = AXS_USDT(*AXS_USDT._fields)
"""
    name: AXS_USDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 1
    min_order_size: 1000000
    max_order_size: 1000000000000
    has_margin: True
    exchange: bitmex
"""


class APE_USDT(Symbol):
    """
        name: APE_USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 1
        min_order_size: 10000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "APE_USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 10000000
    max_order_size: float = 10000000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APE_USDT"

    def __str__(self):
        return "APE_USDT"

    def __call__(self):
        return "APE_USDT"


APE_USDT = APE_USDT(*APE_USDT._fields)
"""
    name: APE_USDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 1
    min_order_size: 10000000
    max_order_size: 10000000000000
    has_margin: True
    exchange: bitmex
"""


class TRX_USDT(Symbol):
    """
        name: TRX_USDT
        significant_digits: None
        tick_size: 0.0001
        min_margin: None
        initial_margin: 1
        min_order_size: 100000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "TRX_USDT"
    significant_digits: int = None
    tick_size: int = 0.0001
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 100000000
    max_order_size: float = 10000000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRX_USDT"

    def __str__(self):
        return "TRX_USDT"

    def __call__(self):
        return "TRX_USDT"


TRX_USDT = TRX_USDT(*TRX_USDT._fields)
"""
    name: TRX_USDT
    significant_digits: None
    tick_size: 0.0001
    min_margin: None
    initial_margin: 1
    min_order_size: 100000000
    max_order_size: 10000000000000
    has_margin: True
    exchange: bitmex
"""


class SOL_USDT(Symbol):
    """
        name: SOL_USDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "SOL_USDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 1000000
    max_order_size: float = 10000000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOL_USDT"

    def __str__(self):
        return "SOL_USDT"

    def __call__(self):
        return "SOL_USDT"


SOL_USDT = SOL_USDT(*SOL_USDT._fields)
"""
    name: SOL_USDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 1
    min_order_size: 1000000
    max_order_size: 10000000000000
    has_margin: True
    exchange: bitmex
"""


class BMEX_USDT(Symbol):
    """
        name: BMEX_USDT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 1000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BMEX_USDT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 1000000
    max_order_size: float = 1000000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BMEX_USDT"

    def __str__(self):
        return "BMEX_USDT"

    def __call__(self):
        return "BMEX_USDT"


BMEX_USDT = BMEX_USDT(*BMEX_USDT._fields)
"""
    name: BMEX_USDT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: 1
    min_order_size: 1000000
    max_order_size: 1000000000000
    has_margin: True
    exchange: bitmex
"""


class _XBT(Symbol):
    """
        name: .XBT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBT"

    def __str__(self):
        return ".XBT"

    def __call__(self):
        return ".XBT"


_XBT = _XBT(*_XBT._fields)
"""
    name: .XBT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XBT30M(Symbol):
    """
        name: .XBT30M
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBT30M"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBT30M"

    def __str__(self):
        return ".XBT30M"

    def __call__(self):
        return ".XBT30M"


_XBT30M = _XBT30M(*_XBT30M._fields)
"""
    name: .XBT30M
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XBTBON(Symbol):
    """
        name: .XBTBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBTBON"

    def __str__(self):
        return ".XBTBON"

    def __call__(self):
        return ".XBTBON"


_XBTBON = _XBTBON(*_XBTBON._fields)
"""
    name: .XBTBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XBTBON8H(Symbol):
    """
        name: .XBTBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBTBON8H"

    def __str__(self):
        return ".XBTBON8H"

    def __call__(self):
        return ".XBTBON8H"


_XBTBON8H = _XBTBON8H(*_XBTBON8H._fields)
"""
    name: .XBTBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XBTUSDPI(Symbol):
    """
        name: .XBTUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBTUSDPI"

    def __str__(self):
        return ".XBTUSDPI"

    def __call__(self):
        return ".XBTUSDPI"


_XBTUSDPI = _XBTUSDPI(*_XBTUSDPI._fields)
"""
    name: .XBTUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XBTUSDPI8H(Symbol):
    """
        name: .XBTUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBTUSDPI8H"

    def __str__(self):
        return ".XBTUSDPI8H"

    def __call__(self):
        return ".XBTUSDPI8H"


_XBTUSDPI8H = _XBTUSDPI8H(*_XBTUSDPI8H._fields)
"""
    name: .XBTUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXBT(Symbol):
    """
        name: .BXBT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXBT"

    def __str__(self):
        return ".BXBT"

    def __call__(self):
        return ".BXBT"


_BXBT = _BXBT(*_BXBT._fields)
"""
    name: .BXBT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXBT30M(Symbol):
    """
        name: .BXBT30M
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBT30M"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXBT30M"

    def __str__(self):
        return ".BXBT30M"

    def __call__(self):
        return ".BXBT30M"


_BXBT30M = _BXBT30M(*_BXBT30M._fields)
"""
    name: .BXBT30M
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXBT_NEXT(Symbol):
    """
        name: .BXBT_NEXT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXBT_NEXT"

    def __str__(self):
        return ".BXBT_NEXT"

    def __call__(self):
        return ".BXBT_NEXT"


_BXBT_NEXT = _BXBT_NEXT(*_BXBT_NEXT._fields)
"""
    name: .BXBT_NEXT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXBTEUR(Symbol):
    """
        name: .BXBTEUR
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTEUR"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXBTEUR"

    def __str__(self):
        return ".BXBTEUR"

    def __call__(self):
        return ".BXBTEUR"


_BXBTEUR = _BXBTEUR(*_BXBTEUR._fields)
"""
    name: .BXBTEUR
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXBTEUR_NEXT(Symbol):
    """
        name: .BXBTEUR_NEXT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTEUR_NEXT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXBTEUR_NEXT"

    def __str__(self):
        return ".BXBTEUR_NEXT"

    def __call__(self):
        return ".BXBTEUR_NEXT"


_BXBTEUR_NEXT = _BXBTEUR_NEXT(*_BXBTEUR_NEXT._fields)
"""
    name: .BXBTEUR_NEXT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XBTEURPI(Symbol):
    """
        name: .XBTEURPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTEURPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBTEURPI"

    def __str__(self):
        return ".XBTEURPI"

    def __call__(self):
        return ".XBTEURPI"


_XBTEURPI = _XBTEURPI(*_XBTEURPI._fields)
"""
    name: .XBTEURPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XBTEURPI8H(Symbol):
    """
        name: .XBTEURPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTEURPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBTEURPI8H"

    def __str__(self):
        return ".XBTEURPI8H"

    def __call__(self):
        return ".XBTEURPI8H"


_XBTEURPI8H = _XBTEURPI8H(*_XBTEURPI8H._fields)
"""
    name: .XBTEURPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXBTEUR30M(Symbol):
    """
        name: .BXBTEUR30M
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTEUR30M"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXBTEUR30M"

    def __str__(self):
        return ".BXBTEUR30M"

    def __call__(self):
        return ".BXBTEUR30M"


_BXBTEUR30M = _BXBTEUR30M(*_BXBTEUR30M._fields)
"""
    name: .BXBTEUR30M
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXBTT(Symbol):
    """
        name: .BXBTT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXBTT"

    def __str__(self):
        return ".BXBTT"

    def __call__(self):
        return ".BXBTT"


_BXBTT = _BXBTT(*_BXBTT._fields)
"""
    name: .BXBTT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXBTT_NEXT(Symbol):
    """
        name: .BXBTT_NEXT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXBTT_NEXT"

    def __str__(self):
        return ".BXBTT_NEXT"

    def __call__(self):
        return ".BXBTT_NEXT"


_BXBTT_NEXT = _BXBTT_NEXT(*_BXBTT_NEXT._fields)
"""
    name: .BXBTT_NEXT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BXBTT30M(Symbol):
    """
        name: .BXBTT30M
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTT30M"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BXBTT30M"

    def __str__(self):
        return ".BXBTT30M"

    def __call__(self):
        return ".BXBTT30M"


_BXBTT30M = _BXBTT30M(*_BXBTT30M._fields)
"""
    name: .BXBTT30M
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XBTUSDTPI(Symbol):
    """
        name: .XBTUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBTUSDTPI"

    def __str__(self):
        return ".XBTUSDTPI"

    def __call__(self):
        return ".XBTUSDTPI"


_XBTUSDTPI = _XBTUSDTPI(*_XBTUSDTPI._fields)
"""
    name: .XBTUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _XBTUSDTPI8H(Symbol):
    """
        name: .XBTUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".XBTUSDTPI8H"

    def __str__(self):
        return ".XBTUSDTPI8H"

    def __call__(self):
        return ".XBTUSDTPI8H"


_XBTUSDTPI8H = _XBTUSDTPI8H(*_XBTUSDTPI8H._fields)
"""
    name: .XBTUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BVOL(Symbol):
    """
        name: .BVOL
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVOL"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BVOL"

    def __str__(self):
        return ".BVOL"

    def __call__(self):
        return ".BVOL"


_BVOL = _BVOL(*_BVOL._fields)
"""
    name: .BVOL
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BVOL24H(Symbol):
    """
        name: .BVOL24H
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVOL24H"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BVOL24H"

    def __str__(self):
        return ".BVOL24H"

    def __call__(self):
        return ".BVOL24H"


_BVOL24H = _BVOL24H(*_BVOL24H._fields)
"""
    name: .BVOL24H
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BVOL7D(Symbol):
    """
        name: .BVOL7D
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVOL7D"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BVOL7D"

    def __str__(self):
        return ".BVOL7D"

    def __call__(self):
        return ".BVOL7D"


_BVOL7D = _BVOL7D(*_BVOL7D._fields)
"""
    name: .BVOL7D
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ETHBON(Symbol):
    """
        name: .ETHBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ETHBON"

    def __str__(self):
        return ".ETHBON"

    def __call__(self):
        return ".ETHBON"


_ETHBON = _ETHBON(*_ETHBON._fields)
"""
    name: .ETHBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ETHBON8H(Symbol):
    """
        name: .ETHBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ETHBON8H"

    def __str__(self):
        return ".ETHBON8H"

    def __call__(self):
        return ".ETHBON8H"


_ETHBON8H = _ETHBON8H(*_ETHBON8H._fields)
"""
    name: .ETHBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ETHUSDPI(Symbol):
    """
        name: .ETHUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ETHUSDPI"

    def __str__(self):
        return ".ETHUSDPI"

    def __call__(self):
        return ".ETHUSDPI"


_ETHUSDPI = _ETHUSDPI(*_ETHUSDPI._fields)
"""
    name: .ETHUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ETHUSDPI8H(Symbol):
    """
        name: .ETHUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ETHUSDPI8H"

    def __str__(self):
        return ".ETHUSDPI8H"

    def __call__(self):
        return ".ETHUSDPI8H"


_ETHUSDPI8H = _ETHUSDPI8H(*_ETHUSDPI8H._fields)
"""
    name: .ETHUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETH(Symbol):
    """
        name: .BETH
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETH"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETH"

    def __str__(self):
        return ".BETH"

    def __call__(self):
        return ".BETH"


_BETH = _BETH(*_BETH._fields)
"""
    name: .BETH
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETH30M(Symbol):
    """
        name: .BETH30M
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETH30M"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETH30M"

    def __str__(self):
        return ".BETH30M"

    def __call__(self):
        return ".BETH30M"


_BETH30M = _BETH30M(*_BETH30M._fields)
"""
    name: .BETH30M
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHXBT(Symbol):
    """
        name: .BETHXBT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHXBT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHXBT"

    def __str__(self):
        return ".BETHXBT"

    def __call__(self):
        return ".BETHXBT"


_BETHXBT = _BETHXBT(*_BETHXBT._fields)
"""
    name: .BETHXBT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHXBT30M(Symbol):
    """
        name: .BETHXBT30M
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHXBT30M"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHXBT30M"

    def __str__(self):
        return ".BETHXBT30M"

    def __call__(self):
        return ".BETHXBT30M"


_BETHXBT30M = _BETHXBT30M(*_BETHXBT30M._fields)
"""
    name: .BETHXBT30M
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETH_NEXT(Symbol):
    """
        name: .BETH_NEXT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETH_NEXT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETH_NEXT"

    def __str__(self):
        return ".BETH_NEXT"

    def __call__(self):
        return ".BETH_NEXT"


_BETH_NEXT = _BETH_NEXT(*_BETH_NEXT._fields)
"""
    name: .BETH_NEXT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHXBT_NEXT(Symbol):
    """
        name: .BETHXBT_NEXT
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHXBT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHXBT_NEXT"

    def __str__(self):
        return ".BETHXBT_NEXT"

    def __call__(self):
        return ".BETHXBT_NEXT"


_BETHXBT_NEXT = _BETHXBT_NEXT(*_BETHXBT_NEXT._fields)
"""
    name: .BETHXBT_NEXT
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHT(Symbol):
    """
        name: .BETHT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHT"

    def __str__(self):
        return ".BETHT"

    def __call__(self):
        return ".BETHT"


_BETHT = _BETHT(*_BETHT._fields)
"""
    name: .BETHT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHT_NEXT(Symbol):
    """
        name: .BETHT_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHT_NEXT"

    def __str__(self):
        return ".BETHT_NEXT"

    def __call__(self):
        return ".BETHT_NEXT"


_BETHT_NEXT = _BETHT_NEXT(*_BETHT_NEXT._fields)
"""
    name: .BETHT_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETHT30M(Symbol):
    """
        name: .BETHT30M
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHT30M"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETHT30M"

    def __str__(self):
        return ".BETHT30M"

    def __call__(self):
        return ".BETHT30M"


_BETHT30M = _BETHT30M(*_BETHT30M._fields)
"""
    name: .BETHT30M
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ETHUSDTPI(Symbol):
    """
        name: .ETHUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ETHUSDTPI"

    def __str__(self):
        return ".ETHUSDTPI"

    def __call__(self):
        return ".ETHUSDTPI"


_ETHUSDTPI = _ETHUSDTPI(*_ETHUSDTPI._fields)
"""
    name: .ETHUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ETHUSDTPI8H(Symbol):
    """
        name: .ETHUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ETHUSDTPI8H"

    def __str__(self):
        return ".ETHUSDTPI8H"

    def __call__(self):
        return ".ETHUSDTPI8H"


_ETHUSDTPI8H = _ETHUSDTPI8H(*_ETHUSDTPI8H._fields)
"""
    name: .ETHUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ETHUSD_ETHPI(Symbol):
    """
        name: .ETHUSD_ETHPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSD_ETHPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ETHUSD_ETHPI"

    def __str__(self):
        return ".ETHUSD_ETHPI"

    def __call__(self):
        return ".ETHUSD_ETHPI"


_ETHUSD_ETHPI = _ETHUSD_ETHPI(*_ETHUSD_ETHPI._fields)
"""
    name: .ETHUSD_ETHPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _ETHUSD_ETHPI8H(Symbol):
    """
        name: .ETHUSD_ETHPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSD_ETHPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".ETHUSD_ETHPI8H"

    def __str__(self):
        return ".ETHUSD_ETHPI8H"

    def __call__(self):
        return ".ETHUSD_ETHPI8H"


_ETHUSD_ETHPI8H = _ETHUSD_ETHPI8H(*_ETHUSD_ETHPI8H._fields)
"""
    name: .ETHUSD_ETHPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BETC(Symbol):
    """
        name: .BETC
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETC"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BETC"

    def __str__(self):
        return ".BETC"

    def __call__(self):
        return ".BETC"


_BETC = _BETC(*_BETC._fields)
"""
    name: .BETC
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LTCBON(Symbol):
    """
        name: .LTCBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LTCBON"

    def __str__(self):
        return ".LTCBON"

    def __call__(self):
        return ".LTCBON"


_LTCBON = _LTCBON(*_LTCBON._fields)
"""
    name: .LTCBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LTCBON8H(Symbol):
    """
        name: .LTCBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LTCBON8H"

    def __str__(self):
        return ".LTCBON8H"

    def __call__(self):
        return ".LTCBON8H"


_LTCBON8H = _LTCBON8H(*_LTCBON8H._fields)
"""
    name: .LTCBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLTCXBT(Symbol):
    """
        name: .BLTCXBT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCXBT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLTCXBT"

    def __str__(self):
        return ".BLTCXBT"

    def __call__(self):
        return ".BLTCXBT"


_BLTCXBT = _BLTCXBT(*_BLTCXBT._fields)
"""
    name: .BLTCXBT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLTCXBT30M(Symbol):
    """
        name: .BLTCXBT30M
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCXBT30M"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLTCXBT30M"

    def __str__(self):
        return ".BLTCXBT30M"

    def __call__(self):
        return ".BLTCXBT30M"


_BLTCXBT30M = _BLTCXBT30M(*_BLTCXBT30M._fields)
"""
    name: .BLTCXBT30M
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLTCXBT_NEXT(Symbol):
    """
        name: .BLTCXBT_NEXT
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCXBT_NEXT"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLTCXBT_NEXT"

    def __str__(self):
        return ".BLTCXBT_NEXT"

    def __call__(self):
        return ".BLTCXBT_NEXT"


_BLTCXBT_NEXT = _BLTCXBT_NEXT(*_BLTCXBT_NEXT._fields)
"""
    name: .BLTCXBT_NEXT
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLTC(Symbol):
    """
        name: .BLTC
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTC"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLTC"

    def __str__(self):
        return ".BLTC"

    def __call__(self):
        return ".BLTC"


_BLTC = _BLTC(*_BLTC._fields)
"""
    name: .BLTC
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LTCUSDPI(Symbol):
    """
        name: .LTCUSDPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCUSDPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LTCUSDPI"

    def __str__(self):
        return ".LTCUSDPI"

    def __call__(self):
        return ".LTCUSDPI"


_LTCUSDPI = _LTCUSDPI(*_LTCUSDPI._fields)
"""
    name: .LTCUSDPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LTCUSDPI8H(Symbol):
    """
        name: .LTCUSDPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCUSDPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LTCUSDPI8H"

    def __str__(self):
        return ".LTCUSDPI8H"

    def __call__(self):
        return ".LTCUSDPI8H"


_LTCUSDPI8H = _LTCUSDPI8H(*_LTCUSDPI8H._fields)
"""
    name: .LTCUSDPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLTC_NEXT(Symbol):
    """
        name: .BLTC_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTC_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLTC_NEXT"

    def __str__(self):
        return ".BLTC_NEXT"

    def __call__(self):
        return ".BLTC_NEXT"


_BLTC_NEXT = _BLTC_NEXT(*_BLTC_NEXT._fields)
"""
    name: .BLTC_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLTCT(Symbol):
    """
        name: .BLTCT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLTCT"

    def __str__(self):
        return ".BLTCT"

    def __call__(self):
        return ".BLTCT"


_BLTCT = _BLTCT(*_BLTCT._fields)
"""
    name: .BLTCT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _BLTCT_NEXT(Symbol):
    """
        name: .BLTCT_NEXT
        significant_digits: None
        tick_size: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCT_NEXT"
    significant_digits: int = None
    tick_size: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BLTCT_NEXT"

    def __str__(self):
        return ".BLTCT_NEXT"

    def __call__(self):
        return ".BLTCT_NEXT"


_BLTCT_NEXT = _BLTCT_NEXT(*_BLTCT_NEXT._fields)
"""
    name: .BLTCT_NEXT
    significant_digits: None
    tick_size: 0.001
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LTCUSDTPI(Symbol):
    """
        name: .LTCUSDTPI
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCUSDTPI"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LTCUSDTPI"

    def __str__(self):
        return ".LTCUSDTPI"

    def __call__(self):
        return ".LTCUSDTPI"


_LTCUSDTPI = _LTCUSDTPI(*_LTCUSDTPI._fields)
"""
    name: .LTCUSDTPI
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _LTCUSDTPI8H(Symbol):
    """
        name: .LTCUSDTPI8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCUSDTPI8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".LTCUSDTPI8H"

    def __str__(self):
        return ".LTCUSDTPI8H"

    def __call__(self):
        return ".LTCUSDTPI8H"


_LTCUSDTPI8H = _LTCUSDTPI8H(*_LTCUSDTPI8H._fields)
"""
    name: .LTCUSDTPI8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDBON(Symbol):
    """
        name: .USDBON
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDBON"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDBON"

    def __str__(self):
        return ".USDBON"

    def __call__(self):
        return ".USDBON"


_USDBON = _USDBON(*_USDBON._fields)
"""
    name: .USDBON
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class _USDBON8H(Symbol):
    """
        name: .USDBON8H
        significant_digits: None
        tick_size: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDBON8H"
    significant_digits: int = None
    tick_size: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
    max_order_size: float = None
    has_margin: bool = False
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".USDBON8H"

    def __str__(self):
        return ".USDBON8H"

    def __call__(self):
        return ".USDBON8H"


_USDBON8H = _USDBON8H(*_USDBON8H._fields)
"""
    name: .USDBON8H
    significant_digits: None
    tick_size: 1e-06
    min_margin: None
    initial_margin: None
    min_order_size: None
    max_order_size: None
    has_margin: False
    exchange: bitmex
"""


class XBTUSD(Symbol):
    """
        name: XBTUSD
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTUSD"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 100
    max_order_size: float = 10000000
    has_margin: bool = True
    exchange: str = "bitmex"

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


XBTUSD = XBTUSD(*XBTUSD._fields)
"""
    name: XBTUSD
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.01
    min_order_size: 100
    max_order_size: 10000000
    has_margin: True
    exchange: bitmex
"""


class XBTUSDT(Symbol):
    """
        name: XBTUSDT
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTUSDT"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: XBTUSDT
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.01
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class XBTEUR(Symbol):
    """
        name: XBTEUR
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.02
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTEUR"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 100
    max_order_size: float = 10000000
    has_margin: bool = True
    exchange: str = "bitmex"

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


XBTEUR = XBTEUR(*XBTEUR._fields)
"""
    name: XBTEUR
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.02
    min_order_size: 100
    max_order_size: 10000000
    has_margin: True
    exchange: bitmex
"""


class XBTK23(Symbol):
    """
        name: XBTK23
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTK23"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 100
    max_order_size: float = 10000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTK23"

    def __str__(self):
        return "XBTK23"

    def __call__(self):
        return "XBTK23"


XBTK23 = XBTK23(*XBTK23._fields)
"""
    name: XBTK23
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.01
    min_order_size: 100
    max_order_size: 10000000
    has_margin: True
    exchange: bitmex
"""


class XBTM23(Symbol):
    """
        name: XBTM23
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTM23"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 100
    max_order_size: float = 10000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTM23"

    def __str__(self):
        return "XBTM23"

    def __call__(self):
        return "XBTM23"


XBTM23 = XBTM23(*XBTM23._fields)
"""
    name: XBTM23
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.01
    min_order_size: 100
    max_order_size: 10000000
    has_margin: True
    exchange: bitmex
"""


class XBTUSDTM23(Symbol):
    """
        name: XBTUSDTM23
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTUSDTM23"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTUSDTM23"

    def __str__(self):
        return "XBTUSDTM23"

    def __call__(self):
        return "XBTUSDTM23"


XBTUSDTM23 = XBTUSDTM23(*XBTUSDTM23._fields)
"""
    name: XBTUSDTM23
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.01
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class XBTU23(Symbol):
    """
        name: XBTU23
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTU23"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 100
    max_order_size: float = 10000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTU23"

    def __str__(self):
        return "XBTU23"

    def __call__(self):
        return "XBTU23"


XBTU23 = XBTU23(*XBTU23._fields)
"""
    name: XBTU23
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.01
    min_order_size: 100
    max_order_size: 10000000
    has_margin: True
    exchange: bitmex
"""


class XBTUSDTU23(Symbol):
    """
        name: XBTUSDTU23
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTUSDTU23"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTUSDTU23"

    def __str__(self):
        return "XBTUSDTU23"

    def __call__(self):
        return "XBTUSDTU23"


XBTUSDTU23 = XBTUSDTU23(*XBTUSDTU23._fields)
"""
    name: XBTUSDTU23
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.01
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class XBTZ23(Symbol):
    """
        name: XBTZ23
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTZ23"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 100
    max_order_size: float = 10000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTZ23"

    def __str__(self):
        return "XBTZ23"

    def __call__(self):
        return "XBTZ23"


XBTZ23 = XBTZ23(*XBTZ23._fields)
"""
    name: XBTZ23
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.01
    min_order_size: 100
    max_order_size: 10000000
    has_margin: True
    exchange: bitmex
"""


class XBT_USDT(Symbol):
    """
        name: XBT_USDT
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 1
        min_order_size: 10000
        max_order_size: 100000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBT_USDT"
    significant_digits: int = None
    tick_size: int = 0.5
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 10000
    max_order_size: float = 100000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBT_USDT"

    def __str__(self):
        return "XBT_USDT"

    def __call__(self):
        return "XBT_USDT"


XBT_USDT = XBT_USDT(*XBT_USDT._fields)
"""
    name: XBT_USDT
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 1
    min_order_size: 10000
    max_order_size: 100000000000
    has_margin: True
    exchange: bitmex
"""


class ETHUSD(Symbol):
    """
        name: ETHUSD
        significant_digits: None
        tick_size: 0.05
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSD"
    significant_digits: int = None
    tick_size: int = 0.05
    min_margin: float = None
    initial_margin: float = 0.01
    min_order_size: float = 1
    max_order_size: float = 10000000
    has_margin: bool = True
    exchange: str = "bitmex"

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


ETHUSD = ETHUSD(*ETHUSD._fields)
"""
    name: ETHUSD
    significant_digits: None
    tick_size: 0.05
    min_margin: None
    initial_margin: 0.01
    min_order_size: 1
    max_order_size: 10000000
    has_margin: True
    exchange: bitmex
"""


class ETHUSDT(Symbol):
    """
        name: ETHUSDT
        significant_digits: None
        tick_size: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSDT"
    significant_digits: int = None
    tick_size: int = 0.05
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: ETHUSDT
    significant_digits: None
    tick_size: 0.05
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class ETHUSD_ETH(Symbol):
    """
        name: ETHUSD_ETH
        significant_digits: None
        tick_size: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSD_ETH"
    significant_digits: int = None
    tick_size: int = 0.05
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 100000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHUSD_ETH"

    def __str__(self):
        return "ETHUSD_ETH"

    def __call__(self):
        return "ETHUSD_ETH"


ETHUSD_ETH = ETHUSD_ETH(*ETHUSD_ETH._fields)
"""
    name: ETHUSD_ETH
    significant_digits: None
    tick_size: 0.05
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 100000000
    has_margin: True
    exchange: bitmex
"""


class ETHM23(Symbol):
    """
        name: ETHM23
        significant_digits: None
        tick_size: 1e-05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHM23"
    significant_digits: int = None
    tick_size: int = 1e-05
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHM23"

    def __str__(self):
        return "ETHM23"

    def __call__(self):
        return "ETHM23"


ETHM23 = ETHM23(*ETHM23._fields)
"""
    name: ETHM23
    significant_digits: None
    tick_size: 1e-05
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class ETHUSDM23(Symbol):
    """
        name: ETHUSDM23
        significant_digits: None
        tick_size: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSDM23"
    significant_digits: int = None
    tick_size: int = 0.05
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 10000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHUSDM23"

    def __str__(self):
        return "ETHUSDM23"

    def __call__(self):
        return "ETHUSDM23"


ETHUSDM23 = ETHUSDM23(*ETHUSDM23._fields)
"""
    name: ETHUSDM23
    significant_digits: None
    tick_size: 0.05
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 10000000
    has_margin: True
    exchange: bitmex
"""


class ETHUSDTM23(Symbol):
    """
        name: ETHUSDTM23
        significant_digits: None
        tick_size: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSDTM23"
    significant_digits: int = None
    tick_size: int = 0.05
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHUSDTM23"

    def __str__(self):
        return "ETHUSDTM23"

    def __call__(self):
        return "ETHUSDTM23"


ETHUSDTM23 = ETHUSDTM23(*ETHUSDTM23._fields)
"""
    name: ETHUSDTM23
    significant_digits: None
    tick_size: 0.05
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""


class ETH_USDT(Symbol):
    """
        name: ETH_USDT
        significant_digits: None
        tick_size: 0.05
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETH_USDT"
    significant_digits: int = None
    tick_size: int = 0.05
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 1000000
    max_order_size: float = 10000000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH_USDT"

    def __str__(self):
        return "ETH_USDT"

    def __call__(self):
        return "ETH_USDT"


ETH_USDT = ETH_USDT(*ETH_USDT._fields)
"""
    name: ETH_USDT
    significant_digits: None
    tick_size: 0.05
    min_margin: None
    initial_margin: 1
    min_order_size: 1000000
    max_order_size: 10000000000000
    has_margin: True
    exchange: bitmex
"""


class ETH_XBT(Symbol):
    """
        name: ETH_XBT
        significant_digits: None
        tick_size: 1e-07
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 100000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETH_XBT"
    significant_digits: int = None
    tick_size: int = 1e-07
    min_margin: float = None
    initial_margin: float = 1
    min_order_size: float = 1000000
    max_order_size: float = 100000000000
    has_margin: bool = True
    exchange: str = "bitmex"

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH_XBT"

    def __str__(self):
        return "ETH_XBT"

    def __call__(self):
        return "ETH_XBT"


ETH_XBT = ETH_XBT(*ETH_XBT._fields)
"""
    name: ETH_XBT
    significant_digits: None
    tick_size: 1e-07
    min_margin: None
    initial_margin: 1
    min_order_size: 1000000
    max_order_size: 100000000000
    has_margin: True
    exchange: bitmex
"""


class LTCUSD(Symbol):
    """
        name: LTCUSD
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LTCUSD"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 0.02
    min_order_size: float = 1
    max_order_size: float = 100000000
    has_margin: bool = True
    exchange: str = "bitmex"

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


LTCUSD = LTCUSD(*LTCUSD._fields)
"""
    name: LTCUSD
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 0.02
    min_order_size: 1
    max_order_size: 100000000
    has_margin: True
    exchange: bitmex
"""


class LTCUSDT(Symbol):
    """
        name: LTCUSDT
        significant_digits: None
        tick_size: 0.01
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LTCUSDT"
    significant_digits: int = None
    tick_size: int = 0.01
    min_margin: float = None
    initial_margin: float = 0.03
    min_order_size: float = 1000
    max_order_size: float = 1000000000
    has_margin: bool = True
    exchange: str = "bitmex"

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
"""
    name: LTCUSDT
    significant_digits: None
    tick_size: 0.01
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""
