from pydantic import BaseModel, Field
from typing import Optional

class MessageRequest(BaseModel):
    message: str = Field(..., description="The message content to send")
    bot_name: Optional[str] = Field(None, description="Name of the bot to use. Uses default if not provided.")

class MessageResponse(BaseModel):
    status: str
    bot_used: str
    message_id: Optional[int] = None
    error: Optional[str] = None
