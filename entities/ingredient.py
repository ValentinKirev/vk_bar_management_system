from utils.validations import name_validation, only_letters_validation, integer_value_validation, \
    quantity_is_positive_number_validation


class Ingredient:
    def __init__(self, name: str, quantity: int, measure_unit: str, id=None):
        self.name = name
        self.quantity = quantity
        self.measure_unit = measure_unit
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
        error_message = "Quantity must be integer number!"
        integer_value_validation(value, error_message)
        error_message = 'Quantity must be positive number!'
        quantity_is_positive_number_validation(value, error_message)
        self.__quantity = value

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'quantity': self.quantity, 'measure unit': self.measure_unit,
                '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        name = jsdict['name']
        quantity = jsdict['quantity']
        measure_unit = jsdict['measure unit']
        id = jsdict['id']
        _module = jsdict['_module']
        _class = jsdict['_class']
        return cls(name, quantity, measure_unit, id)
