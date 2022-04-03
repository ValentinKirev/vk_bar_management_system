import tkinter as tk
from PIL import Image, ImageTk

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x800')
    root.title("VK Bar Management System")
    root.config(background='lightblue')
    ico = Image.open('database/logo.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    root.mainloop()
