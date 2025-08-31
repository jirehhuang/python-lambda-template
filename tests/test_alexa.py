"""Test Alexa skill backend and utility functions."""

import pytest

from lambda_function import lambda_handler
from lambda_function.alexa import _text_output


@pytest.fixture(name="launch_intent_payload", scope="module")
def fixture_launch_intent_payload():
    """Return default Alexa Start Session test event JSON."""
    return {
        "version": "1.0",
        "session": {
            "new": True,
            "sessionId": "amzn1.echo-api.session.123456789012",
            "application": {"applicationId": "amzn1.ask.skill.987654321"},
            "user": {"userId": "amzn1.ask.account.testUser"},
            "attributes": {},
        },
        "context": {
            "AudioPlayer": {"playerActivity": "IDLE"},
            "System": {
                "application": {"applicationId": "amzn1.ask.skill.987654321"},
                "user": {"userId": "amzn1.ask.account.testUser"},
                "device": {"supportedInterfaces": {"AudioPlayer": {}}},
            },
        },
        "request": {
            "type": "LaunchRequest",
            "requestId": "amzn1.echo-api.request.1234",
            "timestamp": "2016-10-27T18:21:44Z",
            "locale": "en-US",
        },
    }


def test_launch_intent(launch_intent_payload):
    """Test that invoking the LaunchRequest returns the expected response."""
    response = lambda_handler(launch_intent_payload, None)
    assert (
        _text_output(group="speak", key="launch")
        in response["response"]["outputSpeech"]["ssml"]
    )
