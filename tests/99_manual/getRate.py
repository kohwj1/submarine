from EorzeaEnv import EorzeaLang, EorzeaTime, EorzeaWeather, EorzeaPlaceName, EorzeaRainbow, errors

def get_weather_by_place_name(place_name, step):
    try:
        result = EorzeaWeather.forecast(EorzeaPlaceName(place_name, strict=False), EorzeaTime.weather_period(step=step), lang=EorzeaLang.KO)
    except errors.WeatherRateDataError:
        result = '날씨 계산에 실패하였습니다.'
    except errors.InvalidEorzeaPlaceName:
        result = '-'
    
    return result


print(get_weather_by_place_name("저지 라노시아", 100))