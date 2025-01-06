import pytest
from src.uin_service import UINService


@pytest.fixture
def uin_service():
    return UINService(
        base_url="https://example.com/api", api_key="test_api_key"
    )


def test_get_or_create_uin(uin_service, mocker):
    mock_response = {
        "code": 0,
        "message": "Success",
        "data": {"uin": "123456"},
    }
    mocker.patch(
        "src.base.requests.request",
        return_value=mocker.Mock(ok=True, json=lambda: mock_response),
    )

    response = uin_service.get_or_create_uin(
        {
            "externalId": "123",
            "firstname": "John",
            "lastname": "Doe",
            "dateOfBirth": "2000-01-01",
            "birthCertificateId": "BC123",
        }
    )

    assert response["data"]["uin"] == "123456"
