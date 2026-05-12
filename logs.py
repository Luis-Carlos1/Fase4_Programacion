import logging

# Configuración general del archivo de registros
logging.basicConfig(
    filename="registro_sistema.log",
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Función para guardar errores
def guardar_error(texto):

    logging.warning(texto)

# Función para guardar actividades del sistema
def guardar_movimiento(texto):

    logging.info(texto)

# Función para guardar mensajes críticos
def guardar_fallo_critico(texto):

    logging.critical(texto)
