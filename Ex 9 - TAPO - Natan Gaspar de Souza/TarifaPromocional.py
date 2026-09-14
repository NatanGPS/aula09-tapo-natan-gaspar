from Tarifa import Tarifa


class TarifaPromocional(Tarifa):
    def calcular(self, horas: int) -> int:
        if horas <= 0:
            raise ValueError("Duracao invalida")
        return horas * 4000
