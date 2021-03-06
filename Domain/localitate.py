from dataclasses import dataclass

from Domain.entity import Entity

@dataclass
class Localitate(Entity):
    nume: str
    tip: str


@dataclass
class LocalitateCuNrRute(Localitate):
    nr_rute: int

