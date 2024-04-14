import requests
import pytest
import json
from src.api_endpoits.authorization import Authorization
from tests.test_data.data_dicts_4_api.data_authorization import DataAuthorization


class TestAuthorization:

    def setup_method(self):
        self.auth = Authorization()
        self.data = DataAuthorization()

    def test_valid_auth(self):

        self.auth.check_authorization(payload=self.data.data_for_login_admin())
        self.auth.check_status_is_200ok()

    def test_invalid_auth(self):

        self.auth.check_authorization(payload=self.data.invalid_data_for_login())
        self.auth.check_status_is_401_unauthorized()































