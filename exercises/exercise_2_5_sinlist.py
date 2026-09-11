import math

s = input("Input a list of numbers: ")
numbers = list(map(float, s.split()))   # ubah tiap teks jadi float

for num in numbers:
    result = math.sin(num)
    print("The sine of " + str(num) + " is " + str(result))
