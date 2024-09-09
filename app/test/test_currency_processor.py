from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_is_check_currency_1():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '2000',  # Price exceeds limit
        "currency": "TWD"
    })
    assert response.status_code == 200

def test_is_check_currency_2():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '20',  # Price exceeds limit
        "currency": "USD"
    })
    assert response.status_code == 200
    
def test_is_check_currency_3():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '20',  # Price exceeds limit
        "currency": "NTD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Currency format is wrong"}
    
def test_convert_currency_1():
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
    assert response.json() == {
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '2000',  
        "currency": "TWD"
    }
    
def test_convert_currency_2():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '100',  
        "currency": "USD"
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '3100',  
        "currency": "TWD"
    }