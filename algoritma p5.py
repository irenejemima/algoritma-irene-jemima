# matriks 2x2

A = []
B = []
C = [[0, 0], [0, 0]]

print("Masukkan matriks A:")
for i in range(2):
    row = []
    for j in range(2):
        angka = int(input(f"A[{i}][{j}] = "))
        row.append(angka)
    A.append(row)

print("\nMasukkan matriks B:")
for i in range(2):
    row = []
    for j in range(2):
        angka = int(input(f"B[{i}][{j}] = "))
        row.append(angka)
    B.append(row)

# Penjumlahan
print("\nHasil Penjumlahan:")
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]
        print(C[i][j], end=" ")
    print()

# Pengurangan
print("\nHasil Pengurangan:")
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] - B[i][j]
        print(C[i][j], end=" ")
    print()

# Perkalian
print("\nHasil Perkalian:")
for i in range(2):
    for j in range(2):
        C[i][j] = 0
        for k in range(2):
            C[i][j] += A[i][k] * B[k][j]
        print(C[i][j], end=" ")
    print()