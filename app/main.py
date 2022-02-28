import yaml

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@router.get("/functions", response_class=HTMLResponse)
async def functions(request: Request):
    with open("app/functions.yml") as f:
        functions = yaml.safe_load(f)

    return templates.TemplateResponse(
        "functions.html",
        {
            "request": request,
            "functions": functions
            }
    )

@router.get("/statistics", response_class=HTMLResponse)
async def statistics(request: Request):
    return templates.TemplateResponse(
        "statistics.html",
        {"request": request}
    )

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        "devtest.html",
        {"request": request}
    )




@router.get("/devtest", response_class=HTMLResponse)
async def devtest(request: Request):
    return templates.TemplateResponse(
        "devtest.html",
        {"request": request}
    )
