from entities.order_details import OrderDetails
from utils.exceptions import ProductNotFoundError
from utils.id_generator import IdGenerator
from repositories.json_repository import JsonRepository


class OrderRepository(JsonRepository):
    def __init__(self, id_generator: IdGenerator, filepath):
        super().__init__(id_generator, filepath)

    def update(self, order_id, ordered_detail: OrderDetails):
        current_order = self.find_by_id(order_id)
        try:
            ordered_product = self.find_by_product_name(order_id, ordered_detail.product)
            ordered_product.quantity += ordered_product.quantity
        except ProductNotFoundError:
            ordered_product = ordered_detail
            current_order.ordered_products.append(ordered_detail)
        ordered_product.total_price = ordered_product.quantity * ordered_product.price
        current_order.total_sum += ordered_product.quantity * ordered_product.price
        return current_order

    def find_by_product_name(self, order_id, product_name):
        current_order = self.find_by_id(order_id)
        for ordered_product in current_order.ordered_products:
            if ordered_product.product == product_name:
                return ordered_product
        raise ProductNotFoundError(f'Product with name: {product_name} was not found!')
