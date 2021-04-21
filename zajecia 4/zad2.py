from zad1 import ReadFile

def LongestWord(arg):
    temp = ''
    f_content = ReadFile(arg).read().split(' ')
    for word in f_content:
        if len(word) > len(temp):
            temp = word
    return temp

if __name__ == '__main__':
    print(LongestWord('./pliki/file1.txt'))
    ReadFile('./pliki/file1.txt').close()