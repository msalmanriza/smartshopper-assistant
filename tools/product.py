def rekomendasi_produk(query: str) -> str:
    """Rekomendasi produk berdasarkan kebutuhan user."""

    q = query.lower()

    if "laptop" in q or "gaming" in q:
        return "Rekomendasi: ASUS TUF Gaming A15, Lenovo LOQ 15, atau Acer Nitro V."

    if "hp" in q or "smartphone" in q:
        return "Rekomendasi: Samsung Galaxy A55, Redmi Note 13 Pro, atau iPhone 13."

    if "headset" in q:
        return "Rekomendasi: HyperX Cloud Stinger atau Logitech H390."

    if "mouse" in q:
        return "Rekomendasi: Logitech G304 atau Rexus Daxa Air."
    
    if "makanan" in q:
        return "Rekomendasi: makanan ringan, minuman kemasan, dan camilan harian."

    return "Sebutkan jenis produk yang ingin dicari, misalnya laptop, smartphone, headset, mouse, makanan."