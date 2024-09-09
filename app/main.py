from typing import Union
from form_validator import Orders
from service import NameProcessor, PriceProcessor, CurrencyProcessor

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/api/orders")
def check_orders(orders: Orders):
    def raise_if_400(http_code, message):
        if http_code==400:
            raise HTTPException(status_code=http_code, detail=message)
    
    name_processor = NameProcessor(orders)
    raise_if_400(*name_processor.process())
    orders=name_processor.orders

    price_processor = PriceProcessor(orders)
    raise_if_400(*price_processor.process())
    orders=price_processor.orders
    
    currency_processor = CurrencyProcessor(orders)
    raise_if_400(*currency_processor.process())
    orders=currency_processor.orders
    return orders
    