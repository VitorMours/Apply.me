from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    MODEL_NAME: str = "qwen3:0.6b"
    OLLAMA_BASE_URL: str = "http://localhost:11434"

    class Config:
        env_file = ".env"


settings = Settings()