#Program służący do mnożenia macierzy /// A program to multiply two matrices
import numpy as np

def Matrix1():
    while True:
        try:
            first_row = int(input('Wprowadź ilość wierszy pierwszej macierzy /// Enter the no. of rows for the first matrix: ')) 
            first_col = int(input('Wprowadź ilość kolumn pierwszej macierzy /// Enter the no. of columns for the first matrix: '))
            if first_row < 1 or first_col < 1:
                print('\nIlość kolumn lub wierszy nie może być niedodatnia. /// The no. of columns or rows can\'t be non-positive.')
                continue
            break
        except ValueError:
            print('Podana wartość nie jest liczbą! /// The entered value is not a number!')
            continue
    return first_row, first_col

def Matrix2():
    while True:
        try:
            second_row = int(input('Wprowadź ilość wierszy drugiej macierzy /// Enter the no. of rows for the second matrix: '))
            second_col = int(input('Wprowadź ilość kolumn drugiej macierzy /// Enter the no. of columns for the second matrix: '))
            if second_row < 1 or second_col < 1:
                print('\nIlość kolumn lub wierszy nie może być niedodatnia. /// The no. of columns or rows can\'t be non-positive.')
                continue
            break
        except ValueError:
            print('Podana wartość nie jest liczbą! /// The entered value is not a number!')
            continue
    return second_row, second_col

def Fill_matrix(matrix, row, col):
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


def UserInput():
    f_row, f_col = Matrix1()
    s_row, s_col = Matrix2()
    while f_col != s_row:
        print('\nIlość kolumn pierwszej macierzy musi odpowiadać ilości wierszy drugiej macierzy. /// The no. of columns of the first matrix must be equal to the no. of rows of the second matrix.')
        f_row, f_col = Matrix1()
        s_row, s_col = Matrix2()
    
    first_matrix = np.empty([f_row, f_col])
    second_matrix = np.empty([s_row, s_col])
    first_matrix = Fill_matrix(first_matrix, f_row, f_col)
    second_matrix = Fill_matrix(second_matrix, s_row, s_col)

    return first_matrix, second_matrix

def Multiply(first_matrix, second_matrix):
    result = np.zeros([len(first_matrix), len(second_matrix[0])])
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            for k in range(len(second_matrix)):
                result[i][j] += first_matrix[i][k] * second_matrix[k][j]
    return result

first_matrix, second_matrix = UserInput()
print(f'Pomnożona macierz to /// The multiplied matrix is: {Multiply(first_matrix, second_matrix)}')