# import pytest, re
# from playwright.sync_api import Page, expect
# import test_data.expected_result.exp_submarine as expected_result

# @pytest.fixture(scope="function", autouse=True)
# def before_each_after_each():
#     print("yield 이전 부분은 scope 전에 수행하는 영역입니다")
    
#     yield
    
#     print("yield 이후 부분은 scope 후에 수행하는 영역입니다")

# def test_function_starts_with_test_underline(page: Page):
#     """
#     여기에 테스트 함수 설명 입력
#     """
#     pass