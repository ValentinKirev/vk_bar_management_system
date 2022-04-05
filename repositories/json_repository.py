import json
from utils.exceptions import EntityNotFoundException
from utils.helpers import dumper, object_hook
from utils.id_generator import IdGenerator


class JsonRepository:
    def __init__(self, id_generator: IdGenerator, filepath):
        self.entities = {}
        self.id_generator = id_generator
        self.filepath = filepath

    def find_all(self):
        return [entity for entity in self.entities.values()]

    def create(self, entity):
        if entity.id is None:
            entity.id = self.id_generator.get_next_id()
        self.entities[entity.id] = entity
        return entity

    def add_all(self, entities):
        for entity in entities:
            self.entities[entity.id] = entity

    def find_by_id(self, id):
        found = self.entities.get(id)
        if found is None:
            raise EntityNotFoundException(f"Entity with ID: {id} not found")
        return found

    def delete_by_id(self, id):
        old = self.find_by_id(id)
        del self.entities[id]
        return old

    def clear(self):
        self.entities.clear()

    def __iter__(self):
        return iter(self.entities.values())

    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.find_all(), file, indent=4, default=dumper)

    def load(self):
        self.clear()
        with open(self.filepath, "rt", encoding="utf-8") as file:
            entities = json.load(file, object_hook=object_hook)
            for entity in entities:
                self.create(entity)
