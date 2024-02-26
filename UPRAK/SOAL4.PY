# INISIALISASI DATA BUAH
daftar_buah = [
    {"nama": "apel", "harga": 5000, "jumlah": 10},
    {"nama": "jeruk", "harga": 3000, "jumlah": 5},
    {"nama": "mangga", "harga": 7000, "jumlah": 7},
    {"nama": "pisang", "harga": 2000, "jumlah": 20},
    {"nama": "semangka", "harga": 15000, "jumlah": 1}
]

# menghitung total belanjaan 
total_belanja = 0
for buah in daftar_buah:
    total_belanja += buah["harga"] *
buah["jumlah"]

# menampilkan total belanjaan 
print(f"total belanjaan ibu sari adalah: 
{total_belanja} rupiah")