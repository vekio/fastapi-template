from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project: str
    version: str
    api_version: str


settings = Settings()
