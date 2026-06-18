import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from tools.common_info import cari_info_umum

query = "How long does shipping take?"

hasil = cari_info_umum(query)

print(hasil)