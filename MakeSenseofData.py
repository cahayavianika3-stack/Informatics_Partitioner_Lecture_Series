import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Simulasikan Dataset Transaksi Invoice
data = {
    'Jumlah_Invoice_Juta': [5, 20, 3, 15, 25, 4, 12, 18, 8, 30],
    'Riwayat_Kredit_Baik': [1, 1, 0, 1, 0, 0, 1, 1, 0, 1], # 1 = Baik, 0 = Buruk
    'Metode_Bayar_Tempo': [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], # 1 = Tempo, 0 = Tunai
    'Terlambat_Bayar': [0, 1, 1, 0, 1, 1, 0, 0, 1, 0]    # Target: 1 = Terlambat, 0 = Tepat Waktu
}

df = pd.DataFrame(data)

# 2. Pisahkan Fitur (X) dan Target (y)
X = df[['Jumlah_Invoice_Juta', 'Riwayat_Kredit_Baik', 'Metode_Bayar_Tempo']]
y = df['Terlambat_Bayar']

# 3. Bagi Data menjadi Training (80%) dan Testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Latih Model menggunakan Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Evaluasi Performa Model
y_pred = model.predict(X_test)
print("Akurasi Model:", accuracy_score(y_test, y_pred))
print("\nLaporan Klasifikasi:\n", classification_report(y_test, y_pred, zero_division=0))

# 6. Prediksi untuk Invoice Baru
# Invoice baru: Jumlah 15 juta, Riwayat Kredit Baik (1), Metode Bayar Tempo (1)
invoice_baru = pd.DataFrame([[15, 1, 1]], columns=['Jumlah_Invoice_Juta', 'Riwayat_Kredit_Baik', 'Metode_Bayar_Tempo'])
prediksi_status = model.predict(invoice_baru)

status_str = "Berpotensi Terlambat" if prediksi_status[0] == 1 else "Tepat Waktu"
print(f"Hasil Prediksi Invoice Baru: {status_str}")