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

    def __str__(self):
        return '{' + f"'id': '{self.id}', 'operator': '{self.operator}', " \
                     f"'ordered products': {[str(product) for product in self.ordered_products]}, " \
                     f"'creation date': '{self.issue_date}', 'creation time': '{self.issue_time}', " \
                     f"'total sum': '{self.total_sum:.2f}', 'payment_type': '{self.payment_type}'" + '}'
