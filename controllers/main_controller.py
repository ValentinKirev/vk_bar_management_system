from services.login_service import LoginService
from services.register_service import RegisterService
from utils.exceptions import *


class MainController:
    def __init__(self, register_service: RegisterService, login_service: LoginService, view=None):
        self.register_service = register_service
        self.login_service = login_service
        self.view = view

    def register(self):
        try:
            return self.register_service.register(self.view.first_name.get(), self.view.last_name.get(),
                                  self.view.username.get(), self.view.role.get(), self.view.password.get(),
                                  self.view.confirm_password.get(), self.view.service_password.get())
        except (UserAlreadyExist, PasswordsAreNotEqual, InvalidRole, WrongServicePassword, ValueError) as ex:
            self.view.string_var.set(str(ex))

    def login(self):
        try:
            return self.login_service.login(self.view.username.get(), self.view.password.get())
        except (UserNotFoundError, InvalidCredentials, ValueError) as ex:
            self.view.string_var.set(str(ex))
