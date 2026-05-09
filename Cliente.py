from modelos.entidad import Entidad

class Cliente(Entidad):

    def __init__(self, id_cliente, nombre, correo, telefono):
        super().__init__(id_cliente)

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__reservas = []

    # GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # SETTERS
    def set_telefono(self, nuevo_telefono):
        if len(nuevo_telefono) < 7:
            raise ValueError("Número telefónico inválido")

        self.__telefono = nuevo_telefono

    # MÉTODOS
    def agregar_reserva(self, reserva):
        self.__reservas.append(reserva)

    def mostrar_reservas(self):
        for reserva in self.__reservas:
            print(reserva)

    def mostrar_info(self):
        print("===== CLIENTE =====")
        print(f"ID: {self._id_entidad}")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Teléfono: {self.__telefono}")
      
