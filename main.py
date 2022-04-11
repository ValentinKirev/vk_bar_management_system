import tkinter as tk
from PIL import Image, ImageTk


from controllers.main_controller import MainController
from controllers.order_controller import OrderController
from repositories.cash_receipt_repository import CashReceiptRepository
from repositories.deliveries_repository import DeliveryRepository
from repositories.employees_repository import EmployeesRepository
from repositories.ingredients_repository import IngredientRepository
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from services.cash_receipt_service import CashReceiptService
from services.delivery_service import DeliveryService
from services.employee_service import EmployeeService
from services.ingredient_service import IngredientService
from services.login_service import LoginService
from services.order_service import OrderService
from services.product_service import ProductService
from services.register_service import RegisterService
from utils.helpers import center_window
from utils.id_generator import IdGenerator
from views.main_view import MainView


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('600x600')
    root.title("VK Bar Management System")
    root.config(background='lightblue')
    ico = Image.open('database/logo.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    employees_repo = EmployeesRepository(IdGenerator(), 'database/employees.json')
    ingredients_repo = IngredientRepository(IdGenerator(), 'database/ingredients.json')
    products_repo = ProductRepository(IdGenerator(), 'database/products.json')
    cash_receipt_repo = CashReceiptRepository(IdGenerator(), 'database/cash_receipts.json')
    orders_repo = OrderRepository(IdGenerator(), 'database/orders.json')
    deliveries_repo = DeliveryRepository(IdGenerator(), 'database/deliveries.json')

    employees_service = EmployeeService(employees_repo)
    ingredients_service = IngredientService(ingredients_repo)
    products_service = ProductService(products_repo, ingredients_repo)
    cash_receipt_service = CashReceiptService(cash_receipt_repo, ingredients_repo, products_repo, orders_repo)
    orders_service = OrderService(orders_repo, products_repo)
    deliveries_service = DeliveryService(deliveries_repo, ingredients_repo)
    register_service = RegisterService(employees_repo)
    login_service = LoginService(employees_repo)

    main_controller = MainController(register_service, login_service)
    order_controller = OrderController(orders_service)

    main_view = MainView(root, main_controller)
    center_window(root)
    root.mainloop()
