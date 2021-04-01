def Position(x, y):
    if x > 0:
        if y > 0:
            return 'I'
        elif y < 0:
            return 'IV'
        else:
            return Axis() 
    elif x < 0:
        if y > 0:
            return 'II'
        elif y < 0:
            return 'III'
        else:
            return Axis()
    else:
        return Axis()

def Axis():
    return 'żadnej'

x, y = [int(x) for x in(input('Wprowadź współrzędne x i y: ')).split()]
print(f'Punkt x:{x}, y:{y} leży na {Position(x, y)} ćwiartce układu współrzędnych.')