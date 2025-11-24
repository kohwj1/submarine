import re
from playwright.sync_api import Page, Locator

def btn_all(page:Page) -> Locator:
    return page.locator(selector="#site-menu > a").all()

def text_guardian(page:Page) -> Locator:
    return page.locator(selector="#guardian")

def text_clock(page:Page) -> Locator:
    return page.locator(selector="#timer")

PAGE_LOCATORS = {
    "btn_all": btn_all,
    "text_guardian": text_guardian,
    "text_clock": text_clock
}