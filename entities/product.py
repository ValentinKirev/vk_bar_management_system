from entities.ingredient import Ingredient
from utils.validations import *


class Product:
    def __init__(self, name: str, type: str, measure_unit: str, quantity: int,
                 expiration_date: str, price: float, ingredients: [Ingredient], id: int = None):
        self.name = name
        self.type = type
        self.measure_unit = measure_unit
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.price = price
        self.ingredients = ingredients
        self.id = id
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Name of product must be at least 2 characters long!"
        name_validation(value, error_message)
        self.__name = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        error_message = "Type of product must contain only letters!"
        product_type_validation(value, error_message)
        self.__type = value

    @property
    def measure_unit(self):
        return self.__measure_unit

    @measure_unit.setter
    def measure_unit(self, value):
        error_message = "Measure unit for product must contain only letters!"
        only_letters_validation(value, error_message)
        self.__measure_unit = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        error_message = "Quantity must be integer number!"
        integer_value_validation(value, error_message)
        self.__quantity = value

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        error_message = "Incorrect data format, should be YYYY.MM.DD!"
        date_validation(value, error_message)
        self.__expiration_date = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        error_message = "Price must be floating point number!"
        float_value_validation(value, error_message)
        self.__price = value

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'type': self.type, 'measure unit': self.measure_unit,
                'quantity': self.quantity, 'expiration date': self.expiration_date, 'price': round(self.price, 2),
                'ingredients': self.ingredients, '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        id = jsdict['id']
        name = jsdict['name']
        type = jsdict['type']
        measure_unit = jsdict['measure unit']
        quantity = jsdict['quantity']
        expiration_date = jsdict['expiration date']
        price = jsdict['price']
        ingredients = jsdict['ingredients']
        _module = jsdict['_module']
        _class = jsdict['_class']
        return cls(name, type, measure_unit, quantity, expiration_date, price, ingredients, id)
