import logging
import uvicorn

from fastapi import FastAPI, Request
from fastapi.logger import logger

app = FastAPI()
logging.getLogger("uvicorn.error")


@app.middleware("http")
async def add_ip(request: Request, call_next):
    request.state.ip = request.client.host
    logger.info(request.state.ip)
    response = await call_next(request)
    return response


@app.get("/")
async def index(request: Request):
    logger.info("hi")
    return {"msg": "hello"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True, debug=True, log_leve="DEBUG")
