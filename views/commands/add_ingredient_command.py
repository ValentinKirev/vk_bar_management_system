from controllers.ingredient_controller import IngredientController
from controllers.order_controller import OrderController
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from services.order_service import OrderService
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
            self.orders_view.__init__(self.operator, OrderController(OrderService(OrderRepository(IdGenerator(),
                        'database/orders.json'), ProductRepository(IdGenerator(), 'database/products.json'))))
