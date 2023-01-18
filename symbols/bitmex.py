from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class _EVOL7D:
    """
        name: .EVOL7D
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EVOL7D"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BADAXBT:
    """
        name: .BADAXBT
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BADAXBT"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BADAXBT30M:
    """
        name: .BADAXBT30M
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BADAXBT30M"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBCHXBT:
    """
        name: .BBCHXBT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBCHXBT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBCHXBT30M:
    """
        name: .BBCHXBT30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBCHXBT30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEOSXBT:
    """
        name: .BEOSXBT
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEOSXBT"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEOSXBT30M:
    """
        name: .BEOSXBT30M
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEOSXBT30M"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXRPXBT:
    """
        name: .BXRPXBT
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXRPXBT"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXRPXBT30M:
    """
        name: .BXRPXBT30M
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXRPXBT30M"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTRXXBT:
    """
        name: .BTRXXBT
        precision: 1e-10
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTRXXBT"
    precision: int = 1e-10
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTRXXBT30M:
    """
        name: .BTRXXBT30M
        precision: 1e-10
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTRXXBT30M"
    precision: int = 1e-10
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BADAXBT_NEXT:
    """
        name: .BADAXBT_NEXT
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BADAXBT_NEXT"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBCHXBT_NEXT:
    """
        name: .BBCHXBT_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBCHXBT_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEOSXBT_NEXT:
    """
        name: .BEOSXBT_NEXT
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEOSXBT_NEXT"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTRXXBT_NEXT:
    """
        name: .BTRXXBT_NEXT
        precision: 1e-10
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTRXXBT_NEXT"
    precision: int = 1e-10
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXRPXBT_NEXT:
    """
        name: .BXRPXBT_NEXT
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXRPXBT_NEXT"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXRP_NEXT:
    """
        name: .BXRP_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXRP_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXRP:
    """
        name: .BXRP
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXRP"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XRPBON:
    """
        name: .XRPBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XRPBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XRPBON8H:
    """
        name: .XRPBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XRPBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XRPUSDPI:
    """
        name: .XRPUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XRPUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XRPUSDPI8H:
    """
        name: .XRPUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XRPUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBCH:
    """
        name: .BBCH
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBCH"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCHBON:
    """
        name: .BCHBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCHBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCHBON8H:
    """
        name: .BCHBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCHBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCHUSDPI:
    """
        name: .BCHUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCHUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCHUSDPI8H:
    """
        name: .BCHUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCHUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBCH_NEXT:
    """
        name: .BBCH_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBCH_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDT:
    """
        name: .BUSDT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDT_NEXT:
    """
        name: .BUSDT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEOST:
    """
        name: .BEOST
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEOST"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEOST_NEXT:
    """
        name: .BEOST_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEOST_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEOST30M:
    """
        name: .BEOST30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEOST30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLINKT:
    """
        name: .BLINKT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLINKT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLINKT_NEXT:
    """
        name: .BLINKT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLINKT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLINKT30M:
    """
        name: .BLINKT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLINKT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BADAT:
    """
        name: .BADAT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BADAT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BADAT_NEXT:
    """
        name: .BADAT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BADAT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BADAT30M:
    """
        name: .BADAT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BADAT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXTZT:
    """
        name: .BXTZT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXTZT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXTZT_NEXT:
    """
        name: .BXTZT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXTZT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXTZT30M:
    """
        name: .BXTZT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXTZT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LINKBON:
    """
        name: .LINKBON
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LINKBON"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LINKBON8H:
    """
        name: .LINKBON8H
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LINKBON8H"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LINKUSDTPI:
    """
        name: .LINKUSDTPI
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LINKUSDTPI"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LINKUSDTPI8H:
    """
        name: .LINKUSDTPI8H
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LINKUSDTPI8H"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTBON:
    """
        name: .USDTBON
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTBON"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTBON8H:
    """
        name: .USDTBON8H
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTBON8H"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBNBT:
    """
        name: .BBNBT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBNBT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBNBT_NEXT:
    """
        name: .BBNBT_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBNBT_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBNBT30M:
    """
        name: .BBNBT30M
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBNBT30M"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOTT:
    """
        name: .BDOTT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOTT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOTT_NEXT:
    """
        name: .BDOTT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOTT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOTT30M:
    """
        name: .BDOTT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOTT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BYFIT:
    """
        name: .BYFIT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BYFIT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BYFIT_NEXT:
    """
        name: .BYFIT_NEXT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BYFIT_NEXT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BYFIT30M:
    """
        name: .BYFIT30M
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BYFIT30M"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOGET:
    """
        name: .BDOGET
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOGET"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOGET_NEXT:
    """
        name: .BDOGET_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOGET_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOGEBON:
    """
        name: .DOGEBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOGEBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOGEBON8H:
    """
        name: .DOGEBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOGEBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOGEUSDTPI:
    """
        name: .DOGEUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOGEUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOGEUSDTPI8H:
    """
        name: .DOGEUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOGEUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNBBON:
    """
        name: .BNBBON
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNBBON"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNBBON8H:
    """
        name: .BNBBON8H
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNBBON8H"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNBUSDTPI:
    """
        name: .BNBUSDTPI
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNBUSDTPI"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNBUSDTPI8H:
    """
        name: .BNBUSDTPI8H
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNBUSDTPI8H"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ADABON:
    """
        name: .ADABON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ADABON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ADABON8H:
    """
        name: .ADABON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ADABON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ADAUSDTPI:
    """
        name: .ADAUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ADAUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ADAUSDTPI8H:
    """
        name: .ADAUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ADAUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOTBON:
    """
        name: .DOTBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOTBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOTBON8H:
    """
        name: .DOTBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOTBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOTUSDTPI:
    """
        name: .DOTUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOTUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOTUSDTPI8H:
    """
        name: .DOTUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOTUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EOSBON:
    """
        name: .EOSBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EOSBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EOSBON8H:
    """
        name: .EOSBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EOSBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EOSUSDTPI:
    """
        name: .EOSUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EOSUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EOSUSDTPI8H:
    """
        name: .EOSUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EOSUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XTZBON:
    """
        name: .XTZBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XTZBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XTZBON8H:
    """
        name: .XTZBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XTZBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XTZUSDTPI:
    """
        name: .XTZUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XTZUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _YFIBON:
    """
        name: .YFIBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".YFIBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _YFIBON8H:
    """
        name: .YFIBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".YFIBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _YFIUSDTPI:
    """
        name: .YFIUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".YFIUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAAVET:
    """
        name: .BAAVET
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAAVET"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAAVET_NEXT:
    """
        name: .BAAVET_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAAVET_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AAVEBON:
    """
        name: .AAVEBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AAVEBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AAVEBON8H:
    """
        name: .AAVEBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AAVEBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AAVEUSDTPI:
    """
        name: .AAVEUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AAVEUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AAVEUSDTPI8H:
    """
        name: .AAVEUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AAVEUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUNIT:
    """
        name: .BUNIT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUNIT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUNIT_NEXT:
    """
        name: .BUNIT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUNIT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _UNIBON:
    """
        name: .UNIBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".UNIBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _UNIBON8H:
    """
        name: .UNIBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".UNIBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _UNIUSDTPI:
    """
        name: .UNIUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".UNIUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _UNIUSDTPI8H:
    """
        name: .UNIUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".UNIUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXLMT:
    """
        name: .BXLMT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXLMT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXLMT_NEXT:
    """
        name: .BXLMT_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXLMT_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XLMBON:
    """
        name: .XLMBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XLMBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XLMBON8H:
    """
        name: .XLMBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XLMBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XLMUSDTPI:
    """
        name: .XLMUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XLMUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XLMUSDTPI8H:
    """
        name: .XLMUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XLMUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTRXT:
    """
        name: .BTRXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTRXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTRXT_NEXT:
    """
        name: .BTRXT_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTRXT_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _TRXBON:
    """
        name: .TRXBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".TRXBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _TRXBON8H:
    """
        name: .TRXBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".TRXBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _TRXUSDTPI:
    """
        name: .TRXUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".TRXUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _TRXUSDTPI8H:
    """
        name: .TRXUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".TRXUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTRXT30M:
    """
        name: .BTRXT30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTRXT30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSOLT:
    """
        name: .BSOLT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSOLT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSOLT_NEXT:
    """
        name: .BSOLT_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSOLT_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SOLBON:
    """
        name: .SOLBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SOLBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SOLBON8H:
    """
        name: .SOLBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SOLBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SOLUSDTPI:
    """
        name: .SOLUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SOLUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SOLUSDTPI8H:
    """
        name: .SOLUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SOLUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFILT:
    """
        name: .BFILT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFILT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFILT_NEXT:
    """
        name: .BFILT_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFILT_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FILBON:
    """
        name: .FILBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FILBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FILBON8H:
    """
        name: .FILBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FILBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FILUSDTPI:
    """
        name: .FILUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FILUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FILUSDTPI8H:
    """
        name: .FILUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FILUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURBON:
    """
        name: .EURBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURBON8H:
    """
        name: .EURBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BVETT:
    """
        name: .BVETT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BVETT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BVETT_NEXT:
    """
        name: .BVETT_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BVETT_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _VETBON:
    """
        name: .VETBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".VETBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _VETBON8H:
    """
        name: .VETBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".VETBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _VETUSDTPI:
    """
        name: .VETUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".VETUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _VETUSDTPI8H:
    """
        name: .VETUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".VETUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMATICT:
    """
        name: .BMATICT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMATICT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMATICT_NEXT:
    """
        name: .BMATICT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMATICT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MATICBON:
    """
        name: .MATICBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MATICBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MATICBON8H:
    """
        name: .MATICBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MATICBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MATICUSDTPI:
    """
        name: .MATICUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MATICUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MATICUSDTPI8H:
    """
        name: .MATICUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MATICUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMKRT:
    """
        name: .BMKRT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMKRT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMKRT_NEXT:
    """
        name: .BMKRT_NEXT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMKRT_NEXT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAVAXT:
    """
        name: .BAVAXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAVAXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAVAXT_NEXT:
    """
        name: .BAVAXT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAVAXT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNAT:
    """
        name: .BLUNAT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNAT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNAT_NEXT:
    """
        name: .BLUNAT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNAT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCOMPT:
    """
        name: .BCOMPT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCOMPT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCOMPT_NEXT:
    """
        name: .BCOMPT_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCOMPT_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSUSHIT:
    """
        name: .BSUSHIT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSUSHIT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSUSHIT_NEXT:
    """
        name: .BSUSHIT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSUSHIT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGRTT:
    """
        name: .BGRTT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGRTT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGRTT_NEXT:
    """
        name: .BGRTT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGRTT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BALTMEX:
    """
        name: .BALTMEX
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BALTMEX"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDEFIMEX:
    """
        name: .BDEFIMEX
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDEFIMEX"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ALTMEXBON:
    """
        name: .ALTMEXBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ALTMEXBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ALTMEXBON8H:
    """
        name: .ALTMEXBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ALTMEXBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ALTMEXUSDPI:
    """
        name: .ALTMEXUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ALTMEXUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ALTMEXUSDPI8H:
    """
        name: .ALTMEXUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ALTMEXUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DEFIMEXBON:
    """
        name: .DEFIMEXBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DEFIMEXBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DEFIMEXBON8H:
    """
        name: .DEFIMEXBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DEFIMEXBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DEFIMEXUSDPI:
    """
        name: .DEFIMEXUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DEFIMEXUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DEFIMEXUSDPI8H:
    """
        name: .DEFIMEXUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DEFIMEXUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SUSHIBON:
    """
        name: .SUSHIBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SUSHIBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SUSHIBON8H:
    """
        name: .SUSHIBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SUSHIBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SUSHIUSDTPI:
    """
        name: .SUSHIUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SUSHIUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SUSHIUSDTPI8H:
    """
        name: .SUSHIUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SUSHIUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAXST:
    """
        name: .BAXST
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAXST"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAXST_NEXT:
    """
        name: .BAXST_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAXST_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AXSBON:
    """
        name: .AXSBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AXSBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AXSBON8H:
    """
        name: .AXSBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AXSBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AXSUSDTPI:
    """
        name: .AXSUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AXSUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AXSUSDTPI8H:
    """
        name: .AXSUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AXSUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSRMT:
    """
        name: .BSRMT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSRMT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSRMT_NEXT:
    """
        name: .BSRMT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSRMT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SRMBON:
    """
        name: .SRMBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SRMBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SRMBON8H:
    """
        name: .SRMBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SRMBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SRMUSDTPI:
    """
        name: .SRMUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SRMUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SRMUSDTPI8H:
    """
        name: .SRMUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SRMUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNA:
    """
        name: .BLUNA
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNA"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNA_NEXT:
    """
        name: .BLUNA_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNA_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LUNABON:
    """
        name: .LUNABON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LUNABON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LUNABON8H:
    """
        name: .LUNABON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LUNABON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LUNAUSDPI:
    """
        name: .LUNAUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LUNAUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LUNAUSDPI8H:
    """
        name: .LUNAUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LUNAUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AVAXBON:
    """
        name: .AVAXBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AVAXBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AVAXBON8H:
    """
        name: .AVAXBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AVAXBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAVAX:
    """
        name: .BAVAX
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAVAX"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAVAX_NEXT:
    """
        name: .BAVAX_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAVAX_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AVAXUSDPI:
    """
        name: .AVAXUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AVAXUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AVAXUSDPI8H:
    """
        name: .AVAXUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AVAXUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BADA:
    """
        name: .BADA
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BADA"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BADA_NEXT:
    """
        name: .BADA_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BADA_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ADAUSDPI:
    """
        name: .ADAUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ADAUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ADAUSDPI8H:
    """
        name: .ADAUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ADAUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOGE:
    """
        name: .BDOGE
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOGE"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOGE_NEXT:
    """
        name: .BDOGE_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOGE_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOGEUSDPI:
    """
        name: .DOGEUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOGEUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOGEUSDPI8H:
    """
        name: .DOGEUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOGEUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBNB:
    """
        name: .BBNB
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBNB"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBNB_NEXT:
    """
        name: .BBNB_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBNB_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNBUSDPI:
    """
        name: .BNBUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNBUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNBUSDPI8H:
    """
        name: .BNBUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNBUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOT:
    """
        name: .BDOT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOT_NEXT:
    """
        name: .BDOT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOTUSDPI:
    """
        name: .DOTUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOTUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DOTUSDPI8H:
    """
        name: .DOTUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DOTUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDOGET30M:
    """
        name: .BDOGET30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDOGET30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFILT30M:
    """
        name: .BFILT30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFILT30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUNIT30M:
    """
        name: .BUNIT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUNIT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXLMT30M:
    """
        name: .BXLMT30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXLMT30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAXS:
    """
        name: .BAXS
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAXS"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAXS_NEXT:
    """
        name: .BAXS_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAXS_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AXSUSDPI:
    """
        name: .AXSUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AXSUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AXSUSDPI8H:
    """
        name: .AXSUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AXSUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEOS:
    """
        name: .BEOS
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEOS"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEOS_NEXT:
    """
        name: .BEOS_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEOS_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EOSUSDPI:
    """
        name: .EOSUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EOSUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EOSUSDPI8H:
    """
        name: .EOSUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EOSUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLINK:
    """
        name: .BLINK
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLINK"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLINK_NEXT:
    """
        name: .BLINK_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLINK_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LINKUSDPI:
    """
        name: .LINKUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LINKUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LINKUSDPI8H:
    """
        name: .LINKUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LINKUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSOL:
    """
        name: .BSOL
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSOL"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSOL_NEXT:
    """
        name: .BSOL_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSOL_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SOLUSDPI:
    """
        name: .SOLUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SOLUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SOLUSDPI8H:
    """
        name: .SOLUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SOLUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAXST30M:
    """
        name: .BAXST30M
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAXST30M"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSOLT30M:
    """
        name: .BSOLT30M
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSOLT30M"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BVETT30M:
    """
        name: .BVETT30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BVETT30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMATICT30M:
    """
        name: .BMATICT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMATICT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAAVET30M:
    """
        name: .BAAVET30M
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAAVET30M"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSUSHIT30M:
    """
        name: .BSUSHIT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSUSHIT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSRMT30M:
    """
        name: .BSRMT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSRMT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXRPT:
    """
        name: .BXRPT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXRPT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXRPT_NEXT:
    """
        name: .BXRPT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXRPT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBCHT:
    """
        name: .BBCHT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBCHT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBCHT_NEXT:
    """
        name: .BBCHT_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBCHT_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XRPUSDTPI:
    """
        name: .XRPUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XRPUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XRPUSDTPI8H:
    """
        name: .XRPUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XRPUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCHUSDTPI:
    """
        name: .BCHUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCHUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCHUSDTPI8H:
    """
        name: .BCHUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCHUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDEFIMEX30M:
    """
        name: .BDEFIMEX30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDEFIMEX30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BALTMEX30M:
    """
        name: .BALTMEX30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BALTMEX30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFTMT:
    """
        name: .BFTMT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFTMT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFTMT_NEXT:
    """
        name: .BFTMT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFTMT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTMBON:
    """
        name: .FTMBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTMBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTMBON8H:
    """
        name: .FTMBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTMBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTMUSDTPI:
    """
        name: .FTMUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTMUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTMUSDTPI8H:
    """
        name: .FTMUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTMUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSHIBT:
    """
        name: .BSHIBT
        precision: 1e-09
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSHIBT"
    precision: int = 1e-09
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSHIBT_NEXT:
    """
        name: .BSHIBT_NEXT
        precision: 1e-09
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSHIBT_NEXT"
    precision: int = 1e-09
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SHIBBON:
    """
        name: .SHIBBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SHIBBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SHIBBON8H:
    """
        name: .SHIBBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SHIBBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SHIBUSDTPI:
    """
        name: .SHIBUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SHIBUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SHIBUSDTPI8H:
    """
        name: .SHIBUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SHIBUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLRCT:
    """
        name: .BLRCT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLRCT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLRCT_NEXT:
    """
        name: .BLRCT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLRCT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMANAT:
    """
        name: .BMANAT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMANAT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMANAT_NEXT:
    """
        name: .BMANAT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMANAT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MANABON:
    """
        name: .MANABON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MANABON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MANABON8H:
    """
        name: .MANABON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MANABON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MANAUSDTPI:
    """
        name: .MANAUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MANAUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MANAUSDTPI8H:
    """
        name: .MANAUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MANAUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSANDT:
    """
        name: .BSANDT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSANDT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSANDT_NEXT:
    """
        name: .BSANDT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSANDT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SANDBON:
    """
        name: .SANDBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SANDBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SANDBON8H:
    """
        name: .SANDBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SANDBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SANDUSDTPI:
    """
        name: .SANDUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SANDUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SANDUSDTPI8H:
    """
        name: .SANDUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SANDUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTHETAT:
    """
        name: .BTHETAT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTHETAT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTHETAT_NEXT:
    """
        name: .BTHETAT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTHETAT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BENJT:
    """
        name: .BENJT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BENJT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BENJT_NEXT:
    """
        name: .BENJT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BENJT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDEFIMEXT:
    """
        name: .BDEFIMEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDEFIMEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DEFIMEXTBON:
    """
        name: .DEFIMEXTBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DEFIMEXTBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DEFIMEXTBON8H:
    """
        name: .DEFIMEXTBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DEFIMEXTBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DEFIMEXTUSDTPI:
    """
        name: .DEFIMEXTUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DEFIMEXTUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _DEFIMEXTUSDTPI8H:
    """
        name: .DEFIMEXTUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".DEFIMEXTUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BALTMEXT:
    """
        name: .BALTMEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BALTMEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ALTMEXTBON:
    """
        name: .ALTMEXTBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ALTMEXTBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ALTMEXTBON8H:
    """
        name: .ALTMEXTBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ALTMEXTBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ALTMEXTUSDTPI:
    """
        name: .ALTMEXTUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ALTMEXTUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ALTMEXTUSDTPI8H:
    """
        name: .ALTMEXTUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ALTMEXTUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMETAMEXT:
    """
        name: .BMETAMEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMETAMEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _METAMEXTBON:
    """
        name: .METAMEXTBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".METAMEXTBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _METAMEXTBON8H:
    """
        name: .METAMEXTBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".METAMEXTBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _METAMEXTUSDTPI:
    """
        name: .METAMEXTUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".METAMEXTUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _METAMEXTUSDTPI8H:
    """
        name: .METAMEXTUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".METAMEXTUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AVAXUSDTPI:
    """
        name: .AVAXUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AVAXUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _AVAXUSDTPI8H:
    """
        name: .AVAXUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".AVAXUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LUNAUSDTPI:
    """
        name: .LUNAUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LUNAUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LUNAUSDTPI8H:
    """
        name: .LUNAUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LUNAUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPET:
    """
        name: .BAPET
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPET"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPET_NEXT:
    """
        name: .BAPET_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPET_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APEBON:
    """
        name: .APEBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APEBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APEBON8H:
    """
        name: .APEBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APEBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APEUSDTPI:
    """
        name: .APEUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APEUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APEUSDTPI8H:
    """
        name: .APEUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APEUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GMTBON:
    """
        name: .GMTBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GMTBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GMTBON8H:
    """
        name: .GMTBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GMTBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GMTUSDTPI:
    """
        name: .GMTUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GMTUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GMTUSDTPI8H:
    """
        name: .GMTUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GMTUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GMTUSDPI:
    """
        name: .GMTUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GMTUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GMTUSDPI8H:
    """
        name: .GMTUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GMTUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGMT:
    """
        name: .BGMT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGMT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGMT_NEXT:
    """
        name: .BGMT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGMT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGMTT:
    """
        name: .BGMTT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGMTT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGMTT_NEXT:
    """
        name: .BGMTT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGMTT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NEARBON:
    """
        name: .NEARBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NEARBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NEARBON8H:
    """
        name: .NEARBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NEARBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NEARUSDTPI:
    """
        name: .NEARUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NEARUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NEARUSDTPI8H:
    """
        name: .NEARUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NEARUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NEARUSDPI:
    """
        name: .NEARUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NEARUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NEARUSDPI8H:
    """
        name: .NEARUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NEARUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNEAR:
    """
        name: .BNEAR
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNEAR"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNEAR_NEXT:
    """
        name: .BNEAR_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNEAR_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNEART:
    """
        name: .BNEART
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNEART"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNEART_NEXT:
    """
        name: .BNEART_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNEART_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNA30M:
    """
        name: .BLUNA30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNA30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNAT30M:
    """
        name: .BLUNAT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNAT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPE:
    """
        name: .BAPE
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPE"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPE_NEXT:
    """
        name: .BAPE_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPE_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTRX:
    """
        name: .BTRX
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTRX"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTRX_NEXT:
    """
        name: .BTRX_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTRX_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGAL:
    """
        name: .BGAL
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGAL"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGAL_NEXT:
    """
        name: .BGAL_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGAL_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGALT:
    """
        name: .BGALT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGALT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGALT_NEXT:
    """
        name: .BGALT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGALT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GALBON:
    """
        name: .GALBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GALBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GALBON8H:
    """
        name: .GALBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GALBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APEUSDPI:
    """
        name: .APEUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APEUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APEUSDPI8H:
    """
        name: .APEUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APEUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _TRXUSDPI:
    """
        name: .TRXUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".TRXUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _TRXUSDPI8H:
    """
        name: .TRXUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".TRXUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GALUSDTPI:
    """
        name: .GALUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GALUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GALUSDTPI8H:
    """
        name: .GALUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GALUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GALUSDPI:
    """
        name: .GALUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GALUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _GALUSDPI8H:
    """
        name: .GALUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".GALUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNC:
    """
        name: .BLUNC
        precision: 1e-09
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNC"
    precision: int = 1e-09
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNC_NEXT:
    """
        name: .BLUNC_NEXT
        precision: 1e-09
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNC_NEXT"
    precision: int = 1e-09
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNCT:
    """
        name: .BLUNCT
        precision: 1e-09
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNCT"
    precision: int = 1e-09
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLUNCT_NEXT:
    """
        name: .BLUNCT_NEXT
        precision: 1e-09
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLUNCT_NEXT"
    precision: int = 1e-09
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDFI:
    """
        name: .BDFI
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDFI"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDFIT:
    """
        name: .BDFIT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDFIT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGRT:
    """
        name: .BGRT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGRT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURUSDPI:
    """
        name: .EURUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDCHFPI:
    """
        name: .USDCHFPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDCHFPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURCHFPI:
    """
        name: .EURCHFPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURCHFPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURTRYPI:
    """
        name: .EURTRYPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURTRYPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTRYPI:
    """
        name: .USDTRYPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTRYPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDINRPI:
    """
        name: .USDINRPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDINRPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDZARPI:
    """
        name: .USDZARPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDZARPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDBRLPI:
    """
        name: .USDBRLPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDBRLPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDMXNPI:
    """
        name: .USDMXNPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDMXNPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NZDUSDPI:
    """
        name: .NZDUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NZDUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDCNHPI:
    """
        name: .USDCNHPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDCNHPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDSEKPI:
    """
        name: .USDSEKPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDSEKPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURUSDPI8H:
    """
        name: .EURUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDCHFPI8H:
    """
        name: .USDCHFPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDCHFPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURCHFPI8H:
    """
        name: .EURCHFPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURCHFPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURTRYPI8H:
    """
        name: .EURTRYPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURTRYPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTRYPI8H:
    """
        name: .USDTRYPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTRYPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDINRPI8H:
    """
        name: .USDINRPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDINRPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDZARPI8H:
    """
        name: .USDZARPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDZARPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDBRLPI8H:
    """
        name: .USDBRLPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDBRLPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDMXNPI8H:
    """
        name: .USDMXNPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDMXNPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NZDUSDPI8H:
    """
        name: .NZDUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NZDUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDCNHPI8H:
    """
        name: .USDCNHPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDCNHPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDSEKPI8H:
    """
        name: .USDSEKPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDSEKPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURUSDTPI:
    """
        name: .EURUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTCHFPI:
    """
        name: .USDTCHFPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTCHFPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTTRYPI:
    """
        name: .USDTTRYPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTTRYPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTINRPI:
    """
        name: .USDTINRPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTINRPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTZARPI:
    """
        name: .USDTZARPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTZARPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTBRLPI:
    """
        name: .USDTBRLPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTBRLPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTMXNPI:
    """
        name: .USDTMXNPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTMXNPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NZDUSDTPI:
    """
        name: .NZDUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NZDUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTCNHPI:
    """
        name: .USDTCNHPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTCNHPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTSEKPI:
    """
        name: .USDTSEKPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTSEKPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _EURUSDTPI8H:
    """
        name: .EURUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".EURUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTCHFPI8H:
    """
        name: .USDTCHFPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTCHFPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTTRYPI8H:
    """
        name: .USDTTRYPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTTRYPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTINRPI8H:
    """
        name: .USDTINRPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTINRPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTZARPI8H:
    """
        name: .USDTZARPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTZARPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTBRLPI8H:
    """
        name: .USDTBRLPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTBRLPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTMXNPI8H:
    """
        name: .USDTMXNPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTMXNPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NZDUSDTPI8H:
    """
        name: .NZDUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NZDUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTCNHPI8H:
    """
        name: .USDTCNHPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTCNHPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDTSEKPI8H:
    """
        name: .USDTSEKPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDTSEKPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CHFBON:
    """
        name: .CHFBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CHFBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _TRYBON:
    """
        name: .TRYBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".TRYBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _INRBON:
    """
        name: .INRBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".INRBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ZARBON:
    """
        name: .ZARBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ZARBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BRLBON:
    """
        name: .BRLBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BRLBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MXNBON:
    """
        name: .MXNBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MXNBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NZDBON:
    """
        name: .NZDBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NZDBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CNHBON:
    """
        name: .CNHBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CNHBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SEKBON:
    """
        name: .SEKBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SEKBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CHFBON8H:
    """
        name: .CHFBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CHFBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _TRYBON8H:
    """
        name: .TRYBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".TRYBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _INRBON8H:
    """
        name: .INRBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".INRBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ZARBON8H:
    """
        name: .ZARBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ZARBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BRLBON8H:
    """
        name: .BRLBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BRLBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _MXNBON8H:
    """
        name: .MXNBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".MXNBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _NZDBON8H:
    """
        name: .NZDBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".NZDBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CNHBON8H:
    """
        name: .CNHBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CNHBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _SEKBON8H:
    """
        name: .SEKBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".SEKBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURUSD:
    """
        name: .BEURUSD
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURUSD"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURUSD"

    def __str__(self):
        return ".BEURUSD"

    def __call__(self):
        return ".BEURUSD"


