from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base, disponible=True):

        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    def verificar_disponibilidad(self):
        return self.disponible
      
