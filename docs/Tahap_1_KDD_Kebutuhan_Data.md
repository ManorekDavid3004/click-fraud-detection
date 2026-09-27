# TAHAP 1 - KDD
## Sistem Deteksi Fraud Klik Iklan Digital Menggunakan Machine Learning

### 1. Tujuan

Tahap pertama dilakukan untuk memahami kebutuhan data dan alur pengolahan data yang akan digunakan dalam sistem deteksi fraud klik iklan digital.

Metode KDD (Knowledge Discovery in Databases) digunakan sebagai kerangka umum untuk menggambarkan proses pengolahan data mulai dari pemilihan data sampai diperoleh pengetahuan atau hasil yang dapat digunakan untuk mendukung proses deteksi fraud.

---

### 2. Alur KDD

Alur KDD yang digunakan dalam proyek terdiri dari:

1. Selection
2. Preprocessing
3. Transformation
4. Data Mining
5. Evaluation / Interpretation

Alur tersebut digunakan sebagai pedoman dalam menyiapkan dataset sebelum digunakan oleh model machine learning.

---

### 3. Selection

Pada tahap Selection dilakukan penentuan dataset dan atribut yang relevan dengan tujuan proyek.

Dataset yang digunakan adalah:

**Fraud Detection Dataset**

Sumber:

**Kaggle - ziya07**

Dataset memiliki 5.000 baris dan 21 kolom.

Variabel target yang dipilih adalah:

`is_fraudulent`

Dengan nilai:

- `0` = Non-Fraud
- `1` = Fraud

Variabel input terdiri dari informasi klik, perangkat, halaman, perilaku pengguna, serta indikator risiko seperti penggunaan VPN, proxy, reputasi IP, dan bot likelihood score.

---

### 4. Preprocessing

Tahap Preprocessing bertujuan untuk memeriksa dan memperbaiki kualitas data sebelum digunakan pada proses berikutnya.

Pemeriksaan awal yang telah dilakukan meliputi:

- pemeriksaan jumlah baris dan kolom;
- pemeriksaan missing value;
- pemeriksaan data duplikat;
- pemeriksaan tipe dan rentang nilai;
- pemeriksaan validitas timestamp;
- pemeriksaan label target;
- pemeriksaan kandidat outlier.

Hasil pemeriksaan awal menunjukkan:

- jumlah data = 5.000 baris;
- jumlah kolom = 21;
- missing value = 0;
- data duplikat = 0;
- timestamp tidak valid = 0;
- label target berada pada nilai 0 dan 1;
- kandidat outlier ditemukan pada `click_duration` sebanyak 263 data.

Kandidat outlier tidak langsung dihapus dan akan dipertimbangkan kembali pada tahap preprocessing berdasarkan kebutuhan sistem.

---

### 5. Transformation

Tahap Transformation dilakukan untuk menyesuaikan data agar dapat digunakan oleh proses machine learning.

Rencana transformation meliputi:

- penyesuaian tipe data;
- normalisasi format data;
- pemetaan nama dan fungsi kolom;
- pengolahan variabel kategorikal jika diperlukan;
- pengolahan timestamp jika diperlukan;
- penyesuaian format data dengan kebutuhan sistem;
- pemisahan variabel input dan target.

Transformation dilakukan tanpa menambahkan informasi baru yang tidak tersedia dalam dataset.

---

### 6. Data Mining

Tahap Data Mining merupakan tahap penggunaan metode machine learning untuk menemukan pola dan melakukan klasifikasi data.

Dalam proyek ini, target klasifikasi adalah:

`is_fraudulent`

Model machine learning akan digunakan untuk memprediksi apakah suatu aktivitas klik termasuk:

- Non-Fraud (`0`), atau
- Fraud (`1`).

Pemilihan dan pembangunan model machine learning dilakukan pada tahap pengembangan model oleh anggota yang bertanggung jawab terhadap bagian tersebut.

---

### 7. Evaluation / Interpretation

Tahap Evaluation digunakan untuk mengevaluasi hasil model dan memastikan bahwa hasil prediksi dapat digunakan sesuai tujuan sistem.

Evaluasi model akan menggunakan metrik seperti:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

Hasil evaluasi akan digunakan untuk mengetahui performa model dalam membedakan klik fraud dan non-fraud.

---

### 8. Kebutuhan Data Sistem

Berdasarkan tujuan proyek, sistem membutuhkan data yang dapat menggambarkan karakteristik aktivitas klik.

Data utama yang tersedia meliputi:

#### Identitas dan Aktivitas Klik
- `click_id`
- `timestamp`
- `user_id`
- `ip_address`

#### Perangkat dan Lingkungan
- `device_type`
- `browser`
- `operating_system`

