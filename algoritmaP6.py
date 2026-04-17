def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def perkalian(a, b):
    return a * b

def main():
    print("1. Barisan Fibonacci\n2. M Kali N\n0. Keluar")
    option = int(input("Pilih menu : \n"))
    if option == 1:
        n = int(input("Masukkan jumlah suku : \n"))
        print(f"Barisan fibonacci sebanyak {n} suku : ")
        for i in range(1, n + 1):
            print(fibonacci(i), end=" ")
        print()
    elif option == 2:
        a = int(input("Masukkan Suatu Bilangan Bulat : \n"))
        b = int(input("Masukkan Suatu Bilangan Pengali : \n"))
        print(f"{a} x {b} = {perkalian(a, b)}")
    elif option == 0:
        return

if __name__ == "__main__":
    main()
