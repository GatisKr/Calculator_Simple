# Simple Calculator program
# Define function to add two numbers
def add(x, y):
    return x + y

# Define function tu substract two numbers
def substract(x, y):
    return x - y

# Define function to multiply two numbers
def multiply(x, y):
    return x * y
# Define function to divide two numbers
def divide(x, y):
    return x / y

# Print operation menu
print("Please select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Please enter your choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))
        
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        else:
            print("Invalid input")
            continue

        # Ask user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")

        # Check user's answer and restart the loop or exit
        if another_calculation.lower() == "yes":
            continue
        else:
            break