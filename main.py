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
from repositories.cash_receipt_repository import CashReceiptRepository
from repositories.delivery_repository import DeliveryRepository
from repositories.employees_repository import EmployeesRepository
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository


if __name__ == '__main__':
    user_repo = EmployeesRepository(IdGenerator(),'database/employees.json')
    user_repo.create(Employee('Ivan', 'Petkov', 'IvPet', 'Ivpetkov1'))
    user_repo.create(HallManager('Stefan', 'Ivanov', 'Stefoto', 'Stefan123'))
    user_repo.create(Manager('Dobri', 'Kostadinov', 'Dobata', 'Manager1'))

    for employee in user_repo:
        print(employee)

    user_repo.delete_by_id(2)
    user_repo.update('Dobata', 'Bartender')
    user_repo.save()
    for employee in user_repo:
        print(employee)

    product_repo = ProductRepository(IdGenerator(), 'database/products.json')
    product_repo.create(BaseProduct('Corona', 'Beer', 'piece', 24, '2024.10.08', 4.99))
    product_repo.create(ComplexProduct('Cappuccino', 'Hot Drink', 'piece', 5, '2024.10.08', 14.99, {'Milk': 200, 'Coffee': 100}))
    product_repo.create(BaseProduct('Coca cola', 'Non alcohol drink', 'piece', 120, '2023.12.08', 4.99))

    product_repo.delete_by_id(1)
    print(product_repo.find_by_id(3))
    print(product_repo.find_by_name('Cappuccino'))
    print(product_repo.find_all())
    product_repo.update('Cappuccino', 'mix', 'milliliters', 0, 2.30, {'Milk': 300, 'Coffee': 150})
    for product in product_repo:
        print(product)

    product_repo.save()

    order_repo = OrderRepository(IdGenerator(), 'database/orders.json')
    order_repo.create(Order('Ivan'))
    order_repo.create(Order('Petko'))
    order_repo.create(Order('Elena'))

    print(order_repo.find_by_id(1))
    order_repo.delete_by_id(2)
    for order in order_repo:
        print(order)
    order_repo.update(1, 'cola', 'piece', 2, 2.50)
    order_repo.update(1, 'juice', 'piece', 2, 2.50)
    order_repo.update(1, 'juice', 'piece', 2, 2)
    order_repo.save()

    receipt_repo = CashReceiptRepository(IdGenerator(), 'database/cash_receipts.json')
    receipt_repo.create(CashReceipt('Ivan', 'Cash', [OrderDetails('cola', 'piece', 2, 3.50), OrderDetails('sok', 'piece', 7, 5)], 50))
    receipt_repo.create(CashReceipt('Petko', 'Card', [OrderDetails('fanta', 'piece', 2, 3), OrderDetails('water', 'piece', 5, 2)], 50))
    receipt_repo.create(CashReceipt('Elena', 'Cash', [OrderDetails('Beer', 'piece', 3, 3.50)], 50))
    receipt_repo.save()
    receipt_repo.delete_by_id(1)
    for receipt in receipt_repo:
        print(receipt)

    deliveries_repo = DeliveryRepository(IdGenerator(), 'database/deliveries.json')
    deliveries_repo.create(Delivery(100, 'Ivan', [DeliveryDetails('cola', 'piece', 2, 3.50, '2000.12.12'),
                                                  DeliveryDetails('juice', 'piece', 7, 3, '2001.12.12')], '2024.10.30', '12:56:23'))
    deliveries_repo.create(Delivery(125, 'Agria', [DeliveryDetails('Coffee', 'piece', 2, 3.50, '2000.12.12')],'2024.10.30',
                                    '12:56:23'))
    deliveries_repo.create(Delivery(165, 'Stoqn', [DeliveryDetails('fanta', 'piece', 2, 4.55, '2022.12.12'),
                                                   DeliveryDetails('fresh', 'piece', 7, 5, '2001.12.12')], '2024.7.30',
                                    '12:56:23'))

    deliveries_repo.update(100, 'Pesho', [DeliveryDetails('juice', 'piece', 3, 3.33, '2000.12.10')], '2022.10.20', '12:33:33')
    print(deliveries_repo.find_by_delivery_number(100))
    deliveries_repo.delete_by_id(2)
    for delivery in deliveries_repo:
        print(delivery)
    deliveries_repo.save()