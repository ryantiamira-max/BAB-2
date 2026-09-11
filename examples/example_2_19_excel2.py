# Example 2.19 - THE EXCEL2.PY PROGRAM
# Membaca file Excel yang dibuat di Example 2.18
# JALANKAN example_2_18_excel.py DULU supaya file test.xlsx ada
# butuh: pip install openpyxl

import pandas

df = pandas.read_excel('test.xlsx', sheet_name='Sheet1')
print(df)
