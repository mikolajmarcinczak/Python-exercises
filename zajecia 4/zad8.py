import matplotlib.pyplot as plt
from zad1 import ReadFile

_dict = {}
for line in ReadFile('./pliki/kursy.csv'):
    key, value = line.split(';')
    _dict[key] = float(value)

plt.plot(_dict.keys(), _dict.values())
plt.show()