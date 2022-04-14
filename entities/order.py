from datetime import date, datetime


class Order:
    def __init__(self, operator: str, table_number, ordered_products=[], creation_date=date.today(),
                 creation_time=datetime.now().strftime("%H:%M:%S"), total_sum=0, id: int=None):
        self.operator = operator
        self.table_number = table_number
        self.ordered_products = ordered_products
        self.id = id
        self.creation_date = creation_date
        self.creation_time = creation_time
        self.total_sum = sum([ordered_product.total_price for ordered_product in self.ordered_products])
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__
        self.table_number = self.table_number

    def to_json(self):
        return {'id': self.id, 'operator': self.operator, 'table number': self.table_number,
                'ordered products': self.ordered_products, 'creation date': str(self.creation_date),
                'creation time': str(self.creation_time), 'total sum': round(self.total_sum, 2),
                '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        operator = jsdict['operator']
        table_number = jsdict['table number']
        id = jsdict['id']
        ordered_products = jsdict['ordered products']
        creation_date = jsdict['creation date']
        creation_time = jsdict['creation time']
        total_sum = jsdict['total sum']
        return cls(operator, table_number, ordered_products, creation_date, creation_time, total_sum, id)
