from entities.order import Order
from services.cash_receipt_service import CashReceiptService


class OrderController:
    def __init__(self, cash_receipt_service: CashReceiptService, view=None):
        self.service = cash_receipt_service
        self.view = view

    def create_order(self, operator, table_number):
        self.reload_orders()
        order = self.service.order_repository.create(Order
                                                   (f"{operator.first_name} {operator.last_name}", table_number))
        self.save_orders()
        return order

    def issue_cash_receipt(self):
        pass

    def get_all_orders(self):
        self.service.order_repository.load()
        return self.service.order_repository.find_all()

    def save_orders(self):
        self.service.order_repository.save()

    def reload_orders(self):
        self.service.order_repository.load()
