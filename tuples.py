# creating a tuple
colours = ("red","blue","yellow")

'''# creating a tuple with 1 item
fruit = ("apple",)
fruit_1= tuple(("apple"))

#check type of tuple
print(type(colours))
print(type(fruit))
print(type(fruit_1))

#check length of tuple
print(len(colours))

#accessing items in tuple
    #positive indxing
print(colours[0])
    #negetive indxing
print(colours[-1])
    #renge indxing
print(colours[1:3])

print(colours[-3:])

#traverse the tuple
for i in colours:
    print(i)

#concatenate 2 tuple
more_colours = ("blue", "brown")
colours = colours + more_colours
print(colours)'''

#unpacking the tuple
colour1, colour2, colour3 = colours
print(colour1, colour2, colour3)