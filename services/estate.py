from instance.db_connect import cursor
from datetime import date, timedelta

def last_updated():
    cur = cursor()

    cur.execute("""SELECT regDate 
                FROM estate
                WHERE isLatest = 1
                ORDER BY regDate DESC""")
    result = cur.fetchone()
    if result:
        updated_date = str(result[0])
    else:
        updated_date = date.today().strftime("%Y%m%d")

    return f"{updated_date[0:4]}-{updated_date[4:6]}-{updated_date[6:8]}"

def get_cycle():
    EPOCH = date(2026, 6, 15)
    today = date.today()
    diff = (today - EPOCH).days % 9

    if diff < 5:
        status_class = "warning"
        next_cycle = today + timedelta(days=5 - diff)
        msg = f"추첨 참가 신청 기간입니다. 결과 발표일은 {next_cycle}입니다."
    else:
        status_class = "success"
        next_cycle = today + timedelta(days=9 - diff)
        msg = f"추첨 결과 발표 기간입니다. 다음 추첨 신청일은 {next_cycle}입니다."
    
    return {"status":status_class, "msg":msg}


def get_estate_list():
    cur = cursor()

    cur.execute("""SELECT housingArea.name AS city, estate.landType AS landType, estate.addDiv AS add1, estate.addStr AS add2, estate.price AS price
                FROM estate
                JOIN housingArea ON estate.cityId = housingArea.cityId
                WHERE isLatest = 1""")
    result = cur.fetchall()
    estate_list = [dict(row) for row in result]

    return estate_list