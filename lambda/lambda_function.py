"""Lambda function handler module."""

from typing import Any
from .utils import format_greeting


# pylint: disable=unused-argument
def lambda_handler(event: Any, context: Any) -> Any:
    """
    Sample AWS Lambda handler for testing deployment.
    """
    return {
        "statusCode": 200,
        "body": format_greeting("python-lambda-template"),
    }
