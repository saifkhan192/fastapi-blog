import os

from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.routing import Route

from app.core import auth, blog, user
from app.core.configs import get_app_settings
from app.database.configuration import engine
from app.models import models

settings = get_app_settings()

models.Base.metadata.create_all(bind=engine)
app = FastAPI(**settings.fastapi_kwargs)

app.mount("/static", StaticFiles(directory="static", html=True))

if settings.allowed_hosts:
    app.add_middleware(
        CORSMiddleware,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
        allow_origins=[origin for origin in settings.allowed_hosts],
    )

app.include_router(blog.router, prefix="/api")
app.include_router(user.router, prefix="/api")
app.include_router(auth.router, prefix="/api")


@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <body>
            <h1>SecureAPI</h1>
            <a href="/docs"><button>SwaggerUI</button></a>
            <a href="/redoc"><button>Redoc</button></a>
        </body>
    </html>
"""


@app.get("/debug")
def debug():
    return settings.__dict__


port = int(os.environ.get("port", "8001"))
if settings.debug:
    from tabulate import tabulate

    url = f"http://127.0.0.1:{port}"
    url_list = [
        [url + route.path, route.name]
        for route in app.routes
        if isinstance(route, Route) or isinstance(route, APIRoute)
    ]

    print(
        tabulate(
            url_list,
            headers=["Path", "Name"],
            showindex="always",
            tablefmt="double_outline",
        )
    )
