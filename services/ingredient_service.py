from entities.ingredient import Ingredient
from repositories.ingredients_repository import IngredientRepository
from utils.exceptions import IngredientAlreadyExist


class IngredientService:
    def __init__(self, ingredients_repository: IngredientRepository):
        self.ingredients_repository = ingredients_repository

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients_repository.load()
        if self.ingredients_repository.check_for_existing(ingredient.name):
            raise IngredientAlreadyExist('Ingredient is already in repository!')
        self.ingredients_repository.create(ingredient)
        self.save_ingredients()
        return ingredient

    def get_all_ingredients(self):
        return self.ingredients_repository.find_all()

    def remove_ingredient_by_id(self, ingredient_id):
        self.ingredients_repository.delete_by_id(ingredient_id)
        self.save_ingredients()

    def update_ingredient(self, ingredient: Ingredient):
        self.ingredients_repository.update(ingredient.name, ingredient.quantity)
        self.save_ingredients()

    def reload_ingredients(self):
        self.ingredients_repository.load()

    def save_ingredients(self):
        self.ingredients_repository.save()