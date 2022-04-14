from controllers.ingredient_controller import IngredientController
from views.add_ingredient_view import AddIngredientView


class RenderAddIngredientCommand:
    def __init__(self, orders_view, operator, controller: IngredientController):
        self.controller = controller
        self.orders_view = orders_view
        self.operator = operator

    def __call__(self, *args, **kwargs):
        self.controller.view = AddIngredientView(self.orders_view, self.operator, self.controller)
