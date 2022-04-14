from controllers.product_controller import ProductController
from views.add_product_view import AddProductView


class RenderAddProductCommand:
    def __init__(self, orders_view, operator, controller: ProductController):
        self.controller = controller
        self.orders_view = orders_view
        self.operator = operator

    def __call__(self, *args, **kwargs):
        self.controller.view = AddProductView(self.orders_view, self.operator, self.controller, [])
