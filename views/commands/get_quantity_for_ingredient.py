from controllers.product_controller import ProductController


class GetQuantityForIngredient:
    def __init__(self, orders_view, operator, current_ingredient, ingredients, controller: ProductController, view):
        self.current_ingredient = current_ingredient
        self.controller = controller
        self.ingredients = ingredients
        self.view = view
        self.orders_view = orders_view
        self.operator = operator

    def __call__(self, *args, **kwargs):
        quantity = self.controller.submit_ingredients_quantity()
        if quantity is not None:
            self.ingredients.append((self.current_ingredient,  quantity))
            self.controller.view = self.view
