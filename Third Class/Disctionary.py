my_dictionary = {
    "name":"fahim",
    "age":75,
    'gender':"male"
}


print (my_dictionary["age"])

print(my_dictionary.get("age"))

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())


my_dictionary["new key"] = "new value"
print(my_dictionary)

my_dictionary["new key"] = "updated value"
print(my_dictionary)

second_dictionary = {
    "how":"what",
    "when":"now"
}

my_dictionary.update(second_dictionary)
print("This extends the second dictionary to the first one",my_dictionary)