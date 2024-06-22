#  string manipulation


a = "hello"
b = "world"
c = a +" "+ b +" "   # merge strings

print("Here a : " + a)
print("Here b : " + b)
print("Here c : " + c)
print("Here c is print double :" + c * 2)    # here * is used to print multiple times(repeatation)

print("Here C is printed in upper case : " + c.upper())   # print c to upper case


upperCase = "HELLO WORLD"
print("Here uppercase is printed in lower case : " + upperCase.lower())   # print c to lower case


paragraph = "Accessing element is fast in Python Arrays because they are in a contiguous manner but insertion and deletion is quite expensive"
print("Here title is printed : " + paragraph.title())   # print c to title case