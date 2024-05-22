import tkinter as tk
from tkinter import ttk, messagebox
from app.services.api_products import fetch_all_products, create_product
class ProductsFrame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=500, height=500,)
        self.root = root
        self.pack(expand=True, fill=tk.BOTH)

        self.products()
        self.deactivate_input()
        self.table_product()

    def products(self):
        # --------------labels-----------------
        self.label_name = tk.Label(self, text='Name:')
        self.label_name.config(font=('Arial', 12, 'bold'))
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.label_model = tk.Label(self, text='Model:')
        self.label_model.config(font=('Arial', 12, 'bold'))
        self.label_model.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.label_manufacture = tk.Label(self, text='Manufacture:')
        self.label_manufacture.config(font=('Arial', 12, 'bold'))
        self.label_manufacture.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        
        self.label_price = tk.Label(self, text='price:')
        self.label_price.config(font=('Arial', 12, 'bold'))
        self.label_price.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        
        self.label_stock = tk.Label(self, text='stock:')
        self.label_stock.config(font=('Arial', 12, 'bold'))
        self.label_stock.grid(row=4, column=0, padx=10, pady=10, sticky=tk.E)
        
        self.label_IMG = tk.Label(self, text='IMG:')
        self.label_IMG.config(font=('Arial', 12, 'bold'))
        self.label_IMG.grid(row=5, column=0, padx=10, pady=10, sticky=tk.E)
        
        self.label_feature = tk.Label(self, text='feature:')
        self.label_feature.config(font=('Arial', 12, 'bold'))
        self.label_feature.grid(row=6, column=0, padx=10, pady=10, sticky=tk.E)

        # --------------Inputs-----------------
        self.my_name = tk.StringVar()
        self.entry_name = tk.Entry(self, textvariable=self.my_name)
        self.entry_name.config(width=50, font=('Arial', 12))
        self.entry_name.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky=tk.W)

        self.my_model = tk.StringVar()
        self.entry_model = tk.Entry(self, textvariable=self.my_model)
        self.entry_model.config(width=50, font=('Arial', 12))
        self.entry_model.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky=tk.W)

        self.my_manufature = tk.StringVar()
        self.entry_manufature = tk.Entry(self, textvariable=self.my_manufature)
        self.entry_manufature.config(width=50, font=('Arial', 12))
        self.entry_manufature.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky=tk.W)
        
        self.my_price = tk.StringVar()
        self.entry_price = tk.Entry(self, textvariable=self.my_price)
        self.entry_price.config(width=50, font=('Arial', 12))
        self.entry_price.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky=tk.W)

        self.my_stock = tk.StringVar()
        self.entry_stock = tk.Entry(self, textvariable=self.my_stock)
        self.entry_stock.config(width=50, font=('Arial', 12))
        self.entry_stock.grid(row=4, column=1, padx=10, pady=10, columnspan=2, sticky=tk.W)

        self.my_IMG = tk.StringVar()
        self.entry_IMG = tk.Entry(self, textvariable=self.my_IMG)
        self.entry_IMG.config(width=50, font=('Arial', 12))
        self.entry_IMG.grid(row=5, column=1, padx=10, pady=10, columnspan=2, sticky=tk.W)
        
        self.my_feature = tk.StringVar()
        self.entry_feature = tk.Entry(self, textvariable=self.my_feature)
        self.entry_feature.config(width=50, font=('Arial', 12))
        self.entry_feature.grid(row=6, column=1, padx=10, pady=10, columnspan=2, sticky=tk.W)

        # --------------buttons-----------------
        # btn new
        self.button_new = tk.Button(self, text="New", command=self.activate_input)
        self.button_new.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.button_new.grid(row=7, column=0, padx=10, pady=10)

        # btn save
        self.button_save = tk.Button(self, text="Save", command=self.save_data)
        self.button_save.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.button_save.grid(row=7, column=1, padx=10, pady=10)

        # btn cancel
        self.button_cancel = tk.Button(self, text="Cancel", command=self.deactivate_input)
        self.button_cancel.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.button_cancel.grid(row=7, column=2, padx=10, pady=10)

    def activate_input(self):
        self.entry_name.config(state='normal')
        self.entry_model.config(state='normal')
        self.entry_manufature.config(state='normal')
        self.entry_price.config(state='normal')
        self.entry_stock.config(state='normal')
        self.entry_IMG.config(state='normal')
        self.entry_feature.config(state='normal')

        self.button_new.config(state='normal')
        self.button_save.config(state='normal')
        self.button_cancel.config(state='normal')

    def deactivate_input(self):
        self.my_name.set('')
        self.my_model.set('')
        self.my_manufature.set('')
        self.my_price.set('')
        self.my_stock.set('')
        self.my_IMG.set('')
        self.my_feature.set('')
        

        self.entry_name.config(state='disabled')
        self.entry_model.config(state='disabled')
        self.entry_manufature.config(state='disabled')
        self.entry_price.config(state='disabled')
        self.entry_stock.config(state='disabled')
        self.entry_IMG.config(state='disabled')
        self.entry_feature.config(state='disabled')

        self.button_save.config(state='disabled')
        self.button_cancel.config(state='disabled')

    def save_data(self):
    # Get data from input fields
        product_data = {
            'product_name': self.my_name.get(),
            'product_model': self.my_model.get(),
            'manufacturer': self.my_manufature.get(),
            'price': self.my_price.get(),
            'stock_on_hand': self.my_stock.get(),
            'img_url': self.my_IMG.get(),
            'feature_id': self.my_feature.get()
        }
    
        # Call create_product function
        response = create_product(product_data)
        print("Response from create_product:", response)  # Debug statement
    
        if response and 'message' in response:
            messagebox.showinfo("Product Created", response['message'])  # Show success message
            self.populate_table()  # Update table with new data
        else:
            messagebox.showerror("Error", "Failed to create product. Check server logs.")  # Show error message
    
        self.deactivate_input()


    def table_product(self):
        self.table = ttk.Treeview(self, columns=(
            'product_name',
            'product_model',
            'manufacturer',
            'price',
            'stock_on_hand',
            'img_url',
            'feature_id'
            )
        )
        self.table.grid(row=8, column=0, columnspan=4, sticky=tk.NSEW)

        self.table.heading('#0', text='ID')
        self.table.heading('#1', text='NAME')
        self.table.heading('#2', text='MODEL')
        self.table.heading('#3', text='MANUFACTURER')
        self.table.heading('#4', text='PRICE')
        self.table.heading('#5', text='STOCK')
        self.table.heading('#6', text='IMAGE URL')
        self.table.heading('#7', text='FEATURE ID')

        self.button_edit = tk.Button(self, text="Edit")
        self.button_edit.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.button_edit.grid(row=9, column=0, padx=10, pady=10)

        self.button_delete = tk.Button(self, text="Delete")
        self.button_delete.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.button_delete.grid(row=9, column=1, padx=10, pady=10)

        self.populate_table()

    def populate_table(self):
        self.table.delete(*self.table.get_children())  # Clear existing data
        data = fetch_all_products()
        if data and 'data' in data:
            for item in data['data']:
                self.table.insert('', 'end', text=item.get('product_id', ''),
                                    values=(
                                        item.get('product_name', ''), 
                                        item.get('product_model', ''), 
                                        item.get('manufacturer', ''), 
                                        item.get('price', ''), 
                                        item.get('stock_on_hand', ''), 
                                        item.get('img_url', ''), 
                                        item.get('feature_id', '')
                                    )
                                )