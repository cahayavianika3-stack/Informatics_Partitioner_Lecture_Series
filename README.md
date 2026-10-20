# Informatics_Partitioner_Lecture_Series 
Dokumentasi dan Implementasi Code Informatics Patitioner Lecture Series : Connecting Academic Knowladge with Industries and Global Techonolgy dalam bentuk Program Python sesuai studi kasus dari enam sesi seminar Informatika. Pembahasan mencakup pengolahan data, pemrosesan paralel, sistem informasi geografis, pembelajaran mesin, interaksi manusia dan komputer, serta pemanfaatan AI untuk mengidentifikasi penyebab deforestasi.

## 📚 Daftar Sesi

| Sesi | Materi                                                                           | Pemateri                             |
| ---- | -------------------------------------------------------------------------------- | ------------------------------------ |
| 1    | Make Sense of Data with Analysis and AI                                          | Andria Arisal, S.T., M.Eng.          |
| 2    | Bridging Global Infrastructure to Address Local Challenges with HPC              | Asst. Prof. Dr. Worawan Diaz Carbalo |
| 3    | Career and Competition in Industrial Era with GIS                                | Widi Primadepa, S.Kom.               |
| 4    | Introduction to Machine Learning                                                 | Dr. Taniza binti Tajuddin            |
| 5    | Human-Computer Interaction & Data Visualization                                  | Dr. Arafat Febriandirza              |
| 6    | Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI | Dr. Bart Slagter                     |

---

## Sesi 1 — Make Sense of Data with Analysis and AI

**Narasumber:** Andria Arisal, S.T., M.Eng.
**Instansi:** Pusat Riset Sains Data dan Informasi – BRIN

### Studi Kasus

**Analisis Risiko Piutang dan Penentuan Strategi Penanganan Kredit**

### Ringkasan

Sesi pertama membahas bagaimana data dapat digunakan untuk membantu proses pengambilan keputusan melalui analisis dan kecerdasan buatan. Studi kasus yang digunakan adalah analisis risiko piutang dan penentuan strategi penanganan kredit.

### Implementasi

* **Pengolahan Data**
  Dataset transaksi dipersiapkan dengan memeriksa nilai yang tidak lengkap dan menggantinya menggunakan nilai median agar data dapat digunakan dalam proses analisis.

* **Analisis Data**
  Analisis deskriptif digunakan untuk melihat kondisi piutang, sedangkan analisis diagnostik digunakan untuk mengetahui pola risiko berdasarkan faktor tertentu seperti diskon.

* **Prediksi Risiko**
  Analisis prediktif digunakan untuk memperkirakan kemungkinan terjadinya gagal bayar.

* **Pemodelan AI**
  Algoritma *Logistic Regression* digunakan untuk mengklasifikasikan tingkat risiko piutang.

* **Rekomendasi**
  Probabilitas yang dihasilkan model digunakan sebagai dasar simulasi rekomendasi kebijakan kredit.

---

## Sesi 2 — Bridging Global Infrastructure to Address Local Challenges with HPC

**Narasumber:** Asst. Prof. Dr. Worawan Diaz Carbalo
**Instansi:** Thammasat University, Thailand

### Studi Kasus

**Pemodelan Penyebaran Polusi Udara PM2.5 dengan Pemrosesan Paralel**

### Ringkasan

Sesi kedua membahas *High Performance Computing* (HPC) dan bagaimana pemrosesan paralel dapat digunakan untuk mempercepat penyelesaian suatu permasalahan komputasi. Implementasi dilakukan melalui simulasi penyebaran polusi udara PM2.5.

### Implementasi

* Membuat grid dua dimensi untuk merepresentasikan wilayah penyebaran polutan.
* Menghitung perubahan konsentrasi polusi secara berulang menggunakan pendekatan numerik.
* Membagi proses perhitungan menggunakan modul `multiprocessing`.
* Menjalankan beberapa proses secara bersamaan untuk membagi beban komputasi.
* Membandingkan waktu eksekusi antara metode sekuensial dan metode paralel.

---

## Sesi 3 — Career and Competition in Industrial Era with GIS

**Narasumber:** Widi Primadepa, S.Kom.
**Posisi:** Asset Management GIS Analyst – City Care Property, Selandia Baru

### Studi Kasus

**Pemantauan Kondisi Aset Infrastruktur Berdasarkan Informasi Geografis**

### Ringkasan

Sesi ketiga membahas pemanfaatan *Geographic Information System* (GIS) dalam pengelolaan dan pemantauan aset. Data lokasi dan kondisi aset digunakan untuk menentukan aset yang memiliki tingkat risiko lebih tinggi sehingga dapat diprioritaskan untuk pemeriksaan.

