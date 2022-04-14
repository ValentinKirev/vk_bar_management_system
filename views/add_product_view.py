import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from controllers.product_controller import ProductController
from utils.helpers import center_window
from views.commands.add_product_command import AddProductCommand
from views.commands.add_quantity_for_ingredient_command import AddQuantityForIngredientCommand


class AddProductView(tk.Toplevel):
    def __init__(self, orders_view, operator, controller: ProductController, ingredients=list()):
        super().__init__()
        self.controller = controller
        self.view = self
        self.ingredients = ingredients
        self.orders_view = orders_view
        self.operator = operator

        self.geometry('800x800')
        self.configure(background='lightblue')
        center_window(self)
        self.grab_set()

        self.frame = tk.Frame(self, background='lightblue')
        self.frame.grid(row=0, column=0)

        # add string vars
        self.product_name = tk.StringVar()
        self.product_type = tk.StringVar()
        self.measure_unit = tk.StringVar()
        self.quantity = tk.StringVar()
        self.price = tk.StringVar()

        # add product_name entry and label
        self.product_name_label = ttk.Label(self.frame, text='Enter product name:', font='bold', background='lightblue')
        self.product_name_label.grid(row=0, column=0, ipady=7)
        self.product_name_entry = ttk.Entry(self.frame, textvariable=self.product_name, width=25)
        self.product_name_entry.grid(row=0, column=1, ipadx=20, ipady=3)

        # add type entry and label
        self.product_type_label = ttk.Label(self.frame, text='Enter product type:', font='bold', background='lightblue')
        self.product_type_label.grid(row=1, column=0, ipady=7)
        self.product_type_entry = ttk.Entry(self.frame, textvariable=self.product_type, width=25)
        self.product_type_entry.grid(row=1, column=1, ipadx=20, ipady=3)

        # add ingredient measure unit entry and label
        self.measure_unit_label = ttk.Label(self.frame, text='Enter measure unit:', font='bold', background='lightblue')
        self.measure_unit_label.grid(row=2, column=0, ipady=7)
        self.measure_unit_entry = ttk.Entry(self.frame, textvariable=self.measure_unit, width=25)
        self.measure_unit_entry.grid(row=2, column=1, ipadx=20, ipady=3)

        # add quantity entry and label
        self.quantity_label = ttk.Label(self.frame, text='Enter quantity:', font='bold', background='lightblue')
        self.quantity_label.grid(row=3, column=0, ipady=7)
        self.quantity_entry = ttk.Entry(self.frame, textvariable=self.quantity, width=25)
        self.quantity_entry.grid(row=3, column=1, ipadx=20, ipady=3)

        # add price entry and label
        self.price_label = ttk.Label(self.frame, text='Enter price:', font='bold', background='lightblue')
        self.price_label.grid(row=5, column=0, ipady=7)
        self.price_entry = ttk.Entry(self.frame, textvariable=self.price, width=25)
        self.price_entry.grid(row=5, column=1, ipadx=20, ipady=3)

        self.empty_label = ttk.Label(self.frame, text='  ', background='lightblue')
        self.empty_label.grid(row=6, column=1)
        self.ingredients_label = ttk.Label(self.frame, text='Choose ingredients for the product:', font='bold', background='lightblue')
        self.ingredients_label.grid(row=7, column=0, columnspan=2)

        # add ingredients canvas
        self.ingredients_canvas = tk.Canvas(self, background='lightblue')
        self.ingredients_canvas.grid(row=1, column=0)

        self.controller.service.ingredients_repository.load()
        self.items = self.controller.service.ingredients_repository.find_all()
        self.item_pos_ids = None

        columns = ('Ingredient name', 'Measure unit', 'Quantity', 'Expiration date')
        self.tree = ttk.Treeview(self.ingredients_canvas, columns=columns, selectmode='extended', show='headings')
        for column in columns:
            self.tree.heading(column, text=column.title())
            self.tree.column(column, width=140)

        self.tree.grid(row=0, column=0, sticky="NSEW")

        # add vertical scrollbar
        vsb = ttk.Scrollbar(self.ingredients_canvas, orient="vertical", command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky='NWS', padx=0)
        self.tree.configure(yscrollcommand=vsb.set)

        # resize the parent window to show treeview widget

        self.tree.update_idletasks()
        self.rowconfigure(0, weight=1, minsize=self.tree.winfo_height())
        self.columnconfigure(0, weight=1, minsize=self.tree.winfo_width())
        # set items
        self.set_items(self.items)

        self.second_frame = tk.Frame(self, background='lightblue')
        self.second_frame.grid(row=2, column=0)

        self.current_ingredient = None

        self.add_ingredients_button = tk.Button(self.second_frame, text='Add ingredients to product',
                                                background='green yellow',
                                                command=AddQuantityForIngredientCommand(self.orders_view, self.operator,
                                                                     self.controller, self.ingredients, self.view))
        self.add_ingredients_button.grid(row=0, column=1)
        # add string var for error message
        self.string_var = tk.StringVar()
        self.string_var_label = tk.Label(self.second_frame, textvariable=self.string_var, font='bold', background='lightblue',
                                         foreground='red')
        self.string_var_label.grid(row=1, column=1, sticky='EW')

        # add product button
        self.add_product_button = tk.Button(self.second_frame, text='ADD PRODUCT', font='bold', width=25,
                                        background='green yellow', command=AddProductCommand(self.orders_view,
                                                self.operator, self.controller, self.ingredients, self.view))
        self.add_product_button.grid(row=2, column=1, ipady=5)

        # add logo image
        self.logo_image = Image.open('database/logo.jpg').resize(size=(150, 150))
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.image_label = ttk.Label(self.second_frame, image=self.logo, background='lightblue')
        self.image_label.grid(row=3, column=1)

    def set_items(self, items):
        def set_item(item):
            values = list(item.__dict__.values())
            for i, val in enumerate(values):
                if isinstance(val, (list, tuple)):
                    values[i] = ', '.join(val)
            return self.tree.insert('', 'end',  values=tuple(values))

        if self.item_pos_ids is not None:
            self.tree.delete(*self.item_pos_ids)
        self.items = items
        self.item_pos_ids = list(map(set_item, self.items))
        self.update_idletasks()
        self.tree.see(self.item_pos_ids[-1])

    def get_selected_items(self):
        selected_item = self.tree.focus()
        ingredient_name = self.tree.item(selected_item)['values'][0]
        return ingredient_name