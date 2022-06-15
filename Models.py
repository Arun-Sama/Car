from pydantic import BaseModel


class CarDetails(BaseModel):
    id: int
    name: str
    brand: str

    class Config:
        orm_mode = True
