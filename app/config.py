from pydantic import BaseSettings
import pathlib


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = f"{pathlib.Path(__file__).resolve().parent}/.env"


settings = Settings()
