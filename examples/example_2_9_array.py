# Example 2.9 - THE ARRAY.PY PROGRAM
# Fungsi untuk mencari nilai maksimum dalam sebuah array (list)

def maxarray(xs):
    m = xs[0]
    for x in xs:
        if m < x:
            m = x
    return m

data = [0, 1, 2, 3, 4, 5]
t = maxarray(data)
print(t)
