# name = input("Enter your name: ")

# pay = int(input("Enter your pay: "))

# hours = int(input("Enter your hours: "))

# total = pay * hours 

# print("Hello ", name, " you made $", total)

# taxes = total * .8

# print(f"Helo {name} you made ${taxes} after taxes") 


e = "Enter your "
p = "Please enter a valid "
y = "You're "
while (gender := input(f"{e}gender: ").lower().strip()) not in {'male', 'female'}:
    print(f"{p}gender")
while not (age := input(f"{e}age: ").strip()).isdecimal():
    print(f"{p}age")
if (age := int(age)) < 18:
    print(f"{y}still in school")
elif age <= 25:
    print(f"{y}going to college")
    print((f"{y}going to Law School", f"{y}going into STEM")[gender == 'male'])
else:
    print("Work is hard")
    print((f"{y}a lawyer", "Programming is fun")[gender == 'male'])