from fastapi import FastAPI, HTTPException, status

# import database
from Models import *
from Code import *

# from database import *
# from sqlalchemy.orm import Session

app = FastAPI()

info = CarInfo()


@app.post("/")
def create_car_details(user_name: str, user_brand: str, user_id: int):
    result = info.enterdetails(user_name, user_brand, user_id)
    if result:
        return result

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="The Id cant be changed")


@app.get("/")
def get_car_details():
    myresult = info.get_details()
    return myresult


@app.get("/{name}")
def get_name_details(name: str):
    myresult = info.get_details_name(name)
    if myresult:
        return myresult

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The details not found")


@app.put("/{id}")
def update_car_details(user_id: int, user_name: str, user_brand: str):
    myresult = info.update_details(user_id, user_name, user_brand)
    if myresult:
        return myresult

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The details not found")


@app.delete("/{id}")
def delete_car_details(user_id: int):
    myresult = info.delete_details(user_id)
    if myresult:
        return myresult

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The details not found")
