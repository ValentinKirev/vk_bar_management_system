from repositories.json_repository import JsonRepository
from utils.exceptions import IngredientNotFoundError
from utils.id_generator import IdGenerator


class IngredientRepository(JsonRepository):
    def __init__(self, id_generator: IdGenerator, filepath):
        super().__init__(id_generator, filepath)

    def update(self, ingredient_name, quantity, measure_unit):
        current_ingredient = self.find_by_ingredient_name(ingredient_name)
        current_ingredient.quantity = quantity
        current_ingredient.measure_unit = measure_unit

    def find_by_ingredient_name(self, ingredient_name):
        for ingredient in self.entities.values():
            if ingredient.name == ingredient_name:
                return ingredient
        raise IngredientNotFoundError(f'Ingredient with name: {ingredient_name} was not found!')
