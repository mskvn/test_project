import os

import allure

from api.request import send_request
from checks import checks


@allure.suite('Select user')
class TestSelectUser:

    @allure.title('Select existed user by phone, success response')
    def test_select__exist_user_by_phone__success_response(self):
        phone = '100'
        with allure.step(f'Add user with phone {phone}'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-100',
                'name': 'name__success_response',
                'surname': 'surname__success_responsee',
                'age': 18,
                'phone': phone
            }
            send_request(os.getenv("app_uri"), add_request)
        with allure.step(f'Select user by phone {phone}'):
            select_request = {
                'id': 'qwerty-101',
                'method': 'select',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_id_correct(response, select_request['id'])
        checks.check_response_success(response)

    @allure.title('Select existed user by phone, user uniq and correct')
    def test_select__exist_user_by_phone__user_uniq_correct(self):
        phone_1 = '101-1'
        phone_2 = '101-2'
        with allure.step(f'Add user with phone {phone_1}'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-100-1',
                'name': 'name__user_uniq_correct',
                'surname': 'surname__user_uniq_correct',
                'age': 18,
                'phone': phone_1
            }
            send_request(os.getenv("app_uri"), add_request)
        with allure.step(f'Add user with phone {phone_2}'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-101-2',
                'name': 'name__user_uniq_correct',
                'surname': 'surname__user_uniq_correct',
                'age': 18,
                'phone': phone_1
            }
            send_request(os.getenv("app_uri"), add_request)
        with allure.step(f'Select user by phone {phone_1}'):
            select_request = {
                'id': 'qwerty-102',
                'method': 'select',
                'phone': phone_1
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_uniq_user_selected(response, add_request['name'], add_request['surname'], add_request['age'])

    @allure.title('Select not existed user by phone')
    def test_select__not_exist_user_by_phone(self):
        phone = '102'
        with allure.step(f'Select user by phone {phone}'):
            select_request = {
                'id': 'qwerty-103',
                'method': 'select',
                'phone': phone
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_response_failure(response)
        checks.check_reason_not_empty(response)

    @allure.title('Select not existed user by name')
    def test_select__not_exist_user_by_name(self):
        name = 'name__not_exist_user_by_name'
        with allure.step(f'Select user by name {name}'):
            select_request = {
                'id': 'qwerty-104',
                'method': 'select',
                'name': name
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_response_failure(response)
        checks.check_reason_not_empty(response)

    @allure.title('Select not existed user by surname')
    def test_select__not_exist_user_by_surname(self):
        surname = 'surname__not_exist_user_by_surname'
        with allure.step(f'Select user by surname {surname}'):
            select_request = {
                'id': 'qwerty-105',
                'method': 'select',
                'surname': surname
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_response_failure(response)
        checks.check_reason_not_empty(response)

    @allure.title('Select existed user by name, user uniq and correct')
    def test_select_exist_user__one_by_name(self):
        name_1 = 'name__one_by_name_1'
        name_2 = 'name__one_by_name_2'
        with allure.step(f'Add user with name {name_1}'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-106',
                'name': name_1,
                'surname': 'surname__one_by_name',
                'age': 18,
                'phone': '103'
            }
            send_request(os.getenv("app_uri"), add_request)
        with allure.step(f'Add user with name {name_2}'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-107',
                'name': name_2,
                'surname': 'surname__one_by_name',
                'age': 18,
                'phone': '104'
            }
            send_request(os.getenv("app_uri"), add_request)
        with allure.step(f'Select user by name {name_1}'):
            select_request = {
                'id': 'qwerty-108',
                'method': 'select',
                'name': name_1
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_uniq_user_selected(response, name_1, add_request['surname'], add_request['age'])

    @allure.title('Select existed user by surname, user uniq and correct')
    def test_select_exist_user__one_by_surname(self):
        surname_1 = 'name__one_by_name_1'
        surname_2 = 'name__one_by_name_2'
        with allure.step(f'Add user with surname {surname_1}'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-109',
                'name': 'name__one_by_surname',
                'surname': surname_1,
                'age': 18,
                'phone': '105'
            }
            send_request(os.getenv("app_uri"), add_request)
        with allure.step(f'Add user with surname {surname_2}'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-110',
                'name': 'name__one_by_surname',
                'surname': surname_2,
                'age': 18,
                'phone': '106'
            }
            send_request(os.getenv("app_uri"), add_request)
        with allure.step(f'Select user by surname {surname_1}'):
            select_request = {
                'id': 'qwerty-111',
                'method': 'select',
                'surname': surname_1
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_uniq_user_selected(response, add_request['name'], surname_1, add_request['age'])

    @allure.title('Select few users by name')
    def test__select_few_users__by_name(self):
        name = 'name__few_users__by_name'
        with allure.step(f'Add user with name {name}'):
            add_request_1 = {
                'method': 'add',
                'id': 'qwerty-112',
                'name': name,
                'surname': 'surname__select_few_users__by_name_1',
                'age': 18,
                'phone': '107'
            }
            send_request(os.getenv("app_uri"), add_request_1)
        with allure.step(f'Add user with the same name {name}'):
            add_request_2 = {
                'method': 'add',
                'id': 'qwerty-113',
                'name': name,
                'surname': 'surname__select_few_users__by_name_2',
                'age': 18,
                'phone': '108'
            }
            send_request(os.getenv("app_uri"), add_request_2)
        with allure.step(f'Select user by name {name}'):
            select_request = {
                'id': 'qwerty-114',
                'method': 'select',
                'name': name
            }
            response = send_request(os.getenv("app_uri"), select_request)

        checks.check_users_count(response, 2)
        for user in [add_request_1, add_request_2]:
            checks.check_user_in_response(response['users'],
                                          age=user['age'],
                                          name=user['name'],
                                          surname=user['surname'],
                                          phone=user['phone'])

    @allure.title('SQL injection OR 1=1')
    def test_select_sql_injection(self):
        name_1 = 'name__sql_injection_1'
        with allure.step(f'Add user with name {name_1}'):
            add_request_1 = {
                'method': 'add',
                'id': 'qwerty-115',
                'name': name_1,
                'surname': 'surname__sql_injection_1',
                'age': 18,
                'phone': '109'
            }
            send_request(os.getenv("app_uri"), add_request_1)
        name_2 = 'name__sql_injection_2'
        with allure.step(f'Add user with name {name_2}'):
            add_request = {
                'method': 'add',
                'id': 'qwerty-116',
                'name': name_2,
                'surname': 'surname__sql_injection_2',
                'age': 18,
                'phone': '110'
            }
            send_request(os.getenv("app_uri"), add_request)

        with allure.step(f'Select user by name {name_1} and with SQL injection'):
            select_request = {
                'id': 'qwerty-117',
                'method': 'select',
                'name': f"{name_1}\"; OR 1=1 --"
            }
            response = send_request(os.getenv("app_uri"), select_request)

        checks.check_users_count(response, 0)

    @allure.title('Select users without parameters')
    def test_select_without_params(self):
        with allure.step(f'Select user without parameters'):
            select_request = {
                'id': 'qwerty-118',
                'method': 'select'
            }
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_response_failure(response)
        with allure.step('Check that app available'):
            response = send_request(os.getenv("app_uri"), select_request)
        checks.check_response_failure(response)