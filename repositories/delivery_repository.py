from exceptions import DeliveryNotFoundError
from id_generator import IdGenerator
from repositories.json_repository import JsonRepository


class DeliveryRepository(JsonRepository):
    def __init__(self, id_generator: IdGenerator, filepath):
        super().__init__(id_generator, filepath)

    def update(self, delivery_number, supplier, delivered_products, delivery_date, delivery_time):
        delivery = self.find_by_delivery_number(delivery_number)
        delivery.supplier = supplier
        delivery.delivered_products = delivered_products
        delivery.delivery_date = delivery_date
        delivery.delivery_time = delivery_time

    def find_by_delivery_number(self, delivery_number):
        for delivery in self.entities.values():
            if delivery_number == delivery.delivery_number:
                return delivery
        raise DeliveryNotFoundError(f"Delivery with delivery number {delivery_number} was not found!")
