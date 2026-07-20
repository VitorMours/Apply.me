from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    MODEL_NAME: str = "llama3.1"
    OLLAMA_BASE_URL: str = "http://ollama:11434"

    class Config:
        env_file = ".env"


settings = Settings()