import pandas as pd
from pathlib import Path


# ==========================================
# 1. Lokasi file
# ==========================================

INPUT_FILE = Path("data/raw/click_fraud_dataset.csv")
OUTPUT_FILE = Path("data/processed/click_fraud_dataset_processed.csv")


# ==========================================
# 2. Membaca dataset
# ==========================================

print("Membaca dataset...")

df = pd.read_csv(INPUT_FILE)

print("Dataset berhasil dibaca.")
print("Jumlah baris :", len(df))
print("Jumlah kolom:", len(df.columns))


# ==========================================
# 3. Memeriksa kolom
# ==========================================

expected_columns = [
    "click_id",
    "timestamp",
    "user_id",
    "ip_address",
    "device_type",
    "browser",
    "operating_system",
    "referrer_url",
    "page_url",
    "click_duration",
    "scroll_depth",
    "mouse_movement",
    "keystrokes_detected",
    "ad_position",
    "click_frequency",
    "time_since_last_click",
    "device_ip_reputation",
    "VPN_usage",
    "proxy_usage",
    "bot_likelihood_score",
    "is_fraudulent"
]

missing_columns = [
    column for column in expected_columns
    if column not in df.columns
]

if missing_columns:
    print("Kolom yang tidak ditemukan:")
    print(missing_columns)
    raise ValueError("Struktur kolom dataset tidak sesuai.")


print("Semua kolom sesuai dengan mapping.")


# ==========================================
# 4. Parsing timestamp
# ==========================================

print("\nMemproses timestamp...")

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

invalid_timestamp = df["timestamp"].isna().sum()

print("Timestamp tidak valid:", invalid_timestamp)


# ==========================================
# 5. Normalisasi kolom indikator
# ==========================================

print("\nMemeriksa kolom indikator...")

for column in ["VPN_usage", "proxy_usage", "is_fraudulent"]:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ==========================================
# 6. Memastikan label 0 dan 1
# ==========================================

invalid_label = ~df["is_fraudulent"].isin([0, 1])

print(
    "Jumlah label di luar 0/1:",
    invalid_label.sum()
)


# ==========================================
# 7. Membuat folder output
# ==========================================

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# 8. Menyimpan dataset hasil persiapan
# ==========================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nDataset berhasil disimpan.")
print("Lokasi:", OUTPUT_FILE)


# ==========================================
# 9. Ringkasan hasil
# ==========================================

print("\n====================================")
print("RINGKASAN DATASET HASIL PERSIAPAN")
print("====================================")

print("Jumlah baris :", len(df))
print("Jumlah kolom:", len(df.columns))

print("\nMissing value:")
print(df.isnull().sum().sum())

print("\nDistribusi label:")
print(df["is_fraudulent"].value_counts())

print("\nProses persiapan data selesai.")