from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/index/", response_class=HTMLResponse)
def index(request: Request):
    films=[
        {"name": "RRR","director":"SS Rajamouli","year":"2021"},
        {"name": "KGF","director":"Prashanth Neel","year":"2018"},
        {"name": "Bahubali","director":"SS Rajamouli","year":"2015"},
    ]

    context = {"request": request,'films':films}
    return templates.TemplateResponse("index.html", context)   