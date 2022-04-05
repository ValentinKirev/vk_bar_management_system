from entities.delivery import Delivery
from entities.ingredient import Ingredient
from repositories.deliveries_repository import DeliveryRepository
from repositories.ingredients_repository import IngredientRepository


class DeliveryService:
    def __init__(self, delivery_repository: DeliveryRepository, ingredients_repository: IngredientRepository):
        self.delivery_repository = delivery_repository
        self.ingredients_repository = ingredients_repository

    def add_delivery(self, delivery: Delivery):
        self.add_update_ingredient(delivery.delivered_products)
        self.delivery_repository.create(delivery)
        self.save_deliveries()
        self.ingredients_repository.save()

    def update_delivery(self, delivery_number, supplier, delivered_products, delivery_date, delivery_time):
        self.delivery_repository.update(delivery_number, supplier, delivered_products, delivery_date, delivery_time)
        self.add_update_ingredient(delivered_products)
        self.save_deliveries()
        self.ingredients_repository.save()

    def add_update_ingredient(self, delivered_products):
        for delivered_product in delivered_products:
            if not self.ingredients_repository.check_for_existing(delivered_product.product):
                new_ingredient = Ingredient(delivered_product.product, delivered_product.quantity,
                                            delivered_product.measure_unit)
                self.ingredients_repository.create(new_ingredient)
            else:
                self.ingredients_repository.update(delivered_product.product, delivered_product.quantity)

    def get_all_deliveries(self):
        return self.delivery_repository.find_all()

    def remove_delivery_by_id(self, delivery_id):
        self.delivery_repository.delete_by_id(delivery_id)
        self.save_deliveries()

    def reload_deliveries(self):
        self.delivery_repository.load()

    def save_deliveries(self):
        self.delivery_repository.save()
