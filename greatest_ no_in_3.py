n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
# normal if-else
if n1 > n2 and n1 > n3:
    print(n1, " is the gretest number.")
elif n2 > n1 and n2 > n3:
    print(n2, " is the gretest number.")
else:
    print(n3, " is the gretest number.")

# nested if-else
if n1 > n2:
    if n1 > n3:
        print(n1, " is the gretest number.")
    else:
        print(n3, " is the gretest number.")
else:
    if n2 > n3:
        print(n2, " is the gretest number.")
    else:
        print(n3, " is the gretest number.")