from pydantic import BaseModel
import datetime


class Alert(BaseModel):
    uuid: str
    ref_client: str
    ref_transaction: str
    date: datetime.datetime
    type: list[int] = []
    comment: str
