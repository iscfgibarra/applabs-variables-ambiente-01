from config import config_from_os
from config import config_from_file


def main():
    # Vienen de la configuración de variables ya establecida en el sistema operativo
    print("Variables desde el SO: ")
    print(config_from_os.aws_database)
    print(config_from_os.aws_secret)

    print("Variables desde el archivo .env: ")
    # Vienen de la configuración "artificial" creada por medio del archivo .env y load_env
    print(config_from_file.aws_database)
    print(config_from_file.aws_secret)


if __name__ == '__main__':
    main()
