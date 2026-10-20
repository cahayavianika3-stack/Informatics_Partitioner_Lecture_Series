import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Simulasikan Data Koordinat Spasial (Latitude & Longitude fiktif titik fasilitas)
data = {
    'Nama_Fasilitas': ['Fasilitas A', 'Fasilitas B', 'Fasilitas C', 'Fasilitas D', 'Fasilitas E', 
                       'Fasilitas F', 'Fasilitas G', 'Fasilitas H', 'Fasilitas I', 'Fasilitas J'],
    'Latitude': [-3.7901, -3.7925, -3.8100, -3.8150, -3.7850, -3.8500, -3.8550, -3.7500, -3.7550, -3.7600],
    'Longitude': [102.2655, [102.2680], [102.3100], [102.3150], [102.2600], 
                  [102.4000], [102.4050], [102.2000], [102.2050], [102.2100]] # Koordinat area Bengkulu/sekitarnya
}

# Membersihkan format list pada longitude (jika ada nested list dari simulasi)
data['Longitude'] = [x[0] if isinstance(x, list) else x for x in data['Longitude']]
df = pd.DataFrame(data)

# 2. Ambil Fitur Koordinat untuk Proses Klastering
X = df[['Latitude', 'Longitude']]

# 3. Terapkan K-Means Clustering (Misal dibagi menjadi 3 zona wilayah)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Zona_Klaster'] = kmeans.fit_predict(X)

# 4. Tampilkan Hasil Pengelompokan Zona
print("Hasil Pengelompokan Wilayah Fasilitas:")
print(df[['Nama_Fasilitas', 'Zona_Klaster']])

# 5. Visualisasi Sebaran Spasial (Opsional)
plt.scatter(df['Longitude'], df['Latitude'], c=df['Zona_Klaster'], cmap='rainbow', s=100)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Spatial Clustering Sebaran Fasilitas (GIS Analysis)')
plt.grid(True)
plt.show()
