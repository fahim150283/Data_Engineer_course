list1 = [1,2,3,4,5,6,7,8,9] 
list1_1 = list()
print(list1)
print(list1_1)

print("*" * 40)

list2 = ["hello", "world","youtube"]
list3 = [1,2,3,"heelo"]

# print lenth of list1
print(len(list1))

print("*" * 40)

list1.append(10)
print(list1)
print("*" * 40)

# merge lists type 1
resultList1 = list2 + list3
print(resultList1)

print("*" * 40)

# merge lists type 2
list3.extend(list2)
print(list3)