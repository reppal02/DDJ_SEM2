import tkinter as tk
from tkinter import messagebox

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class CashierApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gramedia")
        
        self.items = []

        self.create_widgets()

    def create_widgets(self):
        # Item name label and entry
        self.item_name_label = tk.Label(self.master, text="Item Name:")
        self.item_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.item_name_entry = tk.Entry(self.master)
        self.item_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Item price label and entry
        self.item_price_label = tk.Label(self.master, text="Item Price:")
        self.item_price_label.grid(row=1, column=0, padx=5, pady=5)
        self.item_price_entry = tk.Entry(self.master)
        self.item_price_entry.grid(row=1, column=1, padx=5, pady=5)

        # Item quantity label and entry
        self.item_quantity_label = tk.Label(self.master, text="Item Quantity:")
        self.item_quantity_label.grid(row=2, column=0, padx=5, pady=5)
        self.item_quantity_entry = tk.Entry(self.master)
        self.item_quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        # Add item button
        self.add_item_button = tk.Button(self.master, text="Add Item", command=self.add_item)
        self.add_item_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Receipt text widget
        self.receipt_text = tk.Text(self.master, height=10, width=40)
        self.receipt_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Print receipt button
        self.print_receipt_button = tk.Button(self.master, text="Print Receipt", command=self.print_receipt)
        self.print_receipt_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def add_item(self):
        name = self.item_name_entry.get()
        price = float(self.item_price_entry.get())
        quantity = int(self.item_quantity_entry.get())
        item = Item(name, price, quantity)
        self.items.append(item)
        messagebox.showinfo("Success", "Item added successfully!")

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items)
        return total

    def print_receipt(self):
        self.receipt_text.delete('1.0', tk.END)
        self.receipt_text.insert(tk.END, "=== Speed Shop Receipt ===\n")
        for item in self.items:
            self.receipt_text.insert(tk.END, f"{item.name}: Rp{item.price} x {item.quantity}\n")
        self.receipt_text.insert(tk.END, f"Total: Rp{self.calculate_total()}\n")

def main():
    root = tk.Tk()
    app = CashierApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
