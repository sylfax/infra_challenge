from typing import Union

from fastapi import APIRouter, Request

from models.payloads import AccountSignIn, ErrorMessage, SuccessMessage, UserSignedIn
from services import auth_services

router = APIRouter()


@router.post("/login", status_code=200, summary="Sign in of a client")
async def signin(request: Request, account_sign_in: AccountSignIn) -> Union[ErrorMessage, UserSignedIn]:
    try:
        print("account: {}".format(account_sign_in))
        result = await auth_services.signin(request.app.database, account_sign_in)
        return result
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))