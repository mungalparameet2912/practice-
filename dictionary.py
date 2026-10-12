'''phones = {
    "Jone" : 878749344,
    "riya" : 868975925,
    "joy" : 879798989
}
'''
#printing the dict
'print(phones)'

#cheacking type of dict
'print(type(phones))'

#chack the length of dict
'print(len(phones))'

#access items of dict
'''print(phones["Jone"])
print(phones.get("jone"))
print(phones.keys())'''

#update value in dict
'''phones['Jone'] = 77979893
print(phones)'''

#add elements in dict
'''phones["joy"] = 79875972
print(phones["joy"])'''

#Add another dict
'''more_phones = {
    "kia" : 769875676
}
phones.update(more_phones)
print(phones)'''

# how to remove a element in a dict
'''phones.pop("Jone")
print(phones)'''
#popitem will remove the last added item
'''phones.popitem()
print(phones)'''

#this will empty the dict
'''phones.clear()
print(phones)'''

#printing values of a dict
'''for x,y in phones.items():
    print(x,y)'''

#nested dict
phones = {
    "area1" : {
        "x" : 1,
        "y" : 2,
        "z" : 3
    },
       "area2" : {
        "a" : 4,
        "b" : 5,
        "c" : 6
    }
}

print(phones["area1"]["y"])
print(phones["area1"]["z"])
print(phones["area2"]["a"])