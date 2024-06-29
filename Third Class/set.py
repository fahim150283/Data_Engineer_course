my_set = {1,2,3,4,5,6,7,3,5}
print ("print a set : ", my_set)
print()
print("*" * 90)
print()


###############################



my_set1 = {1,2,3,4,5,6,7,3,31,23,34,5,5}
my_set2 = {1,2,3,4,5,6,7,3,5}

print ("print a set1 : ", my_set1)
print ("print a set2 : ", my_set1)
print ("union: ",my_set1.union(my_set2))
print ("intersection: ",my_set1.intersection(my_set2))
print ("difference : ",my_set1.difference(my_set2))
print ("subset : ",my_set1.issubset(my_set2))
print ("superset : ",my_set1.issuperset(my_set2))

print()
print("*" * 90)
print()

###############################



list1 = [1,2,3,4,5,6,7,3,31,23,34,5,5]
my_set = set(list1)
u_list = list(my_set)

print ("print unique numbers only using set : ", u_list)

print()
print("*" * 90)
print()