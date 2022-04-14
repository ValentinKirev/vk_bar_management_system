from controllers.main_controller import MainController
from controllers.order_controller import OrderController
from repositories.cash_receipt_repository import CashReceiptRepository
from repositories.ingredients_repository import IngredientRepository
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from services.cash_receipt_service import CashReceiptService
from utils.id_generator import IdGenerator
from views.orders_view import OrdersView


class LoginCommand:
    def __init__(self, controller: MainController, window):
        self.controller = controller
        self.window = window

    def __call__(self, *args, **kwargs):
        if self.controller.login() is not None:
            self.window.withdraw()
            self.operator = self.controller.login_service.get_current_logged_user()
            OrdersView(self.operator, OrderController(CashReceiptService(
                CashReceiptRepository(IdGenerator(), 'database/cash_receipts.json'),
                IngredientRepository(IdGenerator(), 'database/ingredients.json'),
                ProductRepository(IdGenerator(), 'database/products.json'),
                OrderRepository(IdGenerator(), 'database/orders.json'))))
