from Tarifa import Tarifa


class TarifaMinimaOriginal(Tarifa):
    def calcular(self, horas: int) -> int:
        if horas < 3:
            raise ValueError("Minimo de tres horas")
        return horas * 4000
