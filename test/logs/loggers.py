# import logging

# # Configuración básica
# logging.basicConfig(
#     level=logging.INFO,  # Nivel mínimo de mensajes a registrar
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%Y-%m-%d %H:%M:%S",
# )

# logger = logging.getLogger(__name__)  # Logger específico para el módulo

# logger.info("This is an informational message")
# logger.error("This is an error message")

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("my_application")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = RotatingFileHandler(
    "logs/app.log", maxBytes=1024 * 1024 * 5, backupCount=3
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning")
logger.error("This is an error")
logger.critical("This is critical")
