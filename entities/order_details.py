from utils.validations import name_validation, only_letters_validation, integer_value_validation, \
    float_value_validation, quantity_is_positive_number_validation


class OrderDetails:
    def __init__(self, product: str, measure_unit: str, quantity: int, price: float, total_price=0):
        self.product = product
        self.measure_unit = measure_unit
        self.quantity = quantity
        self.price = price
        self.total_price = self.price * self.quantity
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        error_message = "Name of product must be at least 2 characters long!"
        name_validation(value, error_message)
        self.__product = value

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
        error_message = 'Quantity must be positive number!'
        quantity_is_positive_number_validation(value, error_message)
        self.__quantity = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        error_message = "Price must be floating point number!"
        float_value_validation(value, error_message)
        self.__price = value

    def to_json(self):
        return {'product': self.product, 'measure unit': self.measure_unit, 'quantity': self.quantity,
                'price': round(self.price, 2), 'total price': round(self.total_price, 2),
                '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        product = jsdict['product']
        measure_unit = jsdict['measure unit']
        quantity = jsdict['quantity']
        price = jsdict['price']
        total_price = jsdict['total price']
        _module = jsdict['_module']
        _class = jsdict['_class']
        return cls(product, measure_unit, quantity, price, total_price)
