import pytest, re
from playwright.sync_api import Page, expect
import test_data.expected_result as expected_result

def test_rewards_filter(page: Page, page_url, submarine_locator):
    """
    잠수함 보상 페이지의 아이템 검색 기능을 테스트합니다.

    input에 아이템명의 일부를 입력한 후, 필터링된 첫 번째 아이템명이 검색어를 포함하고 있는지 확인합니다.
    """
    page.goto(page_url["rewards"])

    rewards_input = submarine_locator["rewards_input"](page)
    filter_keyword = expected_result.filter_keyword

    rewards_input.fill(filter_keyword)

    rewards_filtered_list = submarine_locator["rewards_filtered_list"](page)

    for tr in rewards_filtered_list:
        expect(tr).to_contain_text(filter_keyword, use_inner_text=True)