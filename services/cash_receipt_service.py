from entities.cash_receipt import CashReceipt
from entities.order import Order
from repositories.cash_receipt_repository import CashReceiptRepository
from repositories.ingredients_repository import IngredientRepository
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository


class CashReceiptService:
    def __init__(self, cash_receipt_repository: CashReceiptRepository, ingredients_repository: IngredientRepository,
                 product_repository: ProductRepository, order_repository: OrderRepository):
        self.cash_receipt_repository = cash_receipt_repository
        self.ingredients_repository = ingredients_repository
        self.product_repository = product_repository
        self.order_repository = order_repository

    def issue_cash_receipt(self, operator, payment_type, order: Order):
        cash_receipt = CashReceipt(operator, payment_type, order.ordered_products)
        self.cash_receipt_repository.create(cash_receipt)
        self.update_ingredients_quantity_on_sale(cash_receipt.ordered_products)
        self.order_repository.delete_by_id(order.id)
        self.save_cash_receipts()
        self.ingredients_repository.save()
        self.order_repository.save()

    def update_ingredients_quantity_on_sale(self, ordered_products):
        for ordered_product in ordered_products:
            product = self.product_repository.find_by_name(ordered_product.product)
            for ingredient in product.ingredients:
                self.ingredients_repository.update_ingredients_quantity_on_sale(ingredient.name, ordered_product.quantity)

    def get_all_cash_receipts(self):
        return self.cash_receipt_repository.find_all()

    def reload_cash_receipts(self):
        self.cash_receipt_repository.load()

    def save_cash_receipts(self):
        self.cash_receipt_repository.save()
