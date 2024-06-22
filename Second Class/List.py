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

# append
list1.append(10)
print(list1)

list2.append("germany")
print("*" * 40)

# merge lists type 1 (nested list)
resultList1 = list2 + list3
print(resultList1)

print("*" * 40)

# merge lists type 2 (normal single list)
list3.extend(list2)
print(list3)
print("*" *40)

# join
resulted = " ".join(list2)
print(resulted)
resulted = " 'yo neega' ".join(list2)
print(resulted)
print("*" *40)

# split
Splittedresult = resulted.split(" ")
print(Splittedresult)

Splittedresult = resulted.split("neega")
print(Splittedresult)
print("*" *40)


# [x:y]
list1[:]
list1[:5]
list1[5:]

print(list1)
print(list1[4])
print(list1[-1])
print("*" *40)