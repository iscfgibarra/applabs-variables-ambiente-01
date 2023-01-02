import os
from dotenv import load_dotenv


class ConfigFromFile:

    def __init__(self):
        load_dotenv()
        # Nombrar las variables de entorno con un prefijo para evitar
        self.aws_database = os.getenv('PYML_AWS_DATABASE', 'database_default')
        self.aws_secret = os.getenv('PYML_AWS_SECRET', 'secret_default')


config_from_file = ConfigFromFile()
