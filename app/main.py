from typing import Union
from form_validator import Orders

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/orders")
def check_orders(orders: Orders):
    print (orders)
    return orders
    