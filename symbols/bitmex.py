from typing import NamedTuple


class _EVOL7D(NamedTuple):
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


_EVOL7D = _EVOL7D()
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


class _BADAXBT(NamedTuple):
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


_BADAXBT = _BADAXBT()
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


class _BADAXBT30M(NamedTuple):
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


_BADAXBT30M = _BADAXBT30M()
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


class _BBCHXBT(NamedTuple):
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


_BBCHXBT = _BBCHXBT()
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


class _BBCHXBT30M(NamedTuple):
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


_BBCHXBT30M = _BBCHXBT30M()
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


class _BEOSXBT(NamedTuple):
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


_BEOSXBT = _BEOSXBT()
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


class _BEOSXBT30M(NamedTuple):
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


_BEOSXBT30M = _BEOSXBT30M()
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


class _BXRPXBT(NamedTuple):
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


_BXRPXBT = _BXRPXBT()
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


class _BXRPXBT30M(NamedTuple):
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


_BXRPXBT30M = _BXRPXBT30M()
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


class _BTRXXBT(NamedTuple):
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


_BTRXXBT = _BTRXXBT()
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


class _BTRXXBT30M(NamedTuple):
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


_BTRXXBT30M = _BTRXXBT30M()
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


class _BADAXBT_NEXT(NamedTuple):
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


_BADAXBT_NEXT = _BADAXBT_NEXT()
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


class _BBCHXBT_NEXT(NamedTuple):
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


_BBCHXBT_NEXT = _BBCHXBT_NEXT()
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


class _BEOSXBT_NEXT(NamedTuple):
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


_BEOSXBT_NEXT = _BEOSXBT_NEXT()
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


class _BTRXXBT_NEXT(NamedTuple):
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


_BTRXXBT_NEXT = _BTRXXBT_NEXT()
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


class _BXRPXBT_NEXT(NamedTuple):
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


_BXRPXBT_NEXT = _BXRPXBT_NEXT()
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


class _BXRP_NEXT(NamedTuple):
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


_BXRP_NEXT = _BXRP_NEXT()
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


class _BXRP(NamedTuple):
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


_BXRP = _BXRP()
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


class _XRPBON(NamedTuple):
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


_XRPBON = _XRPBON()
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


class _XRPBON8H(NamedTuple):
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


_XRPBON8H = _XRPBON8H()
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


class _XRPUSDPI(NamedTuple):
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


_XRPUSDPI = _XRPUSDPI()
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


class _XRPUSDPI8H(NamedTuple):
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


_XRPUSDPI8H = _XRPUSDPI8H()
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


class _BBCH(NamedTuple):
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


_BBCH = _BBCH()
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


class _BCHBON(NamedTuple):
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


_BCHBON = _BCHBON()
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


class _BCHBON8H(NamedTuple):
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


_BCHBON8H = _BCHBON8H()
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


class _BCHUSDPI(NamedTuple):
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


_BCHUSDPI = _BCHUSDPI()
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


class _BCHUSDPI8H(NamedTuple):
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


_BCHUSDPI8H = _BCHUSDPI8H()
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


class _BBCH_NEXT(NamedTuple):
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


_BBCH_NEXT = _BBCH_NEXT()
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


class _BUSDT(NamedTuple):
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


_BUSDT = _BUSDT()
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


class _BUSDT_NEXT(NamedTuple):
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


_BUSDT_NEXT = _BUSDT_NEXT()
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


class _BEOST(NamedTuple):
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


_BEOST = _BEOST()
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


class _BEOST_NEXT(NamedTuple):
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


_BEOST_NEXT = _BEOST_NEXT()
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


class _BEOST30M(NamedTuple):
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


_BEOST30M = _BEOST30M()
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


class _BLINKT(NamedTuple):
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


_BLINKT = _BLINKT()
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


class _BLINKT_NEXT(NamedTuple):
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


_BLINKT_NEXT = _BLINKT_NEXT()
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


class _BLINKT30M(NamedTuple):
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


_BLINKT30M = _BLINKT30M()
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


class _BADAT(NamedTuple):
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


_BADAT = _BADAT()
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


class _BADAT_NEXT(NamedTuple):
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


_BADAT_NEXT = _BADAT_NEXT()
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


class _BADAT30M(NamedTuple):
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


_BADAT30M = _BADAT30M()
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


class _BXTZT(NamedTuple):
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


_BXTZT = _BXTZT()
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


class _BXTZT_NEXT(NamedTuple):
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


_BXTZT_NEXT = _BXTZT_NEXT()
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


class _BXTZT30M(NamedTuple):
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


_BXTZT30M = _BXTZT30M()
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


class _LINKBON(NamedTuple):
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


_LINKBON = _LINKBON()
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


class _LINKBON8H(NamedTuple):
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


_LINKBON8H = _LINKBON8H()
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


class _LINKUSDTPI(NamedTuple):
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


_LINKUSDTPI = _LINKUSDTPI()
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


class _LINKUSDTPI8H(NamedTuple):
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


_LINKUSDTPI8H = _LINKUSDTPI8H()
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


class _USDTBON(NamedTuple):
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


_USDTBON = _USDTBON()
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


class _USDTBON8H(NamedTuple):
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


_USDTBON8H = _USDTBON8H()
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


class _BBNBT(NamedTuple):
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


_BBNBT = _BBNBT()
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


class _BBNBT_NEXT(NamedTuple):
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


_BBNBT_NEXT = _BBNBT_NEXT()
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


class _BBNBT30M(NamedTuple):
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


_BBNBT30M = _BBNBT30M()
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


class _BDOTT(NamedTuple):
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


_BDOTT = _BDOTT()
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


class _BDOTT_NEXT(NamedTuple):
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


_BDOTT_NEXT = _BDOTT_NEXT()
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


class _BDOTT30M(NamedTuple):
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


_BDOTT30M = _BDOTT30M()
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


class _BYFIT(NamedTuple):
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


_BYFIT = _BYFIT()
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


class _BYFIT_NEXT(NamedTuple):
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


_BYFIT_NEXT = _BYFIT_NEXT()
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


class _BYFIT30M(NamedTuple):
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


_BYFIT30M = _BYFIT30M()
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


class _BDOGET(NamedTuple):
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


_BDOGET = _BDOGET()
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


class _BDOGET_NEXT(NamedTuple):
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


_BDOGET_NEXT = _BDOGET_NEXT()
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


class _DOGEBON(NamedTuple):
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


_DOGEBON = _DOGEBON()
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


class _DOGEBON8H(NamedTuple):
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


_DOGEBON8H = _DOGEBON8H()
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


class _DOGEUSDTPI(NamedTuple):
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


_DOGEUSDTPI = _DOGEUSDTPI()
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


class _DOGEUSDTPI8H(NamedTuple):
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


_DOGEUSDTPI8H = _DOGEUSDTPI8H()
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


class _BNBBON(NamedTuple):
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


_BNBBON = _BNBBON()
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


class _BNBBON8H(NamedTuple):
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


_BNBBON8H = _BNBBON8H()
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


class _BNBUSDTPI(NamedTuple):
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


_BNBUSDTPI = _BNBUSDTPI()
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


class _BNBUSDTPI8H(NamedTuple):
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


_BNBUSDTPI8H = _BNBUSDTPI8H()
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


class _ADABON(NamedTuple):
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


_ADABON = _ADABON()
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


class _ADABON8H(NamedTuple):
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


_ADABON8H = _ADABON8H()
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


class _ADAUSDTPI(NamedTuple):
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


_ADAUSDTPI = _ADAUSDTPI()
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


class _ADAUSDTPI8H(NamedTuple):
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


_ADAUSDTPI8H = _ADAUSDTPI8H()
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


class _DOTBON(NamedTuple):
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


_DOTBON = _DOTBON()
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


class _DOTBON8H(NamedTuple):
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


_DOTBON8H = _DOTBON8H()
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


class _DOTUSDTPI(NamedTuple):
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


_DOTUSDTPI = _DOTUSDTPI()
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


class _DOTUSDTPI8H(NamedTuple):
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


_DOTUSDTPI8H = _DOTUSDTPI8H()
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


class _EOSBON(NamedTuple):
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


_EOSBON = _EOSBON()
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


class _EOSBON8H(NamedTuple):
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


_EOSBON8H = _EOSBON8H()
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


class _EOSUSDTPI(NamedTuple):
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


_EOSUSDTPI = _EOSUSDTPI()
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


class _EOSUSDTPI8H(NamedTuple):
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


_EOSUSDTPI8H = _EOSUSDTPI8H()
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


class _XTZBON(NamedTuple):
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


_XTZBON = _XTZBON()
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


class _XTZBON8H(NamedTuple):
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


_XTZBON8H = _XTZBON8H()
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


class _XTZUSDTPI(NamedTuple):
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


_XTZUSDTPI = _XTZUSDTPI()
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


class _YFIBON(NamedTuple):
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


_YFIBON = _YFIBON()
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


class _YFIBON8H(NamedTuple):
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


_YFIBON8H = _YFIBON8H()
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


class _YFIUSDTPI(NamedTuple):
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


_YFIUSDTPI = _YFIUSDTPI()
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


class _BAAVET(NamedTuple):
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


_BAAVET = _BAAVET()
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


