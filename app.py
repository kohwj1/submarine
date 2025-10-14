from flask import Flask, jsonify, render_template
from services.weather import get_weather_by_place_name, next_rainbow
from data.map_data import weather_all
from apiRoute import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submarine')
def page_submarine():
    return render_template('submarine.html')

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