def en_kucuk_eleman(k, giris_listesi):
    if not giris_listesi or k <= 0 or k > len(giris_listesi):
        return None

    sirali_liste = sorted(giris_listesi)

    en_kucuk = sirali_liste[k - 1]
    return en_kucuk


benim_listem = [5, 7, 9, 4, 6, 8]
k_degeri = 1
sonuc = en_kucuk_eleman(k_degeri, benim_listem)

if sonuc is not None:
    print(f"{k_degeri}. en küçük eleman: {sonuc}")
else:
    print("Geçersiz k değeri veya boş liste.")
