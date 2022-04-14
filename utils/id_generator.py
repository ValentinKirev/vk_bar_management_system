class IdGenerator:
    def __init__(self):
        self._next_id = 0

    def get_next_id(self):
        self._next_id += 1
        return self._next_id
