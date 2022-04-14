import tkinter as tk
from tkinter import ttk

from controllers.ingredient_controller import IngredientController
from controllers.order_controller import OrderController
from controllers.product_controller import ProductController
from repositories.ingredients_repository import IngredientRepository
from repositories.orders_repository import OrderRepository
from repositories.products_repository import ProductRepository
from services.ingredient_service import IngredientService
from services.order_service import OrderService
from services.product_service import ProductService
from utils.id_generator import IdGenerator
from views.commands.create_order_command import CreateOrderCommand
from utils.helpers import center_window
from views.commands.render_add_ingredient_command import RenderAddIngredientCommand
from views.commands.render_add_product_command import RenderAddProductCommand


class OrdersView(tk.Toplevel):
    def __init__(self, operator, controller=OrderController(OrderService(OrderRepository(IdGenerator(), 'database/orders.json'),
                                                    ProductRepository(IdGenerator(), 'database/products.json')))):
        super().__init__()
        self.geometry('600x600')
        self.configure(background='lightblue')
        center_window(self)

        self.operator = operator
        self.controller = controller
        self.controller.view = self

        self.frame = tk.Frame(self, background='lightblue')
        self.frame.grid()

        # add menu
        if operator.role == "Manager" or "HallManager":
            menubar = tk.Menu(self)
            self.config(menu=menubar)

            if operator.role == "Manager":
                ingredients = tk.Menu(menubar, tearoff=False)
                menubar.add_cascade(menu=ingredients, label='INGREDIENTS')
                ingredients.add_command(label='Add ingredient', command=RenderAddIngredientCommand(self, self.operator,
                    IngredientController(IngredientService(IngredientRepository(IdGenerator(),
                                                                                'database/ingredients.json'),))))
                products = tk.Menu(menubar, tearoff=False)
                menubar.add_cascade(menu=products, label='PRODUCTS')
                products.add_command(label='Add product', command=RenderAddProductCommand(self, self.operator,
                    ProductController(ProductService(ProductRepository(IdGenerator(), 'database/products.json'),
                                                     IngredientRepository(IdGenerator(), 'database/ingredients.json')))))
                accounts = tk.Menu(menubar, tearoff=False)
                menubar.add_cascade(menu=accounts, label='ACCOUNTS')

            deliveries = tk.Menu(menubar, tearoff=False)
            menubar.add_cascade(menu=deliveries, label='DELIVERIES')
            cash_receipts = tk.Menu(menubar, tearoff=False)
            menubar.add_cascade(menu=cash_receipts, label='CASH RECEIPTS')
            revision = tk.Menu(menubar, tearoff=False)
            menubar.add_cascade(menu=revision, label='MAKE REVISION')

        column = 0
        row = 0
        for table in range(1, 10):
            label_row = row
            table_number_label = ttk.Label(self.frame, text=f"Table {table}", font='bold', background='lightblue')
            table_number_label.grid(row=label_row, column=column)

            taken_tables = self.get_taken_tables()
            if table not in taken_tables:
                create_update_order_button = tk.Button(self.frame, text='Open new order', font='bold', background='green yellow',
                                                 command=CreateOrderCommand(self.controller, table))
            else:
                create_update_order_button = tk.Button(self.frame, text='Update order', font='bold', background='green yellow',
                                                     command=CreateOrderCommand(self.controller, table))

                issue_cash_receipt_button = tk.Button(self.frame, text='Issue cash receipt', font='bold', background='green yellow',
                                                      command=lambda: print('cash receipt created'))
                issue_cash_receipt_button.grid(row=label_row + 2, column=column, ipadx=30)
            create_update_order_button.grid(row=label_row + 1, column=column, ipadx=30)

            empty_label = ttk.Label(self.frame, text='        ', background='lightblue')
            empty_label.grid(row=label_row + 2, column=column, ipady=25)

            column += 1
            if column == 3:
                row += 3
                column = 0

    def get_taken_tables(self):
        self.controller.reload_orders()
        orders = self.controller.orders_service.get_all_orders()
        taken_tables = [order.table_number for order in orders]
        return taken_tables
