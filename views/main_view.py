import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from controllers.main_controller import MainController
from views.commands.render_login_command import RenderLoginCommand
from views.commands.render_register_command import RenderRegisterCommand


class MainView(tk.Frame):
    def __init__(self, master, controller: MainController):
        super().__init__()
        self.master = master
        self.controller = controller

        # add logo
        self.logo_image = Image.open('database/logo.jpg').resize(size=(450, 450))
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.image_label = ttk.Label(image=self.logo, background='lightblue')
        self.image_label.pack()

        # buttons
        self.login_button = tk.Button(text='LOGIN', font='bold', width=20, background='green yellow',
                                      command=RenderLoginCommand(self.master, self.controller))
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(text='REGISTER', font='bold', width=20, background='green yellow',
                                         command=RenderRegisterCommand(self.master, self.controller))
        self.register_button.pack()

        self.about = tk.Button(text='ABOUT', font='bold', width=10, background='green yellow')
        self.about.pack(side='right', anchor='s')

        self.about = tk.Button(text='HELP', font='bold', width=10, background='green yellow')
        self.about.pack(side='left', anchor='s')
