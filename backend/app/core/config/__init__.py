from pydantic_settings import BaseSettings, SettingsConfigDict 


class Settings(BaseSettings):
    APP_NAME: str = 'Apply backend'
    MONGODB_URL: str
    DB_NAME: str = "TodoCluster"
    model_config = SettingsConfigDict(env_file=".env")



settings = Settings()
