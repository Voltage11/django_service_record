from dotenv import load_dotenv
import os

class AppConfig:
    def __init__(self):
        if not load_dotenv('.env'):
            raise RuntimeError("Не удалось загрузить .env файл")

        # Получаем переменные окружения с проверкой
        self.DbHost = os.environ.get("DB_HOST")
        self.DbUser = os.environ.get("DB_USER")
        self.DbPass = os.environ.get("DB_PASS")
        self.DbPort = os.environ.get("DB_PORT")
        self.DbName = os.environ.get("DB_NAME")
        self.SecretKey = os.environ.get("SECRET_KEY")

        # Проверяем наличие критических переменных
        for attr in [self.DbHost, self.DbUser, self.DbPass, self.DbPort, self.DbName, self.SecretKey]:
            if attr is None:
                raise ValueError(f"Отсутствует обязательная переменная окружения: {attr}")

app_config = AppConfig()