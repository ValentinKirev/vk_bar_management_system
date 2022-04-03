from entities.order_details import OrderDetails
from utils.validations import date_validation


class DeliveryDetails(OrderDetails):
    def __init__(self, product: str, measure_unit: str, quantity: int, price: float, expiration_date: str):
        super().__init__(product, measure_unit, quantity, price)
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
                'quantity': self.quantity, 'price': round(self.price, 2), 'total price': round(self.total_price, 2)}
