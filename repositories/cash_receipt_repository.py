from utils.id_generator import IdGenerator
from repositories.json_repository import JsonRepository


class CashReceiptRepository(JsonRepository):
    def __init__(self, id_generator: IdGenerator, filepath):
        super().__init__(id_generator, filepath)
