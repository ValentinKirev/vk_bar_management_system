from datetime import date, datetime


class Order:
    def __init__(self, operator: str, ordered_products=[], creation_date=date.today(),
                 creation_time=datetime.now().strftime("%H:%M:%S"), total_sum=0, id: int=None):
        self.operator = operator
        self.ordered_products = ordered_products
        self.id = id
        self.creation_date = date.today()
        self.creation_time = datetime.now().strftime("%H:%M:%S")
        self.total_sum = sum([ordered_product.total_price for ordered_product in self.ordered_products])
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__
        self.table_number = 0

    def to_json(self):
        return {'id': self.id, 'operator': self.operator, 'ordered products': self.ordered_products,
                'creation date': str(self.creation_date), 'creation time': str(self.creation_time),
                'total sum': round(self.total_sum, 2), '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        operator = jsdict['operator']
        id = jsdict['id']
        ordered_products = jsdict['ordered products']
        creation_date = jsdict['creation date']
        creation_time = jsdict['creation time']
        total_sum = jsdict['total sum']
        return cls(operator, ordered_products, creation_date, creation_time, total_sum, id)
