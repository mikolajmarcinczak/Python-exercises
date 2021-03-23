import random

arg = []
for i in range(0, 20):
    arg.append(random.randint(1, 100))
arg.sort()

u_input = int(input("Wprowadz liczbe: "))

for item in arg:
    if item % u_input == 0:
        print("Liczba {} jest podzielna przez {}".format(item, u_input))