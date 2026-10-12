ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]
print(ar1,ar2,ar3)
#type casting
s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

s1.intersection_update(s2,s3)

ar1 = list(s1)
print(ar1)

