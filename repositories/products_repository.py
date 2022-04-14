from utils.exceptions import ProductNotFoundError
from repositories.json_repository import JsonRepository


class ProductRepository(JsonRepository):
    def __init__(self, id_generator, filepath):
        super().__init__(id_generator, filepath)

    def update(self, name, type, quantity, price, ingredients):
        product = self.find_by_name(name)
        product.type = type
        product.quantity = quantity
        product.price = price
        product.ingredients = ingredients
        return product

    def check_for_existing(self, product_name):
        for product in self.entities.values():
            if product.name == product_name:
                return True
        return False

    def find_by_name(self, name):
        for product in self.entities.values():
            if product.name == name:
                return product
        raise ProductNotFoundError(f'Product with name: {name} was not found!')
