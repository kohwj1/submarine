import pytest, re, time
from playwright.sync_api import Page, expect
import test_data.expected_result as expected_result

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page, page_url):
    page.goto(page_url["index"])    
    yield

def test_menu_all(page: Page, page_url, index_locator):
    btn_all = index_locator["btn_all"](page)
    link_address = [page_url["submarine_r6"], page_url["weather"], page_url["convert"]]

    for i in range(len(btn_all)):
        page.goto(page_url["index"])
        element = btn_all[i]
        element.click()
        expect(page).to_have_url(link_address[i])

def test_guardian(page: Page, index_locator):
    text_guardian = index_locator["text_guardian"](page)
    assert text_guardian.inner_text()[:-1] in expected_result.guardian

def test_clock(page: Page, index_locator):

    time.sleep(2)
    before_clock = index_locator["text_clock"](page).inner_text()
    print(before_clock)

    time.sleep(3)
    
    print(index_locator["text_clock"](page).inner_text())
    
    expect(index_locator["text_clock"](page)).not_to_have_text(before_clock)



