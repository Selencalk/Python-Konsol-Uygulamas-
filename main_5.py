from functools import reduce
from collections import defaultdict


def kelime_frekanslarini_hesapla(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        kelimeler = dosya.read().split()

    kelime_frekanslari = reduce(
        lambda akumulator, kelime: akumulator.update({kelime: akumulator.get(kelime, 0) + 1}) or akumulator,
        kelimeler,
        defaultdict(int)
    )

    return kelime_frekanslari


dosya_yolu = r'C:\Users\Selen\PycharmProjects\deneme0\main_5.txt'
sonuc = kelime_frekanslarini_hesapla(dosya_yolu)

if sonuc:
    print("Kelimelerin Frekansı:")
    for kelime, frekans in sonuc.items():
        print(f"{kelime}: {frekans}")
else:
    print("Dosya bulunamadı veya okunamadı.")
