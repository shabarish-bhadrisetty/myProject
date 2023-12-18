from fastapi import APIRouter, Request

from scripts.constants import app_constants
from scripts.core.handlers.mongodb_structure_handler import Test
from scripts.logging.log_module import logger as log

setUp = APIRouter()
setup_obj = Test()


@setUp.get(app_constants.Endpoints.Display)
async def display():
    try:
        response = setup_obj.display()

        return response
    except Exception as e:
        log.error("Exception occurred while loading the service " + str(e))


@setUp.post(app_constants.Endpoints.update)
async def update(request: Request):
    try:
        input_json = await request.body()
        response = setup_obj.update(input_json)

        return response
    except Exception as e:
        log.error("Exception occurred while loading the service " + str(e))
