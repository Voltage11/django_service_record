from dotenv import load_dotenv
import os

class Config:
    DbHost: str
    DbUser: str
    DbPass: str
    DbPort: str
    DbName: str
    SecretKey: str
    def __init__(self):
        if __name__ == "__main__":
            if not load_dotenv():
                raise Exception("Ошибка загрузки .env файла")
            self.DbHost = os.getenv("DB_HOST")
            self.DbUser = os.getenv("DB_USER")
            self.DbPass = os.getenv("DB_PASS")
            self.DbPort = os.getenv("DB_PORT")
            self.DbName = os.getenv("DB_NAME")
            self.SecretKey = os.getenv("SECRET_KEY")


