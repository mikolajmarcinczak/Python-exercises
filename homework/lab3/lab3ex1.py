def Draw(width, height, char='*'):
    Bar(width, char)
    print()
    for i in range(height - 2):
        for j in range(width):
            if j == 0:
                print(char, end=" ")
            elif j == width - 1:
                print(char)
                break
            else:
                print(' ', end=" ")
    Bar(width, char)

def Bar(width, char):
    for i in range(width):
        print(char, end=" ")

Draw(12, 8, '%')