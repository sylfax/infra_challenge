from typing import Union

from fastapi import APIRouter, Request

from models.payloads import ErrorMessage, CustomerDTO
from services import customers_services

router = APIRouter()


@router.get("/", status_code=200, summary="get all customers")
async def get_all_customers(request: Request) -> Union[ErrorMessage,list[CustomerDTO]]:
    try:
        customers = await customers_services.load_all(request.app.database)
        return customers
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


@router.get("/{uuid}", status_code=200, summary="get one customer")
async def get_customer(request: Request, uuid: str) -> Union[ErrorMessage, CustomerDTO]:
    try:
        customer = await customers_services.load(request.app.database, uuid)
        return customer
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))
