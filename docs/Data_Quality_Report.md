# DATA QUALITY REPORT
## Sistem Deteksi Fraud Klik Iklan Digital Menggunakan Machine Learning

### 1. Tujuan Pemeriksaan

Pemeriksaan kualitas data dilakukan untuk mengetahui kondisi awal dataset sebelum digunakan pada proses pengolahan data dan machine learning.

Pemeriksaan mencakup jumlah data, struktur kolom, nilai kosong, duplikasi, tipe data, rentang nilai, validitas timestamp, distribusi label, distribusi kategori, dan pemeriksaan kandidat outlier.

---

### 2. Ringkasan Dataset

| Pemeriksaan | Hasil |
|---|---:|
| Jumlah baris | 5.000 |
| Jumlah kolom | 21 |
| Nilai kosong | 0 |
| Data duplikat | 0 |
| Timestamp tidak valid | 0 |
| Nilai label di luar 0 dan 1 | 0 |
| Kolom target | `is_fraudulent` |

Berdasarkan pemeriksaan awal, seluruh 5.000 baris data memiliki nilai pada seluruh kolom dan tidak ditemukan data duplikat.

---

### 3. Pemeriksaan Nilai Kosong

Hasil pemeriksaan terhadap seluruh kolom menunjukkan bahwa tidak terdapat nilai kosong atau missing value.

| Kondisi | Jumlah |
|---|---:|
| Baris dengan missing value | 0 |
| Kolom yang memiliki missing value | 0 |

**Kesimpulan:**

Dataset tidak memerlukan penanganan missing value pada tahap pemeriksaan awal karena seluruh kolom memiliki data yang terisi.

---

### 4. Pemeriksaan Duplikasi

Pemeriksaan duplikasi dilakukan untuk mengetahui apakah terdapat baris data yang sama atau tercatat lebih dari satu kali.

| Pemeriksaan | Hasil |
|---|---:|
| Jumlah data duplikat | 0 |

**Kesimpulan:**

Tidak ditemukan baris duplikat pada dataset sehingga seluruh 5.000 baris dapat dipertahankan pada tahap pemeriksaan awal.

---

### 5. Pemeriksaan Label Fraud

Kolom target yang digunakan adalah `is_fraudulent`.

| Label | Keterangan | Jumlah | Persentase |
|---:|---|---:|---:|
| 0 | Non-Fraud | 3.759 | 75,18% |
| 1 | Fraud | 1.241 | 24,82% |
| **Total** | | **5.000** | **100%** |

**Kesimpulan:**

Dataset memiliki dua kelas, yaitu non-fraud dan fraud. Data non-fraud berjumlah 3.759 data atau 75,18%, sedangkan data fraud berjumlah 1.241 data atau 24,82%.

Distribusi label menunjukkan bahwa jumlah data antar kelas tidak sama, sehingga distribusi kelas perlu diperhatikan pada tahap pengembangan model machine learning.

---

### 6. Pemeriksaan Rentang Nilai Numerik

Hasil pemeriksaan nilai minimum dan maksimum:

| Kolom | Minimum | Maksimum |
|---|---:|---:|
| `click_duration` | 0,0 | 18,28 |
| `scroll_depth` | 0 | 99 |
| `mouse_movement` | 0 | 499 |
| `keystrokes_detected` | 0 | 49 |
| `click_frequency` | 1 | 9 |
| `time_since_last_click` | 1 | 599 |
| `bot_likelihood_score` | 0,0 | 1,0 |
| `VPN_usage` | 0 | 1 |
| `proxy_usage` | 0 | 1 |
| `is_fraudulent` | 0 | 1 |

**Kesimpulan:**

Tidak ditemukan nilai negatif pada variabel numerik yang diperiksa. Variabel `VPN_usage`, `proxy_usage`, dan `is_fraudulent` memiliki rentang nilai 0 sampai 1 sesuai bentuk variabel biner.

---

### 7. Pemeriksaan Timestamp

Kolom `timestamp` diperiksa untuk memastikan nilai dapat dikonversi menjadi format waktu.

Hasil pemeriksaan:

| Pemeriksaan | Hasil |
|---|---|
| Timestamp tidak valid | 0 |
| Timestamp minimum | 2024-02-19 04:56:53 |
| Timestamp maksimum | 2025-02-18 09:55:55 |

**Kesimpulan:**

Seluruh nilai timestamp berhasil dikenali sebagai data waktu sehingga dapat digunakan pada proses pengolahan data berikutnya apabila diperlukan.

---

### 8. Pemeriksaan Kandidat Outlier

Pemeriksaan outlier dilakukan menggunakan metode Interquartile Range (IQR) pada variabel numerik.

| Kolom | Kandidat Outlier |
|---|---:|
| `click_duration` | 263 |
| `scroll_depth` | 0 |
| `mouse_movement` | 0 |
| `keystrokes_detected` | 0 |
| `click_frequency` | 0 |
| `time_since_last_click` | 0 |
| `bot_likelihood_score` | 0 |

