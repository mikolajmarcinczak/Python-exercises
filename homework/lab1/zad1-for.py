ceil = int(input("Wprowadź zakres liczb: "))
_sum = 0

for i in range(ceil):
    try:
        _sum += int(input("Arg {}: ".format(i+1)))
    except ValueError:
        print("Wprowadzona wartość nie jest liczbą całkowitą")
        break
print("Suma wprowadzonych liczb to {}".format(_sum))