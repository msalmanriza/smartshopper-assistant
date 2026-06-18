# SmartShopper Assistant

SmartShopper Assistant adalah AI Assistant sederhana yang digunakan untuk menjawab pertanyaan umum e-commerce dan memberikan rekomendasi produk.

Project ini menggunakan MongoDB Atlas untuk menyimpan data FAQ, Sentence Transformer untuk retrieval, dan Groq sebagai LLM.

## Fitur

* Menjawab pertanyaan umum (pengiriman, pembayaran, refund, akun)
* Memberikan rekomendasi produk
* Routing otomatis berdasarkan pertanyaan user
* Penyimpanan data menggunakan MongoDB Atlas

## Struktur Project

```text
smartshopper_assistant/
│
├── data/
├── scripts/
├── tools/
├── app.py
├── requirements.txt
└── README.md
```
## Clone Repository
git clone https://github.com/msalmanriza/smartshopper-assistant.git
cd smartshopper-assistant

## Menjalankan Project

Install library:

```bash
pip install -r requirements.txt
```

Buat file `.env`:

```env
MONGO_URI=your_mongodb_uri
GROQ_API_KEY=your_groq_api_key
```

Simpan data ke MongoDB:

```bash
python scripts/store_data.py
```

Jalankan aplikasi:

```bash
python app.py
```

## Contoh Pertanyaan

```text
bagaimana cara membuat akun?

berapa lama pengiriman?

saya ingin laptop gaming

rekomendasi mouse gaming
```

## Teknologi

* Python
* MongoDB Atlas
* Sentence Transformers
* Groq API

## Author

Salmanrizaa
