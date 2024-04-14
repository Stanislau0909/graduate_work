import requests
import conftest

class Authorization:

    def check_authorization(self, payload: dict):
        url = "https://api.qa.azkts.ru/auth/realms/azkts/protocol/openid-connect/token"
        self.response = requests.post(url, data=payload)
        self.response_json = self.response.json()
        print("status_code:", self.response.status_code)

    def check_status_is_200ok(self):
        assert self.response.status_code == 200, f"Expected status code 200, but got {self.response.status_code}"

    def check_status_is_401_unauthorized(self):
        assert self.response.status_code == 401, f"Expected status code 401, but got {self.response.status_code}"









