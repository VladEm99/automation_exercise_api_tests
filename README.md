## Running the Tests

To run the tests, use the following command in your terminal:

python -m pytest -v -s



# API Testing Report

## Test Results

| Nr | Test                                                                             | Expected Result                                                                                  | Actual Result                             | Status |
|----|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------|--------|
| 1  | GET to all products list                                                         | Status Code 200, products list                                                                   | Status Code 200, products list            | Passed |
| 2  | DELETE to all products list                                                      | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 3  | PUT to all products list                                                         | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 4  | POST to all products list                                                        | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 5  | GET to all brands list                                                           | Status Code 200, brands list                                                                     | Status Code 200, brands list              | Passed |
| 6  | PUT to all brands list                                                           | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 7  | DELETE to all brands list                                                        | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 8  | POST to all brands list                                                          | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 9  | POST to search product                                                           | Status Code 200, searched product                                                                | Status Code 200, searched product         | Passed |
| 10 | PUT to search product                                                            | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 11 | DELETE to search product                                                         | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 12 | GET to search product                                                            | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 13 | POST to search product without search_product parameter                          | Status Code 400, message: 'Bad request, search_product parameter is missing in POST request.'    | Status Code 400, correct message          | Passed |
| 14 | POST to search non existent product                                              | Status Code 200, empty search result                                                             | Status Code 200, empty search result      | Passed |
| 15 | POST To Verify Login without email parameter                                     | Status Code 400, message: 'Bad request, email or password parameter is missing in POST request.' | Status Code 400, correct message          | Passed |
| 16 | POST To Verify Login without password parameter                                  | Status Code 400, message: 'Bad request, email or password parameter is missing in POST request.' | Status Code 400, correct message          | Passed |
| 17 | POST To Verify Login without password and email parameter                        | Status Code 400, message: 'Bad request, email or password parameter is missing in POST request.' | Status Code 400, correct message          | Passed |
| 18 | DELETE To Verify Login                                                           | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 19 | GET To Verify Login                                                              | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 20 | PUT To Verify Login                                                              | Status Code 405, message: 'This request method is not supported.'                                | Status Code 405, correct message          | Passed |
| 21 | POST To Verify Login with invalid details                                        | Status Code 404, message: 'User not found!'                                                      | Status Code 404, searched product         | Passed |
| 22 | POST To Verify Login with valid details                                          | Status Code 200, message: 'User exists!'                                                         | Status Code 200, correct message          | Passed |
| 23 | POST To Create/Register User Account with valid data                             | Status Code 201, message: 'User created!'                                                        | Status Code 201, correct message          | Passed |
| 24 | PUT To Create/Register User Account                                              | response: 'detail', "Method \"PUT\" not allowed."                                                | correct response                          | Passed |
| 25 | DELETE To Create/Register User Account                                           | response: 'detail', "Method \"DELETE\" not allowed."                                             | correct response                          | Passed |
| 26 | GET To Create/Register User Account                                              | response: 'detail', "Method \"GET\" not allowed."                                                | correct response                          | Passed |
| 27 | PUT To Update User Account                                                       | Status Code 200, message: 'User updated!'                                                        | Status Code 200, correct message          | Passed |
| 28 | GET To Update User Account                                                       | response: 'detail', "Method \"GET\" not allowed."                                                | correct response                          | Passed |
| 29 | DELETE To Update User Account                                                    | response: 'detail', "Method \"DELETE\" not allowed."                                             | correct response                          | Passed |
| 30 | POST To Update User Account                                                      | response: 'detail', "Method \"POST\" not allowed."                                               | correct response                          | Passed |
| 31 | DELETE to delete user account                                                    | Status Code 200, message: 'Account deleted!'                                                     | Status Code 200, correct message          | Passed |
| 32 | GET to delete user account                                                       | response: 'detail', "Method \"GET\" not allowed."                                                | correct response                          | Passed |
| 33 | PUT to delete user account                                                       | response: 'detail', "Method \"PUT\" not allowed."                                                | correct response                          | Passed |
| 34 | POST to delete user account                                                      | response: 'detail', "Method \"POST\" not allowed."                                               | correct response                          | Passed |
| 35 | GET to create new user and then get account details by email                     | Status Code 200, response with user details                                                      | Status Code 200, correct response         | Passed |
| 36 | DELETE to delete non existent account                                            | Status Code 404, message: 'User not found!'                                                      | Status Code 404, correct message          | Passed |
| 37 | GET user information by non existent email                                       | Status Code 404, message: 'Account not found with this email, try another email!'                | Status Code 404, correct message          | Passed |
| 38 | GET user info by email with empty email                                          | Status Code 400, message: 'Bad request, email parameter is missing in GET request.'              | Status Code 400, correct message          | Passed |
| 39 | PUT to update non existent account                                               | Status Code 404, message: 'Account not found!'                                                   | Status Code 404, correct message          | Passed |
| 40 | POST To Create/Register User Account that already exists                         | Status Code 400, message: 'Email already exists!'                                                | Status Code 400, correct message          | Passed |
| 41 | POST to Create user without name                                                 | Status Code 400, message: 'Bad request, name parameter is missing in POST request.'              | Status Code 400, correct message          | Passed |
| 42 | POST to Create user without email                                                | Status Code 400, message: 'Bad request, email parameter is missing in POST request.'             | Status Code 400, correct message          | Passed |
| 43 | POST to Create user without password                                             | Status Code 400, message: 'Bad request, password parameter is missing in POST request.'          | Status Code 400, correct message          | Passed |
| 44 | POST to create user without title                                                | Status Code 400, message: 'Bad request, title parameter is missing in POST request.'             | Status Code 201, message: 'User created!' | Failed |
| 45 | POST to create user without phone number                                         | Status Code 400, message: 'Bad request, mobile_number parameter is missing in POST request.'     | Status Code 400, correct message          | Passed |
| 46 | POST to create user without birth date                                           | Status Code 400, message: 'Bad request, birth_date parameter is missing in POST request.'        | Status Code 201, message: 'User created!' | Failed |
| 47 | POST to create user without birth month                                          | Status Code 400, message: 'Bad request, birth_month parameter is missing in POST request.'       | Status Code 201, message: 'User created!' | Failed |
| 48 | POST to create user without birth year                                           | Status Code 400, message: 'Bad request, birth_year parameter is missing in POST request.'        | Status Code 201, message: 'User created!' | Failed |
| 49 | POST to create user without firstname                                            | Status Code 400, message: 'Bad request, firstname parameter is missing in POST request.'         | Status Code 400, correct message          | Passed |
| 50 | POST to create user without lastname                                             | Status Code 400, message: 'Bad request, lastname parameter is missing in POST request.'          | Status Code 400, correct message          | Passed |
| 51 | POST to create user without company                                              | Status Code 400, message: 'Bad request, company parameter is missing in POST request.'           | Status Code 201, 'User created!'          | Failed |
| 52 | POST to create user without address1                                             | Status Code 400, message: 'Bad request, address1 parameter is missing in POST request.'          | Status Code 400, correct message          | Passed |
| 53 | POST to create user without address2                                             | Status Code 400, message: 'Bad request, address2 parameter is missing in POST request.'          | Status Code 201, 'User created!'          | Failed |
| 54 | POST to create user without country                                              | Status Code 400, message: 'Bad request, country parameter is missing in POST request.'           | Status Code 400, correct message          | Passed |
| 55 | POST to create user without zipcode                                              | Status Code 400, message: 'Bad request, zipcode parameter is missing in POST request.'           | Status Code 400, correct message          | Passed |
| 56 | POST to create user without state                                                | Status Code 400, message: 'Bad request, state parameter is missing in POST request.'             | Status Code 400, correct message          | Passed |
| 57 | POST to create user without city                                                 | Status Code 400, message: 'Bad request, city parameter is missing in POST request.'              | Status Code 400, correct message          | Passed |
| 58 | POST to create user with only name, email and password                           | Status Code 400                                                                                  | Status Code 400                           | Passed |
| 59 | POST to create user with 1000 chars name                                         | Status Code 413, cant register user, too long name                                               | Status Code 201, message: 'User created!' | Failed |
| 60 | POST to create user with 1000 chars email                                        | Status Code 413, cant register user, too long email                                              | Status Code 201, message: 'User created!' | Failed |
| 61 | POST to create user with 1000 chars password                                     | Status Code 413, cant register user, too long name                                               | Status Code 201, message: 'User created!' | Failed |
| 62 | POST to create user with invalid email format                                    | Status Code 400, message: 'Invalid email format.'                                                | Status Code 201, message: 'User created!' | Failed |
| 63 | Create new user, update, get user details and delete created user account        | Status Code 200, message: 'User deleted!'                                                        | Status Code 200, correct message          | Passed |
| 64 | Create new user, delete it and verify that user deleted by getting data by email | Status Code 404, message: 'Account not found with this email, try another email!'                | Status Code 404, correct message          | Passed |
| 65 | Create new user and update it with invalid email                                 | Status Code 404, message: 'Account not found !'                                                  | Status Code 404, correct message          | Passed |
| 66 | Create new user and update it with invalid password                              | Status Code 404, message: 'Account not found !'                                                  | Status Code 404, correct message          | Passed |

## Analysis

### Registration with 1000 character name, password or email

- **Expected Result**: Status Code 413, cant create user
- **Actual Result**: Status Code 201, creating user
- **Possible Reason**: The API does not check the length of the input values.

### Registration with missing birth date, month, year, company, address2

- **Expected Result**: Status Code 413, cant create user
- **Actual Result**: Status Code 201, creating new user with missing data
- **Possible Reason**: The API allows to register user with some missing data.

### Registration with invalid email format

- **Expected Result**: Status Code 400, message: "Invalid email format."
- **Actual Result**: Status Code 201, creating new user with invalid email
- **Possible Reason**: The API does not check email for correct format.

## Suggestions for Improvement

- Add validation to limit the length of the input data to a reasonable maximum (e.g., 50 or 100 characters).
- Add validation of email format.
- Add/Update the API documentation to include all constraints and valid input values, describe fields that can be leaved empty.
