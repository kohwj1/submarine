from flask import Flask, render_template, request, redirect
from services.patchinfo import patch_info
import services.weather as weather
import services.submarine as submarine
from route.api_submarine import api_submarine
from route.api_weather import api_weather
from collections import defaultdict

app = Flask(__name__)
app.register_blueprint(api_submarine)
app.register_blueprint(api_weather)

@app.route('/')
def index():
    now = weather.now_phase()
    return render_template('index.html', data=now)

@app.route('/submarine')
def page_submarine():
    game_version = patch_info.get('version','-')
    region_id = request.args.get("region", type=int)

    if not region_id:
        return redirect('/submarine?region=6')
    
    area_list = submarine.get_area(region_id)

    if not area_list:
        return render_template('error.html'), 404

    unlock_list = submarine.get_unlock(region_id)

    for row in area_list:
        row["unlock"] = [submarine.get_area_name(area["areaUnlock"]) for area in unlock_list if area["areaFrom"] == row["areaId"]]
        row["rewards"] = submarine.get_reward_list(row["areaId"])

    return render_template('submarine.html', patch_info=game_version, data=area_list)

@app.route('/submarine-rewards')
def page_rewards():
    item_data = submarine.get_all_rewards()
    grouped_data = defaultdict(lambda: defaultdict(list))
    
    for item in item_data:
        key = (item['itemName'], item['id'])
        region_id = item['regionId']
        
        if region_id not in grouped_data[key]:
            grouped_data[key][region_id] = {
                'region_name': item['regionName'],
                'area_name': []
            }
        
        grouped_data[key][region_id]['area_name'].append(item['areaName'])

    reward_list = []

    for (itemName, item_id), regions_data in grouped_data.items():
        map_list = []
        
        for region_id, data in regions_data.items():
            map_list.append({
                'region_id': region_id,
                'region_name': data['region_name'],
                'area_name': data['area_name']
            })
        
        reward_list.append({'name': itemName, 'id': item_id, 'map': map_list})

    return render_template('rewards.html', data=reward_list, datav2=item_data)

@app.route('/weather')
def page_weather():
    weather_v2 = weather.get_current_weather_list()
    return render_template('weather.html', data=weather_v2)

@app.route('/weather/detail')
def page_weather_detail():
    weather_step = 10
    place_id = request.args.get("id", type=int)
    place_name_set = weather.get_place_name(place_id)
    
    if not place_name_set:
        return render_template('error.html'), 404
    
    place_name_ko = place_name_set.get('name_ko')
    place_name_en = place_name_set.get('name_en')
    forecast_list = weather.get_weather_by_place_name(place_name_ko, weather_step)
    lt_time_list = weather.generate_weather_period('lt', weather_step)
    et_time_list = weather.generate_weather_period('et', weather_step)
    weather_forecast = []

    for i in range(weather_step):
        weather_forecast.append({'time':{'lt':lt_time_list[i], 'et':et_time_list[i]}, 'weather':forecast_list[i]})

    data_info = {
        'id':place_id,
        'name_ko':place_name_ko,
        'name_en':place_name_en,
        'forecast_msg': weather.combine_weather_msg(place_name_ko, forecast_list[0], forecast_list[1], forecast_list[2], forecast_list[3]),
        'weather_forecast': weather_forecast,
        'next_rainbow': weather.next_rainbow(place_name_ko)
    }

    return render_template('weather_detail.html', data=data_info, unsundered=weather.unsundered, norvrandt=weather.norvrandt)

@app.route('/rainbow')
def page_rainbow():
    rainbow_data = weather.get_current_rainbow_list()
    grouped_data = defaultdict(list)
    
    for item in rainbow_data:
        time_key = item['time']
        place_value = {'id':item['id'], 'place':item['place']}
        grouped_data[time_key].append(place_value)

    rainbow_list = [{'time': time, 'place': places} for time, places in grouped_data.items()]

    return render_template('rainbow.html', data=rainbow_list)

@app.route('/convert')
def page_convert():
    return render_template('convert.html')


@app.route("/api/health")
def health_check():
	return "ok"

if __name__ == '__main__':
    app.run(debug=True)