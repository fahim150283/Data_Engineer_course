# Task

# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Input Format

# A single line containing a string .

# Constraints


# Output Format

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# Sample Input

# qA2
# Sample Output

# True
# True
# True
# True
# True




def string_validators(string):
    b1 = False
    b2 = False
    b3 = False
    b4 = False
    b5 = False
    arr = list(string)
    for i in range (len(arr)):
        if arr[i].isalnum():
            b1 = True
        if arr[i].isalpha():
            b2 = True
        if arr[i].isdigit():
            b3 = True
        if arr[i].islower():
            b4 = True
        if arr[i].isupper():
            b5 = True
    
    s = [b1,b2,b3,b4,b5]
    return s

if __name__ == '__main__':
    S = input()
    s_new = string_validators(S)
    for i in range (len(s_new)):
        print(s_new[i])