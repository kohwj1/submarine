import pytest
from playwright.sync_api import expect
from test_data.urls import ROUTER
import test_data.locator.loc_submarine as submarine
import test_data.locator.loc_common as common
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
def common_locator():
    return common.PAGE_LOCATORS

@pytest.fixture(scope="session")
def submarine_locator():
    return submarine.PAGE_LOCATORS

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    dotenv.load_dotenv()

    slack = os.getenv('SLACK')
    discord = os.getenv('DISCORD')
    runner = os.getenv('RUNNER')
    test_scope = os.getenv('TEST_SCOPE')

    passed = terminalreporter.stats.get('passed', [])
    failed = terminalreporter.stats.get('failed', [])
    skipped = terminalreporter.stats.get('skipped', [])

    start_time = getattr(terminalreporter._session, "start_time", None)

    if start_time:
        duration = time.time() - start_time
    else:
        duration = 0.00

    def get_test_names(reports):
        return [rep.nodeid for rep in reports]
    
    def discord_embed(tc):
        return "\n".join(f"• {name[8:].split('[')[0]}" for name in tc) or "-"

    passed_test = get_test_names(passed)
    failed_test = get_test_names(failed)
    skipped_test = get_test_names(skipped)

    summary = (
        f"✅ Passed: {len(passed_test)}\n"
        f"❌ Failed: {len(failed_test)}\n"
        f"⚠️ Skipped: {len(skipped_test)}\n"
        f"⏱ Duration: {duration:.2f} sec\n"
        f"-----------------------------------\n"
        f"💻 Runner: {runner}"
    )

    block_pass = f"### ✅ {len(passed_test)} Passed\n```{discord_embed(passed_test)}```"
    block_fail = f"### ❌ {len(failed_test)} Failed\n```{discord_embed(failed_test)}```"
    block_skip = f"### ⚠️ {len(skipped_test)} Skipped\n```{discord_embed(skipped_test)}```"

    payload_discord = {
        "username": "Test Result",
        "content": (
            f"## Summary- {test_scope}\n"
            f"```{summary}```\n"
            f"## Detail\n"
            f"{block_pass}\n"
            f"{block_fail}\n"
            f"{block_skip}\n"
        )
    }

    payload_slack = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Summary"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```{summary}```"
                }
            },
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Detail"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{block_pass}"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{block_fail}"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{block_skip}"
                }
            }
        ]
    }

    response_discord = requests.post(discord, json=payload_discord)
    response_slack = requests.post(slack, json=payload_slack)

    # print(response_discord)
    # print(response_slack)