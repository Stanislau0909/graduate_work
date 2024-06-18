import requests
import conftest
from src.api_endpoits.base_endpoint import BaseEndpoints as Base


class Authorization(Base):

    def check_authorization(self, payload: dict):
        url = "https://api.qa.azkts.ru/auth/realms/azkts/protocol/openid-connect/token"
        response = requests.post(url, data=payload)
        response_json = response.json()
        print("status_code:", response.status_code)
        return response
