import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("nilai_siswa.csv")

print("=== INFO DATA ===")
print(data.info())

print("\n=== 5 DATA PERTAMA ===")
print(data.head())

print("\n=== STATISTIK DESKRIPTIF ===")
print(data.describe())

print("\n=== STATISTIK UMUM ===")
print("Rata-rata keseluruhan:", data["Nilai"].mean())
print("Median keseluruhan:", data["Nilai"].median())
print("Modus keseluruhan:", list(data["Nilai"].mode().values))

rata_per_mapel = data.groupby("Matpel")["Nilai"].mean().sort_values(ascending=False)
median_per_mapel = data.groupby("Matpel")["Nilai"].median()
mode_per_mapel = data.groupby("Matpel")["Nilai"].apply(lambda s: list(s.mode().values))
max_min_per_mapel = data.groupby("Matpel")["Nilai"].agg(["max", "min"])

print("\n=== RATA-RATA PER MATPEL ===")
print(rata_per_mapel)

print("\n=== MEDIAN PER MATPEL ===")
print(median_per_mapel)

print("\n=== MODUS PER MATPEL ===")
print(mode_per_mapel)

print("\n=== NILAI MAKSIMUM & MINIMUM PER MATPEL ===")
print(max_min_per_mapel)

rata_per_mapel.to_csv("summary_nilai_per_mapel.csv", header=["Rata-rata"])
print("\n✅ File 'summary_nilai_per_mapel.csv' berhasil dibuat!")

plt.figure(figsize=(7, 4))
rata_per_mapel.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Rata-Rata Nilai per Mata Pelajaran")
plt.xlabel("Mata Pelajaran")
plt.ylabel("Nilai Rata-Rata")
plt.tight_layout()
plt.savefig("rata_per_mapel.png")
plt.show()

plt.figure(figsize=(8, 5))
groups = [data[data["Matpel"] == m]["Nilai"].values for m in rata_per_mapel.index]
plt.boxplot(groups, labels=rata_per_mapel.index, patch_artist=True)
plt.title("Sebaran Nilai per Mata Pelajaran")
plt.xlabel("Mata Pelajaran")
plt.ylabel("Nilai")
plt.tight_layout()
plt.savefig("boxplot_per_mapel.png")
plt.show()

print("\n✅ Gambar telah disimpan sebagai:")
print(" - rata_per_mapel.png")
print(" - boxplot_per_mapel.png")

mapel_tertinggi = rata_per_mapel.idxmax()
nilai_tertinggi = rata_per_mapel.max()
mapel_terendah = rata_per_mapel.idxmin()
nilai_terendah = rata_per_mapel.min()

print("\n=== INTERPRETASI HASIL ===")
print(f"Mata pelajaran dengan rata-rata tertinggi adalah '{mapel_tertinggi}' dengan nilai {nilai_tertinggi:.2f}.")
print(f"Mata pelajaran dengan rata-rata terendah adalah '{mapel_terendah}' dengan nilai {nilai_terendah:.2f}.")
print("\nAnalisis selesai ✅")
