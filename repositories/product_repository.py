from exceptions import ProductNotFoundError
from id_generator import IdGenerator
from repositories.json_repository import JsonRepository


class ProductRepository(JsonRepository):
    def __init__(self, id_generator: IdGenerator, filepath):
        super().__init__(id_generator, filepath)

    def update(self, name, type, measure_unit, quantity, price, ingredients):
        product = self.find_by_name(name)
        product.name = name
        product.type = type
        product.measure_unit = measure_unit
        product.quantity = quantity
        product.price = price
        product.ingredients = ingredients
        id = product.id
        self.entities[id] = product
        return product

    def find_by_name(self, name):
        for product in self.entities.values():
            if product.name == name:
                return product
        raise ProductNotFoundError(f'Product with name: {name} was not found!')