class _BAAVET_NEXT(NamedTuple):
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


_BAAVET_NEXT = _BAAVET_NEXT()
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


class _AAVEBON(NamedTuple):
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


_AAVEBON = _AAVEBON()
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


class _AAVEBON8H(NamedTuple):
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


_AAVEBON8H = _AAVEBON8H()
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


class _AAVEUSDTPI(NamedTuple):
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


_AAVEUSDTPI = _AAVEUSDTPI()
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


class _AAVEUSDTPI8H(NamedTuple):
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


_AAVEUSDTPI8H = _AAVEUSDTPI8H()
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


class _BUNIT(NamedTuple):
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


_BUNIT = _BUNIT()
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


class _BUNIT_NEXT(NamedTuple):
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


_BUNIT_NEXT = _BUNIT_NEXT()
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


class _UNIBON(NamedTuple):
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


_UNIBON = _UNIBON()
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


class _UNIBON8H(NamedTuple):
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


_UNIBON8H = _UNIBON8H()
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


class _UNIUSDTPI(NamedTuple):
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


_UNIUSDTPI = _UNIUSDTPI()
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


class _UNIUSDTPI8H(NamedTuple):
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


_UNIUSDTPI8H = _UNIUSDTPI8H()
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


class _BXLMT(NamedTuple):
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


_BXLMT = _BXLMT()
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


class _BXLMT_NEXT(NamedTuple):
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


_BXLMT_NEXT = _BXLMT_NEXT()
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


class _XLMBON(NamedTuple):
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


_XLMBON = _XLMBON()
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


class _XLMBON8H(NamedTuple):
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


_XLMBON8H = _XLMBON8H()
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


class _XLMUSDTPI(NamedTuple):
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


_XLMUSDTPI = _XLMUSDTPI()
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


class _XLMUSDTPI8H(NamedTuple):
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


_XLMUSDTPI8H = _XLMUSDTPI8H()
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


class _BTRXT(NamedTuple):
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


_BTRXT = _BTRXT()
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


class _BTRXT_NEXT(NamedTuple):
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


_BTRXT_NEXT = _BTRXT_NEXT()
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


class _TRXBON(NamedTuple):
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


_TRXBON = _TRXBON()
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


class _TRXBON8H(NamedTuple):
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


_TRXBON8H = _TRXBON8H()
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


class _TRXUSDTPI(NamedTuple):
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


_TRXUSDTPI = _TRXUSDTPI()
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


class _TRXUSDTPI8H(NamedTuple):
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


_TRXUSDTPI8H = _TRXUSDTPI8H()
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


class _BTRXT30M(NamedTuple):
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


_BTRXT30M = _BTRXT30M()
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


class _BSOLT(NamedTuple):
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


_BSOLT = _BSOLT()
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


class _BSOLT_NEXT(NamedTuple):
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


_BSOLT_NEXT = _BSOLT_NEXT()
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


class _SOLBON(NamedTuple):
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


_SOLBON = _SOLBON()
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


class _SOLBON8H(NamedTuple):
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


_SOLBON8H = _SOLBON8H()
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


class _SOLUSDTPI(NamedTuple):
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


_SOLUSDTPI = _SOLUSDTPI()
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


class _SOLUSDTPI8H(NamedTuple):
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


_SOLUSDTPI8H = _SOLUSDTPI8H()
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


class _BFILT(NamedTuple):
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


_BFILT = _BFILT()
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


class _BFILT_NEXT(NamedTuple):
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


_BFILT_NEXT = _BFILT_NEXT()
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


class _FILBON(NamedTuple):
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


_FILBON = _FILBON()
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


class _FILBON8H(NamedTuple):
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


_FILBON8H = _FILBON8H()
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


class _FILUSDTPI(NamedTuple):
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


_FILUSDTPI = _FILUSDTPI()
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


class _FILUSDTPI8H(NamedTuple):
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


_FILUSDTPI8H = _FILUSDTPI8H()
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


class _EURBON(NamedTuple):
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


_EURBON = _EURBON()
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


class _EURBON8H(NamedTuple):
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


_EURBON8H = _EURBON8H()
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


class _BVETT(NamedTuple):
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


_BVETT = _BVETT()
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


class _BVETT_NEXT(NamedTuple):
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


_BVETT_NEXT = _BVETT_NEXT()
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


class _VETBON(NamedTuple):
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


_VETBON = _VETBON()
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


class _VETBON8H(NamedTuple):
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


_VETBON8H = _VETBON8H()
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


class _VETUSDTPI(NamedTuple):
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


_VETUSDTPI = _VETUSDTPI()
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


class _VETUSDTPI8H(NamedTuple):
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


_VETUSDTPI8H = _VETUSDTPI8H()
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


class _BMATICT(NamedTuple):
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


_BMATICT = _BMATICT()
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


class _BMATICT_NEXT(NamedTuple):
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


_BMATICT_NEXT = _BMATICT_NEXT()
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


class _MATICBON(NamedTuple):
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


_MATICBON = _MATICBON()
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


class _MATICBON8H(NamedTuple):
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


_MATICBON8H = _MATICBON8H()
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


class _MATICUSDTPI(NamedTuple):
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


_MATICUSDTPI = _MATICUSDTPI()
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


class _MATICUSDTPI8H(NamedTuple):
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


_MATICUSDTPI8H = _MATICUSDTPI8H()
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


class _BMKRT(NamedTuple):
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


_BMKRT = _BMKRT()
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


class _BMKRT_NEXT(NamedTuple):
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


_BMKRT_NEXT = _BMKRT_NEXT()
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


class _BAVAXT(NamedTuple):
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


_BAVAXT = _BAVAXT()
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


class _BAVAXT_NEXT(NamedTuple):
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


_BAVAXT_NEXT = _BAVAXT_NEXT()
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


class _BLUNAT(NamedTuple):
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


_BLUNAT = _BLUNAT()
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


class _BLUNAT_NEXT(NamedTuple):
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


_BLUNAT_NEXT = _BLUNAT_NEXT()
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


class _BCOMPT(NamedTuple):
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


_BCOMPT = _BCOMPT()
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


class _BCOMPT_NEXT(NamedTuple):
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


_BCOMPT_NEXT = _BCOMPT_NEXT()
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


class _BSUSHIT(NamedTuple):
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


_BSUSHIT = _BSUSHIT()
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


class _BSUSHIT_NEXT(NamedTuple):
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


_BSUSHIT_NEXT = _BSUSHIT_NEXT()
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


class _BGRTT(NamedTuple):
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


_BGRTT = _BGRTT()
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


class _BGRTT_NEXT(NamedTuple):
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


_BGRTT_NEXT = _BGRTT_NEXT()
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


class _BALTMEX(NamedTuple):
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


_BALTMEX = _BALTMEX()
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


class _BDEFIMEX(NamedTuple):
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


_BDEFIMEX = _BDEFIMEX()
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


class _ALTMEXBON(NamedTuple):
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


_ALTMEXBON = _ALTMEXBON()
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


class _ALTMEXBON8H(NamedTuple):
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


_ALTMEXBON8H = _ALTMEXBON8H()
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


class _ALTMEXUSDPI(NamedTuple):
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


_ALTMEXUSDPI = _ALTMEXUSDPI()
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


class _ALTMEXUSDPI8H(NamedTuple):
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


_ALTMEXUSDPI8H = _ALTMEXUSDPI8H()
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


class _DEFIMEXBON(NamedTuple):
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


_DEFIMEXBON = _DEFIMEXBON()
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


class _DEFIMEXBON8H(NamedTuple):
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


_DEFIMEXBON8H = _DEFIMEXBON8H()
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


class _DEFIMEXUSDPI(NamedTuple):
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


_DEFIMEXUSDPI = _DEFIMEXUSDPI()
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


class _DEFIMEXUSDPI8H(NamedTuple):
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


_DEFIMEXUSDPI8H = _DEFIMEXUSDPI8H()
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


class _SUSHIBON(NamedTuple):
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


_SUSHIBON = _SUSHIBON()
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


class _SUSHIBON8H(NamedTuple):
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


_SUSHIBON8H = _SUSHIBON8H()
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


class _SUSHIUSDTPI(NamedTuple):
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


_SUSHIUSDTPI = _SUSHIUSDTPI()
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


class _SUSHIUSDTPI8H(NamedTuple):
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


_SUSHIUSDTPI8H = _SUSHIUSDTPI8H()
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


class _BAXST(NamedTuple):
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


_BAXST = _BAXST()
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


class _BAXST_NEXT(NamedTuple):
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


_BAXST_NEXT = _BAXST_NEXT()
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


class _AXSBON(NamedTuple):
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


_AXSBON = _AXSBON()
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


class _AXSBON8H(NamedTuple):
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


_AXSBON8H = _AXSBON8H()
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


class _AXSUSDTPI(NamedTuple):
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


_AXSUSDTPI = _AXSUSDTPI()
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


class _AXSUSDTPI8H(NamedTuple):
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


_AXSUSDTPI8H = _AXSUSDTPI8H()
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


class _BSRMT(NamedTuple):
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


_BSRMT = _BSRMT()
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


class _BSRMT_NEXT(NamedTuple):
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


_BSRMT_NEXT = _BSRMT_NEXT()
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


class _SRMBON(NamedTuple):
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


