from vigenere import vigenere
from re import sub

"""this brute-force attack only works if the encryption key is a word."""

def hack(cipherText):
    
    # gather valid words from dictionary file
    x = open('dictionary.txt', "r")
    words = x.readlines()
    x.close

    # make words lowercase and strip of extra formatting
    newWords = []
    for word in words:
        newWords.append(word.strip().lower())

    # use each dictionary word as the key
    for word in newWords:
        result = vigenere(cipherText, word, "decrypt")
        resultWords = result.split()

        # check how many valid words are in the resulting decryption
        counter = 0
        for item in resultWords:
            item = sub(r'[^a-z]+', "", item)
            if item in newWords:
                counter = counter + 1
        print(word + ": " + str(counter / len(resultWords)))

        # show user potentially valid key
        if counter / len(resultWords) > 0.5: # adjust desired accuracy here
            print("this is a potential result. press enter to continue looking.")
            print(word + ": " + result)
            x = input("> ")

    print("complete.")

cipherText = "EDIT ME" # the longer the cipher the better
hack = hack(cipherText)