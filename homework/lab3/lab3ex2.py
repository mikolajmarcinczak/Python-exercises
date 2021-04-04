def Sequence(start, n, diff):
    if n == 1:
        return start
    elif n > 1:
        return Sequence(start, n-1, diff) + diff
    else:
        return 'Ciąg nie może mieć wyrazu niedodatniego!'

def UserInput():
    while True:
        try:
            start = float(input('Podaj wyraz początkowy ciągu: '))
            diff = float(input('Podaj różnicę ciągu: '))
            n = int(input('Który wyraz ciągu chcesz odnaleźć? '))
            break
        except ValueError:
            print('Podana wartość nie jest liczbą! Podaj wartości jeszcze raz!')
            continue
    return start, n, diff

start, n, diff = UserInput()
print(f'{n}-ty wyraz ciągu to: {Sequence(start, n, diff)}')