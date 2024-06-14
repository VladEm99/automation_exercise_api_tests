import pytest
import requests
from requests import Response
from utils.random_data_generation import *
from utils.checking import *
from utils.api import automationexercise_api


""" - GET to all products list"""
def test_can_get_products_list():
    print("\nMethod GET to all products list")
    result_get = automationexercise_api.get_all_products_list()
    Checking.check_status_code(result_get, 200)


""" - DELETE to all products list"""
def test_can_not_delete_to_all_products_list():
    print("\nMethod DELETE to all products list")
    result_delete = automationexercise_api.delete_to_all_products_list()
    Checking.check_json_value(result_delete, 'responseCode', 405)
    Checking.check_json_value(result_delete, 'message', 'This request method is not supported.')


""" - PUT to all products list"""
def test_can_not_put_to_all_products_list():
    print("\nMethod PUT to all products list")
    result_delete = automationexercise_api.put_to_all_products_list()
    Checking.check_json_value(result_delete, 'responseCode', 405)
    Checking.check_json_value(result_delete, 'message', 'This request method is not supported.')


""" - POST to all products list"""
def test_can_not_post_to_all_pruducts_list():
    print("\nMethod POST to all products list")
    result_post = automationexercise_api.post_all_products_list()
    Checking.check_json_token(result_post, ['responseCode', 'message'])
    Checking.check_json_value(result_post, 'responseCode', 405)
    Checking.check_json_value(result_post, 'message', 'This request method is not supported.')


""" - GET to all brands list"""
def test_can_get_all_brands_list():
    print("\nMethod GET to all products list")
    result_get = automationexercise_api.get_to_all_brands_list()
    Checking.check_status_code(result_get, 200)


""" - PUT to all brands list"""
def test_can_not_put_to_all_brands_list():
    print("\nMethod PUT to all brands list")
    result_put = automationexercise_api.put_to_all_brands_list()
    Checking.check_json_token(result_put, ['responseCode', 'message'])
    Checking.check_json_value(result_put, 'responseCode', 405)
    Checking.check_json_value(result_put, 'message', 'This request method is not supported.')


""" - DELETE to all brands list"""
def test_can_not_delete_to_all_brands_list():
    print("\nMethod DELETE to all brands list")
    result_delete = automationexercise_api.delete_to_all_brands_list()
    Checking.check_json_token(result_delete, ['responseCode', 'message'])
    Checking.check_json_value(result_delete, 'responseCode', 405)
    Checking.check_json_value(result_delete, 'message', 'This request method is not supported.')


""" - POST to all brands list"""
def test_can_not_post_to_all_brands_list():
    print("\nMethod POST to all brands list")
    result_post = automationexercise_api.post_to_all_brands_list()
    Checking.check_json_token(result_post, ['responseCode', 'message'])
    Checking.check_json_value(result_post, 'responseCode', 405)
    Checking.check_json_value(result_post, 'message', 'This request method is not supported.')


""" - POST to search product"""
def test_can_search_product_with_valid_data():
    print("\nMethod POST to search product")
    result_post = automationexercise_api.post_to_search_product()
    Checking.check_json_token(result_post, ['responseCode', 'products'])
    Checking.check_status_code(result_post, 200)


""" - PUT to search product"""
def test_can_not_put_to_search_product():
    print("\nMethod PUT to search product")
    result_post = automationexercise_api.put_to_search_product()
    Checking.check_json_value(result_post, 'responseCode', 405)
    Checking.check_json_value(result_post, 'message', 'This request method is not supported.')


""" - DELETE to search product"""
def test_can_not_delete_to_search_product():
    print("\nMethod DELETE to search product")
    result_delete = automationexercise_api.delete_to_search_product()
    Checking.check_json_value(result_delete, 'responseCode', 405)
    Checking.check_json_value(result_delete, 'message', 'This request method is not supported.')


