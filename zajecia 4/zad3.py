from zad1 import ReadFile
import random

def WriteToFile(arg, string):
    print('Writing to file...')    
    print(f'Operation ended with success!' if((open(arg, 'w')).write(string)) else 'Operation failed.')

def Generate(floor = 1, lim = 100, count = 10):
    arr = ''
    for i in range(10):
        element = random.randint(floor, lim)
        arr += f"{element} "
    return arr
    
if __name__ == '__main__':
    WriteToFile('./pliki/ownfile.txt', Generate())
    print((file := ReadFile('./pliki/ownfile.txt')).read())
    file.close()