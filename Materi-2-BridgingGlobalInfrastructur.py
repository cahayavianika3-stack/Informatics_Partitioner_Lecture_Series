import time
from multiprocessing import Pool

# 1. Fungsi Simulasi Analisis Data Berat per Titik Sensor
def proses_analisis_sensor(id_sensor):
    print(f"Memulai analisis data untuk Sensor ID: {id_sensor}")
    # Mensimulasikan beban komputasi berat (misal: kalkulasi matematis/machine learning kecil)
    time.sleep(1) 
    hasil = id_sensor * 3.14159  # Contoh perhitungan sederhana
    return f"Sensor {id_sensor} selesai. Hasil: {hasil:.2f}"

if __name__ == '_main_':
    # Daftar ID sensor yang akan diproses secara paralel
    daftar_sensor = [101, 102, 103, 104, 105, 106, 107, 108]

    print("--- Memulai Simulasi Pemrosesan Paralel (HPC Concept) ---")
    waktu_mulai = time.time()

    # 2. Menggunakan Pool untuk memproses data secara paralel memanfaatkan multi-core CPU
    # Menyesuaikan jumlah proses dengan core yang tersedia
    jumlah_proses = 4 
    with Pool(processes=jumlah_proses) as pool:
        hasil_analisis = pool.map(proses_analisis_sensor, daftar_sensor)

    waktu_selesai = time.time()

    # 3. Menampilkan Hasil dan Waktu Eksekusi
    print("\n--- Hasil Analisis Selesai ---")
    for res in hasil_analisis:
        print(res)

    print(f"\nWaktu total eksekusi secara paralel: {waktu_selesai - waktu_mulai:.2f} detik")
