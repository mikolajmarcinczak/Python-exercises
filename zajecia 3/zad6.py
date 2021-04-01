from zad5 import isPrime

def PrimeNumbers(a, b):
    for n in range(a, b+1):
        if isPrime(n):
            print(f'Liczba {n} jest pierwsza.')

a, b = [int(x) for x in(input('Wprowadź granice przedziału: ')).split()]
PrimeNumbers(a, b)