def berangkat_sekolah(pakaian, buku):
    if pakaian == "seragam" and buku == "bawa":
        print("Berangkat sekolah")
    else:
        print("Pergi main")

def nama_siswa(nama):
    print(nama)

print(nama_siswa("atiek desu"), berangkat_sekolah("seragam", "bawa"))
print(nama_siswa("akbar faisal"), berangkat_sekolah("jeans", "tidak membawa buku"))
print(nama_siswa("dokoni"), berangkat_sekolah("seragam", "tidak membawa buku"))


