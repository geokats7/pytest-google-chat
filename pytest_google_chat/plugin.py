# -*- coding: utf-8 -*-

import pytest
from pytest_google_chat.post_to_google_chat import post_to_google_chat
from pytest_google_chat.config_manager import ConfigManager


class TestResult:
    failed: int
    passed: int
    skipped: int
    error: int
    xfailed: int
    xpassed: int


def pytest_addoption(parser):
    group = parser.getgroup('google-chat')
    group.addoption(
        '--google-chat',
        action='store_true',
        dest='google_chat',
        help='Send test results to Google Chat'
    )
    group.addoption(
        '--gc-webhook',
        action='store',
        dest='gc_webhook',
        default=None,
        help='Set the google chat channel webhook.'
    )
    group.addoption(
        '--report-link',
        action='store',
        dest='report_link',
        default=None,
        help='This link will be included in the report message'
    )
    group.addoption(
        '--report-title',
        action='store',
        dest='report_title',
        default=None,
        help='Set the title for the report message'
    )
    group.addoption(
        '--report-subtitle',
        action='store',
        dest='report_subtitle',
        default=None,
        help='Set the subtitle for the report message'
    )
    group.addoption(
        '--gc-fail-image',
        action='store',
        dest='gc_fail_image',
        default=None,
        help='Set an image (url) for a failed test run.'
    )
    group.addoption(
        '--gc-success-image',
        action='store',
        dest='gc_success_image',
        default=None,
        help='Set an image (url) for a successful test run.'
    )
    group.addoption(
        '--gc-config',
        action='store',
        default='google-chat.cfg',
        help='Set the config file path for google-chat.'
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    yield
    # special check for pytest-xdist plugin, cause we do not want to send report for each worker.
    if hasattr(terminalreporter.config, 'workerinput'):
        return
    test_result = TestResult()
    test_result.failed = len(terminalreporter.stats.get('failed', []))
    test_result.passed = len(terminalreporter.stats.get('passed', []))
    test_result.skipped = len(terminalreporter.stats.get('skipped', []))
    test_result.error = len(terminalreporter.stats.get('error', []))
    test_result.xfailed = len(terminalreporter.stats.get("xfailed", []))
    test_result.xpassed = len(terminalreporter.stats.get("xpassed", []))
    if config.option.google_chat:
        cfg_file_path = config.getoption('--gc-config')
        config_manager = ConfigManager(cfg_file_path, config)
        post_to_google_chat(test_result, config_manager, exitstatus)
