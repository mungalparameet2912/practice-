'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# arithmetic opretion

print("sum",num1 + num2)
print("difference",num1 - num2)
print("product",num1 * num2)
print("division",num1 / num2)
print("floor division",num1 // num2)
print("exponentiation",num1 ** num2)

# assignment opretion
n1 = 4
n2 = n1
print(n1,n2)
n2 *= n1
print(n1,n2)

# comparison opretion
n1 = 4
n2 = 3
print(n1>n2)
'''
# logical opretion
exp1 = 4 > 3
exp2 = 3 >= 2
print("exp1 and exp2:",exp1 and exp2)
print("exp1 or exp2:",exp1 or exp2)
print("not exp1: ",not(exp1))

#identity opretion
x = 5
y = 5
print("if x is y: ", x is y)
print("if x is not y: ", x is not y)

#membership opretion
fruits = ["apple", "banana", "cherry"]
print('if banana is present in fruits: ',"banana" in fruits)
print('if mango is present in fruits: ',"mango" not in fruits)
