from entities.ingredient import Ingredient
from entities.product import Product
from entities.cash_receipt import CashReceipt
from entities.delivery import Delivery
from entities.delivery_details import DeliveryDetails
from entities.employee import Employee
from entities.order import Order
from entities.order_details import OrderDetails
from repositories.ingredients_repository import IngredientRepository
from services.cash_receipt_service import CashReceiptService
from services.delivery_service import DeliveryService
from services.employee_service import EmployeeService
from services.ingredient_service import IngredientService
from services.order_service import OrderService
from services.product_service import ProductService
from utils.id_generator import IdGenerator
from repositories.cash_receipt_repository import CashReceiptRepository
from repositories.deliveries_repository import DeliveryRepository
from repositories.employees_repository import EmployeesRepository
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository


if __name__ == '__main__':
    users_repo = EmployeesRepository(IdGenerator(), 'database/employees.json')
    products_repo = ProductRepository(IdGenerator(), 'database/products.json')
    orders_repo = OrderRepository(IdGenerator(), 'database/orders.json')
    receipts_repo = CashReceiptRepository(IdGenerator(), 'database/cash_receipts.json')
    deliveries_repo = DeliveryRepository(IdGenerator(), 'database/deliveries.json')
    ingredients_repo = IngredientRepository(IdGenerator(), 'database/ingredients.json')

    users_service = EmployeeService(users_repo)
    users_service.add_new_employee(Employee('Valentin', 'Kirev', 'Valdes', 'Valdes30'))
    users_service.add_new_employee(Employee('Spas', 'Dimitrov', 'Spas40', 'Spas40'))

    ingredient_service = IngredientService(ingredients_repo)
    coffee = Ingredient('coffee', 3, 'kilograms')
    milk = Ingredient('milk', 10, 'liters')
    ingredient_service.add_ingredient(coffee)
    ingredient_service.add_ingredient(Ingredient('coca-cola', 100, 'piece'))
    ingredient_service.add_ingredient(milk)
    ingredient_service.update_ingredient(coffee)

    product_service = ProductService(products_repo, ingredients_repo)
    coca_cola_product = Product('coca-cola', 'Non alcohol drink', 'piece', 200, '2023.12.08', 2.50, [Ingredient('coca-cola', 1, 'piece')])
    product_service.add_product(coca_cola_product)
    product_service.add_product(Product('Cappuccino', 'Hot Drink', 'piece', 5, '2024.10.08', 3.50,
                                [milk, coffee]))
    product_service.update_product('coca-cola', 'Non alcohol drink', 250, 3, [Ingredient('coca-cola', 1, 'piece')])

    order_service = OrderService(orders_repo, products_repo)

    order_service.open_new_order(Order('Ivan', [OrderDetails('coca-cola', 'piece', 2, 2.50)]))
    order_service.update_order(1, Product('coca-cola', 'Non alcohol drink', 'piece', 10, '2023.12.08', 4.99,
                                          [Ingredient('coca-cola', 1, 'piece')]), 2)

    cash_receipt_service = CashReceiptService(receipts_repo, ingredients_repo, products_repo)

    cash_receipt_service.issue_cash_receipt(CashReceipt('Ivan', 'Cash', [OrderDetails('coca-cola', 'piece', 10, 3.50)]))

    delivery_service = DeliveryService(deliveries_repo, ingredients_repo)
    delivery_service.add_delivery(Delivery(100, 'Ivan', [DeliveryDetails('coca-cola', 'piece', 100, 2.50, '2000.12.12')],
                                           '2024.10.30', '12:56:23'))
    delivery_service.add_delivery(Delivery(125, 'Illy', [DeliveryDetails('coffee', 'kilograms', 3, 67, '2000.12.12')],
                                           '2024.10.30', '12:56:23'))
    delivery_service.update_delivery(100, 'Stoqn', [DeliveryDetails('fanta', 'piece', 200, 1.80, '2022.12.12')]
                                     , '2024.7.30', '12:56:23')
