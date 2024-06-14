import string

import faker
from faker import Faker
from faker.generator import random
from faker.providers import internet

"""Generates random user data for registration"""

class Data_generation:


    """Generate user data for registration"""
    def generate_user_data(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration with only name, email and password"""
    def generate_user_data_only_name_email_and_password(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": None,
                "birth_date": None,
                "birth_month": None,
                "birth_year": None,
                "firstname": None,
                "lastname": None,
                "company": None,
                "address1": None,
                "address2": None,
                "country": None,
                "zipcode": None,
                "state": None,
                "city": None,
                "mobile_number": None
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data without birth month"""
    def generate_user_data_without_birth_month(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": None,
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without birth year"""
    def generate_user_data_without_birth_year(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": None,
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without firstname"""
    def generate_user_data_without_firstname(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": None,
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without lastname"""
    def generate_user_data_without_lastname(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": None,
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without company"""
    def generate_user_data_without_company(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": None,
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without address1"""
    def generate_user_data_without_address1(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": None,
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without address2"""
    def generate_user_data_without_address2(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": None,
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without country"""
    def generate_user_data_without_country(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": None,
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without zipcode"""
    def generate_user_data_without_zipcode(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": None,
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without state"""
    def generate_user_data_without_state(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": None,
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without city"""
    def generate_user_data_without_city(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": None,
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without birth date"""
    def generate_user_data_without_birth_date(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": None,
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without phone number"""
    def generate_user_data_without_phone_number(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": None
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate item to search (top, tshirt, jean)"""
    @staticmethod
    def generate_item_to_search():
        fake = Faker()
        search_data = ["top", "tshirt", "jean"]
        item = {"search_product": search_data[random.randint(0, 2)]}
        print(item)
        return item


    """Generate user data for registration without name"""
    def generate_user_data_without_name(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": None,
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without email"""
    def generate_user_data_without_email(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": None,
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration without password"""
    def generate_user_data_without_password(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": None,
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Get static user data"""
    @staticmethod
    def give_static_data():
        user = {
            "name": "name",
            "email": "fake.free_email@123.ee",
            "password": "123sdfdsf",
            "title": "Mr",
            "birth_date": 5,
            "birth_month": 5,
            "birth_year": 2000,
            "firstname": "fakename",
            "lastname": "fakename",
            "company": "fakecompany",
            "address1": "fake.address",
            "address2": "fake.address",
            "country": "fake.country",
            "zipcode": "fake.zipcode",
            "state": "fake.name",
            "city": "fake.city",
            "mobile_number": 1231231321
        }
        return user


    """Get static user data without name"""
    @staticmethod
    def give_static_data_no_name():
        user = {
            "name": None,
            "email": "fake.free_email@123.ee",
            "password": "123sdfdsf",
            "title": "Mr",
            "birth_date": 5,
            "birth_month": 5,
            "birth_year": 2000,
            "firstname": "fakename",
            "lastname": "fakename",
            "company": "fakecompany",
            "address1": "fake.address",
            "address2": "fake.address",
            "country": "fake.country",
            "zipcode": "fake.zipcode",
            "state": "fake.name",
            "city": "fake.city",
            "mobile_number": 1231231321
        }
        return user


    """Generate user data for registration without title"""
    def generate_user_data_without_title(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": fake.password(),
                "title": None,
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration with name that contains 100 chars"""
    def generate_user_data_with_100_chars_name(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            def generate_word_100_letters():
                return ''.join(random.choices(string.ascii_lowercase, k=100))
            word = generate_word_100_letters()
            user = {
                "name": word,
                "email": fake.free_email(),
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration with email that contains 100 chars"""
    def generate_user_data_with_100_chars_email(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            def generate_word_100_letters():
                return ''.join(random.choices(string.ascii_lowercase, k=100))
            word = generate_word_100_letters()
            user = {
                "name": fake.name(),
                "email": word,
                "password": fake.password(),
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate user data for registration with password that contains 100 chars"""
    def generate_user_data_with_100_chars_password(num_of_users):
        # Create a Faker instance.
        fake = Faker()
        fake.add_provider(internet)
        user_data = []

        for _ in range(num_of_users):
            # Create a dictionary representing a user with various attributes.
            def generate_word_100_letters():
                return ''.join(random.choices(string.ascii_lowercase, k=100))
            word = generate_word_100_letters()
            user = {
                "name": fake.name(),
                "email": fake.free_email(),
                "password": word,
                "title": "Mr",
                "birth_date": random.randint(1, 31),
                "birth_month": random.randint(1, 12),
                "birth_year": random.randint(1920, 2024),
                "firstname": fake.name(),
                "lastname": fake.name(),
                "company": fake.company(),
                "address1": fake.address(),
                "address2": fake.address(),
                "country": fake.country(),
                "zipcode": fake.zipcode(),
                "state": fake.name(),
                "city": fake.city(),
                "mobile_number": fake.phone_number()
            }
            # Append the user data dictionary to the user_data list.
            user_data.append(user)
        # Return generated user data.
        return user_data[0]


    """Generate 100 chars"""
    @staticmethod
    def generate_word_100_letters():
        item = {"search_product": ''.join(random.choices(string.ascii_lowercase, k=100))}
        return item


