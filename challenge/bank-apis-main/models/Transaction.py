from typing import Optional
import datetime
from pydantic import BaseModel


class Transaction(BaseModel):
    uuid: str
    from_client: str
    to_client: str
    amount: float
    date: datetime.datetime
    status: Optional[str] = 'pending'
