BASE_URL = "http://localhost:5000"
ROUTER = {
    "index": f"{BASE_URL}/",
    "submarine": f"{BASE_URL}/submarine",
    "submarine_nan": f"{BASE_URL}/submarine?region=aaa",
    "submarine_invalid_range": f"{BASE_URL}/submarine?region=999",
    "submarine_r6": f"{BASE_URL}/submarine?region=6",
    "submarine_r5": f"{BASE_URL}/submarine?region=5",
    "rewards": f"{BASE_URL}/submarine-rewards",
    "weather": f"{BASE_URL}/weather",
    "weather_detail": f"{BASE_URL}/weather/detail?id=0",
    "weather_detail_elpis": f"{BASE_URL}/weather/detail?id=70",
    "weather_detail_missing": f"{BASE_URL}/weather/detail",
    "weather_detail_nan": f"{BASE_URL}/weather/detail?id=aaa",
    "weather_detail_invalid_range": f"{BASE_URL}/weather/detail?id=999",
    "rainbow": f"{BASE_URL}/rainbow",
    "convert": f"{BASE_URL}/convert",
    "api_navigate": f"{BASE_URL}/api/submarine/navigate",
}