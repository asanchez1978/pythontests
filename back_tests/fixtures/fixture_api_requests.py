import pytest
from back_tests.framework.request_class import (
    BACKEND_REQUEST_API,
)


@pytest.fixture(scope="session", autouse=True)
def backend_request_api():
    """
    Return the backend_request_api Class instance
    """
    return BACKEND_REQUEST_API
