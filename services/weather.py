from datetime import datetime
from EorzeaEnv import EorzeaLang, EorzeaTime, EorzeaWeather, EorzeaPlaceName, EorzeaRainbow, errors
from data.db_connect import cursor
from data.weather_msg import weather_msg

region_category = ["라노시아", "검은장막 숲", "다날란", "이슈가르드 주변 지역", "기라바니아", "동방 지역", "일사바드 대륙", "투랄 대륙", "노르브란트", "기타", "특수 필드"]

def get_places(region):
    cur = cursor()

    cur.execute("""SELECT id, name_ko, name_en, category, isSpoiler
                FROM place
                WHERE region = ?""", (region, ))
    result = cur.fetchall()
    place_list = [dict(row) for row in result]

    return place_list

def get_weather_by_place_name(place_name, step):
    try:
        result = EorzeaWeather.forecast(EorzeaPlaceName(place_name, strict=False), EorzeaTime.weather_period(step=step), lang=EorzeaLang.KO)
    except errors.WeatherRateDataError:
        result = '날씨 계산에 실패하였습니다.'
    except errors.InvalidEorzeaPlaceName:
        result = '-'
    
    return result

def get_place_name(placeid):
    cur = cursor()

    cur.execute("""SELECT name_ko 
                FROM place
                WHERE id = ?""", (placeid, ))
    result = cur.fetchone()
    place_name = result[0]

    return place_name

def get_current_weather_list():
    result = []

    for region in region_category:
        table_row = {'region':region, 'weather_info': get_places(region)}
        place_list = table_row.get('weather_info')
                
        for place in place_list:
            place['weather'] = get_weather_by_place_name(place['name_ko'], 1)[0]

        result.append(table_row)
    
    return result

def combine_weather_msg(place_name, weather_current, weather_s1, weather_s2, weather_s3):
    if weather_s1 == weather_s2:
        msg1 = weather_msg.get(weather_s1)[3]
    else:
        msg1 = f"{weather_msg.get(weather_s1)[0]} {weather_msg.get(weather_s2)[1]}"

    return f"{place_name}의 현재 날씨는 '{weather_current}'입니다.\n이 시간 이후로 {msg1}\n내일 이 시간에는 {weather_msg.get(weather_s3)[2]}"


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


if __name__ == '__main__':
    get_weather_by_place_name('림사 로민사', 10)