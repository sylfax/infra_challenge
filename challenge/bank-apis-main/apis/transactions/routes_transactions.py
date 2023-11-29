from typing import Union

from fastapi import APIRouter, Request


from models.payloads import ErrorMessage, TransactionPost, Transaction
from services import transactions_services

router = APIRouter()


@router.post("/{uuid_client}", status_code=201, summary="save a transaction of a client")
async def save_transaction(request: Request, uuid_client: str, transaction: TransactionPost) -> Union[ErrorMessage]:
    try:
        result = await transactions_services.save(request.app.database, uuid_client, transaction)
        return result
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


@router.get("/{uuid_client}", status_code=200, summary="get transactions of a client")
async def get_transactions(request: Request, uuid_client: str) -> Union[ErrorMessage, list[Transaction]]:
    try:
        result = await transactions_services.get_client_transactions(request.app.database, uuid_client)
        return result
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


@router.get("/", status_code=200, summary="get all transactions")
async def get_all_transactions(request: Request) -> Union[ErrorMessage, list[Transaction]]:
    try:
        result = await transactions_services.get_all_transactions(request.app.database)
        return result
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


@router.put("/uuid/{uuid_transaction}/{status}", status_code=200, summary="update the status of the transaction")
async def update_transaction_status(request: Request, uuid_transaction: str, status) -> Union[ErrorMessage]:
    try:
        result = await transactions_services.update_transaction_status(request.app.database, uuid_transaction, status)
        return result
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))
