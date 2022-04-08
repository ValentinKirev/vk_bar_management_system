from repositories.employees_repository import EmployeesRepository
from services.register_service import RegisterService
from utils.exceptions import InvalidRole, PasswordsAreNotEqual, UserAlreadyExist, WrongServicePassword
from utils.id_generator import IdGenerator


class RegisterController:
    def __init__(self, service: RegisterService(EmployeesRepository(IdGenerator(), 'database/employees.json')), view=None):
        self.service = service
        self.view = view

    def register(self):
        try:
            return self.service.register(self.view.first_name.get(), self.view.last_name.get(),
                                  self.view.username.get(), self.view.role.get(), self.view.password.get(),
                                  self.view.confirm_password.get(), self.view.service_password.get())
        except (UserAlreadyExist, PasswordsAreNotEqual, InvalidRole, WrongServicePassword, ValueError) as ex:
            self.view.string_var.set(str(ex))
