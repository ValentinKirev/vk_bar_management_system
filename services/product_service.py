from entities.product import BaseProduct
from repositories.products_repository import ProductRepository


class ProductService:
    def __init__(self, products_repository: ProductRepository):
        self._products_repository = products_repository

    def add_product(self, product: BaseProduct):
        self._products_repository.create(product)
