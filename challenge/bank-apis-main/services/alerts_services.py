import uuid
from typing import Union
from decouple import config
import motor.motor_asyncio
import datetime

from models.payloads import ErrorMessage, AlertPost, SuccessMessage, AlertDTO
from models.Alert import Alert


async def get_all_alerts(database: motor.motor_asyncio.AsyncIOMotorDatabase) -> Union[ErrorMessage, list[AlertDTO]]:
    try:
        alerts_db = database[config("ALERTS_COLLECTION")].find()
        alerts = []
        async for alert_db in alerts_db:
            alert = alert_mapping(alert_db)
            alerts.append(alert)
        return alerts
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


async def get_alert(database: motor.motor_asyncio.AsyncIOMotorDatabase, alert_uuid: str) -> Union[ErrorMessage, AlertDTO]:
    try:
        alert_db = await database[config("ALERTS_COLLECTION")].find_one({"uuid": alert_uuid})
        if not alert_db:
            return ErrorMessage(status="404", message="Alert not found!")
        alert = alert_mapping(alert_db)
        return alert
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


async def save(database: motor.motor_asyncio.AsyncIOMotorDatabase, alert_post: AlertPost) \
        -> Union[ErrorMessage, SuccessMessage]:
    try:
        alert = Alert(uuid=str(uuid.uuid4()),
                      ref_transaction=alert_post.ref_transaction,
                      ref_client=alert_post.ref_client,
                      date=datetime.datetime.now(),
                      type=alert_post.type,
                      comment=alert_post.comment)
        await database[config("ALERTS_COLLECTION")].insert_one(alert.model_dump())
        return SuccessMessage(status="201", message="Alert saved")
    except Exception as exc:
        return ErrorMessage(status="500", message="Internal server error".format(exc))


def alert_mapping(alert_db: dict) -> AlertDTO:
    return AlertDTO(ref_client=alert_db['ref_client'],
                    ref_transaction=alert_db['ref_transaction'],
                    uuid=alert_db['uuid'],
                    date=alert_db['date'].strftime("%Y-%m-%d %H:%M:%S"),
                    type=alert_db['type'],
                    comment=alert_db['comment'])


