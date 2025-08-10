"""Test Lambda function handler module."""

from lambda_function import lambda_function


def test_lambda_handler() -> None:
    """Test that lambda_handler returns correct response."""
    response = lambda_function.lambda_handler({}, None)
    assert response["statusCode"] == 200
    assert "Hello" in response["body"]
