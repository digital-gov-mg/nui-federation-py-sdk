from src.request import Request


class UIN(Request):
    def get_or_create_uin(self, citizen_datas: list[dict]):
        return self.request(endpoint="/uins", method="PUT", data=citizen_datas)

    def revoke_uin(self, uin):
        return self.request(endpoint=f"/uins/{uin}/revoke", method="DELETE")

    def generate_uin_batch(self, count):
        params = {"count": count}
        return self.request(
            endpoint="/uins/batch", method="POST", params=params
        )
