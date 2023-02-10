def guessthenumber():
    print("Hello! What is your name?")
    name = input()
    print("Well, ", name, ", I am thinking of a number between 1 and 20.", sep = "")
    print("Take a guess.")
    cnt = 0
    r = random.randint(1, 20)
    while 1:
        n = int(input())
        if n > r: 
            print("Your guess is too large")
            cnt += 1
            print("Take a guess.")
        elif n < r:
            print("Your guess is too low")
            cnt += 1
            print("Take a guess.")
        else:
            cnt += 1
            print("Good job, ", name, "! You guessed my number in ", cnt, " guesses!", sep = "")
            break