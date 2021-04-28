import os

import allure

from api.request import send_request
from checks import checks


@allure.suite('Update user')
class TestUpdateUser:

    @allure.title('Update name for existed user')
    def test_update_existed_user__name(self):
        phone = '400'
        old_name = 'name_update_existed_user__old'
        new_name = 'name_update_existed_user__new'

        with allure.step(f'Add user with phone {phone}'):
            request = {
                'method': 'add',
                'id': 'qwerty-400',
                'name': old_name,
                'surname': 'surname_update_existed_user',
                'age': 18,
                'phone': phone
            }
            send_request(os.getenv("app_uri"), request)
        with allure.step(f"Update user with phone {phone}. Set new name '{new_name}'"):
            request.update(
                {
                    'method': 'update',
                    'name': new_name
                }
            )
            response = send_request(os.getenv("app_uri"), request)
        checks.check_id_correct(response, request['id'])
        checks.check_response_success(response)
        with allure.step(f'Select user by phone {phone}'):
            select_request = {
                'id': 'qwerty-401',
                'method': 'select',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_uniq_user_selected(response, name=new_name, surname=request['surname'], age=request['age'])

    @allure.title('Update surname for existed user')
    def test_update_existed_user__surname(self):
        phone = '401'
        old_surname = 'surname_update_existed_user__old'
        new_surname = 'surname_update_existed_user__new'

        with allure.step(f'Add user with phone {phone}'):
            request = {
                'method': 'add',
                'id': 'qwerty-402',
                'surname': old_surname,
                'name': 'name_update_existed_user',
                'age': 18,
                'phone': phone
            }
            send_request(os.getenv("app_uri"), request)
        with allure.step(f"Update user with phone {phone}. Set new surname '{new_surname}'"):
            request.update(
                {
                    'method': 'update',
                    'surname': new_surname
                }
            )
            response = send_request(os.getenv("app_uri"), request)
        checks.check_response_success(response)
        with allure.step(f'Select user by phone {phone}'):
            select_request = {
                'id': 'qwerty-403',
                'method': 'select',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_uniq_user_selected(response, name=request['name'], surname=new_surname, age=request['age'])

    @allure.title('Update age for existed user')
    def test_update_existed_user__age(self):
        phone = '402'
        old_age = 18
        new_age = 99

        with allure.step(f'Add user with phone {phone}'):
            request = {
                'method': 'add',
                'id': 'qwerty-404',
                'surname': 'surname_update_existed_user',
                'name': 'name_update_existed_user',
                'age': old_age,
                'phone': phone
            }
            send_request(os.getenv("app_uri"), request)
        with allure.step(f"Update user with phone {phone}. Set new age '{new_age}'"):
            request.update(
                {
                    'method': 'update',
                    'age': new_age
                }
            )
            response = send_request(os.getenv("app_uri"), request)

        checks.check_response_success(response)
        with allure.step(f'Select user by phone {phone}'):
            select_request = {
                'id': 'qwerty-405',
                'method': 'select',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_uniq_user_selected(response, name=request['name'], surname=request['surname'], age=new_age)

    @allure.title('Update all fields for existed user')
    def test_update_existed_user__all_fields(self):
        phone = '403'

        with allure.step(f'Add user with phone {phone}'):
            request = {
                'method': 'add',
                'id': 'qwerty-406',
                'surname': 'surname_update_existed_user',
                'name': 'name_update_existed_user',
                'age': 18,
                'phone': phone
            }
            send_request(os.getenv("app_uri"), request)
        with allure.step(f"Update user with phone {phone}. Set new values for all fields'"):
            request.update(
                {
                    'method': 'update',
                    'age': 99,
                    'name': 'new_name',
                    'surname': 'new_surname'
                }
            )
            response = send_request(os.getenv("app_uri"), request)

        checks.check_response_success(response)
        with allure.step(f'Select user by phone {phone}'):
            select_request = {
                'id': 'qwerty-407',
                'method': 'select',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_uniq_user_selected(response, name=request['name'], surname=request['surname'], age=request['age'])

    @allure.title('Update not existed user')
    def test_update_not_existed_user(self):
        phone = '410'
        with allure.step(f'Update user with phone {phone}'):
            request = {
                'method': 'update',
                'id': 'qwerty-401',
                'name': 'name_update_not_existed_user',
                'surname': 'surname_update_not_existed_user',
                'age': 18,
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), request)

        checks.check_response_failure(response)
