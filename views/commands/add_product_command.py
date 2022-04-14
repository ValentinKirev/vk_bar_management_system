from controllers.order_controller import OrderController
from controllers.product_controller import ProductController
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from services.order_service import OrderService
from utils.id_generator import IdGenerator


class AddProductCommand:
    def __init__(self, orders_view, operator, controller: ProductController, ingredients, view):
        self.controller = controller
        self.ingredients = ingredients
        self.view = view
        self.orders_view = orders_view
        self.operator = operator

    def __call__(self, *args, **kwargs):
        if self.controller.add_product(self.ingredients) is not None:
            self.controller.view.withdraw()
            self.controller.view.grab_release()
            self.orders_view.destroy()
            self.orders_view.__init__(self.operator, OrderController(OrderService(OrderRepository(IdGenerator(),
                'database/orders.json'), ProductRepository(IdGenerator(), 'database/products.json'))))
