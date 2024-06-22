#  string manipulation


a = "hello"
b = "world"
c = a +" "+ b +" "   # merge strings (concatination)

print("Here a : " + a)
print("*"*40)
print("Here b : " + b)
print("*"*40)
print("Here c : "+c)       # here * is used to print multiple times (String repeatation)
print("*"*40)

# print c to upper case
print("Here C is printed in upper case : " + c.upper())   
print("*"*40)

# print c to lower case
upperCase = "HELLO WORLD"
print("Here uppercase is printed in lower case : " + upperCase.lower())  
print("*"*40)


# print to title case
paragraph = "Accessing element is fast in Python Arrays because they are in a contiguous manner but insertion and deletion is quite expensive"
print("Here title is printed : " + paragraph.title())   # print to title case
print("*"*40)

# length is printed
print("Here the length is printed :  ")
print(len(paragraph))   
print("*"*40)

# replace
print("This is used to replace characters or words : " + paragraph.replace(" ","_")) 
print("*"*40)
print("This is used to replace characters or words : " + paragraph.replace("Accessing","Dhur chata")) # replace
print("*"*40)

# stripping

print("This is used to strip : " + paragraph.strip()) # stripping is used to remove space and newlines from the begining and the end of the string
print("*"*40)


#find operations
print(paragraph.find("in")) # find indexing or positioning
print("*"*40)


# print from a position to a position
print(paragraph[40:17]) # position from the index 40 to the index 17
print("*"*40)