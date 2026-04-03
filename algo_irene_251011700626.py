# input jumlah hari
x = int(input("Masukin jumlah hari: "))

# hitung
tahun = x // 365
sisa = x % 365

bulan = sisa // 30
hari = sisa % 30

# output
print("Tahun:", tahun)
print("Bulan:", bulan)
print("Hari:", hari)