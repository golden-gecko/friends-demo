import json

from http import HTTPStatus

from encoding import Encoder
from logger import get_logger


logger = get_logger()


def response(code: int, message: str = '', data: [dict, list] = None) -> tuple:
    body = {
        'meta': {
            'code': code
        }
    }

    if message:
        body['meta']['message'] = message

    if data is not None:
        body['response'] = data

    body = json.dumps(body, sort_keys=True, cls=Encoder)
    body = json.loads(body)

    return body, code


def bad_request(message: str = 'Bad Request', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.BAD_REQUEST, message=message, data=data)


def not_found(message: str = 'Not Found', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.NOT_FOUND, message=message, data=data)


def conflict(message: str = 'Conflict', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.CONFLICT, message=message, data=data)


def success(message: str = 'Success', data: [dict, list] = None) -> tuple:
    return response(code=HTTPStatus.OK, message=message, data=data)
