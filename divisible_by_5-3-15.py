n1 = int(input("Enter a possitive number:"))

if n1 % 15 == 0:
    print("Number is divisible by 15")
else:
    if n1 % 3 == 0 or n1 % 5 == 0:
        print("Number is not divisible by 15 but divisible by 3 or 5.")
    else:
        print("Number is not divisible by 15,5 or 3.")