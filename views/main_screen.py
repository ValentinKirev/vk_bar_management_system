import tkinter as tk

from PIL import Image, ImageTk


class MainScreen(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master

        self.logo_image = Image.open('database/logo.jpg')
        self.logo = ImageTk.PhotoImage(self.logo_image)
