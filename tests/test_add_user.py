import os

import allure

from api.request import send_request
from checks.checks import check_response_success, check_user_added


@allure.suite('Add user')
class TestAddUser:

    @allure.title('Add new user, correct')
    def test_add_new_user(self):
        with allure.step('Add user'):
            request = {
                'method': 'add',
                'id': 'qwerty-123',
                'name': 'test_name',
                'surname': 'test_surname',
                'age': 18,
                'phone': '200'
            }
            response = send_request(os.getenv("app_uri"), request)

        check_response_success(response)
        check_user_added(request['phone'], request['name'], request['surname'], request['age'])
