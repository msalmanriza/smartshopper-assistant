import json
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["smartshopper"]
collection = db["common_info"]

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/common_info.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)

data = raw_data["questions"]

collection.delete_many({})

for item in data:
    teks = item["question"] + " " + item["answer"]
    item["embedding"] = model.encode(teks).tolist()
    collection.insert_one(item)

print("data berhasil kesimpan")