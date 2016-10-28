class vertex:
    def __init__(self,char,frequency):
        self.char=char
        self.frequency=frequency
        self.left=0
        self.right=0
        self.ledge=0
        self.redge=1
    def setLeftchild(self,vi):
        self.left=vi
    def setRightchild(self,vj):
        self.right=vj
    def getChar(self):
        return self.char
    def getFreq(self):
        return self.frequency


class dict:
    def __init__(self,char, binary):
        self.char=char
        self.binary=binary
    def getChar(self):
        return self.char
    def getBinary(self):
        return self.binary


def Read():
    chars=[]
    freq=[]
    i = 0
    f = open('data', 'r', encoding='utf-8')
    char=' '
    while char:
        char=f.read(1)
        if char in chars:
            freq[chars.index(char)]+=1
        else:
            chars.append(char)
            freq.append(1)
    d = open('dictionary', 'r')
    for line in d:
        if line[0]!=' ':
           line.split()
    chars[4]='$'
    chars[55]='*'
    return chars, freq


def Tree(Chars,Freq):
    W=Chars.copy()
    freq=Freq.copy()
    vertecies=[]
    i=0
    for n in W:
        vnew= vertex(n,freq[i])
        vertecies.append(vnew)
        i+=1

    while len(vertecies)>1:
        ind=freq.index(min(freq))
        vi=vertecies[ind]
        vertecies.remove(vi)
        freq.remove(freq[ind])

        ind = freq.index(min(freq))
        vj = vertecies[ind]
        vertecies.remove(vj)
        freq.remove(freq[ind])

        Vij=vertex(vi.getChar()+vj.getChar(),vi.getFreq()+vj.getFreq())
        Vij.setLeftchild(vi)
        Vij.setRightchild(vj)
        vertecies.append(Vij)
        freq.append(Vij.getFreq())
    return Vij

def TurnToBinary(V,char):
    vi = V.left
    vj = V.right
    if vi != 0 and vj != 0:
        if char in vi.getChar():
            return '0'+TurnToBinary(vi,char)
        elif char in vj.getChar():
            return '1'+TurnToBinary(vj, char)
    else:
        return ''





Chars,Freq=Read()
print(Chars)
print(Freq)
print(len(Chars))
V=Tree(Chars,Freq)
dictionary=[]

for char in Chars:
    bin=dict(char,TurnToBinary(V,char))
    dictionary.append(bin)

string =V.getChar()
print (string)
binary=''
for n in dictionary:
    print(n.getChar(),"  ",n.getBinary())
# print("  \n")
# for n in string:
#     for m in dictionary:
#         if n==m.getChar():
#             binary+=m.getBinary()
#             break
Huff_len=0
i=0
for char in dictionary:
    Huff_len+=(len(char.getBinary())*Freq[i])
    i+=1
print(Huff_len)



dictionary_idsd = dictionary.copy()
print("Dictionary length: ",len(dictionary))
# for each_bitstring in dictionary:
#     string=each_bitstring.getBinary()
#     dictionary_idsd.remove(each_bitstring)
#     for each_other in dictionary_idsd:
#         if string in each_other.getBinary():
#             print("We fucked up")












