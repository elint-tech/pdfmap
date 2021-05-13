import enum
from numbers import Number

from dataclassy import dataclass


@dataclass(frozen=True)
class Shape:
    height: Number
    width: Number


class Origin(enum.Enum):
    TOP_LEFT = enum.auto()
    BOTTOM_LEFT = enum.auto()
