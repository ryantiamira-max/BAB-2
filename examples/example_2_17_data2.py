# Example 2.17 - THE DATA2.PY PROGRAM
# Membaca file CSV yang dibuat di Example 2.16
# JALANKAN example_2_16_data.py DULU supaya file test.csv ada

import pandas
df = pandas.read_csv('test.csv')
print(df)
