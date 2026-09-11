# Exercise 2.5
# Soal: Berdasarkan Example 2.10 dan 2.13, buat program yang membaca
# SEKUMPULAN angka float dari keyboard (dipisah spasi), lalu menghitung
# nilai sin() dari tiap angka, dan menampilkan hasilnya.

import math

s = input("Input a list of numbers: ")
numbers = list(map(float, s.split()))   # ubah tiap teks jadi float

for num in numbers:
    result = math.sin(num)
    print("The sine of " + str(num) + " is " + str(result))
