from pydantic import BaseSettings


class Settings(BaseSettings):
    prefix: str = ""
    secret_key: str = 'Secret Value'

    class Config:
        env_file = ".env"

settings = Settings()