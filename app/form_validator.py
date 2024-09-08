from pydantic import BaseModel

class Address(BaseModel):
    city: str
    district: str
    street: str

class Orders(BaseModel):
    id: str
    name: str
    address: Address
    price: str
    currency: str