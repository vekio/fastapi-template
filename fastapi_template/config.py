from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project: str
    version: str
    api_version: str
    api_host: str
    api_port: int
    # web_host: str
    # web_port: int

    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
print(settings)
