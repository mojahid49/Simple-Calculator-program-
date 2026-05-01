#making a calculator 

num1= float(input("Enter your 1st number: "))
op =input("Enter your operator: ")
num2 = float(input("Enter your 2nd number: "))

if op ==  "+":
	print( num1 +  num2)
elif op==  "-":
	print( num1 -  num2)
elif op==  " * ":
	print( num1  *  num2)
elif op==   "/":
	print( num1 /  num2)
elif op==  "%":
	print(  num1 %  num2)
else:
	print("Invalid operator")
	

