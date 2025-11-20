import pytest, re
from playwright.sync_api import Page, expect
import test_data.expected_result.exp_submarine as expected_result

# @pytest.fixture(scope="function", autouse=True)
# def before_each_after_each():
#     print("yield 이전 부분은 scope 전에 수행하는 영역입니다")
    
#     yield
    
#     print("yield 이후 부분은 scope 후에 수행하는 영역입니다")

def test_index(page: Page, page_url):
    response = page.request.get(page_url["index"])
    expect(response).to_be_ok()

def test_submarine_redirect(page: Page, page_url):
    response = page.request.get(page_url["submarine"])
    expect(response).to_be_ok() #실제 응답은 302 --> 200 순으로 수행되므로 최종적으로 200인지 여부를 검증

def test_submarine_nan(page: Page, page_url):
    response = page.request.get(page_url["submarine_nan"])
    expect(response).to_be_ok() #실제 응답은 302 --> 200 순으로 수행되므로 최종적으로 200인지 여부를 검증

def test_submarine_invalid_param(page: Page, page_url):
    response = page.request.get(page_url["submarine_invalid_range"])
    expect(response).not_to_be_ok()

def test_submarine_valid_param(page: Page, page_url):
    response = page.request.get(page_url["submarine_r6"])
    expect(response).to_be_ok()

def test_navigate_api(page: Page, page_url):
    response = page.request.post(
        url=page_url["api_navigate"],
        data={"navigate_path":["6g","6h"]}
    )
    assert response.ok
    assert response.json().get("path") == expected_result.optimized_route

def test_submarine_rewards(page: Page, page_url):
    response = page.request.get(page_url["rewards"])
    expect(response).to_be_ok()

def test_weather(page: Page, page_url):
    response = page.request.get(page_url["weather"])
    expect(response).to_be_ok()

def test_weather_detail_param_missing(page: Page, page_url):
    response = page.request.get(page_url["weather_detail_missing"])
    expect(response).not_to_be_ok()

def test_weather_detail_nan(page: Page, page_url):
    response = page.request.get(page_url["weather_detail_nan"])
    expect(response).not_to_be_ok()

def test_weather_detail_invalid_param(page: Page, page_url):
    response = page.request.get(page_url["weather_detail_invalid_range"])
    expect(response).not_to_be_ok()

@pytest.mark.skipif(True, reason="EorzeaEnv does not support Dawntrail ko Placename...")
def test_rainbow(page: Page, page_url):
    response = page.request.get(page_url["rainbow"])
    expect(response).to_be_ok()
    
def test_convert(page: Page, page_url):
    response = page.request.get(page_url["convert"])
    expect(response).to_be_ok()