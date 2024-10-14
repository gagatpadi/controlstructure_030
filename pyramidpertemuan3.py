def desain_angka(n):
    for i in range(1, n + 1):
        print((str(i) + '') * i)


#contoh penggunaan 
n = int(input("Masukkan nilai n untuk menghasilkan desain angka: "))
desain_angka(n)