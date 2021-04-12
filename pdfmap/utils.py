import enum
from dataclasses import dataclass
from numbers import Number


@dataclass(frozen=True)
class Shape:
    height: Number
    width: Number


class Origin(enum.Enum):
    TOP_LEFT = enum.auto()
    BOTTOM_LEFT = enum.auto()
