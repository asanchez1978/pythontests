import pytest as pytest


@pytest.mark.request_api_tests
@pytest.mark.parametrize(
    "endpoint, user", [("/public/v2/users/", "6732586")],
)
def test_get(backend_request_api, endpoint, user):
    result = backend_request_api.get(endpoint, user)
    print(f"GET {result}")
    assert result["name"] == "Ghanaanand Chopra"


@pytest.mark.request_api_tests
@pytest.mark.parametrize(
    "endpoint, create_user", [("/public/v2/users/", {"name": "Denali Ramakrishna", "gender": "male",
                                                     "email": "Denali.ramakrishna@299ce.com", "status": "active"})],
)
def test_post(backend_request_api, endpoint, create_user):
    result = backend_request_api.post(endpoint, create_user)

    print(f"POST {result}")

    if isinstance(result, dict):
        assert result["name"] == "Denali Ramakrishna"
    else:
        assert result[0]["message"] == "has already been taken"


@pytest.mark.request_api_tests
@pytest.mark.parametrize(
    "endpoint,user_id,modify_user", [("/public/v2/users/", "6733626", {"name": "Denali Gupta", "gender": "male",
                                                                       "email": "Denali.Gupta@15ce.com",
                                                                       "status": "active"})],
)
def test_patch(backend_request_api, endpoint, user_id, modify_user):
    result = backend_request_api.patch(endpoint, user_id, modify_user)

    print(f"PATCH {result}")
    assert result["name"] == "Denali Gupta"


@pytest.mark.request_api_tests
@pytest.mark.parametrize(
    "endpoint, user", [("/public/v2/users/", "6734199")],
)
def test_delete(backend_request_api, endpoint, user):
    result = backend_request_api.delete(endpoint, user)

    print(f"DELETE {result}")
    assert result == 204
