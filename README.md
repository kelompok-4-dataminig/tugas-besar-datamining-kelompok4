# Judul Kasus
Prediksi Kelayakan Pinjaman Menggunakan Algoritma Data Mining

## Anggota Kelompok & NIM
- M Fachriza Farhan (714220005)
- Muhammad Rafli Alfarisi (714220008)
- Fulandi Hudza Grahitama (714220010)
- Fathya Fathimah Azzahra (714220012)

## Deskripsi Kasus
Proyek ini bertujuan untuk menganalisis sentimen dari berbagai ulasan konsumen terhadap produk sunscreen Amaterasun UV Serum, guna memahami persepsi dan tanggapan pelanggan, mengidentifikasi sentimen positif, negatif, atau netral, serta mengevaluasi aspek-aspek yang paling memengaruhi kepuasan pengguna terhadap produk tersebut.  
Analisis ini diharapkan dapat memberikan wawasan yang berguna dalam pengambilan keputusan strategis untuk pemasaran, peningkatan kualitas produk, dan pengembangan produk serupa di masa mendatang.

## Sumber Dataset
Dataset diambil dari hasil scraping ulasan pengguna terhadap produk sunscreen **Amaterasun UV Serum SPF 50+ PA++++** pada situs Female Daily:  
🔗 [https://reviews.femaledaily.com/products/moisturizer/sun-protection-1/amaterasun/uv-sunscreen-serum-spf-50-pa?cat=&cat_id=0&age_range=&skin_type=&skin_tone=&skin_undertone=&hair_texture=&hair_type=&order=newest&page=2](https://reviews.femaledaily.com/products/moisturizer/sun-protection-1/amaterasun/uv-sunscreen-serum-spf-50-pa?cat=&cat_id=0&age_range=&skin_type=&skin_tone=&skin_undertone=&hair_texture=&hair_type=&order=newest&page=2)

Scraping dilakukan dari halaman-halaman ulasan dengan menggunakan teknik web scraping berbasis Python (menggunakan pustaka `requests`, `BeautifulSoup`, dan `pandas`).

Datasetnya juga diambil dari platform X

## Langkah Preprocessing
1. **Cleaning**: Menghapus karakter spesial, angka, dan tanda baca yang tidak diperlukan.
2. **Case Folding**: Mengubah seluruh teks ke huruf kecil.
3. **Tokenization**: Memisahkan kalimat menjadi kata-kata.
4. **Stopword Removal**: Menghapus kata-kata umum yang tidak memiliki makna signifikan.
5. **Stemming**: Mengembalikan kata ke bentuk dasarnya menggunakan Sastrawi.
6. **Labeling Sentimen**: Memberi label sentimen (positif, negatif, netral) secara manual atau semi-otomatis.

## Algoritma yang Digunakan
- **Naive Bayes (NB)**  
  Digunakan untuk klasifikasi sentimen berdasarkan probabilitas kemunculan kata.
  
- **Support Vector Machine (SVM)**  
  Digunakan untuk membentuk hyperplane optimal dalam membedakan kelas sentimen.

- **Logistic Regression**  
  Digunakan untuk memprediksi probabilitas suatu ulasan termasuk ke dalam kategori sentimen tertentu.

## Evaluasi & Hasil
Evaluasi dilakukan menggunakan beberapa metrik performa model:
- **Akurasi**
- **Precision**
- **Recall**
- **F1-Score**
- **Confusion Matrix**

Hasil evaluasi menunjukkan bahwa:
- **SVM** memberikan akurasi terbaik sebesar **0.7881/78%**  
- **Logistic Regression** berada di urutan kedua dengan akurasi **0.7458/74%**  
- **Naive Bayes** memberikan hasil akurasi **0.6949/69%**

## Cara Menjalankan
1. Clone repository ke lokal:
   ```bash
   git clone https://github.com/kelompok-4-dataminig/tugas-besar-datamining-kelompok4.git

2. Jalankan file run.sh yang ada pada folder tersebut