Hanya `click_duration` yang menghasilkan kandidat outlier sebanyak 263 data.

**Keputusan:**

Kandidat outlier pada `click_duration` tidak langsung dihapus. Nilai tersebut dipertahankan terlebih dahulu karena outlier secara statistik belum tentu merupakan kesalahan data. Dalam konteks deteksi fraud, perilaku yang berbeda dari mayoritas data dapat memiliki informasi yang relevan untuk proses klasifikasi.

Penanganan lebih lanjut terhadap kandidat outlier akan dipertimbangkan pada tahap preprocessing berdasarkan kebutuhan model dan validasi data.

---

### 9. Distribusi Kategori Berdasarkan Status Fraud

Pemeriksaan distribusi kategori dilakukan terhadap beberapa variabel kategorikal untuk melihat jumlah data non-fraud dan fraud pada masing-masing kategori.

#### Device Type

| Device | Non-Fraud | Fraud | Total |
|---|---:|---:|---:|
| Desktop | 1.298 | 440 | 1.738 |
| Mobile | 1.229 | 411 | 1.640 |
| Tablet | 1.232 | 390 | 1.622 |
| **Total** | **3.759** | **1.241** | **5.000** |

#### Browser

| Browser | Non-Fraud | Fraud | Total |
|---|---:|---:|---:|
| Chrome | 754 | 239 | 993 |
| Edge | 716 | 268 | 984 |
| Firefox | 816 | 249 | 1.065 |
| Opera | 754 | 240 | 994 |
| Safari | 719 | 245 | 964 |
| **Total** | **3.759** | **1.241** | **5.000** |

#### Operating System

| Operating System | Non-Fraud | Fraud | Total |
|---|---:|---:|---:|
| Android | 722 | 250 | 972 |
| Linux | 786 | 254 | 1.040 |
| Windows | 732 | 247 | 979 |
| iOS | 771 | 237 | 1.008 |
| macOS | 748 | 253 | 1.001 |
| **Total** | **3.759** | **1.241** | **5.000** |

#### Ad Position

| Ad Position | Non-Fraud | Fraud | Total |
|---|---:|---:|---:|
| Bottom | 1.246 | 421 | 1.667 |
| Side | 1.275 | 419 | 1.694 |
| Top | 1.238 | 401 | 1.639 |
| **Total** | **3.759** | **1.241** | **5.000** |

#### Device IP Reputation

| Reputation | Non-Fraud | Fraud | Total |
|---|---:|---:|---:|
| Bad | 180 | 60 | 240 |
| Good | 3.023 | 968 | 3.991 |
| Suspicious | 556 | 213 | 769 |
| **Total** | **3.759** | **1.241** | **5.000** |

---

### 10. Pemeriksaan VPN dan Proxy

#### VPN Usage

| VPN Usage | Non-Fraud | Fraud | Total |
|---:|---:|---:|---:|
| 0 | 3.373 | 1.125 | 4.498 |
| 1 | 386 | 116 | 502 |
| **Total** | **3.759** | **1.241** | **5.000** |

#### Proxy Usage

| Proxy Usage | Non-Fraud | Fraud | Total |
|---:|---:|---:|---:|
| 0 | 3.180 | 1.056 | 4.236 |
| 1 | 579 | 185 | 764 |
| **Total** | **3.759** | **1.241** | **5.000** |

---

### 11. Perbandingan Variabel Numerik Fraud dan Non-Fraud

Pemeriksaan rata-rata dilakukan terhadap variabel perilaku dan indikator risiko untuk memperoleh gambaran awal perbedaan antara data fraud dan non-fraud.

Hasil yang diperoleh menunjukkan bahwa nilai rata-rata `bot_likelihood_score` berbeda antara kedua kelompok:

| Status | Rata-rata `click_duration` | Rata-rata `bot_likelihood_score` |
|---|---:|---:|
| Non-Fraud (0) | 2,004850 | 0,378130 |
| Fraud (1) | 2,011273 | 0,874561 |

Nilai rata-rata `bot_likelihood_score` pada kelompok fraud lebih tinggi dibandingkan kelompok non-fraud. Temuan ini merupakan hasil eksplorasi awal dan belum dapat digunakan sebagai kesimpulan akhir mengenai penyebab fraud.

---

### 12. Kesimpulan Pemeriksaan Kualitas Data

Berdasarkan pemeriksaan awal terhadap dataset sebanyak 5.000 baris dan 21 kolom, tidak ditemukan missing value, data duplikat, maupun timestamp yang tidak valid. Nilai target `is_fraudulent` juga berada pada rentang 0 sampai 1.

Ditemukan 263 kandidat outlier pada `click_duration`, tetapi data tersebut tidak dihapus karena masih perlu dinilai berdasarkan konteks dan kebutuhan preprocessing.

Dataset secara umum dapat dilanjutkan ke tahap persiapan data. Tahap berikutnya mencakup penentuan format data utama, pemetaan kolom, normalisasi, dan persiapan dataset processed sesuai kebutuhan sistem.