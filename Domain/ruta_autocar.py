from dataclasses import dataclass

from Domain.entity import Entity

@dataclass
class RutaAutocar(Entity):
    id_oras_oprire: str
    id_oras_pornire: str
    pret: float
    dus_intors: bool


@dataclass
class RutaAutocarCuLocalitateOprire(RutaAutocar):
    nume_localitate_oprire: str
