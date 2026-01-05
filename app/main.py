from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.schemas.message import MessageRequest, MessageResponse
from app.services.telegram import telegram_service
from app.config import config
import os

app = FastAPI(title="Telegram Api Sender")

# Mount static files for the web interface
# We'll use the static folder for both index.html and any assets
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("app/static/index.html", "r", encoding="utf-8") as f:
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
    uvicorn.run(app, host="0.0.0.0", port=8000)
