def dumper(entity):
    return entity.to_json()


def object_hook(jsdict):
    entity_module_name = jsdict['_module']
    entity_class_name = jsdict['_class']
    module = __import__(entity_module_name, fromlist=[entity_class_name])
    cls = getattr(module, entity_class_name)
    return cls.from_json(jsdict)


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - win_width // 2
    y = window.winfo_screenheight() // 2 - win_height // 2
    window.geometry(f'{width}x{height}+{x}+{y}')
    window.deiconify()


def destroy_widgets(window):
    for child in window.winfo_children():
        child.destroy()

