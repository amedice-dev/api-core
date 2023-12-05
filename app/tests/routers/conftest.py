import pytest
from faker import Faker
from rest_framework.test import APIClient
from rest_framework import status

from app.users.models import User


@pytest.fixture(scope="session")
def password():
    """User password."""
    fake = Faker()
    return fake.password()


@pytest.fixture(scope="session")
def owner_payload(password: str):
    """Owner payload fixture."""
    fake = Faker()
    return {
        "email": fake.email(),
        "password": password,
        "first_name": "John",
        "last_name": "Doe",
        "phone_number": "+38921391213",
        "user_role": "Owners",
    }


@pytest.fixture(scope="session")
def visitor_payload(password: str):
    """Visitor payload fixture."""
    fake = Faker()
    return {
        "email": fake.email(),
        "password": password,
        "first_name": "Sam",
        "last_name": "Smith",
        "phone_number": "+72399494449",
        "user_role": "Visitors",
    }


@pytest.fixture(scope="session")
def administrator_payload(password: str):
    """Administrator payload fixture."""
    fake = Faker()
    return {
        "email": fake.email(),
        "password": password,
        "first_name": "Bob",
        "last_name": "Brown",
        "phone_number": "+109598583838",
        "user_role": "Administrators",
    }


@pytest.fixture(scope="session")
async def owner_dict(client: APIClient, owner_payload: dict):
    """Owner dict fixture."""
    response = await client.post("/auth/register", json=owner_payload)
    assert response.status_code == status.HTTP_201_CREATED
    owner_dict = response.json()
    assert "id" in owner_dict.keys()
    yield owner_dict
    user_id = owner_dict["id"]
    User.objects.filter(id=user_id).delete()


@pytest.fixture(scope="session")
async def authorization(client: APIClient, owner_dict: dict, password: str):
    """Authorization header value."""
    email = owner_dict["email"]
    login_payload = {"username": email, "password": password}
    response = await client.post("/auth/token", data=login_payload)
    access_token = response.json()["access"]
    return f"Bearer {access_token}"
