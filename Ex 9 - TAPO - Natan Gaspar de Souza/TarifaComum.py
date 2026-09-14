from Tarifa import Tarifa


class TarifaComum(Tarifa):
    def calcular(self, horas: int) -> int:
        if horas <= 0:
            raise ValueError("Duracao invalida")
        return horas * 5000
