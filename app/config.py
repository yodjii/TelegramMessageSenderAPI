import json
import os
from pathlib import Path
from typing import Dict, Optional
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class BotConfig(BaseModel):
    token: str
    chat_id: str

class AppConfig:
    def __init__(self):
        # Resolve path relative to the project root (one level up from app/)
        self.base_dir = Path(__file__).resolve().parent.parent
        default_config = str(self.base_dir / "config" / "bots.json")
        
        self.config_path = os.getenv("CONFIG_FILE", default_config)
        self.default_bot_name = os.getenv("DEFAULT_BOT_NAME", "bot1")
        self._config_data = self._load_config()

    def _load_config(self) -> Dict:
        if not Path(self.config_path).exists():
            # Fallback to example if bots.json doesn't exist yet for dev
            example_path = f"{self.config_path}.example"
            if Path(example_path).exists():
                with open(example_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            return {"bots": {}, "default_bot": ""}
        
        with open(self.config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_bot(self, name: Optional[str] = None) -> Optional[BotConfig]:
        bot_name = name or self._config_data.get("default_bot") or self.default_bot_name
        bots = self._config_data.get("bots", {})
        
        if bot_name in bots:
            return BotConfig(**bots[bot_name])
        return None

    def list_bots(self) -> list:
        return list(self._config_data.get("bots", {}).keys())

config = AppConfig()
