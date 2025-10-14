from datetime import datetime
from EorzeaEnv import EorzeaLang, EorzeaTime, EorzeaWeather, EorzeaPlaceName, EorzeaRainbow, errors
from data.map_data import weather_map

def get_weather_by_place_name(place_name, step):
    try:
        result = EorzeaWeather.forecast(EorzeaPlaceName(place_name, strict=False), EorzeaTime.weather_period(step=step), lang=EorzeaLang.KO)
    except errors.WeatherRateDataError:
        result = '날씨 계산에 실패하였습니다.'
    except errors.InvalidEorzeaPlaceName:
        result = '-'
    
    return result

def get_weather_by_region(area):
    target_area = weather_map.get(area)
    if not target_area:
        return None

    weather_forecast_list = [get_weather_by_place_name(place_name, 2) for place_name in target_area]
    return (target_area, weather_forecast_list)

def next_rainbow(place_name):
    place = EorzeaPlaceName(place_name, strict=False)
    the_rainbow = EorzeaRainbow(place_name=place)

    try:
        for t in EorzeaTime.weather_period(step=80):
            the_rainbow.append(t, EorzeaWeather.forecast(place, t, raw=True, lang=EorzeaLang.KO))
            if the_rainbow.is_appear:
                return datetime.fromtimestamp(t.get_unix_time()).isoformat().replace('T', ' ')
    except errors.WeatherRateDataError:
        return None
    except errors.InvalidEorzeaPlaceName:
        return None
    return None