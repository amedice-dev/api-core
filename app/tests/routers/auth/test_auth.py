import pytest
from rest_framework import status
from rest_framework.test import APIClient


class TestAuth:
    @pytest.mark.django_db
    async def test_auth_login(self, client: APIClient, owner_dict: dict, password: str):
        email = owner_dict["email"]
        login_payload = {"username": email, "password": password}

        response = await client.post("/auth/token", data=login_payload)
        assert response.status_code == status.HTTP_200_OK

        response_dict = response.json()
        assert type(response_dict["access"]) is str
        assert response_dict["token_type"] == "bearer"
