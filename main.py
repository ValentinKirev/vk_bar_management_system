import json

from entities.base_product import BaseProduct
from entities.cash_receipt import CashReceipt
from entities.complex_product import ComplexProduct
from entities.delivery import Delivery
from entities.delivery_details import DeliveryDetails
from entities.employee import Employee
from entities.hall_manager import HallManager
from entities.manager import Manager
from entities.order import Order
from entities.order_details import OrderDetails
from id_generator import IdGenerator
from repositories.delivery_repository import DeliveryRepository
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository


if __name__ == '__main__':
    user_repo = UserRepository(IdGenerator())
    user_repo.create(Employee('Ivan', 'Petkov', 'IvPet', 'Ivpetkov1'))
    user_repo.create(HallManager('Stefan', 'Ivanov', 'Stefoto', 'Stefan123'))
    user_repo.create(Manager('Dobri', 'Kostadinov', 'Dobata', 'Manager1'))

    for employee in user_repo:
        print(employee)

    user_repo.delete_by_id(2)
    user_repo.update('Dobata', 'Bartender')

    for employee in user_repo:
        print(employee)

    product_repo = ProductRepository(IdGenerator())
    product_repo.create(BaseProduct('Corona', 'Beer', 'piece', 24, '2024.10.08', 4.99))
    product_repo.create(ComplexProduct('Cappuccino', 'Hot Drink', 'piece', 5, '2024.10.08', 14.99, {'Milk': 200, 'Coffee': 100}))
    product_repo.create(BaseProduct('Coca cola', 'Non alcohol drink', 'piece', 120, '2023.12.08', 4.99))

    product_repo.delete_by_id(1)
    print(product_repo.find_by_id(3))
    print(product_repo.find_by_name('Cappuccino'))
    for product in product_repo:
        print(product)

    product_repo.update('Cappuccino', 'mix', 'mililiters', 0, 2.30, {'Milk': 300, 'Coffee': 150})

    for product in product_repo:
        print(product)
    print(str(product_repo.find_by_id(2)))

    with open('database/products.json', 'w') as file:
        json.dump([eval(str(product)) for product in product_repo], file, indent=4)

    with open('database/employees.json', 'w') as file:
        json.dump([eval(str(employee)) for employee in user_repo], file, indent=4)

    order_repo = OrderRepository(IdGenerator())
    order_repo.create(Order('Ivan'))
    order_repo.create(Order('Petko'))
    order_repo.create(Order('Elena'))
    order_repo.delete_by_id(2)
    for order in order_repo:
        print(order)
    order_repo.update(1, 'cola', 'piece', 2, 2.50)
    order_repo.update(1, 'cola', 'piece', 2, 2.50)

    print(OrderDetails('cola', 'piece', 2, 2.50))

    print(order_repo.find_by_id(1))

    with open('database/orders.json', 'w') as file:
        json.dump([eval(str(order)) for order in order_repo], file, indent=4)

    receipt_repo = OrderRepository(IdGenerator())
    receipt_repo.create(CashReceipt('Ivan', 'Cash', [OrderDetails('cola', 'piece', 2, 3.50), OrderDetails('sok', 'piece', 7, 5)], 50))
    receipt_repo.create(CashReceipt('Petko', 'Card', [OrderDetails('fanta', 'piece', 2, 3), OrderDetails('water', 'piece', 5, 2)], 50))
    receipt_repo.create(CashReceipt('Elena', 'Cash', [OrderDetails('Beer', 'piece', 3, 3.50)], 50))
    receipt_repo.delete_by_id(1)
    for receipt in receipt_repo:
        print(receipt)

    with open('database/cash_receipts.json', 'w') as file:
        json.dump([eval(str(receipt)) for receipt in receipt_repo], file, indent=4)

    deliveries_repo = DeliveryRepository(IdGenerator())
    deliveries_repo.create(Delivery(100, 'Ivan', [DeliveryDetails('cola', 'piece', 2, 3.50, '2000.12.12'),
                                                  DeliveryDetails('juice', 'piece', 7, 3, '2001.12.12')], '2024.10.30', '12:56:23'))
    deliveries_repo.create(Delivery(125, 'Agria', [DeliveryDetails('Coffee', 'piece', 2, 3.50, '2000.12.12')],'2024.10.30',
                                    '12:56:23'))
    deliveries_repo.create(Delivery(165, 'Stoqn', [DeliveryDetails('fanta', 'piece', 2, 4.50, '2022.12.12'),
                                                   DeliveryDetails('fresh', 'piece', 7, 5, '2001.12.12')], '2024.7.30',
                                    '12:56:23'))

    deliveries_repo.delete_by_id(1)
    for delivery in deliveries_repo:
        print(delivery)

    with open('database/deliveries.json', 'w') as file:
        json.dump([eval(str(delivery)) for delivery in deliveries_repo], file, indent=4)
