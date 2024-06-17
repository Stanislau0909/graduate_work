from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PORT: str
    DP_PASSWORD: str
    DB_ECHO: bool = True

    @property
    def get_db_uri(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DP_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def get_db_uri_async(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DP_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = "..\..\env_configs\.env"


settings = Settings()
