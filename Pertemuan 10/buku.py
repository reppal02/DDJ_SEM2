import tkinter as tk
from tkinter import messagebox

def add_to_cart():
    selected_book = selected_book_var.get()
    quantity = int(quantity_var.get())

    if selected_book not in shopping_cart:
        shopping_cart[selected_book] = 0
    shopping_cart[selected_book] += quantity

    update_cart_display()

def update_cart_display():
    cart_text.delete(1.0, tk.END)
    total_price = 0
    for book, quantity in shopping_cart.items():
        price = harga_buku[book] * quantity
        cart_text.insert(tk.END, f"{book}: {quantity} x Rp {harga_buku[book]} = Rp {price}\n")
        total_price += price
    total_label.config(text=f"Total: Rp {total_price}")

def generate_receipt():
    nama_pembeli = pembeli_entry.get()
    uang_pembeli = int(uang_entry.get())
    total_price = sum(harga_buku[book] * quantity for book, quantity in shopping_cart.items())

    if uang_pembeli < total_price:
        messagebox.showerror("Error", "Uang yang diberikan tidak mencukupi.")
        return

    kembalian = uang_pembeli - total_price

    struk = f"Nama Pembeli: {nama_pembeli}\n\n"
    struk += "Pembelian:\n"
    for book, quantity in shopping_cart.items():
        price = harga_buku[book] * quantity
        struk += f"{book}: {quantity} x Rp {harga_buku[book]} = Rp {price}\n"
    struk += f"\nTotal: Rp {total_price}\n"
    struk += f"Uang Pembeli: Rp {uang_pembeli}\n"
    struk += f"Kembalian: Rp {kembalian}"

    messagebox.showinfo("Struk Beli", struk)

# Create main window
root = tk.Tk()
root.title("Program Toko Buku")

# Define book prices
harga_buku = {
    "Buku Novel": 40000,
    "Buku Pelajaran": 45000,
    "Buku Fiksi": 38000,
    "Buku Komik": 37000,
    "Buku Kamus": 42000
}

# Initialize shopping cart
shopping_cart = {}

# Add widgets
tk.Label(root, text="Nama Pembeli:").grid(row=0, column=0, sticky="w")
pembeli_entry = tk.Entry(root)
pembeli_entry.grid(row=0, column=1)

tk.Label(root, text="Pilih Buku:").grid(row=1, column=0, sticky="w")
book_options = list(harga_buku.keys())
selected_book_var = tk.StringVar(root)
selected_book_var.set(book_options[0])
book_dropdown = tk.OptionMenu(root, selected_book_var, *book_options)
book_dropdown.grid(row=1, column=1)

tk.Label(root, text="Jumlah:").grid(row=2, column=0, sticky="w")
quantity_var = tk.StringVar(root, value="1")
quantity_entry = tk.Entry(root, textvariable=quantity_var)
quantity_entry.grid(row=2, column=1)

add_to_cart_button = tk.Button(root, text="Tambah ke Keranjang", command=add_to_cart)
add_to_cart_button.grid(row=3, columnspan=2)

tk.Label(root, text="Keranjang Belanja:").grid(row=4, columnspan=2, sticky="w")
cart_text = tk.Text(root, height=8, width=40)
cart_text.grid(row=5, columnspan=2)

total_label = tk.Label(root, text="Total: Rp 0")
total_label.grid(row=6, columnspan=2)

tk.Label(root, text="Uang Tunai Pembeli:").grid(row=7, column=0, sticky="w")
uang_entry = tk.Entry(root)
uang_entry.grid(row=7, column=1)

generate_button = tk.Button(root, text="Cetak Struk", command=generate_receipt)
generate_button.grid(row=8, columnspan=2)

root.mainloop()
