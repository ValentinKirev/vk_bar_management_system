from entities.order_details import OrderDetails
from exceptions import ProductNotFoundError
from id_generator import IdGenerator
from repositories.base_repository import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self, id_generator: IdGenerator):
        super().__init__(id_generator)

    def update(self, order_id, product_name, measure_unit, quantity, price):
        current_order = self.find_by_id(order_id)
        try:
            ordered_product = self.find_by_product_name(order_id, product_name)
            ordered_product.quantity += quantity
        except ProductNotFoundError:
            ordered_product = OrderDetails(product_name, measure_unit, quantity, price)
            current_order.ordered_products.append(ordered_product)
        finally:
            ordered_product.total_price = ordered_product.quantity * ordered_product.price
        return current_order

    def find_by_product_name(self, order_id, product_name):
        current_order = self.find_by_id(order_id)
        for ordered_product in current_order.ordered_products:
            if ordered_product.product == product_name:
                return ordered_product
        raise ProductNotFoundError(f'Product with name: {product_name} was not found!')