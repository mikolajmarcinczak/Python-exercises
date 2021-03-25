ceil = c = int(input("Wprowadź zakres liczb: "))
_sum = 0

while c > 0:
    try:
        _sum += int(input("Arg {}: ".format(abs(ceil-(c-1)))))
    except ValueError:
        print("Wprowadzona wartość nie jest liczbą całkowitą")
        break
    c -= 1
print("Suma wprowadzonych liczb to {}".format(_sum))