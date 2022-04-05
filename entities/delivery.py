from entities.delivery_details import DeliveryDetails
from utils.validations import integer_value_validation, date_validation, time_validation


class Delivery:
    def __init__(self, delivery_number: int, supplier: str, delivered_products: list[DeliveryDetails],
                 delivery_date: str, delivery_time: str, tax_base=0, vat=0, total_sum=0, id: int=None):
        self.delivery_number = delivery_number
        self.supplier = supplier
        self.delivered_products = delivered_products
        self.delivery_date = delivery_date
        self.delivery_time = delivery_time
        self.id = id
        self.tax_base = sum([delivered_product.total_price for delivered_product in delivered_products])
        self.vat = self.tax_base * 0.20
        self.total_sum = self.tax_base + self.vat
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

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

    def to_json(self):
        return {'id': self.id, 'delivery number': self.delivery_number, 'supplier': self.supplier,
                'delivered products': self.delivered_products, 'delivery date': str(self.delivery_date),
                'delivery time': self.delivery_time, 'tax base': round(self.tax_base, 2), 'VAT': round(self.vat, 2),
                'total sum': round(self.total_sum, 2), '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        id = jsdict['id']
        delivery_number = jsdict['delivery number']
        supplier = jsdict['supplier']
        delivered_products = jsdict['delivered products']
        delivery_date = jsdict['delivery date']
        delivery_time = jsdict['delivery time']
        tax_base = jsdict['tax base']
        vat = jsdict['VAT']
        total_sum = jsdict['total sum']
        _module = jsdict['_module']
        _class = jsdict['_class']
        return cls(delivery_number, supplier, delivered_products, delivery_date, delivery_time, tax_base, vat, total_sum, id)