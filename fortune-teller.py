import random

question = input("What is your question? ")

number = random.randint (1,10)

if number == 1:
    print("Something unexpected will soon enter your life.")
elif number == 2:
    print("The path ahead is unclear, but you will find your way.")
elif number == 3:
    print("A small decision will lead to a big outcome.")
elif number == 4:
    print("You will learn something important in the near future.")
elif number == 5:
    print("Change is coming—be ready to adapt.")
elif number == 6:
    print("Your future holds a moment of clarity.")
elif number == 7:
    print("A quiet moment will reveal a hidden truth.")
elif number == 8:
    print("You will soon face a choice that shapes your path.")
elif number == 9:
    print("The energy you give is about to come back to you.")
elif number == 10:
    print("New beginnings are closer than you think.")
else:
    print(number)