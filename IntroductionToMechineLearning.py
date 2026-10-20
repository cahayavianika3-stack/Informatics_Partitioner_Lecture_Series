import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Simulasikan Dataset Historis Nasabah
data = {
    'Pendapatan_Juta': [5, 12, 3, 8, 15, 4, 10, 6, 14, 7],
    'Jumlah_Pinjaman_Juta': [50, 100, 30, 60, 120, 40, 90, 50, 110, 55],
    'Riwayat_Kredit_Baik': [1, 1, 0, 1, 1, 0, 1, 0, 1, 1], # 1 = Baik, 0 = Buruk
    'Status_Pekerjaan_Tetap': [1, 1, 0, 1, 1, 0, 1, 0, 1, 1], # 1 = Ya, 0 = Tidak
    'Target_Disetujui': [1, 1, 0, 1, 1, 0, 1, 0, 1, 1] # 1 = Disetujui, 0 = Ditolak
}

df = pd.DataFrame(data)

# 2. Pisahkan Fitur (X) dan Target (y)
X = df[['Pendapatan_Juta', 'Jumlah_Pinjaman_Juta', 'Riwayat_Kredit_Baik', 'Status_Pekerjaan_Tetap']]
y = df['Target_Disetujui']

# 3. Split Data: Training (80%) dan Testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Pilih dan Latih Model (Menggunakan Random Forest Classifier)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Evaluasi Model pada Data Uji (Unseen Data)
y_pred = model.predict(X_test)
print("Akurasi Model:", accuracy_score(y_test, y_pred))
print("\nLaporan Klasifikasi:\n", classification_report(y_test, y_pred, zero_division=0))

# 6. Simulasi Prediksi untuk Nasabah Baru
# Nasabah baru: Pendapatan 10 juta, Pinjaman 80 juta, Riwayat Kredit Baik (1), Pekerjaan Tetap (1)
data_nasabah_baru = pd.DataFrame([[10, 80, 1, 1]], columns=['Pendapatan_Juta', 'Jumlah_Pinjaman_Juta', 'Riwayat_Kredit_Baik', 'Status_Pekerjaan_Tetap'])
prediksi = model.predict(data_nasabah_baru)

status = "Disetujui" if prediksi[0] == 1 else "Ditolak"
print(f"Hasil Prediksi untuk Nasabah Baru: Pinjaman {status}")