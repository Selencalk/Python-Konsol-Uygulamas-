def en_buyuk_ortak_bolen(sayi1, sayi2):
    if sayi2 == 0:
        return sayi1
    else:
        return en_buyuk_ortak_bolen(sayi2, sayi1 % sayi2)


sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
ebob = en_buyuk_ortak_bolen(sayi1, sayi2)
print(f"{sayi1} ve {sayi2} sayılarının en büyük ortak böleni: {ebob}")
