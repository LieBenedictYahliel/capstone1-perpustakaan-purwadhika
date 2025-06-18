# Sistem Manajemen Perpustakaan - Python (Capstone Project)

Proyek ini merupakan implementasi sistem manajemen perpustakaan berbasis teks yang dikembangkan menggunakan bahasa pemrograman Python. Tujuan utama dari program ini adalah untuk menampilkan pemahaman terhadap konsep dasar pemrograman struktural, termasuk pengelolaan data dengan struktur list, kontrol alur program, pemisahan fungsi, serta penerapan validasi input.

Program memungkinkan pengguna untuk melakukan operasi dasar seperti menambahkan, menampilkan, mengubah, dan menghapus data buku (CRUD). Selain itu, disediakan fitur identifikasi peminjaman buku serta perhitungan denda keterlambatan. Program ini bersifat mandiri dan tidak terhubung dengan penyimpanan eksternal (database atau file), sehingga seluruh data bersifat sementara selama program berjalan.

Proyek ini dikembangkan sebagai bagian dari tugas akhir (capstone project) dan bertujuan sebagai portofolio yang merepresentasikan penguasaan materi dasar Python di tingkat pemula-menengah.

## Fitur Utama

- Login dan registrasi pengguna (dengan penyimpanan sementara)
- Penambahan data buku dengan validasi input
- Pengeditan data buku (judul, pengarang, penerbit, tahun terbit, genre, jumlah halaman, dan nama peminjam)
- Penghapusan data buku berdasarkan ID, judul, pengarang, genre, dan nama peminjam
- Identifikasi ID buku yang unik secara otomatis berdasarkan kombinasi data
- Penanganan data duplikat (dengan pemilihan berdasarkan ID)
- Pemeriksaan data peminjaman dan perhitungan denda
- Penampilan data dalam bentuk tabel teks yang terstruktur dan mudah dibaca

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal di perangkat.
2. Unduh file program dengan ekstensi `.py`.
3. Jalankan melalui terminal atau command prompt dengan perintah:
   ```
   python nama_file_program.py
   ```
4. Ikuti petunjuk yang ditampilkan di layar.

## Struktur File

```
📁 Sistem-Perpustakaan/
│
├── perpustakaan.py      # File utama yang berisi seluruh kode program
├── README.md            # File ini
```

## Contoh Tampilan Output

Berikut adalah contoh tampilan tabel data buku:

```
Book ID     | Judul Buku     | Nama Pengarang | Penerbit
---------------------------------------------------------
04BNA20     | Bumi           | Tere Liye      | Gramedia
04BPE20     | Perahu Kertas  | Dee Lestari    | Bentang
```

## Catatan Teknis

- Program ini tidak menggunakan database atau file eksternal. Semua data disimpan dalam memori selama program berjalan.
- ID buku dibentuk dari kombinasi tahun terbit, huruf awal judul, dan nama peminjam. Namun, ID tidak diperbarui secara otomatis apabila data penting (seperti judul atau peminjam) diubah.

## Tujuan Proyek

Capstone ini ditujukan untuk menunjukkan kemampuan dasar pemrograman Python, khususnya dalam:
- Mengelola data dalam list
- Membuat struktur fungsi terpisah
- Menangani validasi input
- Menampilkan data dalam bentuk terstruktur
- Melakukan operasi CRUD (Create, Read, Update, Delete)

## Informasi Peserta

Nama: JCDS 2702- Lie Benedict Yahliel
Tanggal Selesai: Juni 2025  
Kegiatan: Capstone Project - Purwadhika
