from flask import Blueprint, jsonify, request
import itertools, json
from collections import deque
import services.submarine as submarine

api_submarine = Blueprint("api_submarine", __name__, url_prefix="/api/submarine")


@api_submarine.route("/navigate", methods=["POST"])
def get_best_route():
	submited = request.get_json()
	if not submited:
		return jsonify({'error':'Unknown'}), 400

	selected_path = submited.get("navigate_path")
	if not selected_path:
		return jsonify({'error':'None of areas selected'}), 400

	path_cases = list(itertools.permutations(selected_path, len(selected_path)))
	route_list = []

	for path in path_cases:
		path_order = ["home"]
		path_order.extend(list(path))
		navigate_time = []

		for i in range(len(path_order) - 1):
			try:
				navigate_time.append(submarine.get_moving_time(path_order[i], path_order[i+1]))
			except TypeError:
				return jsonify({'error':'Invalid navigation path'}), 400
		
		path_order = path_order[1:]
		explore_time = [submarine.get_explore_time(area) for area in path_order]
		route_list.append({"path":" > ".join(path_order).upper(), "time":sum(explore_time) + sum(navigate_time)})
	
	route_list.sort(key=lambda item: item["time"])

	return jsonify(route_list[0])