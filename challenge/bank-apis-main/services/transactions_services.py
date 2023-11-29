import datetime
import uuid
from typing import Union, List, Any

import motor.motor_asyncio
from decouple import config

import models.payloads
from models.Transaction import Transaction
from models.payloads import TransactionPost, ErrorMessage, SuccessMessage


async def save(database: motor.motor_asyncio.AsyncIOMotorDatabase, uuid_client: str, transaction_post: TransactionPost) \
        -> [ErrorMessage, SuccessMessage]:
    try:
        customer = await database[config("ACCOUNTS_COLLECTION")].find_one({"uuid": uuid_client})
        if not customer:
            return ErrorMessage(status="404", message="Customer not found!")
        transaction = transaction_mapping(uuid_client, transaction_post)
        await database[config("TRANSACTIONS_COLLECTION")].insert_one(transaction.model_dump())
        return SuccessMessage(status="200", message="Transaction saved")
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


async def get_client_transactions(database: motor.motor_asyncio.AsyncIOMotorDatabase, uuid_client: str) \
        -> ErrorMessage | list[models.payloads.Transaction]:
    try:
        customer = await database[config("ACCOUNTS_COLLECTION")].find_one({"uuid": uuid_client})
        if not customer:
            return ErrorMessage(status="404", message="Customer not found!")
        transactions_db = database[config("TRANSACTIONS_COLLECTION")].find({"from_client": uuid_client})
        transactions = []
        async for transaction_db in transactions_db:
            transaction = transaction_mapping_2(transaction_db, customer['username'])
            transactions.append(transaction)
        return transactions
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


async def get_all_transactions(database: motor.motor_asyncio.AsyncIOMotorDatabase):
    try:
        transactions_db = database[config("TRANSACTIONS_COLLECTION")].find()
        transactions = []
        async for transaction_db in transactions_db:
            customer = await database[config("ACCOUNTS_COLLECTION")].find_one({"uuid": transaction_db["from_client"]})
            transaction = transaction_mapping_2(transaction_db, customer['username'])
            transactions.append(transaction)
        return transactions
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


async def update_transaction_status(database: motor.motor_asyncio.AsyncIOMotorDatabase,
                                    uuid_transaction: str, status: str):
    try:
        transaction_db = await database[config("TRANSACTIONS_COLLECTION")].find_one({"uuid": uuid_transaction})
        if not transaction_db:
            return ErrorMessage(status="404", message="Transaction not found!")
        transaction_db["status"] = status
        await database[config("TRANSACTIONS_COLLECTION")].replace_one({"uuid": uuid_transaction}, transaction_db)
        return SuccessMessage(status="200", message="Transaction status updated")
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


def transaction_mapping(client_uuid: str, transaction_post: TransactionPost) -> Transaction:
    transaction = Transaction(uuid=str(uuid.uuid4()),
                              date=datetime.datetime.now(),
                              from_client=client_uuid,
                              to_client=transaction_post.to_client,
                              status=transaction_post.status,
                              amount=transaction_post.amount)
    return transaction


def transaction_mapping_2(transaction_db: dict, username: str) -> models.payloads.Transaction:
    transaction = models.payloads.Transaction(uuid=transaction_db["uuid"],
                                              username=username,
                                              date=transaction_db["date"].strftime("%Y-%m-%d %H:%M:%S"),
                                              from_client=transaction_db["from_client"],
                                              to_client=transaction_db["to_client"],
                                              amount=transaction_db["amount"],
                                              status=transaction_db["status"])

    return transaction


