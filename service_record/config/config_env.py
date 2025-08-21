import os

from dotenv import load_dotenv


class ConfigEnv:
    def __init__(self):
        load_dotenv()        
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        if not self.SECRET_KEY:            
            raise Exception("Не задана переменная окружения SECRET_KEY")

        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASS = os.getenv("DB_PASS")
        self.DB_NAME = os.getenv("DB_NAME")
        if not (self.DB_HOST and self.DB_PORT and self.DB_USER and self.DB_PASS and self.DB_NAME):
            raise Exception("Не заданы переменные окружения для подключения к БД")
        
        debug = os.getenv("DEBUG")
        if debug and debug.lower() == "false":
            self.DEBUG = False
        else:
            self.DEBUG = True
        

config_env = ConfigEnv()

