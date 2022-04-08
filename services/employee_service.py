from entities.employee import Employee
from repositories.employees_repository import EmployeesRepository
from utils.exceptions import UserAlreadyExist


class EmployeeService:
    def __init__(self, employees_repository: EmployeesRepository):
        self.employees_repository = employees_repository

    def add_new_employee(self, employee: Employee):
        if self.employees_repository.check_for_existing(employee.username):
            raise UserAlreadyExist(f'User with username {employee.username} already exist!')
        self.employees_repository.create(employee)
        self.save_employees()

    def update_employee_account(self, username, role):
        employee = self.employees_repository.find_by_username(username)
        employee.role = role
        self.save_employees()

    def remove_employee_by_username(self, username):
        employees = self.get_all_employees()
        for employee in employees:
            if employee.username == username:
                del self.employees_repository.entities[employee.id]
        self.save_employees()

    def get_all_employees(self):
        return self.employees_repository.find_all()

    def reload_employees(self):
        self.employees_repository.load()

    def save_employees(self):
        self.employees_repository.save()
