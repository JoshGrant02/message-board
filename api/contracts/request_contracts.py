from pydantic import BaseModel
from datetime import datetime

class createMessageRequest(BaseModel):
    message: str
    createdWhen: datetime
    createdWho: str
