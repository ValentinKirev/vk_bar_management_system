from entities.order import Order
from entities.order_details import OrderDetails
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository


class OrderService:
    def __init__(self, order_repository: OrderRepository, product_repository: ProductRepository):
        self.orders_repository = order_repository
        self.product_repository = product_repository

    def open_new_order(self, order: Order):
        self.orders_repository.create(order)
        self.save_orders()

    def get_all_orders(self):
        return self.orders_repository.find_all()

    def reload_orders(self):
        self.orders_repository.load()

    def update_order(self, order_id, ordered_detail: OrderDetails):
        self.product_repository.find_by_name(ordered_detail.product)
        self.orders_repository.update(order_id, ordered_detail)
        self.save_orders()

    def remove_order_by_id(self, order_id):
        self.orders_repository.delete_by_id(order_id)
        self.save_orders()

    def save_orders(self):
        self.orders_repository.save()
