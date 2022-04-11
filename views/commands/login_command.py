from controllers.main_controller import MainController
from utils.helpers import destroy_widgets
from views.orders_view import OrdersView


class LoginCommand:
    def __init__(self, controller: MainController, window):
        self.controller = controller
        self.window = window

    def __call__(self, *args, **kwargs):
        if self.controller.login() is not None:
            destroy_widgets(self.window)
            self.controller.view = OrdersView(self.controller)
