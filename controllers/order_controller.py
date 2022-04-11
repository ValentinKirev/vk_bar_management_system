from entities.order import Order
from services.order_service import OrderService


class OrderController:
    def __init__(self, orders_service: OrderService, view=None):
        self.orders_service = orders_service
        self.view = view

    def create_order(self, table_number):
        order = self.orders_service.open_new_order(Order(self.view.operator))
        order.table_number = table_number

    def get_all_orders(self):
        self.orders_service.reload_orders()
        return self.orders_service.get_all_orders()
