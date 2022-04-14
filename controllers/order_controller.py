from entities.order import Order
from services.cash_receipt_service import CashReceiptService
from services.order_service import OrderService


class OrderController:
    def __init__(self, orders_service: OrderService, cash_receipt_service: CashReceiptService, view=None):
        self.orders_service = orders_service
        self.cash_receipt_service = cash_receipt_service
        self.view = view

    def create_order(self, table_number):
        order = self.orders_service.open_new_order(Order
                                                   (f"{self.view.operator.first_name} {self.view.operator.last_name}", table_number))
        return order

    def issue_cash_receipt(self):

    def get_all_orders(self):
        self.orders_service.reload_orders()
        return self.orders_service.get_all_orders()

    def save_orders(self):
        self.orders_service.save_orders()

    def reload_orders(self):
        self.orders_service.reload_orders()
