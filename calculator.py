num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

list = ["+","-","*","/"]
print("Choose: 1(+), 2(-), 3(*), 4(/)")
chosse_operator = int(input("Choose a operator no. :"))
op = list[chosse_operator - 1]
print("Choosen operator is ",op)

match op:
    case "+":
        print("Sum of given 2 numbers is", num1 + num2)
    case "-":
        print("Difference of given 2 numbers is", num1 - num2)
    case "*":
        print("Product of given 2 numbers is ", num1 * num2)
    case "/":
        print("Division of given 2 numbers is ", num1 / num2)
    case _:
        print("Please enter a valid operator. ")