""" - GET to search product"""
def test_can_not_get_to_search_product():
    print("\nMethod GET to search product")
    result_get = automationexercise_api.get_to_search_product()
    Checking.check_json_value(result_get, 'responseCode', 405)
    Checking.check_json_value(result_get, 'message', 'This request method is not supported.')


""" - POST to search product without search_product parameter"""
def test_can_not_search_product_without_parameter():
    print("\nMethod POST to search product without search_product parameter")
    result_post = automationexercise_api.post_to_search_product_without_search_parameter()
    Checking.check_json_value(result_post, 'message', 'Bad request, search_product parameter is missing in POST request.')
    Checking.check_json_value(result_post, 'responseCode', 400)


""" - POST to search non existent product"""
def test_cant_find_non_existent_product():
    print("\nMethod POST To find non existent product")
    result_post = automationexercise_api.post_to_search_non_existent_product()
    Checking.check_json_token(result_post, ['responseCode', 'products'])
    Checking.check_json_value(result_post, 'responseCode', 200)


""" - POST To Verify Login without email parameter"""
def test_post_to_verify_login_without_email():
    print("\nMethod POST To Verify Login without email parameter")
    result_post = automationexercise_api.post_to_verify_login_without_email()
    Checking.check_json_token(result_post, ['responseCode', 'message'])
    Checking.check_json_value(result_post, 'message', 'Bad request, email or password parameter is missing in POST request.')
    Checking.check_json_value(result_post, 'responseCode', 400)


""" - POST To Verify Login without password parameter"""
def test_cant_verify_login_without_password():
    print("\nMethod POST to verify login without password parameter")
    result_post = automationexercise_api.post_to_verify_login_without_password()
    Checking.check_json_token(result_post, ['responseCode', 'message'])
    Checking.check_json_value(result_post, 'message', 'Bad request, email or password parameter is missing in POST request.')
    Checking.check_json_value(result_post, 'responseCode', 400)


""" - POST To Verify Login without password and email parameter"""
def test_cant_verify_login_without_password_and_email():
    print("\nMethod POST to verify login without password and email parameter")
    result_post = automationexercise_api.post_to_verify_login_without_password_and_email()
    Checking.check_json_token(result_post, ['responseCode', 'message'])
    Checking.check_json_value(result_post, 'message', 'Bad request, email or password parameter is missing in POST request.')
    Checking.check_json_value(result_post, 'responseCode', 400)


""" - DELETE To Verify Login"""
def test_delete_to_verify_login():
    print("\nMethod DELETE To Verify Login")
    result_delete = automationexercise_api.delete_to_verify_login()
    Checking.check_json_token(result_delete, ['responseCode', 'message'])
    Checking.check_json_value(result_delete, 'message', 'This request method is not supported.')
    Checking.check_json_value(result_delete, 'responseCode', 405)


""" - GET To Verify Login"""
def test_can_not_get_to_verify_login():
    print("\nMethod GET To Verify Login")
    result_get = automationexercise_api.get_to_verify_login()
    Checking.check_json_token(result_get, ['responseCode', 'message'])
    Checking.check_json_value(result_get, 'message', 'This request method is not supported.')
    Checking.check_json_value(result_get, 'responseCode', 405)


""" - PUT To Verify Login"""
def test_can_not_put_to_verify_login():
    print("\nMethod PUT To Verify Login")
    result_put = automationexercise_api.put_to_verify_login()
    Checking.check_json_token(result_put, ['responseCode', 'message'])
    Checking.check_json_value(result_put, 'message', 'This request method is not supported.')
    Checking.check_json_value(result_put, 'responseCode', 405)


""" - POST To Verify Login with invalid details"""
def test_post_to_verify_login_with_invalid_details():
    print("\nMethod POST To Verify Login with invalid details")
    result_post = automationexercise_api.post_to_verify_login_with_invalid_details()
    Checking.check_json_token(result_post, ['responseCode', 'message'])
    Checking.check_json_value(result_post, 'responseCode', 404)
    Checking.check_json_value(result_post, 'message', "User not found!")


