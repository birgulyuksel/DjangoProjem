import pandas as pd

# Örnek veri
data = [
    {"marka": "BMW", "model": "320i", "yil": 2020, "km": 50000, "fiyat": 700000, "sehir": "İstanbul"},
    {"marka": "Mercedes", "model": "C200", "yil": 2021, "km": 30000, "fiyat": 800000, "sehir": "Ankara"},
]

df = pd.DataFrame(data)  # Veriyi DataFrame'e çevir

print("DataFrame:")
print(df)

# Excel'e yazma
file_path = 'Yeni_Arac_Verileri_2.xlsx'
try:
    df.to_excel(file_path, index=False)
    print(f"Veriler {file_path} dosyasına başarıyla yazıldı.")
except Exception as e:
    print(f"Excel yazma hatası: {str(e)}")