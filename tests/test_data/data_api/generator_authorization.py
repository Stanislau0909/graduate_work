class DataAuthorization:

    def data_for_login_admin(self):
        payload = {
            "username": "dpkappadmin",
            "password": "524598",
            "grant_type": "password",
            "client_secret": "ebNLe1qZ5GfiAUJp74HUMLmkwRnTcucG",
            "client_id": "azk"
        }
        return payload

    def invalid_data_for_login(self):
        payload = {
            "username": "dpkappadmin",
            "password": "5245989",
            "grant_type": "password",
            "client_secret": "ebNLe1qZ5GfiAUJp74HUMLmkwRnTcucG",
            "client_id": "azk"
        }
        return payload


class GeneratorLogins:

    def __init__(self):
        self.result = {}
        self.build()

    def set_user_name(self, username="dpkappadmin"):
        self.result['username'] = username
        return self

    def set_password(self, password="524598"):
        self.result['password'] = password
        return self

    def set_grant_type(self, grant_type="password"):
        self.result['grant_type'] = grant_type
        return self

    def set_client_secret(self, client_secret="ebNLe1qZ5GfiAUJp74HUMLmkwRnTcucG"):
        self.result['client_secret'] = client_secret
        return self

    def set_client_id(self, client_id="azk"):
        self.result['client_id'] = client_id
        return self

    def reset(self):
        self.set_user_name()
        self.set_password()
        self.set_grant_type()
        self.set_client_secret()
        self.set_client_id()
        return self

    def build(self):
        return self.result
