from flask import Blueprint, jsonify, request
import services.submarine as submarine

api_submarine = Blueprint("api_submarine", __name__, url_prefix="/api/submarine")

@api_submarine.route("/health")
def health_check():
	return "ok"

@api_submarine.route("/area")
def get_area_list():
	region_id = request.args.get("id", type=int)
	area_list = submarine.get_area(region_id)
	unlock_list = submarine.get_unlock(region_id)

	for row in area_list:
		row["unlock"] = [submarine.get_area_name(area["areaUnlock"]) for area in unlock_list if area["areaFrom"] == row["areaId"]]
		row["rewards"] = submarine.get_reward_list(row["areaId"])

	return jsonify({'data': area_list})

@api_submarine.route("/navigate")
def get_navigate_list():
	region_id = request.args.get('id', type=int)
	area_list = submarine.get_area(region_id)
	return jsonify({'data': area_list})