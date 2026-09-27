# DATA DICTIONARY
## Sistem Deteksi Fraud Klik Iklan Digital Menggunakan Machine Learning

### 1. Informasi Dataset

| Informasi | Keterangan |
|---|---|
| Nama Dataset | Fraud Detection Dataset |
| Jumlah Baris | 5.000 |
| Jumlah Kolom | 21 |
| Target/Label | `is_fraudulent` |
| Jenis Permasalahan | Klasifikasi biner |
| Nilai Label | 0 = Non-Fraud, 1 = Fraud |
| Sumber | Kaggle |
| Author | ziya07 |

---

### 2. Struktur Data

Dataset terdiri dari data identitas klik, informasi perangkat dan lingkungan pengguna, informasi halaman, perilaku pengguna saat melakukan klik, indikator risiko, serta label yang menunjukkan apakah suatu klik termasuk fraudulent atau tidak.

| No | Nama Kolom | Tipe Data | Peran | Deskripsi |
|---:|---|---|---|---|
| 1 | `click_id` | Object | Identifier | Identitas unik untuk setiap data klik. |
| 2 | `timestamp` | Object | Input | Waktu ketika aktivitas klik tercatat. |
| 3 | `user_id` | Object | Input/Identifier | Identitas pengguna yang melakukan klik. |
| 4 | `ip_address` | Object | Input/Identifier | Alamat IP yang digunakan saat melakukan klik. |
| 5 | `device_type` | Object | Input | Jenis perangkat yang digunakan, seperti Desktop, Mobile, atau Tablet. |
| 6 | `browser` | Object | Input | Browser yang digunakan ketika melakukan klik. |
| 7 | `operating_system` | Object | Input | Sistem operasi perangkat yang digunakan. |
| 8 | `referrer_url` | Object | Input | URL atau sumber halaman yang mengarahkan pengguna sebelum aktivitas klik. |
| 9 | `page_url` | Object | Input | URL halaman yang berkaitan dengan aktivitas klik iklan. |
| 10 | `click_duration` | Float | Input/Behavior | Nilai yang menunjukkan durasi aktivitas klik. |
| 11 | `scroll_depth` | Integer | Input/Behavior | Nilai yang menunjukkan kedalaman scrolling pengguna pada halaman. |
| 12 | `mouse_movement` | Integer | Input/Behavior | Jumlah atau tingkat aktivitas pergerakan mouse yang tercatat. |
| 13 | `keystrokes_detected` | Integer | Input/Behavior | Jumlah aktivitas penekanan tombol yang terdeteksi. |
| 14 | `ad_position` | Object | Input | Posisi iklan pada halaman, seperti Top, Side, atau Bottom. |
| 15 | `click_frequency` | Integer | Input/Behavior | Frekuensi klik yang tercatat dalam aktivitas pengguna. |
| 16 | `time_since_last_click` | Integer | Input/Behavior | Jarak waktu sejak aktivitas klik sebelumnya. |
| 17 | `device_ip_reputation` | Object | Input/Risk Indicator | Reputasi perangkat atau alamat IP yang dikategorikan sebagai Good, Suspicious, atau Bad. |
| 18 | `VPN_usage` | Integer | Input/Risk Indicator | Indikator penggunaan VPN, dengan 0 = tidak menggunakan dan 1 = menggunakan. |
| 19 | `proxy_usage` | Integer | Input/Risk Indicator | Indikator penggunaan proxy, dengan 0 = tidak menggunakan dan 1 = menggunakan. |
| 20 | `bot_likelihood_score` | Float | Input/Risk Indicator | Nilai yang menunjukkan tingkat kemungkinan aktivitas berasal dari bot. |
| 21 | `is_fraudulent` | Integer | Target/Label | Label klasifikasi klik. Nilai 0 menunjukkan non-fraud dan nilai 1 menunjukkan fraud. |

---

### 3. Kelompok Variabel

#### A. Identitas dan Informasi Klik
- `click_id`
- `timestamp`
- `user_id`
- `ip_address`

#### B. Informasi Perangkat dan Lingkungan
- `device_type`
- `browser`
- `operating_system`

#### C. Informasi Halaman
- `referrer_url`
- `page_url`
- `ad_position`

#### D. Perilaku Pengguna
- `click_duration`
- `scroll_depth`
- `mouse_movement`
- `keystrokes_detected`
- `click_frequency`
- `time_since_last_click`

#### E. Indikator Risiko
- `device_ip_reputation`
- `VPN_usage`
- `proxy_usage`
- `bot_likelihood_score`

#### F. Target
- `is_fraudulent`

---

### 4. Variabel Target

Variabel target yang digunakan dalam sistem adalah:

`is_fraudulent`

Keterangan nilai:

| Nilai | Keterangan |
|---:|---|
| 0 | Non-Fraud |
| 1 | Fraud |

Variabel `is_fraudulent` menjadi target yang akan diprediksi oleh model machine learning pada tahap pengembangan model.

---

### 5. Ringkasan Struktur Dataset

Dataset memiliki 5.000 baris dan 21 kolom. Variabel yang tersedia mencakup informasi klik, pengguna, perangkat, aktivitas perilaku, indikator risiko, dan label fraud.

Data dengan label `is_fraudulent = 0` berjumlah 3.759 data, sedangkan data dengan label `is_fraudulent = 1` berjumlah 1.241 data.

Dataset ini digunakan sebagai data awal (raw data) untuk proses pemeriksaan, persiapan, dan pengolahan data sebelum digunakan pada tahap machine learning.