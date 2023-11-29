from typing import Union

import motor.motor_asyncio
from decouple import config
from models.payloads import CustomerDTO, ErrorMessage


async def load_all(database: motor.motor_asyncio.AsyncIOMotorDatabase) -> Union[ErrorMessage, list[CustomerDTO]]:
    try:
        customers_db = database[config("ACCOUNTS_COLLECTION")].find()
        customers = []
        async for customer_db in customers_db:
            customer = customer_mapping(customer_db)
            customers.append(customer)
        return customers
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


async def load(database: motor.motor_asyncio.AsyncIOMotorDatabase, uuid: str) -> Union[ErrorMessage, CustomerDTO]:
    try:
        customer_db = await database[config("ACCOUNTS_COLLECTION")].find_one({"uuid": uuid})
        if not customer_db:
            return ErrorMessage(status="404", message="Customer not found!")
        customer = customer_mapping(customer_db)
        return customer
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


def customer_mapping(customer_db: dict) -> CustomerDTO:
    customer = CustomerDTO(
        uuid=customer_db["uuid"],
        username=customer_db["username"],
        firstNameClient=customer_db["first_name"],
        lastNameClient=customer_db["last_name"],
        nationalityClient=customer_db["nationality"],
        company=customer_db["company"],
        birthDateClient=customer_db["birthdate"],
        addressClient=customer_db["address"],
        cityClient=customer_db["city"],
        countryClient=customer_db["country"],
        emailClient=customer_db["email"],
        risk=customer_db["risk"],
        actions=customer_db["actions"],
    )
    return customer


