from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Message(BaseModel):
    messageId: int
    message: str
    createdWhen: datetime
    createdWho: str