class Solicitante:
    def __init__(self, nome: str, email: str, telefone: str):
        self.nome = nome
        self.__email = email
        self.__telefone = telefone

    def obter_email(self) -> str:
        return self.__email

    def obter_telefone(self) -> str:
        return self.__telefone
