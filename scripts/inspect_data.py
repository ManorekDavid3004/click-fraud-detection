import pandas as pd

# Lokasi dataset
file_path = "data/raw/click_fraud_dataset.csv"

# Membaca dataset
df = pd.read_csv(file_path)

# Informasi dasar dataset
print("=" * 50)
print("INFORMASI DATASET")
print("=" * 50)

print("Jumlah baris :", len(df))
print("Jumlah kolom :", len(df.columns))

print("\nNama kolom:")
for column in df.columns:
    print("-", column)

print("\n5 data pertama:")
print(df.head())

print("\nTipe data setiap kolom:")
print(df.dtypes)

print("\nJumlah data kosong setiap kolom:")
print(df.isnull().sum())

print("\n" + "=" * 50)
print("PEMERIKSAAN DUPLIKAT")
print("=" * 50)

print("Jumlah baris duplikat:", df.duplicated().sum())
print("Jumlah click_id duplikat:", df["click_id"].duplicated().sum())


print("\n" + "=" * 50)
print("PEMERIKSAAN LABEL FRAUD")
print("=" * 50)

print("Nilai unik is_fraudulent:")
print(df["is_fraudulent"].unique())

print("\nJumlah masing-masing label:")
print(df["is_fraudulent"].value_counts())


print("\n" + "=" * 50)
print("INFORMASI STATISTIK")
print("=" * 50)

print(df.describe())

print("\n" + "=" * 50)
print("RINGKASAN DUPLIKAT")
print("=" * 50)

print("Duplicate seluruh baris :", df.duplicated().sum())
print("Duplicate click_id     :", df["click_id"].duplicated().sum())

print("\n" + "=" * 50)
print("TIPE DATA SETIAP KOLOM")
print("=" * 50)

print(df.dtypes)

print("\n" + "=" * 50)
print("PEMERIKSAAN NILAI UNIK KOLOM BINER")
print("=" * 50)

print("VPN_usage:", df["VPN_usage"].unique())
print("proxy_usage:", df["proxy_usage"].unique())
print("is_fraudulent:", df["is_fraudulent"].unique())


print("\n" + "=" * 50)
print("RENTANG DATA NUMERIK")
print("=" * 50)

numeric_columns = [
    "click_duration",
    "scroll_depth",
    "mouse_movement",
    "keystrokes_detected",
    "click_frequency",
    "time_since_last_click",
    "bot_likelihood_score"
]

print(df[numeric_columns].describe().T)


print("\n" + "=" * 50)
print("NILAI NEGATIF")
print("=" * 50)

for column in numeric_columns:
    negative_count = (df[column] < 0).sum()
    print(f"{column}: {negative_count}")

    print("\n" + "=" * 50)
print("PEMERIKSAAN TIMESTAMP")
print("=" * 50)

timestamp_check = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

invalid_timestamp = timestamp_check.isna().sum()

print("Jumlah timestamp tidak valid:", invalid_timestamp)

print("\nRentang waktu:")
print("Tanggal paling awal :", timestamp_check.min())
print("Tanggal paling akhir:", timestamp_check.max())

print("\n" + "=" * 50)
print("PEMERIKSAAN OUTLIER DENGAN IQR")
print("=" * 50)

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outlier_count = (
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ).sum()

    print(f"\n{column}")
    print(f"Q1           : {Q1}")
    print(f"Q3           : {Q3}")
    print(f"IQR          : {IQR}")
    print(f"Batas bawah  : {lower_bound}")
    print(f"Batas atas   : {upper_bound}")
    print(f"Jumlah outlier: {outlier_count}")

    print("\n" + "=" * 50)
print("PERBANDINGAN DATA FRAUD VS NON-FRAUD")
print("=" * 50)

comparison_columns = [
    "click_duration",
    "scroll_depth",
    "mouse_movement",
    "keystrokes_detected",
    "click_frequency",
    "time_since_last_click",
    "bot_likelihood_score"
]

comparison = df.groupby("is_fraudulent")[comparison_columns].mean()

print(comparison)

print("\n" + "=" * 50)
print("DISTRIBUSI LABEL FRAUD")
print("=" * 50)

label_count = df["is_fraudulent"].value_counts().sort_index()
label_percentage = df["is_fraudulent"].value_counts(
    normalize=True
).sort_index() * 100

print("Jumlah:")
print(label_count)

print("\nPersentase:")
print(label_percentage)

categorical_columns = [
    "device_type",
    "browser",
    "operating_system",
    "ad_position",
    "device_ip_reputation"
]

print("\n" + "=" * 50)
print("DISTRIBUSI KATEGORI BERDASARKAN STATUS FRAUD")
print("=" * 50)

for column in categorical_columns:
    print("\n---", column, "---")
    print(pd.crosstab(
        df[column],
        df["is_fraudulent"],
        margins=True
    ))

    binary_columns = [
    "VPN_usage",
    "proxy_usage"
]

print("\n" + "=" * 50)
print("VPN DAN PROXY VS FRAUD")
print("=" * 50)

for column in binary_columns:
    print("\n---", column, "---")
    print(pd.crosstab(
        df[column],
        df["is_fraudulent"],
        margins=True
    ))

    print("\n" + "=" * 50)
print("PEMERIKSAAN RENTANG NILAI")
print("=" * 50)

range_checks = {
    "click_duration": (0, None),
    "scroll_depth": (0, 100),
    "mouse_movement": (0, None),
    "keystrokes_detected": (0, None),
    "click_frequency": (0, None),
    "time_since_last_click": (0, None),
    "bot_likelihood_score": (0, 1),
    "VPN_usage": (0, 1),
    "proxy_usage": (0, 1),
    "is_fraudulent": (0, 1)
}

for column, (minimum, maximum) in range_checks.items():
    actual_min = df[column].min()
    actual_max = df[column].max()

    print(
        f"{column}: "
        f"min={actual_min}, max={actual_max}"
    )

    print("\n" + "=" * 50)
print("PEMERIKSAAN TIMESTAMP")
print("=" * 50)

timestamp = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

print("Jumlah timestamp tidak valid:",
      timestamp.isna().sum())

print("Timestamp minimum:",
      timestamp.min())

print("Timestamp maksimum:",
      timestamp.max())