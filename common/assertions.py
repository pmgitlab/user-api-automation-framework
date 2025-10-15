def assert_response(response, expected_code=200):
    assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"
    body = response.json()
    assert body['code'] == expected_code, f"Expected body code {expected_code}, got {body['code']}"
