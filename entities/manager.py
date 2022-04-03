from entities.hall_manager import HallManager


class Manager(HallManager):
    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)
        self.role = 'Manager'
