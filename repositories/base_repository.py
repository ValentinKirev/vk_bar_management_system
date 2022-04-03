from exceptions import EntityNotFoundException
from id_generator import IdGenerator


class BaseRepository:
    def __init__(self, id_generator: IdGenerator):
        self.entities = {}
        self.id_generator = id_generator

    def create(self, entity):
        entity.id = self.id_generator.get_next_id()
        self.entities[entity.id] = entity
        return entity

    def find_by_id(self, id):
        found = self.entities.get(id)
        if found is None:
            raise EntityNotFoundException(f"Entity with ID: {id} not found")
        return found

    def delete_by_id(self, id):
        old = self.find_by_id(id)
        del self.entities[id]
        return old

    def __iter__(self):
        return iter(self.entities.values())
