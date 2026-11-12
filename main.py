import random

hikayeler = [
    ("Kimse Bu Kuyuya Bakamiyor", "Bu koyde 40 yildir kimse bu kuyuya bakamiyor. Her gece saat 03:00'te kuyudan bir ses geliyor."),
    ("Eve Giren Cikamiyor", "Bu ev 20 yildir bos. Sahibi var ama girmiyor. Geceleri isiklari kendi kendine yaniyor."),
]

baslik, metin = random.choice(hikayeler)
print(baslik)
print(metin)
