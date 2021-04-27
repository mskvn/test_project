import json

import allure
import websocket


@allure.step('Send request')
def send_request(uri, payload):
    request = json.dumps(payload)
    print(request)
    allure.attach(request, name='request', attachment_type=allure.attachment_type.JSON)

    ws = websocket.create_connection(uri)
    ws.send(request)
    response = ws.recv()
    ws.close()

    print(response)
    allure.attach(response, name='response', attachment_type=allure.attachment_type.JSON)

    return json.loads(response)
