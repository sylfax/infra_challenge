from typing import Optional

from pydantic import BaseModel


class Customer(BaseModel):
    uuid: str
    username: str
    password: str
    first_name: str
    last_name: str
    nationality: str
    company: bool = False
    birthdate: Optional[str] = None
    address: str
    city: str
    country: str
    email: str
    risk: Optional[str] = 'low'
    actions: Optional[str] = 'no'
