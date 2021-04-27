import os

import allure

from api.request import send_request


@allure.suite('Add method')
class TestAddMethod:
    method = 'add'

    @allure.title('Add new user, correct')
    def test_add_new_user(self):
        request = {
            'method': self.method,
            'id': 'qwerty-123',
            'name': 'test_name',
            'surname': 'test_surname',
            'age': 18
        }
        response = send_request(os.getenv("app_uri"), request)
        assert response, 'Get empty response'
        assert response['status'], 'Status key absence in response'
        assert response['status'] == 'success', 'Get non success response'
