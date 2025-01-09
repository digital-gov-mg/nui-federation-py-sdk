import requests
from requests import RequestException


def validate_citizen_data(citizen_data):
    required_keys = [
        "externalId",
        "firstname",
        "lastname",
        "dateOfBirth",
        "birthCertificateId",
    ]
    for key in required_keys:
        if key not in citizen_data:
            raise ValueError(f"Missing required field: {key}")


def fetch_access_token(base_url, client_id, client_secret):
    try:
        response = requests.post(
            f"{base_url}/systems/token",
            json={
                "clientId": client_id,
                "clientSecret": client_secret,
            },
            headers={"Content-Type": "application/json"},
        )

        response.raise_for_status()
        return response.json().get("access_token")
    except RequestException as e:
        raise ValueError(f"Failed to fetch access token: {str(e)}")
