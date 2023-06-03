import random
from string import digits, ascii_letters

listOfChar = list(digits + ascii_letters)

def encryption(message):
    random.shuffle(listOfChar)
    rotVersion = random.randint(1,62)
    key = ''.join([l for l in listOfChar])

    encryptedMessage = ''
    for i in range(len(message)):
        if message[i] in key:
            index = key.index(message[i])
            encryptedMessage += key[(index+rotVersion)%62]
        else:
            encryptedMessage += message[i]

    return rotVersion, key, encryptedMessage

if __name__=="__main__":
    print(encryption('hello'))