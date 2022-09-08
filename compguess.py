upper = int(input("Enter the number range from 1 to x: "))
lower = 1

while True:

    guess = (lower + upper) // 2

    answer = input(f"Is {guess} your number? Y / N")

    if answer == 'y':
        print("I have guessed your number")
        break
    else:
       get_hi_lo = input("Is your number higher or lower? h / l: ")

       if get_hi_lo == "h":
            lower = guess + 1
       else:
            upper = guess - 1

