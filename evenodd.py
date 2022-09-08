
def getevenodd(user_input): 

    if user_input % 2 == 0:
        print("even")
    else:
        print("odd")

    if user_input % 2 == 0:
        print("yes it's divisible")
    else: 
        print("Remainder: ", user_input % 2)
    if user_input % 3 == 0:
        print("yes it's divisible")
    else: 
        print("Remainder: ", user_input % 3)
    if user_input % 4 == 0:
        print("yes it's divisible")
    else: 
        print("Remainder: ", user_input % 4)
    if user_input % 5 == 0:
        print("yes it's divisible")
    else: 
        print("Remainder: ", user_input % 5)

    return "Goodbye"

result = getevenodd(5)
getevenodd(77)

print(result)