_BEURUSD = _BEURUSD()
"""
    name: .BEURUSD
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDCHF:
    """
        name: .BUSDCHF
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDCHF"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDCHF"

    def __str__(self):
        return ".BUSDCHF"

    def __call__(self):
        return ".BUSDCHF"


_BUSDCHF = _BUSDCHF()
"""
    name: .BUSDCHF
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURCHF:
    """
        name: .BEURCHF
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURCHF"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURCHF"

    def __str__(self):
        return ".BEURCHF"

    def __call__(self):
        return ".BEURCHF"


_BEURCHF = _BEURCHF()
"""
    name: .BEURCHF
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURTRY:
    """
        name: .BEURTRY
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURTRY"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURTRY"

    def __str__(self):
        return ".BEURTRY"

    def __call__(self):
        return ".BEURTRY"


_BEURTRY = _BEURTRY()
"""
    name: .BEURTRY
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTRY:
    """
        name: .BUSDTRY
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTRY"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTRY"

    def __str__(self):
        return ".BUSDTRY"

    def __call__(self):
        return ".BUSDTRY"


_BUSDTRY = _BUSDTRY()
"""
    name: .BUSDTRY
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDINR:
    """
        name: .BUSDINR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDINR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDINR"

    def __str__(self):
        return ".BUSDINR"

    def __call__(self):
        return ".BUSDINR"


