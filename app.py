from flask import Flask, render_template, request
from services.patchinfo import patch_info
from services.weather import get_weather_by_place_name, next_rainbow
import services.submarine as submarine
from data.map_data import weather_all
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
    region_id = request.args.get("region", 6, type=int)
    area_list = submarine.get_area(region_id)
    unlock_list = submarine.get_unlock(region_id)

    for row in area_list:
        row["unlock"] = [submarine.get_area_name(area["areaUnlock"]) for area in unlock_list if area["areaFrom"] == row["areaId"]]
        row["rewards"] = submarine.get_reward_list(row["areaId"])

    return render_template('submarine.html', patch_info=game_version, data=area_list)

@app.route('/weather')
def page_weather():
    weather_list = [[place_name, get_weather_by_place_name(place_name, 1)[0]]for place_name in weather_all]
    return render_template('weather.html', data=weather_list)

@app.route('/rainbow')
def page_rainbow():
    weather_list = [[place_name, next_rainbow(place_name)] for place_name in weather_all if next_rainbow(place_name)]
    weather_list.sort(key=lambda x:x[1])
    return render_template('rainbow.html', data=weather_list)

@app.route("/api/health")
def health_check():
	return "ok"

if __name__ == '__main__':
    app.run(debug=True)