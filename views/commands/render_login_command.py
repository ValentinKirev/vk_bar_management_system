from controllers.main_controller import MainController
from utils.helpers import destroy_widgets
from views.login_view import LoginView


class RenderLoginCommand:
    def __init__(self, window, controller: MainController):
        self.window = window
        self.controller = controller

    def __call__(self, *args, **kwargs):
        destroy_widgets(self.window)
        self.controller.view = LoginView(self.controller)