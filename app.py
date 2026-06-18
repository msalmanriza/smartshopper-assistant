import os

from dotenv import load_dotenv
from groq import Groq

from tools.common_info import cari_info_umum
from tools.product import rekomendasi_produk

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def pilih_tool(pesan):
    teks = pesan.lower()

    info_words = [
        "shipping", "delivery", "pengiriman", "kirim",
        "payment", "pembayaran", "bayar",
        "refund", "return", "retur",
        "account", "akun", "daftar", "sign up",
        "cancel", "batal",
        "track", "tracking", "lacak"
    ]

    if any(kata in teks for kata in info_words):
        return "common"

    return "product"


def jawab(pesan):
    tool = pilih_tool(pesan)

    if tool == "common":
        konteks = cari_info_umum(pesan)
    else:
        konteks = rekomendasi_produk(pesan)

    prompt = f"""
Kamu adalah SmartShopper Assistant.
Jawab singkat, jelas, dan sesuai konteks user.

Pertanyaan user:
{pesan}

Data dari tool:
{konteks}
"""

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return res.choices[0].message.content


if __name__ == "__main__":
    print("SmartShopper Assistant siap. Ketik 'exit' untuk keluar.\n")

    while True:
        pesan = input("User: ")

        if pesan.lower() == "exit":
            break

        hasil = jawab(pesan)
        print("Assistant:", hasil)
        print()