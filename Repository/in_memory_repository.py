from typing import Dict, Union, Optional, List, Type

from Domain.entity import Entity


class InMemoryRepository():

    def __init__(self):
        super().__init__()
        self.__entities = {}

    def create(self, entity: Entity) -> None:

        if self.read(entity.id_entity) is not None:
            raise KeyError(f'Exista deja o '
                           f'entitate cu id-ul {entity.id_entity}.')

        self.__entities[entity.id_entity] = entity

    def read(self, id_entity: object = None) \
            -> Type[Union[Optional[Entity], List[Entity]]]:

        if id_entity:
            if id_entity in self.__entities:
                return self.__entities[id_entity]
            else:
                return None

        return list(self.__entities.values())

    def update(self, entity: Entity) -> None:

        if self.read(entity.id_entity) is None:
            msg = f'Nu exista o entitate cu id-ul ' \
                  f'{entity.id_entity} de actualizat.'
            raise KeyError(msg)

        self.__entities[entity.id_entity] = entity

    def delete(self, id_entity: str) -> None:

        if self.read(id_entity) is None:
            raise KeyError(
                f'Nu exista o entitate cu id-ul '
                f'{id_entity} pe care sa o stergem.')

        del self.__entities[id_entity]