_SRMBON = _SRMBON()
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


class _SRMBON8H(NamedTuple):
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


_SRMBON8H = _SRMBON8H()
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


class _SRMUSDTPI(NamedTuple):
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


_SRMUSDTPI = _SRMUSDTPI()
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


class _SRMUSDTPI8H(NamedTuple):
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


_SRMUSDTPI8H = _SRMUSDTPI8H()
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


class _BLUNA(NamedTuple):
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


_BLUNA = _BLUNA()
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


class _BLUNA_NEXT(NamedTuple):
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


_BLUNA_NEXT = _BLUNA_NEXT()
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


class _LUNABON(NamedTuple):
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


_LUNABON = _LUNABON()
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


class _LUNABON8H(NamedTuple):
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


_LUNABON8H = _LUNABON8H()
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


class _LUNAUSDPI(NamedTuple):
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


_LUNAUSDPI = _LUNAUSDPI()
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


class _LUNAUSDPI8H(NamedTuple):
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


_LUNAUSDPI8H = _LUNAUSDPI8H()
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


class _AVAXBON(NamedTuple):
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


_AVAXBON = _AVAXBON()
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


class _AVAXBON8H(NamedTuple):
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


_AVAXBON8H = _AVAXBON8H()
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


class _BAVAX(NamedTuple):
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


_BAVAX = _BAVAX()
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


class _BAVAX_NEXT(NamedTuple):
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


_BAVAX_NEXT = _BAVAX_NEXT()
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


class _AVAXUSDPI(NamedTuple):
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


_AVAXUSDPI = _AVAXUSDPI()
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


class _AVAXUSDPI8H(NamedTuple):
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


_AVAXUSDPI8H = _AVAXUSDPI8H()
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


class _BADA(NamedTuple):
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


_BADA = _BADA()
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


class _BADA_NEXT(NamedTuple):
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


_BADA_NEXT = _BADA_NEXT()
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


class _ADAUSDPI(NamedTuple):
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


_ADAUSDPI = _ADAUSDPI()
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


class _ADAUSDPI8H(NamedTuple):
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


_ADAUSDPI8H = _ADAUSDPI8H()
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


class _BDOGE(NamedTuple):
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


_BDOGE = _BDOGE()
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


class _BDOGE_NEXT(NamedTuple):
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


_BDOGE_NEXT = _BDOGE_NEXT()
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


class _DOGEUSDPI(NamedTuple):
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


_DOGEUSDPI = _DOGEUSDPI()
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


class _DOGEUSDPI8H(NamedTuple):
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


_DOGEUSDPI8H = _DOGEUSDPI8H()
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


class _BBNB(NamedTuple):
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


_BBNB = _BBNB()
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


class _BBNB_NEXT(NamedTuple):
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


_BBNB_NEXT = _BBNB_NEXT()
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


class _BNBUSDPI(NamedTuple):
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


_BNBUSDPI = _BNBUSDPI()
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


class _BNBUSDPI8H(NamedTuple):
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


_BNBUSDPI8H = _BNBUSDPI8H()
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


class _BDOT(NamedTuple):
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


_BDOT = _BDOT()
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


class _BDOT_NEXT(NamedTuple):
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


_BDOT_NEXT = _BDOT_NEXT()
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


class _DOTUSDPI(NamedTuple):
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


_DOTUSDPI = _DOTUSDPI()
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


class _DOTUSDPI8H(NamedTuple):
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


_DOTUSDPI8H = _DOTUSDPI8H()
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


class _BDOGET30M(NamedTuple):
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


_BDOGET30M = _BDOGET30M()
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


class _BFILT30M(NamedTuple):
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


_BFILT30M = _BFILT30M()
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


class _BUNIT30M(NamedTuple):
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


_BUNIT30M = _BUNIT30M()
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


class _BXLMT30M(NamedTuple):
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


_BXLMT30M = _BXLMT30M()
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


class _BAXS(NamedTuple):
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


_BAXS = _BAXS()
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


class _BAXS_NEXT(NamedTuple):
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


_BAXS_NEXT = _BAXS_NEXT()
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


class _AXSUSDPI(NamedTuple):
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


_AXSUSDPI = _AXSUSDPI()
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


class _AXSUSDPI8H(NamedTuple):
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


_AXSUSDPI8H = _AXSUSDPI8H()
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


class _BEOS(NamedTuple):
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


_BEOS = _BEOS()
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


class _BEOS_NEXT(NamedTuple):
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


_BEOS_NEXT = _BEOS_NEXT()
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


class _EOSUSDPI(NamedTuple):
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


_EOSUSDPI = _EOSUSDPI()
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


class _EOSUSDPI8H(NamedTuple):
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


_EOSUSDPI8H = _EOSUSDPI8H()
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


class _BLINK(NamedTuple):
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


_BLINK = _BLINK()
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


class _BLINK_NEXT(NamedTuple):
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


_BLINK_NEXT = _BLINK_NEXT()
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


class _LINKUSDPI(NamedTuple):
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


_LINKUSDPI = _LINKUSDPI()
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


class _LINKUSDPI8H(NamedTuple):
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


_LINKUSDPI8H = _LINKUSDPI8H()
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


class _BSOL(NamedTuple):
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


_BSOL = _BSOL()
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


class _BSOL_NEXT(NamedTuple):
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


_BSOL_NEXT = _BSOL_NEXT()
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


class _SOLUSDPI(NamedTuple):
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


_SOLUSDPI = _SOLUSDPI()
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


class _SOLUSDPI8H(NamedTuple):
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


_SOLUSDPI8H = _SOLUSDPI8H()
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


class _BAXST30M(NamedTuple):
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


_BAXST30M = _BAXST30M()
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


class _BSOLT30M(NamedTuple):
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


_BSOLT30M = _BSOLT30M()
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


class _BVETT30M(NamedTuple):
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


_BVETT30M = _BVETT30M()
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


class _BMATICT30M(NamedTuple):
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


_BMATICT30M = _BMATICT30M()
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


class _BAAVET30M(NamedTuple):
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


_BAAVET30M = _BAAVET30M()
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


class _BSUSHIT30M(NamedTuple):
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


_BSUSHIT30M = _BSUSHIT30M()
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


class _BSRMT30M(NamedTuple):
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


_BSRMT30M = _BSRMT30M()
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


class _BXRPT(NamedTuple):
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


_BXRPT = _BXRPT()
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


class _BXRPT_NEXT(NamedTuple):
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


_BXRPT_NEXT = _BXRPT_NEXT()
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


class _BBCHT(NamedTuple):
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


_BBCHT = _BBCHT()
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


class _BBCHT_NEXT(NamedTuple):
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


_BBCHT_NEXT = _BBCHT_NEXT()
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


class _XRPUSDTPI(NamedTuple):
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


_XRPUSDTPI = _XRPUSDTPI()
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


class _XRPUSDTPI8H(NamedTuple):
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


_XRPUSDTPI8H = _XRPUSDTPI8H()
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


class _BCHUSDTPI(NamedTuple):
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


_BCHUSDTPI = _BCHUSDTPI()
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


class _BCHUSDTPI8H(NamedTuple):
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


_BCHUSDTPI8H = _BCHUSDTPI8H()
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


class _BDEFIMEX30M(NamedTuple):
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


_BDEFIMEX30M = _BDEFIMEX30M()
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


class _BALTMEX30M(NamedTuple):
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


_BALTMEX30M = _BALTMEX30M()
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


class _BFTMT(NamedTuple):
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


_BFTMT = _BFTMT()
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


class _BFTMT_NEXT(NamedTuple):
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


_BFTMT_NEXT = _BFTMT_NEXT()
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


class _FTMBON(NamedTuple):
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


_FTMBON = _FTMBON()
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


class _FTMBON8H(NamedTuple):
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


_FTMBON8H = _FTMBON8H()
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


class _FTMUSDTPI(NamedTuple):
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


_FTMUSDTPI = _FTMUSDTPI()
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


class _FTMUSDTPI8H(NamedTuple):
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


_FTMUSDTPI8H = _FTMUSDTPI8H()
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


class _BSHIBT(NamedTuple):
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


_BSHIBT = _BSHIBT()
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


class _BSHIBT_NEXT(NamedTuple):
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


_BSHIBT_NEXT = _BSHIBT_NEXT()
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


class _SHIBBON(NamedTuple):
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


_SHIBBON = _SHIBBON()
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


class _SHIBBON8H(NamedTuple):
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


_SHIBBON8H = _SHIBBON8H()
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


class _SHIBUSDTPI(NamedTuple):
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


_SHIBUSDTPI = _SHIBUSDTPI()
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


class _SHIBUSDTPI8H(NamedTuple):
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


_SHIBUSDTPI8H = _SHIBUSDTPI8H()
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


class _BLRCT(NamedTuple):
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


_BLRCT = _BLRCT()
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


class _BLRCT_NEXT(NamedTuple):
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


_BLRCT_NEXT = _BLRCT_NEXT()
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


class _BMANAT(NamedTuple):
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


_BMANAT = _BMANAT()
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


class _BMANAT_NEXT(NamedTuple):
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


_BMANAT_NEXT = _BMANAT_NEXT()
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


class _MANABON(NamedTuple):
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


_MANABON = _MANABON()
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


