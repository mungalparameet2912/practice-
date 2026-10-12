n = int(input("Enter size of list: "))

my_list = []

for _ in range(n):
    num = int(input())
    my_list.append(num)

print("The list is ",my_list)


index_list = list(range(len(my_list)))
print("The index list is: ",index_list)

indx1 = int(input("Enter indx1 = "))
indx2 = int(input("Enter indx2 = "))

temp = my_list[indx1]
my_list[indx1] = my_list[indx2]
my_list[indx2] = temp

print(my_list)

