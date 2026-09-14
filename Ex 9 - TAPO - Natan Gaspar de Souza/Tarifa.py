from abc import ABC, abstractmethod


class Tarifa(ABC):
    @abstractmethod
    def calcular(self, horas: int) -> int:
        pass
