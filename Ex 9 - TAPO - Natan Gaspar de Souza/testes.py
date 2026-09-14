from contextlib import redirect_stdout
from io import StringIO
from EnviadorEmail import EnviadorEmail
from EnviadorSMS import EnviadorSMS
from Reserva import Reserva
from Sala import Sala
from Solicitante import Solicitante
from TarifaComum import TarifaComum
from TarifaMinima import TarifaMinima
from TarifaMinimaOriginal import TarifaMinimaOriginal
from TarifaPacote import TarifaPacote
from TarifaPromocional import TarifaPromocional


def deve_lancar_erro(operacao):
    try:
        operacao()
    except ValueError:
        return
    raise AssertionError("Era esperado ValueError")


ana = Solicitante("Ana", "ana@example.com", "31999990000")
bruno = Solicitante("Bruno", "bruno@example.com", "31988880000")
assert ana.obter_email() == "ana@example.com"
assert ana.obter_telefone() == "31999990000"
assert TarifaComum().calcular(2) == 10000
assert TarifaPacote().calcular(6) == 20000
assert TarifaPromocional().calcular(2) == 8000

saida_email = StringIO()
with redirect_stdout(saida_email):
    sala_email = Sala("Sala 201")
    total_email = Reserva(sala_email, ana, 2, TarifaPromocional(), EnviadorEmail()).registrar()
assert total_email == 8000
assert sala_email.reservada is True
assert saida_email.getvalue().count("E-mail para") == 1
assert "ana@example.com" in saida_email.getvalue()

saida_sms = StringIO()
with redirect_stdout(saida_sms):
    sala_sms = Sala("Sala 202")
    total_sms = Reserva(sala_sms, bruno, 2, TarifaPromocional(), EnviadorSMS()).registrar()
assert total_sms == 8000
assert sala_sms.reservada is True
assert saida_sms.getvalue().count("SMS para") == 1
assert "31988880000" in saida_sms.getvalue()

deve_lancar_erro(lambda: TarifaPromocional().calcular(0))
deve_lancar_erro(lambda: TarifaMinimaOriginal().calcular(1))
assert TarifaPromocional().calcular(1) == 4000
assert TarifaMinima().calcular(1) == 12000
assert TarifaMinima().calcular(2) == 12000
assert TarifaMinima().calcular(3) == 12000
assert TarifaMinima().calcular(4) == 16000
deve_lancar_erro(lambda: TarifaMinima().calcular(0))
deve_lancar_erro(lambda: TarifaMinima().calcular(-1))

saida_minima = StringIO()
with redirect_stdout(saida_minima):
    sala_minima = Sala("Sala 203")
    total_minimo = Reserva(sala_minima, ana, 1, TarifaMinima(), EnviadorEmail()).registrar()
assert total_minimo == 12000
assert sala_minima.reservada is True
assert saida_minima.getvalue().count("E-mail para") == 1

sala_indisponivel = Sala("Sala 204")
saida_indisponivel = StringIO()
with redirect_stdout(saida_indisponivel):
    Reserva(sala_indisponivel, ana, 1, TarifaComum(), EnviadorEmail()).registrar()
deve_lancar_erro(lambda: Reserva(sala_indisponivel, bruno, 1, TarifaComum(), EnviadorSMS()).registrar())
sala_invalida = Sala("Sala 205")
deve_lancar_erro(lambda: Reserva(sala_invalida, ana, 0, TarifaComum(), EnviadorEmail()).registrar())
assert sala_invalida.reservada is False
print("Todos os asserts foram executados com sucesso.")
