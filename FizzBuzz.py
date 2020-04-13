# for every integer in a set range n
for i in list(range(100)):
    if i % 3 == 0 and i % 5 == 0: # has to be first if statement otherwise FizzBuzz doesn't work
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) # ensures loop continues