def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num2 * num1

def divide(num1, num2):
    return num1/num2

while True:
    print("""Please Select Your choice.
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division""")

    user_choice = int(input())
    
    if user_choice == 1:
        print(addition(int(input("Please enter the first number: ")),int(input("Please enter the second number: "))))
    
    elif user_choice == 2: 
        print(subtraction(int(input("Please enter the first number: ")),int(input("Please enter the second number: "))))
    
    elif user_choice == 3: 
        print(multiplication(int(input("Please enter the first number: ")),int(input("Please enter the second number: "))))
    
    elif user_choice == 4: 
        print(divide(int(input("Please enter the first number: ")),int(input("Please enter the second number: "))))
    
    next_move = input("Would you like to play again.Y/N \n")

    if next_move.upper() != "Y":
        break

