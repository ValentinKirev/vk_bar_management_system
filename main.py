import tkinter as tk
from PIL import Image, ImageTk


from controllers.main_controller import MainController
from repositories.employees_repository import EmployeesRepository
from services.login_service import LoginService
from services.register_service import RegisterService
from utils.helpers import center_window
from utils.id_generator import IdGenerator
from views.main_view import MainView


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('600x600')
    root.title("VK Bar Management System")
    root.config(background='lightblue')
    ico = Image.open('database/logo.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    employees_repo = EmployeesRepository(IdGenerator(), 'database/employees.json')

    register_service = RegisterService(employees_repo)
    login_service = LoginService(employees_repo)

    main_controller = MainController(register_service, login_service)

    main_view = MainView(root, main_controller)
    center_window(root)
    root.mainloop()