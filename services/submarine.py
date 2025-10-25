from data.db_connect import cursor

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