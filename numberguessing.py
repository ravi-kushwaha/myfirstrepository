n =30

i=0

while i <= 8:
    userinput = int(input("Please guese the number."))
    if userinput == n:
        print("Congratulation! You guess the right number.")
        break

    elif userinput > n:
        print("Sorry! You choose the high number.")
        i += 1
    elif userinput < n:
        print("Sorry! You choose the low number.")
        i += 1
    if i >= 9:
        print("You are out of move.")
