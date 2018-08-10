#Python Standard Library (Imports and Research) https://docs.python.org/3/library/#
import random
import sys
def mentalmath():
    problems = 0
    correct = 0
    run = 0
    points = 0
    print("HELLO AND WELCOME TO MY MENTAL MATH PRACTICE PROGRAM.")
    dig = input("PLEASE INPUT THE MAX DIGIT COUNT A NUMBER CAN HAVE (UP TO 4): ")
    if not dig.isnumeric():
        sys.exit("WE ACCEPT ONLY WHOLE NUMBER ANSWERS. PLEASE TRY AGAIN")
    elif int(dig) > 4:
        sys.exit("WE DO NOT ACCEPT NUMBERS HIGHER THAN 4. PLEASE TRY AGAIN.")
    elif int(dig) <= 0:
        sys.exit("WE DO NOT ACCEPT 0 OR NEGATIVE NUMBERS. PLEASE TRY AGAIN.")
    while run == 0:
        a = numdig(int(dig))
        b = numdig(int(dig))
        c = a*b
        ans = input("%i x %i = " % (a,b))
        if not ans.isnumeric():
            if ans == "end" or ans == "quit":
                print("Thank you for playing. You answered %i problem(s) and got %i of them correct." % (problems,correct))
                print("Goodbye.")
                run += 1
            else:
                print("Invalid input. The correct answer was %i." % (c))
        elif int(ans) == c:
            print("Correct!")
            problems += 1
            correct += 1
        else:
            print("Incorrect. The answer was %i." %(c))
            problems += 1

def numdig(k):
    numblank = 0
    m = 0
    j = random.randint(1, k)
    while m < j:
        x = random.randint(0, 9)
        numblank += x * 10**m
        m += 1
    return(numblank)

mentalmath()
