from flask import Blueprint, jsonify, request
from services.submarine import get_area
from data.map_data import weather_all

api_submarine = Blueprint('api_submarine', __name__, url_prefix='/api/submarine')

@api_submarine.route("/health")
def health_check():
	return "ok"

@api_submarine.route("/area")
def get_area_list():
	region_id = request.args.get('id', type=int)
	area_list = get_area(region_id)
	# print(area_list)
	return jsonify({'data': area_list})