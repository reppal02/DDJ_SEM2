data_penjualan = [
    {"buah": "semangka", "jumlah":40},
    {"sayur": "brokoli", "jumlah":33},
    {"makanan": "sushi", "jumlah":63},
    {"minuman": "icedtea", "jumlah":12},
]

total_penjualan = 0
for item in data_penjualan:
    total_penjualan += item["jumlah"]

print("total penjualan : ", total_penjualan)