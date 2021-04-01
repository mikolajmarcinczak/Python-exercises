import random as rd

def Draw(a, b, n):
    for i in range(n):
        print(rd.randint(a, b))

Draw(1, 50, 8)