class _MANABON8H(NamedTuple):
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


_MANABON8H = _MANABON8H()
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


class _MANAUSDTPI(NamedTuple):
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


_MANAUSDTPI = _MANAUSDTPI()
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


class _MANAUSDTPI8H(NamedTuple):
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


_MANAUSDTPI8H = _MANAUSDTPI8H()
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


class _BSANDT(NamedTuple):
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


_BSANDT = _BSANDT()
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


class _BSANDT_NEXT(NamedTuple):
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


_BSANDT_NEXT = _BSANDT_NEXT()
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


class _SANDBON(NamedTuple):
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


_SANDBON = _SANDBON()
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


class _SANDBON8H(NamedTuple):
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


_SANDBON8H = _SANDBON8H()
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


class _SANDUSDTPI(NamedTuple):
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


_SANDUSDTPI = _SANDUSDTPI()
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


class _SANDUSDTPI8H(NamedTuple):
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


_SANDUSDTPI8H = _SANDUSDTPI8H()
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


class _BTHETAT(NamedTuple):
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


_BTHETAT = _BTHETAT()
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


class _BTHETAT_NEXT(NamedTuple):
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


_BTHETAT_NEXT = _BTHETAT_NEXT()
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


class _BENJT(NamedTuple):
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


_BENJT = _BENJT()
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


class _BENJT_NEXT(NamedTuple):
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


_BENJT_NEXT = _BENJT_NEXT()
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


class _BDEFIMEXT(NamedTuple):
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


_BDEFIMEXT = _BDEFIMEXT()
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


class _DEFIMEXTBON(NamedTuple):
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


_DEFIMEXTBON = _DEFIMEXTBON()
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


class _DEFIMEXTBON8H(NamedTuple):
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


_DEFIMEXTBON8H = _DEFIMEXTBON8H()
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


class _DEFIMEXTUSDTPI(NamedTuple):
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


_DEFIMEXTUSDTPI = _DEFIMEXTUSDTPI()
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


class _DEFIMEXTUSDTPI8H(NamedTuple):
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


_DEFIMEXTUSDTPI8H = _DEFIMEXTUSDTPI8H()
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


class _BALTMEXT(NamedTuple):
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


_BALTMEXT = _BALTMEXT()
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


class _ALTMEXTBON(NamedTuple):
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


_ALTMEXTBON = _ALTMEXTBON()
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


class _ALTMEXTBON8H(NamedTuple):
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


_ALTMEXTBON8H = _ALTMEXTBON8H()
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


class _ALTMEXTUSDTPI(NamedTuple):
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


_ALTMEXTUSDTPI = _ALTMEXTUSDTPI()
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


class _ALTMEXTUSDTPI8H(NamedTuple):
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


_ALTMEXTUSDTPI8H = _ALTMEXTUSDTPI8H()
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


class _BMETAMEXT(NamedTuple):
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


_BMETAMEXT = _BMETAMEXT()
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


class _METAMEXTBON(NamedTuple):
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


_METAMEXTBON = _METAMEXTBON()
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


class _METAMEXTBON8H(NamedTuple):
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


_METAMEXTBON8H = _METAMEXTBON8H()
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


class _METAMEXTUSDTPI(NamedTuple):
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


_METAMEXTUSDTPI = _METAMEXTUSDTPI()
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


class _METAMEXTUSDTPI8H(NamedTuple):
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


_METAMEXTUSDTPI8H = _METAMEXTUSDTPI8H()
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


class _AVAXUSDTPI(NamedTuple):
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


_AVAXUSDTPI = _AVAXUSDTPI()
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


class _AVAXUSDTPI8H(NamedTuple):
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


_AVAXUSDTPI8H = _AVAXUSDTPI8H()
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


class _LUNAUSDTPI(NamedTuple):
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


_LUNAUSDTPI = _LUNAUSDTPI()
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


class _LUNAUSDTPI8H(NamedTuple):
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


_LUNAUSDTPI8H = _LUNAUSDTPI8H()
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


class _BAPET(NamedTuple):
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


_BAPET = _BAPET()
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


class _BAPET_NEXT(NamedTuple):
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


_BAPET_NEXT = _BAPET_NEXT()
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


class _APEBON(NamedTuple):
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


_APEBON = _APEBON()
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


class _APEBON8H(NamedTuple):
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


_APEBON8H = _APEBON8H()
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


class _APEUSDTPI(NamedTuple):
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


_APEUSDTPI = _APEUSDTPI()
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


class _APEUSDTPI8H(NamedTuple):
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


_APEUSDTPI8H = _APEUSDTPI8H()
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


class _GMTBON(NamedTuple):
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


_GMTBON = _GMTBON()
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


class _GMTBON8H(NamedTuple):
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


_GMTBON8H = _GMTBON8H()
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


class _GMTUSDTPI(NamedTuple):
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


_GMTUSDTPI = _GMTUSDTPI()
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


class _GMTUSDTPI8H(NamedTuple):
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


_GMTUSDTPI8H = _GMTUSDTPI8H()
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


class _GMTUSDPI(NamedTuple):
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


_GMTUSDPI = _GMTUSDPI()
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


class _GMTUSDPI8H(NamedTuple):
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


_GMTUSDPI8H = _GMTUSDPI8H()
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


class _BGMT(NamedTuple):
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


_BGMT = _BGMT()
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


class _BGMT_NEXT(NamedTuple):
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


_BGMT_NEXT = _BGMT_NEXT()
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


class _BGMTT(NamedTuple):
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


_BGMTT = _BGMTT()
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


class _BGMTT_NEXT(NamedTuple):
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


_BGMTT_NEXT = _BGMTT_NEXT()
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


class _NEARBON(NamedTuple):
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


_NEARBON = _NEARBON()
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


class _NEARBON8H(NamedTuple):
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


_NEARBON8H = _NEARBON8H()
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


class _NEARUSDTPI(NamedTuple):
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


_NEARUSDTPI = _NEARUSDTPI()
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


class _NEARUSDTPI8H(NamedTuple):
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


_NEARUSDTPI8H = _NEARUSDTPI8H()
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


class _NEARUSDPI(NamedTuple):
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


_NEARUSDPI = _NEARUSDPI()
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


class _NEARUSDPI8H(NamedTuple):
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


_NEARUSDPI8H = _NEARUSDPI8H()
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


class _BNEAR(NamedTuple):
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


_BNEAR = _BNEAR()
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


class _BNEAR_NEXT(NamedTuple):
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


_BNEAR_NEXT = _BNEAR_NEXT()
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


class _BNEART(NamedTuple):
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


_BNEART = _BNEART()
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


class _BNEART_NEXT(NamedTuple):
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


_BNEART_NEXT = _BNEART_NEXT()
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


class _BLUNA30M(NamedTuple):
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


_BLUNA30M = _BLUNA30M()
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


class _BLUNAT30M(NamedTuple):
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


_BLUNAT30M = _BLUNAT30M()
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


class _BAPE(NamedTuple):
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


_BAPE = _BAPE()
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


class _BAPE_NEXT(NamedTuple):
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


_BAPE_NEXT = _BAPE_NEXT()
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


class _BTRX(NamedTuple):
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


_BTRX = _BTRX()
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


class _BTRX_NEXT(NamedTuple):
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


_BTRX_NEXT = _BTRX_NEXT()
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


class _BGAL(NamedTuple):
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


_BGAL = _BGAL()
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


class _BGAL_NEXT(NamedTuple):
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


_BGAL_NEXT = _BGAL_NEXT()
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


class _BGALT(NamedTuple):
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


_BGALT = _BGALT()
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


class _BGALT_NEXT(NamedTuple):
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


_BGALT_NEXT = _BGALT_NEXT()
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


class _GALBON(NamedTuple):
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


_GALBON = _GALBON()
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


class _GALBON8H(NamedTuple):
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


_GALBON8H = _GALBON8H()
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


class _APEUSDPI(NamedTuple):
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


_APEUSDPI = _APEUSDPI()
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


class _APEUSDPI8H(NamedTuple):
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


_APEUSDPI8H = _APEUSDPI8H()
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


class _TRXUSDPI(NamedTuple):
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


_TRXUSDPI = _TRXUSDPI()
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


class _TRXUSDPI8H(NamedTuple):
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


_TRXUSDPI8H = _TRXUSDPI8H()
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


class _GALUSDTPI(NamedTuple):
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


_GALUSDTPI = _GALUSDTPI()
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


class _GALUSDTPI8H(NamedTuple):
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


_GALUSDTPI8H = _GALUSDTPI8H()
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


class _GALUSDPI(NamedTuple):
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


_GALUSDPI = _GALUSDPI()
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


class _GALUSDPI8H(NamedTuple):
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


_GALUSDPI8H = _GALUSDPI8H()
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


class _BLUNC(NamedTuple):
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


_BLUNC = _BLUNC()
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


class _BLUNC_NEXT(NamedTuple):
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


_BLUNC_NEXT = _BLUNC_NEXT()
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


class _BLUNCT(NamedTuple):
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


_BLUNCT = _BLUNCT()
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


class _BLUNCT_NEXT(NamedTuple):
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


_BLUNCT_NEXT = _BLUNCT_NEXT()
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


class _BDFI(NamedTuple):
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


