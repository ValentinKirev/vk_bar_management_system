from entities.ingredient import Ingredient
from services.ingredient_service import IngredientService
from utils.exceptions import IngredientAlreadyExist


class IngredientController:
    def __init__(self, service: IngredientService, view=None):
        self.service = service
        self.view = view

    def create_ingredient(self):
        try:
            return self.service.add_ingredient(Ingredient(self.view.ingredient_name.get(), self.view.measure_unit.get(),
                                               int(self.view.quantity.get()), self.view.expiration_date.get()))
        except (IngredientAlreadyExist, ValueError) as ex:
            self.view.string_var.set(str(ex))

    def save_ingredients(self):
        self.service.save_ingredients()

    def reload_ingredients(self):
        self.service.reload_ingredients()