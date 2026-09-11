# Exercise 2.2
# Soal: Modifikasi program dari Example 2.9 untuk membuat fungsi
# sortarray(xs) yang mengurutkan array secara ascending (dari kecil ke besar).
#
# Di sini pakai algoritma bubble sort sederhana supaya konsisten
# dengan gaya Example 2.9 (pakai for loop manual, bukan xs.sort() langsung).

def sortarray(xs):
    n = len(xs)
    for i in range(n):
        for j in range(0, n - i - 1):
            if xs[j] > xs[j + 1]:
                # tukar posisi jika elemen kiri lebih besar dari elemen kanan
                xs[j], xs[j + 1] = xs[j + 1], xs[j]
    return xs

data = [5, 3, 8, 1, 9, 4]
t = sortarray(data)
print("Array terurut:", t)
