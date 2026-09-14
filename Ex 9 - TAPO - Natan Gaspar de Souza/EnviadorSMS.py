from Enviador import Enviador


class EnviadorSMS(Enviador):
    def enviar(self, solicitante, mensagem: str) -> None:
        print(f"SMS para {solicitante.obter_telefone()}: {mensagem}")
