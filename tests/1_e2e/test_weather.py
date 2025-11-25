import pytest, re
from playwright.sync_api import Page, expect
import test_data.expected_result as expected_result

def test_weather_list(page: Page, page_url, weather_locator, common_locator):
    """
    날씨 목록에서 현재 날씨가 정상 노출되고 있는지 확인합니다.

    :param page: Page object
    :type page: Page
    :param page_url: 테스트할 대상의 페이지 URL
    :type page_url: dict[str, str]
    :param weather_locator: weather 관련 페이지의 각 엘리먼트 로케이터
    :type weather_locator: dict[str, Callable[..., Locator]]
    :param common_locator: 공통 엘리먼트 로케이터
    :type common_locator: dict[str, Callable[..., Locator]]
    """
    page.goto(page_url["weather"])

    weather_icon = weather_locator["weather_list"](page)[0]
    weather_icon.hover()
    current_place = weather_icon.inner_text()

    layer_tooltip = common_locator["layer_tooltip"](page)
    current_weather = layer_tooltip.inner_text()

    print(f"{current_place}: {current_weather}")

    assert current_weather in expected_result.weather_list
    
    weather_icon.click()
    expect(page).to_have_url(page_url["weather_detail"])


def test_spoiler_filter(page: Page, page_url, weather_locator):
    """
    날씨 목록 페이지 접근 시 스포일러 지역의 블러 처리가 되어 있는지,
    스위치를 off하면 지역명의 블러 처리가 사라지는지 테스트합니다.
    
    :param page: Page object
    :type page: Page
    :param page_url: 테스트할 대상의 페이지 URL
    :type page_url: dict[str, str]
    :param weather_locator: weather 관련 페이지의 각 엘리먼트 로케이터
    :type weather_locator: dict[str, Callable[..., Locator]]
    """
    page.goto(page_url["weather"])

    place_elpis = weather_locator["spoiler_elpis"](page)
    expect(place_elpis).to_have_css("filter", "blur(5px)")

    toggle_switch = weather_locator["toggle_switch"](page)
    toggle_switch.click()
    expect(toggle_switch).not_to_be_checked()
    expect(place_elpis).not_to_have_css("filter", "blur(5px)")