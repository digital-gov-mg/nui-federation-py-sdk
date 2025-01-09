from src.features.uin import UIN


class NuiFederation:
    def __init__(
        self, base_url: str, api_key: str, client_id: str, client_secret: str
    ):
        self.uin = UIN(
            base_url=base_url,
            api_key=api_key,
            client_id=client_id,
            client_secret=client_secret,
        )
