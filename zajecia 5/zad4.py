curr = [4.57, 5.26, 3.79, 4.13, (3.51/100)]

def Convert(amount, currency):
    return amount/currency

if __name__ == '__main__':
    amount = int(input('Podaj liczbę złotówek: '))
    choice = int(input('Wybierz walutę(0 - EUR, 1 - GBP, 2 - USD, 3 - CHF, 4 -JPY): '))
    print(f'{amount} zł to {Convert(amount, curr[choice])} wybranej waluty.')