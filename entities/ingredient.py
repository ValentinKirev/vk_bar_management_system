from utils.validations import name_validation, only_letters_validation, \
    quantity_is_positive_number_validation, date_validation, float_value_validation


class Ingredient:
    def __init__(self, name: str, measure_unit: str, quantity: float, expiration_date: str, id=None):
        self.name = name
        self.measure_unit = measure_unit
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.id = id
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        error_message = "Name of ingredient must be at least 2 characters long!"
        name_validation(value, error_message)
        self.__name = value

    @property
    def measure_unit(self):
        return self.__measure_unit

    @measure_unit.setter
    def measure_unit(self, value):
        error_message = "Measure unit for ingredient must contain only letters!"
        only_letters_validation(value, error_message)
        self.__measure_unit = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        error_message = "Quantity must be integer or float number!"
        float_value_validation(value, error_message)
        error_message = 'Quantity must be positive number!'
        quantity_is_positive_number_validation(value, error_message)
        self.__quantity = value

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        error_message = "Incorrect data format, should be YYYY.MM.DD!"
        date_validation(value, error_message)
        self.__expiration_date = value

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'quantity': self.quantity, 'measure unit': self.measure_unit,
                'expiration date': self.expiration_date, '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        name = jsdict['name']
        quantity = jsdict['quantity']
        measure_unit = jsdict['measure unit']
        expiration_date = jsdict['expiration date']
        id = jsdict['id']
        _module = jsdict['_module']
        _class = jsdict['_class']
        return cls(name, measure_unit, quantity, expiration_date, id)