"""" - POST To Verify Login with valid details"""
def test_post_to_verify_login_with_valid_details():
    print("\nMethod POST To Verify Login with valid details")
    result_post = automationexercise_api.post_to_create_new_user_and_verify_login_with_valid_details()
    Checking.check_json_token(result_post, ['responseCode', 'message'])
    Checking.check_json_value(result_post, 'responseCode', 200)
    Checking.check_json_value(result_post, 'message', "User exists!")


""" - POST To Create/Register User Account"""
def test_post_to_register_user():
    print("\nMethod POST To register user")
    result_post = automationexercise_api.post_to_register_user()
    Checking.check_json_token(result_post, ['responseCode', 'message'])
    Checking.check_json_value(result_post, 'responseCode', 201)
    Checking.check_json_value(result_post, 'message', "User created!")


""" - PUT To Create/Register User Account"""
def test_can_not_put_to_register_user():
    print("\nMethod PUT To register user")
    result_put = automationexercise_api.put_to_register_user()
    Checking.check_json_value(result_put, 'detail', "Method \"PUT\" not allowed.")

""" - DELETE To Create/Register User Account"""
def test_can_not_delete_to_register_user():
    print("\nMethod DELETE To register user")
    result_delete = automationexercise_api.delete_to_register_user()
    Checking.check_json_value(result_delete, 'detail', "Method \"DELETE\" not allowed.")


""" - GET To Create/Register User Account"""
def test_can_not_get_to_register_user():
    print("\nMethod GET To register user")
    result_get = automationexercise_api.get_to_register_user()
    Checking.check_json_value(result_get, 'detail', "Method \"GET\" not allowed.")


""" - PUT To Update User Account"""
def test_can_create_and_update_user_account_data():
    print("\nMethod PUT To create new user and update data of created user")
    result_put = automationexercise_api.put_to_create_and_update_user_account_data()
    Checking.check_json_token(result_put, ['responseCode', 'message'])
    Checking.check_json_value(result_put, 'responseCode', 200)
    Checking.check_json_value(result_put, 'message', "User updated!")

""" - GET To Update User Account"""
def test_can_not_get_to_create_and_update_user_account_data():
    print("\nMethod GET To create new user and update data of created user")
    result_get = automationexercise_api.get_to_create_and_update_user_account_data()
    Checking.check_json_value(result_get, 'detail', "Method \"GET\" not allowed.")


""" - DELETE To Update User Account"""
def test_can_not_delete_to_create_and_update_user_account_data():
    print("\nMethod DELETE To create new user and update data of created user")
    result_delete = automationexercise_api.delete_to_create_and_update_user_account_data()
    Checking.check_json_value(result_delete, 'detail', "Method \"DELETE\" not allowed.")


""" - POST To Update User Account"""
def test_can_not_post_to_create_and_update_user_account_data():
    print("\nMethod POST To create new user and update data of created user")
    result_post = automationexercise_api.post_to_create_and_update_user_account_data()
    Checking.check_json_value(result_post, 'detail', "Method \"POST\" not allowed.")


""" - DELETE to delete user account"""
def test_can_create_new_user_account_and_delete_it():
    print("\nMethod DELETE To create new user and then delete it")
    result_delete = automationexercise_api.delete_to_create_new_user_account_and_delete_it()
    Checking.check_json_token(result_delete, ['responseCode', 'message'])
    Checking.check_json_value(result_delete, 'responseCode', 200)
    Checking.check_json_value(result_delete, 'message', "Account deleted!")


""" - GET to delete user account"""
def test_can_not_get_to_delete_user_account():
    print("\nMethod GET To create new user and then delete it")
    result_get = automationexercise_api.get_to_create_new_user_account_and_delete_it()
    Checking.check_json_value(result_get, 'detail', "Method \"GET\" not allowed.")


