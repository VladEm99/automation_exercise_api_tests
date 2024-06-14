import json
import requests
import pytest
from utils.random_data_generation import *


"""Test methods for API"""

base_url = "https://automationexercise.com/api"

class automationexercise_api():


    """ - GET method for getting all products list"""
    @staticmethod
    def get_all_products_list():
        get_resource = "/productsList" #resource of method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        return result_get


    """DELETE to all products list"""
    @staticmethod
    def delete_to_all_products_list():
        delete_resource = "/productsList" #resource of method DELETE
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = requests.delete(delete_url)
        print(result_delete.text)
        return result_delete


    """PUT to all products list"""
    @staticmethod
    def put_to_all_products_list():
        put_resource = "/productsList"  # resource of method PUT
        put_url = base_url + put_resource
        print(put_url)
        result_put = requests.delete(put_url)
        print(result_put.text)
        return result_put


    """ - POST method to all products list"""
    @staticmethod
    def post_all_products_list():
        post_resource = "/productsList"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, None)
        print(result_post.text)
        return result_post


    """ - GET to All Brands List"""
    @staticmethod
    def get_to_all_brands_list():
        get_resource = "/brandsList"  # resource of method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        return result_get


    """ - PUT To All Brands List"""
    @staticmethod
    def put_to_all_brands_list():
        put_resource = "/brandsList"  # resource of method PUT
        put_url = base_url + put_resource
        print(put_url)
        result_put = requests.put(put_url, None)
        print(result_put.text)
        return result_put


    """ - DELETE To All Brands List"""
    @staticmethod
    def delete_to_all_brands_list():
        delete_resource = "/brandsList"  # resource of method DELETE
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = requests.delete(delete_url)
        print(result_delete.text)
        return result_delete


    """ - POST To All Brands List"""
    @staticmethod
    def post_to_all_brands_list():
        post_resource = "/brandsList"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, None)
        print(result_post.text)
        return result_post


    """ - POST to search product"""
    @staticmethod
    def post_to_search_product():
        json_for_product_search = Data_generation.generate_item_to_search()
        post_resource = "/searchProduct"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=json_for_product_search)
        print(result_post.text)
        return result_post


    """ - PUT to search product"""
    @staticmethod
    def put_to_search_product():
        put_resource = "/searchProduct"  # resource of method PUT
        put_url = base_url + put_resource
        print(put_url)
        result_put = requests.put(put_url, None)
        print(result_put.text)
        return result_put


    """ - DELETE to search product"""
    @staticmethod
    def delete_to_search_product():
        delete_resource = "/searchProduct"  # resource of method DELETE
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = requests.delete(delete_url)
        print(result_delete.text)
        return result_delete


    """ - GET to search product"""
    @staticmethod
    def get_to_search_product():
        get_resource = "/searchProduct"  # resource of method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        return result_get


    """ - POST to search product without search_product parameter"""
    @staticmethod
    def post_to_search_product_without_search_parameter():
        post_resource = "/searchProduct"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, None)
        print(result_post.text)
        return result_post


    """ - POST to search non existent product"""
    @staticmethod
    def post_to_search_non_existent_product():
        json_for_product_search = Data_generation.generate_word_100_letters()
        post_resource = "/searchProduct"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=json_for_product_search)
        print(result_post.text)
        return result_post


    """ - POST To Verify Login without email parameter"""
    @staticmethod
    def post_to_verify_login_without_email():
        data = {"email": None, "password": "123123"}
        post_resource = "/verifyLogin"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=data)
        print(result_post.text)
        return result_post


    """ - POST To Verify Login without password parameter"""
    @staticmethod
    def post_to_verify_login_without_password():
        data = {"email": "123@qwe.ee", "password": None}
        post_resource = "/verifyLogin"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=data)
        print(result_post.text)
        return result_post


    """ - POST To Verify Login without password and email parameter"""
    @staticmethod
    def post_to_verify_login_without_password_and_email():
        data = {"email": None, "password": None}
        post_resource = "/verifyLogin"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=data)
        print(result_post.text)
        return result_post


    """ - DELETE To Verify Login"""
    @staticmethod
    def delete_to_verify_login():
        delete_resource = "/verifyLogin"  # resource of method DELETE
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = requests.delete(delete_url)
        print(result_delete.text)
        return result_delete


    """ - GET To Verify Login"""
    @staticmethod
    def get_to_verify_login():
        get_resource = "/verifyLogin"  # resource of method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        return result_get


    """ - PUT To Verify Login"""
    @staticmethod
    def put_to_verify_login():
        put_resource = "/verifyLogin"  # resource of method PUT
        put_url = base_url + put_resource
        print(put_url)
        result_put = requests.put(put_url)
        print(result_put.text)
        return result_put


    """ - POST To Verify Login with invalid details"""
    @staticmethod
    def post_to_verify_login_with_invalid_details():
        login_data = {"email": "0", "password": "0"}
        post_resource = "/verifyLogin"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=login_data)
        print(result_post.text)
        return result_post


    """" - POST To Verify Login with valid details"""
    @staticmethod
    def post_to_create_new_user_and_verify_login_with_valid_details():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)

        # getting email and password from generated data to verify later
        login_data = {
            "email": user_registration_data["email"],
            "password": user_registration_data["password"]
        }

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # verifying registered acc
        post_resource_to_verify = "/verifyLogin"  # resource of method POST
        post_url_to_verify = base_url + post_resource_to_verify
        print(post_url_to_verify)
        result_post = requests.post(post_url_to_verify, data=login_data)
        print(result_post.text)
        return result_post


    """ - POST To Create/Register User Account"""
    @staticmethod
    def post_to_register_user():
        user_data = Data_generation.generate_user_data(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_data)
        print(result_post.text)
        return result_post


    """ - PUT To Create/Register User Account"""
    @staticmethod
    def put_to_register_user():
        user_data = Data_generation.generate_user_data(1)
        put_resource = "/createAccount"  # resource of method PUT
        put_url = base_url + put_resource
        print(put_url)
        result_put = requests.put(put_url, data=user_data)
        print(result_put.text)
        return result_put


    """ - DELETE To Create/Register User Account"""
    @staticmethod
    def delete_to_register_user():
        user_data = Data_generation.generate_user_data(1)
        delete_resource = "/createAccount"  # resource of method DELETE
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = requests.delete(delete_url, data=user_data)
        print(result_delete.text)
        return result_delete


    """ - GET To Create/Register User Account"""
    @staticmethod
    def get_to_register_user():
        user_data = Data_generation.generate_user_data(1)
        get_resource = "/createAccount"  # resource of method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url, data=user_data)
        print(result_get.text)
        return result_get


    """ - PUT METHOD To Update User Account"""
    @staticmethod
    def put_to_create_and_update_user_account_data():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)
        data_to_update_user = {
            "name": user_registration_data["name"],
            "email": user_registration_data["email"],
            "password": user_registration_data["password"],
            "title": "Mr",
            "birth_date": 5,
            "birth_month": 10,
            "birth_year": 1999,
            "firstname": "Vlad",
            "lastname": "VL",
            "company": "test",
            "address1": "test",
            "address2": "test",
            "country": "test",
            "zipcode": 1555,
            "state": "test",
            "city": "test",
            "mobile_number": 777777
        }

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # making API request to update user account data
        put_resource_to_update_user = "/updateAccount"
        put_url_to_update_user = base_url + put_resource_to_update_user
        print(put_url_to_update_user)
        result_put = requests.put(put_url_to_update_user, data=data_to_update_user)
        print(result_put.text)
        return result_put


    """ - GET METHOD To Update User Account"""
    @staticmethod
    def get_to_create_and_update_user_account_data():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)
        data_to_update_user = {
            "name": user_registration_data["name"],
            "email": user_registration_data["email"],
            "password": user_registration_data["password"],
            "title": "Mr",
            "birth_date": 5,
            "birth_month": 10,
            "birth_year": 1999,
            "firstname": "Vlad",
            "lastname": "VL",
            "company": "test",
            "address1": "test",
            "address2": "test",
            "country": "test",
            "zipcode": 1555,
            "state": "test",
            "city": "test",
            "mobile_number": 777777
        }

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # making API request to update user account data
        get_resource_to_update_user = "/updateAccount"
        get_url_to_update_user = base_url + get_resource_to_update_user
        print(get_url_to_update_user)
        result_get = requests.get(get_url_to_update_user, data=data_to_update_user)
        print(result_get.text)
        return result_get


    """ - DELETE METHOD To Update User Account"""
    @staticmethod
    def delete_to_create_and_update_user_account_data():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)
        data_to_update_user = {
            "name": user_registration_data["name"],
            "email": user_registration_data["email"],
            "password": user_registration_data["password"],
            "title": "Mr",
            "birth_date": 5,
            "birth_month": 10,
            "birth_year": 1999,
            "firstname": "Vlad",
            "lastname": "VL",
            "company": "test",
            "address1": "test",
            "address2": "test",
            "country": "test",
            "zipcode": 1555,
            "state": "test",
            "city": "test",
            "mobile_number": 777777
        }

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # making API request to update user account data
        delete_resource_to_update_user = "/updateAccount"
        delete_url_to_update_user = base_url + delete_resource_to_update_user
        print(delete_url_to_update_user)
        result_delete = requests.delete(delete_url_to_update_user, data=data_to_update_user)
        print(result_delete.text)
        return result_delete


    """ - POST METHOD To Update User Account"""
    @staticmethod
    def post_to_create_and_update_user_account_data():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)
        data_to_update_user = {
            "name": user_registration_data["name"],
            "email": user_registration_data["email"],
            "password": user_registration_data["password"],
            "title": "Mr",
            "birth_date": 5,
            "birth_month": 10,
            "birth_year": 1999,
            "firstname": "Vlad",
            "lastname": "VL",
            "company": "test",
            "address1": "test",
            "address2": "test",
            "country": "test",
            "zipcode": 1555,
            "state": "test",
            "city": "test",
            "mobile_number": 777777
        }

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # making API request to update user account data
        post_resource_to_update_user = "/updateAccount"
        post_url_to_update_user = base_url + post_resource_to_update_user
        print(post_url_to_update_user)
        result_post = requests.post(post_url_to_update_user, data=data_to_update_user)
        print(result_post.text)
        return result_post


    """ - DELETE METHOD To create new user and Delete created User Account"""
    @staticmethod
    def delete_to_create_new_user_account_and_delete_it():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)

        # getting email and password from generated data to delete later
        delete_data = {
            "email": user_registration_data["email"],
            "password": user_registration_data["password"]
        }
        email = {"email": user_registration_data["email"]}

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # making API request to delete created account
        delete_resource = "/deleteAccount"  # resource of method DELETE
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = requests.delete(delete_url, data=delete_data)
        print(result_delete.text)
        return result_delete


    """ - GET METHOD To create new user and Delete created User Account"""
    @staticmethod
    def get_to_create_new_user_account_and_delete_it():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)

        # getting email and password from generated data to delete later
        delete_data = {
            "email": user_registration_data["email"],
            "password": user_registration_data["password"]
        }
        email = {"email": user_registration_data["email"]}

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # making API request to delete created account
        get_resource = "/deleteAccount"  # resource of method GET
        get_url = base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url, data=delete_data)
        print(result_get.text)
        return result_get


    """ - PUT METHOD To create new user and Delete created User Account"""
    @staticmethod
    def put_to_create_new_user_account_and_delete_it():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)

        # getting email and password from generated data to delete later
        delete_data = {
            "email": user_registration_data["email"],
            "password": user_registration_data["password"]
        }
        email = {"email": user_registration_data["email"]}

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # making API request to delete created account
        put_resource = "/deleteAccount"  # resource of method PUT
        put_url = base_url + put_resource
        print(put_url)
        result_put = requests.put(put_url, data=delete_data)
        print(result_put.text)
        return result_put


    """ - POST METHOD To create new user and Delete created User Account"""
    @staticmethod
    def post_to_create_new_user_account_and_delete_it():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)

        # getting email and password from generated data to delete later
        delete_data = {
            "email": user_registration_data["email"],
            "password": user_registration_data["password"]
        }
        email = {"email": user_registration_data["email"]}

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # making API request to delete created account
        post_resource = "/deleteAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=delete_data)
        print(result_post.text)
        return result_post


    """ - GET to create user account and then get details by email"""
    @staticmethod
    def get_to_create_user_and_then_get_info_by_email():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data(1)

        # getting email data to get user account details by email later
        email_data = {
            "email": user_registration_data["email"]}

        # making API request to register new user with generated data
        post_resource_to_register = "/createAccount"  # resource of method POST
        post_url_to_register = base_url + post_resource_to_register
        result_post = requests.post(post_url_to_register, data=user_registration_data)

        # creating API request to get info by email of created user
        get_resource = "/getUserDetailByEmail"
        get_url = base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url, email_data)
        print(result_get.text)
        return result_get


    """ - GET user account detail by email"""
    @staticmethod
    def get_user_info_by_email(email_data):
        get_resource = "/getUserDetailByEmail"
        get_url = base_url + get_resource
        print(get_url)
        result_get = requests.get(get_url, {"email": email_data})
        print(result_get.text)
        return result_get


    """ - DELETE METHOD To  Delete User Account"""
    @staticmethod
    def delete_to_delete_account(email, password):
        # making API request to delete created account
        delete_resource = "/deleteAccount"  # resource of method DELETE
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = requests.delete(delete_url, data = {"email": email, "password": password})
        print(result_delete.text)
        return result_delete


    """ - POST to register new account"""
    @staticmethod
    def post_to_register_new_user(name, email, password, title, birth_date, birth_month, birth_year,
                                  firstname, lastname, company, address1, address2, country, zipcode,
                                  state, city, mobile_number):
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data={"name", "email", "password", "title", "birth_date", "birth_month", "birth_year",
                                  "firstname", "lastname", "company", "address1", "address2", "country", "zipcode",
                                  "state", "city", "mobile_number"})
        print(result_post.text)
        return result_post


    """ - PUT to update acc"""
    @staticmethod
    def put_to_update_acc():
        # data to update user info
        # making API request to update user account data
        data_to_update_user = Data_generation.generate_user_data_without_name(1)
        put_resource_to_update_user = "/updateAccount"
        put_url_to_update_user = base_url + put_resource_to_update_user
        print(put_url_to_update_user)
        result_put = requests.put(put_url_to_update_user, data=data_to_update_user)
        print(result_put.text)
        return result_put


    """ - register user with static data"""
    @staticmethod
    def post_to_register_user_static():
        data_to_create_user = Data_generation.give_static_data()
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=data_to_create_user)
        print(result_post.text)
        return result_post


    """ - register user with static data without name"""
    @staticmethod
    def post_to_register_user_with_no_name():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_name(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - register user with static data without email"""
    @staticmethod
    def post_to_register_user_with_no_email():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_email(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - register user with static data without password"""
    @staticmethod
    def post_to_register_user_with_no_password():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_password(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without title"""
    @staticmethod
    def post_to_register_user_with_no_title():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_title(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without phone number"""
    @staticmethod
    def post_to_register_user_with_no_phone_number():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_phone_number(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without birth date"""
    @staticmethod
    def post_to_register_user_with_no_birth_date():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_birth_date(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without birth month"""
    @staticmethod
    def post_to_register_user_with_no_birth_month():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_birth_month(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without birth year"""
    @staticmethod
    def post_to_register_user_with_no_birth_year():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_birth_year(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without firstname"""
    @staticmethod
    def post_to_register_user_without_firstname():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_firstname(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without lastname"""
    @staticmethod
    def post_to_register_user_without_lastname():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_lastname(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without company"""
    @staticmethod
    def post_to_register_user_without_company():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_company(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without address1"""
    @staticmethod
    def post_to_register_user_without_address1():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_address1(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without address2"""
    @staticmethod
    def post_to_register_user_without_address2():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_address2(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without country"""
    @staticmethod
    def post_to_register_user_without_country():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_country(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without zipcode"""
    @staticmethod
    def post_to_register_user_without_zipcode():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_zipcode(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without state"""
    @staticmethod
    def post_to_register_user_without_state():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_state(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user without city"""
    @staticmethod
    def post_to_register_user_without_city():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_without_city(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user with only name, email and password"""
    @staticmethod
    def post_to_register_user_with_only_name_email_and_password():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_only_name_email_and_password(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user with 100 chars name"""
    @staticmethod
    def post_to_register_user_with_100_chars_name():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_with_100_chars_name(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user with 100 chars email"""
    @staticmethod
    def post_to_register_user_with_100_chars_email():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_with_100_chars_email(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST to register user with 100 chars email"""
    @staticmethod
    def post_to_register_user_with_100_chars_password():
        # generating new user data
        user_registration_data = Data_generation.generate_user_data_with_100_chars_password(1)
        post_resource = "/createAccount"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=user_registration_data)
        print(result_post.text)
        return result_post


    """ - POST To Verify Login without password parameter"""
    @staticmethod
    def post_to_verify_login_without_password():
        data = {"email": "123@qwe.ee", "password": None}
        post_resource = "/verifyLogin"  # resource of method POST
        post_url = base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, data=data)
        print(result_post.text)
        return result_post