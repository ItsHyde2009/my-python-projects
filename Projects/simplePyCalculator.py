import math

def ask_for_input():
    n1 = float(input("Insert the first number: "));
    n2 = float(input("Insert the second number: "));
    return n1, n2;

op = input("Please, select your operation: ");

match op:
    case "+":
        numbers = ask_for_input();
        print("The result of the operation is: ", numbers[0] + numbers[1]);
    case "-":
        numbers = ask_for_input();
        print("The result of the operation is: ", numbers[0] - numbers[1]);
    case "*":
        numbers = ask_for_input();
        print("The result of the operation is: ", numbers[0] * numbers[1]);
    case "/":
        numbers = ask_for_input();
        print("The result of the operation is: ", numbers[0] / numbers[1]);
    case "^":
        numbers = ask_for_input();
        print("The result of the operation is: ", numbers[0] ** numbers[1]);
    case "v":
        print("The result of the operation is: ", math.sqrt(float(input("Insert the number: "))));
    case _:
        print("The operator you entered is invalid for this calculator app!");

