import tkinter as tk

# Data barang-barang dari Gramedia
daftar_barang = {
    "Buku Novel": 40000,
    "Buku Pelajaran": 45000,
    "Buku Fiksi": 38000,
    "Buku Komik": 37000,
    "Buku Kamus": 42000
}

def hitung_total():
    harga = daftar_barang[combo_barang.get()]
    jumlah = int(entry_jumlah.get())
    total = harga * jumlah
    label_total.config(text="Total: Rp " + str(total))

# Membuat jendela utama
root = tk.Tk()
root.title("Program Kasir Sederhana")

# Membuat label untuk pilihan barang
label_barang = tk.Label(root, text="Pilih Barang:")
label_barang.pack()

# Membuat dropdown untuk memilih barang
barang_options = list(daftar_barang.keys())
combo_barang = tk.StringVar(root)
combo_barang.set(barang_options[0])  # default value
dropdown_barang = tk.OptionMenu(root, combo_barang, *barang_options)
dropdown_barang.pack()

# Membuat label untuk input jumlah
label_jumlah = tk.Label(root, text="Jumlah Barang:")
label_jumlah.pack()

# Membuat entry untuk input jumlah
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# Tombol untuk menghitung total
tombol_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
tombol_hitung.pack()

# Label untuk menampilkan total
label_total = tk.Label(root, text="")
label_total.pack()

root.mainloop()
