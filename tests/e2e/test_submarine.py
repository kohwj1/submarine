import pytest, re
from playwright.sync_api import Page, expect
import test_data.expected_result.exp_submarine as expected_result

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each():
    print("yield 이전 부분은 scope 전에 수행하는 영역입니다")
    
    yield
    
    print("yield 이후 부분은 scope 후에 수행하는 영역입니다")

def test_redirection(page: Page, page_url, error_locator):
    """
    잠수함 페이지 리다이렉션 기능을 테스트하는 함수입니다.

    파라미터가 없거나 숫자가 아닌 경우 최신 해역으로 리다이렉트되며, 비정상 범위의 숫자인 경우 에러 페이지가 노출되는지 확인합니다.

    e.g.)
    - region 파라미터 없음: region=6으로 리다이렉트
    - region=aaaa로 요청: region=6으로 리다이렉트
    - region=999로 요청: 에러 화면 노출
    """
    page.goto(page_url["submarine"])
    expect(page).to_have_url(page_url["submarine_r6"])

    page.goto(page_url["submarine_nan"])
    expect(page).to_have_url(page_url["submarine_r6"])

    page.goto(page_url["submarine_invalid_range"])
    expect(page).to_have_title("The Aetherial Sea")

    error_title = error_locator["heading1"](page)
    error_btn = error_locator["btn_return"](page)

    expect(error_title).to_be_in_viewport()
    error_btn.click()

    expect(page).to_have_url(page_url["index"])


def test_reward_filter(page: Page, page_url, submarine_locator):
    """
    잠수함 보상 필터 동작을 확인합니다.
    
    필터가 기본값 상태(on)인 경우 최고등급 보상만 보이는지, 필터를 클릭해서 off가 되면 모든 보상이 보이는지 검증합니다.
    """
    page.goto(page_url["submarine_r6"])

    table_first_row = submarine_locator["table_first_row"](page)
    expect(table_first_row).to_have_text(expected_result.reward_tier1, use_inner_text=True) #textContent의 경우 visible하지 않아도 텍스트가 읽히는 문제가 있어 inner_text로 비교

    reward_filter = submarine_locator["reward_filter"](page)
    reward_filter.click()
    expect(reward_filter).not_to_be_checked()
    expect(table_first_row).to_have_text(expected_result.reward_all)

def test_calculator(page: Page, page_url, submarine_locator):
    """
    최적 탐사 경로 계산기의 UI 펼치기/접기 및 기본 계산 기능 동작을 확인합니다.

    지정된 목적지 (창망의 바다 남쪽 02, 갈고리발톱 섬)를 선택했을 때, 기대결과와 동일하게 계산되는지 검증합니다.
    """
    page.goto(page_url["submarine_r6"])

    btn_display_calculator = submarine_locator["btn_display_calculator"](page)
    btn_display_calculator.click()

    btn_close_calculator = submarine_locator["btn_close_calculator"](page)
    expect(btn_close_calculator).to_be_visible()

    btn_close_calculator.click()
    expect(btn_close_calculator).not_to_be_visible()

    btn_display_calculator.click()

    btn_area_6g = submarine_locator["btn_area_6g"](page)
    btn_area_6h = submarine_locator["btn_area_6h"](page)

    btn_area_6g.click()
    btn_area_6h.click()

    btn_request_calculator = submarine_locator["btn_request_calculator"](page)
    btn_request_calculator.click()

    calculate_result = submarine_locator["calculate_result"](page)
    expect(calculate_result).to_contain_text(f"최적 경로: {expected_result.optimized_route}")

def test_navigate_api(page: Page, page_url):
    response = page.request.post(
        url=page_url["api_navigate"],
        data={"navigate_path":["6g","6h"]}
    )
    assert response.ok
    assert response.json().get("path") == expected_result.optimized_route