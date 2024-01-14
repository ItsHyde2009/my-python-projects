import math
n1 = input("Insert a number: ")
n2 = input("Insert another number (omit for square root): ")
op = input("Please select the operation: ")
if op == "+":
#I know that the next part is non-optimised as heck, but for now I can't figure out how to make it better.
#And yes, I don't know how to convert floats into ints to make the final result an int when there are no decimal numbers.
    print("The result of the operation is: ", float(n1) + float(n2))
elif op == "-":
    print("The result of the operation is: ", float(n1) - float(n2))
elif op == "*":
    print("The result of the operation is: ", float(n1) * float(n2))
elif op == "/":
    print("The result of the operation is: ", float(n1) / float(n2))
elif op == "^":
    print("The result of the operation is: ", float(n1) ^ float(n2))
elif op == "v":
    print("The result of the operation is: ", math.sqrt(float(n1)))
else:
    print("The operator you entered is invalid for this calculator app")