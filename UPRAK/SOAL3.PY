# DICTIONARY DENGAN NILAI NILAI SISWA
nilai_siswa = (
    "siswa 1":85,
    "siswa 2":90,
    "siswa 3":78,
    "siswa 4":92,
    "siswa 5":88 
)

# menghitung jumlah total nilai siswa
total_nilai = 0 
for nilai in nilai_siswa.values():
    total_nilai += nilai

print("jumlah total nilai semua siswa adalah", total_nilai) 