from typing import Union
from fastapi import APIRouter, Request

from models.payloads import AccountClientSignUp, ErrorMessage, SuccessMessage
from services import onboarding_services

router = APIRouter()


@router.post("/", status_code=201, summary="Onboard a client")
async def onboard(request: Request, client_sign_up: AccountClientSignUp) -> Union[ErrorMessage, SuccessMessage]:
    try:
        result = await onboarding_services.onboard(request.app.database, client_sign_up)
        return result
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))