# Exercise 2.1
# Soal: Modifikasi program dari Example 2.9 untuk membuat fungsi
# minarray(xs) yang mencari nilai MINIMUM dari sebuah array.

def minarray(xs):
    m = xs[0]           # anggap dulu elemen pertama sebagai nilai minimum
    for x in xs:
        if m > x:        # kalau ketemu elemen yang lebih kecil, update m
            m = x
    return m

data = [5, 3, 8, 1, 9, 4]
t = minarray(data)
print("Nilai minimum:", t)
