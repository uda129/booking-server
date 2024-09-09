from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_is_price_above_threshold_1():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '2000',  
        "currency": "TWD"
    })
    assert response.status_code == 200

def test_is_price_above_threshold_2():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '2001',  
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Price is over 2000"}
    