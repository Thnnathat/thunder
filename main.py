from fastapi import FastAPI
from h11 import Data
import uvicorn
from pydantic import BaseModel
from typing import Dict
from database_main import Activity
from math import pi

database = Activity(user="root", password="2362539", database="sample", dictionary=True)

app = FastAPI()
class User(BaseModel):
   ID: int
   username: str
   password: str
   admin: Dict[str, str] = {"username": "admin", "password": "admin"}

@app.get("/")
async def connect():
    return {"Hello" : "World"} 

@app.get("/myname")
async def myname(name):
    name = {"name": name}
    return name

@app.get("/area")
async def area(w: int, h: int):
    data = 1/2*w*h
    print(data)
    return data

@app.get("/circle")
async def circle(r: float):
    cir = 2*pi*r
    data = {"circumferance": f"Circumferance: {cir:.2f}"}
    return data

@app.get("/circle_area")
async def circle_area(r: float):
    res = pi*r*r
    return {"area_circle": f"Area circle: {res:.2f}"}

@app.get("/{table}")
async def select(table):
    se = database.activity_select_all(table)
    return se

@app.post("/account_admin")
async def account(user: User):
    username = user.username
    password = user.password
    if (user.admin["username"] == username and user.admin["password"] == password):
        data = {"Status": "Login succeses", "error": False}
    else:
        data = {"status": "Login fail", "error": True}
    return data

if __name__ == "__main__":
    uvicorn.run("main:app", host=('0.0.0.0'), port=(8000), reload=True)