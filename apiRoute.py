from flask import Blueprint, jsonify
from services.weather import get_weather_by_place_name, next_rainbow
from data.map_data import weather_all

api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/health")
def health_check():
	return "ok"

@api.route("/rainbow")
def rainbow():
	weather_list = [{'place_name':place_name, 'time':next_rainbow(place_name)} for place_name in weather_all if next_rainbow(place_name)]
	return weather_list