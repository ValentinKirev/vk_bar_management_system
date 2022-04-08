from repositories.employees_repository import EmployeesRepository
from services.login_service import LoginService
from utils.exceptions import InvalidCredentials, UserNotFoundError
from utils.id_generator import IdGenerator


class LoginController:
    def __init__(self, service: LoginService(EmployeesRepository(IdGenerator(), 'database/employees.json')), view=None):
        self.service = service
        self.view = view

    def login(self):
        try:
            return self.service.login(self.view.username.get(), self.view.password.get())
        except (UserNotFoundError, InvalidCredentials, ValueError) as ex:
            self.view.string_var.set(str(ex))
