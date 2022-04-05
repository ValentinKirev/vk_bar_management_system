from entities.employee import Employee


class HallManager(Employee):
    def __init__(self, first_name, last_name, username, password, id=None):
        super().__init__(first_name, last_name, username, password, id)
        self.role = 'HallManager'