#### Informasi Halaman
- `referrer_url`
- `page_url`
- `ad_position`

#### Perilaku Pengguna
- `click_duration`
- `scroll_depth`
- `mouse_movement`
- `keystrokes_detected`
- `click_frequency`
- `time_since_last_click`

#### Indikator Risiko
- `device_ip_reputation`
- `VPN_usage`
- `proxy_usage`
- `bot_likelihood_score`

#### Target
- `is_fraudulent`

---

### 9. Input dan Output Sistem

#### Input

Input utama sistem adalah data aktivitas klik iklan yang memiliki informasi mengenai pengguna, perangkat, perilaku klik, serta indikator risiko.

#### Proses

Data akan melalui proses:

Raw Dataset
→ Data Validation
→ Data Preprocessing
→ Feature Preparation
→ Machine Learning
→ Prediction

#### Output

Output utama sistem adalah hasil klasifikasi terhadap aktivitas klik:

- Non-Fraud
- Fraud

Output tersebut kemudian dapat digunakan oleh sistem untuk menampilkan hasil prediksi dan informasi pendukung lainnya.

---

### 10. Hasil Tahap 1

Pada tahap awal, dataset telah berhasil diperiksa dan didokumentasikan.

Hasil yang telah diperoleh:

1. Dataset berhasil ditentukan.
2. Struktur dataset telah diidentifikasi.
3. 21 kolom telah didokumentasikan.
4. Variabel target telah ditentukan, yaitu `is_fraudulent`.
5. Tidak ditemukan missing value.
6. Tidak ditemukan data duplikat.
7. Tidak ditemukan timestamp yang tidak valid.
8. Distribusi label telah diperiksa.
9. Kandidat outlier telah diidentifikasi.
10. Sumber dataset dan lisensi telah dicatat.

Tahap selanjutnya adalah melakukan persiapan format data, pemetaan kolom, parser, dan normalisasi data sesuai kebutuhan sistem.

---

### 11. Batasan Tahap 1

Tahap ini berfokus pada pemahaman dataset, kebutuhan data, dokumentasi, dan pemeriksaan kualitas awal.

Pembangunan model machine learning, integrasi database, API, dashboard, dan sistem prediksi belum menjadi bagian utama dari tahap ini dan akan dilakukan pada tahapan proyek berikutnya sesuai pembagian tugas anggota.

##############################################################

# TAHAP 1 - KDD DAN KEBUTUHAN DATA

## Sistem Deteksi Fraud Klik Iklan Digital Menggunakan Machine Learning

### 1. Tujuan Tahap

Tahap ini dilakukan untuk memahami kebutuhan data yang diperlukan
dalam pengembangan Sistem Deteksi Fraud Klik Iklan Digital
Menggunakan Machine Learning.

Kegiatan pada tahap ini meliputi pemahaman alur KDD, identifikasi
data yang dibutuhkan sistem, penentuan target yang akan diprediksi,
identifikasi keluaran sistem, serta dokumentasi sumber dan lisensi
dataset.

---

## 2. Alur KDD

Proses pengembangan data pada proyek ini mengacu pada tahapan
Knowledge Discovery in Databases (KDD).

Tahapan yang digunakan adalah:

1. Selection
2. Preprocessing
3. Transformation
4. Data Mining
5. Evaluation

### 2.1 Selection

Pada tahap selection dilakukan pemilihan dataset dan atribut yang
relevan dengan tujuan sistem.

Dataset yang digunakan adalah Fraud Detection Dataset yang diperoleh
dari Kaggle.

Dataset memiliki 5.000 data dan 21 atribut.

Atribut yang tersedia mencakup informasi waktu, pengguna, alamat IP,
perangkat, browser, sistem operasi, aktivitas pengguna, posisi iklan,
reputasi IP, penggunaan VPN/proxy, dan nilai kemungkinan bot.

### 2.2 Preprocessing

Tahap preprocessing dilakukan untuk memeriksa dan mempersiapkan
kualitas data sebelum digunakan pada proses berikutnya.

Pemeriksaan awal meliputi:

- missing value
- data duplikat
- tipe data
- validitas timestamp
- rentang nilai
- validitas label
- pemeriksaan kandidat outlier

Hasil pemeriksaan awal didokumentasikan pada file
`Data_Quality_Report.md`.

### 2.3 Transformation

Tahap transformation dilakukan untuk menyesuaikan bentuk data agar
dapat digunakan oleh proses machine learning.

Tahap ini akan mencakup penyesuaian tipe data, pengolahan atribut
kategorikal, dan normalisasi atau transformasi atribut apabila
diperlukan.

Transformation dilakukan pada tahap persiapan data dan tidak
menambahkan informasi yang tidak tersedia pada dataset asli.

