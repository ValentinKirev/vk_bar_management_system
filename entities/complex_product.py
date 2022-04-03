from entities.base_product import BaseProduct


class ComplexProduct(BaseProduct):
    def __init__(self, name: str, type: str, measure_unit: str, quantity: int,
                 expiration_date: str, price: float, ingredients: dict):
        super().__init__(name, type, measure_unit, quantity, expiration_date, price)
        self.ingredients = ingredients

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'type': self.type, 'measure unit': self.measure_unit,
                'quantity': self.quantity, 'expiration date': self.expiration_date, 'price': round(self.price, 2),
                'ingredients': self.ingredients}
