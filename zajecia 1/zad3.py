import math

radius = float(input("Wprowadz promień koła: "))
if radius <= 0:
    print("Promień mniejszy od zera.")
    quit()
else:
    area = math.pi * radius ** 2
    circ = 2 * math.pi * radius
    template = 'Pole koła to: {:0.2f}, Obwód to {:1.2f}'.format(area, circ)
    print(template)