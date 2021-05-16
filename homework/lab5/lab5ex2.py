import math

def uInput():
    while True:
        try:
            num1, num2 = input("Wprowadź liczby: ").split()
        except ValueError:
            print('Wartości nieprawidłowe.')
            continue
        break
    return num1, num2

def Split(num):
    res = []
    isMinus = False
    for digit in num:
        try:
            res.append(int(digit))
        except ValueError:
            if (digit == '-'):
                isMinus = True
                continue
    return res, isMinus

def Convert(arr):
    res = [str(a) for a in arr]
    res = float("".join(res))
    return res

def LongDivision(num1, num2):
    num1, flag1 = Split(num1)
    tem = int(num2)
    r, i = 0, 0
    res = []
    for digit in num1:
        digit = int(digit) + r
        num2 = abs(int(num2))
        res.append(abs(int(digit/num2)))
        r = (digit % num2) * 10
        i += 1
    res.append('.')
    for j in range(5):
        res.append(abs(int(r/num2)))
        r = (r % num2) * 10
    result = Convert(res)
    r = r/10
    if flag1 or (tem < 0):
        result = result*(-1)
    return result, r


if __name__ == '__main__':
    num1, num2 = uInput()
    res, r = LongDivision(num1, num2)
    print(f'{res} r {r}')