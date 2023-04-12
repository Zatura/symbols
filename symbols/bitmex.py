from typing import NamedTuple


class _EVOL7D(NamedTuple):
    """
        name: .EVOL7D
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EVOL7D"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAXBT"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAXBT30M"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHXBT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHXBT30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOSXBT"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOSXBT30M"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPXBT"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPXBT30M"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-10
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXXBT"
    precision: int = 1e-10
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-10
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
        precision: 1e-10
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXXBT30M"
    precision: int = 1e-10
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-10
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAXBT_NEXT"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHXBT_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOSXBT_NEXT"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-10
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXXBT_NEXT"
    precision: int = 1e-10
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-10
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPXBT_NEXT"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRP_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRP"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCH"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCH_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOST"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOST_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOST30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINKT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINKT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINKT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADAT30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXTZT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXTZT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXTZT30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKBON"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKBON8H"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKUSDTPI"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKUSDTPI8H"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTBON"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTBON8H"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNBT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNBT_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNBT30M"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOTT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOTT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOTT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BYFIT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BYFIT_NEXT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BYFIT30M"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGET"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGET_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBBON"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBBON8H"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBUSDTPI"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBUSDTPI8H"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADABON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADABON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADAUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADAUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XTZBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XTZBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XTZUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".YFIBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".YFIBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".YFIUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAAVET"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAAVET_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AAVEBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AAVEBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AAVEUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AAVEUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUNIT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUNIT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".UNIBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".UNIBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".UNIUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".UNIUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXLMT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXLMT_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XLMBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XLMBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XLMUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XLMUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXT_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRXT30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOLT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOLT_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFILT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFILT_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FILBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FILBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FILUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FILUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVETT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVETT_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".VETBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".VETBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".VETUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".VETUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMATICT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMATICT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MATICBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MATICBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MATICUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MATICUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMKRT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMKRT_NEXT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAVAXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAVAXT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNAT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNAT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCOMPT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCOMPT_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUSHIT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUSHIT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGRTT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGRTT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BALTMEX"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDEFIMEX"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUSHIBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUSHIBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUSHIUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SUSHIUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXST"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXST_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSRMT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSRMT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SRMBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SRMBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SRMUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SRMUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNA"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNA_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNABON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNABON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNAUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNAUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAVAX"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAVAX_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADA"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BADA_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADAUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ADAUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGE"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGE_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOGEUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNB"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBNB_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNBUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DOTUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDOGET30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFILT30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUNIT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXLMT30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXS"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXS_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AXSUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOS"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEOS_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EOSUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINK"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLINK_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LINKUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOL"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOL_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SOLUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAXST30M"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSOLT30M"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVETT30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMATICT30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAAVET30M"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSUSHIT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSRMT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXRPT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBCHT_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XRPUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCHUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDEFIMEX30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BALTMEX30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTMT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTMT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTMBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTMBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTMUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTMUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSHIBT"
    precision: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-09
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
        precision: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSHIBT_NEXT"
    precision: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-09
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SHIBBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SHIBBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SHIBUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SHIBUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLRCT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLRCT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMANAT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMANAT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MANABON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MANABON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MANAUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MANAUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSANDT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSANDT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SANDBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SANDBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SANDUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SANDUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTHETAT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTHETAT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BENJT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BENJT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDEFIMEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXTBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXTBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXTUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".DEFIMEXTUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BALTMEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXTBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXTBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXTUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ALTMEXTUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMETAMEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".METAMEXTBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".METAMEXTBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".METAMEXTUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".METAMEXTUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".AVAXUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNAUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LUNAUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPET"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPET_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMTUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMTT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMTT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NEARUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEAR"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEAR_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEART"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEART_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNA30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNAT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPE"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPE_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRX"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRX_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGAL"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGAL_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGALT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGALT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APEUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRXUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GALUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNC"
    precision: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-09
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
        precision: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNC_NEXT"
    precision: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-09
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
        precision: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNCT"
    precision: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-09
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
        precision: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLUNCT_NEXT"
    precision: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-09
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDFI"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDFIT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGRT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCHFPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURCHFPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURTRYPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTRYPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDINRPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDZARPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDBRLPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDMXNPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCNHPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDSEKPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCHFPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURCHFPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURTRYPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTRYPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDINRPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDZARPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDBRLPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDMXNPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCNHPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDSEKPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTCHFPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTTRYPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTINRPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTZARPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTBRLPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTMXNPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTCNHPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTSEKPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".EURUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTCHFPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTTRYPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTINRPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTZARPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTBRLPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTMXNPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTCNHPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTSEKPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CHFBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRYBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".INRBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ZARBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BRLBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MXNBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CNHBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SEKBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CHFBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".TRYBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".INRBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ZARBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BRLBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".MXNBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".NZDBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CNHBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".SEKBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOP"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOP_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOPT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOPT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".OPUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDC"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDCT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHPOWT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHPOWT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHPOWT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BALTMEXT30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDEFIMEXT30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMETAMEXT30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDC_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDCT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BKLAY"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BKLAY_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BKLAYT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BKLAYT_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".KLAYBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSTETH"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSTETHT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDAI"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BDAIT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBUSD"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBUSDT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BWBTC"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BWBTCT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCRO"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BCROT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BQNT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BQNTT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOKB"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOKBT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLEO"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLEOT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAAVE"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMANA"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXLM"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVET"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFIL"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXTZ"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMKR"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLOW"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLOWT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BHBAR"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BHBART"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEGLD"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BEGLDT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTUSD"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTUSDT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDP"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BHNT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BHNTT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BIOTA"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BIOTAT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXEC"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 1e-08
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXECT"
    precision: int = 1e-08
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-08
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTTT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSANDT30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BNEART30M"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMANAT30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-09
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BSHIBT30M"
    precision: int = 1e-09
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-09
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOPT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGALT30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGAL30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BTRX30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BOP30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPE30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTMT30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPTT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPTT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BAPTT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".APTUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTTT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FTTUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BMEXUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBMEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBMEXT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBMEX"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBMEX_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROBON"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROBON8H"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".CROUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFTTT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHYLD"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLRT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLRT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLRT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".FLRUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLR"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BFLR_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLURUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBLUR"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBLUR_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBLURT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BBLURT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMXT_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMX"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BGMX_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".GMXUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCBON"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDCBON8H"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTUSDCPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDTUSDCPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BUSDTUSDC"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARBT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARBT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARBT30M"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARB"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BARB_NEXT"
    precision: int = 0.0001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.0001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ARBUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-08
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ADAM23"
    precision: int = 1e-08
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
    precision: 1e-08
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
        precision: 1e-08
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XRPM23"
    precision: int = 1e-08
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
    precision: 1e-08
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ARBUSDTM23"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "KLAYUSD"
    precision: int = 1e-05
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "KLAYUSDT"
    precision: int = 1e-05
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XRPUSD"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BCHUSD"
    precision: int = 0.05
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
    precision: 0.05
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
        precision: 1e-05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 5000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "DOGEUSD"
    precision: int = 1e-05
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
    precision: 1e-05
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
        precision: 0.01
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BNBUSD"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LINKUSD"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.01
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "SOLUSD"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "APTUSD"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BMEXUSD"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 5000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "CROUSD"
    precision: int = 1e-05
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "FLRUSD"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BLURUSD"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.01
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "GMXUSD"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ARBUSD"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 10000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "DOGEUSDT"
    precision: int = 1e-05
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
    precision: 1e-05
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "DOTUSDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ADAUSDT"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.01
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BNBUSDT"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "SOLUSDT"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ADAUSD"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "EOSUSD"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XRPUSDT"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.05
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BCHUSDT"
    precision: int = 0.05
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
    precision: 0.05
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "APEUSDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "GMTUSDT"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "GMTUSD"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "NEARUSD"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "APTUSDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BMEXUSDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 1e-05
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 10000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "CROUSDT"
    precision: int = 1e-05
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
    precision: 1e-05
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "FLRUSDT"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BLURUSDT"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.01
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "GMXUSDT"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.03
        min_order_size: 100
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ARBUSDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.04
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LUNAUSD"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.04
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "DOTUSD"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "MATICUSDT"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1
        max_order_size: 500000
        has_margin: True
        exchange: bitmex
    """
    name: str = "AVAXUSD"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.01
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1
        max_order_size: 1000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "AXSUSD"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "AVAXUSDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.05
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LUNAUSDT"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 0.1
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "USDTUSDC"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.001
        min_margin: None
        initial_margin: 1
        min_order_size: 10000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "UNI_USDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: 1
        min_order_size: 10000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LINK_USDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 1
        min_order_size: 100000000
        max_order_size: 100000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "MATIC_USDT"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.01
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 1000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "AXS_USDT"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.001
        min_margin: None
        initial_margin: 1
        min_order_size: 10000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "APE_USDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.0001
        min_margin: None
        initial_margin: 1
        min_order_size: 100000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "TRX_USDT"
    precision: int = 0.0001
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
    precision: 0.0001
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
        precision: 0.01
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "SOL_USDT"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.001
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 1000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "BMEX_USDT"
    precision: int = 0.001
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
    precision: 0.001
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBT30M"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBT30M"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBT_NEXT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTEUR"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTEUR_NEXT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTEURPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTEURPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTEUR30M"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTT_NEXT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BXBTT30M"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".XBTUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVOL"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVOL24H"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BVOL7D"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETH"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETH30M"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHXBT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHXBT30M"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.01
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETH_NEXT"
    precision: int = 0.01
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.01
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHXBT_NEXT"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHT_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETHT30M"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSD_ETHPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".ETHUSD_ETHPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-05
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BETC"
    precision: int = 1e-05
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-05
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCXBT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCXBT30M"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCXBT_NEXT"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTC"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCUSDPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCUSDPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTC_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 0.001
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".BLTCT_NEXT"
    precision: int = 0.001
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 0.001
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCUSDTPI"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".LTCUSDTPI8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDBON"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 1e-06
        min_margin: None
        initial_margin: None
        min_order_size: None
        max_order_size: None
        has_margin: False
        exchange: bitmex
    """
    name: str = ".USDBON8H"
    precision: int = 1e-06
    min_margin: float = None
    initial_margin: float = None
    min_order_size: float = None
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
    precision: 1e-06
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
        precision: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTUSD"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTUSDT"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.5
        min_margin: None
        initial_margin: 0.02
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTEUR"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTJ23"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTM23"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTUSDTM23"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTU23"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTUSDTU23"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.5
        min_margin: None
        initial_margin: 0.01
        min_order_size: 100
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBTZ23"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.5
        min_margin: None
        initial_margin: 1
        min_order_size: 10000
        max_order_size: 100000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "XBT_USDT"
    precision: int = 0.5
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
    precision: 0.5
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
        precision: 0.05
        min_margin: None
        initial_margin: 0.01
        min_order_size: 1
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSD"
    precision: int = 0.05
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
    precision: 0.05
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
        precision: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSDT"
    precision: int = 0.05
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
    precision: 0.05
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
        precision: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSD_ETH"
    precision: int = 0.05
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
    precision: 0.05
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
        precision: 1e-05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHM23"
    precision: int = 1e-05
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
    precision: 1e-05
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
        precision: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 10000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSDM23"
    precision: int = 0.05
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
    precision: 0.05
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
        precision: 0.05
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETHUSDTM23"
    precision: int = 0.05
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
    precision: 0.05
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
        precision: 0.05
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 10000000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETH_USDT"
    precision: int = 0.05
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
    precision: 0.05
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
        precision: 1e-07
        min_margin: None
        initial_margin: 1
        min_order_size: 1000000
        max_order_size: 100000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "ETH_XBT"
    precision: int = 1e-07
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
    precision: 1e-07
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
        precision: 0.01
        min_margin: None
        initial_margin: 0.02
        min_order_size: 1
        max_order_size: 100000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LTCUSD"
    precision: int = 0.01
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
    precision: 0.01
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
        precision: 0.01
        min_margin: None
        initial_margin: 0.03
        min_order_size: 1000
        max_order_size: 1000000000
        has_margin: True
        exchange: bitmex
    """
    name: str = "LTCUSDT"
    precision: int = 0.01
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
    precision: 0.01
    min_margin: None
    initial_margin: 0.03
    min_order_size: 1000
    max_order_size: 1000000000
    has_margin: True
    exchange: bitmex
"""
