# data diri
nama = "Irene Jemima"
nim = "251011700626"

print("Nama:", nama)
print("NIM:", nim)

# fizzbuzz 1 - 100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)