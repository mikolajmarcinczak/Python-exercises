def ReadFile(arg):
    return open(arg, 'r')

if __name__ == '__main__':
    print((file := ReadFile('./pliki/file1.txt')).read())
    file.close()