# Example 2.12 - THE INPUTLIST.PY PROGRAM
# Membaca daftar angka dari keyboard (dipisah spasi)

s = input("Input a list of numbers: ")
numbers = list(map(int, s.split()))
print(numbers)
