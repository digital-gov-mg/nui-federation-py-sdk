from src.features.uin import UIN

__version__ = "0.1.0"
__author__ = "UGD"


class NuiFederation:
    def __init__(self, base_url: str, api_key: str):
        self.uin = UIN(base_url=base_url, api_key=api_key)

    def main(self):
        print(f"Version: {__version__}")
