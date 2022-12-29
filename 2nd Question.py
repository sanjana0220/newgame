choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    for i in range(5):
        print(" " * i + "* " * (5 - i))
elif choice == 2:
    for i in range(5):
        print(" " * i + "* " * (5 - i))
    for i in range(4):
        print(" " * (4 - i) + "- " * (i + 2))
else:
    print("Invalid Input")
