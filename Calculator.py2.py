first = float(input("enter first number:"))
operator = input("enter operator:(+,-,*,/,%):")
second = float(input("enter second number:"))

if operator == '+':
    print("result:",first+second)
elif operator == '-':
    print("result:",first-second)
elif operator == "*":
    print("result:",first*second)
elif operator == "/":
    print("result:",first/second)
elif operator == "%":
    print("result;",first%second)
else:
    print("not valid number")