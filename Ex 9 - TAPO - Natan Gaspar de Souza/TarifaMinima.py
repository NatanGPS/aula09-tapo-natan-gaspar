from Tarifa import Tarifa


class TarifaMinima(Tarifa):
    def calcular(self, horas: int) -> int:
        if horas <= 0:
            raise ValueError("Duracao invalida")
        return max(horas, 3) * 4000
