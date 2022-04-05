from entities.ingredient import Ingredient
from entities.product import Product
from entities.cash_receipt import CashReceipt
from entities.delivery import Delivery
from entities.delivery_details import DeliveryDetails
from entities.employee import Employee
from entities.hall_manager import HallManager
from entities.manager import Manager
from entities.order import Order
from entities.order_details import OrderDetails
from repositories.ingredients_repository import IngredientRepository
from utils.id_generator import IdGenerator
from repositories.cash_receipt_repository import CashReceiptRepository
from repositories.deliveries_repository import DeliveryRepository
from repositories.employees_repository import EmployeesRepository
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository


if __name__ == '__main__':
    user_repo = EmployeesRepository(IdGenerator(),'database/employees.json')
    user_repo.create(Employee('Ivan', 'Petkov', 'IvPet', 'Ivpetkov1'))
    user_repo.create(HallManager('Stefan', 'Ivanov', 'Stefoto', 'Stefan123'))
    user_repo.create(Manager('Dobri', 'Kostadinov', 'Dobata', 'Manager1'))

    user_repo.save()
    user_repo.load()
    print(user_repo.find_all())
    for user in user_repo:
        print(user)
    product_repo = ProductRepository(IdGenerator(), 'database/products.json')
    product_repo.create(Product('Corona', 'Beer', 'piece', 24, '2024.10.08', 4.99, [Ingredient('Corona', 1, 'piece')]))
    product_repo.create(Product('Cappuccino', 'Hot Drink', 'piece', 5, '2024.10.08', 14.99,
                                [Ingredient('Milk', 100, 'mililiters'), Ingredient('Coffee', 100, 'grams')]))
    product_repo.create(Product('Coca cola', 'Non alcohol drink', 'piece', 120, '2023.12.08', 4.99,
                                Ingredient('Coca cola', 1, 'piece')))

    product_repo.save()
    product_repo.load()
    print(product_repo.find_all())
    for product in product_repo:
        print(product)

    order_repo = OrderRepository(IdGenerator(), 'database/orders.json')
    order_repo.create(Order('Ivan', [OrderDetails('cola', 'piece', 2, 3.50), OrderDetails('sok', 'piece', 7, 5)]))
    order_repo.create(Order('Petko', [OrderDetails('fanta', 'piece', 2, 3), OrderDetails('water', 'piece', 5, 2)]))
    order_repo.create(Order('Elena', [OrderDetails('Beer', 'piece', 3, 3.50)]))

    order_repo.save()
    order_repo.load()
    print(order_repo.find_all())
    for order in order_repo:
        print(order)

    receipt_repo = CashReceiptRepository(IdGenerator(), 'database/cash_receipts.json')
    receipt_repo.create(CashReceipt('Ivan', 'Cash', [OrderDetails('cola', 'piece', 2, 3.50), OrderDetails('sok', 'piece', 7, 5)]))
    receipt_repo.create(CashReceipt('Petko', 'Card', [OrderDetails('fanta', 'piece', 2, 3), OrderDetails('water', 'piece', 5, 2)]))
    receipt_repo.create(CashReceipt('Elena', 'Cash', [OrderDetails('Beer', 'piece', 3, 3.50)]))
    receipt_repo.save()
    receipt_repo.load()
    for bill in receipt_repo:
        print(bill)

    deliveries_repo = DeliveryRepository(IdGenerator(), 'database/deliveries.json')
    deliveries_repo.create(Delivery(100, 'Ivan', [DeliveryDetails('cola', 'piece', 10, 2.50, '2000.12.12')], '2024.10.30', '12:56:23'))
    deliveries_repo.create(Delivery(125, 'Agria', [DeliveryDetails('Coffee', 'piece', 2, 3.50, '2000.12.12')],'2024.10.30',
                                    '12:56:23'))
    deliveries_repo.create(Delivery(165, 'Stoqn', [DeliveryDetails('fanta', 'piece', 2, 4.55, '2022.12.12'),
                                                   DeliveryDetails('fresh', 'piece', 7, 5, '2001.12.12')], '2024.7.30',
                                    '12:56:23'))
    deliveries_repo.save()
    deliveries_repo.load()
    for delivery in deliveries_repo:
        print(delivery)

    ingredient_repo = IngredientRepository(IdGenerator(), 'database/ingredients.json')
    ingredient_repo.create(Ingredient('Coffee', 1000, 'grams'))
    ingredient_repo.create(Ingredient('Milk', 1000, 'mililiters'))
    ingredient_repo.create(Ingredient('Cola', 10, 'piece'))

    ingredient_repo.save()
    ingredient_repo.load()

    for ingredient in ingredient_repo:
        print(ingredient)