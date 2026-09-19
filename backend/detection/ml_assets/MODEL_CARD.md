# HealthyRice AI - Model Card

## Ringkasan
- Arsitektur      : convnextv2_tiny.fcmae_ft_in22k_in1k (timm, transfer learning)
- Tugas           : klasifikasi 7 kelas (penyakit daun padi + kelas penolak not_rice)
- Kelas           : blast, blight, brown_spot, healthy, scald, tungro, not_rice
- Input           : RGB 224x224, NCHW, rentang 0..1 (model_web.onnx) / ternormalisasi (model.onnx)
- Tanggal training: 2026-09-17

## Data
- Total gambar setelah cleaning : 14325
- Split (group-aware, stratified): train 10035 / val 2141 / test 2149
- Anti-leakage: gambar near-duplicate (pHash Hamming <= 5) dikunci dalam group yang sama sehingga tidak tersebar antar split.

## Performa (test set)
| Metrik | Nilai |
|---|---|
| Accuracy | 0.9767 |
| Macro F1 | 0.9762 |
| Macro Precision | 0.9778 |
| Macro Recall | 0.9748 |

## Keterbatasan
- Dilatih pada dataset publik multi-source, performa pada foto HP di sawah nyata bisa lebih rendah (domain gap).
- Model tidak mengenali kondisi di luar 7 kelas (hama, defisiensi hara) - gunakan gerbang energy + confidence threshold 0.8.
- Ruang lingkup model hanya klasifikasi gambar (label + confidence). Rekomendasi penanganan dikelola aplikasi web.

## Cara pakai
Lihat `inference.py` dan `preprocess_config.json`.
