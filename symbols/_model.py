from typing import NamedTuple


class Symbol(NamedTuple):
    name: str
    significant_digits: int
    tick_size: int
    min_margin: float
    initial_margin: float
    min_order_size: float
    max_order_size: float
    has_margin: bool
    exchange: str
