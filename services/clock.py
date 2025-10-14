# import json
from EorzeaEnv import EorzeaTime

def get_et():
    et_now = EorzeaTime().now()
    return {"hour": et_now.hour, "minute": et_now.minute, "moon_name":et_now.moon_name, "moon_phase":et_now.moon_phase}

if __name__ == '__main__':
    print(get_et())