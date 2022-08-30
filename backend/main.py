import uvicorn
import backend.controller
from fastapi import FastAPI

from sqlalchemy.exc import SQLAlchemyError

from backend import __version__, controller


# noinspection PyUnresolvedReferences
from backend.core.config import settings  # noqa


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(controller.router)
    return app


app = create_app()
app.include_router(backend.controller.router)


if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8010, reload=True)



