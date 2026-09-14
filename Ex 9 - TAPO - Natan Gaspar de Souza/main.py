from EnviadorEmail import EnviadorEmail
from EnviadorSMS import EnviadorSMS
from Reserva import Reserva
from Sala import Sala
from Solicitante import Solicitante
from TarifaComum import TarifaComum
from TarifaMinima import TarifaMinima
from TarifaPacote import TarifaPacote
from TarifaPromocional import TarifaPromocional


def registrar_reserva(sala, solicitante, horas, tarifa, enviador):
    reserva = Reserva(sala, solicitante, horas, tarifa, enviador)
    return reserva.registrar()


if __name__ == "__main__":
    ana = Solicitante("Ana", "ana@example.com", "31999990000")
    bruno = Solicitante("Bruno", "bruno@example.com", "31988880000")
    total_email = registrar_reserva(Sala("Sala 101"), ana, 2, TarifaPromocional(), EnviadorEmail())
    total_sms = registrar_reserva(Sala("Sala 102"), bruno, 2, TarifaPromocional(), EnviadorSMS())
    total_minimo = registrar_reserva(Sala("Sala 103"), ana, 1, TarifaMinima(), EnviadorEmail())
    total_comum = registrar_reserva(Sala("Sala 104"), bruno, 2, TarifaComum(), EnviadorEmail())
    total_pacote = registrar_reserva(Sala("Sala 105"), ana, 6, TarifaPacote(), EnviadorEmail())
    print(f"Total promocional por e-mail: {total_email} centavos")
    print(f"Total promocional por SMS: {total_sms} centavos")
    print(f"Total com tarifa minima: {total_minimo} centavos")
    print(f"Total com tarifa comum: {total_comum} centavos")
    print(f"Total com tarifa pacote: {total_pacote} centavos")
