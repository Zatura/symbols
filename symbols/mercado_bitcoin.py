from typing import NamedTuple


class REQ_BRL(NamedTuple):
    """
        name: REQ-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "REQ-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REQ-BRL"

    def __str__(self):
        return "REQ-BRL"

    def __call__(self):
        return "REQ-BRL"


REQ_BRL = REQ_BRL()
"""
    name: REQ-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ANKR_BRL(NamedTuple):
    """
        name: ANKR-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ANKR-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANKR-BRL"

    def __str__(self):
        return "ANKR-BRL"

    def __call__(self):
        return "ANKR-BRL"


ANKR_BRL = ANKR_BRL()
"""
    name: ANKR-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class LPT_BRL(NamedTuple):
    """
        name: LPT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "LPT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LPT-BRL"

    def __str__(self):
        return "LPT-BRL"

    def __call__(self):
        return "LPT-BRL"


LPT_BRL = LPT_BRL()
"""
    name: LPT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class KNC_BRL(NamedTuple):
    """
        name: KNC-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "KNC-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KNC-BRL"

    def __str__(self):
        return "KNC-BRL"

    def __call__(self):
        return "KNC-BRL"


KNC_BRL = KNC_BRL()
"""
    name: KNC-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CSCONS01_BRL(NamedTuple):
    """
        name: CSCONS01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CSCONS01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CSCONS01-BRL"

    def __str__(self):
        return "CSCONS01-BRL"

    def __call__(self):
        return "CSCONS01-BRL"


CSCONS01_BRL = CSCONS01_BRL()
"""
    name: CSCONS01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class XTZ_BRL(NamedTuple):
    """
        name: XTZ-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "XTZ-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XTZ-BRL"

    def __str__(self):
        return "XTZ-BRL"

    def __call__(self):
        return "XTZ-BRL"


XTZ_BRL = XTZ_BRL()
"""
    name: XTZ-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class XLM_BRL(NamedTuple):
    """
        name: XLM-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "XLM-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XLM-BRL"

    def __str__(self):
        return "XLM-BRL"

    def __call__(self):
        return "XLM-BRL"


XLM_BRL = XLM_BRL()
"""
    name: XLM-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BNT_BRL(NamedTuple):
    """
        name: BNT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BNT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BNT-BRL"

    def __str__(self):
        return "BNT-BRL"

    def __call__(self):
        return "BNT-BRL"


BNT_BRL = BNT_BRL()
"""
    name: BNT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SRM_BRL(NamedTuple):
    """
        name: SRM-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SRM-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SRM-BRL"

    def __str__(self):
        return "SRM-BRL"

    def __call__(self):
        return "SRM-BRL"


SRM_BRL = SRM_BRL()
"""
    name: SRM-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class STORJ_BRL(NamedTuple):
    """
        name: STORJ-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "STORJ-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STORJ-BRL"

    def __str__(self):
        return "STORJ-BRL"

    def __call__(self):
        return "STORJ-BRL"


STORJ_BRL = STORJ_BRL()
"""
    name: STORJ-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class AIOZ_BRL(NamedTuple):
    """
        name: AIOZ-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "AIOZ-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AIOZ-BRL"

    def __str__(self):
        return "AIOZ-BRL"

    def __call__(self):
        return "AIOZ-BRL"


AIOZ_BRL = AIOZ_BRL()
"""
    name: AIOZ-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class RACA_BRL(NamedTuple):
    """
        name: RACA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "RACA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RACA-BRL"

    def __str__(self):
        return "RACA-BRL"

    def __call__(self):
        return "RACA-BRL"


RACA_BRL = RACA_BRL()
"""
    name: RACA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ENS_BRL(NamedTuple):
    """
        name: ENS-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ENS-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENS-BRL"

    def __str__(self):
        return "ENS-BRL"

    def __call__(self):
        return "ENS-BRL"


ENS_BRL = ENS_BRL()
"""
    name: ENS-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BAL_BRL(NamedTuple):
    """
        name: BAL-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BAL-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAL-BRL"

    def __str__(self):
        return "BAL-BRL"

    def __call__(self):
        return "BAL-BRL"


BAL_BRL = BAL_BRL()
"""
    name: BAL-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BARFT_BRL(NamedTuple):
    """
        name: BARFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BARFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BARFT-BRL"

    def __str__(self):
        return "BARFT-BRL"

    def __call__(self):
        return "BARFT-BRL"


BARFT_BRL = BARFT_BRL()
"""
    name: BARFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class GHST_BRL(NamedTuple):
    """
        name: GHST-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "GHST-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GHST-BRL"

    def __str__(self):
        return "GHST-BRL"

    def __call__(self):
        return "GHST-BRL"


GHST_BRL = GHST_BRL()
"""
    name: GHST-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class AMFT_BRL(NamedTuple):
    """
        name: AMFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "AMFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AMFT-BRL"

    def __str__(self):
        return "AMFT-BRL"

    def __call__(self):
        return "AMFT-BRL"


AMFT_BRL = AMFT_BRL()
"""
    name: AMFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class RFDFP16_BRL(NamedTuple):
    """
        name: RFDFP16-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "RFDFP16-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RFDFP16-BRL"

    def __str__(self):
        return "RFDFP16-BRL"

    def __call__(self):
        return "RFDFP16-BRL"


RFDFP16_BRL = RFDFP16_BRL()
"""
    name: RFDFP16-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class IMX_BRL(NamedTuple):
    """
        name: IMX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "IMX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "IMX-BRL"

    def __str__(self):
        return "IMX-BRL"

    def __call__(self):
        return "IMX-BRL"


IMX_BRL = IMX_BRL()
"""
    name: IMX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ALICE_BRL(NamedTuple):
    """
        name: ALICE-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ALICE-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALICE-BRL"

    def __str__(self):
        return "ALICE-BRL"

    def __call__(self):
        return "ALICE-BRL"


ALICE_BRL = ALICE_BRL()
"""
    name: ALICE-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ALCX_BRL(NamedTuple):
    """
        name: ALCX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ALCX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALCX-BRL"

    def __str__(self):
        return "ALCX-BRL"

    def __call__(self):
        return "ALCX-BRL"


ALCX_BRL = ALCX_BRL()
"""
    name: ALCX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class NODL_BRL(NamedTuple):
    """
        name: NODL-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "NODL-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NODL-BRL"

    def __str__(self):
        return "NODL-BRL"

    def __call__(self):
        return "NODL-BRL"


NODL_BRL = NODL_BRL()
"""
    name: NODL-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class TLM_BRL(NamedTuple):
    """
        name: TLM-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "TLM-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TLM-BRL"

    def __str__(self):
        return "TLM-BRL"

    def __call__(self):
        return "TLM-BRL"


TLM_BRL = TLM_BRL()
"""
    name: TLM-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class WEMIX_BRL(NamedTuple):
    """
        name: WEMIX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "WEMIX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WEMIX-BRL"

    def __str__(self):
        return "WEMIX-BRL"

    def __call__(self):
        return "WEMIX-BRL"


WEMIX_BRL = WEMIX_BRL()
"""
    name: WEMIX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class NAVIFT_BRL(NamedTuple):
    """
        name: NAVIFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "NAVIFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "NAVIFT-BRL"

    def __str__(self):
        return "NAVIFT-BRL"

    def __call__(self):
        return "NAVIFT-BRL"


NAVIFT_BRL = NAVIFT_BRL()
"""
    name: NAVIFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH04_BRL(NamedTuple):
    """
        name: MBCCSH04-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH04-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH04-BRL"

    def __str__(self):
        return "MBCCSH04-BRL"

    def __call__(self):
        return "MBCCSH04-BRL"


MBCCSH04_BRL = MBCCSH04_BRL()
"""
    name: MBCCSH04-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBFP13_BRL(NamedTuple):
    """
        name: MBFP13-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBFP13-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBFP13-BRL"

    def __str__(self):
        return "MBFP13-BRL"

    def __call__(self):
        return "MBFP13-BRL"


MBFP13_BRL = MBFP13_BRL()
"""
    name: MBFP13-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class APE_BRL(NamedTuple):
    """
        name: APE-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "APE-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APE-BRL"

    def __str__(self):
        return "APE-BRL"

    def __call__(self):
        return "APE-BRL"


APE_BRL = APE_BRL()
"""
    name: APE-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ALPHA_BRL(NamedTuple):
    """
        name: ALPHA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ALPHA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALPHA-BRL"

    def __str__(self):
        return "ALPHA-BRL"

    def __call__(self):
        return "ALPHA-BRL"


ALPHA_BRL = ALPHA_BRL()
"""
    name: ALPHA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class GALFT_BRL(NamedTuple):
    """
        name: GALFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "GALFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALFT-BRL"

    def __str__(self):
        return "GALFT-BRL"

    def __call__(self):
        return "GALFT-BRL"


GALFT_BRL = GALFT_BRL()
"""
    name: GALFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBRL_BRL(NamedTuple):
    """
        name: MBRL-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBRL-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBRL-BRL"

    def __str__(self):
        return "MBRL-BRL"

    def __call__(self):
        return "MBRL-BRL"


MBRL_BRL = MBRL_BRL()
"""
    name: MBRL-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class OGN_BRL(NamedTuple):
    """
        name: OGN-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "OGN-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OGN-BRL"

    def __str__(self):
        return "OGN-BRL"

    def __call__(self):
        return "OGN-BRL"


OGN_BRL = OGN_BRL()
"""
    name: OGN-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CHZ_BRL(NamedTuple):
    """
        name: CHZ-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CHZ-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CHZ-BRL"

    def __str__(self):
        return "CHZ-BRL"

    def __call__(self):
        return "CHZ-BRL"


CHZ_BRL = CHZ_BRL()
"""
    name: CHZ-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBPRK02_BRL(NamedTuple):
    """
        name: MBPRK02-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBPRK02-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBPRK02-BRL"

    def __str__(self):
        return "MBPRK02-BRL"

    def __call__(self):
        return "MBPRK02-BRL"


MBPRK02_BRL = MBPRK02_BRL()
"""
    name: MBPRK02-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class OP_BRL(NamedTuple):
    """
        name: OP-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "OP-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OP-BRL"

    def __str__(self):
        return "OP-BRL"

    def __call__(self):
        return "OP-BRL"


OP_BRL = OP_BRL()
"""
    name: OP-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class AVAX_BRL(NamedTuple):
    """
        name: AVAX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "AVAX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AVAX-BRL"

    def __str__(self):
        return "AVAX-BRL"

    def __call__(self):
        return "AVAX-BRL"


AVAX_BRL = AVAX_BRL()
"""
    name: AVAX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBFP15_BRL(NamedTuple):
    """
        name: MBFP15-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBFP15-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBFP15-BRL"

    def __str__(self):
        return "MBFP15-BRL"

    def __call__(self):
        return "MBFP15-BRL"


MBFP15_BRL = MBFP15_BRL()
"""
    name: MBFP15-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ABFY_BRL(NamedTuple):
    """
        name: ABFY-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ABFY-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ABFY-BRL"

    def __str__(self):
        return "ABFY-BRL"

    def __call__(self):
        return "ABFY-BRL"


ABFY_BRL = ABFY_BRL()
"""
    name: ABFY-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class YFI_BRL(NamedTuple):
    """
        name: YFI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "YFI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YFI-BRL"

    def __str__(self):
        return "YFI-BRL"

    def __call__(self):
        return "YFI-BRL"


YFI_BRL = YFI_BRL()
"""
    name: YFI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBPRK06_BRL(NamedTuple):
    """
        name: MBPRK06-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBPRK06-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBPRK06-BRL"

    def __str__(self):
        return "MBPRK06-BRL"

    def __call__(self):
        return "MBPRK06-BRL"


MBPRK06_BRL = MBPRK06_BRL()
"""
    name: MBPRK06-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBFP08_BRL(NamedTuple):
    """
        name: MBFP08-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBFP08-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBFP08-BRL"

    def __str__(self):
        return "MBFP08-BRL"

    def __call__(self):
        return "MBFP08-BRL"


MBFP08_BRL = MBFP08_BRL()
"""
    name: MBFP08-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBFP09_BRL(NamedTuple):
    """
        name: MBFP09-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBFP09-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBFP09-BRL"

    def __str__(self):
        return "MBFP09-BRL"

    def __call__(self):
        return "MBFP09-BRL"


MBFP09_BRL = MBFP09_BRL()
"""
    name: MBFP09-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class KEEP_BRL(NamedTuple):
    """
        name: KEEP-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "KEEP-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KEEP-BRL"

    def __str__(self):
        return "KEEP-BRL"

    def __call__(self):
        return "KEEP-BRL"


KEEP_BRL = KEEP_BRL()
"""
    name: KEEP-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBPRK07_BRL(NamedTuple):
    """
        name: MBPRK07-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBPRK07-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBPRK07-BRL"

    def __str__(self):
        return "MBPRK07-BRL"

    def __call__(self):
        return "MBPRK07-BRL"


MBPRK07_BRL = MBPRK07_BRL()
"""
    name: MBPRK07-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH01_BRL(NamedTuple):
    """
        name: MBCCSH01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH01-BRL"

    def __str__(self):
        return "MBCCSH01-BRL"

    def __call__(self):
        return "MBCCSH01-BRL"


MBCCSH01_BRL = MBCCSH01_BRL()
"""
    name: MBCCSH01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SKL_BRL(NamedTuple):
    """
        name: SKL-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SKL-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SKL-BRL"

    def __str__(self):
        return "SKL-BRL"

    def __call__(self):
        return "SKL-BRL"


SKL_BRL = SKL_BRL()
"""
    name: SKL-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class VSPRK01_BRL(NamedTuple):
    """
        name: VSPRK01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "VSPRK01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "VSPRK01-BRL"

    def __str__(self):
        return "VSPRK01-BRL"

    def __call__(self):
        return "VSPRK01-BRL"


VSPRK01_BRL = VSPRK01_BRL()
"""
    name: VSPRK01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CAIFT_BRL(NamedTuple):
    """
        name: CAIFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CAIFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CAIFT-BRL"

    def __str__(self):
        return "CAIFT-BRL"

    def __call__(self):
        return "CAIFT-BRL"


CAIFT_BRL = CAIFT_BRL()
"""
    name: CAIFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH13_BRL(NamedTuple):
    """
        name: MBCCSH13-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH13-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH13-BRL"

    def __str__(self):
        return "MBCCSH13-BRL"

    def __call__(self):
        return "MBCCSH13-BRL"


MBCCSH13_BRL = MBCCSH13_BRL()
"""
    name: MBCCSH13-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SYN_BRL(NamedTuple):
    """
        name: SYN-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SYN-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SYN-BRL"

    def __str__(self):
        return "SYN-BRL"

    def __call__(self):
        return "SYN-BRL"


SYN_BRL = SYN_BRL()
"""
    name: SYN-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class WBX_BRL(NamedTuple):
    """
        name: WBX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "WBX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WBX-BRL"

    def __str__(self):
        return "WBX-BRL"

    def __call__(self):
        return "WBX-BRL"


WBX_BRL = WBX_BRL()
"""
    name: WBX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class OMG_BRL(NamedTuple):
    """
        name: OMG-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "OMG-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OMG-BRL"

    def __str__(self):
        return "OMG-BRL"

    def __call__(self):
        return "OMG-BRL"


OMG_BRL = OMG_BRL()
"""
    name: OMG-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class GODS_BRL(NamedTuple):
    """
        name: GODS-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "GODS-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GODS-BRL"

    def __str__(self):
        return "GODS-BRL"

    def __call__(self):
        return "GODS-BRL"


GODS_BRL = GODS_BRL()
"""
    name: GODS-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH07_BRL(NamedTuple):
    """
        name: MBCCSH07-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH07-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH07-BRL"

    def __str__(self):
        return "MBCCSH07-BRL"

    def __call__(self):
        return "MBCCSH07-BRL"


MBCCSH07_BRL = MBCCSH07_BRL()
"""
    name: MBCCSH07-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BTB10_BRL(NamedTuple):
    """
        name: BTB10-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BTB10-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTB10-BRL"

    def __str__(self):
        return "BTB10-BRL"

    def __call__(self):
        return "BTB10-BRL"


BTB10_BRL = BTB10_BRL()
"""
    name: BTB10-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class LRC_BRL(NamedTuple):
    """
        name: LRC-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "LRC-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LRC-BRL"

    def __str__(self):
        return "LRC-BRL"

    def __call__(self):
        return "LRC-BRL"


LRC_BRL = LRC_BRL()
"""
    name: LRC-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class FLOKI_BRL(NamedTuple):
    """
        name: FLOKI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "FLOKI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLOKI-BRL"

    def __str__(self):
        return "FLOKI-BRL"

    def __call__(self):
        return "FLOKI-BRL"


FLOKI_BRL = FLOKI_BRL()
"""
    name: FLOKI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ETH_BRL(NamedTuple):
    """
        name: ETH-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ETH-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ETH-BRL"

    def __str__(self):
        return "ETH-BRL"

    def __call__(self):
        return "ETH-BRL"


ETH_BRL = ETH_BRL()
"""
    name: ETH-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class GALA_BRL(NamedTuple):
    """
        name: GALA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "GALA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALA-BRL"

    def __str__(self):
        return "GALA-BRL"

    def __call__(self):
        return "GALA-BRL"


GALA_BRL = GALA_BRL()
"""
    name: GALA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class PLA_BRL(NamedTuple):
    """
        name: PLA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "PLA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PLA-BRL"

    def __str__(self):
        return "PLA-BRL"

    def __call__(self):
        return "PLA-BRL"


PLA_BRL = PLA_BRL()
"""
    name: PLA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class USDP_BRL(NamedTuple):
    """
        name: USDP-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "USDP-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDP-BRL"

    def __str__(self):
        return "USDP-BRL"

    def __call__(self):
        return "USDP-BRL"


USDP_BRL = USDP_BRL()
"""
    name: USDP-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MPL_BRL(NamedTuple):
    """
        name: MPL-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MPL-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MPL-BRL"

    def __str__(self):
        return "MPL-BRL"

    def __call__(self):
        return "MPL-BRL"


MPL_BRL = MPL_BRL()
"""
    name: MPL-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ADA_BRL(NamedTuple):
    """
        name: ADA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ADA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADA-BRL"

    def __str__(self):
        return "ADA-BRL"

    def __call__(self):
        return "ADA-BRL"


ADA_BRL = ADA_BRL()
"""
    name: ADA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ACH_BRL(NamedTuple):
    """
        name: ACH-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ACH-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ACH-BRL"

    def __str__(self):
        return "ACH-BRL"

    def __call__(self):
        return "ACH-BRL"


ACH_BRL = ACH_BRL()
"""
    name: ACH-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class HOT_BRL(NamedTuple):
    """
        name: HOT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "HOT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HOT-BRL"

    def __str__(self):
        return "HOT-BRL"

    def __call__(self):
        return "HOT-BRL"


HOT_BRL = HOT_BRL()
"""
    name: HOT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CTSI_BRL(NamedTuple):
    """
        name: CTSI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CTSI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CTSI-BRL"

    def __str__(self):
        return "CTSI-BRL"

    def __call__(self):
        return "CTSI-BRL"


CTSI_BRL = CTSI_BRL()
"""
    name: CTSI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class RAD_BRL(NamedTuple):
    """
        name: RAD-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "RAD-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RAD-BRL"

    def __str__(self):
        return "RAD-BRL"

    def __call__(self):
        return "RAD-BRL"


RAD_BRL = RAD_BRL()
"""
    name: RAD-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class RNDR_BRL(NamedTuple):
    """
        name: RNDR-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "RNDR-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RNDR-BRL"

    def __str__(self):
        return "RNDR-BRL"

    def __call__(self):
        return "RNDR-BRL"


RNDR_BRL = RNDR_BRL()
"""
    name: RNDR-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CEEK_BRL(NamedTuple):
    """
        name: CEEK-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CEEK-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CEEK-BRL"

    def __str__(self):
        return "CEEK-BRL"

    def __call__(self):
        return "CEEK-BRL"


CEEK_BRL = CEEK_BRL()
"""
    name: CEEK-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class LINK_BRL(NamedTuple):
    """
        name: LINK-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "LINK-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LINK-BRL"

    def __str__(self):
        return "LINK-BRL"

    def __call__(self):
        return "LINK-BRL"


LINK_BRL = LINK_BRL()
"""
    name: LINK-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class COTI_BRL(NamedTuple):
    """
        name: COTI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "COTI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COTI-BRL"

    def __str__(self):
        return "COTI-BRL"

    def __call__(self):
        return "COTI-BRL"


COTI_BRL = COTI_BRL()
"""
    name: COTI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class THFT_BRL(NamedTuple):
    """
        name: THFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "THFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "THFT-BRL"

    def __str__(self):
        return "THFT-BRL"

    def __call__(self):
        return "THFT-BRL"


THFT_BRL = THFT_BRL()
"""
    name: THFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class UMA_BRL(NamedTuple):
    """
        name: UMA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "UMA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UMA-BRL"

    def __str__(self):
        return "UMA-BRL"

    def __call__(self):
        return "UMA-BRL"


UMA_BRL = UMA_BRL()
"""
    name: UMA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BTRST_BRL(NamedTuple):
    """
        name: BTRST-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BTRST-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTRST-BRL"

    def __str__(self):
        return "BTRST-BRL"

    def __call__(self):
        return "BTRST-BRL"


BTRST_BRL = BTRST_BRL()
"""
    name: BTRST-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class LQTY_BRL(NamedTuple):
    """
        name: LQTY-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "LQTY-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LQTY-BRL"

    def __str__(self):
        return "LQTY-BRL"

    def __call__(self):
        return "LQTY-BRL"


LQTY_BRL = LQTY_BRL()
"""
    name: LQTY-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MINA_BRL(NamedTuple):
    """
        name: MINA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MINA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MINA-BRL"

    def __str__(self):
        return "MINA-BRL"

    def __call__(self):
        return "MINA-BRL"


MINA_BRL = MINA_BRL()
"""
    name: MINA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCONS01_BRL(NamedTuple):
    """
        name: MBCONS01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCONS01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCONS01-BRL"

    def __str__(self):
        return "MBCONS01-BRL"

    def __call__(self):
        return "MBCONS01-BRL"


MBCONS01_BRL = MBCONS01_BRL()
"""
    name: MBCONS01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SOL_BRL(NamedTuple):
    """
        name: SOL-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SOL-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SOL-BRL"

    def __str__(self):
        return "SOL-BRL"

    def __call__(self):
        return "SOL-BRL"


SOL_BRL = SOL_BRL()
"""
    name: SOL-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH08_BRL(NamedTuple):
    """
        name: MBCCSH08-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH08-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH08-BRL"

    def __str__(self):
        return "MBCCSH08-BRL"

    def __call__(self):
        return "MBCCSH08-BRL"


MBCCSH08_BRL = MBCCSH08_BRL()
"""
    name: MBCCSH08-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ICP_BRL(NamedTuple):
    """
        name: ICP-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ICP-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ICP-BRL"

    def __str__(self):
        return "ICP-BRL"

    def __call__(self):
        return "ICP-BRL"


ICP_BRL = ICP_BRL()
"""
    name: ICP-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBTKN01_BRL(NamedTuple):
    """
        name: MBTKN01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBTKN01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBTKN01-BRL"

    def __str__(self):
        return "MBTKN01-BRL"

    def __call__(self):
        return "MBTKN01-BRL"


MBTKN01_BRL = MBTKN01_BRL()
"""
    name: MBTKN01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH10_BRL(NamedTuple):
    """
        name: MBCCSH10-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH10-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH10-BRL"

    def __str__(self):
        return "MBCCSH10-BRL"

    def __call__(self):
        return "MBCCSH10-BRL"


MBCCSH10_BRL = MBCCSH10_BRL()
"""
    name: MBCCSH10-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SPELL_BRL(NamedTuple):
    """
        name: SPELL-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SPELL-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SPELL-BRL"

    def __str__(self):
        return "SPELL-BRL"

    def __call__(self):
        return "SPELL-BRL"


SPELL_BRL = SPELL_BRL()
"""
    name: SPELL-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MANA_BRL(NamedTuple):
    """
        name: MANA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MANA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MANA-BRL"

    def __str__(self):
        return "MANA-BRL"

    def __call__(self):
        return "MANA-BRL"


MANA_BRL = MANA_BRL()
"""
    name: MANA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MKR_BRL(NamedTuple):
    """
        name: MKR-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MKR-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MKR-BRL"

    def __str__(self):
        return "MKR-BRL"

    def __call__(self):
        return "MKR-BRL"


MKR_BRL = MKR_BRL()
"""
    name: MKR-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH11_BRL(NamedTuple):
    """
        name: MBCCSH11-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH11-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH11-BRL"

    def __str__(self):
        return "MBCCSH11-BRL"

    def __call__(self):
        return "MBCCSH11-BRL"


MBCCSH11_BRL = MBCCSH11_BRL()
"""
    name: MBCCSH11-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class API3_BRL(NamedTuple):
    """
        name: API3-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "API3-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "API3-BRL"

    def __str__(self):
        return "API3-BRL"

    def __call__(self):
        return "API3-BRL"


API3_BRL = API3_BRL()
"""
    name: API3-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ENER02_BRL(NamedTuple):
    """
        name: ENER02-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ENER02-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENER02-BRL"

    def __str__(self):
        return "ENER02-BRL"

    def __call__(self):
        return "ENER02-BRL"


ENER02_BRL = ENER02_BRL()
"""
    name: ENER02-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH09_BRL(NamedTuple):
    """
        name: MBCCSH09-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH09-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH09-BRL"

    def __str__(self):
        return "MBCCSH09-BRL"

    def __call__(self):
        return "MBCCSH09-BRL"


MBCCSH09_BRL = MBCCSH09_BRL()
"""
    name: MBCCSH09-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class GST_BRL(NamedTuple):
    """
        name: GST-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "GST-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GST-BRL"

    def __str__(self):
        return "GST-BRL"

    def __call__(self):
        return "GST-BRL"


GST_BRL = GST_BRL()
"""
    name: GST-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class KSM_BRL(NamedTuple):
    """
        name: KSM-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "KSM-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KSM-BRL"

    def __str__(self):
        return "KSM-BRL"

    def __call__(self):
        return "KSM-BRL"


KSM_BRL = KSM_BRL()
"""
    name: KSM-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class DOT_BRL(NamedTuple):
    """
        name: DOT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "DOT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOT-BRL"

    def __str__(self):
        return "DOT-BRL"

    def __call__(self):
        return "DOT-BRL"


DOT_BRL = DOT_BRL()
"""
    name: DOT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class POWR_BRL(NamedTuple):
    """
        name: POWR-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "POWR-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POWR-BRL"

    def __str__(self):
        return "POWR-BRL"

    def __call__(self):
        return "POWR-BRL"


POWR_BRL = POWR_BRL()
"""
    name: POWR-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBFP14_BRL(NamedTuple):
    """
        name: MBFP14-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBFP14-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBFP14-BRL"

    def __str__(self):
        return "MBFP14-BRL"

    def __call__(self):
        return "MBFP14-BRL"


MBFP14_BRL = MBFP14_BRL()
"""
    name: MBFP14-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class OXT_BRL(NamedTuple):
    """
        name: OXT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "OXT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OXT-BRL"

    def __str__(self):
        return "OXT-BRL"

    def __call__(self):
        return "OXT-BRL"


OXT_BRL = OXT_BRL()
"""
    name: OXT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MIR_BRL(NamedTuple):
    """
        name: MIR-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MIR-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MIR-BRL"

    def __str__(self):
        return "MIR-BRL"

    def __call__(self):
        return "MIR-BRL"


MIR_BRL = MIR_BRL()
"""
    name: MIR-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CLV_BRL(NamedTuple):
    """
        name: CLV-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CLV-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CLV-BRL"

    def __str__(self):
        return "CLV-BRL"

    def __call__(self):
        return "CLV-BRL"


CLV_BRL = CLV_BRL()
"""
    name: CLV-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class LOOKS_BRL(NamedTuple):
    """
        name: LOOKS-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "LOOKS-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LOOKS-BRL"

    def __str__(self):
        return "LOOKS-BRL"

    def __call__(self):
        return "LOOKS-BRL"


LOOKS_BRL = LOOKS_BRL()
"""
    name: LOOKS-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class LTC_BRL(NamedTuple):
    """
        name: LTC-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "LTC-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LTC-BRL"

    def __str__(self):
        return "LTC-BRL"

    def __call__(self):
        return "LTC-BRL"


LTC_BRL = LTC_BRL()
"""
    name: LTC-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBPRK03_BRL(NamedTuple):
    """
        name: MBPRK03-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBPRK03-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBPRK03-BRL"

    def __str__(self):
        return "MBPRK03-BRL"

    def __call__(self):
        return "MBPRK03-BRL"


MBPRK03_BRL = MBPRK03_BRL()
"""
    name: MBPRK03-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class PSGFT_BRL(NamedTuple):
    """
        name: PSGFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "PSGFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PSGFT-BRL"

    def __str__(self):
        return "PSGFT-BRL"

    def __call__(self):
        return "PSGFT-BRL"


PSGFT_BRL = PSGFT_BRL()
"""
    name: PSGFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MATIC_BRL(NamedTuple):
    """
        name: MATIC-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MATIC-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MATIC-BRL"

    def __str__(self):
        return "MATIC-BRL"

    def __call__(self):
        return "MATIC-BRL"


MATIC_BRL = MATIC_BRL()
"""
    name: MATIC-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SPFCFT_BRL(NamedTuple):
    """
        name: SPFCFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SPFCFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SPFCFT-BRL"

    def __str__(self):
        return "SPFCFT-BRL"

    def __call__(self):
        return "SPFCFT-BRL"


SPFCFT_BRL = SPFCFT_BRL()
"""
    name: SPFCFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ENER01_BRL(NamedTuple):
    """
        name: ENER01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ENER01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENER01-BRL"

    def __str__(self):
        return "ENER01-BRL"

    def __call__(self):
        return "ENER01-BRL"


ENER01_BRL = ENER01_BRL()
"""
    name: ENER01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class FET_BRL(NamedTuple):
    """
        name: FET-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "FET-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FET-BRL"

    def __str__(self):
        return "FET-BRL"

    def __call__(self):
        return "FET-BRL"


FET_BRL = FET_BRL()
"""
    name: FET-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ALLFT_BRL(NamedTuple):
    """
        name: ALLFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ALLFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALLFT-BRL"

    def __str__(self):
        return "ALLFT-BRL"

    def __call__(self):
        return "ALLFT-BRL"


ALLFT_BRL = ALLFT_BRL()
"""
    name: ALLFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBPRK05_BRL(NamedTuple):
    """
        name: MBPRK05-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBPRK05-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBPRK05-BRL"

    def __str__(self):
        return "MBPRK05-BRL"

    def __call__(self):
        return "MBPRK05-BRL"


MBPRK05_BRL = MBPRK05_BRL()
"""
    name: MBPRK05-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CRV_BRL(NamedTuple):
    """
        name: CRV-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CRV-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CRV-BRL"

    def __str__(self):
        return "CRV-BRL"

    def __call__(self):
        return "CRV-BRL"


CRV_BRL = CRV_BRL()
"""
    name: CRV-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class AMP_BRL(NamedTuple):
    """
        name: AMP-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "AMP-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AMP-BRL"

    def __str__(self):
        return "AMP-BRL"

    def __call__(self):
        return "AMP-BRL"


AMP_BRL = AMP_BRL()
"""
    name: AMP-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BAT_BRL(NamedTuple):
    """
        name: BAT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BAT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAT-BRL"

    def __str__(self):
        return "BAT-BRL"

    def __call__(self):
        return "BAT-BRL"


BAT_BRL = BAT_BRL()
"""
    name: BAT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SDAO_BRL(NamedTuple):
    """
        name: SDAO-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SDAO-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SDAO-BRL"

    def __str__(self):
        return "SDAO-BRL"

    def __call__(self):
        return "SDAO-BRL"


SDAO_BRL = SDAO_BRL()
"""
    name: SDAO-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CSCONS03_BRL(NamedTuple):
    """
        name: CSCONS03-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CSCONS03-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CSCONS03-BRL"

    def __str__(self):
        return "CSCONS03-BRL"

    def __call__(self):
        return "CSCONS03-BRL"


CSCONS03_BRL = CSCONS03_BRL()
"""
    name: CSCONS03-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class REN_BRL(NamedTuple):
    """
        name: REN-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "REN-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "REN-BRL"

    def __str__(self):
        return "REN-BRL"

    def __call__(self):
        return "REN-BRL"


REN_BRL = REN_BRL()
"""
    name: REN-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MENGOFT_BRL(NamedTuple):
    """
        name: MENGOFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MENGOFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MENGOFT-BRL"

    def __str__(self):
        return "MENGOFT-BRL"

    def __call__(self):
        return "MENGOFT-BRL"


MENGOFT_BRL = MENGOFT_BRL()
"""
    name: MENGOFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH16_BRL(NamedTuple):
    """
        name: MBCCSH16-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH16-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH16-BRL"

    def __str__(self):
        return "MBCCSH16-BRL"

    def __call__(self):
        return "MBCCSH16-BRL"


MBCCSH16_BRL = MBCCSH16_BRL()
"""
    name: MBCCSH16-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CVC_BRL(NamedTuple):
    """
        name: CVC-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CVC-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CVC-BRL"

    def __str__(self):
        return "CVC-BRL"

    def __call__(self):
        return "CVC-BRL"


CVC_BRL = CVC_BRL()
"""
    name: CVC-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBPRK04_BRL(NamedTuple):
    """
        name: MBPRK04-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBPRK04-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBPRK04-BRL"

    def __str__(self):
        return "MBPRK04-BRL"

    def __call__(self):
        return "MBPRK04-BRL"


MBPRK04_BRL = MBPRK04_BRL()
"""
    name: MBPRK04-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class JUVFT_BRL(NamedTuple):
    """
        name: JUVFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "JUVFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "JUVFT-BRL"

    def __str__(self):
        return "JUVFT-BRL"

    def __call__(self):
        return "JUVFT-BRL"


JUVFT_BRL = JUVFT_BRL()
"""
    name: JUVFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class RLY_BRL(NamedTuple):
    """
        name: RLY-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "RLY-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RLY-BRL"

    def __str__(self):
        return "RLY-BRL"

    def __call__(self):
        return "RLY-BRL"


RLY_BRL = RLY_BRL()
"""
    name: RLY-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class FIL_BRL(NamedTuple):
    """
        name: FIL-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "FIL-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FIL-BRL"

    def __str__(self):
        return "FIL-BRL"

    def __call__(self):
        return "FIL-BRL"


FIL_BRL = FIL_BRL()
"""
    name: FIL-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class APT_BRL(NamedTuple):
    """
        name: APT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "APT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "APT-BRL"

    def __str__(self):
        return "APT-BRL"

    def __call__(self):
        return "APT-BRL"


APT_BRL = APT_BRL()
"""
    name: APT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class UNI_BRL(NamedTuple):
    """
        name: UNI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "UNI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UNI-BRL"

    def __str__(self):
        return "UNI-BRL"

    def __call__(self):
        return "UNI-BRL"


UNI_BRL = UNI_BRL()
"""
    name: UNI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class DAI_BRL(NamedTuple):
    """
        name: DAI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "DAI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DAI-BRL"

    def __str__(self):
        return "DAI-BRL"

    def __call__(self):
        return "DAI-BRL"


DAI_BRL = DAI_BRL()
"""
    name: DAI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class OCEAN_BRL(NamedTuple):
    """
        name: OCEAN-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "OCEAN-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OCEAN-BRL"

    def __str__(self):
        return "OCEAN-BRL"

    def __call__(self):
        return "OCEAN-BRL"


OCEAN_BRL = OCEAN_BRL()
"""
    name: OCEAN-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class AAVE_BRL(NamedTuple):
    """
        name: AAVE-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "AAVE-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AAVE-BRL"

    def __str__(self):
        return "AAVE-BRL"

    def __call__(self):
        return "AAVE-BRL"


AAVE_BRL = AAVE_BRL()
"""
    name: AAVE-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH03_BRL(NamedTuple):
    """
        name: MBCCSH03-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH03-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH03-BRL"

    def __str__(self):
        return "MBCCSH03-BRL"

    def __call__(self):
        return "MBCCSH03-BRL"


MBCCSH03_BRL = MBCCSH03_BRL()
"""
    name: MBCCSH03-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ENJ_BRL(NamedTuple):
    """
        name: ENJ-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ENJ-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENJ-BRL"

    def __str__(self):
        return "ENJ-BRL"

    def __call__(self):
        return "ENJ-BRL"


ENJ_BRL = ENJ_BRL()
"""
    name: ENJ-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH05_BRL(NamedTuple):
    """
        name: MBCCSH05-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH05-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH05-BRL"

    def __str__(self):
        return "MBCCSH05-BRL"

    def __call__(self):
        return "MBCCSH05-BRL"


MBCCSH05_BRL = MBCCSH05_BRL()
"""
    name: MBCCSH05-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SLP_BRL(NamedTuple):
    """
        name: SLP-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SLP-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SLP-BRL"

    def __str__(self):
        return "SLP-BRL"

    def __call__(self):
        return "SLP-BRL"


SLP_BRL = SLP_BRL()
"""
    name: SLP-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class DYDX_BRL(NamedTuple):
    """
        name: DYDX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "DYDX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DYDX-BRL"

    def __str__(self):
        return "DYDX-BRL"

    def __call__(self):
        return "DYDX-BRL"


DYDX_BRL = DYDX_BRL()
"""
    name: DYDX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBFP12_BRL(NamedTuple):
    """
        name: MBFP12-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBFP12-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBFP12-BRL"

    def __str__(self):
        return "MBFP12-BRL"

    def __call__(self):
        return "MBFP12-BRL"


MBFP12_BRL = MBFP12_BRL()
"""
    name: MBFP12-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class YGG_BRL(NamedTuple):
    """
        name: YGG-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "YGG-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YGG-BRL"

    def __str__(self):
        return "YGG-BRL"

    def __call__(self):
        return "YGG-BRL"


YGG_BRL = YGG_BRL()
"""
    name: YGG-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ENER03_BRL(NamedTuple):
    """
        name: ENER03-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ENER03-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ENER03-BRL"

    def __str__(self):
        return "ENER03-BRL"

    def __call__(self):
        return "ENER03-BRL"


ENER03_BRL = ENER03_BRL()
"""
    name: ENER03-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ACMFT_BRL(NamedTuple):
    """
        name: ACMFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ACMFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ACMFT-BRL"

    def __str__(self):
        return "ACMFT-BRL"

    def __call__(self):
        return "ACMFT-BRL"


ACMFT_BRL = ACMFT_BRL()
"""
    name: ACMFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class WBTC_BRL(NamedTuple):
    """
        name: WBTC-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "WBTC-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WBTC-BRL"

    def __str__(self):
        return "WBTC-BRL"

    def __call__(self):
        return "WBTC-BRL"


WBTC_BRL = WBTC_BRL()
"""
    name: WBTC-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH02_BRL(NamedTuple):
    """
        name: MBCCSH02-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH02-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH02-BRL"

    def __str__(self):
        return "MBCCSH02-BRL"

    def __call__(self):
        return "MBCCSH02-BRL"


MBCCSH02_BRL = MBCCSH02_BRL()
"""
    name: MBCCSH02-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class OPUL_BRL(NamedTuple):
    """
        name: OPUL-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "OPUL-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OPUL-BRL"

    def __str__(self):
        return "OPUL-BRL"

    def __call__(self):
        return "OPUL-BRL"


OPUL_BRL = OPUL_BRL()
"""
    name: OPUL-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CSCONS05_BRL(NamedTuple):
    """
        name: CSCONS05-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CSCONS05-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CSCONS05-BRL"

    def __str__(self):
        return "CSCONS05-BRL"

    def __call__(self):
        return "CSCONS05-BRL"


CSCONS05_BRL = CSCONS05_BRL()
"""
    name: CSCONS05-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MC_BRL(NamedTuple):
    """
        name: MC-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MC-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MC-BRL"

    def __str__(self):
        return "MC-BRL"

    def __call__(self):
        return "MC-BRL"


MC_BRL = MC_BRL()
"""
    name: MC-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class USDC_BRL(NamedTuple):
    """
        name: USDC-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "USDC-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "USDC-BRL"

    def __str__(self):
        return "USDC-BRL"

    def __call__(self):
        return "USDC-BRL"


USDC_BRL = USDC_BRL()
"""
    name: USDC-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CVX_BRL(NamedTuple):
    """
        name: CVX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CVX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CVX-BRL"

    def __str__(self):
        return "CVX-BRL"

    def __call__(self):
        return "CVX-BRL"


CVX_BRL = CVX_BRL()
"""
    name: CVX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class DPI_BRL(NamedTuple):
    """
        name: DPI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "DPI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DPI-BRL"

    def __str__(self):
        return "DPI-BRL"

    def __call__(self):
        return "DPI-BRL"


DPI_BRL = DPI_BRL()
"""
    name: DPI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class FARM_BRL(NamedTuple):
    """
        name: FARM-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "FARM-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FARM-BRL"

    def __str__(self):
        return "FARM-BRL"

    def __call__(self):
        return "FARM-BRL"


FARM_BRL = FARM_BRL()
"""
    name: FARM-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ADS_BRL(NamedTuple):
    """
        name: ADS-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ADS-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ADS-BRL"

    def __str__(self):
        return "ADS-BRL"

    def __call__(self):
        return "ADS-BRL"


ADS_BRL = ADS_BRL()
"""
    name: ADS-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CONS01_BRL(NamedTuple):
    """
        name: CONS01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CONS01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CONS01-BRL"

    def __str__(self):
        return "CONS01-BRL"

    def __call__(self):
        return "CONS01-BRL"


CONS01_BRL = CONS01_BRL()
"""
    name: CONS01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ATLAS_BRL(NamedTuple):
    """
        name: ATLAS-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ATLAS-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATLAS-BRL"

    def __str__(self):
        return "ATLAS-BRL"

    def __call__(self):
        return "ATLAS-BRL"


ATLAS_BRL = ATLAS_BRL()
"""
    name: ATLAS-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH14_BRL(NamedTuple):
    """
        name: MBCCSH14-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH14-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH14-BRL"

    def __str__(self):
        return "MBCCSH14-BRL"

    def __call__(self):
        return "MBCCSH14-BRL"


MBCCSH14_BRL = MBCCSH14_BRL()
"""
    name: MBCCSH14-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class LDO_BRL(NamedTuple):
    """
        name: LDO-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "LDO-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "LDO-BRL"

    def __str__(self):
        return "LDO-BRL"

    def __call__(self):
        return "LDO-BRL"


LDO_BRL = LDO_BRL()
"""
    name: LDO-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class INTERFT_BRL(NamedTuple):
    """
        name: INTERFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "INTERFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "INTERFT-BRL"

    def __str__(self):
        return "INTERFT-BRL"

    def __call__(self):
        return "INTERFT-BRL"


INTERFT_BRL = INTERFT_BRL()
"""
    name: INTERFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ROSE_BRL(NamedTuple):
    """
        name: ROSE-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ROSE-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ROSE-BRL"

    def __str__(self):
        return "ROSE-BRL"

    def __call__(self):
        return "ROSE-BRL"


ROSE_BRL = ROSE_BRL()
"""
    name: ROSE-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class RARE_BRL(NamedTuple):
    """
        name: RARE-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "RARE-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RARE-BRL"

    def __str__(self):
        return "RARE-BRL"

    def __call__(self):
        return "RARE-BRL"


RARE_BRL = RARE_BRL()
"""
    name: RARE-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class UFCFT_BRL(NamedTuple):
    """
        name: UFCFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "UFCFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "UFCFT-BRL"

    def __str__(self):
        return "UFCFT-BRL"

    def __call__(self):
        return "UFCFT-BRL"


UFCFT_BRL = UFCFT_BRL()
"""
    name: UFCFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class PFLFT_BRL(NamedTuple):
    """
        name: PFLFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "PFLFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PFLFT-BRL"

    def __str__(self):
        return "PFLFT-BRL"

    def __call__(self):
        return "PFLFT-BRL"


PFLFT_BRL = PFLFT_BRL()
"""
    name: PFLFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SAND_BRL(NamedTuple):
    """
        name: SAND-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SAND-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SAND-BRL"

    def __str__(self):
        return "SAND-BRL"

    def __call__(self):
        return "SAND-BRL"


SAND_BRL = SAND_BRL()
"""
    name: SAND-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class WLUNA_BRL(NamedTuple):
    """
        name: WLUNA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "WLUNA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "WLUNA-BRL"

    def __str__(self):
        return "WLUNA-BRL"

    def __call__(self):
        return "WLUNA-BRL"


WLUNA_BRL = WLUNA_BRL()
"""
    name: WLUNA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBVASCO01_BRL(NamedTuple):
    """
        name: MBVASCO01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBVASCO01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBVASCO01-BRL"

    def __str__(self):
        return "MBVASCO01-BRL"

    def __call__(self):
        return "MBVASCO01-BRL"


MBVASCO01_BRL = MBVASCO01_BRL()
"""
    name: MBVASCO01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBPRK01_BRL(NamedTuple):
    """
        name: MBPRK01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBPRK01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBPRK01-BRL"

    def __str__(self):
        return "MBPRK01-BRL"

    def __call__(self):
        return "MBPRK01-BRL"


MBPRK01_BRL = MBPRK01_BRL()
"""
    name: MBPRK01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class POLY_BRL(NamedTuple):
    """
        name: POLY-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "POLY-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLY-BRL"

    def __str__(self):
        return "POLY-BRL"

    def __call__(self):
        return "POLY-BRL"


POLY_BRL = POLY_BRL()
"""
    name: POLY-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SCCPFT_BRL(NamedTuple):
    """
        name: SCCPFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SCCPFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SCCPFT-BRL"

    def __str__(self):
        return "SCCPFT-BRL"

    def __call__(self):
        return "SCCPFT-BRL"


SCCPFT_BRL = SCCPFT_BRL()
"""
    name: SCCPFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CSCONS04_BRL(NamedTuple):
    """
        name: CSCONS04-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CSCONS04-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CSCONS04-BRL"

    def __str__(self):
        return "CSCONS04-BRL"

    def __call__(self):
        return "CSCONS04-BRL"


CSCONS04_BRL = CSCONS04_BRL()
"""
    name: CSCONS04-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class AGIX_BRL(NamedTuple):
    """
        name: AGIX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "AGIX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AGIX-BRL"

    def __str__(self):
        return "AGIX-BRL"

    def __call__(self):
        return "AGIX-BRL"


AGIX_BRL = AGIX_BRL()
"""
    name: AGIX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CSCONS02_BRL(NamedTuple):
    """
        name: CSCONS02-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CSCONS02-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CSCONS02-BRL"

    def __str__(self):
        return "CSCONS02-BRL"

    def __call__(self):
        return "CSCONS02-BRL"


CSCONS02_BRL = CSCONS02_BRL()
"""
    name: CSCONS02-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ANT_BRL(NamedTuple):
    """
        name: ANT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ANT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ANT-BRL"

    def __str__(self):
        return "ANT-BRL"

    def __call__(self):
        return "ANT-BRL"


ANT_BRL = ANT_BRL()
"""
    name: ANT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH15_BRL(NamedTuple):
    """
        name: MBCCSH15-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH15-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH15-BRL"

    def __str__(self):
        return "MBCCSH15-BRL"

    def __call__(self):
        return "MBCCSH15-BRL"


MBCCSH15_BRL = MBCCSH15_BRL()
"""
    name: MBCCSH15-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class DG_BRL(NamedTuple):
    """
        name: DG-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "DG-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DG-BRL"

    def __str__(self):
        return "DG-BRL"

    def __call__(self):
        return "DG-BRL"


DG_BRL = DG_BRL()
"""
    name: DG-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ASRFT_BRL(NamedTuple):
    """
        name: ASRFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ASRFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ASRFT-BRL"

    def __str__(self):
        return "ASRFT-BRL"

    def __call__(self):
        return "ASRFT-BRL"


ASRFT_BRL = ASRFT_BRL()
"""
    name: ASRFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class STX_BRL(NamedTuple):
    """
        name: STX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "STX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STX-BRL"

    def __str__(self):
        return "STX-BRL"

    def __call__(self):
        return "STX-BRL"


STX_BRL = STX_BRL()
"""
    name: STX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class PAXG_BRL(NamedTuple):
    """
        name: PAXG-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "PAXG-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PAXG-BRL"

    def __str__(self):
        return "PAXG-BRL"

    def __call__(self):
        return "PAXG-BRL"


PAXG_BRL = PAXG_BRL()
"""
    name: PAXG-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ARGFT_BRL(NamedTuple):
    """
        name: ARGFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ARGFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ARGFT-BRL"

    def __str__(self):
        return "ARGFT-BRL"

    def __call__(self):
        return "ARGFT-BRL"


ARGFT_BRL = ARGFT_BRL()
"""
    name: ARGFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class PERP_BRL(NamedTuple):
    """
        name: PERP-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "PERP-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PERP-BRL"

    def __str__(self):
        return "PERP-BRL"

    def __call__(self):
        return "PERP-BRL"


PERP_BRL = PERP_BRL()
"""
    name: PERP-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class STVFT_BRL(NamedTuple):
    """
        name: STVFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "STVFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STVFT-BRL"

    def __str__(self):
        return "STVFT-BRL"

    def __call__(self):
        return "STVFT-BRL"


STVFT_BRL = STVFT_BRL()
"""
    name: STVFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BTC_BRL(NamedTuple):
    """
        name: BTC-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BTC-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTC-BRL"

    def __str__(self):
        return "BTC-BRL"

    def __call__(self):
        return "BTC-BRL"


BTC_BRL = BTC_BRL()
"""
    name: BTC-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ERN_BRL(NamedTuple):
    """
        name: ERN-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ERN-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ERN-BRL"

    def __str__(self):
        return "ERN-BRL"

    def __call__(self):
        return "ERN-BRL"


ERN_BRL = ERN_BRL()
"""
    name: ERN-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class METIS_BRL(NamedTuple):
    """
        name: METIS-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "METIS-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "METIS-BRL"

    def __str__(self):
        return "METIS-BRL"

    def __call__(self):
        return "METIS-BRL"


METIS_BRL = METIS_BRL()
"""
    name: METIS-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class PORFT_BRL(NamedTuple):
    """
        name: PORFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "PORFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "PORFT-BRL"

    def __str__(self):
        return "PORFT-BRL"

    def __call__(self):
        return "PORFT-BRL"


PORFT_BRL = PORFT_BRL()
"""
    name: PORFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class AUDIO_BRL(NamedTuple):
    """
        name: AUDIO-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "AUDIO-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AUDIO-BRL"

    def __str__(self):
        return "AUDIO-BRL"

    def __call__(self):
        return "AUDIO-BRL"


AUDIO_BRL = AUDIO_BRL()
"""
    name: AUDIO-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class STG_BRL(NamedTuple):
    """
        name: STG-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "STG-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "STG-BRL"

    def __str__(self):
        return "STG-BRL"

    def __call__(self):
        return "STG-BRL"


STG_BRL = STG_BRL()
"""
    name: STG-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class RARI_BRL(NamedTuple):
    """
        name: RARI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "RARI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "RARI-BRL"

    def __str__(self):
        return "RARI-BRL"

    def __call__(self):
        return "RARI-BRL"


RARI_BRL = RARI_BRL()
"""
    name: RARI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BCH_BRL(NamedTuple):
    """
        name: BCH-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BCH-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BCH-BRL"

    def __str__(self):
        return "BCH-BRL"

    def __call__(self):
        return "BCH-BRL"


BCH_BRL = BCH_BRL()
"""
    name: BCH-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class KP3R_BRL(NamedTuple):
    """
        name: KP3R-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "KP3R-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "KP3R-BRL"

    def __str__(self):
        return "KP3R-BRL"

    def __call__(self):
        return "KP3R-BRL"


KP3R_BRL = KP3R_BRL()
"""
    name: KP3R-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class YBOFT_BRL(NamedTuple):
    """
        name: YBOFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "YBOFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "YBOFT-BRL"

    def __str__(self):
        return "YBOFT-BRL"

    def __call__(self):
        return "YBOFT-BRL"


YBOFT_BRL = YBOFT_BRL()
"""
    name: YBOFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class DIA_BRL(NamedTuple):
    """
        name: DIA-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "DIA-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DIA-BRL"

    def __str__(self):
        return "DIA-BRL"

    def __call__(self):
        return "DIA-BRL"


DIA_BRL = DIA_BRL()
"""
    name: DIA-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ATOM_BRL(NamedTuple):
    """
        name: ATOM-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ATOM-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATOM-BRL"

    def __str__(self):
        return "ATOM-BRL"

    def __call__(self):
        return "ATOM-BRL"


ATOM_BRL = ATOM_BRL()
"""
    name: ATOM-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBFP11_BRL(NamedTuple):
    """
        name: MBFP11-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBFP11-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBFP11-BRL"

    def __str__(self):
        return "MBFP11-BRL"

    def __call__(self):
        return "MBFP11-BRL"


MBFP11_BRL = MBFP11_BRL()
"""
    name: MBFP11-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SNX_BRL(NamedTuple):
    """
        name: SNX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SNX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SNX-BRL"

    def __str__(self):
        return "SNX-BRL"

    def __call__(self):
        return "SNX-BRL"


SNX_BRL = SNX_BRL()
"""
    name: SNX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class OGFT_BRL(NamedTuple):
    """
        name: OGFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "OGFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "OGFT-BRL"

    def __str__(self):
        return "OGFT-BRL"

    def __call__(self):
        return "OGFT-BRL"


OGFT_BRL = OGFT_BRL()
"""
    name: OGFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class GMT_BRL(NamedTuple):
    """
        name: GMT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "GMT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GMT-BRL"

    def __str__(self):
        return "GMT-BRL"

    def __call__(self):
        return "GMT-BRL"


GMT_BRL = GMT_BRL()
"""
    name: GMT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class HIGH_BRL(NamedTuple):
    """
        name: HIGH-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "HIGH-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "HIGH-BRL"

    def __str__(self):
        return "HIGH-BRL"

    def __call__(self):
        return "HIGH-BRL"


HIGH_BRL = HIGH_BRL()
"""
    name: HIGH-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH12_BRL(NamedTuple):
    """
        name: MBCCSH12-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH12-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH12-BRL"

    def __str__(self):
        return "MBCCSH12-BRL"

    def __call__(self):
        return "MBCCSH12-BRL"


MBCCSH12_BRL = MBCCSH12_BRL()
"""
    name: MBCCSH12-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ATMFT_BRL(NamedTuple):
    """
        name: ATMFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ATMFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ATMFT-BRL"

    def __str__(self):
        return "ATMFT-BRL"

    def __call__(self):
        return "ATMFT-BRL"


ATMFT_BRL = ATMFT_BRL()
"""
    name: ATMFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBFP10_BRL(NamedTuple):
    """
        name: MBFP10-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBFP10-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBFP10-BRL"

    def __str__(self):
        return "MBFP10-BRL"

    def __call__(self):
        return "MBFP10-BRL"


MBFP10_BRL = MBFP10_BRL()
"""
    name: MBFP10-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ALGO_BRL(NamedTuple):
    """
        name: ALGO-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ALGO-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ALGO-BRL"

    def __str__(self):
        return "ALGO-BRL"

    def __call__(self):
        return "ALGO-BRL"


ALGO_BRL = ALGO_BRL()
"""
    name: ALGO-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCONS02_BRL(NamedTuple):
    """
        name: MBCONS02-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCONS02-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCONS02-BRL"

    def __str__(self):
        return "MBCONS02-BRL"

    def __call__(self):
        return "MBCONS02-BRL"


MBCONS02_BRL = MBCONS02_BRL()
"""
    name: MBCONS02-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBFP07_BRL(NamedTuple):
    """
        name: MBFP07-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBFP07-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBFP07-BRL"

    def __str__(self):
        return "MBFP07-BRL"

    def __call__(self):
        return "MBFP07-BRL"


MBFP07_BRL = MBFP07_BRL()
"""
    name: MBFP07-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class POLS_BRL(NamedTuple):
    """
        name: POLS-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "POLS-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "POLS-BRL"

    def __str__(self):
        return "POLS-BRL"

    def __call__(self):
        return "POLS-BRL"


POLS_BRL = POLS_BRL()
"""
    name: POLS-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BAND_BRL(NamedTuple):
    """
        name: BAND-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BAND-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BAND-BRL"

    def __str__(self):
        return "BAND-BRL"

    def __call__(self):
        return "BAND-BRL"


BAND_BRL = BAND_BRL()
"""
    name: BAND-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class FLOW_BRL(NamedTuple):
    """
        name: FLOW-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "FLOW-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "FLOW-BRL"

    def __str__(self):
        return "FLOW-BRL"

    def __call__(self):
        return "FLOW-BRL"


FLOW_BRL = FLOW_BRL()
"""
    name: FLOW-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBCCSH06_BRL(NamedTuple):
    """
        name: MBCCSH06-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBCCSH06-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBCCSH06-BRL"

    def __str__(self):
        return "MBCCSH06-BRL"

    def __call__(self):
        return "MBCCSH06-BRL"


MBCCSH06_BRL = MBCCSH06_BRL()
"""
    name: MBCCSH06-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SAUBERFT_BRL(NamedTuple):
    """
        name: SAUBERFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SAUBERFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SAUBERFT-BRL"

    def __str__(self):
        return "SAUBERFT-BRL"

    def __call__(self):
        return "SAUBERFT-BRL"


SAUBERFT_BRL = SAUBERFT_BRL()
"""
    name: SAUBERFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BTB05_BRL(NamedTuple):
    """
        name: BTB05-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BTB05-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BTB05-BRL"

    def __str__(self):
        return "BTB05-BRL"

    def __call__(self):
        return "BTB05-BRL"


BTB05_BRL = BTB05_BRL()
"""
    name: BTB05-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BLZ_BRL(NamedTuple):
    """
        name: BLZ-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BLZ-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BLZ-BRL"

    def __str__(self):
        return "BLZ-BRL"

    def __call__(self):
        return "BLZ-BRL"


BLZ_BRL = BLZ_BRL()
"""
    name: BLZ-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SUSHI_BRL(NamedTuple):
    """
        name: SUSHI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SUSHI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUSHI-BRL"

    def __str__(self):
        return "SUSHI-BRL"

    def __call__(self):
        return "SUSHI-BRL"


SUSHI_BRL = SUSHI_BRL()
"""
    name: SUSHI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class TRB_BRL(NamedTuple):
    """
        name: TRB-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "TRB-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRB-BRL"

    def __str__(self):
        return "TRB-BRL"

    def __call__(self):
        return "TRB-BRL"


TRB_BRL = TRB_BRL()
"""
    name: TRB-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class QNT_BRL(NamedTuple):
    """
        name: QNT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "QNT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "QNT-BRL"

    def __str__(self):
        return "QNT-BRL"

    def __call__(self):
        return "QNT-BRL"


QNT_BRL = QNT_BRL()
"""
    name: QNT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class DOGE_BRL(NamedTuple):
    """
        name: DOGE-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "DOGE-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "DOGE-BRL"

    def __str__(self):
        return "DOGE-BRL"

    def __call__(self):
        return "DOGE-BRL"


DOGE_BRL = DOGE_BRL()
"""
    name: DOGE-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class GNO_BRL(NamedTuple):
    """
        name: GNO-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "GNO-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GNO-BRL"

    def __str__(self):
        return "GNO-BRL"

    def __call__(self):
        return "GNO-BRL"


GNO_BRL = GNO_BRL()
"""
    name: GNO-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class JASMY_BRL(NamedTuple):
    """
        name: JASMY-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "JASMY-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "JASMY-BRL"

    def __str__(self):
        return "JASMY-BRL"

    def __call__(self):
        return "JASMY-BRL"


JASMY_BRL = JASMY_BRL()
"""
    name: JASMY-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ZRX_BRL(NamedTuple):
    """
        name: ZRX-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ZRX-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ZRX-BRL"

    def __str__(self):
        return "ZRX-BRL"

    def __call__(self):
        return "ZRX-BRL"


ZRX_BRL = ZRX_BRL()
"""
    name: ZRX-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class GRT_BRL(NamedTuple):
    """
        name: GRT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "GRT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GRT-BRL"

    def __str__(self):
        return "GRT-BRL"

    def __call__(self):
        return "GRT-BRL"


GRT_BRL = GRT_BRL()
"""
    name: GRT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class GALOFT_BRL(NamedTuple):
    """
        name: GALOFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "GALOFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "GALOFT-BRL"

    def __str__(self):
        return "GALOFT-BRL"

    def __call__(self):
        return "GALOFT-BRL"


GALOFT_BRL = GALOFT_BRL()
"""
    name: GALOFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MBSANTOS01_BRL(NamedTuple):
    """
        name: MBSANTOS01-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MBSANTOS01-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MBSANTOS01-BRL"

    def __str__(self):
        return "MBSANTOS01-BRL"

    def __call__(self):
        return "MBSANTOS01-BRL"


MBSANTOS01_BRL = MBSANTOS01_BRL()
"""
    name: MBSANTOS01-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class XRP_BRL(NamedTuple):
    """
        name: XRP-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "XRP-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "XRP-BRL"

    def __str__(self):
        return "XRP-BRL"

    def __call__(self):
        return "XRP-BRL"


XRP_BRL = XRP_BRL()
"""
    name: XRP-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class AXS_BRL(NamedTuple):
    """
        name: AXS-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "AXS-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "AXS-BRL"

    def __str__(self):
        return "AXS-BRL"

    def __call__(self):
        return "AXS-BRL"


AXS_BRL = AXS_BRL()
"""
    name: AXS-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SHIB_BRL(NamedTuple):
    """
        name: SHIB-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SHIB-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SHIB-BRL"

    def __str__(self):
        return "SHIB-BRL"

    def __call__(self):
        return "SHIB-BRL"


SHIB_BRL = SHIB_BRL()
"""
    name: SHIB-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BADGER_BRL(NamedTuple):
    """
        name: BADGER-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BADGER-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BADGER-BRL"

    def __str__(self):
        return "BADGER-BRL"

    def __call__(self):
        return "BADGER-BRL"


BADGER_BRL = BADGER_BRL()
"""
    name: BADGER-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class CITYFT_BRL(NamedTuple):
    """
        name: CITYFT-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "CITYFT-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "CITYFT-BRL"

    def __str__(self):
        return "CITYFT-BRL"

    def __call__(self):
        return "CITYFT-BRL"


CITYFT_BRL = CITYFT_BRL()
"""
    name: CITYFT-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class COMP_BRL(NamedTuple):
    """
        name: COMP-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "COMP-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "COMP-BRL"

    def __str__(self):
        return "COMP-BRL"

    def __call__(self):
        return "COMP-BRL"


COMP_BRL = COMP_BRL()
"""
    name: COMP-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MVI_BRL(NamedTuple):
    """
        name: MVI-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MVI-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MVI-BRL"

    def __str__(self):
        return "MVI-BRL"

    def __call__(self):
        return "MVI-BRL"


MVI_BRL = MVI_BRL()
"""
    name: MVI-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class ILV_BRL(NamedTuple):
    """
        name: ILV-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "ILV-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "ILV-BRL"

    def __str__(self):
        return "ILV-BRL"

    def __call__(self):
        return "ILV-BRL"


ILV_BRL = ILV_BRL()
"""
    name: ILV-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class SUPER_BRL(NamedTuple):
    """
        name: SUPER-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "SUPER-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "SUPER-BRL"

    def __str__(self):
        return "SUPER-BRL"

    def __call__(self):
        return "SUPER-BRL"


SUPER_BRL = SUPER_BRL()
"""
    name: SUPER-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class MCO2_BRL(NamedTuple):
    """
        name: MCO2-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "MCO2-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "MCO2-BRL"

    def __str__(self):
        return "MCO2-BRL"

    def __call__(self):
        return "MCO2-BRL"


MCO2_BRL = MCO2_BRL()
"""
    name: MCO2-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class TRU_BRL(NamedTuple):
    """
        name: TRU-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "TRU-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "TRU-BRL"

    def __str__(self):
        return "TRU-BRL"

    def __call__(self):
        return "TRU-BRL"


TRU_BRL = TRU_BRL()
"""
    name: TRU-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""


class BICO_BRL(NamedTuple):
    """
        name: BICO-BRL
        precision: 8
        minimum_margin: None
        initial_margin: None
        minimum_order_size: None
        maximum_order_size: None
        margin: False
    """
    name: str = "BICO-BRL"
    precision: int = 8
    minimum_margin: float = None
    initial_margin: float = None
    minimum_order_size: float = None
    maximum_order_size: float = None
    margin: bool = False

    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        if type(self) == type(other):
            return self.name == other.name

    def __repr__(self):
        return "BICO-BRL"

    def __str__(self):
        return "BICO-BRL"

    def __call__(self):
        return "BICO-BRL"


BICO_BRL = BICO_BRL()
"""
    name: BICO-BRL
    precision: 8
    minimum_margin: None
    initial_margin: None
    minimum_order_size: None
    maximum_order_size: None
    margin: False
"""
