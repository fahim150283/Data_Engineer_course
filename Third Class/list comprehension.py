# [expression for expression in list]

my_list = [1,2,3,4,5,6,7]

updated_list = [x**2 for x in my_list]  # square every value

print ("Given list : ", my_list)
print ("This is the updated list of squares using list comprehension : " ,updated_list)
print()
print("*" * 90)
print()




################################


my_list = [1,2,3,4,5,6,7]

updated_list = [x**2 for x in my_list if x%2==0]  # square every even value

print ("Given list : ", my_list)
print ("This is the updated list of even squares using list comprehension : " ,updated_list)
print()
print("*" * 90)
print()


###############################


my_list = [1,2,3,4,5,6,7]

updated_list = [x**2 for x in my_list if x%2==0 and x>3]  # square every even value

print ("Given list : ", my_list)
print ("This is the updated list of even and greater than 3, squares using list comprehension : " ,updated_list)
print()
print("*" * 90)
print()


###############################


my_list = [1,2,3,4,5,6,7]

updated_list = [x**2 for x in my_list if x%2!=0 or x>3]  # square every odd value

print ("Given list : ", my_list)
print ("This is the updated list of odd and greater than 3, squares using list comprehension : " ,updated_list)
print()
print("*" * 90)
print()




###############################


my_list = [1,2,3,4,5,6,7]

updated_list = [x**2 for x in my_list if x%2!=0 or x>3 if x**2>25]  # square every odd value

print ("Given list : ", my_list)
print ("This is the updated list of odd and greater than 3, squares using list comprehension : " ,updated_list)
print()
print("*" * 90)
print()
