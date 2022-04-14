import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from controllers.main_controller import MainController
from views.commands.login_command import LoginCommand


class LoginView(tk.Canvas):
    def __init__(self, controller: MainController):
        super().__init__()
        self.controller = controller
        self.controller.view = self

        # add string vars
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # add username entry and label
        self.username_label = ttk.Label(self.master, text='Username:', font='bold', background='lightblue', width=15)
        self.username_label.grid(row=1, column=1, ipady=7)
        self.username_entry = ttk.Entry(self.master, textvariable=self.username, width=30)
        self.username_entry.grid(row=1, column=2, ipadx=20, ipady=3)

        # add password entry and label
        self.password_label = ttk.Label(self.master, text='Password:', font='bold', background='lightblue', width=15)
        self.password_label.grid(row=2, column=1, ipady=7)
        self.username_entry = ttk.Entry(self.master, textvariable=self.password, width=30, show='*')
        self.username_entry.grid(row=2, column=2, ipadx=20, ipady=3)

        # add string var for error message
        self.string_var = tk.StringVar()
        self.string_var_label = tk.Label(self.master, textvariable=self.string_var, font='bold', background='lightblue',
                                         foreground='red')
        self.string_var_label.grid(row=3, column=2)

        # add buttons
        self.login_button = tk.Button(self.master, text='LOGIN', font='bold', width=30, background='green yellow',
                                      command=LoginCommand(self.controller, self.master))
        self.login_button.grid(row=4, column=2, ipady=5)

        self.empty_label = ttk.Label(text='', background='lightblue')
        self.empty_label.grid(row=5, column=2, ipady=50)

        # add logo image
        self.logo_image = Image.open('database/logo.jpg').resize(size=(300, 300))
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.image_label = ttk.Label(image=self.logo, background='lightblue')
        self.image_label.grid(row=6, column=2)
