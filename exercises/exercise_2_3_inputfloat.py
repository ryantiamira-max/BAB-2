# Exercise 2.3
# Soal: Modifikasi program dari Example 2.11 supaya membaca angka FLOAT
# (angka berkoma) dari keyboard, lalu menghitung kuadratnya.

print('Input a number: ')
x = input()
y = float(x)          # bedanya di sini: pakai float() bukan int()
y = y ** 2
print('The square of ' + str(x) + " is " + str(y))
