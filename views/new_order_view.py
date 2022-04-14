import tkinter as tk
from tkinter import ttk

from controllers.order_controller import OrderController
from utils.helpers import center_window
from views.commands.add_products_to_order_command import AddProductsToOrderCommand


class NewOrderView(tk.Toplevel):
    def __init__(self, controller: OrderController):
        super().__init__()
        self.controller = controller
        self.controller.view = self

        self.geometry('1000x600')
        self.configure(background='lightblue')
        center_window(self)
        self.grab_set()

        self.controller.service.product_repository.load()
        self.items = self.controller.service.product_repository.find_all()
        self.item_pos_ids = None

        self.products_canvas = tk.Canvas(self, background='lightblue')
        self.products_canvas.grid(row=0, column=0)

        columns = ('Product name', 'Product type', 'Measure unit', 'Quantity', 'Price', 'Ingredients')
        self.tree = ttk.Treeview(self.products_canvas, columns=columns, selectmode='extended', show='headings')
        for column in columns:
            self.tree.heading(column, text=column.title())
            self.tree.column(column, width=140)

        self.tree.grid(row=0, column=0, sticky="NSEW")

        # add vertical scrollbar
        vsb = ttk.Scrollbar(self.products_canvas, orient="vertical", command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky='NWS', padx=0)
        self.tree.configure(yscrollcommand=vsb.set)

        self.add_product_button = tk.Button(self.products_canvas, text='Add product to order', background='green yellow')
        self.add_product_button.grid(row=1, column=0)
        # resize the parent window to show treeview widget

        self.tree.update_idletasks()
        self.rowconfigure(0, weight=1, minsize=self.tree.winfo_height())
        self.columnconfigure(0, weight=1, minsize=self.tree.winfo_width())
        # set items
        self.set_items(self.items)

    def set_items(self, items):
        def set_item(item):
            values = list(item.__dict__.values())
            for i, val in enumerate(values):
                result = ''
                if isinstance(val, (list, tuple)):
                    for element in val:
                        if isinstance(element, (list, tuple)):
                            result += ', '.join(str(x) for x in element)
                    values[i] = result
            return self.tree.insert('', 'end', values=tuple(values))

        if self.item_pos_ids is not None:
            self.tree.delete(*self.item_pos_ids)
        self.items = items
        self.item_pos_ids = list(map(set_item, self.items))
        self.update_idletasks()
        self.tree.see(self.item_pos_ids[-1])

    def get_selected_items(self):
        selected_item = self.tree.focus()
        ingredient_name = self.tree.item(selected_item)['values'][0]
        price = self.tree.item(selected_item)['values'][4]
        return ingredient_name, price