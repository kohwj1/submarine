import pytest, re, time
from playwright.sync_api import Page, expect
import test_data.expected_result as expected_result

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page, page_url):
    page.goto(page_url["index"])    
    yield

def test_menu_all(page: Page, page_url, index_locator):
    """
    index 페이지 내의 카드 메뉴 링크 동작 확인 테스트입니다.
    
    :param page: Description
    :type page: Page
    :param page_url: Description
    :type page_url: dict[str, str]
    :param index_locator: Description
    :type index_locator: dict[str, Callable[..., Locator]]
    """
    btn_all = index_locator["btn_all"](page)
    link_address = [page_url["submarine_r6"], page_url["weather"], page_url["convert"]]

    for i in range(len(btn_all)):
        page.goto(page_url["index"])
        element = btn_all[i]
        element.click()
        expect(page).to_have_url(link_address[i])

def test_guardian(page: Page, index_locator):
    """
    index 페이지에 수호신 이름이 정상적으로 표시되었는지 확인하는 테스트입니다.
    
    :param page: Description
    :type page: Page
    :param index_locator: Description
    :type index_locator: dict[str, Callable[..., Locator]]
    """
    
    text_guardian = index_locator["text_guardian"](page)
    assert text_guardian.inner_text()[:-1] in expected_result.guardian

def test_clock(page: Page, index_locator):
    """
    index 페이지의 ET 시계가 동작하는지 확인하는 테스트입니다.
    
    :param page: Description
    :type page: Page
    :param index_locator: Description
    :type index_locator: dict[str, Callable[..., Locator]]
    """

    time.sleep(2)
    before_clock = index_locator["text_clock"](page).inner_text()
    print(before_clock)

    time.sleep(3)
    
    print(index_locator["text_clock"](page).inner_text())
    
    expect(index_locator["text_clock"](page)).not_to_have_text(before_clock)



