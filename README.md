# SmartShopper Assistant

SmartShopper Assistant adalah AI Assistant sederhana yang dibuat untuk membantu pengguna mencari informasi umum toko dan memberikan rekomendasi produk berdasarkan kebutuhan pengguna.

Project ini menggunakan MongoDB sebagai penyimpanan data FAQ, Sentence Transformer untuk membuat embedding, dan Groq sebagai Large Language Model (LLM).

## Fitur

* Menjawab pertanyaan umum toko
* Memberikan rekomendasi produk
* Menggunakan MongoDB Atlas sebagai database
* Retrieval informasi berdasarkan kemiripan pertanyaan
* Integrasi dengan Groq API

## Struktur Project

```text
smartshopper_assistant/
│
├── data/
│   └── common_info.json
│
├── scripts/
│   ├── store_data.py
│   ├── test_connection.py
│   └── test_retrieval.py
│
├── tools/
│   ├── common_info.py
│   └── product.py
│
├── app.py
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

## Instalasi

Clone repository:

```bash
git clone https://github.com/msalmanriza
cd smartshopper_assistant
```

Install dependency:

```bash
pip install -r requirements.txt
```

Buat file `.env`:

```env
MONGO_URI=your_mongodb_connection
GROQ_API_KEY=your_groq_api_key
```

## Menyimpan Data ke MongoDB

Jalankan:

```bash
python scripts/store_data.py
```

## Menjalankan Assistant

```bash
python app.py
```

Contoh pertanyaan:

* Bagaimana cara membuat akun?
* Apa metode pembayaran yang tersedia?
* Saya ingin mencari laptop gaming
* Rekomendasi smartphone

## Teknologi yang Digunakan

* Python
* MongoDB Atlas
* Sentence Transformers
* Groq API
* PyMongo

## Hasil

Assistant dapat mengambil informasi dari database MongoDB dan memberikan jawaban sesuai konteks pertanyaan pengguna.
