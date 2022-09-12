import logging


DB_NAME = "exchange.db"
LOGGER_CONFIG = dict(level=logging.DEBUG, file="app.log", formatter=logging.Formatter("%(asctime)s [%(levelname)s]- %(name)s:%(message)s")
                     )