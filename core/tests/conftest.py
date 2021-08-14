import pytest
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

@pytest.fixture
def admin_user():
    user = User.objects.create(username="admin", email="email@email.com", is_superuser=True)
    return user

@pytest.fixture
def regular_user():
    user = User.objects.create(username="regular", email="regular@email.com", is_superuser=False)
    return user

@pytest.fixture
def regular_client(regular_user):
    token, created = Token.objects.get_or_create(user=regular_user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Authorization ' + token.key)
    return client

@pytest.fixture
def admin_client(admin_user):
    token, created = Token.objects.get_or_create(user=admin_user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Authorization ' + token.key)
    return client
