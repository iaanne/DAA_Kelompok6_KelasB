# DAA_KELOMPOK6_KELASB

Menggunakan bahasa dan library:

- ![Python](https://img.shields.io/badge/Python-3.x-blue)  
  Bahasa pemrograman utama yang digunakan dalam implementasi algoritma.

- ![NumPy](https://img.shields.io/badge/NumPy-latest-orange)  
  Digunakan untuk operasi numerik dan pengolahan array.

- ![Pandas](https://img.shields.io/badge/Pandas-latest-purple)  
  Digunakan untuk analisis dan pengelolaan data hasil eksperimen.

- ![Matplotlib](https://img.shields.io/badge/Matplotlib-latest-green)  
  Digunakan untuk visualisasi grafik dan perbandingan performa algoritma.

- ![Seaborn](https://img.shields.io/badge/Seaborn-latest-blueviolet)  
  Digunakan untuk visualisasi statistik yang lebih informatif.

---
## 📌 Gambaran Umum

**DAA_Kelompok6_KelasB** adalah project mata kuliah Desain dan Analisis Algothma untuk menyelesaikan dan menganalisis **masalah 0/1 Knapsack** menggunakan beberapa pendekatan algoritma, yaitu **Greedy**, **Dynamic Programming**, dan **Branch and Bound**.

Project ini mendukung pembuatan data knapsack secara otomatis serta menyediakan metrik performa yang detail, sehingga sangat cocok digunakan untuk eksperimen, analisis, dan perbandingan algoritma optimasi.

---

## 👥 Anggota Kelompok
- Nadhifa Sakha Tri Yasmin – L0224036

- Adrian Farrel Aziz Yatyoga - L0224040

---

### ❓ Mengapa DAA_Kelompok6_KelasB?

* 🔁 **Keberagaman Algoritma**
  Mengimplementasikan algoritma Greedy, Dynamic Programming, dan Branch and Bound untuk menyelesaikan masalah knapsack dari berbagai sudut pandang.

* 🎲 **Pembuatan Data Otomatis**
  Mampu menghasilkan dataset knapsack secara acak untuk kebutuhan pengujian dan benchmarking.

* 📊 **Metrik Performa**
  Menyediakan informasi seperti waktu eksekusi, kualitas solusi, dan penggunaan sumber daya.

* 🧪 **Eksperimen yang Fleksibel**
  Memudahkan pengguna dalam mengatur parameter dan membandingkan berbagai pendekatan algoritma.

* 📝 **Analisis Solusi**
  Menyajikan hasil dan laporan perbandingan untuk mengevaluasi efektivitas setiap algoritma.

---

## 🚀 Instalasi

Build **DAA_Kelompok6_KelasB** dari source dan install dependensi yang dibutuhkan:

1. **Clone repository**

   ```bash
   git clone https://github.com/username/DAA_Kelompok6_KelasB
   ```

2. **Masuk ke direktori proyek**

   ```bash
   cd DAA_Kelompok6_KelasB
   ```

3. **Install dependensi** (menggunakan pip)

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Penggunaan

Jalankan proyek dengan perintah berikut:

```bash
python run.py --instance data/knapsack_labA_inv.json --algo greedy
```

Pilihan algoritma yang tersedia:

* **Greedy**

  ```bash
  python run.py --instance data/knapsack_labA_inv.json --algo greedy
  ```

* **Dynamic Programming**

  ```bash
  python run.py --instance data/knapsack_labA_inv.json --algo dp
  ```

* **Branch and Bound**

  ```bash
  python run.py --instance data/knapsack_labA_inv.json --algo bnb
  ```

---

