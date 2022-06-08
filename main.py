from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from math import pi

app = FastAPI()
class User(BaseModel):
   ID: int
   username: str
   password: str

@app.get("/")
async def connect():
    return {"Hello" : "World"} 

@app.get("/area")
async def area(w: int, h: int):
    data = 1/2*w*h
    print(data)
    return data

@app.get("/circle")
async def circle(r: float):
    cir = 2*pi*r
    return {"circumferance": f"Circumferance: {cir:.2f}"}

@app.get("/circle_area")
async def circle_area(r: float):
    res = pi*r*r
    return {"area_circle": f"Area circle: {res:.2f}"}

@app.post("/account")
async def account(user: User):
    return user

if __name__ == "__main__":
    uvicorn.run("main:app", host=('0.0.0.0'), port=(8000), reload=True)