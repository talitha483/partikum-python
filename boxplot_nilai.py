import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("nilai_siswa.csv")

print(data.head())

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