### 2.4 Data Mining

Tahap data mining digunakan untuk membangun model klasifikasi yang
dapat membedakan aktivitas klik fraud dan non-fraud.

Target klasifikasi adalah:

`is_fraudulent`

dengan nilai:

- 0 = Non-Fraud
- 1 = Fraud

Pemodelan machine learning akan dikerjakan pada tahap berikutnya
sesuai pembagian tugas anggota proyek.

### 2.5 Evaluation

Tahap evaluation digunakan untuk menilai hasil model dan memastikan
bahwa model dapat memberikan hasil prediksi sesuai kebutuhan sistem.

Evaluasi akan menggunakan metrik yang ditentukan pada tahap
pengembangan machine learning, seperti accuracy, precision, recall,
F1-score, dan ROC-AUC.

---

# 3. Kebutuhan Data Masuk

Data yang masuk ke sistem berasal dari aktivitas klik iklan digital.

Atribut yang tersedia dalam dataset meliputi:

- click_id
- timestamp
- user_id
- ip_address
- device_type
- browser
- operating_system
- referrer_url
- page_url
- click_duration
- scroll_depth
- mouse_movement
- keystrokes_detected
- ad_position
- click_frequency
- time_since_last_click
- device_ip_reputation
- VPN_usage
- proxy_usage
- bot_likelihood_score

Data tersebut digunakan sebagai informasi untuk menganalisis
karakteristik aktivitas klik.

---

# 4. Target Data

Target yang digunakan dalam sistem adalah:

`is_fraudulent`

Keterangan:

| Nilai | Keterangan |
|---|---|
| 0 | Non-Fraud |
| 1 | Fraud |

Target tersebut digunakan untuk proses klasifikasi machine learning.

---

# 5. Kebutuhan Output Sistem

Output utama yang diharapkan dari sistem adalah hasil klasifikasi
terhadap suatu aktivitas klik.

Output sistem berupa:

- prediksi Non-Fraud
- prediksi Fraud

Hasil prediksi tersebut akan menjadi dasar bagi sistem untuk
mengidentifikasi aktivitas klik yang terindikasi fraud.

---

# 6. Kebutuhan Data untuk Pengembangan Sistem

Data yang dibutuhkan dapat dikelompokkan menjadi:

### A. Data Identitas dan Aktivitas

- click_id
- timestamp
- user_id
- ip_address

### B. Data Perangkat

- device_type
- browser
- operating_system

### C. Data Aktivitas Pengguna

- click_duration
- scroll_depth
- mouse_movement
- keystrokes_detected
- click_frequency
- time_since_last_click

### D. Data Iklan dan Halaman

- referrer_url
- page_url
- ad_position

### E. Data Keamanan dan Risiko

- device_ip_reputation
- VPN_usage
- proxy_usage
- bot_likelihood_score

### F. Label

- is_fraudulent

---

# 7. Kondisi Awal Dataset

Berdasarkan pemeriksaan awal terhadap dataset:

- Jumlah data: 5.000 baris
- Jumlah atribut: 21 kolom
- Missing value: 0
- Timestamp tidak valid: 0
- Label: 0 dan 1
- Non-Fraud: 3.759 data
- Fraud: 1.241 data

Pemeriksaan lebih rinci dicatat dalam
`Data_Quality_Report.md`.

---

# 8. Lokasi Dataset

Dataset asli disimpan pada:

`data/raw/click_fraud_dataset.csv`

Dataset asli tidak diubah secara langsung. Proses pengolahan dan
transformasi selanjutnya akan menghasilkan data pada folder:

`data/processed/`

---

# 9. Sumber Dataset

Dataset yang digunakan adalah:

**Fraud Detection Dataset**

Sumber:

**Kaggle**

Author:

**ziya07**

URL:

https://www.kaggle.com/datasets/ziya07/fraud-detection-dataset

Lisensi:

**CC0: Public Domain**

Tanggal pengambilan dataset:

**22 September 2026**

Informasi sumber dan lisensi didokumentasikan secara terpisah pada:

`sumber_dataset.md`

---

# 10. Kesimpulan Tahap 1

Berdasarkan tahap awal KDD, dataset yang digunakan telah
diidentifikasi dan kebutuhan data sistem telah ditentukan.

Dataset memiliki 5.000 data dengan 21 atribut yang mencakup
informasi aktivitas pengguna, perangkat, halaman, keamanan, serta
label fraud.

Target sistem adalah `is_fraudulent`, dengan nilai 0 sebagai
Non-Fraud dan 1 sebagai Fraud.

Hasil tahap ini menjadi dasar untuk proses persiapan dan pengolahan
data pada tahap berikutnya.