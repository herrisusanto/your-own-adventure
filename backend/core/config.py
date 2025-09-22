from typing import List, Optional

from fastapi import FastAPI
from pydantic_settings import BaseSettings
from pydantic import field_validator
import os


class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False

    DATABASE_URL: str = None

    ALLOWED_ORIGINS: str = ""

    OPENAI_API_KEY: Optional[str] = None

    # def __init__(self, **values):
    #     super().__init__(**values)
    #     if not self.DEBUG:
    #         db_user = os.environ.get("DB_USER")
    #         db_password = os.environ.get("DB_PASSWORD")
    #         db_host = os.environ.get("DB_HOST")
    #         db_name = os.environ.get("DB_NAME")
    #         db_port = os.environ.get("DB_PORT")
    #         self.DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"


    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

