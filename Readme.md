# Gesture Meme

Gesture Meme adalah aplikasi **Computer Vision** berbasis Python yang mendeteksi gesture tangan secara *real-time* menggunakan webcam dan menampilkan gambar meme hamster yang sesuai dengan gesture yang dikenali.

Aplikasi ini memanfaatkan **MediaPipe Hands** untuk mendeteksi landmark tangan, kemudian menggunakan pendekatan **Rule-Based Gesture Recognition** untuk mengklasifikasikan gesture berdasarkan posisi setiap jari. Setelah gesture dikenali, aplikasi akan menampilkan gambar meme hamster pada jendela terpisah.

> **Catatan:** Proyek ini tidak melakukan pelatihan (*training*) model Machine Learning sendiri. Model deteksi tangan berasal dari MediaPipe, sedangkan proses klasifikasi gesture diimplementasikan menggunakan logika berbasis aturan (*rule-based*) pada source code.

---

# Fitur

* Deteksi gesture tangan secara *real-time* menggunakan webcam.
* Menampilkan landmark tangan menggunakan MediaPipe.
* Klasifikasi gesture menggunakan metode Rule-Based.
* Menampilkan gambar meme hamster sesuai gesture yang dikenali.
* Mendukung deteksi hingga dua tangan (sesuai konfigurasi MediaPipe).
* Menampilkan dua jendela aplikasi secara bersamaan:

  * **Camera** → Menampilkan hasil deteksi tangan beserta landmark.
  * **Meme** → Menampilkan gambar hamster sesuai gesture.

---

# Pemetaan Gesture

| Gesture      | Deskripsi                    | Meme yang Ditampilkan           |
| ------------ | ---------------------------- | ------------------------------- |
| 👍 Thumb     | Jempol                       | Hamster pose jempol             |
| ✌ Peace      | Dua jari (telunjuk & tengah) | Hamster pose peace              |
| ✊ Fist       | Kepalan tangan               | Hamster ketakutan (*Screaming*) |
| 🖐 High Five | Lima jari terbuka            | Hamster mengangkat tangan       |

---

# Teknologi yang Digunakan

* Python 3.11.4
* OpenCV
* MediaPipe
* NumPy

---

# Cara Kerja Sistem

Aplikasi bekerja melalui tahapan berikut.

```text
Webcam
   │
   ▼
MediaPipe Hands
   │
   ▼
Deteksi 21 Landmark Tangan
   │
   ▼
Analisis Posisi Jari
   │
   ▼
Rule-Based Gesture Recognition
   │
   ▼
Menampilkan Meme Hamster
```

Tahapan klasifikasi gesture dilakukan melalui dua fungsi utama:

* **get_finger_states()** → Menentukan status setiap jari (terbuka atau tertutup).
* **classify_gesture()** → Mengklasifikasikan gesture berdasarkan kombinasi posisi jari.

---

# Tampilan Aplikasi

Folder `docs/screenshots/` berisi dokumentasi hasil pengujian aplikasi.

Setiap screenshot menampilkan dua jendela aplikasi secara bersamaan:

* Camera
* Meme

Screenshot yang tersedia:

* Thumb
* Peace
* Fist
* High Five

---

# Struktur Proyek

```text
Gesture-Meme/
│
├── assets/
│   ├── Happy.jpg
│   ├── Peace.jpg
│   ├── Screaming.jpg
│   └── Thumb.jpg
│
├── docs/
│   └── screenshots/
│
├── src/
│   ├── main.py
│   └── test.py
│
├── venv/
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# Instalasi

## Clone repository

```bash
git clone https://github.com/andiubaid09/hamster-gesture-meme.git
```

## Masuk ke folder proyek

```bash
cd gesture-meme
```

## Membuat Virtual Environment

Windows

```bash
python -m venv venv
```

Aktifkan Virtual Environment

Command Prompt (CMD)

```bash
venv\Scripts\activate
```

PowerShell

```powershell
venv\Scripts\Activate.ps1
```

## Install Dependency

```bash
pip install -r requirements.txt
```

---

# Menjalankan Program

Masuk ke folder `src`, kemudian jalankan:

```bash
python main.py
```

atau

```bash
python src/main.py
```

Tekan tombol **ESC** untuk menutup aplikasi.

---

# Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan pada proyek ini:

* Menambahkan lebih banyak gesture tangan.
* Menggunakan model Machine Learning untuk klasifikasi gesture.
* Menambahkan animasi meme.
* Menampilkan meme langsung pada jendela kamera.
* Menambahkan antarmuka pengguna (GUI).
* Mendukung gambar atau GIF sebagai output.
* Menambahkan dokumentasi video demonstrasi.

---

# Lisensi

Proyek ini menggunakan lisensi **MIT License**.

---

# Penulis

**Muhammad Andi Ubaidillah**

Mahasiswa Teknik Komputer Jaringan yang memiliki ketertarikan pada bidang Computer Vision, Machine Learning, dan Data Science.
