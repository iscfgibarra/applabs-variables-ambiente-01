import os


class ConfigFromOs:

    def __init__(self):
        # Nombrar las variables de entorno con un prefijo para evitar
        self.aws_database = os.getenv('PYML_AWS_DATABASE_OS', 'database_default')
        self.aws_secret = os.getenv('PYML_AWS_SECRET_OS', 'secret_default')


config_from_os = ConfigFromOs()
