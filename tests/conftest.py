import os

import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_app.settings")


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
