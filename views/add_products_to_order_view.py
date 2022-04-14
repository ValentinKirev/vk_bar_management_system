import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from controllers.order_controller import OrderController
from utils.helpers import center_window



class AddProductsToOrderView(tk.Toplevel):
    def __init__(self, product_name, price, controller: OrderController):
        super().__init__()
        self.product_name = product_name
        self.price = price
        self.controller = controller

        self.geometry('320x250')
        self.configure(background='lightblue')
        center_window(self)
        self.grab_set()

        self.quantity = tk.StringVar()
        self.frame = tk.Frame(self, background='lightblue')
        self.frame.grid(row=0, column=0)

        self.label = ttk.Label(self.frame, text='Enter quantity:', background='lightblue')
        self.label.grid(row=0, column=0)
        self.entry = ttk.Entry(self.frame, textvariable=self.quantity, width=15)
        self.entry.grid(row=0, column=1)

        # add string var for error message
        self.string_var = tk.StringVar()
        self.string_var_label = tk.Label(self.frame, textvariable=self.string_var, font='bold',
                                         background='lightblue',
                                         foreground='red')
        self.string_var_label.grid(row=1, column=1, sticky='EW')

        self.submit_button = tk.Button(self.frame, text='SUBMIT', background='green yellow')

        self.submit_button.grid(row=2, column=1)

        # add logo image
        self.logo_image = Image.open('database/logo.jpg').resize(size=(150, 150))
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.image_label = ttk.Label(self.frame, image=self.logo, background='lightblue')
        self.image_label.grid(row=3, column=1)