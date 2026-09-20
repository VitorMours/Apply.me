import pytest
from main import app
from fastapi.testclient import TestClient 


client = TestClient(app)

class TestWebRoutes:
  def test_if_is_running(self) -> None:
    assert True 
    
  def test_if_web_index_route_exists(self) -> None:
    response = client.get("/")
    assert response.status_code == 200 
    headers = response.headers 
    assert "text/html" in headers["Content-Type"]
    
    