from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis.apis_base import api_router
import motor.motor_asyncio
from decouple import config

app = FastAPI()


def include_router(app_tmp):
    """
    add router for the API
    :param app_tmp: FastAPI app
    :return: None
    """
    app_tmp.include_router(api_router)


def start_application():
    app_temp = FastAPI(title="API for Bank (Tezos hackathon)")
    origins = [
        "*"
    ]
    app_temp.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app_temp)
    return app_temp


app = start_application()


@app.on_event("startup")
def startup():
    app.mongodb_client = motor.motor_asyncio.AsyncIOMotorClient(config("MONGODB_URL"))
    app.database = app.mongodb_client[config("MONGODB_DBNAME")]


@app.on_event("shutdown")
def shutdown():
    app.mongodb_client.close()
