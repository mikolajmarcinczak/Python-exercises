import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Compare_num(number):
    counter = 0
    while True:
        counter += 1
        try:
            answer = int(input("Answer with a number from 1 to 100: "))
            cls()
        except ValueError:
            print("Your answer is not an integer. Try again.\n")
            continue
        if answer == number:
            print("You guessed the number correctly on your {} try! The answer was {}.".format(counter, number))
            break
        elif answer not in range(1, 101):
            print("You entered a value outside of the specified range. Try again.\n")
            continue
        else:
            if answer < number:
                print("Your number is lower than mine. Try again.\n")
                continue
            else:
                print("Your number is greater than mine. Try again.\n")
                continue

Compare_num(random.randint(1, 100))