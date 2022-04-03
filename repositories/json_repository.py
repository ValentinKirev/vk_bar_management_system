import json
from exceptions import EntityNotFoundException
from helpers import dumper
from id_generator import IdGenerator


class JsonRepository:
    def __init__(self, id_generator: IdGenerator, filepath):
        self.entities = {}
        self.id_generator = id_generator
        self.filepath = filepath

    def find_all(self):
        return [entity for entity in self.entities.values()]

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

    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.find_all(), file, indent=4, default=dumper)

    def load(self):
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            for element in data:
                print(element)
