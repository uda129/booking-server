from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_is_all_name_letters_1():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '1000',  
        "currency": "TWD"
    })
    assert response.status_code == 200

def test_is_all_name_letters_2():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Gran$d ^Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '1000',  
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Name contains non-English characters"}
    
def test_is_all_name_letters_3():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand 1Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '1000',  
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Name contains non-English characters"}
    
    
def test_are_name_initials_uppercase_1():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand Hotel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '1000', 
        "currency": "TWD"
    })
    assert response.status_code == 200

def test_are_name_initials_uppercase_2():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "Grand otel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '1000',  
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Name is not capitalized"}

def test_are_name_initials_uppercase_3():
    response = client.post("/api/orders", json={
        "id": "A0000003",
        "name": "rand otel",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": '1000',  
        "currency": "TWD"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Name is not capitalized"}
