def isPrime(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

#print(f'Liczba {"nie " if not isPrime(int(input("Wprowadź liczbę: "))) else ""}jest pierwsza')