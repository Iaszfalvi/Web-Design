grade = int(input("Please enter a grade: "))

if grade in range(94, 101):
    print("A")
if grade in range(90, 94):
    print("A-")

if 80 <= grade <= 89:
    print("B")