from controllers.main_controller import MainController
from views.orders_view import OrdersView


class LoginCommand:
    def __init__(self, controller: MainController, window):
        self.controller = controller
        self.window = window

    def __call__(self, *args, **kwargs):
        if self.controller.login() is not None:
            self.window.withdraw()
            self.operator = self.controller.login_service.get_current_logged_user()
            OrdersView(self.operator)
