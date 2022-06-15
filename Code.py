from sqlalchemy.orm import Session

# import Models
from Models import *
from database import *


class CarInfo:

    def enterdetails(self, user_name, user_brand, user_id):
        db = Session(engine)
        user = CarDetails(name=user_name, brand=user_brand, id=user_id)
        car_info = Cars(id=user.id, name=user.name, brand=user.brand)
        db.add(car_info)
        db.commit()
        return "The details is updated"

    def get_details(self):
        db = Session(engine)
        result = db.query(Cars).all()
        return result

    def get_details_name(self, name):
        db = Session(engine)
        result = db.query(Cars).filter(Cars.name == name).first()
        return result

    def update_details(self, user_id, user_name, user_brand):
        db = Session(engine)
        result = db.query(Cars).filter(Cars.id == user_id).update({'name': user_name, 'brand': user_brand})
        db.commit()
        return result

    def delete_details(self, user_id):
        db = Session(engine)
        result = db.query(Cars).filter(Cars.id == user_id).delete()
        db.commit()
        return "It is deleted"
