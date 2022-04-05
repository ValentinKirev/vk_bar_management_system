from entities.order import Order
from entities.product import Product
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from utils.exceptions import ProductNotFoundError


class OrderService:
    def __init__(self, order_repository: OrderRepository, product_repository: ProductRepository):
        self.orders_repository = order_repository
        self.product_repository = product_repository

    def open_new_order(self, order: Order):
        for ordered_product in order.ordered_products:
            if not self.product_repository.check_for_existing(ordered_product.product):
                raise ProductNotFoundError(f'Product with name {ordered_product.product} does not exist!')
        self.orders_repository.create(order)
        self.save_orders()

    def get_all_orders(self):
        return self.orders_repository.find_all()

    def reload_orders(self):
        self.orders_repository.load()

    def update_order(self, order_id, product: Product, quantity):
        existing_product = self.product_repository.find_by_name(product.name)
        self.orders_repository.update(order_id, existing_product, quantity)
        self.save_orders()

    def remove_order_by_id(self, order_id):
        self.orders_repository.delete_by_id(order_id)
        self.save_orders()

    def save_orders(self):
        self.orders_repository.save()
