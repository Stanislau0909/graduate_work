

class BaseEndpoints:

    response = None
    response_json = None

    def check_status_is_200ok(self):
        assert self.response.status_code == 200, f"Expected status code 200, but got {self.response.status_code}"

    def check_status_is_201created(self):
        assert self.response.status_code == 201, f"Expected status code 201, but got {self.response.status_code}"

    def check_status_is_204_No_Content(self):
        assert self.response.status_code == 204, f"Expected status code 204, but got {self.response.status_code}"

    def check_status_is_422_Unprocessable_Entity(self):
        assert self.response.status_code == 422, f"Expected status code 422, but got {self.response.status_code}"




