from abc import ABC, abstractmethod
from typing import Protocol


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Parrot(Bird):
    def fly(self):
        print('Parrot flying')

# b = Bird()
p = Parrot()
p.fly()

print(isinstance(p, Parrot))
print(isinstance(p, Bird))

class Aeroplane(ABC):
    @abstractmethod
    def fly(self):
        pass

class Boeing(Aeroplane):
    def fly(self):
        print('Boeing flying')

b = Boeing()
b.fly()

print(isinstance(b, Aeroplane))
print(isinstance(b, Boeing))


class CanFly(Protocol):
    def fly(self) -> None:
        pass

class World():
    def make_obj_fly(self, obj: CanFly):
        obj.fly()

w = World()
w.make_obj_fly(p)
w.make_obj_fly(b)
