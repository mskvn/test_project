import json
import os

import allure

from api.request import send_request


@allure.step('Check that response succeeded')
def check_response_success(response):
    assert response, 'Get empty response'
    assert response['status'], 'Status key absence in response'
    assert response['status'] == 'success', 'Get non success response'


@allure.step('Check that response failured')
def check_response_failure(response):
    assert response, 'Get empty response'
    assert response['status'], 'Status key absence in response'
    assert response['status'] == 'failure', 'Get success response'


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
    assert user['age'] == age, f"Expect that user age is {age}, but actual is {user['age']}"


@allure.step('Check that reason not empty')
def check_reason_not_empty(response):
    assert 'reason' in response, 'Reason absence in response'


@allure.step('Check users count')
def check_users_count(response, count):
    assert 'users' in response, 'Users are empty'
    users = response['users']
    assert len(users) == count, f'Expect {count} users, but found {len(users)}'


@allure.step('Check that user in response')
def check_user_in_response(users, name, surname, age, phone):
    for user in users:
        if user['phone'] == phone and user['name'] == name and user['surname'] == surname and user['age'] == age:
            return
    raise AssertionError(f"Cant find user with name='{name}', surname='{surname}', age={age}, phone={phone} "
                         f"in users:\n{json.dumps(users, indent=2)}")


@allure.step('Check users absence')
def check_users_absence(response):
    assert 'users' not in response, 'Expect that users absense in response'


@allure.title('Check id correct')
def check_id_correct(response, expected_id):
    assert 'id' in response, 'id key absence in response'
    assert response['id'] == expected_id, f"Expect thar response with id {expected_id}, but actual is {response['id']}"
