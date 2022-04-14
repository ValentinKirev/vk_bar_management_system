import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from controllers.ingredient_controller import IngredientController
from utils.helpers import center_window
from views.commands.add_ingredient_command import AddIngredientCommand


class AddIngredientView(tk.Toplevel):
    def __init__(self, orders_view, operator, controller: IngredientController):
        super().__init__()
        self.controller = controller
        self.operator = operator
        self.controller.view = self
        self.orders_view = orders_view

        self.geometry('500x500')
        self.configure(background='lightblue')
        center_window(self)
        self.grab_set()

        self.frame = tk.Frame(self, background='lightblue')
        self.frame.grid()

        # add string vars
        self.ingredient_name = tk.StringVar()
        self.measure_unit = tk.StringVar()
        self.quantity = tk.StringVar()
        self.expiration_date = tk.StringVar()

        # add ingredient name entry and label
        self.ingredient_name_label = ttk.Label(self.frame, text='Enter ingredient name:', font='bold', background='lightblue')
        self.ingredient_name_label.grid(row=0, column=0, ipady=7)
        self.ingredient_name_entry = ttk.Entry(self.frame, textvariable=self.ingredient_name, width=25)
        self.ingredient_name_entry.grid(row=0, column=1, ipadx=20, ipady=3)

        # add ingredient measure unit entry and label
        self.measure_unit_label = ttk.Label(self.frame, text='Enter measure unit:', font='bold',
                                               background='lightblue')
        self.measure_unit_label.grid(row=1, column=0, ipady=7)
        self.measure_unit_entry = ttk.Entry(self.frame, textvariable=self.measure_unit, width=25)
        self.measure_unit_entry.grid(row=1, column=1, ipadx=20, ipady=3)

        # add quantity entry and label
        self.quantity_label = ttk.Label(self.frame, text='Enter quantity:', font='bold',
                                               background='lightblue')
        self.quantity_label.grid(row=2, column=0, ipady=7)
        self.quantity_entry = ttk.Entry(self.frame, textvariable=self.quantity, width=25)
        self.quantity_entry.grid(row=2, column=1, ipadx=20, ipady=3)

        # add expiration date entry and label
        self.expiration_date_label = ttk.Label(self.frame, text='Enter expiration date:', font='bold',
                                               background='lightblue')
        self.expiration_date_label.grid(row=3, column=0, ipady=7)
        self.expiration_date_entry = ttk.Entry(self.frame, textvariable=self.expiration_date, width=25)
        self.expiration_date_entry.grid(row=3, column=1, ipadx=20, ipady=3)

        # add string var for error message
        self.string_var = tk.StringVar()
        self.string_var_label = tk.Label(self.frame, textvariable=self.string_var, font='bold', background='lightblue',
                                         foreground='red')
        self.string_var_label.grid(row=4, column=1)

        # add add ingredient button
        self.add_ingredient = tk.Button(self.frame, text='ADD INGREDIENT', font='bold', width=25, background='green yellow',
                                        command=AddIngredientCommand(self.orders_view, self.operator, self.controller))
        self.add_ingredient.grid(row=5, column=1, ipady=5)

        self.empty_label = ttk.Label(self.frame, text='       ', background='lightblue')
        self.empty_label.grid(row=6, column=1, ipady=10)

        # add logo image
        self.logo_image = Image.open('database/logo.jpg').resize(size=(200, 200))
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.image_label = ttk.Label(self.frame, image=self.logo, background='lightblue')
        self.image_label.grid(row=7, column=1)