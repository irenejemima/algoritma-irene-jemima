def bubble_sort_desc(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # tukar jika elemen kiri lebih kecil
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    n = int(input("Masukkan jumlah data: "))
    data = []
    for i in range(n):
        angka = int(input(f"Masukkan data ke-{i+1}: "))
        data.append(angka)

    print("Data sebelum diurutkan:", data)
    hasil = bubble_sort_desc(data)
    print("Data setelah diurutkan (descending):", hasil)