import random

number = random.randint(1, 100)

print("Wylosowana liczba to: ", number)

if number % 2 == 0:
    print("Liczba {} jest parzysta".format(number))
if number % 3 == 0:
    print("Liczba {} jest podzielna przez 3".format(number))
