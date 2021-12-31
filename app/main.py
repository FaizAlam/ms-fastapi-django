from os import DirEntry
from fastapi import FastAPI, Request
import json
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))



@app.get("/", response_class=HTMLResponse)
def home_view(request:Request):
    print(request)
    return templates.TemplateResponse("home.html",{"request":request,"abc":123})


@app.post("/")
def home_detail_view():
    return {"hello":"world"}