import json

from requests import Response


class Checking():

    """Method for checking status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        print("Correct, status code = " + str(response.status_code))


    """Method for checking mandatory fields in response"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields exist!")


    """Method for checking values of mandatory fields"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name, " is correct!")