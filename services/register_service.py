from entities.employee import Employee
from entities.hall_manager import HallManager
from entities.manager import Manager
from repositories.employees_repository import EmployeesRepository
from utils.exceptions import UserAlreadyExist, PasswordsAreNotEqual, InvalidRole, WrongServicePassword


class RegisterService:
    def __init__(self, employees_repository: EmployeesRepository):
        self.employees_repository = employees_repository

    def register(self, first_name, last_name, username, role, password, confirm_password, service_password):
        accounts_types = {"Employee": Employee, 'HallManager': HallManager, 'Manager': Manager}

        if password != confirm_password:
            raise PasswordsAreNotEqual('Password and confirm password must match!')
        if role != 'Employee' and role != 'HallManager' and role != 'Manager':
            raise InvalidRole('Role must be "Employee", "HallManager" or "Manager"')
        if (role == 'Employee' and service_password == 'VK@BAR') \
                or (role == 'HallManager' and service_password == 'VK@HALL') \
                or (role == 'Manager' and service_password == 'VK@ADMIN'):
            if self.employees_repository.check_for_existing(username):
                raise UserAlreadyExist(f'User with username {username} already exist!')
        else:
            raise WrongServicePassword('Wrong service password!')

        new_user = self.employees_repository.create(accounts_types[role](first_name, last_name, username, password))
        self.save_employee()
        return new_user

    def save_employee(self):
        self.employees_repository.save()
