from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from accounts.models import User
from events.models import Stadium


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="admin@admin.com", password="a/@1234567", is_verified=True, is_staff=True, is_superuser=True
    )
    return user


@pytest.mark.django_db
class TestEventApi:
    def test_get_event_response_200_status(self, api_client):
        url = reverse("events:api-v1:event-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_event_response_401_status(self, api_client):
        url = reverse("events:api-v1:event-list")
        data = {
            "name": "test_event",
            "stadium": 1,
            "date": datetime.now(),
            "description": "description",
            "price": 100,
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_event_response_201_status(self, api_client, common_user):
        url = reverse("events:api-v1:event-list")
        stadium_data = {
            "name": "test_stadium",
            "capacity": 100,
            "city": "test",
            "country": "test",
            "address": "test",
            "opened": 100,
            "description": "test",
        }
        created_stadium = Stadium.objects.create(**stadium_data)
        stadium_pk = created_stadium.pk

        data = {
            "name": "test_event",
            "stadium": stadium_pk,
            "date": "2023-11-07",
            "price": 22,
            "description": "descripttion"
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_event_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("events:api-v1:event-list")
        data = {
            "name": "test_event",
            "stadium": 1,
            "date": "2023-11-07",
            "price": 22,
            "description": "descripttion"
        }
        user = common_user

        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
