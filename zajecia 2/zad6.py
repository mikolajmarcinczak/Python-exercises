source = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
arr = []

floor, ceil = [int(a) for a in input("Wprowadź zakres: ").split()]

for i in range(floor, ceil):
    arr.append(source[i])

print("Wartość najwyższa to: {}".format(max(arr)))
print("Wartość najniższa to: {}".format(min(arr)))