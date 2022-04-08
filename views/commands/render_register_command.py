from controllers.register_controller import RegisterController
from repositories.employees_repository import EmployeesRepository
from services.register_service import RegisterService
from utils.helpers import destroy_widgets
from utils.id_generator import IdGenerator
from views.register_view import RegisterView


class RenderRegisterCommand:
    def __init__(self, window):
        self.window = window

    def __call__(self, *args, **kwargs):
        destroy_widgets(self.window)
        RegisterView(RegisterController(RegisterService(EmployeesRepository(IdGenerator(), 'database/employees.json'))))