_BUSDINR = _BUSDINR()
"""
    name: .BUSDINR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDZAR:
    """
        name: .BUSDZAR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDZAR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDZAR"

    def __str__(self):
        return ".BUSDZAR"

    def __call__(self):
        return ".BUSDZAR"


_BUSDZAR = _BUSDZAR()
"""
    name: .BUSDZAR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDBRL:
    """
        name: .BUSDBRL
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDBRL"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDBRL"

    def __str__(self):
        return ".BUSDBRL"

    def __call__(self):
        return ".BUSDBRL"


_BUSDBRL = _BUSDBRL()
"""
    name: .BUSDBRL
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDMXN:
    """
        name: .BUSDMXN
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDMXN"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDMXN"

    def __str__(self):
        return ".BUSDMXN"

    def __call__(self):
        return ".BUSDMXN"


_BUSDMXN = _BUSDMXN()
"""
    name: .BUSDMXN
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNZDUSD:
    """
        name: .BNZDUSD
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNZDUSD"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNZDUSD"

    def __str__(self):
        return ".BNZDUSD"

    def __call__(self):
        return ".BNZDUSD"


_BNZDUSD = _BNZDUSD()
"""
    name: .BNZDUSD
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDCNH:
    """
        name: .BUSDCNH
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDCNH"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDCNH"

    def __str__(self):
        return ".BUSDCNH"

    def __call__(self):
        return ".BUSDCNH"


