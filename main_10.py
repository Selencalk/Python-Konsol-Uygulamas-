def hizlandirilmis_fibonacci(n, k, current, previous):
    if k == n:
        return current

    return hizlandirilmis_fibonacci(n, k + 1, current + previous, current)


def hesapla_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return hizlandirilmis_fibonacci(n, 1, 1, 0)


n = 10
sonuc = hesapla_fibonacci(n)
print(f"Fibonacci({n}) = {sonuc}")
