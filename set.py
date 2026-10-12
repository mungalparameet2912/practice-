#creating a set
names = {"sia", "hia", "tia"}

#print set
'print(names)'

#check length of set
'print(len(names))'

#chack data type of set
'print(type(names))'

#accessing item of set
'''for x in names:
    print(x)'''

#check if an item exists in a set
'''if "sia" in names:
    print("sia is the in the names.")'''

#add element in set
'''names.add("sia")
print(names)'''

#add another sequence in a set
'''names_list = ["riya", "kiya"]
names.update(names_list)
print(names)'''

#removing element from a set
'''names.discard("ria")#this function will not throw an error if value is not present in set
print(names)'''

#joining a 2 set
s1 = {'a','b','c'}
s2 = {'d','e','a'}
s3 = {'w','t','a'}
print(s1, s2,s3)

s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)

#keep only duplicates while joining
'''s1.intersection_update(s2,s3)
print(s1)'''

#keep all values expect duplicates
'''s1.symmetric_difference_update(s2)
print(s1)'''