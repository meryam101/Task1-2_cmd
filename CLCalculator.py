# DISPLAY welcome message and instructions
print("Welcome to the simple calculator,")
print(" please type the first number, an operation and a second number in order")
# Repeat
continue_calc = "Yes"

while continue_calc == "Yes":
    # OBTAIN first number from user
    # STORE that first number
    first_number = float(input("First number: "))
    # OBTAIN the operation the user wants to perform
    # STORE that operation (+, -, *, or /)
    operation = input("Operation(+,-,*, or /: ")
    # OBTAIN second number from user
    # STORE the second number
    second_number = float(input("Second number: "))
    # CALCULATE the operation based on the inputs
    output = 0
    if operation == "+":
        output = first_number + second_number
    elif operation == "-":
        output = first_number - second_number
    elif operation == "*":
        output = first_number * second_number
    elif operation == "/":
        output = first_number / second_number
    # DISPLAY result of calculation
    print(output)
    # Ask the user if they want to perform another calculation
    continue_calc = input("Continue calculations?(Yes/No): ")

# DISPLAY goodbye message and END
print("Thank you!")
