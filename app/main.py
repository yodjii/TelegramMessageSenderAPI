from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.schemas.message import MessageRequest, MessageResponse
from app.services.telegram import telegram_service
from app.config import config
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title="Telegram Api Sender")

# Mount static files using absolute path
static_dir = os.path.join(BASE_DIR, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    index_path = os.path.join(static_dir, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/bots")
async def list_bots():
    return {"bots": config.list_bots(), "default": config.get_bot().chat_id if config.get_bot() else None}

@app.post("/send", response_model=MessageResponse)
async def send_message(request: MessageRequest):
    bot_cfg = config.get_bot(request.bot_name)
    if not bot_cfg:
        raise HTTPException(status_code=404, detail=f"Bot '{request.bot_name or 'default'}' not found in configuration")
    
    result = await telegram_service.send_message(bot_cfg, request.message)
    
    if result.get("ok"):
        return MessageResponse(
            status="success",
            bot_used=request.bot_name or config.default_bot_name,
            message_id=result.get("result", {}).get("message_id")
        )
    else:
        return MessageResponse(
            status="error",
            bot_used=request.bot_name or config.default_bot_name,
            error=result.get("error", "Unknown error")
        )

if __name__ == "__main__":
    import uvicorn
    # Use AlwaysData environment variables if available, else fallback to defaults
    host = os.getenv("IP", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)
