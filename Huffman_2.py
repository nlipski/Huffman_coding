class dict:
    def __init__(self, char, binary):
        self.char=char
        self.binary=binary


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


def read_file(dictionary):
    mystery = ''
    bin_code = ''
    i = 0
    possible = 0
    f = open('mystery', 'r')
    char = ' '
    list_of_possible = []
    while char:
        char = f.read(1)
        i += 1
        counter=0
        bin_code += char
        for word in dictionary:
                if len(word.binary) >= i and word.binary[:i] == bin_code[:i]:
                    list_of_possible.append(word)
                    counter+=1
                if counter>2:
                    break
        possible = len(list_of_possible)
        if possible == 1:
            if list_of_possible[0].char=='<LF>':
                list_of_possible[0].char='\n'
            mystery += list_of_possible[0].char
            i=0
            bin_code=''

        list_of_possible = []
    return mystery

dictionary=read_dictionary()
print(read_file(dictionary))







