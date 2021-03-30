#Program służący do mnożenia macierzy /// A program to multiply two matrices
import numpy as np

def Matrix(flag = 0): #Funkcja na wprowadzanie ilości wierszy i kolumn /// A function to input the no. of rows and columns
    while True:
        try:
            row = int(input(f'Wprowadź ilość wierszy {"pierwszej" if flag == 0 else "drugiej"} macierzy /// Enter the no. of rows for the {"first" if flag == 0 else "second"} matrix: ')) 
            col = int(input(f'Wprowadź ilość kolumn {"pierwszej" if flag == 0 else "drugiej"} macierzy /// Enter the no. of columns for the {"first" if flag == 0 else "second"} matrix: '))
            if row < 1 or col < 1:
                print('\nIlość kolumn lub wierszy nie może być niedodatnia. /// The no. of columns or rows can\'t be non-positive.')
                continue
            break
        except ValueError:
            print('Podana wartość nie jest liczbą! /// The entered value is not a number!')
            continue
    return row, col

def Fill_matrix(matrix, row, col): #Funkcja na wypełnienie macierzy wartościami /// A function to fill the matrix with values
    i = 0
    while i < row:
        j = 0
        while j < col:
            try:
                matrix[i][j] = int(input(f'Wprowadź wartość komórki[{i}][{j}] /// Enter the value of cell [{i}][{j}]: '))
                j += 1
            except ValueError:
                print('Podana wartość nie jest liczbą! /// The entered value is not a number!')
                continue
        i += 1
    return matrix


def UserInput(): #Funkcja na utworzenie macierzy do obliczeń /// A function to create the matrices
    f_row, f_col = Matrix()
    s_row, s_col = Matrix(1)
    while f_col != s_row:
        print('\nIlość kolumn pierwszej macierzy musi odpowiadać ilości wierszy drugiej macierzy. /// The no. of columns of the first matrix must be equal to the no. of rows of the second matrix.')
        f_row, f_col = Matrix()
        s_row, s_col = Matrix(1)
    
    first_matrix = np.empty([f_row, f_col])
    second_matrix = np.empty([s_row, s_col])
    print('\nPierwsza macierz /// First matrix')
    first_matrix = Fill_matrix(first_matrix, f_row, f_col)
    print('\nDruga macierz /// Second matrix')
    second_matrix = Fill_matrix(second_matrix, s_row, s_col)

    return first_matrix, second_matrix

def Multiply(first_matrix, second_matrix): #Funkcja na mnożenie macierzy /// A function to multiply the matrices
    result = np.zeros([len(first_matrix), len(second_matrix[0])])
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            for k in range(len(second_matrix)):
                result[i][j] += first_matrix[i][k] * second_matrix[k][j]
    return result

first_matrix, second_matrix = UserInput()
print(f'Pomnożona macierz to /// The multiplied matrix is: {Multiply(first_matrix, second_matrix)}')