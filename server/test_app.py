import pytest
from unittest.mock import patch
from app import app

@pytest.fixture #This is a decorator used to prevent duplicating setup and configuration for each test
def mock_items(): #This function handles setting up the mock data to be used in the test
    """Provides a consistent mock inventory list for testing."""
    return [
        {"id": 1, "brands": "BrandA", "product_name": "Item 1", "code": "1234567891234"},
        {"id": 2, "brands": "BrandB", "product_name": "Item 2", "code": "7894561237894"}
    ]

@pytest.fixture
def client(mock_items):
    """Configures the Flask test client and mocks the global items list."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        with patch("app.items", mock_items):
            yield client

# Testing GET /inventory 

def test_show_items(client, mock_items):
    """Tests retrieving all inventory items."""
    response = client.get("/inventory")
    assert response.status_code == 200
    assert response.json == mock_items

# Testing GET /inventory/<id>

def test_show_item_success(client):
    """Tests retrieving a single item by a valid ID."""
    response = client.get("/inventory/1")
    assert response.status_code == 200
    assert response.json["product_name"] == "Item 1"

def test_show_item_not_found(client):
    """Tests error handling for a non-existent item ID."""
    response = client.get("/inventory/999")
    assert response.status_code == 404
    assert "error" in response.json

# Testing POST /inventory 

def test_add_item(client):
    """Tests creating a new inventory item."""
    new_payload = {
        "brands": "BrandC",
        "product_name": "Item 3",
        "code": "4561237891234"
    }
    response = client.post("/inventory", json=new_payload)
    assert response.status_code == 201
    assert "succesfully added" in response.json["message"]

# Testing PUT/PATCH /inventory/<id> 

def test_update_item_full(client):
    """Tests updating both fields of an item."""
    update_payload = {"brands": "BrandX", "product_name": "Updated Item"}
    response = client.patch("/inventory/1", json=update_payload)
    assert response.status_code == 200
    assert "updated successfully" in response.json["message"]

def test_update_item_partial(client):
    """Tests updating only one field of an item."""
    update_payload = {"product_name": "Partial Update"}
    response = client.patch("/inventory/2", json=update_payload)
    assert response.status_code == 200
    assert "updated successfully" in response.json["message"]

def test_update_item_not_found(client):
    """Tests updating an item that does not exist."""
    update_payload = {"product_name": "Ghost"}
    response = client.patch("/inventory/999", json=update_payload)
    assert response.status_code == 404

# Testing DELETE /inventory/<id> 

def test_delete_item_success(client):
    """Tests successfully deleting an item."""
    response = client.delete("/inventory/1")
    assert response.status_code == 200
    assert "deleted successfully" in response.json["message"]

def test_delete_item_not_found(client):
    """Tests deleting an item that does not exist."""
    response = client.delete("/inventory/999")
    assert response.status_code == 404
