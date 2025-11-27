import pytest, re
from playwright.sync_api import Page, expect

def test_error_redirection(page: Page, page_url, common_locator):
    """
    각 페이지의 에러 리다이렉션 기능을 테스트하는 함수입니다.

    파라미터가 비정상 범위의 숫자인 경우 에러 페이지가 노출되는지 확인합니다.

    e.g.) 잠수함
    - region 파라미터 없음: region=6으로 리다이렉트
    - region=aaaa로 요청: region=6으로 리다이렉트
    - region=999로 요청: 에러 화면 노출

    e.g.) 날씨
    - region 파라미터 없음: 에러 화면 노출
    - region=aaaa로 요청: 에러 화면 노출
    - region=999로 요청: 에러 화면 노출

    :param page: Page object
    :type page: Page
    :param page_url: 테스트할 대상의 페이지 URL
    :type page_url: dict[str, str]
    :param common_locator: 공통 엘리먼트 로케이터
    :type common_locator: dict[str, Callable[..., Locator]]
    """
    page.goto(page_url["submarine_invalid_range"])
    expect(page).to_have_title("The Aetherial Sea")

def test_error_page(page: Page, page_url, common_locator):
    """
    에러 페이지 기능을 테스트하는 함수입니다.
    
    :param page: Page object
    :type page: Page
    :param page_url: 테스트할 대상의 페이지 URL
    :type page_url: dict[str, str]
    :param common_locator: 공통 엘리먼트 로케이터
    :type common_locator: dict[str, Callable[..., Locator]]
    """
    page.goto(page_url["submarine_invalid_range"])

    error_title = common_locator["err_heading1"](page)
    error_btn = common_locator["err_btn_return"](page)

    expect(error_title).to_be_in_viewport()
    error_btn.click()

    expect(page).to_have_url(page_url["index"])

def test_tooltip(page: Page, page_url, common_locator):
    """
    각 페이지에서 Bootstrap을 이용하여 구현한 툴팁이 정상 노출되는지 확인하는 테스트입니다.
    
    :param page: Page object
    :type page: Page
    :param page_url: 테스트할 대상의 페이지 URL
    :type page_url: dict[str, str]
    :param common_locator: 공통 엘리먼트 로케이터
    :type common_locator: dict[str, Callable[..., Locator]]]
    """
    target_page = [page_url["submarine"], page_url["rewards"], page_url["weather"]]
    
    for target in target_page:
        page.goto(target)

        btn_tooptip = common_locator["btn_tooltip"](page)
        btn_tooptip.hover()

        layer_tooltip = common_locator["layer_tooltip"](page)
        expect(layer_tooltip).to_be_visible()