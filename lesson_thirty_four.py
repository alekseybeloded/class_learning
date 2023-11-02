from dataclasses import dataclass, field


@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list)


t = ThingData('Учебник по Python', 100, 1024)
print(t)
