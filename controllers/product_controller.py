from entities.product import Product
from services.product_service import ProductService
from utils.exceptions import ProductAlreadyExist


class ProductController:
    def __init__(self, service: ProductService, view=None):
        self.service = service
        self.view = view

    def add_product(self, ingredients):
        try:
            try:
                return self.service.add_product(Product(self.view.product_name.get(), self.view.product_type.get(),
                                             self.view.measure_unit.get(),
                                        float(self.view.quantity.get()), float(self.view.price.get()), ingredients))
            except (ValueError, ProductAlreadyExist) as ex:
                self.view.string_var.set(str(ex))
            try:
                float(self.view.quantity.get())
            except ValueError:
                raise ValueError('Quantity must be integer or float number!')
            try:
                float(self.view.price.get())
            except ValueError:
                raise ValueError('Price must be integer or float number!')
        except (ValueError, ProductAlreadyExist) as ex:
            self.view.string_var.set(str(ex))

    def submit_ingredients_quantity(self):
        try:
            quantity = float(self.view.quantity.get())
        except ValueError:
            self.view.string_var.set('Must be integer or float number!')
        else:
            self.view.withdraw()
            self.view.grab_release()
            return quantity
