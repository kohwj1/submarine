import re
from playwright.sync_api import Page, Locator

def toggle_switch(page: Page) -> Locator:
    return page.get_by_role("switch")

def weather_list(page:Page) -> Locator:
    return page.locator(selector=".placename").all()

def spoiler_elpis(page:Page) -> Locator:
    return page.get_by_text('엘피스')

PAGE_LOCATORS = {
    "toggle_switch":toggle_switch,
    "weather_list": weather_list,
    "spoiler_elpis": spoiler_elpis,
}