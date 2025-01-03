from .base import Base


class UINService(Base):
    def get_or_create_uin(self, citizen_data):
        """
        Get or create a UIN for a citizen.
        """
        endpoint = "/uins"
        return self.request("PUT", endpoint, data=citizen_data)

    def revoke_uin(self, uin):
        """
        Revoke a UIN.
        """
        endpoint = f"/uins/{uin}/revoke"
        return self.request("DELETE", endpoint)

    def generate_uin_batch(self, count):
        """
        Generate a batch of UINs.
        """
        endpoint = "/uins/batch"
        params = {"count": count}
        return self.request("POST", endpoint, params=params)
