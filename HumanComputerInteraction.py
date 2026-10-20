import pandas as pd
import matplotlib.pyplot as plt

# 1. Menyiapkan Data Penjualan Bulanan
data = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
    'Total_Penjualan_Juta_IDR': [120, 135, 125, 142, 160, 175, 170, 185, 190, 210, 225, 250]
}

df = pd.DataFrame(data)

# 2. Mengatur Gaya Visualisasi yang Bersih dan Minimalis (Prinsip Data Visualization)
plt.figure(figsize=(10, 5))
plt.plot(df['Bulan'], df['Total_Penjualan_Juta_IDR'], marker='o', color='#1f77b4', linewidth=2.5, markersize=6)

# 3. Menambahkan Judul dan Label yang Informatif
plt.title('Tren Kinerja Penjualan Bulanan Perusahaan (Tahun Berjalan)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Bulan', fontsize=11)
plt.ylabel('Total Penjualan (Juta IDR)', fontsize=11)

# 4. Mengoptimalkan Layout & Menghilangkan Chartjunk (Grid tipis untuk kejelasan)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# 5. Menampilkan Grafik Interaktif/Visual
plt.show()