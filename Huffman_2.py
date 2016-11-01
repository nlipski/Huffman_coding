"""Part 2 of Assignment 3
    CMPE 380
    Nick Lipski
    Temi Ogunsanya"""

""" dict class
    used to store generated unique binary and its character
    attributes: binary, character
    """
class dict:
    def __init__(self, char, binary):
        self.char=char
        self.binary=binary

"""Read dictionary method
    reads a a dictionary file
    returns a list of dictionary list filled with dict objects"""
def read_dictionary():
    dictionary=[]
    f = open('dictionary', 'r')
    for line in f:
        if line[0]!=' ':
            char, binary=line.split(' ')
            dictionary.append(dict(char,binary[:-1]))
        else:
            binary=line[2:]
            dictionary.append(dict(' ',binary[:-1]))

    return dictionary


"""Read file method
    receives a dictionary list
    returns a decoded string """
def read_file(dictionary):
    mystery = ''    # initializing some of the variables
    bin_code = ''
    i = 0
    possible = 0
    f = open('mystery', 'r')    # reades the encoded file
    char = ' '
    list_of_possible = []

    while char:     # loops each character at a time
        char = f.read(1)
        i += 1  # increments the length counter
        counter=0   # initializes the counter of matching binaries
        bin_code += char
        for word in dictionary: # loops though the dictionary
                if len(word.binary) >= i and word.binary[:i] == bin_code[:i]:   # checks if any binary matches the acquired code
                    list_of_possible.append(word)   # adds to the possibilities list
                    counter+=1
                if counter>1:   # if there are more than one matching binary then break
                    break
        possible = len(list_of_possible)    # number of possibilities
        if possible == 1:                   # if there is only one possible char
            if list_of_possible[0].char=='<LF>':    # changes the character
                list_of_possible[0].char='\n'
            mystery += list_of_possible[0].char # adds the character to the string
            i = 0   # sets the counter back to zero
            bin_code = '' # and clears binary string

        list_of_possible = []  # clears up list of possible binaries

    return mystery # returns a decoded string

dictionary=read_dictionary() # creates dictionary list
print(read_file(dictionary)) # retrieves decoded message
