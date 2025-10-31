from flask import Flask, render_template, request, redirect
from services.patchinfo import patch_info
from services.weather import get_weather_by_place_name, get_place_name, get_current_weather_list, next_rainbow, combine_weather_msg, generate_weather_period, time_convert
import services.submarine as submarine
from data.map_data import weather_map
from route.api_submarine import api_submarine
from route.api_weather import api_weather

app = Flask(__name__)
app.register_blueprint(api_submarine)
app.register_blueprint(api_weather)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submarine')
def page_submarine():
    game_version = patch_info.get('version','-')
    region_id = request.args.get("region", type=int)

    if not region_id:
        return redirect('/submarine?region=6')

    area_list = submarine.get_area(region_id)
    unlock_list = submarine.get_unlock(region_id)

    for row in area_list:
        row["unlock"] = [submarine.get_area_name(area["areaUnlock"]) for area in unlock_list if area["areaFrom"] == row["areaId"]]
        row["rewards"] = submarine.get_reward_list(row["areaId"])

    return render_template('submarine.html', patch_info=game_version, data=area_list)

@app.route('/weather')
def page_weather():
    weather_v2 = get_current_weather_list()
    return render_template('weather.html', data=weather_v2)

@app.route('/weather/detail')
def page_weather_detail():
    weather_step = 10
    place_id = request.args.get("id", type=int)
    place_name_set = get_place_name(place_id)
    place_name_ko = place_name_set.get('name_ko')
    place_name_en = place_name_set.get('name_en')
    forecast_list = get_weather_by_place_name(place_name_ko, weather_step)
    lt_time_list = generate_weather_period('lt', weather_step)
    et_time_list = generate_weather_period('et', weather_step)
    weather_forecast = []

    for i in range(weather_step):
        weather_forecast.append({'time':{'lt':lt_time_list[i], 'et':et_time_list[i]}, 'weather':forecast_list[i]})

    data_info = {
        'id':place_id,
        'name_ko':place_name_ko,
        'name_en':place_name_en,
        'forecast_msg':combine_weather_msg(place_name_ko, forecast_list[0], forecast_list[1], forecast_list[2], forecast_list[3]),
        'weather_forecast': weather_forecast,
        'next_rainbow': next_rainbow(place_name_ko)
    }

    return render_template('weather_detail.html', data=data_info)

@app.route('/rainbow')
def page_rainbow():
    weather_list = [[place.get('name'), next_rainbow(place.get('name'))] for place in weather_map if next_rainbow(place.get('name'))]
    weather_list.sort(key=lambda x:x[1])
    return render_template('rainbow.html', data=weather_list)

@app.route("/api/health")
def health_check():
	return "ok"

if __name__ == '__main__':
    app.run(debug=True)