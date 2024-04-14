

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