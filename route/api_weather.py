from flask import Blueprint, jsonify, request
from services.weather import get_weather_by_place_name, next_rainbow

api_weather = Blueprint('api_weather', __name__, url_prefix='/api/weather')

@api_weather.route("/place")
def get_place_weather():
	place_id = request.args.get('id', type=int)
	forecase_step = request.args.get('step', type=int)

	if type(place_id) != int or type(forecase_step) != int:
		return jsonify({'error':'Invalid input'}), 400 

	return jsonify({'error':'Service under construction'}), 500

@api_weather.route("/rainbow")
def rainbow():
	return jsonify({'error':'Service under construction'}), 500