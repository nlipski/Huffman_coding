"""Part 1 of Assignment 3
    CMPE 380
    Nick Lipski
    Temi Ogunsanya"""


""" Node class
    attributes: characters string, frequency of character's appearance in text file
    methods: return the character, return the character's frequency, set the left child as a node, set right child as a node """
class vertex:
    def __init__(self,char,frequency):
        self.char=char
        self.frequency=frequency
        self.left=0
        self.right=0
        self.ledge=0
        self.redge=1
    def setLeftchild(self,vi):  #setting left child
        self.left=vi
    def setRightchild(self,vj): #setting right child
        self.right=vj
    def getChar(self):  #getting character
        return self.char
    def getFreq(self):
        return self.frequency

""" dict class
    used to store generated unique binary and its character
    attributes: binary, character
    methods: get binary, get character
    """
class dict:
    def __init__(self,char, binary):
        self.char=char
        self.binary=binary
    def getChar(self):
        return self.char
    def getBinary(self):
        return self.binary

"""Read method
    reads the data from the file character by character and stores newly identified inside a characters list and its frequency in frequency array
    Receives a file name that should be opened
    Returns list of frequencies and list of characters, both in the same order"""
def Read (filename):
    chars = []      # initializing  both lists
    freq = []
    f = open(filename, 'r', encoding='utf-8') # Opens the file and uses utf-8 encoding
    char = ' ' # initializes first
    while char: # loops through each character
        char = f.read(1)
        if char in chars:   # checks if the character has already been added to the array
            freq[chars.index(char)] += 1    # increases the frequency of a character
        else:
            chars.append(char)  # if hasn't been spotted yet, appends to the characters list
            freq.append(1)  # and sets the frequency to 1

    return chars, freq # returns the lists

"""Tree method
    Receives the lists with characters and frequencies
    creates a tree of nodes by combining all the characters into one node based on the frequencies
    returns a node that branches nad contains a combined string
    """
def Tree (Chars,Freq):
    W=Chars.copy()      #copies frequency and characters lists
    freq=Freq.copy()
    vertecies=[]    # creates a list for nodes
    i=0
    for n in W:    # loops through characters and frequencies lists
        vnew= vertex(n,freq[i]) # creates a node for each character and its frequency
        vertecies.append(vnew)  # appends a node to a new list
        i+=1

    while len(vertecies)>1: # loops till there is only one parent node
        ind=freq.index(min(freq))   # finds an index of the node with min frequency
        vi=vertecies[ind]           # creates it as a node
        vertecies.remove(vi)        # deletes it from frquencies and characters lists
        freq.remove(freq[ind])

        ind = freq.index(min(freq)) # same process for the other node
        vj = vertecies[ind]
        vertecies.remove(vj)
        freq.remove(freq[ind])

        Vij=vertex(vi.getChar()+vj.getChar(),vi.getFreq()+vj.getFreq()) # creates a parent node that combines 2 other nodes
        Vij.setLeftchild(vi)    # sets those 2 nodes a its children
        Vij.setRightchild(vj)
        vertecies.append(Vij)   # appends the parent to a vertices list
        freq.append(Vij.getFreq())  # appends its frequency to the frequency list for search purposes
    return Vij


""" Turning into binary method
    receives a parent node and a desired character and creates a binary path for the character
    returns a binary path"""
def TurnToBinary (V,char):
    vi = V.left # initialzies children nodes
    vj = V.right
    if vi != 0 or vj != 0:  # checks if its not at the leaf
        if char in vi.getChar():       # checks if character in the left child
            return '0'+TurnToBinary(vi,char)    # adds 0 to the path string
        elif char in vj.getChar():     # checks if character is in the right child
            return '1'+TurnToBinary(vj, char)   # adds 1 to the path string
    else:
        return ''

"""Main method of the class"""
Chars,Freq=Read('data') # gets frequency characters lists
print("Number of unique characters: ", len(Chars))
V = Tree(Chars, Freq) # gets a parent node
dictionary=[] # creates a dictionary list

for char in Chars:  # fills up the dictionary list
    bin=dict(char,TurnToBinary(V,char))
    dictionary.append(bin)

Huff_len=0
i=0
for char in dictionary:     # calculates the amount of bits required for newly compressed file
    Huff_len += (len(char.getBinary())*Freq[i])
    i += 1
print("Bits required for encoded file: ", Huff_len)
