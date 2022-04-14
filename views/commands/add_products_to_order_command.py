from controllers.order_controller import OrderController
from repositories.cash_receipt_repository import CashReceiptRepository
from repositories.ingredients_repository import IngredientRepository
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from services.cash_receipt_service import CashReceiptService
from utils.id_generator import IdGenerator
from views.add_products_to_order_view import AddProductsToOrderView


class AddProductsToOrderCommand:
    def __init__(self, controller: OrderController):
        self.controller = controller

    def __call__(self, *args, **kwargs):
        try:
            product_name, price = self.controller.view.get_selected_items()
        except IndexError:
            self.controller.view.string_var.set('You must select product!')
        else:
            print(product_name, price)
            # self.controller.view = AddProductsToOrderView(product_name, price, OrderController(CashReceiptService(
            #     CashReceiptRepository(IdGenerator(), 'database/cash_receipts.json'),
            #     IngredientRepository(IdGenerator(), 'database/ingredients.json'),
            #     ProductRepository(IdGenerator(), 'database/products.json'),
            #     OrderRepository(IdGenerator(), 'database/orders.json'))))
