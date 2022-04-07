from datetime import date, datetime


class CashReceipt:
    def __init__(self, operator: str, payment_type: str, ordered_products=[],
                 issue_date=date.today(), issue_time=datetime.now().strftime("%H:%M:%S"), total_sum=0, id: int=None):
        self.operator = operator
        self.payment_type = payment_type
        self.ordered_products = ordered_products
        self.issue_date = date.today()
        self.issue_time = datetime.now().strftime("%H:%M:%S")
        self.total_sum = sum([ordered_product.total_price for ordered_product in self.ordered_products])
        self.id = id
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    def to_json(self):
        return {'id': self.id, 'operator': self.operator, 'ordered products': self.ordered_products,
                'issue date': str(self.issue_date), 'issue time': str(self.issue_time),
                'total sum': round(self.total_sum, 2), 'payment type': self.payment_type,
                '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        operator = jsdict['operator']
        payment_type = jsdict['payment type']
        ordered_products = jsdict['ordered products']
        issue_date = jsdict['issue date']
        issue_time = jsdict['issue time']
        total_sum = jsdict['total sum']
        id = jsdict['id']
        return cls(operator, payment_type, ordered_products, issue_date, issue_time, total_sum, id)
