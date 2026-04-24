from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / ".env"
load_dotenv(ENV_PATH)


class Settings(BaseSettings):
    environment: str = "development"
    database_url: str = "mysql+mysqldb://root:password@127.0.0.1:3306/meditech"
    secret_key: str = "change-me-please"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"


settings = Settings()
