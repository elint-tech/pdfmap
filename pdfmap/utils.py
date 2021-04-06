from dataclasses import dataclass
from numbers import Number


@dataclass(frozen=True)
class Shape:
    height: Number
    width: Number