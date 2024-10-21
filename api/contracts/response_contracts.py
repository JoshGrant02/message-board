from pydantic import BaseModel
from typing import List, Optional

from contracts.data_contracts import Message

class getMessagesResponse(BaseModel):
    messages: List[Message]
