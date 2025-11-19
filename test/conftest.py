import pytest
from playwright.sync_api import expect
from test_data.urls import ROUTER
import test_data.locator.loc_submarine as submarine
import test_data.locator.loc_error as error
import time, requests, dotenv, os

expect.set_options(timeout=10_000)

def pytest_sessionstart(session):
    session.start_time = time.time()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "device_scale_factor": 1.0
    }

@pytest.fixture(scope="session")
def page_url():
    return ROUTER

@pytest.fixture(scope="session")
def submarine_locator():
    return submarine.PAGE_LOCATORS

@pytest.fixture(scope="session")
def error_locator():
    return error.PAGE_LOCATORS

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    dotenv.load_dotenv()
    slack = os.getenv('SLACK')
    discord = os.getenv('DISCORD')

    passed = terminalreporter.stats.get('passed', [])
    failed = terminalreporter.stats.get('failed', [])
    skipped = terminalreporter.stats.get('skipped', [])

    start_time = getattr(terminalreporter._session, "start_time", None)

    if start_time:
        duration = time.time() - start_time
    else:
        duration = 0.00

    summary = (
        f"✅ Passed: {len(passed)}\n"
        f"❌ Failed: {len(failed)}\n"
        f"⚠️ Skipped: {len(skipped)}\n"
        f"⏱ Duration: {duration:.2f} sec\n"
    )

    #디코용 포맷
    payload = {
        "content": f"## 테스트 수행 완료\n```{summary}```",
        "username": "Test Result"
    }

    response = requests.post(discord, json=payload)

    # 슬랙용 포맷 (현재 디코로 수신하기를 원해서 일단 주석처리 해둠)
    # payload = {
	# "blocks": [
    #             {
    #                 "type": "header",
    #                 "text": {
    #                     "type": "plain_text",
    #                     "text": "테스트 수행 완료",
    #                 }
    #             },
    #             {
    #                 "type": "divider"
    #             },
    #             {
    #                 "type": "section",
    #                 "text": {
    #                     "type": "mrkdwn",
    #                     "text": f"```{summary}```"
    #                 }
    #             }
    #         ]
    #     }

    # response = requests.post(slack, json=payload)

    # print(response)