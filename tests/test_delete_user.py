import os

import allure

from api.request import send_request
from checks import checks


@allure.suite('Delete user')
class TestDeleteUser:

    # TODO: check that retrun same id

    @allure.title('Delete existed user')
    def test_delete_existed_user(self):
        phone = '300'
        with allure.step(f'Add user with phone {phone}'):
            request = {
                'method': 'add',
                'id': 'qwerty-300',
                'name': 'test_delete_existed_user',
                'surname': 'test_delete_existed_user',
                'age': 18,
                'phone': phone
            }
            send_request(os.getenv("app_uri"), request)
        with allure.step(f'Delete user with phone {phone}'):
            request = {
                'method': 'delete',
                'id': 'qwerty-301',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), request)
        checks.check_id_correct(response, request['id'])
        checks.check_response_success(response)
        with allure.step(f'Select user by phone {phone}'):
            select_request = {
                'id': 'qwerty-302',
                'method': 'select',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), select_request)

        checks.check_users_absence(response)

    @allure.title('Delete user without phone')
    def test_delete_user_without_phone(self):
        phone = '301'
        with allure.step(f'Add user with phone {phone}'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-303',
                'name': 'test_delete_user_without_phone',
                'surname': 'test_delete_user_without_phoner',
                'age': 18,
                'phone': phone
            }
            send_request(os.getenv("app_uri"), add_request)
        with allure.step(f'Delete user with phone {phone}'):
            delete_request = {
                'method': 'delete',
                'id': 'qwerty-304'
            }
            response = send_request(os.getenv("app_uri"), delete_request)
        checks.check_response_failure(response)
        with allure.step(f'Select user by phone {phone}'):
            select_request = {
                'id': 'qwerty-305',
                'method': 'select',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_uniq_user_selected(response, name=add_request['name'], surname=add_request['surname'],
                                        age=add_request['age'])

    @allure.title('Delete not existed user')
    def test_delete_not_existed_user(self):
        phone = '302'
        with allure.step(f'Delete user with phone {phone}'):
            request = {
                'method': 'delete',
                'id': 'qwerty-306',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), request)
        checks.check_response_failure(response)
