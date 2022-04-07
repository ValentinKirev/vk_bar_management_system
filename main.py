import tkinter as tk
from PIL import Image, ImageTk

from utils.helpers import center_window
from views.main_view import MainView

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('700x800')
    root.title("VK Bar Management System")
    root.config(background='lightblue')
    ico = Image.open('database/logo.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    main_view = MainView(root)
    center_window(root)
    root.mainloop()
