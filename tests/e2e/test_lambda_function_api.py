"""Test Lambda function end-to-end (E2E) via API."""

import pytest
import requests


@pytest.mark.e2e
def test_lambda_handler_api(api_url, api_key):
    if not api_url:
        pytest.skip("No --url provided; skipping E2E test")

    headers = {}
    if api_key:
        headers["x-api-key"] = api_key

    resp = requests.get(api_url, headers=headers, timeout=10)
    assert resp.status_code == 200, f"Unexpected response: {resp.text}"
    assert "Hello from python-lambda-template!" in resp.text
