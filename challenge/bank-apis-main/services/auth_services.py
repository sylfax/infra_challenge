from typing import Union

import motor.motor_asyncio
from decouple import config

from models.Customer import Customer
from models.payloads import AccountSignIn, ErrorMessage, UserSignedIn


async def signin(database: motor.motor_asyncio.AsyncIOMotorDatabase, client_sign_in: AccountSignIn) -> Union[ErrorMessage, UserSignedIn]:
    try:
        user = await database[config("ACCOUNTS_COLLECTION")].find_one({"username": client_sign_in.username})
        if user and user["password"] == client_sign_in.password:
            user_sign_in = user_signed_in_mapping(user)
            return user_sign_in
        return ErrorMessage(status="404", message="Internal server error")
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


def user_signed_in_mapping(customer: dict) -> UserSignedIn:
    user_sign_in = UserSignedIn(uuid=customer['uuid'],
                                username=customer['username'],
                                firstNameClient=customer['first_name'],
                                lastNameClient=customer['last_name'],
                                nationalityClient=customer['nationality'],
                                company=customer['company'],
                                birthDateClient=customer['birthdate'],
                                addressClient=customer['address'],
                                cityClient=customer['city'],
                                countryClient=customer['country'],
                                emailClient=customer['email'],
                                risk=customer['risk'],
                                actions=customer['actions'])
    return user_sign_in


