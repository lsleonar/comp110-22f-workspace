n = input("Enter number")
number: int = n / 2
if number == 2:
    if number in range(2,5):
        print("Not Weird")
    else:
        print("Weird")