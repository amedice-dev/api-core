import os
from datetime import timedelta
from functools import lru_cache
from typing import List

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict
from pydantic_settings_yaml import YamlBaseSettings


class Database(BaseModel):
    url: str
    database_name: str
    engine: str = "django.db.backends.postgresql_psycopg2"
    conn_health_check: bool = False
    conn_max_age: int = 600


class Application(BaseModel):
    allowed_hosts: List[str] = ["localhost", "127.0.0.1", "0.0.0.0"]
    csrf_trusted: List[str] = ["http://localhost:1337"]
    debug: bool = False
    secret_key: str
    timezone: str = "Asia/Tashkent"
    language: str = "ru"
    access_token_lifetime: timedelta = timedelta(minutes=15)
    refresh_token_lifetime: timedelta = timedelta(days=7)


class Settings(YamlBaseSettings):
    database: Database
    application: Application

    # configure paths to secrets directory and YAML config file
    model_config = SettingsConfigDict(
        yaml_file=os.environ.get("CONFIG_NAME", "etc/config/config.yaml"),
        secrets_dir=os.environ.get("SECRETS_DIR", "etc/secrets"),
    )


settings = Settings()


@lru_cache()
def get_settings() -> Settings:
    return Settings()
