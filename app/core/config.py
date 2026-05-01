from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DataBaseConfig(BaseModel):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int


class AuthJWTConfig(BaseModel):
    private_key: str
    public_key: str
    algorithm: str = "RS256"


class Settings(BaseSettings):
    db: DataBaseConfig
    auth_jwt: AuthJWTConfig

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )


settings = Settings()  # type: ignore значения подтягиваются SettingsConfigDict