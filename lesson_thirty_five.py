from dataclasses import dataclass, field, InitVar

@dataclass(frozen=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)


v = V3D(1, 2, 3, True)
