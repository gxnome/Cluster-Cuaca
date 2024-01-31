import pandas as pd

# Membaca file Excel
file_path = 'Data_Cuaca.xlsx'
data = pd.read_excel(file_path)

# 1. Mengambil kolom yang dibutuhkan
selected_columns = ['name', 'datetime', 'tempmax', 'tempmin']
data_selected = data[selected_columns]

# 2. Mengubah titik menjadi koma pada kolom tempmax dan tempmin
data_selected['tempmax'] = data_selected['tempmax'].astype(str).str.replace(',', '.').astype(float)
data_selected['tempmin'] = data_selected['tempmin'].astype(str).str.replace(',', '.').astype(float)

# 3. Menghilangkan data duplikat
data_selected.drop_duplicates(inplace=True)

# 4. Menghilangkan baris dengan data kosong
data_selected.dropna(inplace=True)

# 5. Menghapus data outlier
data_selected = data_selected[(data_selected['tempmax'] <= 40) & (data_selected['tempmin'] >= 20)]

# Menyimpan data yang sudah diolah ke file baru (Opsional)
output_file_path = 'Data_Cuaca_Bersih.xlsx'
data_selected.to_excel(output_file_path, index=False)

# Menampilkan data yang sudah diolah
print("Data Berhasil Dibersihkan")
