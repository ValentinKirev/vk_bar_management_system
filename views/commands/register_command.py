from controllers.main_controller import MainController
from utils.helpers import destroy_widgets
from views.login_view import LoginView


class RegisterCommand:
    def __init__(self, controller: MainController, window):
        self.controller = controller
        self.window = window

    def __call__(self, *args, **kwargs):
        if self.controller.register() is not None:
            destroy_widgets(self.window)
            self.controller.view = LoginView(self.controller)
