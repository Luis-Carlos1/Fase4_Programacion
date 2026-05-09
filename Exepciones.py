class ErrorSistema(Exception):
    pass

class ClienteNoValido(ErrorSistema):
    pass

class ServicioNoDisponible(ErrorSistema):
    pass

class ReservaInvalida(ErrorSistema):
    pass
