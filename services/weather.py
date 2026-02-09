from datetime import datetime
from EorzeaEnv import EorzeaLang, EorzeaTime, EorzeaWeather, EorzeaPlaceName, EorzeaRainbow, errors
from instance.db_connect import cursor
from instance.weather_msg import weather_msg

region_category = ["라노시아", "검은장막 숲", "다날란", "이슈가르드 주변 지역", "기라바니아", "동방 지역", "일사바드 대륙", "투랄 대륙", "노르브란트", "기타", "특수 필드"]
unsundered = ["Elpis","Heritage Found","Solution Nine","Living Memory", "Sinus Ardorum", "Phaenna", "Oizys"]
norvrandt = ["The Crystarium","Eulmore","Lakeland", "Kholusia", "Amh Araeng", "Il Mheg", "The Rak'tika Greatwood", "The Tempest"]

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

    cur.execute("""SELECT name_ko, name_en
                FROM place
                WHERE id = ?""", (placeid, ))
    result = cur.fetchone()

    if not result:
        return None

    place_name = dict(result)

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

def generate_weather_period(time_type, t):
    if time_type == 'et':
        et_hour = EorzeaTime.now().hour
        print(et_hour)

        if et_hour >=0 and et_hour < 8:
            time_list = [f"ET {i % 24}:00" for i in range(0, 0 + 8*t, 8)]
        if et_hour >=8 and et_hour < 16:
            time_list = [f"ET {i % 24}:00" for i in range(8, 8 + 8*t, 8)]
        if et_hour >=16 and et_hour < 24:
            time_list = [f"ET {i % 24}:00" for i in range(16, 16 + 8*t, 8)]
    
    else:
        time_list = [datetime.fromtimestamp(timestamp.get_unix_time()).isoformat().replace('T', ' ') for timestamp in EorzeaTime.weather_period(step=t)]
    return time_list

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

def get_current_rainbow_list():
    place_list = []

    for region in region_category:
        place_list.extend(get_places(region))

    result = [{'id':place.get('id'), 'place':place.get('name_ko'), 'time':next_rainbow(place.get('name_ko'))} for place in place_list if next_rainbow(place.get('name_ko'))]
    result.sort(key=lambda x:x['time'])

    return result

def now_phase():
    return {'guardian':EorzeaTime.now().guardian, 'moon_phase':EorzeaTime.now().moon_phase}