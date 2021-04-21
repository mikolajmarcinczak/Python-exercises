import random
import numpy as np
import matplotlib.pyplot as plt

numbers = []
for i in range(10001):
    numbers.append(random.randint(1,10))

distinct = np.array([int(x) for x in range(1, 11)])

values = []
for element in distinct:
    values.append(numbers.count(element))

plt.figure(figsize=(10, 5))
plt.bar(distinct, values, color='green')

for index, data in enumerate(values):
    plt.text(index + 0.8, data/values[index] + 10, s=f'{data}')

plt.show()