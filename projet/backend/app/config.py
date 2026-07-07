from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    gitlab_url: str = "https://gitlab.com"
    gitlab_token: str = ""
    database_url: str = "sqlite:///./tdb.db"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}


settings = Settings()
