
def minarray(xs):
    m = xs[0]           # anggap dulu elemen pertama sebagai nilai minimum
    for x in xs:
        if m > x:        # kalau ketemu elemen yang lebih kecil, update m
            m = x
    return m

data = [5, 3, 8, 1, 9, 4]
t = minarray(data)
print("Nilai minimum:", t)
