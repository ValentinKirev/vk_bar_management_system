from controllers.register_controller import RegisterController
from utils.helpers import destroy_widgets
from views.login_view import LoginView


class RegisterCommand:
    def __init__(self, controller: RegisterController, window):
        self.controller = controller
        self.window = window

    def __call__(self, *args, **kwargs):
        if self.controller.register() is not None:
            destroy_widgets(self.window)
            self.view = LoginView(self.window)
