from playwright.sync_api import Page, Locator
# import test_data.urls as urls

def heading1(page: Page) -> Locator:
    return page.get_by_role("heading", level=1, name="The Aetherial Sea")

def btn_return(page:Page) -> Locator:
    return page.get_by_role("link", name="Return to The source")

PAGE_LOCATORS = {
    "heading1": heading1,
    "btn_return": btn_return,
}