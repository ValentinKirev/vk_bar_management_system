from validations import *


class Employee:
    def __init__(self, first_name: str, last_name: str, username: str, password: str, id: int=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.role = 'Employee'
        self.id = id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        error_message = "First name must be at least 2 characters long!"
        name_validation(value, error_message)
        error_message = "First name must contain only letters!"
        only_letters_validation(value, error_message)
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        error_message = "Last name must be at least 2 characters long!"
        name_validation(value, error_message)
        error_message = "Last name must contain only letters!"
        only_letters_validation(value, error_message)
        self.__last_name = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        error_message = "Username must be between 3 and 15 characters long!"
        username_validation(value, error_message)
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        error_message = "Password must be at least 6 characters long!"
        password_lenght_validation(value, error_message)
        error_message = "Password must contain at least 1 digit!"
        password_have_digit_validation(value, error_message)
        error_message = 'Password must contain at least 1 upper letter!'
        password_have_upper_letter_validation(value, error_message)
        self.__password = value

    def to_json(self):
        return {'id': self.id, 'first name': self.first_name, 'last name': self.last_name, 'username': self.username,
                'password': self.password, 'role': self.role}
