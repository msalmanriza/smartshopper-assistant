import os
import numpy as np

from dotenv import load_dotenv
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["smartshopper"]
collection = db["common_info"]

model = SentenceTransformer("all-MiniLM-L6-v2")


def hitung_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def cari_info_umum(query: str) -> str:
    """Cari info umum toko dari data FAQ."""
    
    data = list(collection.find({}, {"_id": 0}))

    if not data:
        return "Informasi belum tersedia nih dari data toko."

    kata_kunci = {
        "shipping": ["shipping", "delivery", "pengiriman", "kirim"],
        "payment": ["payment", "pembayaran", "bayar"],
        "refund": ["refund", "return", "retur"],
        "account": ["account", "akun", "sign up", "daftar"],
        "cancel": ["cancel", "batal"],
        "track": ["track", "lacak"]
    }

    q = query.lower()

    for daftar_kata in kata_kunci.values():
        if any(kata in q for kata in daftar_kata):
            for item in data:
                isi = (item["question"] + " " + item["answer"]).lower()
                if any(kata in isi for kata in daftar_kata):
                    return item["answer"]

    query_vector = model.encode(query).tolist()

    hasil = []
    for item in data:
        score = hitung_similarity(query_vector, item["embedding"])
        hasil.append((score, item))

    hasil.sort(key=lambda x: x[0], reverse=True)

    return hasil[0][1]["answer"]