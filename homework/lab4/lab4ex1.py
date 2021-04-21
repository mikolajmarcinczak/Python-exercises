import numpy as np
file = open('projektowe.txt', 'r')
text = file.read()

def LetterCount(text):
    counter = []
    alpha = np.array([chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]) 
    for letter in alpha:
        counter.append(text.count(letter))
    return alpha, counter

if __name__ == '__main__':
    a, c = LetterCount(text)
    for k, v in zip(a, c):
        print(f'[{k}] : [{v}]')
    print(f'Liczba znaków w pliku // The no. of characters in the file: {len(text)}\nLiczba znaków w pliku(wyłączając spacje) // The no. of characters in the file(excl. spaces): {len(text.replace(" ",""))}')