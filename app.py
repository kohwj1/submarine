from flask import Flask, jsonify, render_template
from services.patchinfo import patch_info
from services.weather import get_weather_by_place_name, next_rainbow
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
    game_version = patch_info.get('client_version','-')
    return render_template('submarine.html', patch_info=game_version)

@app.route('/weather')
def page_weather():
    weather_list = [[place_name, get_weather_by_place_name(place_name, 1)[0]]for place_name in weather_all]
    return render_template('weather.html', data=weather_list)

@app.route('/rainbow')
def page_rainbow():
    weather_list = [[place_name, next_rainbow(place_name)] for place_name in weather_all if next_rainbow(place_name)]
    weather_list.sort(key=lambda x:x[1])
    return render_template('rainbow.html', data=weather_list)

if __name__ == '__main__':
    app.run(debug=True)