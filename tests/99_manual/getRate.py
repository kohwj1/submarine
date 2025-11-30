from EorzeaEnv import EorzeaLang, EorzeaTime, EorzeaWeather, EorzeaPlaceName, EorzeaRainbow, errors

def get_weather_by_place_name(place_name, step):
    try:
        result = EorzeaWeather.forecast(EorzeaPlaceName(place_name, strict=False), EorzeaTime.weather_period(step=step), lang=EorzeaLang.KO)
    except errors.WeatherRateDataError:
        result = '날씨 계산에 실패하였습니다.'
    except errors.InvalidEorzeaPlaceName:
        result = '-'
    
    return result


if __name__ == '__main__':
    import sys
    try:
        count = int(sys.argv[1])
        print(get_weather_by_place_name("초승달 섬 남부", count))
    except IndexError:
        sys.stdout('Forecast count required')
    except TypeError:
        sys.stdout('Forecast count input must be integer')