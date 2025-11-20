import re
from playwright.sync_api import Page, Locator
# import test_data.urls as urls

def reward_filter(page: Page) -> Locator:
    return page.get_by_role("switch")

def table_first_row(page:Page) -> Locator:
    return page.locator(selector="#submarine-tbody > tr:nth-child(1) > td:nth-child(4)")

def btn_display_calculator(page:Page) -> Locator:
    return page.get_by_label("calulator-display")

def btn_close_calculator(page:Page) -> Locator:
    return page.get_by_label("calulator-close")

def btn_area_6g(page:Page) -> Locator:
    return page.locator('label[for="6g"]')

def btn_area_6h(page:Page) -> Locator:
    return page.locator('label[for="6h"]')

def btn_request_calculator(page:Page) -> Locator:
    return page.get_by_role("button", name="계산하기")

def calculate_result(page:Page) -> Locator:
    return page.locator(selector="#estimate-time > div > ul > li:nth-child(1)")

PAGE_LOCATORS = {
    "reward_filter": reward_filter,
    "table_first_row": table_first_row,
    "btn_display_calculator": btn_display_calculator,
    "btn_close_calculator": btn_close_calculator,
    "btn_request_calculator": btn_request_calculator,
    "btn_area_6g": btn_area_6g,
    "btn_area_6h": btn_area_6h,
    "calculate_result":calculate_result
}