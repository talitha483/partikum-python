<img width="1919" height="1079" alt="Screenshot 2025-11-13 112336" src="https://github.com/user-attachments/assets/99cca2e2-7474-434c-861a-ca18b8cddf1d" />
<img width="1917" height="1079" alt="Screenshot 2025-11-13 112408" src="https://github.com/user-attachments/assets/9136b94f-d894-496f-9a4b-126706ca7a5f" />
 Analisis Data & Visualisasi Data

Mata Pelajaran: Koding Kecerdasan Artifisial
Kelas: XI RPL

 Tujuan Pembelajaran

Siswa mampu menghitung ukuran statistik dasar menggunakan Pandas.

Siswa mampu menganalisis pola data berdasarkan rata-rata dan persebaran.

Siswa mampu membuat visualisasi data sederhana menggunakan Matplotlib dan Seaborn.
 Langkah Kerja Praktikum
1️ Instalasi Library

Buka VS Code, Jupyter Notebook, atau Google Colab, lalu jalankan perintah berikut di Terminal:
pip install pandas
pip install matplotlib
pip install seaborn

2️ Siapkan Dataset

Buat file bernama nilai_siswa.csv dan isi dengan data berikut:
Nama,Matpel,Nilai
Ade,Bahasa Indonesia,87
Aira,Bahasa Indonesia,88
Badi,Bahasa Inggris,78
Cyla,Bahasa Inggris,90
Khansa,Matematika,98
Maya,Bahasa Inggris,85
Dwi,Matematika,85
Raka,Fisika,95
Rasya,Fisika,90
Mala,Produktif,80
Sania,Fisika,86
Agus,Bahasa Indonesia,87
Gilam,Bahasa Indonesia,75
Rudi,Fisika,75
Faizal,Produktif,80
Hanif,Produktif,90
Danish,Produktif,85
Darian,Produktif,85
Evelyn,Fisika,90
Raina,Fisika,95
Ade,Fisika,90
Rasya,Fisika,85

3️ Jalankan Kode Analisis
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

4️ Visualisasi Menggunakan Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("nilai_siswa.csv")

if 'Matpel' in data.columns:
    data = data.rename(columns={'Matpel': 'Mapel'})

plt.figure(figsize=(8,5))
sns.boxplot(x="Mapel", y="Nilai", data=data, palette="Set2")
sns.stripplot(x="Mapel", y="Nilai", data=data, color="black", size=4, jitter=True)

plt.title("Sebaran Nilai Siswa per Mata Pelajaran", fontsize=12)
plt.xlabel("Mata Pelajaran")
plt.ylabel("Nilai")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

 Hasil Ringkasan Nilai per Mapel
| Mata Pelajaran   | Rata-rata |
| ---------------- | --------- |
| Matematika       | 91.50     |
| Fisika           | 88.25     |
| Bahasa Inggris   | 84.33     |
| Bahasa Indonesia | 84.25     |
| Produktif        | 84.00     |

 Analisis dan Pertanyaan

1. Mapel mana yang memiliki rata-rata nilai tertinggi?
 Matematika (91.5) memiliki rata-rata tertinggi dari seluruh mata pelajaran.

2. Mapel mana yang memiliki rata-rata nilai terendah?
 Produktif (84.0) memiliki rata-rata nilai terendah.

3. Bagaimana visualisasi membantu dalam memahami data?
 Visualisasi seperti bar chart dan boxplot membantu memahami perbedaan antar-mapel dan persebaran nilai siswa secara cepat dan menarik.

 Refleksi Siswa

1. Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data?
 Saya belajar menggunakan Pandas, Matplotlib, dan Seaborn untuk membaca data, menghitung statistik, serta membuat grafik otomatis.

2. Kesulitan apa yang kamu alami dalam membuat grafik?
 Mengatur tampilan grafik agar rapi dan menangani error saat membaca file CSV.

3. Menurut kamu, apakah AI membantu dalam analisis sebuah data?
 Ya, AI sangat membantu karena bisa mengolah data besar dengan cepat, menganalisis pola, dan menghasilkan prediksi yang akurat.

 Disusun oleh: Talitha Alya Aurely XI RPL
Mata Pelajaran Koding Kecerdasan Artifisial
