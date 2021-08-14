import pytest


@pytest.mark.django_db
def test_create_user_unauthenticated(client):
    response = client.post("/api/users/", data={"email": "email@email.com", "username": "test"})
    assert response.status_code == 201
@pytest.mark.django_db
def test_create_user_as_regular_user(regular_client):
    response = regular_client.post("/api/users/", data={"email": "email@email.com", "username": "test"})
    assert response.status_code == 201
@pytest.mark.django_db
def test_create_user_as_admin_user(admin_client):
    response = admin_client.post("/api/users/", data={"email": "email@email.com", "username": "test"})
    assert response.status_code == 201