from id_generator import IdGenerator
from repositories.base_repository import BaseRepository


class DeliveryRepository(BaseRepository):
    def __init__(self, id_generator: IdGenerator):
        super().__init__(id_generator)
