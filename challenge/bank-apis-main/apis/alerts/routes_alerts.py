from typing import Union

from fastapi import APIRouter, Request

from models.payloads import ErrorMessage, AlertPost, AlertDTO
from services import alerts_services

router = APIRouter()


@router.get("/", status_code=200, summary="get all alerts")
async def get_all_alerts(request: Request) -> Union[ErrorMessage, list[AlertDTO]]:
    try:
        result = await alerts_services.get_all_alerts(request.app.database)
        return result
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


@router.get("/{alert_uuid}", status_code=200, summary="get one alert")
async def get_one_alert(request: Request, alert_uuid: str) -> Union[ErrorMessage, AlertDTO]:
    try:
        result = await alerts_services.get_alert(request.app.database, alert_uuid)
        return result
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


@router.post("/", status_code=201, summary="create and save an alert")
async def save_alert(request: Request, alert_post: AlertPost) -> Union[ErrorMessage]:
    try:
        result = await alerts_services.save(request.app.database, alert_post)
        return result
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))