_BUSDCNH = _BUSDCNH()
"""
    name: .BUSDCNH
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDSEK:
    """
        name: .BUSDSEK
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDSEK"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDSEK"

    def __str__(self):
        return ".BUSDSEK"

    def __call__(self):
        return ".BUSDSEK"


_BUSDSEK = _BUSDSEK()
"""
    name: .BUSDSEK
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURUSD_NEXT:
    """
        name: .BEURUSD_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURUSD_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURUSD_NEXT"

    def __str__(self):
        return ".BEURUSD_NEXT"

    def __call__(self):
        return ".BEURUSD_NEXT"


_BEURUSD_NEXT = _BEURUSD_NEXT()
"""
    name: .BEURUSD_NEXT
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDCHF_NEXT:
    """
        name: .BUSDCHF_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDCHF_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDCHF_NEXT"

    def __str__(self):
        return ".BUSDCHF_NEXT"

    def __call__(self):
        return ".BUSDCHF_NEXT"


_BUSDCHF_NEXT = _BUSDCHF_NEXT()
"""
    name: .BUSDCHF_NEXT
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURCHF_NEXT:
    """
        name: .BEURCHF_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURCHF_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURCHF_NEXT"

    def __str__(self):
        return ".BEURCHF_NEXT"

    def __call__(self):
        return ".BEURCHF_NEXT"


_BEURCHF_NEXT = _BEURCHF_NEXT()
"""
    name: .BEURCHF_NEXT
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURTRY_NEXT:
    """
        name: .BEURTRY_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURTRY_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURTRY_NEXT"

    def __str__(self):
        return ".BEURTRY_NEXT"

    def __call__(self):
        return ".BEURTRY_NEXT"


_BEURTRY_NEXT = _BEURTRY_NEXT()
"""
    name: .BEURTRY_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTRY_NEXT:
    """
        name: .BUSDTRY_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTRY_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTRY_NEXT"

    def __str__(self):
        return ".BUSDTRY_NEXT"

    def __call__(self):
        return ".BUSDTRY_NEXT"


_BUSDTRY_NEXT = _BUSDTRY_NEXT()
"""
    name: .BUSDTRY_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDINR_NEXT:
    """
        name: .BUSDINR_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDINR_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDINR_NEXT"

    def __str__(self):
        return ".BUSDINR_NEXT"

    def __call__(self):
        return ".BUSDINR_NEXT"


_BUSDINR_NEXT = _BUSDINR_NEXT()
"""
    name: .BUSDINR_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDZAR_NEXT:
    """
        name: .BUSDZAR_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDZAR_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDZAR_NEXT"

    def __str__(self):
        return ".BUSDZAR_NEXT"

    def __call__(self):
        return ".BUSDZAR_NEXT"


_BUSDZAR_NEXT = _BUSDZAR_NEXT()
"""
    name: .BUSDZAR_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDBRL_NEXT:
    """
        name: .BUSDBRL_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDBRL_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDBRL_NEXT"

    def __str__(self):
        return ".BUSDBRL_NEXT"

    def __call__(self):
        return ".BUSDBRL_NEXT"


_BUSDBRL_NEXT = _BUSDBRL_NEXT()
"""
    name: .BUSDBRL_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDMXN_NEXT:
    """
        name: .BUSDMXN_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDMXN_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDMXN_NEXT"

    def __str__(self):
        return ".BUSDMXN_NEXT"

    def __call__(self):
        return ".BUSDMXN_NEXT"


_BUSDMXN_NEXT = _BUSDMXN_NEXT()
"""
    name: .BUSDMXN_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNZDUSD_NEXT:
    """
        name: .BNZDUSD_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNZDUSD_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNZDUSD_NEXT"

    def __str__(self):
        return ".BNZDUSD_NEXT"

    def __call__(self):
        return ".BNZDUSD_NEXT"


_BNZDUSD_NEXT = _BNZDUSD_NEXT()
"""
    name: .BNZDUSD_NEXT
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDCNH_NEXT:
    """
        name: .BUSDCNH_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDCNH_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDCNH_NEXT"

    def __str__(self):
        return ".BUSDCNH_NEXT"

    def __call__(self):
        return ".BUSDCNH_NEXT"


_BUSDCNH_NEXT = _BUSDCNH_NEXT()
"""
    name: .BUSDCNH_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDSEK_NEXT:
    """
        name: .BUSDSEK_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDSEK_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDSEK_NEXT"

    def __str__(self):
        return ".BUSDSEK_NEXT"

    def __call__(self):
        return ".BUSDSEK_NEXT"


_BUSDSEK_NEXT = _BUSDSEK_NEXT()
"""
    name: .BUSDSEK_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURUSDT:
    """
        name: .BEURUSDT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURUSDT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURUSDT"

    def __str__(self):
        return ".BEURUSDT"

    def __call__(self):
        return ".BEURUSDT"


_BEURUSDT = _BEURUSDT()
"""
    name: .BEURUSDT
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTCHF:
    """
        name: .BUSDTCHF
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTCHF"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTCHF"

    def __str__(self):
        return ".BUSDTCHF"

    def __call__(self):
        return ".BUSDTCHF"


_BUSDTCHF = _BUSDTCHF()
"""
    name: .BUSDTCHF
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTTRY:
    """
        name: .BUSDTTRY
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTTRY"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTTRY"

    def __str__(self):
        return ".BUSDTTRY"

    def __call__(self):
        return ".BUSDTTRY"


_BUSDTTRY = _BUSDTTRY()
"""
    name: .BUSDTTRY
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTINR:
    """
        name: .BUSDTINR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTINR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTINR"

    def __str__(self):
        return ".BUSDTINR"

    def __call__(self):
        return ".BUSDTINR"


_BUSDTINR = _BUSDTINR()
"""
    name: .BUSDTINR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTZAR:
    """
        name: .BUSDTZAR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTZAR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTZAR"

    def __str__(self):
        return ".BUSDTZAR"

    def __call__(self):
        return ".BUSDTZAR"


_BUSDTZAR = _BUSDTZAR()
"""
    name: .BUSDTZAR
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTBRL:
    """
        name: .BUSDTBRL
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTBRL"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTBRL"

    def __str__(self):
        return ".BUSDTBRL"

    def __call__(self):
        return ".BUSDTBRL"


_BUSDTBRL = _BUSDTBRL()
"""
    name: .BUSDTBRL
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTMXN:
    """
        name: .BUSDTMXN
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTMXN"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTMXN"

    def __str__(self):
        return ".BUSDTMXN"

    def __call__(self):
        return ".BUSDTMXN"


_BUSDTMXN = _BUSDTMXN()
"""
    name: .BUSDTMXN
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNZDUSDT:
    """
        name: .BNZDUSDT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNZDUSDT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNZDUSDT"

    def __str__(self):
        return ".BNZDUSDT"

    def __call__(self):
        return ".BNZDUSDT"


_BNZDUSDT = _BNZDUSDT()
"""
    name: .BNZDUSDT
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTCNH:
    """
        name: .BUSDTCNH
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTCNH"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTCNH"

    def __str__(self):
        return ".BUSDTCNH"

    def __call__(self):
        return ".BUSDTCNH"


_BUSDTCNH = _BUSDTCNH()
"""
    name: .BUSDTCNH
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTSEK:
    """
        name: .BUSDTSEK
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTSEK"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTSEK"

    def __str__(self):
        return ".BUSDTSEK"

    def __call__(self):
        return ".BUSDTSEK"


_BUSDTSEK = _BUSDTSEK()
"""
    name: .BUSDTSEK
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURUSDT_NEXT:
    """
        name: .BEURUSDT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURUSDT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURUSDT_NEXT"

    def __str__(self):
        return ".BEURUSDT_NEXT"

    def __call__(self):
        return ".BEURUSDT_NEXT"


_BEURUSDT_NEXT = _BEURUSDT_NEXT()
"""
    name: .BEURUSDT_NEXT
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTCHF_NEXT:
    """
        name: .BUSDTCHF_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTCHF_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTCHF_NEXT"

    def __str__(self):
        return ".BUSDTCHF_NEXT"

    def __call__(self):
        return ".BUSDTCHF_NEXT"


_BUSDTCHF_NEXT = _BUSDTCHF_NEXT()
"""
    name: .BUSDTCHF_NEXT
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTTRY_NEXT:
    """
        name: .BUSDTTRY_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTTRY_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTTRY_NEXT"

    def __str__(self):
        return ".BUSDTTRY_NEXT"

    def __call__(self):
        return ".BUSDTTRY_NEXT"


_BUSDTTRY_NEXT = _BUSDTTRY_NEXT()
"""
    name: .BUSDTTRY_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTINR_NEXT:
    """
        name: .BUSDTINR_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTINR_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTINR_NEXT"

    def __str__(self):
        return ".BUSDTINR_NEXT"

    def __call__(self):
        return ".BUSDTINR_NEXT"


