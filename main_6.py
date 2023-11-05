def en_kucuk_bul(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        en_kucuk_sonraki_1 = en_kucuk_bul(liste[1:])
        if liste[0] < en_kucuk_sonraki_1:
            return liste[0]
        else:
            return en_kucuk_sonraki_1


liste = [18, 20, 35, 50, 44]
en_kucuk = en_kucuk_bul(liste)
print("En küçük değer:", en_kucuk)
