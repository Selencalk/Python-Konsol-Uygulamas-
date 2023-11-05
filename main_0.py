import subprocess


def secenek_1():
    print("Seçenek 1 seçildi")
    subprocess.run(["python", "main_1.py"])
    return "Seçenek 1 işlem sonucu"


def secenek_2():
    print("Seçenek 2 seçildi")
    subprocess.run(["python", "main_2.py"])
    return "Seçenek 2 işlem sonucu"


def secenek_3():
    print("Seçenek 3 seçildi")
    subprocess.run(["python", "main_3.py"])
    return "Seçenek 3 işlem sonucu"


def secenek_4():
    print("Seçenek 4 seçildi")
    subprocess.run(["python", "main_4.py"])
    return "Seçenek 4 işlem sonucu"


def secenek_5():
    print("Seçenek 5 seçildi")
    subprocess.run(["python", "main_5.py"])
    return "Seçenek 5 işlem sonucu"


def secenek_6():
    print("Seçenek 6 seçildi")
    subprocess.run(["python", "main_6.py"])
    return "Seçenek 6 işlem sonucu"


def secenek_7():
    print("Seçenek 7 seçildi")
    subprocess.run(["python", "main_7.py"])
    return "Seçenek 7 işlem sonucu"


def secenek_8():
    print("Seçenek 8 seçildi")
    subprocess.run(["python", "main_8.py"])
    return "Seçenek 8 işlem sonucu"


def secenek_9():
    print("Seçenek 9 seçildi")
    subprocess.run(["python", "main_9.py"])
    return "Seçenek 9 işlem sonucu"


def secenek_10():
    print("Seçenek 10 seçildi")
    subprocess.run(["python", "main_10.py"])
    return "Seçenek 10 işlem sonucu"


def cikis_0():
    print("Çıkış 0 seçildi")
    return "Çıkış 0 işlem sonucu"


def main_menu():
    while True:
        print("---------------------------------------------")
        print("\nConsole Menü")
        print("1. k’nıncı En Küçük Elemanı Bulma")
        print("2. En Yakın Çifti Bulma")
        print("3. SBir Listenin Tekrar Eden Elemanlarını Bulma")
        print("4. Matris Çarpımı")
        print("5. Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
        print("6. Liste İçinde En Küçük Değeri Bulma")
        print("7. Karekök Fonksiyonu")
        print("8. En Büyük Ortak Bölen")
        print("9. Asallık Testi")
        print("10. Daha Hızlı Fibonacci Hesabı")
        print("0. Çıkış")
        print("---------------------------------------------")

        secim = input("Bir seçenek numarası girin: ")

        if secim == "1":
            sonuc = secenek_1()
            print(f"Sonuç: {sonuc}")
        elif secim == "2":
            sonuc = secenek_2()
            print(f"Sonuç: {sonuc}")
        elif secim == "3":
            sonuc = secenek_3()
            print(f"Sonuç: {sonuc}")
        elif secim == "4":
            sonuc = secenek_4()
            print(f"Sonuç: {sonuc}")
        elif secim == "5":
            sonuc = secenek_5()
            print(f"Sonuç: {sonuc}")
        elif secim == "6":
            sonuc = secenek_6()
            print(f"Sonuç: {sonuc}")
        elif secim == "7":
            sonuc = secenek_7()
            print(f"Sonuç: {sonuc}")
        elif secim == "8":
            sonuc = secenek_8()
            print(f"Sonuç: {sonuc}")
        elif secim == "9":
            sonuc = secenek_9()
            print(f"Sonuç: {sonuc}")
        elif secim == "10":
            sonuc = secenek_10()
            print(f"Sonuç: {sonuc}")
        elif secim == "0":
            print("Çıkış seçeneği seçildi. Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main_menu()