_BUSDTINR_NEXT = _BUSDTINR_NEXT()
"""
    name: .BUSDTINR_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTZAR_NEXT:
    """
        name: .BUSDTZAR_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTZAR_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTZAR_NEXT"

    def __str__(self):
        return ".BUSDTZAR_NEXT"

    def __call__(self):
        return ".BUSDTZAR_NEXT"


_BUSDTZAR_NEXT = _BUSDTZAR_NEXT()
"""
    name: .BUSDTZAR_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTBRL_NEXT:
    """
        name: .BUSDTBRL_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTBRL_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTBRL_NEXT"

    def __str__(self):
        return ".BUSDTBRL_NEXT"

    def __call__(self):
        return ".BUSDTBRL_NEXT"


_BUSDTBRL_NEXT = _BUSDTBRL_NEXT()
"""
    name: .BUSDTBRL_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTMXN_NEXT:
    """
        name: .BUSDTMXN_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTMXN_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTMXN_NEXT"

    def __str__(self):
        return ".BUSDTMXN_NEXT"

    def __call__(self):
        return ".BUSDTMXN_NEXT"


_BUSDTMXN_NEXT = _BUSDTMXN_NEXT()
"""
    name: .BUSDTMXN_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNZDUSDT_NEXT:
    """
        name: .BNZDUSDT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNZDUSDT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNZDUSDT_NEXT"

    def __str__(self):
        return ".BNZDUSDT_NEXT"

    def __call__(self):
        return ".BNZDUSDT_NEXT"


_BNZDUSDT_NEXT = _BNZDUSDT_NEXT()
"""
    name: .BNZDUSDT_NEXT
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTCNH_NEXT:
    """
        name: .BUSDTCNH_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTCNH_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTCNH_NEXT"

    def __str__(self):
        return ".BUSDTCNH_NEXT"

    def __call__(self):
        return ".BUSDTCNH_NEXT"


_BUSDTCNH_NEXT = _BUSDTCNH_NEXT()
"""
    name: .BUSDTCNH_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTSEK_NEXT:
    """
        name: .BUSDTSEK_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTSEK_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTSEK_NEXT"

    def __str__(self):
        return ".BUSDTSEK_NEXT"

    def __call__(self):
        return ".BUSDTSEK_NEXT"


_BUSDTSEK_NEXT = _BUSDTSEK_NEXT()
"""
    name: .BUSDTSEK_NEXT
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BOP:
    """
        name: .BOP
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BOP"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BOP_NEXT:
    """
        name: .BOP_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BOP_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BOPT:
    """
        name: .BOPT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BOPT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BOPT_NEXT:
    """
        name: .BOPT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BOPT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _OPBON:
    """
        name: .OPBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".OPBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _OPBON8H:
    """
        name: .OPBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".OPBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _OPUSDTPI:
    """
        name: .OPUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".OPUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _OPUSDTPI8H:
    """
        name: .OPUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".OPUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _OPUSDPI:
    """
        name: .OPUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".OPUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _OPUSDPI8H:
    """
        name: .OPUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".OPUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDC:
    """
        name: .BUSDC
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDC"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDCT:
    """
        name: .BUSDCT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDCT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHPOWT:
    """
        name: .BETHPOWT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHPOWT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHPOWT_NEXT:
    """
        name: .BETHPOWT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHPOWT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHPOWT30M:
    """
        name: .BETHPOWT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHPOWT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BALTMEXT30M:
    """
        name: .BALTMEXT30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BALTMEXT30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDEFIMEXT30M:
    """
        name: .BDEFIMEXT30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDEFIMEXT30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMETAMEXT30M:
    """
        name: .BMETAMEXT30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMETAMEXT30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDC_NEXT:
    """
        name: .BUSDC_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDC_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDCT_NEXT:
    """
        name: .BUSDCT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDCT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BKLAY:
    """
        name: .BKLAY
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BKLAY"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BKLAY_NEXT:
    """
        name: .BKLAY_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BKLAY_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BKLAYT:
    """
        name: .BKLAYT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BKLAYT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BKLAYT_NEXT:
    """
        name: .BKLAYT_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BKLAYT_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _KLAYUSDTPI:
    """
        name: .KLAYUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".KLAYUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _KLAYUSDTPI8H:
    """
        name: .KLAYUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".KLAYUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _KLAYUSDPI:
    """
        name: .KLAYUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".KLAYUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _KLAYUSDPI8H:
    """
        name: .KLAYUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".KLAYUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _KLAYBON:
    """
        name: .KLAYBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".KLAYBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _KLAYBON8H:
    """
        name: .KLAYBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".KLAYBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSTETH:
    """
        name: .BSTETH
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSTETH"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSTETHT:
    """
        name: .BSTETHT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSTETHT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDAI:
    """
        name: .BDAI
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDAI"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BDAIT:
    """
        name: .BDAIT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BDAIT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBUSD:
    """
        name: .BBUSD
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBUSD"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBUSDT:
    """
        name: .BBUSDT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBUSDT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BWBTC:
    """
        name: .BWBTC
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BWBTC"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BWBTCT:
    """
        name: .BWBTCT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BWBTCT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCRO:
    """
        name: .BCRO
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCRO"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BCROT:
    """
        name: .BCROT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BCROT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BQNT:
    """
        name: .BQNT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BQNT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BQNTT:
    """
        name: .BQNTT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BQNTT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BOKB:
    """
        name: .BOKB
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BOKB"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BOKBT:
    """
        name: .BOKBT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BOKBT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLEO:
    """
        name: .BLEO
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLEO"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLEOT:
    """
        name: .BLEOT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLEOT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAAVE:
    """
        name: .BAAVE
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAAVE"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMANA:
    """
        name: .BMANA
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMANA"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXLM:
    """
        name: .BXLM
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXLM"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BVET:
    """
        name: .BVET
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BVET"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFIL:
    """
        name: .BFIL
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFIL"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXTZ:
    """
        name: .BXTZ
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXTZ"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMKR:
    """
        name: .BMKR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMKR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFLOW:
    """
        name: .BFLOW
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFLOW"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFLOWT:
    """
        name: .BFLOWT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFLOWT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BHBAR:
    """
        name: .BHBAR
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BHBAR"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BHBART:
    """
        name: .BHBART
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BHBART"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEGLD:
    """
        name: .BEGLD
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEGLD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEGLDT:
    """
        name: .BEGLDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEGLDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTUSD:
    """
        name: .BTUSD
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTUSD"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTUSDT:
    """
        name: .BTUSDT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTUSDT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDP:
    """
        name: .BUSDP
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDP"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BHNT:
    """
        name: .BHNT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BHNT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BHNTT:
    """
        name: .BHNTT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BHNTT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BIOTA:
    """
        name: .BIOTA
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BIOTA"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BIOTAT:
    """
        name: .BIOTAT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BIOTAT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXEC:
    """
        name: .BXEC
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXEC"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXECT:
    """
        name: .BXECT
        precision: 1e-08
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXECT"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFTTT:
    """
        name: .BFTTT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFTTT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDCHF30M:
    """
        name: .BUSDCHF30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDCHF30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDCHF30M"

    def __str__(self):
        return ".BUSDCHF30M"

    def __call__(self):
        return ".BUSDCHF30M"


_BUSDCHF30M = _BUSDCHF30M()
"""
    name: .BUSDCHF30M
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURCHF30M:
    """
        name: .BEURCHF30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURCHF30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURCHF30M"

    def __str__(self):
        return ".BEURCHF30M"

    def __call__(self):
        return ".BEURCHF30M"


_BEURCHF30M = _BEURCHF30M()
"""
    name: .BEURCHF30M
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURTRY30M:
    """
        name: .BEURTRY30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURTRY30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURTRY30M"

    def __str__(self):
        return ".BEURTRY30M"

    def __call__(self):
        return ".BEURTRY30M"


_BEURTRY30M = _BEURTRY30M()
"""
    name: .BEURTRY30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTRY30M:
    """
        name: .BUSDTRY30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTRY30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTRY30M"

    def __str__(self):
        return ".BUSDTRY30M"

    def __call__(self):
        return ".BUSDTRY30M"


_BUSDTRY30M = _BUSDTRY30M()
"""
    name: .BUSDTRY30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDINR30M:
    """
        name: .BUSDINR30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDINR30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDINR30M"

    def __str__(self):
        return ".BUSDINR30M"

    def __call__(self):
        return ".BUSDINR30M"


_BUSDINR30M = _BUSDINR30M()
"""
    name: .BUSDINR30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDZAR30M:
    """
        name: .BUSDZAR30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDZAR30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDZAR30M"

    def __str__(self):
        return ".BUSDZAR30M"

    def __call__(self):
        return ".BUSDZAR30M"


_BUSDZAR30M = _BUSDZAR30M()
"""
    name: .BUSDZAR30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDBRL30M:
    """
        name: .BUSDBRL30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDBRL30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDBRL30M"

    def __str__(self):
        return ".BUSDBRL30M"

    def __call__(self):
        return ".BUSDBRL30M"


_BUSDBRL30M = _BUSDBRL30M()
"""
    name: .BUSDBRL30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDMXN30M:
    """
        name: .BUSDMXN30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDMXN30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDMXN30M"

    def __str__(self):
        return ".BUSDMXN30M"

    def __call__(self):
        return ".BUSDMXN30M"


_BUSDMXN30M = _BUSDMXN30M()
"""
    name: .BUSDMXN30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNZDUSD30M:
    """
        name: .BNZDUSD30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNZDUSD30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNZDUSD30M"

    def __str__(self):
        return ".BNZDUSD30M"

    def __call__(self):
        return ".BNZDUSD30M"


_BNZDUSD30M = _BNZDUSD30M()
"""
    name: .BNZDUSD30M
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDCNH30M:
    """
        name: .BUSDCNH30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDCNH30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDCNH30M"

    def __str__(self):
        return ".BUSDCNH30M"

    def __call__(self):
        return ".BUSDCNH30M"


_BUSDCNH30M = _BUSDCNH30M()
"""
    name: .BUSDCNH30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDSEK30M:
    """
        name: .BUSDSEK30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDSEK30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDSEK30M"

    def __str__(self):
        return ".BUSDSEK30M"

    def __call__(self):
        return ".BUSDSEK30M"


_BUSDSEK30M = _BUSDSEK30M()
"""
    name: .BUSDSEK30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTCHF30M:
    """
        name: .BUSDTCHF30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTCHF30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTCHF30M"

    def __str__(self):
        return ".BUSDTCHF30M"

    def __call__(self):
        return ".BUSDTCHF30M"


_BUSDTCHF30M = _BUSDTCHF30M()
"""
    name: .BUSDTCHF30M
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNZDUSDT30M:
    """
        name: .BNZDUSDT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNZDUSDT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BNZDUSDT30M"

    def __str__(self):
        return ".BNZDUSDT30M"

    def __call__(self):
        return ".BNZDUSDT30M"


_BNZDUSDT30M = _BNZDUSDT30M()
"""
    name: .BNZDUSDT30M
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTCNH30M:
    """
        name: .BUSDTCNH30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTCNH30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTCNH30M"

    def __str__(self):
        return ".BUSDTCNH30M"

    def __call__(self):
        return ".BUSDTCNH30M"


_BUSDTCNH30M = _BUSDTCNH30M()
"""
    name: .BUSDTCNH30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSANDT30M:
    """
        name: .BSANDT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSANDT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BNEART30M:
    """
        name: .BNEART30M
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BNEART30M"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMANAT30M:
    """
        name: .BMANAT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMANAT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BSHIBT30M:
    """
        name: .BSHIBT30M
        precision: 1e-09
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BSHIBT30M"
    precision: int = 1e-09
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BOPT30M:
    """
        name: .BOPT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BOPT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGALT30M:
    """
        name: .BGALT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGALT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BGAL30M:
    """
        name: .BGAL30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BGAL30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BTRX30M:
    """
        name: .BTRX30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BTRX30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BOP30M:
    """
        name: .BOP30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BOP30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPE30M:
    """
        name: .BAPE30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPE30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFTMT30M:
    """
        name: .BFTMT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFTMT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPT:
    """
        name: .BAPT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPT_NEXT:
    """
        name: .BAPT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPT30M:
    """
        name: .BAPT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPTT:
    """
        name: .BAPTT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPTT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPTT_NEXT:
    """
        name: .BAPTT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPTT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BAPTT30M:
    """
        name: .BAPTT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BAPTT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APTBON:
    """
        name: .APTBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APTBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APTBON8H:
    """
        name: .APTBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APTBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APTUSDTPI:
    """
        name: .APTUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APTUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APTUSDTPI8H:
    """
        name: .APTUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APTUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APTUSDPI:
    """
        name: .APTUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APTUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _APTUSDPI8H:
    """
        name: .APTUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".APTUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFTT:
    """
        name: .BFTT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFTT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFTT_NEXT:
    """
        name: .BFTT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFTT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFTTT_NEXT:
    """
        name: .BFTTT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFTTT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTTBON:
    """
        name: .FTTBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTTBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTTBON8H:
    """
        name: .FTTBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTTBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTTUSDTPI:
    """
        name: .FTTUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTTUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTTUSDTPI8H:
    """
        name: .FTTUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTTUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTTUSDPI:
    """
        name: .FTTUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTTUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FTTUSDPI8H:
    """
        name: .FTTUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FTTUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMEXBON:
    """
        name: .BMEXBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMEXBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMEXBON8H:
    """
        name: .BMEXBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMEXBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMEXUSDTPI:
    """
        name: .BMEXUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMEXUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMEXUSDTPI8H:
    """
        name: .BMEXUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMEXUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMEXUSDPI:
    """
        name: .BMEXUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMEXUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BMEXUSDPI8H:
    """
        name: .BMEXUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BMEXUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBMEXT:
    """
        name: .BBMEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBMEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBMEXT_NEXT:
    """
        name: .BBMEXT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBMEXT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBMEX:
    """
        name: .BBMEX
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBMEX"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BBMEX_NEXT:
    """
        name: .BBMEX_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BBMEX_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CROBON:
    """
        name: .CROBON
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CROBON"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CROBON8H:
    """
        name: .CROBON8H
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CROBON8H"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CROUSDTPI:
    """
        name: .CROUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CROUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CROUSDTPI8H:
    """
        name: .CROUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CROUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CROUSDPI:
    """
        name: .CROUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CROUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _CROUSDPI8H:
    """
        name: .CROUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".CROUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFTT30M:
    """
        name: .BFTT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFTT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFTTT30M:
    """
        name: .BFTTT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFTTT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHYLD:
    """
        name: .BETHYLD
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHYLD"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURUSD30M:
    """
        name: .BEURUSD30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURUSD30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURUSD30M"

    def __str__(self):
        return ".BEURUSD30M"

    def __call__(self):
        return ".BEURUSD30M"


