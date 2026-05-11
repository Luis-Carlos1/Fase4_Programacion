from modelos.cliente import Cliente
from modelos.reserva import Reserva

from servicios.sala import Sala
from servicios.equipo import Equipo
from servicios.asesoria import Asesoria

from logger import registrar_log

print("========== SOFTWARE FJ ==========")

try:

    # CLIENTES
    cliente1 = Cliente(
        1,
        "Luis Mina",
        "luis@gmail.com",
        "312456789"
    )

    cliente1.mostrar_info()

    # SERVICIOS
    sala1 = Sala(
        "S01",
        "Sala Premium",
        100000,
        30
    )

    equipo1 = Equipo(
        "E01",
        "Computador Gamer",
        150000,
        "Tecnología"
    )

    asesoria1 = Asesoria(
        "A01",
        "Asesoría Programación",
        200000,
        "Ingeniero Senior"
    )

    # MOSTRAR SERVICIOS
    sala1.mostrar_info()
    equipo1.mostrar_info()
    asesoria1.mostrar_info()

    # RESERVAS
    reserva1 = Reserva(cliente1, sala1, 3)

    reserva1.confirmar()

    reserva1.mostrar_detalle()

    # AGREGAR RESERVA AL CLIENTE
    cliente1.agregar_reserva(reserva1)

except Exception as e:

    print("ERROR EN EL SISTEMA:", e)

    registrar_log(str(e))

finally:

    print("Sistema finalizado correctamente")
