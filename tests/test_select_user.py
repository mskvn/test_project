import os

import allure

from api.request import send_request
from checks.checks import check_response_success, check_uniq_user_selected


@allure.suite('Select method')
class TestSelectUser:
    method = 'select'

    @allure.title('Select existed user')
    def test_select_user(self):
        with allure.step('Add user'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-123',
                'name': 'test_name',
                'surname': 'test_surname',
                'age': 18,
                'phone': '113'
            }
            send_request(os.getenv("app_uri"), add_request)
        with allure.step('Select user'):
            select_request = {
                'id': 'id',
                'method': 'select',
                'phone': add_request['phone']
            }
        response = send_request(os.getenv("app_uri"), select_request)
        check_response_success(response)
        check_uniq_user_selected(response, add_request['name'], add_request['surname'], add_request['age'])
