import tkinter as tk
import importlib
import sys
import time
from client.products import ProductsFrame
  # Assuming ProductsFrame is correctly imported

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x600')

        # Menu and Navigation Setup
        self.create_menu()

        # Placeholder for current frame
        self.current_frame = None

    def create_menu(self):
        # Example menu creation
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        products_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Products', menu=products_menu)
        products_menu.add_command(label='View Products', command=self.show_products_frame)

        # Add other menus and commands for users, orders, etc.

    def show_products_frame(self):
        # Show ProductsFrame when Products menu item is clicked
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = ProductsFrame(self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

def run_with_autoreload(module_name):
    while True:
        try:
            module = importlib.import_module(module_name)
            importlib.reload(module)
            print(f'Reloaded {module_name} at {time.strftime("%H:%M:%S")}')
        except Exception as e:
            print(f'Error reloading {module_name}: {e}')
        time.sleep(1)  # Adjust sleep time as needed

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
