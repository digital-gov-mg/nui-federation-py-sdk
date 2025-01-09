import requests
from requests import RequestException
from .utils import fetch_access_token


class Request:
    def __init__(
        self, base_url=None, api_key=None, client_id=None, client_secret=None
    ):
        self.base_url = base_url
        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

        self.access_token = None
        self.is_already_fetching_access_token = False

        self.session = requests.Session()

        if not all(
            [self.base_url, self.api_key, self.client_id, self.client_secret]
        ):
            raise ValueError(
                "Please provide all required configurations parameters"
            )

    def request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }

        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"

        try:
            response = self.session.request(
                method, url, headers=headers, json=data, params=params
            )

            if response.status_code in {401, 403}:
                if not self.is_already_fetching_access_token:
                    self.is_already_fetching_access_token = True
                    try:
                        self.access_token = fetch_access_token(
                            base_url=self.base_url,
                            client_id=self.client_id,
                            client_secret=self.client_secret,
                        )
                    finally:
                        self.is_already_fetching_access_token = False

                    headers["Authorization"] = f"Bearer {self.access_token}"

                    response = self.session.request(
                        method, url, headers=headers, json=data, params=params
                    )

            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise ValueError(f"Request failed: {str(e)}")
