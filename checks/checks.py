import os

import allure

from api.request import send_request


@allure.step('Check that response succeeded')
def check_response_success(response):
    assert response, 'Get empty response'
    assert response['status'], 'Status key absence in response'
    assert response['status'] == 'success', 'Get non success response'


@allure.step('Check that user added')
def check_user_added(phone, name, surname, age):
    request = {
        'id': 'id',
        'method': 'select',
        'phone': phone
    }
    response = send_request(os.getenv("app_uri"), request)
    check_uniq_user_selected(response, name, surname, age)


@allure.step('Check that selected only one and correct user')
def check_uniq_user_selected(response, name, surname, age):
    assert 'users' in response, 'Users are empty'
    users = response['users']
    assert len(users) == 1, f'Expect only one user, but find {len(users)}'
    user = users[0]
    # TODO: use soft asserts
    assert user['name'] == name, f"Expect that user name is {name}, but actual is {user['name']}"
    assert user['surname'] == surname, f"Expect that user surname is {surname}, but actual is {user['surname']}"
    assert user['age'] == age, f"Expect that user age is {name}, but actual is {user['age']}"
