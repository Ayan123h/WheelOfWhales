from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str
   
    AUTO_TAP: bool = True

    SQUAD_NAME: str = 'yummy_squad'

    REF_ID: str = ''

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()


