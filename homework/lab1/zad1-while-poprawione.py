floor, ceil = [int(a) for a in input("Wprowadź zakres liczb: ").split()]
_sum = 0

while ceil >= floor :
    _sum += ceil
    ceil -= 1
print("Suma wprowadzonych liczb to {}".format(_sum))