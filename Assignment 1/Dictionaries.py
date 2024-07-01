
################################################################################
                                # Task 1
################################################################################

dic = {
    "Title" : "The Hound of the Baskervilles",
    "Author" : "Arthur Conan Doyle",
    "Year" : "1902"
}
print("#" * 90)


################################################################################
                                # Task 2
################################################################################

print ("In the dictionary, the field Title :" , dic["Title"])
print ("In the dictionary, the field Author :" , dic["Author"])
print ("In the dictionary, the field Year :" , dic["Year"])
print("#" * 90)


################################################################################
                                # Task 3
################################################################################

dic1 = {"Genre":"Crime Fiction"}
dic.update(dic1)
print ("In the dictionary, the field Title :" , dic["Title"])
print ("In the dictionary, the field Author :" , dic["Author"])
print ("In the dictionary, the field Year :" , dic["Year"])
print ("In the dictionary, the field Genre :" , dic["Genre"])
print("#" * 90)



################################################################################
                                # Task 4
################################################################################

for i in dic.keys():
    print(dic[i])