_BDFI = _BDFI()
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


class _BDFIT(NamedTuple):
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


_BDFIT = _BDFIT()
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


class _BGRT(NamedTuple):
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


_BGRT = _BGRT()
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


class _EURUSDPI(NamedTuple):
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


_EURUSDPI = _EURUSDPI()
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


class _USDCHFPI(NamedTuple):
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


_USDCHFPI = _USDCHFPI()
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


class _EURCHFPI(NamedTuple):
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


_EURCHFPI = _EURCHFPI()
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


class _EURTRYPI(NamedTuple):
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


_EURTRYPI = _EURTRYPI()
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


class _USDTRYPI(NamedTuple):
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


_USDTRYPI = _USDTRYPI()
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


class _USDINRPI(NamedTuple):
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


_USDINRPI = _USDINRPI()
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


class _USDZARPI(NamedTuple):
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


_USDZARPI = _USDZARPI()
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


class _USDBRLPI(NamedTuple):
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


_USDBRLPI = _USDBRLPI()
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


class _USDMXNPI(NamedTuple):
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


_USDMXNPI = _USDMXNPI()
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


class _NZDUSDPI(NamedTuple):
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


_NZDUSDPI = _NZDUSDPI()
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


class _USDCNHPI(NamedTuple):
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


_USDCNHPI = _USDCNHPI()
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


class _USDSEKPI(NamedTuple):
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


_USDSEKPI = _USDSEKPI()
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


class _EURUSDPI8H(NamedTuple):
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


_EURUSDPI8H = _EURUSDPI8H()
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


class _USDCHFPI8H(NamedTuple):
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


_USDCHFPI8H = _USDCHFPI8H()
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


class _EURCHFPI8H(NamedTuple):
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


_EURCHFPI8H = _EURCHFPI8H()
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


class _EURTRYPI8H(NamedTuple):
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


_EURTRYPI8H = _EURTRYPI8H()
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


class _USDTRYPI8H(NamedTuple):
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


_USDTRYPI8H = _USDTRYPI8H()
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


class _USDINRPI8H(NamedTuple):
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


_USDINRPI8H = _USDINRPI8H()
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


class _USDZARPI8H(NamedTuple):
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


_USDZARPI8H = _USDZARPI8H()
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


class _USDBRLPI8H(NamedTuple):
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


_USDBRLPI8H = _USDBRLPI8H()
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


class _USDMXNPI8H(NamedTuple):
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


_USDMXNPI8H = _USDMXNPI8H()
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


class _NZDUSDPI8H(NamedTuple):
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


_NZDUSDPI8H = _NZDUSDPI8H()
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


class _USDCNHPI8H(NamedTuple):
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


_USDCNHPI8H = _USDCNHPI8H()
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


class _USDSEKPI8H(NamedTuple):
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


_USDSEKPI8H = _USDSEKPI8H()
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


class _EURUSDTPI(NamedTuple):
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


_EURUSDTPI = _EURUSDTPI()
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


class _USDTCHFPI(NamedTuple):
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


_USDTCHFPI = _USDTCHFPI()
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


class _USDTTRYPI(NamedTuple):
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


_USDTTRYPI = _USDTTRYPI()
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


class _USDTINRPI(NamedTuple):
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


_USDTINRPI = _USDTINRPI()
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


class _USDTZARPI(NamedTuple):
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


_USDTZARPI = _USDTZARPI()
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


class _USDTBRLPI(NamedTuple):
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


_USDTBRLPI = _USDTBRLPI()
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


class _USDTMXNPI(NamedTuple):
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


_USDTMXNPI = _USDTMXNPI()
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


class _NZDUSDTPI(NamedTuple):
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


_NZDUSDTPI = _NZDUSDTPI()
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


class _USDTCNHPI(NamedTuple):
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


_USDTCNHPI = _USDTCNHPI()
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


class _USDTSEKPI(NamedTuple):
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


_USDTSEKPI = _USDTSEKPI()
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


class _EURUSDTPI8H(NamedTuple):
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


_EURUSDTPI8H = _EURUSDTPI8H()
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


class _USDTCHFPI8H(NamedTuple):
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


_USDTCHFPI8H = _USDTCHFPI8H()
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


class _USDTTRYPI8H(NamedTuple):
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


_USDTTRYPI8H = _USDTTRYPI8H()
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


class _USDTINRPI8H(NamedTuple):
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


_USDTINRPI8H = _USDTINRPI8H()
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


class _USDTZARPI8H(NamedTuple):
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


_USDTZARPI8H = _USDTZARPI8H()
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


class _USDTBRLPI8H(NamedTuple):
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


_USDTBRLPI8H = _USDTBRLPI8H()
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


class _USDTMXNPI8H(NamedTuple):
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


_USDTMXNPI8H = _USDTMXNPI8H()
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


class _NZDUSDTPI8H(NamedTuple):
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


_NZDUSDTPI8H = _NZDUSDTPI8H()
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


class _USDTCNHPI8H(NamedTuple):
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


_USDTCNHPI8H = _USDTCNHPI8H()
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


class _USDTSEKPI8H(NamedTuple):
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


_USDTSEKPI8H = _USDTSEKPI8H()
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


class _CHFBON(NamedTuple):
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


_CHFBON = _CHFBON()
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


class _TRYBON(NamedTuple):
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


_TRYBON = _TRYBON()
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


class _INRBON(NamedTuple):
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


_INRBON = _INRBON()
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


class _ZARBON(NamedTuple):
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


_ZARBON = _ZARBON()
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


class _BRLBON(NamedTuple):
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


_BRLBON = _BRLBON()
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


class _MXNBON(NamedTuple):
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


_MXNBON = _MXNBON()
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


class _NZDBON(NamedTuple):
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


_NZDBON = _NZDBON()
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


class _CNHBON(NamedTuple):
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


_CNHBON = _CNHBON()
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


class _SEKBON(NamedTuple):
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


_SEKBON = _SEKBON()
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


class _CHFBON8H(NamedTuple):
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


_CHFBON8H = _CHFBON8H()
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


class _TRYBON8H(NamedTuple):
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


_TRYBON8H = _TRYBON8H()
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


class _INRBON8H(NamedTuple):
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


_INRBON8H = _INRBON8H()
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


class _ZARBON8H(NamedTuple):
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


_ZARBON8H = _ZARBON8H()
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


class _BRLBON8H(NamedTuple):
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


_BRLBON8H = _BRLBON8H()
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


class _MXNBON8H(NamedTuple):
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


_MXNBON8H = _MXNBON8H()
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


class _NZDBON8H(NamedTuple):
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


_NZDBON8H = _NZDBON8H()
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


class _CNHBON8H(NamedTuple):
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


_CNHBON8H = _CNHBON8H()
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


class _SEKBON8H(NamedTuple):
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


_SEKBON8H = _SEKBON8H()
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


class _BOP(NamedTuple):
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


_BOP = _BOP()
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


class _BOP_NEXT(NamedTuple):
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


_BOP_NEXT = _BOP_NEXT()
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


class _BOPT(NamedTuple):
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


_BOPT = _BOPT()
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


class _BOPT_NEXT(NamedTuple):
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


_BOPT_NEXT = _BOPT_NEXT()
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


class _OPBON(NamedTuple):
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


_OPBON = _OPBON()
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


class _OPBON8H(NamedTuple):
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


_OPBON8H = _OPBON8H()
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


class _OPUSDTPI(NamedTuple):
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


_OPUSDTPI = _OPUSDTPI()
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


class _OPUSDTPI8H(NamedTuple):
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


_OPUSDTPI8H = _OPUSDTPI8H()
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


class _OPUSDPI(NamedTuple):
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


_OPUSDPI = _OPUSDPI()
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


class _OPUSDPI8H(NamedTuple):
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


_OPUSDPI8H = _OPUSDPI8H()
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


class _BUSDC(NamedTuple):
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


_BUSDC = _BUSDC()
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


class _BUSDCT(NamedTuple):
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


_BUSDCT = _BUSDCT()
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


class _BETHPOWT(NamedTuple):
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


_BETHPOWT = _BETHPOWT()
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


class _BETHPOWT_NEXT(NamedTuple):
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


_BETHPOWT_NEXT = _BETHPOWT_NEXT()
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


class _BETHPOWT30M(NamedTuple):
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


_BETHPOWT30M = _BETHPOWT30M()
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


class _BALTMEXT30M(NamedTuple):
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


_BALTMEXT30M = _BALTMEXT30M()
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


class _BDEFIMEXT30M(NamedTuple):
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


_BDEFIMEXT30M = _BDEFIMEXT30M()
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


class _BMETAMEXT30M(NamedTuple):
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


_BMETAMEXT30M = _BMETAMEXT30M()
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


class _BUSDC_NEXT(NamedTuple):
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


_BUSDC_NEXT = _BUSDC_NEXT()
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


class _BUSDCT_NEXT(NamedTuple):
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


_BUSDCT_NEXT = _BUSDCT_NEXT()
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


class _BKLAY(NamedTuple):
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


_BKLAY = _BKLAY()
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


class _BKLAY_NEXT(NamedTuple):
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


_BKLAY_NEXT = _BKLAY_NEXT()
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


class _BKLAYT(NamedTuple):
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


_BKLAYT = _BKLAYT()
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


