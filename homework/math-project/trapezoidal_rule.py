#algorytm obliczania całek wielomianów kwadraturą trapezów /// Trapezoidal rule polynomial integral calculation algorithm
def Polynomial(deg, x, factor, i=0): #Funkcja obliczająca sumę wielomianu /// A function calculating the sum of the polynomial
    if deg == 0:
        return factor[-1]
    return (factor[i]*x**deg) + Polynomial(deg-1, x, factor, i+1)

def ValError():
    print('Wprowadzona wartość nie jest liczbą! /// The entered value is not a number!')

def UserInput(): #Funkcja przyjmująca wartości od użytkownika /// A function to take input from the user
    limits, factor, i = [], [], 0

    while True:
        try:
            deg = int(input('Wprowadź stopień wielomianu /// Enter the polynomial degree: '))
            if deg < 0:
                print('Stopień wielomianu nie może być niższy od 0 /// The polynomial degree can\'t be lower than 0')
                continue
            break
        except ValueError:
            ValError()
            continue

    while i < 2:
        try:
            element = int(input(f'Wprowadź granice całki ({"dolną" if i == 0 else "górną"}) /// Enter the limits of the integral ({"lower" if i == 0 else "higher"}): '))
            if (i == 1) and (element <= limits[0]): #Dla poprawności matematycznej /// For mathematical correctness
                print('Dolna wartość musi być niższa od górnej. /// The lower limit of an integral must be lower than the upper limit.')
                continue
            limits.append(element)
            i += 1
        except ValueError:
            ValError()
            continue

    i = 0
    while i <= deg:
        try:
            factor.append(float(input(f'Wprowadź współczynnik stopnia {deg - i} /// Enter the factor of degree {deg - i}: ')))
            i += 1
        except ValueError:
            ValError()
            continue

    return deg, limits, factor

def Trapezoidal(deg, limits, factor): #Funkcja obliczająca całkę wielomianu /// A function calculating the inegral of a polynomial
    a = limits[0]
    b = limits[-1]
    return ((b - a) / 2) * (Polynomial(deg, a, factor) + Polynomial(deg, b, factor))

deg, limits, factor = UserInput()
print(f'\nWartość całki wynosi /// The value of the integral is: {Trapezoidal(deg, limits, factor)}')