""" - PUT to delete user account"""
def test_can_not_put_to_delete_user_account():
    print("\nMethod PUT To create new user and then delete it")
    result_put = automationexercise_api.put_to_create_new_user_account_and_delete_it()
    Checking.check_json_value(result_put, 'detail', "Method \"PUT\" not allowed.")


""" - POST to delete user account"""
def test_can_not_post_to_delete_user_account():
    print("\nMethod POST To create new user and then delete it")
    result_post = automationexercise_api.post_to_create_new_user_account_and_delete_it()
    Checking.check_json_value(result_post, 'detail', "Method \"POST\" not allowed.")


""" - GET to create new user and then get account details by email"""
def test_get_to_create_user_and_then_get_info_by_email():
    print("\nMethod GET To create new user and then get details by email")
    result_get = automationexercise_api.get_to_create_user_and_then_get_info_by_email()
    Checking.check_json_token(result_get, ['responseCode', 'user'])
    Checking.check_json_value(result_get, 'responseCode', 200)


""" - DELETE to delete non existent account"""
def test_delete_non_existent_account():
    result_delete = automationexercise_api.delete_to_delete_account(123,123)
    Checking.check_json_value(result_delete, 'responseCode', 404)
    Checking.check_json_value(result_delete, 'message', "Account not found!")


""" - GET user information by non existent email"""
def test_can_not_get_account_detail_by_non_existent_email():
    result_get = automationexercise_api.get_user_info_by_email('777@777.qwe')
    Checking.check_json_value(result_get, 'responseCode', 404)
    Checking.check_json_value(result_get, 'message', "Account not found with this email, try another email!")


""" - GET user info by email with empty email"""
def test_can_not_get_account_detail_with_empty_email():
    result_get = automationexercise_api.get_user_info_by_email(None)
    Checking.check_json_value(result_get, 'responseCode', 400)
    Checking.check_json_value(result_get, 'message', "Bad request, email parameter is missing in GET request.")


""" - PUT to update non existent account"""
def test_cant_update_non_existent_acc():
    result_put = automationexercise_api.put_to_update_acc()
    Checking.check_json_value(result_put, 'responseCode', 404)
    Checking.check_json_value(result_put, 'message', "Account not found!")


""" - POST To Create/Register User Account that already exists"""
def test_cant_register_already_existent_account():
    print("\nMethod POST To register already existent user")
    result_post = automationexercise_api.post_to_register_user_static()
    result_post_second = automationexercise_api.post_to_register_user_static()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Email already exists!")


""" - POST to Create user without name"""
def test_cant_register_missing_name():
    print("\nMethod POST To register without name")
    result_post = automationexercise_api.post_to_register_user_with_no_name()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, name parameter is missing in POST request.")


""" - POST to Create user without email"""
def test_cant_register_missing_email():
    print("\nMethod POST To register without email")
    result_post = automationexercise_api.post_to_register_user_with_no_email()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, email parameter is missing in POST request.")


""" - POST to Create user without password"""
def test_cant_register_missing_password():
    print("\nMethod POST To register without password")
    result_post = automationexercise_api.post_to_register_user_with_no_password()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, password parameter is missing in POST request.")


""" - POST to create user without title"""
def test_cant_register_without_title():
    print("\nMethod POST To register without title")
    result_post = automationexercise_api.post_to_register_user_with_no_title()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, title parameter is missing in POST request.")


""" - POST to create user without phone number"""
def test_cant_register_without_phone_number():
    print("\nMethod POST To register without phone number")
    result_post = automationexercise_api.post_to_register_user_with_no_phone_number()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, mobile_number parameter is missing in POST request.")


""" - POST to create user without birth date"""
def test_cant_register_without_birth_date():
    print("\nMethod POST To register without birth date")
    result_post = automationexercise_api.post_to_register_user_with_no_birth_date()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, birth_date parameter is missing in POST request.")


