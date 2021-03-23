import math

source = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
num = int(input("Wprowadź ilość list: "))
limiter = math.ceil(len(source)/num)
arr = []
it = 0

while it < len(source):
    for i in range(num):
        temp = []
        for i in range(limiter):
            temp.append(source[it])
            it += 1
        arr.append(temp)
print(arr)