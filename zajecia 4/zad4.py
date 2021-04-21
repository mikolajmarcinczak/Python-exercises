from zad1 import ReadFile
from zad3 import WriteToFile

def JoinStrings(str1, str2):
    result = ''
    str1, str2 = str1.split(), str2.split()
    if len(str1) > len(str2):
        for i in range (len(str1)):
            result += str1[i] + str2[i] + '\n'
    else:
        for i in range (len(str2)):
            result += str1[i] + str2[i] + '\n'
    return result

if __name__ == '__main__':
    file2, file3 = ReadFile('./pliki/file2.txt'), ReadFile('./pliki/file3.txt')
    WriteToFile('./pliki/zad4_out.txt', JoinStrings(file2.read(), file3.read()))
    file2.close()
    file3.close()