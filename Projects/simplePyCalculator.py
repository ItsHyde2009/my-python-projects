import math

def ask_for_input():
    n1 = float(input("Insert the first number: "));
    n2 = float(input("Insert the second number: "));
    return n1, n2;

print("Select the operation you want to perform:\n\t" 
     + "+) Addition\n\t" 
     + "-) Substraction\n\t" 
     + "*) Multiplication\n\t"  
     + "/) Division\n\t"
     + "^) Power\n\t" 
     + "v) Square root\n"
 + 'Type "exit" to stop the execution of the calculator\n\n')

op = input("Please, select your operation: ");

while(op != "exit"):
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
     
    print("\n\nSelect the operation you want to perform:\n\t" 
        + "+) Addition\n\t" 
        + "-) Substraction\n\t" 
        + "*) Multiplication\n\t"  
        + "/) Division\n\t"
        + "^) Power\n\t" 
        + "v) Square root\n"
    + 'Type "exit" to stop the execution of the calculator\n\n')
    
    op = input("Please, select your operation: ");

