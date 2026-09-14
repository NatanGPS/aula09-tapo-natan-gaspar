from Tarifa import Tarifa


class TarifaPacote(Tarifa):
    def calcular(self, horas: int) -> int:
        if horas <= 0:
            raise ValueError("Duracao invalida")
        return min(horas * 5000, 20000)
