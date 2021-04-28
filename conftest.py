import os
import time

import allure
import docker
import pytest
import requests
from docker.errors import NotFound

from api.request import send_request


def pytest_addoption(parser):
    default_port = 4000
    default_host = '0.0.0.0'
    default_path = './app/tester.so'
    parser.addoption('--app_port', action='store', default=default_port, help=f'By default: {default_port}')
    parser.addoption('--app_host', action='store', default=default_host, help=f'By default: {default_host}')
    parser.addoption('--app_bin_path', action='store', default=default_path, help=f"By default: {default_path}")


@allure.title('Start app')
@pytest.fixture(scope='class', autouse=True)
def start_app(pytestconfig):
    app_bin_path = pytestconfig.getoption('--app_bin_path')
    port = pytestconfig.getoption('--app_port')
    host = pytestconfig.getoption('--app_host')
    app_abs_bin_path = os.path.abspath(os.path.join(os.getcwd(), app_bin_path))
    if not os.path.isfile(app_abs_bin_path):
        raise ValueError(f'Can not find bin file by path: {app_abs_bin_path}')

    client = docker.from_env()
    app_container_name = 'tester'
    remove_containers(client, app_container_name)
    app = client.containers.run(image='ubuntu:18.04',
                                volumes={
                                    app_abs_bin_path: {'bind': '/app/tester.so'}
                                },
                                command=f'/app/tester.so {host} {port}',
                                ports={4000: 4000},
                                name=app_container_name,
                                detach=True)

    os.environ['app_uri'] = f'ws://{host}:{port}'
    wait_while_app_ready()
    yield
    app_logs = app.logs()
    print(app_logs)
    allure.attach(app_logs, name='app logs', attachment_type=allure.attachment_type.TEXT)
    app.remove(force=True)


def wait_while_app_ready(timeout=10):
    max_time = time.time() + timeout
    while time.time() < max_time:
        try:
            send_request(os.getenv('app_uri'), {'id': 'health_check'})
            return
        except ConnectionRefusedError:
            print(f'App not ready yet...Try again')
            time.sleep(1)

    raise TimeoutError(f"App does not ready within {timeout} sec")


def remove_containers(client, container_name):
    try:
        container = client.containers.get(container_name)
        container.stop()
        container.remove(force=True)
    except (NotFound, requests.exceptions.ChunkedEncodingError):
        print(f'Container {container_name} already removed')