class _BKLAYT_NEXT(NamedTuple):
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


_BKLAYT_NEXT = _BKLAYT_NEXT()
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


class _KLAYUSDTPI(NamedTuple):
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


_KLAYUSDTPI = _KLAYUSDTPI()
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


class _KLAYUSDTPI8H(NamedTuple):
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


_KLAYUSDTPI8H = _KLAYUSDTPI8H()
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


class _KLAYUSDPI(NamedTuple):
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


_KLAYUSDPI = _KLAYUSDPI()
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


class _KLAYUSDPI8H(NamedTuple):
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


_KLAYUSDPI8H = _KLAYUSDPI8H()
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


class _KLAYBON(NamedTuple):
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


_KLAYBON = _KLAYBON()
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


class _KLAYBON8H(NamedTuple):
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


_KLAYBON8H = _KLAYBON8H()
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


class _BSTETH(NamedTuple):
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


_BSTETH = _BSTETH()
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


class _BSTETHT(NamedTuple):
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


_BSTETHT = _BSTETHT()
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


class _BDAI(NamedTuple):
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


_BDAI = _BDAI()
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


class _BDAIT(NamedTuple):
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


_BDAIT = _BDAIT()
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


class _BBUSD(NamedTuple):
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


_BBUSD = _BBUSD()
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


class _BBUSDT(NamedTuple):
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


_BBUSDT = _BBUSDT()
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


class _BWBTC(NamedTuple):
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


_BWBTC = _BWBTC()
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


class _BWBTCT(NamedTuple):
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


_BWBTCT = _BWBTCT()
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


class _BCRO(NamedTuple):
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


_BCRO = _BCRO()
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


class _BCROT(NamedTuple):
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


_BCROT = _BCROT()
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


class _BQNT(NamedTuple):
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


_BQNT = _BQNT()
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


class _BQNTT(NamedTuple):
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


_BQNTT = _BQNTT()
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


class _BOKB(NamedTuple):
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


_BOKB = _BOKB()
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


class _BOKBT(NamedTuple):
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


_BOKBT = _BOKBT()
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


class _BLEO(NamedTuple):
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


_BLEO = _BLEO()
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


class _BLEOT(NamedTuple):
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


_BLEOT = _BLEOT()
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


class _BAAVE(NamedTuple):
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


_BAAVE = _BAAVE()
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


class _BMANA(NamedTuple):
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


_BMANA = _BMANA()
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


class _BXLM(NamedTuple):
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


_BXLM = _BXLM()
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


class _BVET(NamedTuple):
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


_BVET = _BVET()
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


class _BFIL(NamedTuple):
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


_BFIL = _BFIL()
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


class _BXTZ(NamedTuple):
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


_BXTZ = _BXTZ()
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


class _BMKR(NamedTuple):
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


_BMKR = _BMKR()
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


class _BFLOW(NamedTuple):
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


_BFLOW = _BFLOW()
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


class _BFLOWT(NamedTuple):
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


_BFLOWT = _BFLOWT()
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


class _BHBAR(NamedTuple):
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


_BHBAR = _BHBAR()
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


class _BHBART(NamedTuple):
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


_BHBART = _BHBART()
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


class _BEGLD(NamedTuple):
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


_BEGLD = _BEGLD()
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


class _BEGLDT(NamedTuple):
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


_BEGLDT = _BEGLDT()
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


class _BTUSD(NamedTuple):
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


_BTUSD = _BTUSD()
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


class _BTUSDT(NamedTuple):
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


_BTUSDT = _BTUSDT()
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


class _BUSDP(NamedTuple):
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


_BUSDP = _BUSDP()
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


class _BHNT(NamedTuple):
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


_BHNT = _BHNT()
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


class _BHNTT(NamedTuple):
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


_BHNTT = _BHNTT()
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


class _BIOTA(NamedTuple):
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


_BIOTA = _BIOTA()
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


class _BIOTAT(NamedTuple):
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


_BIOTAT = _BIOTAT()
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


class _BXEC(NamedTuple):
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


_BXEC = _BXEC()
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


class _BXECT(NamedTuple):
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


_BXECT = _BXECT()
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


class _BFTTT(NamedTuple):
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


_BFTTT = _BFTTT()
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


class _BSANDT30M(NamedTuple):
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


_BSANDT30M = _BSANDT30M()
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


class _BNEART30M(NamedTuple):
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


_BNEART30M = _BNEART30M()
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


class _BMANAT30M(NamedTuple):
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


_BMANAT30M = _BMANAT30M()
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


class _BSHIBT30M(NamedTuple):
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


_BSHIBT30M = _BSHIBT30M()
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


class _BOPT30M(NamedTuple):
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


_BOPT30M = _BOPT30M()
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


class _BGALT30M(NamedTuple):
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


_BGALT30M = _BGALT30M()
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


class _BGAL30M(NamedTuple):
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


_BGAL30M = _BGAL30M()
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


class _BTRX30M(NamedTuple):
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


_BTRX30M = _BTRX30M()
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


class _BOP30M(NamedTuple):
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


_BOP30M = _BOP30M()
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


class _BAPE30M(NamedTuple):
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


_BAPE30M = _BAPE30M()
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


class _BFTMT30M(NamedTuple):
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


_BFTMT30M = _BFTMT30M()
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


class _BAPT(NamedTuple):
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


_BAPT = _BAPT()
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


class _BAPT_NEXT(NamedTuple):
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


_BAPT_NEXT = _BAPT_NEXT()
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


class _BAPT30M(NamedTuple):
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


_BAPT30M = _BAPT30M()
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


class _BAPTT(NamedTuple):
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


_BAPTT = _BAPTT()
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


class _BAPTT_NEXT(NamedTuple):
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


_BAPTT_NEXT = _BAPTT_NEXT()
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


class _BAPTT30M(NamedTuple):
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


_BAPTT30M = _BAPTT30M()
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


class _APTBON(NamedTuple):
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


_APTBON = _APTBON()
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


class _APTBON8H(NamedTuple):
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


_APTBON8H = _APTBON8H()
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


class _APTUSDTPI(NamedTuple):
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


_APTUSDTPI = _APTUSDTPI()
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


class _APTUSDTPI8H(NamedTuple):
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


_APTUSDTPI8H = _APTUSDTPI8H()
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


class _APTUSDPI(NamedTuple):
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


_APTUSDPI = _APTUSDPI()
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


class _APTUSDPI8H(NamedTuple):
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


_APTUSDPI8H = _APTUSDPI8H()
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


class _BFTT(NamedTuple):
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


_BFTT = _BFTT()
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


class _BFTT_NEXT(NamedTuple):
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


_BFTT_NEXT = _BFTT_NEXT()
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


class _BFTTT_NEXT(NamedTuple):
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


_BFTTT_NEXT = _BFTTT_NEXT()
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


class _FTTBON(NamedTuple):
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


_FTTBON = _FTTBON()
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


class _FTTBON8H(NamedTuple):
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


_FTTBON8H = _FTTBON8H()
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


class _FTTUSDTPI(NamedTuple):
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


_FTTUSDTPI = _FTTUSDTPI()
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


class _FTTUSDTPI8H(NamedTuple):
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


_FTTUSDTPI8H = _FTTUSDTPI8H()
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


class _FTTUSDPI(NamedTuple):
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


_FTTUSDPI = _FTTUSDPI()
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


class _FTTUSDPI8H(NamedTuple):
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


_FTTUSDPI8H = _FTTUSDPI8H()
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


class _BMEXBON(NamedTuple):
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


_BMEXBON = _BMEXBON()
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


class _BMEXBON8H(NamedTuple):
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


_BMEXBON8H = _BMEXBON8H()
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


class _BMEXUSDTPI(NamedTuple):
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


_BMEXUSDTPI = _BMEXUSDTPI()
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


class _BMEXUSDTPI8H(NamedTuple):
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


_BMEXUSDTPI8H = _BMEXUSDTPI8H()
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


class _BMEXUSDPI(NamedTuple):
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


_BMEXUSDPI = _BMEXUSDPI()
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


class _BMEXUSDPI8H(NamedTuple):
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


_BMEXUSDPI8H = _BMEXUSDPI8H()
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


class _BBMEXT(NamedTuple):
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


_BBMEXT = _BBMEXT()
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


class _BBMEXT_NEXT(NamedTuple):
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


_BBMEXT_NEXT = _BBMEXT_NEXT()
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


class _BBMEX(NamedTuple):
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


_BBMEX = _BBMEX()
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


class _BBMEX_NEXT(NamedTuple):
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


_BBMEX_NEXT = _BBMEX_NEXT()
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


class _CROBON(NamedTuple):
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


_CROBON = _CROBON()
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


class _CROBON8H(NamedTuple):
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


_CROBON8H = _CROBON8H()
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


class _CROUSDTPI(NamedTuple):
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


_CROUSDTPI = _CROUSDTPI()
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


class _CROUSDTPI8H(NamedTuple):
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


_CROUSDTPI8H = _CROUSDTPI8H()
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


class _CROUSDPI(NamedTuple):
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


_CROUSDPI = _CROUSDPI()
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


class _CROUSDPI8H(NamedTuple):
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


_CROUSDPI8H = _CROUSDPI8H()
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


