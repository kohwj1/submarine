import re
from playwright.sync_api import Page, Locator
# import test_data.urls as urls

def btn_tooltip(page:Page) -> Locator:
    return page.locator(selector="#btn-tooltip")

def layer_tooltip(page:Page) -> Locator:
    return page.get_by_role("tooltip")

def footer(page:Page) -> Locator:
    return page.locator(selector="body > footer")

def err_heading1(page: Page) -> Locator:
    return page.get_by_role("heading", level=1, name="The Aetherial Sea")

def err_btn_return(page:Page) -> Locator:
    return page.get_by_role("link", name="Return to The source")

PAGE_LOCATORS = {
    "btn_tooltip": btn_tooltip,
    "layer_tooltip": layer_tooltip,
    "footer": footer,
    "err_heading1":err_heading1,
    "err_btn_return":err_btn_return
}