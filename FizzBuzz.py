for i in range (100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 4 == 0:
        print("BUzz")
    else:
        print(i)