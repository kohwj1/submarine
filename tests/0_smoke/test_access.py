import pytest, re
from playwright.sync_api import Page, expect
import test_data.expected_result as expected_result

def test_index(page: Page, page_url):
    response = page.request.get(page_url["index"])
    assert response.ok

def test_submarine_redirect(page: Page, page_url):
    response = page.request.get(page_url["submarine"])
    #리다이렉트 로직으로 정상 페이지로 이동시켜 주는 경우, 실제 응답은 302 --> 200 순으로 수행되므로 최종적으로 200인지 여부를 검증
    assert response.ok

def test_submarine_nan(page: Page, page_url):
    response = page.request.get(page_url["submarine_nan"])
    assert response.ok

def test_submarine_invalid_param(page: Page, page_url):
    response = page.request.get(page_url["submarine_invalid_range"])
    assert not response.ok

def test_submarine_valid_param(page: Page, page_url):
    response = page.request.get(page_url["submarine_r6"])
    assert response.ok

def test_navigate_api(page: Page, page_url):
    response = page.request.post(
        url=page_url["api_navigate"],
        data={"navigate_path":["6g","6h"]}
    )
    assert response.ok
    assert response.json().get("path") == expected_result.optimized_route

def test_submarine_rewards(page: Page, page_url):
    response = page.request.get(page_url["rewards"])
    assert response.ok

def test_weather(page: Page, page_url):
    response = page.request.get(page_url["weather"])
    assert response.ok

def test_weather_detail_param_missing(page: Page, page_url):
    response = page.request.get(page_url["weather_detail_missing"])
    assert not response.ok

def test_weather_detail_nan(page: Page, page_url):
    response = page.request.get(page_url["weather_detail_nan"])
    assert not response.ok

def test_weather_detail_invalid_param(page: Page, page_url):
    response = page.request.get(page_url["weather_detail_invalid_range"])
    assert not response.ok

@pytest.mark.skipif(True, reason="EorzeaEnv does not support Dawntrail ko Placename...")
def test_rainbow(page: Page, page_url):
    response = page.request.get(page_url["rainbow"])
    assert response.ok
    
def test_convert(page: Page, page_url):
    response = page.request.get(page_url["convert"])
    assert response.ok