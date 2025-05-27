import pytest
from weather.utils import get_city_coordinates, fetch_weather


def test_real_geocoding():
    """Тест проверяющий корректность данных в ответе API."""
    result = get_city_coordinates("Moscow")
    assert result is not None
    assert isinstance(result["lat"], float)
    assert isinstance(result["lon"], float)


@pytest.mark.slow
def test_real_weather_fetch():
    """Тест проверяющий работоспособность API."""
    result = fetch_weather(55.7558, 37.6176)
    assert "current_weather" in result
