def hedefe_en_yakin_cifti_bul(hedef_toplam, benim_listem):
    if not benim_listem or len(benim_listem) < 2:
        return None

    sirali_liste = sorted(benim_listem)

    en_yakin_cift = (sirali_liste[0], sirali_liste[1])
    min_fark = abs(hedef_toplam - sum(en_yakin_cift))

    for i in range(len(sirali_liste) - 1):
        for j in range(i + 1, len(sirali_liste)):
            mevcut_cift = (sirali_liste[i], sirali_liste[j])
            mevcut_fark = abs(hedef_toplam - sum(mevcut_cift))

            if mevcut_fark < min_fark:
                en_yakin_cift = mevcut_cift
                min_fark = mevcut_fark

    return en_yakin_cift


hedef_toplam = 10
benim_listem = [1, 5, 8, 2, 3, 7]
sonuc = hedefe_en_yakin_cifti_bul(hedef_toplam, benim_listem)

if sonuc is not None:
    print(f"Belirtilen sayıya en yakın çift: {sonuc}")
else:
    print("Liste boş veya eleman sayısı yetersiz.")
