Word=[]
Vowels=[]
FlippedVowels=[]
VowelLocation=[]
ListOfVowels=['A','E','I','O','U','a','e','i','o','u']

UserInput=input("Enter a word: ")


def VowelExtractor(UserInput):
    for i in range (len (UserInput)):
        Word.append(UserInput[i])
        if UserInput[i] in ListOfVowels:
            Vowels.append(UserInput[i])
            VowelLocation.append(i)

    return Vowels,Word

def VowelSwapper(Vowels):
    VowelExtractor(UserInput)
    j=len(Vowels)
    while 0<j:
        FlippedVowels.append(Vowels[j-1])
        j-=1
    return FlippedVowels
    
def VowelPlacer():
    VowelSwapper(Vowels)
    for i in range (len(VowelLocation)):
        Word[VowelLocation[i]]=FlippedVowels[i]
    print(''.join(Word))
    

VowelPlacer()
