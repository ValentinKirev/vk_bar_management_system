from entities.base_product import BaseProduct


class ComplexProduct(BaseProduct):
    def __init__(self, name: str, type: str, measure_unit: str, quantity: int,
                 expiration_date: str, price: float, ingredients: dict):
        super().__init__(name, type, measure_unit, quantity, expiration_date, price)
        self.ingredients = ingredients

    def __str__(self):
        ingredients = {key: str(value) for (key, value) in self.ingredients.items()}
        return '{' + f"'id': '{self.id}', 'name': '{self.name}', 'type': '{self.type}'," \
                     f" 'measure unit': '{self.measure_unit}', 'quantity': '{self.quantity}'," \
                     f" 'expiration date': '{self.expiration_date}', 'price': '{self.price:.2f}', " \
                     f"'ingredients': {ingredients}" + '}'
