import random

number1, number2 = random.randint(1, 100), random.randint(1, 100)

try:
    userSum = int(input("Jaka jest suma podanych liczb?"))
except ValueError:
    print("Wprowadzona wartość nie jest liczbą całkowitą")

if userSum == number1+number2:
    print("Odgadłeś!")
else:
    print("Niestety nie odgadłeś.")