def asal_midir(sayi_3, bolen=2):
    if sayi_3 <= 1:
        return False
    if bolen * bolen > sayi_3:
        return True
    if sayi_3 % bolen == 0:
        return False
    return asal_midir(sayi_3, bolen + 1)


sayi_3 = int(input("Bir sayı girin: "))
if asal_midir(sayi_3):
    print(f"{sayi_3} asal bir sayıdır.")
else:
    print(f"{sayi_3} asal bir sayı değildir.")
