num1 = float(input("First number: "))
num2 = float(input("Second number: "))

op = input("Choose +, -, *, or /: ")

if op == "+":
 print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
   print("Result:", num1 * num2)
elif op == "/":
    if num2 == 0:
       print("Error: You cannot divide by zero.")
    else:
       print("Result:", num1 / num2)
else:
    print("Error: Invalid operator.")