from datetime import date, datetime


class Order:
    def __init__(self, operator: str, id: int=None):
        self.operator = operator
        self.ordered_products = []
        self.total_sum = sum(ordered_product.total_price for ordered_product in self.ordered_products)
        self.id = id
        self.creation_date = date.today()
        self.creation_time = datetime.now().strftime("%H:%M:%S")

    def __str__(self):
        return '{' + f"'id': '{self.id}', 'operator': '{self.operator}', " \
                     f"'ordered products': {[str(ordered_product) for ordered_product in self.ordered_products]}, " \
                     f"'creation date': '{self.creation_date}', 'creation time': '{self.creation_time}', " \
                     f"'total sum': '{self.total_sum:.2f}'" + '}'
