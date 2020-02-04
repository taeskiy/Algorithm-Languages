#small program that handles Encryption/Decryption using Caesar cipher
#shifting characters by N positions to the right. A, B, C --1--> B, C, D

def Caesar(message, shift, ModeSelection):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if(char.isupper()):
            if(ModeSelection == 'E'):
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif(ModeSelection == 'D'):
                result += chr((ord(char) - shift - 65) % 26 + 65)

        if (char.islower()):
            if (ModeSelection == 'E'):
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif (ModeSelection == 'D'):
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += message[i]
    return result

message = input("Message: ")
shift = int(input("Shift by N units: "))
ModeSelection = input("'E' to Encrypt, 'D' to Decrypt: ")

print(Caesar(message, shift, ModeSelection))