from datetime import datetime


def name_validation(value, error_message):
    if len(value) < 2:
        raise ValueError(error_message)


def product_type_validation(value, error_message):
    for letter in value:
        if not letter.isalpha() and letter != ' ':
            raise ValueError(error_message)


def only_letters_validation(value, error_message):
    for letter in value:
        if not letter.isalpha():
            raise ValueError(error_message)


def integer_value_validation(value, error_message):
    if not isinstance(value, int):
        raise ValueError(error_message)


def float_value_validation(value, error_message):
    if not isinstance(value, float) and not isinstance(value, int):
        raise ValueError(error_message)


def date_validation(value, error_message):
    try:
        datetime.strptime(value, '%Y.%m.%d')
    except ValueError:
        raise ValueError(error_message)


def time_validation(value, error_message):
    try:
        datetime.strptime(value, '%H:%M:%S')
    except ValueError:
        raise ValueError(error_message)


def username_validation(value, error_message):
    if len(value) < 3 or len(value) > 15:
        raise ValueError(error_message)


def password_lenght_validation(value, error_message):
    if len(value) < 6:
        raise ValueError(error_message)


def password_have_digit_validation(value, error_message):
    digit_is_present = False
    for letter in value:
        if letter.isdigit():
            digit_is_present = True
    if not digit_is_present:
        raise ValueError(error_message)


def password_have_upper_letter_validation(value, error_message):
    upper_letter_is_present = False
    for letter in value:
        if letter.isupper():
            upper_letter_is_present = True
    if not upper_letter_is_present:
        raise ValueError(error_message)


def quantity_is_positive_number_validation(value, error_message):
    if value <= 0:
        raise ValueError(error_message)
