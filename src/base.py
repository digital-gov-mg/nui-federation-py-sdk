import requests


class Base:
    def __init__(self, base_url=None, api_key=None):
        self.base_url = base_url
        self.api_key = api_key

        if not self.base_url or not self.api_key:
            raise ValueError("Please provide a base URL and an API key")

    def request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }

        response = requests.request(
            method, url, headers=headers, json=data, params=params
        )

        if response.ok:
            return response.json()
        else:
            response.raise_for_status()
