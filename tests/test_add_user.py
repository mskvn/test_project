import os

import allure

from api.request import send_request
from checks import checks


@allure.suite('Add user')
class TestAddUser:

    @allure.title('Add new user, correct')
    def test_add_new_user(self):
        with allure.step('Add user'):
            request = {
                'method': 'add',
                'id': 'qwerty-200',
                'name': 'test_new_user',
                'surname': 'test_new_user',
                'age': 18,
                'phone': '200'
            }
            response = send_request(os.getenv("app_uri"), request)

        checks.check_id_correct(response, request['id'])
        checks.check_response_success(response)
        checks.check_user_added(request['phone'], request['name'], request['surname'], request['age'])

    @allure.title('Add already existed user')
    def test_add_new_user__already_existed(self):
        phone = '201'
        with allure.step(f'Add user with phone {phone}'):
            request = {
                'method': 'add',
                'id': 'qwerty-201',
                'name': 'test_name',
                'surname': 'test_surname',
                'age': 18,
                'phone': phone
            }
            send_request(os.getenv("app_uri"), request)
        with allure.step(f'Add user with phone {phone} again'):
            response = send_request(os.getenv("app_uri"), request)

        checks.check_response_failure(response)

    @allure.title('Add user user without phone')
    def test_add_user_without_phone(self):
        with allure.step('Add user without phone'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-202',
                'name': 'name_without_phone',
                'surname': 'name_without_phone',
                'age': 18,
            }
            response = send_request(os.getenv("app_uri"), add_request)
        checks.check_response_failure(response)
        with allure.step(f"Select user by name {add_request['name']}"):
            select_request = {
                'id': 'qwerty-203',
                'method': 'select',
                'name': add_request['name']
            }
            response = send_request(os.getenv("app_uri"), select_request)

        checks.check_users_count(response, 0)

    @allure.title('Add user user without age')
    def test_add_user_without_age(self):
        with allure.step('Add user without age'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-204',
                'name': 'name_without_age',
                'surname': 'name_without_age',
                'phone': '202',
            }
            response = send_request(os.getenv("app_uri"), add_request)
        checks.check_response_failure(response)
        with allure.step(f"Select user by phone {add_request['phone']}"):
            select_request = {
                'id': 'qwerty-205',
                'method': 'select',
                'phone': add_request['phone']
            }
            response = send_request(os.getenv("app_uri"), select_request)

        checks.check_users_absence(response)

    @allure.title('Add user user without name')
    def test_add_user_without_name(self):
        with allure.step('Add user without name'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-205',
                'surname': 'name_without_name',
                'phone': '203',
            }
            response = send_request(os.getenv("app_uri"), add_request)
        checks.check_response_failure(response)
        with allure.step(f"Select user by phone {add_request['phone']}"):
            select_request = {
                'id': 'qwerty-206',
                'method': 'select',
                'phone': add_request['phone']
            }
            response = send_request(os.getenv("app_uri"), select_request)

        checks.check_users_absence(response)
