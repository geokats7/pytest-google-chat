import requests
import logging
import pytest


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def post_to_google_chat(test_result, config_manager, exitstatus):
    gc_webhook = config_manager.getoption("gc-webhook", "gc_webhook", "GOOGLE-CHAT")
    if gc_webhook is None:
        pytest.exit("\nERROR: Google Chat Webhook not configured")
    gc_webhook = gc_webhook.strip('"').strip("'")
    report_link = config_manager.getoption("report-link", "report_link", "GOOGLE-CHAT")

    report_title = config_manager.getoption("report-title", "report_title", "GOOGLE-CHAT")
    report_subtitle = config_manager.getoption("report-subtitle", "report_subtitle", "GOOGLE-CHAT")

    # Set context of message depending on the exit status
    if int(exitstatus) != 0:
        image = config_manager.getoption("gc-fail-image", "gc_fail_image", "GOOGLE-CHAT")
        status_color = "#FF0000"
        status = "FAILED"

    else:
        image = config_manager.getoption("gc-success-image", "gc_success_image", "GOOGLE-CHAT")
        status_color = "#2E8B57"
        status = "PASSED"

    passed_tests = f"Passed: {test_result.passed}" if test_result.passed else ""
    failed_tests = f"\nFailed: {test_result.failed}" if test_result.failed else ""
    skipped_tests = f"\nSkipped: {test_result.skipped}" if test_result.skipped else ""
    error_tests = f"\nError: {test_result.error}" if test_result.error else ""
    xfailed_tests = f"\nXFailed: {test_result.xfailed}" if test_result.xfailed else ""
    xpassed_tests = f"\nXPassed: {test_result.xpassed}" if test_result.xpassed else ""

    report_message = passed_tests + failed_tests + skipped_tests + error_tests + xfailed_tests + xpassed_tests

    # Arrange your data in pre-defined format. See an example here:
    # https://developers.google.com/hangouts/chat/reference/message-formats/cards
    main_message = {
        "cards": [
            {
                "header": {
                    "title": report_title,
                    "subtitle": report_subtitle,
                    "imageUrl": image,
                },
                "sections": [
                    {"widgets": [{"keyValue": {"topLabel": "Status", "content": f"<font color={status_color}>" + status + "</font>"}}]},
                    {"widgets": [{"textParagraph": {"text": report_message}}]} if report_message is not None else None,
                    {
                        "widgets": [
                            {
                                "buttons": [
                                    {
                                        "textButton": {
                                            "text": "CHECK THE REPORT HERE",
                                            "onClick": {"openLink": {"url": report_link}},
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                    if report_link is not None else None,
                ],
            }
        ]
    }

    response = requests.post(url=gc_webhook, json=main_message, headers={"Content-type": "application/json"})
    if response.status_code == 200:
        logger.info("\n Successfully posted pytest report on google chat")
    else:
        logger.info(f"\n Something went wrong. Unable to post pytest report on google chat. Response: {response}")