class _BFTT30M(NamedTuple):
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


_BFTT30M = _BFTT30M()
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


class _BFTTT30M(NamedTuple):
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


_BFTTT30M = _BFTTT30M()
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


class _BETHYLD(NamedTuple):
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


_BETHYLD = _BETHYLD()
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


class _BFLRT(NamedTuple):
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


_BFLRT = _BFLRT()
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


class _BFLRT_NEXT(NamedTuple):
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


_BFLRT_NEXT = _BFLRT_NEXT()
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


class _BFLRT30M(NamedTuple):
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


_BFLRT30M = _BFLRT30M()
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


class _FLRBON(NamedTuple):
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


_FLRBON = _FLRBON()
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


class _FLRBON8H(NamedTuple):
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


_FLRBON8H = _FLRBON8H()
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


class _FLRUSDTPI(NamedTuple):
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


_FLRUSDTPI = _FLRUSDTPI()
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


class _FLRUSDTPI8H(NamedTuple):
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


_FLRUSDTPI8H = _FLRUSDTPI8H()
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


class _FLRUSDPI(NamedTuple):
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


_FLRUSDPI = _FLRUSDPI()
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


class _FLRUSDPI8H(NamedTuple):
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


_FLRUSDPI8H = _FLRUSDPI8H()
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


class _BFLR(NamedTuple):
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


_BFLR = _BFLR()
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


class _BFLR_NEXT(NamedTuple):
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


_BFLR_NEXT = _BFLR_NEXT()
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


class _BLURBON(NamedTuple):
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


_BLURBON = _BLURBON()
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


class _BLURBON8H(NamedTuple):
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


_BLURBON8H = _BLURBON8H()
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


class _BLURUSDTPI(NamedTuple):
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


_BLURUSDTPI = _BLURUSDTPI()
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


class _BLURUSDTPI8H(NamedTuple):
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


_BLURUSDTPI8H = _BLURUSDTPI8H()
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


class _BLURUSDPI(NamedTuple):
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


_BLURUSDPI = _BLURUSDPI()
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


class _BLURUSDPI8H(NamedTuple):
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


_BLURUSDPI8H = _BLURUSDPI8H()
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


class _BBLUR(NamedTuple):
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


_BBLUR = _BBLUR()
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


class _BBLUR_NEXT(NamedTuple):
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


_BBLUR_NEXT = _BBLUR_NEXT()
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


class _BBLURT(NamedTuple):
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


_BBLURT = _BBLURT()
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


class _BBLURT_NEXT(NamedTuple):
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


_BBLURT_NEXT = _BBLURT_NEXT()
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


class _BGMXT(NamedTuple):
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


_BGMXT = _BGMXT()
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


class _BGMXT_NEXT(NamedTuple):
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


_BGMXT_NEXT = _BGMXT_NEXT()
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


class _BGMX(NamedTuple):
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


_BGMX = _BGMX()
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


class _BGMX_NEXT(NamedTuple):
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


_BGMX_NEXT = _BGMX_NEXT()
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


class _GMXBON(NamedTuple):
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


_GMXBON = _GMXBON()
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


class _GMXBON8H(NamedTuple):
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


_GMXBON8H = _GMXBON8H()
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


class _GMXUSDTPI(NamedTuple):
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


_GMXUSDTPI = _GMXUSDTPI()
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


class _GMXUSDTPI8H(NamedTuple):
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


_GMXUSDTPI8H = _GMXUSDTPI8H()
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


class _GMXUSDPI(NamedTuple):
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


_GMXUSDPI = _GMXUSDPI()
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


class _GMXUSDPI8H(NamedTuple):
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


_GMXUSDPI8H = _GMXUSDPI8H()
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


class _USDCBON(NamedTuple):
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


_USDCBON = _USDCBON()
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


class _USDCBON8H(NamedTuple):
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


_USDCBON8H = _USDCBON8H()
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


class _USDTUSDCPI(NamedTuple):
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


_USDTUSDCPI = _USDTUSDCPI()
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


class _USDTUSDCPI8H(NamedTuple):
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


_USDTUSDCPI8H = _USDTUSDCPI8H()
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


class _BUSDTUSDC(NamedTuple):
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


_BUSDTUSDC = _BUSDTUSDC()
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


class _BARBT(NamedTuple):
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


_BARBT = _BARBT()
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


class _BARBT_NEXT(NamedTuple):
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


_BARBT_NEXT = _BARBT_NEXT()
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


class _BARBT30M(NamedTuple):
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


_BARBT30M = _BARBT30M()
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


class _BARB(NamedTuple):
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


_BARB = _BARB()
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


class _BARB_NEXT(NamedTuple):
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


_BARB_NEXT = _BARB_NEXT()
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


class _ARBBON(NamedTuple):
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


_ARBBON = _ARBBON()
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


class _ARBBON8H(NamedTuple):
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


_ARBBON8H = _ARBBON8H()
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


class _ARBUSDTPI(NamedTuple):
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


_ARBUSDTPI = _ARBUSDTPI()
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


class _ARBUSDTPI8H(NamedTuple):
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


_ARBUSDTPI8H = _ARBUSDTPI8H()
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


class _ARBUSDPI(NamedTuple):
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


_ARBUSDPI = _ARBUSDPI()
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


class _ARBUSDPI8H(NamedTuple):
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


_ARBUSDPI8H = _ARBUSDPI8H()
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


class ADAM23(NamedTuple):
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


ADAM23 = ADAM23()
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


class XRPM23(NamedTuple):
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


XRPM23 = XRPM23()
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


class ARBUSDTM23(NamedTuple):
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


ARBUSDTM23 = ARBUSDTM23()
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


class KLAYUSD(NamedTuple):
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


KLAYUSD = KLAYUSD()
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


class KLAYUSDT(NamedTuple):
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


KLAYUSDT = KLAYUSDT()
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


class XRPUSD(NamedTuple):
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


XRPUSD = XRPUSD()
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


class BCHUSD(NamedTuple):
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


BCHUSD = BCHUSD()
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


class DOGEUSD(NamedTuple):
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


DOGEUSD = DOGEUSD()
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


class BNBUSD(NamedTuple):
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


BNBUSD = BNBUSD()
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


class LINKUSD(NamedTuple):
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


LINKUSD = LINKUSD()
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


class SOLUSD(NamedTuple):
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


SOLUSD = SOLUSD()
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


class APTUSD(NamedTuple):
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


APTUSD = APTUSD()
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


class BMEXUSD(NamedTuple):
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


BMEXUSD = BMEXUSD()
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


class CROUSD(NamedTuple):
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


CROUSD = CROUSD()
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


class FLRUSD(NamedTuple):
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


FLRUSD = FLRUSD()
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


class BLURUSD(NamedTuple):
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


BLURUSD = BLURUSD()
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


class GMXUSD(NamedTuple):
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


GMXUSD = GMXUSD()
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


class ARBUSD(NamedTuple):
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


ARBUSD = ARBUSD()
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


class DOGEUSDT(NamedTuple):
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


DOGEUSDT = DOGEUSDT()
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


class DOTUSDT(NamedTuple):
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


DOTUSDT = DOTUSDT()
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


class ADAUSDT(NamedTuple):
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


ADAUSDT = ADAUSDT()
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


class BNBUSDT(NamedTuple):
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


BNBUSDT = BNBUSDT()
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


class SOLUSDT(NamedTuple):
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


SOLUSDT = SOLUSDT()
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


class ADAUSD(NamedTuple):
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


ADAUSD = ADAUSD()
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


class EOSUSD(NamedTuple):
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


EOSUSD = EOSUSD()
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


class XRPUSDT(NamedTuple):
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


XRPUSDT = XRPUSDT()
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


class BCHUSDT(NamedTuple):
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


BCHUSDT = BCHUSDT()
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


class APEUSDT(NamedTuple):
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


APEUSDT = APEUSDT()
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


class GMTUSDT(NamedTuple):
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


GMTUSDT = GMTUSDT()
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


class GMTUSD(NamedTuple):
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


GMTUSD = GMTUSD()
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


class NEARUSD(NamedTuple):
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


NEARUSD = NEARUSD()
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


class APTUSDT(NamedTuple):
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


APTUSDT = APTUSDT()
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


class BMEXUSDT(NamedTuple):
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


BMEXUSDT = BMEXUSDT()
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


class CROUSDT(NamedTuple):
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


CROUSDT = CROUSDT()
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


class FLRUSDT(NamedTuple):
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


FLRUSDT = FLRUSDT()
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


class BLURUSDT(NamedTuple):
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


BLURUSDT = BLURUSDT()
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


class GMXUSDT(NamedTuple):
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


GMXUSDT = GMXUSDT()
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


class ARBUSDT(NamedTuple):
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


ARBUSDT = ARBUSDT()
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


class LUNAUSD(NamedTuple):
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


LUNAUSD = LUNAUSD()
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


class DOTUSD(NamedTuple):
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


DOTUSD = DOTUSD()
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


class MATICUSDT(NamedTuple):
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


MATICUSDT = MATICUSDT()
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


class AVAXUSD(NamedTuple):
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


AVAXUSD = AVAXUSD()
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


class AXSUSD(NamedTuple):
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


AXSUSD = AXSUSD()
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


class AVAXUSDT(NamedTuple):
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


