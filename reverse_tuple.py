input_tuple = (1,2,3,4,5,6)
print("The orignal tuple is:",input_tuple)

list = []

#add reverse values in a list
for x in reversed(input_tuple):
    list.append(x)

output_tuple = tuple(list)
print("The reversed tuple is:",output_tuple)