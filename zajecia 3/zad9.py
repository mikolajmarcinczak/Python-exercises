def Pow(a, b):
    if b == 0:
        return 1
    return a * Pow(a, b - 1)