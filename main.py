from re import A
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from callback import Callback

activity = Callback(user="root", password="2362539", database="user", dictionary=True)

app = FastAPI()
class User(BaseModel):
   username: str
   first_name: str
   last_name: str
   password: str

@app.get("/database")
async def database():
    data = activity.select(table_name="hardware_control")
    
@app.get("/")
async def connect():
    return {"Hello" : "World"} 

@app.get("/sample")
async def show_table():
    data = activity.show_table()
    return data

@app.get("/sample/{table_name}")
async def select(table_name):
    data = activity.select(table_name)
    return data

@app.get("/user/change")
async def change(Id, username, password):
   data = activity.update(table_name="account", Id=Id, username=username, password=password)
   print(data)

@app.post("/register")
async def register(user: User):
    data = activity.register(user, table_name="account") 
    return data

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