print("\nPenggunaan Break pada looping")
print("--------------------\n")
a = 0
b = float(input("Masukan angka anda : "))
while a < b: # a < b adalah syarat 
    print(a)
    if a == 5: # Seleksi kondisi
        break # Break point 
    a += 1 # increment