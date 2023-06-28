# vigenere

before i figure out how to break the enigma, i think it would be wise to try and crack a simpler polyalphabetic code: the vigenere cipher. based on the letters of a keyword, the vigenere cipher uses interwoven caesar ciphers to encrypt alphabetic text.

in a caesar cipher, each letter of a message is shifted by some number of places. in a caesar cipher with a shift of 4, the letter 'a' might correspond to 'e' and the letter 'f' might become 'j'. in a vigenere cipher, each letter has a different shift value based on the key.

let's assume the plaintext that is to be encrypted is `apocalypse` and the key is `cas`. the first step is to 'extend' the key so that it covers each letter of the plaintext: `cas` would become `cascascasc`. now for each letter in the plaintext, you find the corresponding letter in the extend key, and shift the plaintext letter over by the index of the key letter in the alphabet. 

so the letter 'a' in `apocalypse` corresponds with the letter 'c' in `cascascasc`, and since the index of 'c' in the alphabet is 2, 'a' shifts twice over to become 'c'. for the plaintext letter 'p', the key letter is 'a' with an index of 0, so 'p' doesn't shift (it shifts by 0). so on and so forth.

eventually...
plaintext: `apocalypse`
key: `cas` -> `cascascasc`
ciphertext: `cpgeadapkg`

now that we understand what the vigenere cipher is, here is two ways of deciphering vigenere ciphertext **without** knowing the key.

### dictionary attack

this is a type of brute force attack -- with a list of words from the dictionary, we can use trial-and-error to guess what a potential key might be. note that this only works when the key is a single english word, anything else and brute forcing the ciphertext won't work.

in python, i iterated through each word in a dictionary file and set it as a potential key. then, i would decipher the ciphertext with that key and checked each word in the output to see if it was also in the dictionary file. if a certain percentage of the words in deciphered text were also found in the dictionary file, i alerted the user that a potential match may be found.

### kasiski examination

a kasiski analysis has two main parts: finding the length of the key using n-grams and finding the letters of the key using frequency analysis. the examination involves searching for strings of characters that are repeated within the ciphertext.

#### finding key length using n-grams
this logic is so simple yet so fascinating. in a cipher text, we can capitalize on certain strings of characters that repeat themselves to figure out the length of a key. these strings of characters are known as n-grams, bigrams for two letter (or word) strings or trigrams for three letter (or word) strings. for this kasiski examination, i chose to find four-letter 'quadgrams' for my character strings. it is basically imperative that the cipher text we conduct the analysis upon is rather large, so we have many quadgrams to work with. now, if we look at the distance between quadgrams, we know that our key is almost always a factor of that distance (sometimes there are coincidental repetitions). so if we calculate all the distances between all quadgrams, our key length will be the greatest common factor of all the distances.

#### finding key letters using frequency analysis
after figuring out the key length, we can conduct frequency analysis to figure out the letters of the key. the basis of frequency analysis relies on the frequency of letter usage in the english language.

![frequency](/images/frequency.png)
from [cornell's dept of math](http://pi.math.cornell.edu/~morris/135/letfreq.html)

for each index of our key, we need to iterate through the alphabet and calculate the letter which produces a frequency distribution that most closely resembles the relative frequency of letters in english. i did this by assigning each potential letter in the key with a score that is equal to the sum of the individual letter occurances in the deciphered text * letter relative frequency in english. by taking the highest value of this score, we can find a letter for the key which produces deciphered text that most closely mirrors the standard letter frequency. 

figuring the logic and how to work with so many python dictionaries at once took me hours, but i did it. next up on the cryptography to-do list is making the python bombe machine to crack the enigma code.
