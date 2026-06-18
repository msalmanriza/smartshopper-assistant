import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Nice berhasil terhubung ke MongoDB Atlas")
except Exception as e:
    print("Koneksi gagal")
    print(e)