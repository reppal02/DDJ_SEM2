for num in range(1,21):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzfuzz")
    elif num % 5 == 0:
        print("fuzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)