""" - POST to create user without birth month"""
def test_cant_register_without_birth_month():
    print("\nMethod POST To register without birth date")
    result_post = automationexercise_api.post_to_register_user_with_no_birth_month()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, birth_month parameter is missing in POST request.")


""" - POST to create user without birth year"""
def test_cant_register_without_birth_year():
    print("\nMethod POST To register without birth year")
    result_post = automationexercise_api.post_to_register_user_with_no_birth_year()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, birth_year parameter is missing in POST request.")


""" - POST to create user without firstname"""
def test_cant_register_without_firstname():
    print("\nMethod POST To register without firstname")
    result_post = automationexercise_api.post_to_register_user_without_firstname()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, firstname parameter is missing in POST request.")


""" - POST to create user without lastname"""
def test_cant_register_without_lastname():
    print("\nMethod POST To register without lastname")
    result_post = automationexercise_api.post_to_register_user_without_lastname()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, lastname parameter is missing in POST request.")


""" - POST to create user without company"""
def test_cant_register_without_company():
    print("\nMethod POST To register without company")
    result_post = automationexercise_api.post_to_register_user_without_company()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, company parameter is missing in POST request.")


""" - POST to create user without address1"""
def test_cant_register_without_address1():
    print("\nMethod POST To register without address1")
    result_post = automationexercise_api.post_to_register_user_without_address1()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, address1 parameter is missing in POST request.")


""" - POST to create user without address2"""
def test_cant_register_without_address2():
    print("\nMethod POST To register without address2")
    result_post = automationexercise_api.post_to_register_user_without_address2()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, address2 parameter is missing in POST request.")


""" - POST to create user without country"""
def test_cant_register_without_country():
    print("\nMethod POST To register without country")
    result_post = automationexercise_api.post_to_register_user_without_country()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, country parameter is missing in POST request.")


""" - POST to create user without zipcode"""
def test_cant_register_without_zipcode():
    print("\nMethod POST To register without zipcode")
    result_post = automationexercise_api.post_to_register_user_without_zipcode()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, zipcode parameter is missing in POST request.")


""" - POST to create user without state"""
def test_cant_register_without_state():
    print("\nMethod POST To register without state")
    result_post = automationexercise_api.post_to_register_user_without_state()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, state parameter is missing in POST request.")


""" - POST to create user without city"""
def test_cant_register_without_city():
    print("\nMethod POST To register without city")
    result_post = automationexercise_api.post_to_register_user_without_city()
    Checking.check_json_value(result_post, 'responseCode', 400)
    Checking.check_json_value(result_post, 'message', "Bad request, city parameter is missing in POST request.")


""" - POST to create user with only name, email and password"""
def test_cant_register_without_zipcode():
    print("\nMethod POST To register without zipcode")
    result_post = automationexercise_api.post_to_register_user_with_only_name_email_and_password()
    Checking.check_json_value(result_post, 'responseCode', 400)


""" - POST to create user with 100 chars name"""
def test_cant_register_user_with_100_chars_name():
    print("\nMethod POST To register with 100 chars name")
    result_post = automationexercise_api.post_to_register_user_with_100_chars_name()
    Checking.check_json_value(result_post, 'responseCode', 413)


""" - POST to create user with 100 chars email"""
def test_cant_register_user_with_100_chars_email():
     print("\nMethod POST To register with 100 chars email")
     result_post = automationexercise_api.post_to_register_user_with_100_chars_email()
     Checking.check_json_value(result_post, 'responseCode', 413)


""" - POST to create user with 100 chars password"""
def test_cant_register_user_with_100_chars_password():
    print("\nMethod POST To register with 100 chars password")
    result_post = automationexercise_api.post_to_register_user_with_100_chars_password()
    Checking.check_json_value(result_post, 'responseCode', 413)


