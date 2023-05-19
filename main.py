from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/index/", response_class=HTMLResponse)
def index(request: Request, hx_request: Optional[str] = Header(None)): #hx-request
    films=[
        {"name": "RRR","director":"SS Rajamouli","year":"2021"},
        {"name": "KGF","director":"Prashanth Neel","year":"2018"},
        {"name": "Bahubali","director":"SS Rajamouli","year":"2015"},
    ]

    context = {"request": request,'films':films}
    if hx_request:
        return templates.TemplateResponse("table.html", context)
    
    return templates.TemplateResponse("index.html", context)   