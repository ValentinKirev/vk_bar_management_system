from entities.product import Product
from repositories.ingredients_repository import IngredientRepository
from repositories.products_repository import ProductRepository
from utils.exceptions import ProductAlreadyExist


class ProductService:
    def __init__(self, products_repository: ProductRepository, ingredients_repository: IngredientRepository):
        self.products_repository = products_repository
        self.ingredients_repository = ingredients_repository

    def add_product(self, product: Product):
        for ingredient in product.ingredients:
            self.ingredients_repository.find_by_ingredient_name(ingredient.name)
        if self.products_repository.check_for_existing(product.name):
            raise ProductAlreadyExist('Product is already in repository!')
        self.products_repository.create(product)
        self.save_products()

    def get_all_products(self):
        return self.products_repository.find_all()

    def remove_product_by_id(self, product_id):
        self.products_repository.delete_by_id(product_id)
        self.save_products()

    def update_product(self, name, type, quantity, price, ingredients):
        self.products_repository.update(name, type, quantity, price, ingredients)
        self.save_products()

    def reload_products(self):
        self.products_repository.load()

    def save_products(self):
        self.products_repository.save()