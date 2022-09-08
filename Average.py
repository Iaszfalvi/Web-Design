
user_numbers = []
counter = 0
total = 0

while True:

    user_input = input("Please enter a number or done to quit: ")

    if user_input == "quit":
        break    
    else: 
        user_numbers.append(int(user_input))
        counter = counter + 1
        total = total + int(user_input)


print("list is: ", user_numbers, "avarege is: ", total/counter)