### Implementasi

* Menyimpan informasi aset seperti identitas, jenis, koordinat, usia, dan kondisi fisik menggunakan struktur data Python.
* Menggunakan rumus *Haversine* untuk menghitung jarak antara aset dengan pusat zona bahaya.
* Menentukan aset yang berada dalam jangkauan wilayah berisiko.
* Menggabungkan usia aset, tingkat kerusakan, dan jarak dari zona bahaya untuk menentukan prioritas pemeriksaan.
* Mengekspor hasil pengolahan dalam format **GeoJSON** agar dapat digunakan pada perangkat lunak GIS.

---

## Sesi 4 — Introduction to Machine Learning

**Narasumber:** Dr. Taniza binti Tajuddin
**Instansi:** Universiti Teknologi MARA (UiTM), Malaysia

### Studi Kasus

**Prediksi Kelayakan Pinjaman Menggunakan Algoritma Random Forest**

### Ringkasan

Sesi keempat memperkenalkan konsep dasar *Machine Learning* melalui studi kasus prediksi kelayakan pinjaman. Data pemohon digunakan untuk melatih model agar dapat memprediksi apakah suatu pengajuan pinjaman dapat disetujui.

### Implementasi

* Membuat dataset simulasi yang berisi pendapatan, jumlah pinjaman, skor kredit, usia, dan rasio utang.
* Membagi dataset menjadi **80% data latih** dan **20% data pengujian**.
* Melatih model menggunakan algoritma **Random Forest Classifier**.
* Menguji kemampuan model menggunakan *Confusion Matrix*, *Precision*, *Recall*, dan *F1-Score*.
* Menggunakan model yang telah dilatih untuk me

## Sesi 5 — Human-Computer Interaction & Data Visualization

**Narasumber:** Dr. Arafat Febriandirza
**Jabatan:** Kepala Kelompok Riset IMK & Visualisasi – BRIN

### Studi Kasus

Pembuatan Dashboard Pemantauan Kinerja Sistem dengan Antarmuka Interaktif

### Ringkasan

Sesi kelima membahas konsep Human-Computer Interaction (HCI) dan Data Visualization. Implementasinya dilakukan melalui pembuatan dashboard yang menyajikan informasi kinerja sistem dalam bentuk visual dan menyediakan interaksi bagi pengguna.

### Implementasi
Menampilkan indikator operasional dalam bentuk kartu agar informasi mudah dibaca.
Menggunakan perbedaan warna untuk menunjukkan kondisi optimal, waspada, dan kritis.
Mengelompokkan informasi berdasarkan jenis metrik agar dashboard lebih terstruktur.
Membuat tombol diagnostik menggunakan JavaScript.
Menampilkan pesan sebagai bentuk feedback setelah pengguna melakukan interaksi.
Menerapkan konsep affordance, visibilitas fungsi, dan umpan balik sistem.
Sesi 6 — Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI

**Narasumber:**  Dr. Bart Slagter
**Instansi:** Laboratory of Geo-Information Science & Remote Sensing

### Studi Kasus

Identifikasi Faktor Penyebab Deforestasi Menggunakan Data Satelit dan Machine Learning

### Ringkasan

Sesi keenam membahas pemanfaatan data citra satelit dan Machine Learning untuk mengidentifikasi faktor yang menyebabkan terjadinya deforestasi. Data perubahan vegetasi, kebakaran, lokasi jalan, dan luas pembukaan lahan digunakan sebagai fitur dalam proses klasifikasi.

### Implementasi
Membuat dataset simulasi yang berisi perubahan NDVI, perubahan NBR, jarak dari jalan, dan luas pembukaan tutupan lahan.
Menentukan label penyebab deforestasi berdasarkan aturan tertentu.
Mengelompokkan kemungkinan penyebab menjadi kebakaran hutan dan lahan, perkebunan, pembangunan infrastruktur jalan, serta perambahan skala kecil.
Melatih model Random Forest Classifier menggunakan fitur yang tersedia.
Mengevaluasi kinerja model menggunakan laporan klasifikasi.
Menggunakan model untuk memprediksi kategori penyebab dari data peringatan baru.
📌 Catatan

Seluruh program dalam repositori ini merupakan implementasi pembelajaran menggunakan data simulasi.

Hasil perhitungan dan prediksi yang dihasilkan digunakan untuk memahami konsep, metode, serta alur kerja dari masing-masing bidang yang dibahas dalam seminar.

Program dan hasil yang terdapat dalam repositori ini bukan merupakan pengganti analisis lapangan maupun sistem operasional yang telah tervalidasi.
