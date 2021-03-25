import random

def Randomize(): #Draw 6 random numbers in <1;49> range
    arr = []

    for i in range (6):
        if (element := random.randint(1, 49)) not in arr: #Assignment expression; prevents multiple assignments of the same value
            arr.append(element)
        else:
            i -= 1
    arr.sort() #For more readability
    return arr

def User_compare(draw): #Let the user input 6 numbers and find them in formerly drawn array
    arr = []
    counter, i = 0, 0

    print("Enter six numbers between 1 and 49.\n")
    while i < 6:
        try:
            if (element := int(input("Your answer #{}: ".format(i+1)))) not in arr: #Prevents the user from entering the same value multiple times
                if element not in range(1, 50):
                    print("Your answer is not in range of <1;49>.")
                    continue
                arr.append(element)
                i += 1
            else:
                print("You entered the same value again!")
                continue
        except ValueError:
            print("Your answer is not an integer. Try again.\n")

    for i in range(6):
        if arr[i] in draw:
            counter += 1
    arr.sort() #For more readability
    return counter, arr

draw = Randomize()
count, user_array = User_compare(draw)
print("\nYou guessed {} numbers correctly!\nThe drawn array: {}\nYour array: {}".format(count, draw, user_array))