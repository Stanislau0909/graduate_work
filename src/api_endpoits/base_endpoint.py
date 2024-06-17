class BaseEndpoints:
    response = None
    response_json = None

    def check_status_is_200ok(self, response):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    def check_status_is_201created(self, response):
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    def check_status_is_204_No_Content(self, response):
        assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"

    def check_status_is_400_Bad_request(self, response):
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    def check_status_is_403_Forbidden(self, response):
        assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"

    def check_status_is_409_Conflict(self, response):
        assert response.status_code == 409, f"Expected status code 409, but got {response.status_code}"

    def check_status_is_422_Unprocessable_Entity(self, response):
        assert response.status_code == 422, f"Expected status code 422, but got {response.status_code}"
