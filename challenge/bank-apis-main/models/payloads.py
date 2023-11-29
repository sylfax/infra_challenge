import datetime
from typing import Optional

from pydantic import BaseModel


class ErrorMessage(BaseModel):
    status: str
    message: str


class SuccessMessage(BaseModel):
    status: str
    message: str


class AccountClientSignUp(BaseModel):
    username: str
    password: str
    firstNameClient: str
    lastNameClient: str
    nationalityClient: str
    company: bool = False
    birthDateClient: Optional[str] = None
    addressClient: str
    cityClient: str
    countryClient: str
    emailClient: str
    risk: Optional[str] = 'low'
    actions: Optional[str] = 'no'


class AccountSignIn(BaseModel):
    username: str
    password: str


class UserSignedIn(BaseModel):
    uuid: str
    username: str
    firstNameClient: str
    lastNameClient: str
    nationalityClient: str
    company: bool = False
    birthDateClient: Optional[str] = None
    addressClient: str
    cityClient: str
    countryClient: str
    emailClient: str
    risk: Optional[str] = 'low'
    actions: Optional[str] = 'no'


class TransactionPost(BaseModel):
    to_client: str
    amount: float
    status: Optional[str] = "pending"


class Transaction(BaseModel):
    uuid: str
    username: str
    from_client: str
    to_client: str
    amount: float
    date: str
    status: Optional[str] = 'pending'


class AlertPost(BaseModel):
    ref_client: str
    ref_transaction: str
    type: list[int] = []
    comment: str


class AlertDTO(BaseModel):
    uuid: str
    ref_client: str
    ref_transaction: str
    date: datetime.datetime
    type: list[int] = []
    comment: str


class CustomerDTO(BaseModel):
    uuid: str
    username: str
    firstNameClient: str
    lastNameClient: str
    nationalityClient: str
    company: bool = False
    birthDateClient: Optional[str] = None
    addressClient: str
    cityClient: str
    countryClient: str
    emailClient: str
    risk: Optional[str] = 'low'
    actions: Optional[str] = 'no'

