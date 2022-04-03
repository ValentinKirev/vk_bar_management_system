from entities.delivery_details import DeliveryDetails
from validations import integer_value_validation, date_validation, time_validation


class Delivery:
    def __init__(self, delivery_number: int, supplier: str, delivered_products: list[DeliveryDetails],
                 delivery_date: str, delivery_time: str, id: int=None):
        self.delivery_number = delivery_number
        self.supplier = supplier
        self.delivered_products = delivered_products
        self.delivery_date = delivery_date
        self.delivery_time = delivery_time
        self.id = id
        self.tax_base = sum(delivered_product.total_price for delivered_product in delivered_products)
        self.vat = self.tax_base * 0.20
        self.total_sum = self.tax_base + self.vat

    @property
    def delivery_number(self):
        return self.__delivery_number

    @delivery_number.setter
    def delivery_number(self, value):
        error_message = "Delivery number must be integer number!"
        integer_value_validation(value, error_message)
        self.__delivery_number = value

    @property
    def delivery_date(self):
        return self.__delivery_date

    @delivery_date.setter
    def delivery_date(self, value):
        error_message = "Incorrect data format, should be YYYY.MM.DD!"
        date_validation(value, error_message)
        self.__delivery_date = value

    @property
    def delivery_time(self):
        return self.__delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        error_message = 'Incorrect time format, should be HH:MM:SS!'
        time_validation(value, error_message)
        self.__delivery_time = value

    def __str__(self):
        return '{' + f"'id': '{self.id}', 'delivery number': '{self.delivery_number}', " \
                     f"'supplier': '{self.supplier}', " \
                     f"'delivered_products': {[str(product) for product in self.delivered_products]}, " \
                     f"'delivery date': '{self.delivery_date}', 'delivery time': '{self.delivery_time}', " \
                     f"'tax base': '{self.tax_base:.2f}', 'VAT': '{self.vat:.2f}', 'total sum': '{self.total_sum:.2f}'" + '}'
