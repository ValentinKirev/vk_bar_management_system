from controllers.ingredient_controller import IngredientController
from controllers.order_controller import OrderController
from repositories.cash_receipt_repository import CashReceiptRepository
from repositories.ingredients_repository import IngredientRepository
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from services.cash_receipt_service import CashReceiptService
from utils.id_generator import IdGenerator


class AddIngredientCommand:
    def __init__(self, orders_view, operator, controller: IngredientController):
        self.controller = controller
        self.orders_view = orders_view
        self.operator = operator

    def __call__(self, *args, **kwargs):
        if self.controller.create_ingredient() is not None:
            self.controller.view.withdraw()
            self.controller.view.grab_release()
            self.orders_view.destroy()
            self.orders_view.__init__(self.operator, OrderController(CashReceiptService(
                CashReceiptRepository(IdGenerator(), 'database/cash_receipts.json'),
                IngredientRepository(IdGenerator(), 'database/ingredients.json'),
                ProductRepository(IdGenerator(), 'database/products.json'),
                OrderRepository(IdGenerator(), 'database/orders.json'))))
