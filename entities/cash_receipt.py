from datetime import date, datetime


class CashReceipt:
    def __init__(self, operator: str, payment_type: str, ordered_products, id: int=None):
        self.operator = operator
        self.payment_type = payment_type
        self.ordered_products = ordered_products
        self.id = id
        self.issue_date = date.today()
        self.issue_time = datetime.now().strftime("%H:%M:%S")
        self.total_sum = sum(ordered_product.total_price for ordered_product in ordered_products)

    def to_json(self):
        return {'id': self.id, 'operator': self.operator, 'ordered products': self.ordered_products,
                'creation date': str(self.issue_date), 'creation time': str(self.issue_time),
                'total sum': round(self.total_sum, 2), 'payment_type': self.payment_type}
