import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Simulasikan Dataset Fitur Spasial (Contoh: Luas area tebangan & Jarak ke jalan/sungai)
data = {
    'Luas_Tebangan_Hektar': [1.2, 45.0, 0.8, 50.5, 2.1, 38.0, 1.5, 60.0],
    'Jarak_Ke_Jalan_Km': [0.5, 2.1, 0.2, 1.8, 0.4, 2.5, 0.3, 1.2],
    'Jarak_Ke_Sungai_Km': [2.0, 10.5, 1.5, 8.0, 3.0, 9.2, 2.2, 6.5],
    # Label Target: 0 = Pertanian Skala Kecil, 1 = Pertanian/Industri Skala Besar
    'Kategori_Penyebab': [0, 1, 0, 1, 0, 1, 0, 1] 
}

df = pd.DataFrame(data)

# 2. Memisahkan Fitur (X) dan Target (y)
X = df[['Luas_Tebangan_Hektar', 'Jarak_Ke_Jalan_Km', 'Jarak_Ke_Sungai_Km']]
y = df['Kategori_Penyebab']

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. Melatih Model Machine Learning (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
