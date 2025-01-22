# Google Scholar Scraper

Google Scholar Scraper merupakan program Python yang digunakan untuk mencari dan mengambil data artikel dari Google Scholar berdasarkan kata kunci, rentang tahun, dan jumlah artikel yang diinginkan. Hasil pencarian akan ditampilkan di konsol dan disimpan dalam file Excel.

## Persyaratan
Pastikan Anda telah menginstal Python dan library berikut sebelum menjalankan program:

- Selenium
- BeautifulSoup4
- Pandas
- Webdriver-Manager
- OpenPyxl

### Instalasi Library

1. Install library secara manual menggunakan perintah:
   ```bash
   pip install selenium beautifulsoup4 pandas webdriver-manager openpyxl
   ```

2. Alternatifnya, install semua library yang dibutuhkan dari file `requirements.txt` dengan perintah:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Program

1. Jalankan program dengan perintah:
   ```bash
   python google_scholar_scraper.py
   ```

2. Program akan meminta Anda untuk memasukkan data berikut:

   - **Kata Kunci**: Masukkan kata kunci pencarian artikel yang diinginkan.
   - **Tahun Awal**: Masukkan tahun awal dari rentang pencarian.
   - **Tahun Akhir**: Masukkan tahun akhir dari rentang pencarian.
   - **Jumlah Artikel**: Masukkan jumlah artikel yang ingin diambil.

3. Setelah data dimasukkan, program akan memproses pencarian artikel di Google Scholar.

## Hasil

- Artikel-artikel yang ditemukan akan ditampilkan di konsol.
- Data artikel juga akan disimpan dalam file Excel dengan format nama file berdasarkan kata kunci pencarian.

## File Output
File Excel hasil pencarian akan berisi kolom-kolom berikut:

- **Judul Jurnal**: Judul artikel yang ditemukan.
- **Penulis**: Nama penulis artikel.
- **Tahun Publikasi**: Tahun terbit artikel.
- **Abstrak**: Deskripsi atau ringkasan artikel.
- **DOI/URL**: Link ke artikel.
- **Jumlah Sitasi**: Informasi jumlah sitasi artikel (jika tersedia).

