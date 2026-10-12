fruits = ["apple", "mango", "cherry", "banana","apple"]# create a list
print(fruits)# how to print list

#check type of list
'print(type(fruits))'
# check length of list
'print(len(fruits))'

# checking if an item is present in my list
'''if "banana" in fruits:
    print("Banana is part of the list")'''

# checking if an item is not present in my list
'''if "kiwi" not in fruits:
    print("Kiwi is not part of the list.")'''

# indexing in list
'''print(fruits[1]) #mango
print(fruits[-3]) #mango
print(fruits[1:3]) #[mango,cherry]
print(fruits[-3:-1]) #[mango,cherry]'''

#adding element to a list
fruits.append("apple")
print(fruits)

fruits.insert(2,"kiwi")
print(fruits)

list2 = ["kiwi","papaya"]
fruits.extend(list2)
print(fruits)
# removing element from the list
'''fruits.remove("banana")
print(fruits)'''

'''fruits.pop()
print(fruits)'''

#changing/updating item in a list
'''fruits[1] = "kiwi"
print(fruits)'''

'''fruits[1:3] = ["papaya"]
print(fruits)'''

# sorting a list 
'''fruits.sort() #by defualt ascending
fruits.sort(reverse=False) # descending
print(fruits)'''

# list comprehension
new_fruits = [ i for i in fruits if "a" in i]
print(new_fruits)

# copy a list
'''new_fruits = fruits.copy()
print(new_fruits)

new_fruits = fruits + new_fruits
print(new_fruits)'''

# nested list
'''fruits.insert(2,["kiwi","papaya"])
print(fruits)
print(fruits[2][1])'''

