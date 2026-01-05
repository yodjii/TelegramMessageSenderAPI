import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import config, BotConfig
from unittest.mock import patch, MagicMock

client = TestClient(app)

def test_list_bots_fallback():
    """Verify that bots are listed from the fallback config/bots.json.example if bots.json missing"""
    bots = config.list_bots()
    assert isinstance(bots, list)
    assert len(bots) >= 1

def test_get_default_bot():
    bot = config.get_bot()
    assert bot is not None
    assert hasattr(bot, "token")
    assert hasattr(bot, "chat_id")

@patch("app.services.telegram.TelegramService.send_message")
def test_send_message_endpoint_success(mock_send):
    # Mock successful response from Telegram
    mock_send.return_value = {"ok": True, "result": {"message_id": 12345}}
    
    response = client.post("/send", json={
        "message": "Test message",
        "bot_name": "bot1"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message_id"] == 12345

@patch("app.services.telegram.TelegramService.send_message")
def test_send_message_endpoint_error(mock_send):
    # Mock error response from Telegram
    mock_send.return_value = {"ok": False, "error": "Unauthorized"}
    
    response = client.post("/send", json={
        "message": "Test message",
        "bot_name": "bot1"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert data["error"] == "Unauthorized"

def test_send_message_bot_not_found():
    response = client.post("/send", json={
        "message": "Test message",
        "bot_name": "non_existent_bot"
    })
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
