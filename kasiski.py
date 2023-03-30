from re import sub
from vigenere import vigenere

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
frequency = {"a": 8.2 ,"b": 1.5, "c": 2.8, "d": 4.3, "e": 13, "f": 2.2,
              "g": 2, "h": 6.1, "i": 7, "j": 0.15, "k": 0.77, "l": 4,
              "m": 2.4, "n": 6.7, "o": 7.5, "p": 1.9, "q": 0.095, "r": 6,
              "s": 6.3, "t": 9.1, "u": 2.8, "v": 0.98, "w": 2.4, "x": 0.15,
              "y": 2, "z": 0.074}

def kasiski(message):
    message = sub(r'[^a-z]+', "", message.lower())
    return(findKey(message, findKeyLength(findRepeats(message))))

def findRepeats(message):
    sequences = {}
    for seqLength in range(4,5): #choose n-grams here

        #gather sequences
        for seqBegin in range(len(message) - seqLength):
            seq = message[seqBegin : seqBegin + seqLength]

            #check for repetitions
            for i in range(seqBegin + seqLength, len(message) - seqLength):
                if message[i : i + seqLength] == seq:
                    if seq not in sequences:
                        sequences[seq] = []
                    sequences[seq].append(i - seqBegin)

    return sequences

def findKeyLength(sequences):

    #see if the distance between repetitions is divisible by a given number
    potentialKeyAccuracy = {}
    for i in range(2, 17): #adjust potential key lengths here
        counter = 0
        secondaryCounter = 0
        for item in sequences:
            for num in sequences[item]:
                secondaryCounter = secondaryCounter + 1
                if num % i == 0:
                    counter = counter + 1
        if secondaryCounter == 0:
            raise Exception("uh oh! this ciphertext isn't going to work. try again with a different cipher! (the longer the cipher the better)")
        counter = counter / secondaryCounter
        potentialKeyAccuracy[i] =  counter
    
    #filter out key lengths which cannot almost always divide the repetition distance 
    potentialKeys = []
    for item in potentialKeyAccuracy:
        if potentialKeyAccuracy[item] > 0.80: #adjust desired accuracy here
            potentialKeys.append(item)

    #return the greatest number which divides the repetition distances consistently
    return max(potentialKeys)

def findKey(message, keyLength):
    key = ""

    #iterate through each key position
    for i in range(keyLength):

        #initialize dictionaries to store letter occurances
        positionalDict = {}
        scoredDict = {}
        for letter in ALPHABET:
            positionalDict[letter] = {}
            scoredDict[letter] = 0
            for letter2 in ALPHABET:
                positionalDict[letter][letter2] = 0

        #iterate through each potential letter for the key position
        for letter in ALPHABET:   
            index = i
            while index < len(message):
                row = ALPHABET.find(message[index])
                column = ALPHABET.find(letter)
                positionalDict[letter][ALPHABET[(row-column) % 26]] = positionalDict[letter][ALPHABET[(row-column) % 26]] + 1
                index = index + keyLength

            #frequency analysis score by multiplying a character's natural frequency and occurances in the cipher
            for char in ALPHABET:
                scoredDict[letter] = scoredDict[letter] + (positionalDict[letter][char] * frequency[char])

        #find the letter with the highest score
        letter = max(scoredDict, key=scoredDict.get)
        key = key + letter
    
    return key

message = "EDIT ME" # edit cipher here, the longer the cipher the better

print("\n" + "the key is probably: " + "\n" + kasiski(message) + "\n")
print("therefore, the deciphered text is probably:" + "\n" + vigenere(message, kasiski(message), "decrypt") + "\n")