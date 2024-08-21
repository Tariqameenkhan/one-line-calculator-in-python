# advanced and also error in one line calculator
#  also space with work like 4 (space) + (space) 8 = 12



def evaluate_expression():
    # Get input from the user
    user_input = input("Enter a mathematical expression (e.g., 5 + 8): ")

    # Split the input into components
    components = user_input.split()
    
    if len(components) != 3:
        print("Invalid input. Please enter an expression in the format: num1 operator num2")
        return
    
    try:
        num1 = float(components[0])
        opr = components[1]
        num2 = float(components[2])
    except ValueError:
        print("Invalid numbers. Please enter valid numeric values.")
        return

    if opr == "+":
        print(num1 + num2)
    elif opr == "-":
        print(num1 - num2)
    elif opr == "*":
        print(num1 * num2)
    elif opr == "/":
        if num2 == 0:
            print("Error: Division by zero.")
        else:
            print(num1 / num2)
    else:
        print("Error: Unsupported operator. Use +, -, *, or /.")

# Call the function to execute
evaluate_expression()
