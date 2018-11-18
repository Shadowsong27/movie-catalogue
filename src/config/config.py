import configparser

# CONSTANT CONFIG
config_file_name = "movie_catalogue.cfg"


class AppConfig:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(config_file_name)

    def parse_core(self):
        pass

    def parse_database(self):
        pass

    def parse_webserver(self):
        pass


appconfig = AppConfig()
