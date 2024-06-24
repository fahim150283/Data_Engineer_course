###############           Task          ###########################
#
#           Sample Input
#
#           STDIN           Function
#           -----           --------
#           abracadabra     s = 'abracadabra'
#           5 k             position = 5, character = 'k'
#           Sample Output
#
#           abrackdabra


###########         answer          ################

def mutate_string(string, position, character):

    array = list(string)
    array[position]=character
    String = "".join(array)

    return String

if __name__ == '__main__':
    s = input("Please Input the string : ")
    i, c = input("Please input the index number and then a space and then the character : ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)