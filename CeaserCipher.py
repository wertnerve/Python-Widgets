import random
import CCModule
import time

def generateCipher():
    encryptedMessage=""
    cipherShift=random.randint(1,25)
 
    print("The cipher will shift each letter",cipherShift,'places!')
    with open('message.txt') as f:
     while True:
      currentChar = f.read(1)
      if not currentChar:
       f.close()
       break
      cipherChar=CCModule.encrypt(currentChar,cipherShift)              
      encryptedMessage+=cipherChar
       
    outputEncryptedMessage(encryptedMessage)

def outputEncryptedMessage(encryptedMessage):
    print("CipherText => ",encryptedMessage)
    newFile=open("encrypted_message.txt","w")
    newFile.write(encryptedMessage)
    newFile.close()
    
    
def buffer():
    string = "..."
    for char in string:
     print(char, end='')
     time.sleep(.25)
    
#lowercase comes after uppercase
while True:

 print("Select an option!")
 print("Enter 1 to encrypt a new file!")
 print("Enter 2 to encrypt the pre-existing file")
 print("Enter any other key to decrypt the file! ")
 print("Enter 0 to close the program")


 answer=input("=> ")
 buffer()
 print()
#skip to decrypt
#answer=2

 if (answer=='1'):
    message=input("Enter the message you want to encrypt => ")
    newFile=open('message.txt','w')
    newFile.write(message)
    newFile.close()
    generateCipher() 

 elif (answer=='2'):
    generateCipher()

 elif(answer=='0'):
    print("Thank you for using this program! Annyeonghi kaseyo!(Bye-Bye!)")
    exit()
    
 else:
  cipherNum=int(input("Enter the cipher number => "))
  decryptedMessage=""
  with open('encrypted_message.txt') as f:
   while True:
     currentChar = f.read(1)
     if not currentChar:
       f.close()
       break
    
     cipherChar=CCModule.decrypt(currentChar,cipherNum)
     decryptedMessage+=cipherChar
  print("With",cipherNum,"as your key, your plaintext is =>", decryptedMessage)
 buffer()
 print()
 
