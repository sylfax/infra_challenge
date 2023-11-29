import uuid
from typing import Union

import motor.motor_asyncio
from decouple import config

from models.Customer import Customer
from models.payloads import ErrorMessage, SuccessMessage, AccountClientSignUp


async def onboard(database: motor.motor_asyncio.AsyncIOMotorDatabase, client_sign_up: AccountClientSignUp) \
        -> Union[ErrorMessage, SuccessMessage]:
    try:
        username_db = await database[config("ACCOUNTS_COLLECTION")].find_one({"username": client_sign_up.username})
        if username_db:
            return ErrorMessage(status="404", message="username already exists!")
        customer = customer_mapping(client_sign_up)
        result = await database[config("ACCOUNTS_COLLECTION")].insert_one(customer.model_dump())
        return SuccessMessage(status="200", message="Client onboarded")
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


def customer_mapping(client_sign_up: AccountClientSignUp):
    customer = Customer(uuid=str(uuid.uuid4()),
                        username=client_sign_up.username,
                        password=client_sign_up.password,
                        first_name=client_sign_up.firstNameClient,
                        last_name=client_sign_up.lastNameClient,
                        nationality=client_sign_up.nationalityClient,
                        company=client_sign_up.company,
                        birthdate=client_sign_up.birthDateClient,
                        address=client_sign_up.addressClient,
                        city=client_sign_up.cityClient,
                        country=client_sign_up.countryClient,
                        email=client_sign_up.emailClient,
                        risk=client_sign_up.risk,
                        actions=client_sign_up.actions)
    return customer
