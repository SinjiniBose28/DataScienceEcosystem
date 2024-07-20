#TASK2 - Week 2- Simple CAlCULATOR- Sinjini

# Functions for:

#Adding two numbers
def add(a, b):
    return a + b

#Subtracting two numbers
def subtract(a, b):
    return a - b

#Multiplying two numbers
def multiply(a, b):
    return a * b

#Dividing two numbers
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    else:
        return a / b

#Main function for operating the calculator
def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            
            break  # Exit the loop after valid input and calculation
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4)")

#to Run the calculator function 
calculator()
