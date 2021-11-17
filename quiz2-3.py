# Author RTS 11/17/21
import random

win = list(input("Enter 3 #s between 1-50: "))
lst_1 = random.randint[0:50]
lst_2 = random.randint[0:50]
lst_3 = random.randint[0:50]

if lst_1 + lst_2 +lst_3 == win:
    print("you win")
elif lst_3 + lst_2 +lst_1 == win:
    print("you win")
elif lst_2 + lst_1 +lst_3 == win:
    print("you win")
elif lst_1 + lst_3 +lst_2 == win:
    print("you win")
elif lst_3 + lst_1 +lst_2 == win:
    print("you win")
elif lst_2 + lst_3 +lst_1 == win:
    print("you win")
else:
    print("you loose!")
    