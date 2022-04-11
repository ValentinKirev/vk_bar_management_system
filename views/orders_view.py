import tkinter as tk
from tkinter import ttk
from controllers.main_controller import MainController
from controllers.order_controller import OrderController
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from services.order_service import OrderService
from utils.id_generator import IdGenerator
from views.commands.create_order_command import CreateOrderCommand


order_controller = OrderController(OrderService(OrderRepository(IdGenerator(), 'database/orders.json'),
                                                    ProductRepository(IdGenerator(), 'database/products.json')))

class OrdersView(tk.Canvas):
    def __init__(self, controller: MainController):
        super().__init__()
        self.controller = controller
        self.operator = self.controller.login_service.get_current_logged_user()
        self.controller = order_controller
        self.controller.view = self

        column = 0
        row = 0
        for table in range(1, 10):
            label_row = row
            self.table_number_label = ttk.Label(text=f"Table {table}", font='bold', background='lightblue')
            self.table_number_label.grid(row=label_row, column=column)

            taken_tables = self.get_taken_tables()
            if table not in taken_tables:
                self.create_update_order_button = tk.Button(text='Open new order', font='bold', background='green yellow',
                                                 command=CreateOrderCommand(self.controller, table))
            else:
                self.create_update_order_button = tk.Button(text='Update order', font='bold', background='green yellow',
                                                     command=CreateOrderCommand(self.controller, table))
            self.create_update_order_button.grid(row=label_row + 1, column=column, ipadx=30)

            self.empty_label = ttk.Label(text='        ', background='lightblue')
            self.empty_label.grid(row=label_row + 2, column=column, ipady=25)

            column += 1
            if column == 3:
                row += 3
                column = 0

    def get_taken_tables(self):
        orders = self.controller.orders_service.get_all_orders()
        taken_tables = [order.table_number for order in orders]
        return taken_tables
