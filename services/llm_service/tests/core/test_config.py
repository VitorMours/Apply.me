from src.core.config import Settings


def test_default_ollama_base_url_targets_host_docker_internal(monkeypatch):
    monkeypatch.delenv("OLLAMA_BASE_URL", raising=False)

    settings = Settings()

    assert settings.OLLAMA_BASE_URL == "http://host.docker.internal:11434"
