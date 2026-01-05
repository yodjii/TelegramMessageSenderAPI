import httpx
from typing import Optional
from app.config import BotConfig

class TelegramService:
    @staticmethod
    async def send_message(bot_config: BotConfig, text: str) -> dict:
        url = f"https://api.telegram.org/bot{bot_config.token}/sendMessage"
        payload = {
            "chat_id": bot_config.chat_id,
            "text": text,
            "parse_mode": "HTML"
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, timeout=10.0)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                return {"ok": False, "error": f"HTTP error {e.response.status_code}: {e.response.text}"}
            except Exception as e:
                return {"ok": False, "error": str(e)}

telegram_service = TelegramService()
