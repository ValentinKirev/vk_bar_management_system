from controllers.login_controller import LoginController
from repositories.employees_repository import EmployeesRepository
from services.login_service import LoginService
from utils.helpers import destroy_widgets
from utils.id_generator import IdGenerator
from views.login_view import LoginView


class RenderLoginCommand:
    def __init__(self, window):
        self.window = window

    def __call__(self, *args, **kwargs):
        destroy_widgets(self.window)
        LoginView(LoginController(LoginService(EmployeesRepository(IdGenerator(),
                                                                                   'database/employees.json'))))
