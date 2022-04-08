from controllers.login_controller import LoginController
from utils.helpers import destroy_widgets


class LoginCommand:
    def __init__(self, controller: LoginController, window):
        self.controller = controller
        self.window = window

    def __call__(self, *args, **kwargs):
        if self.controller.login() is not None:
            destroy_widgets(self.window)
