def Factorial(n):
    if n == 0:
        return 1
    return n * Factorial(n - 1)

print(f'Silnia liczby {(n := int(input("Wprowadź liczbę: ")))} to {Factorial(n)}')