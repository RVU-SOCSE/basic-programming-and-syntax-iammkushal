#prog to find simple calcultor
#USN :1RUA25BCA0053
#Name : Kushal R


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

match op:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid operation")
