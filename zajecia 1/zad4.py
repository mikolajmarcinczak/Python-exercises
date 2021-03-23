import math

a, b = [int(a) for a in input("Wprowadź boki prostokąta: ").split()]
if a <= 0 | b <= 0:
    print("Nie robi się tak")
    quit()
else:
    area = a * b
    length = 2 * a * b
    diag = math.sqrt((a**2)+(b**2))
    print('Pole prostokąta to: {}, Obwód to {}, Przekątna to: {}'.format(area, length, diag))