_BEURUSD30M = _BEURUSD30M()
"""
    name: .BEURUSD30M
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BEURUSDT30M:
    """
        name: .BEURUSDT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BEURUSDT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BEURUSDT30M"

    def __str__(self):
        return ".BEURUSDT30M"

    def __call__(self):
        return ".BEURUSDT30M"


_BEURUSDT30M = _BEURUSDT30M()
"""
    name: .BEURUSDT30M
    precision: 1e-05
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTBRL30M:
    """
        name: .BUSDTBRL30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTBRL30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTBRL30M"

    def __str__(self):
        return ".BUSDTBRL30M"

    def __call__(self):
        return ".BUSDTBRL30M"


_BUSDTBRL30M = _BUSDTBRL30M()
"""
    name: .BUSDTBRL30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTINR30M:
    """
        name: .BUSDTINR30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTINR30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTINR30M"

    def __str__(self):
        return ".BUSDTINR30M"

    def __call__(self):
        return ".BUSDTINR30M"


_BUSDTINR30M = _BUSDTINR30M()
"""
    name: .BUSDTINR30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTMXN30M:
    """
        name: .BUSDTMXN30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTMXN30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTMXN30M"

    def __str__(self):
        return ".BUSDTMXN30M"

    def __call__(self):
        return ".BUSDTMXN30M"


_BUSDTMXN30M = _BUSDTMXN30M()
"""
    name: .BUSDTMXN30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTSEK30M:
    """
        name: .BUSDTSEK30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTSEK30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTSEK30M"

    def __str__(self):
        return ".BUSDTSEK30M"

    def __call__(self):
        return ".BUSDTSEK30M"


_BUSDTSEK30M = _BUSDTSEK30M()
"""
    name: .BUSDTSEK30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTTRY30M:
    """
        name: .BUSDTTRY30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTTRY30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTTRY30M"

    def __str__(self):
        return ".BUSDTTRY30M"

    def __call__(self):
        return ".BUSDTTRY30M"


_BUSDTTRY30M = _BUSDTTRY30M()
"""
    name: .BUSDTTRY30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BUSDTZAR30M:
    """
        name: .BUSDTZAR30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BUSDTZAR30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return ".BUSDTZAR30M"

    def __str__(self):
        return ".BUSDTZAR30M"

    def __call__(self):
        return ".BUSDTZAR30M"


