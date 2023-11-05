def karekok(n, x0, tol=1e-10, maxiter=10):
    x = x0
    for i in range(maxiter):
        x_next = 0.5 * (x + n / x)
        hata = abs(x_next ** 2 - n)
        if hata < tol:
            return x_next
        x = x_next

    print(f"{maxiter} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin")
    return x


sonuc1 = karekok(10, 1)
print(sonuc1)  # Sonuc: 3.162277660168379

sonuc2 = karekok(10000, 0.1)
print(sonuc2)  # Sonuc: 103.38412392442035

sonuc3 = karekok(10000, 0.1, maxiter=15)
print(sonuc3)  # Sonuc: 100.0
