from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_weather_api_empty_city(api_client):
    """Тест на пустой город -> 400."""
    response = api_client.post(
        reverse("weather-api"),
        {"city": ""},
        format="json"
    )
    assert response.status_code == 400
    assert "error" in response.data


@pytest.mark.django_db
def test_weather_api_real_city(api_client):
    """Тест на существующий город -> 200."""
    response = api_client.post(
        reverse("weather-api"),
        {"city": "Moscow"},
        format="json"
    )
    assert response.status_code == 200
    assert "current_weather" in response.data


@pytest.mark.django_db
def test_weather_api_invalid_city(api_client):
    """Тест на неправильный город -> 404."""
    response = api_client.post(
        reverse("weather-api"),
        {"city": "InvalidCity12345"},
        format="json"
    )
    assert response.status_code == 404
    assert "error" in response.data
