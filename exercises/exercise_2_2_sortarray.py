
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
