def tekrar_edan_elemanlari_bul(giris_listesi):
    if not giris_listesi or len(giris_listesi) < 2:
        return None

    benzersiz_elemanlar = set()
    tekrarlar = {eleman for eleman in giris_listesi if eleman in benzersiz_elemanlar or benzersiz_elemanlar.add(eleman)}

    return list(tekrarlar)


benim_listem = [1, 2, 3, 2, 4, 5, 6, 5, 7, 8]
sonuc = tekrar_edan_elemanlari_bul(benim_listem)

if sonuc is not None:
    print(f"Tekrar eden elemanlar: {sonuc}")
else:
    print("Liste boş veya eleman sayısı yetersiz.")
