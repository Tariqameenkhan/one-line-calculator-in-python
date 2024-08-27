def dmas():
 user_input = input("Enter the expression (e.g., 8/2*6+3-2): ")
	
	    # Convert the input string into components
 num1 = float(user_input[0])
 opr1 = user_input[1]
 num2 = float(user_input[2])
 opr2 = user_input[3]
 num3 = float(user_input[4])
 opr3 = user_input[5]
 num4 = float(user_input[6])
	
	# Apply DMAS: Division -> Multiplication -> Addition -> Subtraction
 if opr1 == "/" and opr2 == "*" and opr3 == "+":
  result = (num1 / num2) * num3 + num4
 elif opr1 == "*" and opr2 == "+" and opr3 == "-":
  result = (num1 * num2) + num3 - num4
 elif opr1 == "+" and opr2 == "-" and opr3 == "*":
  result = (num1 + num2) - (num3 * num4)
 elif opr1 == "-" and opr2 == "*" and opr3 == "/":
  result = (num1 - (num2 * num3)) / num4
 else:
	        # Default case or handle different operator combinations
  result = num1 - num2 + num3 * num4 / num4
	
 print("The result is:", result)
	
	# Call the function
dmas()
