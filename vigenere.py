ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main():

    #encryption
    messageOne = "EDIT ME" # edit message here
    keyOne = "EDIT ME" # edit key here

    print("encryption")
    print(vigenere(messageOne, keyOne, "encrypt"))
    print("\n")

    #decryption
    messageTwo = "EDIT ME" # edit message here
    keyTwo = "EDIT ME" # edit key here

    print("decryption")
    print(vigenere(messageTwo, keyTwo, "decrypt"))
    print("\n")

def vigenere(message, key, direction):

    # make message and key lowercase for consistency
    message = message.lower()
    key = key.lower()

    #adjust key for message length
    while len(key) < len(message):
        key = key + key
    

    result = ""
    for i in range(len(message)):
        # ignore non-letter characters
        if not message[i].isalpha():
            result = result + message[i]
            key = key[:i] + " " + key[i:]
        else:
            messageLetter = message[i]
            keyLetter = key[i]

            # row and column refers to the vigenere square
            row = ALPHABET.find(messageLetter)
            column = ALPHABET.find(keyLetter)
            if direction == "encrypt":
                result = result + ALPHABET[(row+column) % 26]
            elif direction == "decrypt":
                result = result + ALPHABET[(row-column) % 26]
            else:
                print("invalid direction")
                return ""
    return result
    
if __name__ == "__main__":
    main()