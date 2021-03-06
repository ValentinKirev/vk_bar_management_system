from utils.exceptions import UserNotFoundError
from utils.id_generator import IdGenerator
from repositories.json_repository import JsonRepository


class EmployeesRepository(JsonRepository):
    def __init__(self, id_generator=IdGenerator(), filepath='database.employees.json'):
        super().__init__(id_generator, filepath)

    def update(self, username, role):
        user = self.find_by_username(username)
        user.role = role
        id = user.id
        self.entities[id] = user
        return user

    def find_by_username(self, username):
        for user in self.entities.values():
            if user.username == username:
                return user
        raise UserNotFoundError(f'User with username {username} was not found!')

    def check_for_existing(self, username):
        for user in self.entities.values():
            if user.username == username:
                return True
        return False