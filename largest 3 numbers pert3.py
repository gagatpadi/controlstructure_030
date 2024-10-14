def angka_terbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else :
        return c
    
#contoh penggunaan
num1 = int(input("Masukan angka pertama: "))
num2 = int(input("Masukan angka kedua: "))
num3 = int(input("Masukan angka ketiga: "))
terbesar=angka_terbesar(num1, num2, num3)
print(f"angka terbesar adalah: ", terbesar)