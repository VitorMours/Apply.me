import pytest 
from unittest.mock import AsyncMock, MagicMock


@pytest.fixture
def mock_llm_response():
    def _make(content: str):
        mock_result = MagicMock()
        mock_result.content = content
        return mock_result
    return _make