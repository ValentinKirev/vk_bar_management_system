from controllers.order_controller import OrderController
from views.new_order_view import NewOrderView


class RenderNewOrderView:
    def __init__(self, controller: OrderController):
        self.controller = controller

    def __call__(self, *args, **kwargs):
        self.controller.view = NewOrderView(self.controller)