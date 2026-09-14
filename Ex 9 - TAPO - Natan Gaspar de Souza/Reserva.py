class Reserva:
    def __init__(self, sala, solicitante, horas: int, tarifa, enviador):
        self.sala = sala
        self.solicitante = solicitante
        self.horas = horas
        self.tarifa = tarifa
        self.enviador = enviador

    def registrar(self) -> int:
        if self.horas <= 0:
            raise ValueError("Duracao invalida")
        if self.sala.reservada:
            raise ValueError("Sala indisponivel")
        total = self.tarifa.calcular(self.horas)
        self.sala.reservada = True
        mensagem = f"Reserva de {self.sala.nome}: {total} centavos"
        self.enviador.enviar(self.solicitante, mensagem)
        return total
