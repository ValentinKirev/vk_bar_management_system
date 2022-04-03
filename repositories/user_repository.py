from exceptions import UserNotFoundError
from id_generator import IdGenerator
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, id_generator: IdGenerator):
        super().__init__(id_generator)

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
        raise UserNotFoundError(f'User with username: {username} was not found!')