_BUSDTZAR30M = _BUSDTZAR30M()
"""
    name: .BUSDTZAR30M
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFLRT:
    """
        name: .BFLRT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFLRT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFLRT_NEXT:
    """
        name: .BFLRT_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFLRT_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFLRT30M:
    """
        name: .BFLRT30M
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFLRT30M"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FLRBON:
    """
        name: .FLRBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FLRBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FLRBON8H:
    """
        name: .FLRBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FLRBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FLRUSDTPI:
    """
        name: .FLRUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FLRUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FLRUSDTPI8H:
    """
        name: .FLRUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FLRUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FLRUSDPI:
    """
        name: .FLRUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FLRUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _FLRUSDPI8H:
    """
        name: .FLRUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".FLRUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFLR:
    """
        name: .BFLR
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFLR"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BFLR_NEXT:
    """
        name: .BFLR_NEXT
        precision: 0.0001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BFLR_NEXT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    precision: 0.0001
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class ADAH23:
    """
        name: ADAH23
        precision: 1e-08
        minimum_margin: None
        initial_margin: 0.05
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "ADAH23"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = 0.05
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADAH23"

    def __str__(self):
        return "ADAH23"

    def __call__(self):
        return "ADAH23"


ADAH23 = ADAH23()
"""
    name: ADAH23
    precision: 1e-08
    minimum_margin: None
    initial_margin: 0.05
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XRPH23:
    """
        name: XRPH23
        precision: 1e-08
        minimum_margin: None
        initial_margin: 0.05
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "XRPH23"
    precision: int = 1e-08
    minimum_margin: float = None
    initial_margin: float = 0.05
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRPH23"

    def __str__(self):
        return "XRPH23"

    def __call__(self):
        return "XRPH23"


XRPH23 = XRPH23()
"""
    name: XRPH23
    precision: 1e-08
    minimum_margin: None
    initial_margin: 0.05
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class FLRUSDTH23:
    """
        name: FLRUSDTH23
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.5
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "FLRUSDTH23"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.5
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLRUSDTH23"

    def __str__(self):
        return "FLRUSDTH23"

    def __call__(self):
        return "FLRUSDTH23"


FLRUSDTH23 = FLRUSDTH23()
"""
    name: FLRUSDTH23
    precision: 0.0001
    minimum_margin: None
    initial_margin: 0.5
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class KLAYUSD:
    """
        name: KLAYUSD
        precision: 1e-05
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 1
        maximum_order_size: 500000
        margin: True
    """
    name: str = "KLAYUSD"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 1
    maximum_order_size: float = 500000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 1
    maximum_order_size: 500000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class KLAYUSDT:
    """
        name: KLAYUSDT
        precision: 1e-05
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "KLAYUSDT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XRPUSD:
    """
        name: XRPUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 100000000
        margin: True
    """
    name: str = "XRPUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 100000000
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


XRPUSD = XRPUSD()
"""
    name: XRPUSD
    precision: 0.0001
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 100000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BCHUSD:
    """
        name: BCHUSD
        precision: 0.05
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 100000000
        margin: True
    """
    name: str = "BCHUSD"
    precision: int = 0.05
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 100000000
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
    precision: 0.05
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 100000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DOGEUSD:
    """
        name: DOGEUSD
        precision: 1e-05
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 5000000
        margin: True
    """
    name: str = "DOGEUSD"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 5000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 5000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BNBUSD:
    """
        name: BNBUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 1000000
        margin: True
    """
    name: str = "BNBUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 1000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 1000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LINKUSD:
    """
        name: LINKUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 1000000
        margin: True
    """
    name: str = "LINKUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 1000000
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
    precision: 0.001
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 1000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SOLUSD:
    """
        name: SOLUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 1000000
        margin: True
    """
    name: str = "SOLUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 1000000
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
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 1000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class APTUSD:
    """
        name: APTUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 1000000
        margin: True
    """
    name: str = "APTUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 1000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 1000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BMEXUSD:
    """
        name: BMEXUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 1000000
        margin: True
    """
    name: str = "BMEXUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 1000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 1000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class CROUSD:
    """
        name: CROUSD
        precision: 1e-05
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 5000000
        margin: True
    """
    name: str = "CROUSD"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 5000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 5000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class FLRUSD:
    """
        name: FLRUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 500000
        margin: True
    """
    name: str = "FLRUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 500000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 500000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DOGEUSDT:
    """
        name: DOGEUSDT
        precision: 1e-05
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 10000000000
        margin: True
    """
    name: str = "DOGEUSDT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 10000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 10000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DOTUSDT:
    """
        name: DOTUSDT
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "DOTUSDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
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
    precision: 0.001
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ADAUSDT:
    """
        name: ADAUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "ADAUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
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
    precision: 0.0001
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BNBUSDT:
    """
        name: BNBUSDT
        precision: 0.01
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "BNBUSDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SOLUSDT:
    """
        name: SOLUSDT
        precision: 0.01
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "SOLUSDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ADAUSD:
    """
        name: ADAUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1
        maximum_order_size: 500000
        margin: True
    """
    name: str = "ADAUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1
    maximum_order_size: float = 500000
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
    precision: 0.0001
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1
    maximum_order_size: 500000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class EOSUSD:
    """
        name: EOSUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1
        maximum_order_size: 500000
        margin: True
    """
    name: str = "EOSUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1
    maximum_order_size: float = 500000
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
    initial_margin: 0.03
    minimum_order_size: 1
    maximum_order_size: 500000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XRPUSDT:
    """
        name: XRPUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "XRPUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
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
    precision: 0.0001
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BCHUSDT:
    """
        name: BCHUSDT
        precision: 0.05
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "BCHUSDT"
    precision: int = 0.05
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class APEUSDT:
    """
        name: APEUSDT
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "APEUSDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class GMTUSDT:
    """
        name: GMTUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "GMTUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class GMTUSD:
    """
        name: GMTUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1
        maximum_order_size: 500000
        margin: True
    """
    name: str = "GMTUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1
    maximum_order_size: float = 500000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1
    maximum_order_size: 500000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class NEARUSD:
    """
        name: NEARUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1
        maximum_order_size: 500000
        margin: True
    """
    name: str = "NEARUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1
    maximum_order_size: float = 500000
    margin: bool = True

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
    initial_margin: 0.03
    minimum_order_size: 1
    maximum_order_size: 500000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class APTUSDT:
    """
        name: APTUSDT
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "APTUSDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BMEXUSDT:
    """
        name: BMEXUSDT
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "BMEXUSDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class CROUSDT:
    """
        name: CROUSDT
        precision: 1e-05
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 10000000000
        margin: True
    """
    name: str = "CROUSDT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 10000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 10000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class FLRUSDT:
    """
        name: FLRUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "FLRUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LUNAUSD:
    """
        name: LUNAUSD
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.04
        minimum_order_size: 1
        maximum_order_size: 500000
        margin: True
    """
    name: str = "LUNAUSD"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.04
    minimum_order_size: float = 1
    maximum_order_size: float = 500000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.04
    minimum_order_size: 1
    maximum_order_size: 500000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class DOTUSD:
    """
        name: DOTUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.04
        minimum_order_size: 1
        maximum_order_size: 1000000
        margin: True
    """
    name: str = "DOTUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.04
    minimum_order_size: float = 1
    maximum_order_size: float = 1000000
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
    precision: 0.001
    minimum_margin: None
    initial_margin: 0.04
    minimum_order_size: 1
    maximum_order_size: 1000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class MATICUSDT:
    """
        name: MATICUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.05
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "MATICUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.05
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    initial_margin: 0.05
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AVAXUSD:
    """
        name: AVAXUSD
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.05
        minimum_order_size: 1
        maximum_order_size: 500000
        margin: True
    """
    name: str = "AVAXUSD"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.05
    minimum_order_size: float = 1
    maximum_order_size: float = 500000
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
    precision: 0.001
    minimum_margin: None
    initial_margin: 0.05
    minimum_order_size: 1
    maximum_order_size: 500000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AXSUSD:
    """
        name: AXSUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: 0.05
        minimum_order_size: 1
        maximum_order_size: 1000000
        margin: True
    """
    name: str = "AXSUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = 0.05
    minimum_order_size: float = 1
    maximum_order_size: float = 1000000
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
    precision: 0.01
    minimum_margin: None
    initial_margin: 0.05
    minimum_order_size: 1
    maximum_order_size: 1000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AVAXUSDT:
    """
        name: AVAXUSDT
        precision: 0.001
        minimum_margin: None
        initial_margin: 0.05
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "AVAXUSDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 0.05
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.05
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LUNAUSDT:
    """
        name: LUNAUSDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: 0.05
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "LUNAUSDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 0.05
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.05
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class UNI_USDT:
    """
        name: UNI_USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 10000000
        maximum_order_size: 10000000000000
        margin: True
    """
    name: str = "UNI_USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 10000000
    maximum_order_size: float = 10000000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 10000000
    maximum_order_size: 10000000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LINK_USDT:
    """
        name: LINK_USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 10000000
        maximum_order_size: 10000000000000
        margin: True
    """
    name: str = "LINK_USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 10000000
    maximum_order_size: float = 10000000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 10000000
    maximum_order_size: 10000000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class MATIC_USDT:
    """
        name: MATIC_USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 100000000
        maximum_order_size: 100000000000000
        margin: True
    """
    name: str = "MATIC_USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 100000000
    maximum_order_size: float = 100000000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 100000000
    maximum_order_size: 100000000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class AXS_USDT:
    """
        name: AXS_USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 1000000
        maximum_order_size: 1000000000000
        margin: True
    """
    name: str = "AXS_USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 1000000
    maximum_order_size: float = 1000000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 1000000
    maximum_order_size: 1000000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class APE_USDT:
    """
        name: APE_USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 10000000
        maximum_order_size: 10000000000000
        margin: True
    """
    name: str = "APE_USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 10000000
    maximum_order_size: float = 10000000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 10000000
    maximum_order_size: 10000000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class TRX_USDT:
    """
        name: TRX_USDT
        precision: 0.0001
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 100000000
        maximum_order_size: 10000000000000
        margin: True
    """
    name: str = "TRX_USDT"
    precision: int = 0.0001
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 100000000
    maximum_order_size: float = 10000000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 100000000
    maximum_order_size: 10000000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class SOL_USDT:
    """
        name: SOL_USDT
        precision: 0.01
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 1000000
        maximum_order_size: 10000000000000
        margin: True
    """
    name: str = "SOL_USDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 1000000
    maximum_order_size: float = 10000000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 1000000
    maximum_order_size: 10000000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class BMEX_USDT:
    """
        name: BMEX_USDT
        precision: 0.001
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 1000000
        maximum_order_size: 1000000000000
        margin: True
    """
    name: str = "BMEX_USDT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 1000000
    maximum_order_size: float = 1000000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 1000000
    maximum_order_size: 1000000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class _XBT:
    """
        name: .XBT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XBT30M:
    """
        name: .XBT30M
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBT30M"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XBTBON:
    """
        name: .XBTBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBTBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XBTBON8H:
    """
        name: .XBTBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBTBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XBTUSDPI:
    """
        name: .XBTUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBTUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XBTUSDPI8H:
    """
        name: .XBTUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBTUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXBT:
    """
        name: .BXBT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXBT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXBT30M:
    """
        name: .BXBT30M
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXBT30M"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXBT_NEXT:
    """
        name: .BXBT_NEXT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXBT_NEXT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXBTEUR:
    """
        name: .BXBTEUR
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXBTEUR"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXBTEUR_NEXT:
    """
        name: .BXBTEUR_NEXT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXBTEUR_NEXT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XBTEURPI:
    """
        name: .XBTEURPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBTEURPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XBTEURPI8H:
    """
        name: .XBTEURPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBTEURPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXBTEUR30M:
    """
        name: .BXBTEUR30M
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXBTEUR30M"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXBTT:
    """
        name: .BXBTT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXBTT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXBTT_NEXT:
    """
        name: .BXBTT_NEXT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXBTT_NEXT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BXBTT30M:
    """
        name: .BXBTT30M
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BXBTT30M"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XBTUSDTPI:
    """
        name: .XBTUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBTUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _XBTUSDTPI8H:
    """
        name: .XBTUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".XBTUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BVOL:
    """
        name: .BVOL
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BVOL"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BVOL24H:
    """
        name: .BVOL24H
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BVOL24H"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BVOL7D:
    """
        name: .BVOL7D
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BVOL7D"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ETHBON:
    """
        name: .ETHBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ETHBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ETHBON8H:
    """
        name: .ETHBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ETHBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ETHUSDPI:
    """
        name: .ETHUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ETHUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ETHUSDPI8H:
    """
        name: .ETHUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ETHUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETH:
    """
        name: .BETH
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETH"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETH30M:
    """
        name: .BETH30M
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETH30M"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHXBT:
    """
        name: .BETHXBT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHXBT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHXBT30M:
    """
        name: .BETHXBT30M
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHXBT30M"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETH_NEXT:
    """
        name: .BETH_NEXT
        precision: 0.01
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETH_NEXT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHXBT_NEXT:
    """
        name: .BETHXBT_NEXT
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHXBT_NEXT"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHT:
    """
        name: .BETHT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHT_NEXT:
    """
        name: .BETHT_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHT_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETHT30M:
    """
        name: .BETHT30M
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETHT30M"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ETHUSDTPI:
    """
        name: .ETHUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ETHUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ETHUSDTPI8H:
    """
        name: .ETHUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ETHUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ETHUSD_ETHPI:
    """
        name: .ETHUSD_ETHPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ETHUSD_ETHPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _ETHUSD_ETHPI8H:
    """
        name: .ETHUSD_ETHPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".ETHUSD_ETHPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BETC:
    """
        name: .BETC
        precision: 1e-05
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BETC"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LTCBON:
    """
        name: .LTCBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LTCBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LTCBON8H:
    """
        name: .LTCBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LTCBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLTCXBT:
    """
        name: .BLTCXBT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLTCXBT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLTCXBT30M:
    """
        name: .BLTCXBT30M
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLTCXBT30M"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLTCXBT_NEXT:
    """
        name: .BLTCXBT_NEXT
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLTCXBT_NEXT"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLTC:
    """
        name: .BLTC
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLTC"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LTCUSDPI:
    """
        name: .LTCUSDPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LTCUSDPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LTCUSDPI8H:
    """
        name: .LTCUSDPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LTCUSDPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLTC_NEXT:
    """
        name: .BLTC_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLTC_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLTCT:
    """
        name: .BLTCT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLTCT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _BLTCT_NEXT:
    """
        name: .BLTCT_NEXT
        precision: 0.001
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".BLTCT_NEXT"
    precision: int = 0.001
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LTCUSDTPI:
    """
        name: .LTCUSDTPI
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LTCUSDTPI"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _LTCUSDTPI8H:
    """
        name: .LTCUSDTPI8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".LTCUSDTPI8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDBON:
    """
        name: .USDBON
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDBON"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class _USDBON8H:
    """
        name: .USDBON8H
        precision: 1e-06
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = ".USDBON8H"
    precision: int = 1e-06
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

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
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


@dataclass(slots=True, frozen=True)
class XBTUSD:
    """
        name: XBTUSD
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 100
        maximum_order_size: 10000000
        margin: True
    """
    name: str = "XBTUSD"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 100
    maximum_order_size: float = 10000000
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


XBTUSD = XBTUSD()
"""
    name: XBTUSD
    precision: 0.5
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 100
    maximum_order_size: 10000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTUSDT:
    """
        name: XBTUSDT
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "XBTUSDT"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
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
    precision: 0.5
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTEUR:
    """
        name: XBTEUR
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 100
        maximum_order_size: 10000000
        margin: True
    """
    name: str = "XBTEUR"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 100
    maximum_order_size: float = 10000000
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


XBTEUR = XBTEUR()
"""
    name: XBTEUR
    precision: 0.5
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 100
    maximum_order_size: 10000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTF23:
    """
        name: XBTF23
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 100
        maximum_order_size: 10000000
        margin: True
    """
    name: str = "XBTF23"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 100
    maximum_order_size: float = 10000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTF23"

    def __str__(self):
        return "XBTF23"

    def __call__(self):
        return "XBTF23"


