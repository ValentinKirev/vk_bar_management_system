from controllers.product_controller import ProductController
from views.add_ingredients_to_product_view import AddIngredientsToProductView


class AddQuantityForIngredientCommand:
    def __init__(self, orders_view, operator, controller: ProductController, ingredients, view):
        self.controller = controller
        self.ingredients = ingredients
        self.view = view
        self.orders_view = orders_view
        self.operator = operator

    def __call__(self, *args, **kwargs):
        current_ingredient = None
        try:
            self.controller.view.current_ingredient = self.controller.view.get_selected_items()
            current_ingredient= self.controller.view.current_ingredient
        except IndexError:
            self.controller.view.string_var.set('You must select ingredient!')
        else:
            self.controller.view = AddIngredientsToProductView(self.orders_view, self.operator,
                                                current_ingredient, self.ingredients, self.controller, self.view)
