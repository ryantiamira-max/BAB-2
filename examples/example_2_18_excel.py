
import pandas as pd

data = {'Name': ['Tony', 'Robert', 'John', 'Alice'],
        'Age':  [18, 24, 19, 21],
        }

df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)
writer = pd.ExcelWriter("test.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
# Catatan: pandas versi baru sudah tidak punya writer.save(),
# gunakan writer.close() sebagai gantinya
writer.close()
