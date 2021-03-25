floor, ceil = [int(a) for a in input("Wprowadź zakres liczb: ").split()]
_sum = 0

for i in range(floor, ceil+1):
        _sum += i
print("Suma wprowadzonych liczb to {}".format(_sum))