class EntityNotFoundException(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class UsertAlreadyExist(Exception):
    pass


class ProductNotFoundError(Exception):
    pass


class ProductAlreadyExist(Exception):
    pass


class DeliveryNotFoundError(Exception):
    pass


class IngredientNotFoundError(Exception):
    pass


class IngredientAlreadyExist(Exception):
    pass


class InvalidCredentials(Exception):
    pass


class PasswordsAreNotEqual(Exception):
    pass
