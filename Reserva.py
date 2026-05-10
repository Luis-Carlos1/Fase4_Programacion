from datetime import datetime
class Reserva:

    def __init__(self, cliente, servicio, duracion_horas):

        if duracion_horas <= 0:
            raise ValueError("La duración debe ser positiva")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "PENDIENTE"
        self.fecha = datetime.now()

    def confirmar(self):

        if not self.servicio.verificar_disponibilidad():
            raise Exception("Servicio no disponible")

        self.estado = "CONFIRMADA"

    def cancelar(self):

        if self.estado == "CANCELADA":
            raise Exception("La reserva ya fue cancelada")

        self.estado = "CANCELADA"

    def calcular_total(self):
        return self.servicio.calcular_costo() * self.duracion_horas

    def mostrar_detalle(self):

        print("===== RESERVA =====")
        print(f"Cliente: {self.cliente.get_nombre()}")
        print(f"Servicio: {self.servicio.nombre}")
        print(f"Horas: {self.duracion_horas}")
        print(f"Estado: {self.estado}")
        print(f"Total: {self.calcular_total()}")
