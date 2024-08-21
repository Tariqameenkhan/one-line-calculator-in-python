# calculator in one line code
#  4 + 6 = 10


def evaluate_expression():
 
 
 user_input = input("value :")
 
#  components = user_input.split() then 6  +  8  =  14
 components = user_input

 num1 = float(components[0])
 opr= components[1]
 num2 = float(components[2])
#  opr= components[3]
#  num3 = float(components[4]) 4+6+5=15

 
 if opr=="+":
  print(num1+ num2)    
# print(num1+num2+num3)
 
 elif opr=="-":
  print(num1-num2)
 # print(num1-num2-num3)

 elif opr=="*":
  print(num1*num2)
  #print(num1*num2*num3)

 elif opr=="/":
  if num2 == 0:
   print("error")
  
  # elif num3 == 0:
   #print("error")
  
  else:
   print(num1/num2)
   #print(num1/num2/num3)

 else:
  print("error")

evaluate_expression() 
 
 
 
