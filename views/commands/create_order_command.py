from controllers.order_controller import OrderController
from repositories.cash_receipt_repository import CashReceiptRepository
from repositories.ingredients_repository import IngredientRepository
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from services.cash_receipt_service import CashReceiptService
from utils.id_generator import IdGenerator


class CreateOrderCommand:
    def __init__(self, view, operator, controller: OrderController, table_number):
        self.controller = controller
        self.table_number = table_number
        self.operator = operator
        self.view = view

    def __call__(self, *args, **kwargs):
        self.controller.create_order(self.operator, self.table_number)
        self.view.destroy()
        self.view.__init__(self.operator, OrderController(CashReceiptService(
                CashReceiptRepository(IdGenerator(), 'database/cash_receipts.json'),
                IngredientRepository(IdGenerator(), 'database/ingredients.json'),
                ProductRepository(IdGenerator(), 'database/products.json'),
                OrderRepository(IdGenerator(), 'database/orders.json'))))

