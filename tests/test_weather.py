import pytest
from services.weather import get_weather_by_place_name

def test_weather():
    expected_results = []

    assert get_weather_by_place_name('툴라이욜라') == expected_results