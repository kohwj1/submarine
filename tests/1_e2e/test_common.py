import pytest, re
from playwright.sync_api import Page, expect

def test_tooltip(page: Page, page_url, common_locator):
    target_page = [page_url["submarine"], page_url["rewards"], page_url["weather"]]
    
    for target in target_page:
        page.goto(target)

        btn_tooptip = common_locator["btn_tooltip"](page)
        btn_tooptip.hover()

        layer_tooltip = common_locator["layer_tooltip"](page)
        expect(layer_tooltip).to_be_visible()