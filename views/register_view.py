import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from controllers.main_controller import MainController
from views.commands.register_command import RegisterCommand


class RegisterView(tk.Canvas):
    def __init__(self, controller: MainController):
        super().__init__()
        self.controller = controller
        self.controller.view = self

        # add string vars
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.username = tk.StringVar()
        self.role = tk.StringVar()
        self.password = tk.StringVar()
        self.confirm_password = tk.StringVar()
        self.service_password = tk.StringVar()

        # add first name entry and label
        self.first_name_label = ttk.Label(self.master, text='Enter first name:', font='bold', background='lightblue')
        self.first_name_label.grid(row=2, column=1, ipady=7)
        self.first_name_entry = ttk.Entry(self.master, textvariable=self.first_name, width=25)
        self.first_name_entry.grid(row=2, column=2, ipadx=20, ipady=3)

        # add last name entry and label
        self.last_name_label = ttk.Label(self.master, text='Enter last name:', font='bold', background='lightblue')
        self.last_name_label.grid(row=3, column=1, ipady=7)
        self.last_name_entry = ttk.Entry(self.master, textvariable=self.last_name, width=25)
        self.last_name_entry.grid(row=3, column=2, ipadx=20, ipady=3)

        # add username entry and label
        self.username_label = ttk.Label(self.master, text='Enter username:', font='bold', background='lightblue')
        self.username_label.grid(row=4, column=1, ipady=7)
        self.username_entry = ttk.Entry(self.master, textvariable=self.username, width=25)
        self.username_entry.grid(row=4, column=2, ipadx=20, ipady=3)

        # add role entry and label
        self.role_label = ttk.Label(self.master, text='Enter role:', font='bold', background='lightblue')
        self.role_label.grid(row=5, column=1, ipady=7)
        self.role_entry = ttk.Entry(self.master, textvariable=self.role, width=25)
        self.role_entry.grid(row=5, column=2, ipadx=20, ipady=3)

        # add password entry and label
        self.password_label = ttk.Label(self.master, text='Enter password:', font='bold', background='lightblue')
        self.password_label.grid(row=6, column=1, ipady=7)
        self.password_entry = ttk.Entry(self.master, textvariable=self.password, width=25, show='*')
        self.password_entry.grid(row=6, column=2, ipadx=20, ipady=3)

        # add confirm password entry and label
        self.confirm_password_label = ttk.Label(self.master, text='Confirm password:', font='bold',
                                                background='lightblue')
        self.confirm_password_label.grid(row=7, column=1, ipady=7)
        self.confirm_password_entry = ttk.Entry(self.master, textvariable=self.confirm_password, width=25, show='*')
        self.confirm_password_entry.grid(row=7, column=2, ipadx=20, ipady=3)

        # add service password entry and label
        self.service_password_label = ttk.Label(self.master, text='Enter service password:', font='bold',
                                                background='lightblue')
        self.service_password_label.grid(row=8, column=1, ipady=7)
        self.service_password_entry = ttk.Entry(self.master, textvariable=self.service_password, width=25, show='*')
        self.service_password_entry.grid(row=8, column=2, ipadx=20, ipady=3)

        # add string var for error message
        self.string_var = tk.StringVar()
        self.string_var_label = tk.Label(self.master, textvariable=self.string_var, font='bold', background='lightblue',
                                         foreground='red')
        self.string_var_label.grid(row=9, column=2)

        # add button
        self.register_button = tk.Button(self.master, text='REGISTER', font='bold', width=25, background='green yellow',
                                         command=RegisterCommand(self.controller, self.master))
        self.register_button.grid(row=10, column=2, ipady=5)

        self.empty_label = ttk.Label(text='    ', background='lightblue')
        self.empty_label.grid(row=11, column=2)

        # add logo image
        self.logo_image = Image.open('database/logo.jpg').resize(size=(300, 300))
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.image_label = ttk.Label(image=self.logo, background='lightblue')
        self.image_label.grid(row=12, column=2)