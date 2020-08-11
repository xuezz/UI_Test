"""
@author:xue
@time:2020/8/10
@desc:
"""
import jsonpatch

from common.logger import Logger


class Assertion:
    def __init__(self):
        self._log = Logger().get_logger()

    def assert_code(self, code, expected_code):
        try:
            assert code == expected_code
            return True
        except Exception as e:
            print(e)
            self._log.error('statusCode error, expected_code is {}, statusCode is {} '.format(code, expected_code))

    def assert_body(self, body, body_msg, excepted_msg):
        try:
            assert excepted_msg == body[body_msg]
            return True
        except Exception as e:
            print(e)
            self._log.error('Response body msg != excepted msg ,body msg :{} ,excepted msg:{}'.format(body[body_msg], excepted_msg))

    def assert_in_text(self, body, excepted_msg):
        try:
            assert excepted_msg in body
            return True
        except Exception as e:
            print(e)
            self._log.error('The response data is not contained :{}'.format(excepted_msg))

    def assert_json(self, body, dst_json):
        patch = jsonpatch.JsonPatch.from_diff(body, dst_json)
        try:
            assert len(patch.to_string()) == 2
            return True
        except Exception as e:
            print(e)
            self._log.error(patch.to_string())


if __name__ == '__main__':
    Assertion().assert_code(2023, 204)
    dict1 = {
        "code": 2001,
        "msg": "成功!",
        "data": {
            "city": "南京",
            "aqi": None,
            "forecast": [
                {
                    "date": "21日星期一"
                }
            ]
        }
    }
    dict2 = {
        "code": 2099,
        "msg": "成功!",
        "data": {

            "aqi": None,
            "forecast": [
                {
                    "date": "21日星期一"
                }
            ]
        }
    }
    Assertion().assert_json(dict1, dict2)
