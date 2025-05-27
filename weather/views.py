from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import get_city_coordinates, fetch_weather


def home_view(request):
    return render(request, 'weather/index.html')


class WeatherView(APIView):
    def post(self, request):
        city = request.data.get("city", "").strip()
        if not city:
            return Response({"error": "Введите название города"}, status=400)

        coords = get_city_coordinates(city)
        if not coords:
            return Response({"error": "Город не найден"}, status=404)

        weather_data = fetch_weather(coords["lat"], coords["lon"])
        weather_data["city"] = coords["name"]
        return Response(weather_data)
