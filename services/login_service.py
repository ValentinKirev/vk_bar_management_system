from repositories.employees_repository import EmployeesRepository
from utils.exceptions import InvalidCredentials


class LoginService:
    def __init__(self, employees_repository: EmployeesRepository):
        self.employees_repository = employees_repository
        self.current_logged_user = None

    def login(self, username, password):
        self.employees_repository.load()
        user = self.employees_repository.find_by_username(username)
        if user:
            if user.password == password:
                self.current_logged_user = user
                return user
        raise InvalidCredentials('Invalid password, please try again!')

    def logout(self):
        self.current_logged_user = None

    def get_current_logged_user(self):
        return self.current_logged_user