AVAXUSDT = AVAXUSDT()
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


class LUNAUSDT(NamedTuple):
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


LUNAUSDT = LUNAUSDT()
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


class USDTUSDC(NamedTuple):
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


USDTUSDC = USDTUSDC()
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


class UNI_USDT(NamedTuple):
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


UNI_USDT = UNI_USDT()
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


class LINK_USDT(NamedTuple):
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


LINK_USDT = LINK_USDT()
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


class MATIC_USDT(NamedTuple):
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


MATIC_USDT = MATIC_USDT()
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


class AXS_USDT(NamedTuple):
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


AXS_USDT = AXS_USDT()
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


class APE_USDT(NamedTuple):
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


APE_USDT = APE_USDT()
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


class TRX_USDT(NamedTuple):
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


TRX_USDT = TRX_USDT()
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


class SOL_USDT(NamedTuple):
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


SOL_USDT = SOL_USDT()
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


class BMEX_USDT(NamedTuple):
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


BMEX_USDT = BMEX_USDT()
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


class _XBT(NamedTuple):
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


_XBT = _XBT()
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


class _XBT30M(NamedTuple):
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


_XBT30M = _XBT30M()
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


class _XBTBON(NamedTuple):
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


_XBTBON = _XBTBON()
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


class _XBTBON8H(NamedTuple):
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


_XBTBON8H = _XBTBON8H()
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


class _XBTUSDPI(NamedTuple):
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


_XBTUSDPI = _XBTUSDPI()
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


class _XBTUSDPI8H(NamedTuple):
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


_XBTUSDPI8H = _XBTUSDPI8H()
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


class _BXBT(NamedTuple):
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


_BXBT = _BXBT()
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


class _BXBT30M(NamedTuple):
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


_BXBT30M = _BXBT30M()
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


class _BXBT_NEXT(NamedTuple):
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


_BXBT_NEXT = _BXBT_NEXT()
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


class _BXBTEUR(NamedTuple):
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


_BXBTEUR = _BXBTEUR()
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


class _BXBTEUR_NEXT(NamedTuple):
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


_BXBTEUR_NEXT = _BXBTEUR_NEXT()
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


class _XBTEURPI(NamedTuple):
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


_XBTEURPI = _XBTEURPI()
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


class _XBTEURPI8H(NamedTuple):
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


_XBTEURPI8H = _XBTEURPI8H()
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


class _BXBTEUR30M(NamedTuple):
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


_BXBTEUR30M = _BXBTEUR30M()
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


class _BXBTT(NamedTuple):
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


_BXBTT = _BXBTT()
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


class _BXBTT_NEXT(NamedTuple):
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


_BXBTT_NEXT = _BXBTT_NEXT()
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


class _BXBTT30M(NamedTuple):
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


_BXBTT30M = _BXBTT30M()
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


class _XBTUSDTPI(NamedTuple):
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


_XBTUSDTPI = _XBTUSDTPI()
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


class _XBTUSDTPI8H(NamedTuple):
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


_XBTUSDTPI8H = _XBTUSDTPI8H()
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


class _BVOL(NamedTuple):
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


_BVOL = _BVOL()
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


class _BVOL24H(NamedTuple):
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


_BVOL24H = _BVOL24H()
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


class _BVOL7D(NamedTuple):
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


_BVOL7D = _BVOL7D()
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


class _ETHBON(NamedTuple):
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


_ETHBON = _ETHBON()
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


class _ETHBON8H(NamedTuple):
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


_ETHBON8H = _ETHBON8H()
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


class _ETHUSDPI(NamedTuple):
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


_ETHUSDPI = _ETHUSDPI()
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


class _ETHUSDPI8H(NamedTuple):
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


_ETHUSDPI8H = _ETHUSDPI8H()
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


class _BETH(NamedTuple):
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


_BETH = _BETH()
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


class _BETH30M(NamedTuple):
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


_BETH30M = _BETH30M()
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


class _BETHXBT(NamedTuple):
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


_BETHXBT = _BETHXBT()
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


class _BETHXBT30M(NamedTuple):
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


_BETHXBT30M = _BETHXBT30M()
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


class _BETH_NEXT(NamedTuple):
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


_BETH_NEXT = _BETH_NEXT()
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


class _BETHXBT_NEXT(NamedTuple):
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


_BETHXBT_NEXT = _BETHXBT_NEXT()
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


class _BETHT(NamedTuple):
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


_BETHT = _BETHT()
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


class _BETHT_NEXT(NamedTuple):
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


_BETHT_NEXT = _BETHT_NEXT()
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


class _BETHT30M(NamedTuple):
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


_BETHT30M = _BETHT30M()
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


class _ETHUSDTPI(NamedTuple):
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


_ETHUSDTPI = _ETHUSDTPI()
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


class _ETHUSDTPI8H(NamedTuple):
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


_ETHUSDTPI8H = _ETHUSDTPI8H()
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


class _ETHUSD_ETHPI(NamedTuple):
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


_ETHUSD_ETHPI = _ETHUSD_ETHPI()
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


class _ETHUSD_ETHPI8H(NamedTuple):
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


_ETHUSD_ETHPI8H = _ETHUSD_ETHPI8H()
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


class _BETC(NamedTuple):
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


_BETC = _BETC()
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


class _LTCBON(NamedTuple):
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


_LTCBON = _LTCBON()
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


class _LTCBON8H(NamedTuple):
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


_LTCBON8H = _LTCBON8H()
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


class _BLTCXBT(NamedTuple):
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


_BLTCXBT = _BLTCXBT()
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


class _BLTCXBT30M(NamedTuple):
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


_BLTCXBT30M = _BLTCXBT30M()
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


class _BLTCXBT_NEXT(NamedTuple):
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


_BLTCXBT_NEXT = _BLTCXBT_NEXT()
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


class _BLTC(NamedTuple):
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


_BLTC = _BLTC()
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


class _LTCUSDPI(NamedTuple):
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


_LTCUSDPI = _LTCUSDPI()
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


class _LTCUSDPI8H(NamedTuple):
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


_LTCUSDPI8H = _LTCUSDPI8H()
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


class _BLTC_NEXT(NamedTuple):
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


_BLTC_NEXT = _BLTC_NEXT()
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


class _BLTCT(NamedTuple):
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


_BLTCT = _BLTCT()
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


class _BLTCT_NEXT(NamedTuple):
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


_BLTCT_NEXT = _BLTCT_NEXT()
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


class _LTCUSDTPI(NamedTuple):
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


_LTCUSDTPI = _LTCUSDTPI()
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


class _LTCUSDTPI8H(NamedTuple):
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


_LTCUSDTPI8H = _LTCUSDTPI8H()
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


class _USDBON(NamedTuple):
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


_USDBON = _USDBON()
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


class _USDBON8H(NamedTuple):
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


_USDBON8H = _USDBON8H()
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


class XBTUSD(NamedTuple):
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


XBTUSD = XBTUSD()
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


class XBTUSDT(NamedTuple):
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


XBTUSDT = XBTUSDT()
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


class XBTEUR(NamedTuple):
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


XBTEUR = XBTEUR()
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


class XBTJ23(NamedTuple):
    """
        name: XBTJ23
        significant_digits: None
        tick_size: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTJ23"
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
        return "XBTJ23"

    def __str__(self):
        return "XBTJ23"

    def __call__(self):
        return "XBTJ23"


XBTJ23 = XBTJ23()
"""
    name: XBTJ23
    significant_digits: None
    tick_size: 0.5
    min_margin: None
    initial_margin: 0.01
    min_order_size: 100
    max_order_size: 10000000
    has_margin: True
    exchange: bitmex
"""


class XBTM23(NamedTuple):
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


XBTM23 = XBTM23()
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


class XBTUSDTM23(NamedTuple):
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


XBTUSDTM23 = XBTUSDTM23()
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


class XBTU23(NamedTuple):
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


XBTU23 = XBTU23()
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


class XBTUSDTU23(NamedTuple):
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


XBTUSDTU23 = XBTUSDTU23()
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


class XBTZ23(NamedTuple):
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


XBTZ23 = XBTZ23()
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


class XBT_USDT(NamedTuple):
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


XBT_USDT = XBT_USDT()
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


class ETHUSD(NamedTuple):
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


ETHUSD = ETHUSD()
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


class ETHUSDT(NamedTuple):
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


ETHUSDT = ETHUSDT()
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


class ETHUSD_ETH(NamedTuple):
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


ETHUSD_ETH = ETHUSD_ETH()
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


class ETHM23(NamedTuple):
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


ETHM23 = ETHM23()
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


class ETHUSDM23(NamedTuple):
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


ETHUSDM23 = ETHUSDM23()
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


class ETHUSDTM23(NamedTuple):
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


ETHUSDTM23 = ETHUSDTM23()
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


class ETH_USDT(NamedTuple):
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


ETH_USDT = ETH_USDT()
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


class ETH_XBT(NamedTuple):
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


ETH_XBT = ETH_XBT()
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


class LTCUSD(NamedTuple):
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


LTCUSD = LTCUSD()
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


class LTCUSDT(NamedTuple):
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


LTCUSDT = LTCUSDT()
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


class XBTK23(NamedTuple):
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


XBTK23 = XBTK23()
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
