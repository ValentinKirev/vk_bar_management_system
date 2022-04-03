from datetime import date, datetime


class Order:
    def __init__(self, operator: str, id: int=None):
        self.operator = operator
        self.ordered_products = []
        self.total_sum = 0
        self.id = id
        self.creation_date = date.today()
        self.creation_time = datetime.now().strftime("%H:%M:%S")

    def to_json(self):
        return {'id': self.id, 'operator': self.operator, 'ordered products': self.ordered_products,
                'creation date': str(self.creation_date), 'creation time': str(self.creation_time),
                'total sum': round(self.total_sum, 2)}
