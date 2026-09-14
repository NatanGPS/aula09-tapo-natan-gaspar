from abc import ABC, abstractmethod


class Enviador(ABC):
    @abstractmethod
    def enviar(self, solicitante, mensagem: str) -> None:
        pass
