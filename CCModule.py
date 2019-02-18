
lowerAlphaMax=ord('z')
upperAlphaMax=ord('Z')

lowerAlphaMin=ord('a')
upperAlphaMin=ord('A')
upperBound=90

def encrypt(currentChar,cipherShift) :

    alphaValue=ord(currentChar)
    
    if(currentChar==' 'or ord(currentChar)==32) : cipherChar=currentChar
    #if uppercase and passing Z
    elif(alphaValue<=90 and (alphaValue+cipherShift)>upperAlphaMax) :
        difference=((alphaValue+cipherShift)-upperAlphaMax)
        cipherChar=chr(64+difference)
        
    #if lowercase and passing z
    elif(alphaValue>upperBound and (alphaValue+cipherShift)>lowerAlphaMax) :
        difference=((alphaValue+cipherShift)-lowerAlphaMax)
        cipherChar=chr(96+difference)

    #if cipher shift does not pass z is lowercase or Z if upperCase
    else : cipherChar=chr(ord(currentChar)+cipherShift)
    return cipherChar


def decrypt(currentChar,cipherShift) :

    alphaValue=ord(currentChar)
    
    if(currentChar==' 'or ord(currentChar)==32) : cipherChar=currentChar
    #if uppercase and going further back thanA
    elif(alphaValue<=90 and (alphaValue-cipherShift)<upperAlphaMin) :
        difference=(cipherShift-(alphaValue-upperAlphaMin))
        cipherChar=chr(91-difference)
        
    #if lowercase and going further back than a
    elif(alphaValue>upperBound and (alphaValue-cipherShift)<lowerAlphaMin) :
        difference=(cipherShift-(alphaValue-lowerAlphaMin))
        cipherChar=chr(123-difference)

    #if cipher shift does not go under a and is lowercase or A if upperCase
    else : cipherChar=chr(ord(currentChar)-cipherShift)
    return cipherChar
