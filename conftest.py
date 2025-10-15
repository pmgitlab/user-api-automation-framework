import pytest

@pytest.fixture(scope="session")
def base_setup():
    print("\nStarting API tests...")
    yield
    print("\nCompleted API tests.")
