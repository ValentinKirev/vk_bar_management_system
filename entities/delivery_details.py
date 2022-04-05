from entities.order_details import OrderDetails
from utils.validations import date_validation


class DeliveryDetails(OrderDetails):
    def __init__(self, product: str, measure_unit: str, quantity: int, price: float, expiration_date: str, total_price=0):
        super().__init__(product, measure_unit, quantity, price, total_price)
        self.expiration_date = expiration_date

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        error_message = "Incorrect data format, should be YYYY.MM.DD!"
        date_validation(value, error_message)
        self.__expiration_date = value

    def to_json(self):
        return {'product': self.product, 'expiration date': self.expiration_date, 'measure unit': self.measure_unit,
                'quantity': self.quantity, 'price': round(self.price, 2), 'total price': round(self.total_price, 2),
                '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        product = jsdict['product']
        expiration_date = jsdict['expiration date']
        measure_unit = jsdict['measure unit']
        quantity = jsdict['quantity']
        price = jsdict['price']
        total_price = jsdict['total price']
        _module = jsdict['_module']
        _class = jsdict['_class']
        return cls(product, measure_unit, quantity, price, expiration_date, total_price)
