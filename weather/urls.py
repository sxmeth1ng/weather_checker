from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import WeatherView, home_view


urlpatterns = [
    path("", home_view, name="home"),
    path("api/weather/", WeatherView.as_view(), name="weather-api"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
