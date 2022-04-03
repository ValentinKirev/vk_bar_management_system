from entities.order_details import OrderDetails
from validations import date_validation


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
