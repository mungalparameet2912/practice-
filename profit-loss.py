# cp => cost price
cp = int(input("Enter the CP:"))
# sp => selling price
sp = int(input("Enter the SP"))

if sp > cp:
    profit = sp - cp
    print("saler is in profit.")
    print("Profit is: ",profit)
elif sp < cp:
    loss = cp - sp
    print("Saler is in the loss.")
    print("Loss is: ",loss)
else:
    print("We have need no profit no loss.")