XBTF23 = XBTF23()
"""
    name: XBTF23
    precision: 0.5
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 100
    maximum_order_size: 10000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTG23:
    """
        name: XBTG23
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 100
        maximum_order_size: 10000000
        margin: True
    """
    name: str = "XBTG23"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 100
    maximum_order_size: float = 10000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTG23"

    def __str__(self):
        return "XBTG23"

    def __call__(self):
        return "XBTG23"


XBTG23 = XBTG23()
"""
    name: XBTG23
    precision: 0.5
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 100
    maximum_order_size: 10000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTH23:
    """
        name: XBTH23
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 100
        maximum_order_size: 10000000
        margin: True
    """
    name: str = "XBTH23"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 100
    maximum_order_size: float = 10000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTH23"

    def __str__(self):
        return "XBTH23"

    def __call__(self):
        return "XBTH23"


XBTH23 = XBTH23()
"""
    name: XBTH23
    precision: 0.5
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 100
    maximum_order_size: 10000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTUSDTH23:
    """
        name: XBTUSDTH23
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "XBTUSDTH23"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XBTUSDTH23"

    def __str__(self):
        return "XBTUSDTH23"

    def __call__(self):
        return "XBTUSDTH23"


XBTUSDTH23 = XBTUSDTH23()
"""
    name: XBTUSDTH23
    precision: 0.5
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTM23:
    """
        name: XBTM23
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 100
        maximum_order_size: 10000000
        margin: True
    """
    name: str = "XBTM23"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 100
    maximum_order_size: float = 10000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 100
    maximum_order_size: 10000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTUSDTM23:
    """
        name: XBTUSDTM23
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "XBTUSDTM23"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTU23:
    """
        name: XBTU23
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 100
        maximum_order_size: 10000000
        margin: True
    """
    name: str = "XBTU23"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 100
    maximum_order_size: float = 10000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 100
    maximum_order_size: 10000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBTUSDTU23:
    """
        name: XBTUSDTU23
        precision: 0.5
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "XBTUSDTU23"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class XBT_USDT:
    """
        name: XBT_USDT
        precision: 0.5
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 10000
        maximum_order_size: 100000000000
        margin: True
    """
    name: str = "XBT_USDT"
    precision: int = 0.5
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 10000
    maximum_order_size: float = 100000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 10000
    maximum_order_size: 100000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHUSD:
    """
        name: ETHUSD
        precision: 0.05
        minimum_margin: None
        initial_margin: 0.01
        minimum_order_size: 1
        maximum_order_size: 10000000
        margin: True
    """
    name: str = "ETHUSD"
    precision: int = 0.05
    minimum_margin: float = None
    initial_margin: float = 0.01
    minimum_order_size: float = 1
    maximum_order_size: float = 10000000
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


ETHUSD = ETHUSD()
"""
    name: ETHUSD
    precision: 0.05
    minimum_margin: None
    initial_margin: 0.01
    minimum_order_size: 1
    maximum_order_size: 10000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHUSDT:
    """
        name: ETHUSDT
        precision: 0.05
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "ETHUSDT"
    precision: int = 0.05
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
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
    precision: 0.05
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHUSD_ETH:
    """
        name: ETHUSD_ETH
        precision: 0.05
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 100000000
        margin: True
    """
    name: str = "ETHUSD_ETH"
    precision: int = 0.05
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 100000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 100000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHH23:
    """
        name: ETHH23
        precision: 1e-05
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "ETHH23"
    precision: int = 1e-05
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHH23"

    def __str__(self):
        return "ETHH23"

    def __call__(self):
        return "ETHH23"


ETHH23 = ETHH23()
"""
    name: ETHH23
    precision: 1e-05
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHUSDH23:
    """
        name: ETHUSDH23
        precision: 0.05
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 10000000
        margin: True
    """
    name: str = "ETHUSDH23"
    precision: int = 0.05
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 10000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHUSDH23"

    def __str__(self):
        return "ETHUSDH23"

    def __call__(self):
        return "ETHUSDH23"


ETHUSDH23 = ETHUSDH23()
"""
    name: ETHUSDH23
    precision: 0.05
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 10000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHUSDTH23:
    """
        name: ETHUSDTH23
        precision: 0.05
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "ETHUSDTH23"
    precision: int = 0.05
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHUSDTH23"

    def __str__(self):
        return "ETHUSDTH23"

    def __call__(self):
        return "ETHUSDTH23"


ETHUSDTH23 = ETHUSDTH23()
"""
    name: ETHUSDTH23
    precision: 0.05
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETHUSDH23_ETH:
    """
        name: ETHUSDH23_ETH
        precision: 0.05
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 100000000
        margin: True
    """
    name: str = "ETHUSDH23_ETH"
    precision: int = 0.05
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 100000000
    margin: bool = True

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETHUSDH23_ETH"

    def __str__(self):
        return "ETHUSDH23_ETH"

    def __call__(self):
        return "ETHUSDH23_ETH"


ETHUSDH23_ETH = ETHUSDH23_ETH()
"""
    name: ETHUSDH23_ETH
    precision: 0.05
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 100000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETH_USDT:
    """
        name: ETH_USDT
        precision: 0.05
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 1000000
        maximum_order_size: 10000000000000
        margin: True
    """
    name: str = "ETH_USDT"
    precision: int = 0.05
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 1000000
    maximum_order_size: float = 10000000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 1000000
    maximum_order_size: 10000000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class ETH_XBT:
    """
        name: ETH_XBT
        precision: 1e-07
        minimum_margin: None
        initial_margin: 1
        minimum_order_size: 1000000
        maximum_order_size: 100000000000
        margin: True
    """
    name: str = "ETH_XBT"
    precision: int = 1e-07
    minimum_margin: float = None
    initial_margin: float = 1
    minimum_order_size: float = 1000000
    maximum_order_size: float = 100000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 1
    minimum_order_size: 1000000
    maximum_order_size: 100000000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LTCUSD:
    """
        name: LTCUSD
        precision: 0.01
        minimum_margin: None
        initial_margin: 0.02
        minimum_order_size: 1
        maximum_order_size: 100000000
        margin: True
    """
    name: str = "LTCUSD"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = 0.02
    minimum_order_size: float = 1
    maximum_order_size: float = 100000000
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


LTCUSD = LTCUSD()
"""
    name: LTCUSD
    precision: 0.01
    minimum_margin: None
    initial_margin: 0.02
    minimum_order_size: 1
    maximum_order_size: 100000000
    margin: True
"""


@dataclass(slots=True, frozen=True)
class LTCUSDT:
    """
        name: LTCUSDT
        precision: 0.01
        minimum_margin: None
        initial_margin: 0.03
        minimum_order_size: 1000
        maximum_order_size: 1000000000
        margin: True
    """
    name: str = "LTCUSDT"
    precision: int = 0.01
    minimum_margin: float = None
    initial_margin: float = 0.03
    minimum_order_size: float = 1000
    maximum_order_size: float = 1000000000
    margin: bool = True

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
    minimum_margin: None
    initial_margin: 0.03
    minimum_order_size: 1000
    maximum_order_size: 1000000000
    margin: True
"""
