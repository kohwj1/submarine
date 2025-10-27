from data.db_connect import cursor

def get_area_name(areaId):
    cur = cursor()

    cur.execute("""SELECT name 
                FROM area
                WHERE areaId = ?""", (areaId, ))
    result = cur.fetchone()
    area_name = result[0]

    return area_name

def get_area(region):
    cur = cursor()

    cur.execute("""SELECT * 
                FROM area
                WHERE regionId = ?""", (region, ))
    result = cur.fetchall()
    area_list = [dict(row) for row in result]

    return area_list

def get_unlock(region):
    cur = cursor()

    cur.execute("""SELECT * 
                FROM unlock
                WHERE areaFrom LIKE ?""", (f"{region}%", ))
    result = cur.fetchall()
    area_list = [dict(row) for row in result]

    return area_list

def get_reward_list(areaId):
    cur = cursor()

    cur.execute("""SELECT rewards.tier, items.name, items.itemId
                FROM items
                JOIN rewards ON rewards.itemId = items.itemId
                JOIN area ON rewards.areaId = area.areaId
                WHERE area.areaId = ?""", (areaId, ))
    result = cur.fetchall()
    reward_list = [dict(row) for row in result]

    list_tier0 = [{'itemId':row['itemId'], 'name':row['name']} for row in reward_list if row.get('tier') == 0]
    list_tier1 = [{'itemId':row['itemId'], 'name':row['name']} for row in reward_list if row.get('tier') == 1]
    list_tier2 = [{'itemId':row['itemId'], 'name':row['name']} for row in reward_list if row.get('tier') == 2]

    return {'tier0':list_tier0, 'tier1':list_tier1, 'tier2':list_tier2}

def get_moving_time(areaFrom, areaTo):
    cur = cursor()

    cur.execute("""SELECT time 
                FROM navigation
                WHERE areaFrom = ? AND areaTo = ?""", (areaFrom, areaTo))
    result = cur.fetchone()
    navigate_time = result[0]

    return navigate_time

def get_explore_time(areaId):
    cur = cursor()

    cur.execute("""SELECT time 
                FROM area
                WHERE areaId = ?""", (areaId, ))
    result = cur.fetchone()
    explore_time = result[0]

    return explore_time