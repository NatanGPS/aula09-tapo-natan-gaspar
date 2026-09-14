from Enviador import Enviador


class EnviadorEmail(Enviador):
    def enviar(self, solicitante, mensagem: str) -> None:
        print(f"E-mail para {solicitante.obter_email()}: {mensagem}")
