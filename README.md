# HealthyRice AI

**Platform Deteksi Penyakit dan Rekomendasi Penanganan Tanaman Padi**

HealthyRice AI adalah aplikasi web berbasis kecerdasan buatan yang membantu petani mengenali penyakit pada daun padi hanya dari sebuah foto. Pengguna mengunggah atau memotret daun padi, lalu model computer vision mengklasifikasikan kondisi daun dan website menampilkan hasil diagnosis, tingkat keyakinan, serta rekomendasi penanganan awal.

Capstone Project **Dicoding Bootcamp Batch 14** · Grup **DB14-G002**

---

## 🔗 Tautan

Website https://healthyrice-wyjl.vercel.app

---

## Tim DB14-G002

| Name                       | Student ID   | Role                  |
| -------------------------- | ------------ | --------------------- |
| `Rafi Dzaki Azhari`        | `B26B14S008` | `Data Science`        |
| `Revino Sava Gavrila`      | `B26B14S003` | `Data Science`        |
| `IKG Wisnu Satryo Nugroho` | `B26B14R007` | `Fullstack Developer` |
| `Muhammad Najib Izzulhaq`  | `B26B14R011` | `Fullstack Developer` |

---

## Latar Belakang

Produktivitas padi di Indonesia masih terancam oleh penyakit daun seperti hawar daun bakteri, blast, dan tungro. Gejala awalnya sulit dibedakan secara visual oleh petani, sementara akses terhadap penyuluh dan ahli agronomi terbatas, terutama di pedesaan. Akibatnya penanganan sering terlambat dan risiko penurunan hasil panen meningkat. HealthyRice AI hadir agar petani dapat melakukan skrining awal secara cepat dan mudah.

---

## Fitur Utama

- **Deteksi penyakit dari foto**: unggah dari galeri (JPG/JPEG/PNG) atau ambil langsung dengan kamera.
- **Hasil diagnosis**: nama penyakit, tingkat keyakinan (_confidence_), dan deskripsi singkat.
- **Pengaman hasil**: foto yang bukan daun padi atau yang keyakinannya di bawah 80% tidak diberi diagnosis, dan pengguna diminta memotret ulang.
- **Informasi & penanganan penyakit**: penyebab, gejala, cara penanganan, pencegahan, dan sumber referensi untuk setiap penyakit.
- **Riwayat deteksi**: tersimpan per akun, bisa dibuka kembali, difilter, atau dihapus.
- **Akun pengguna**: registrasi dan login dengan autentikasi JWT.

---

## Tech Stack

| Bagian             | Teknologi                                                                     |
| ------------------ | ----------------------------------------------------------------------------- |
| Frontend           | React, Vite, React Router, Axios                                              |
| Backend            | Django, Django REST Framework, Simple JWT, drf-spectacular (Swagger/OpenAPI)  |
| Machine Learning   | PyTorch, timm, Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn, ONNX Runtime |
| Database           | PostgreSQL (Neon)                                                             |
| Penyimpanan Gambar | Vercel Blob                                                                   |
| Deployment         | Vercel (frontend & backend)                                                   |

---

## Arsitektur

```
┌──────────────┐   Axios (HTTPS)   ┌─────────────────────────┐
│   Frontend   │ ────────────────▶ │   Backend (Django DRF)  │
│ React + Vite │ ◀──────────────── │      /api/v1/...        │
└──────────────┘       JSON        └───────────┬─────────────┘
                                               │
                     ┌─────────────────────────┼─────────────────────────┐
                     ▼                         ▼                         ▼
             ┌───────────────┐       ┌──────────────────┐       ┌────────────────┐
             │ ONNX Runtime  │       │   PostgreSQL     │       │  Vercel Blob   │
             │ (model CNN)   │       │ user, penyakit,  │       │ (foto deteksi) │
             └───────────────┘       │ riwayat deteksi  │       └────────────────┘
                                     └──────────────────┘
```

---

## Struktur Proyek

```
.
├── Notebook_HealthyRiceAI.ipynb   # EDA, cleaning, training, evaluasi, export model
├── backend/                       # Django REST API
│   ├── api/index.py               # entry point serverless Vercel
│   ├── config/                    # settings & URL utama
│   ├── accounts/                  # registrasi, login (JWT), profil
│   ├── diseases/                  # katalog penyakit + seed data
│   ├── detection/                 # upload foto, inference, riwayat
│   │   ├── ml_engine.py           # preprocessing & inference ONNX
│   │   └── ml_assets/             # model ONNX, labels, config, model card
│   ├── core/                      # penanganan error API
│   ├── healthyriceai.postman_collection.json
│   ├── requirements.txt
│   └── vercel.json
└── frontend/                      # React + Vite
    ├── src/
    │   ├── pages/                 # Home, Upload, Result, History, Disease List/Detail, Login, Register
    │   ├── components/            # layout, kamera, kartu penyakit, section home
    │   ├── services/              # pemanggilan API (Axios)
    │   └── context/               # state autentikasi
    └── vercel.json
```
