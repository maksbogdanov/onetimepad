# One-Time Pad
Let us see what goes wrong when a stream cipher key is used more than once. First I encrypted eleven messages with the same key:
```Python
KEY = "The secret message is: When using a stream cipher, never use the key more than once"

MSGS = (
    "When using a stream cipher, never use the key more than once",
    "We can factor the number 15 with quantum computers. We can also factor the number 1",
    "Euler would probably enjoy that now his theorem becomes a corner stone of crypto - ",
    "The nice thing about Keeyloq is now we cryptographers can drive a lot of fancy cars",
    "The ciphertext produced by a weak encryption algorithm looks as good as ciphertext ",
    "You don't want to buy a set of car keys from a guy who specializes in stealing cars",
    "There are two types of cryptography - that which will keep secrets safe from your l",
    "There are two types of cyptography: one that allows the Government to use brute for",
    "We can see the point where the chip is unhappy if a wrong bit is sent and consumes ",
    "A (private-key)  encryption scheme states 3 algorithms, namely a procedure for gene",
    " The Concise OxfordDictionary (2006) deﬁnes crypto as the art of  writing o r sol",
)

chipertexts = [onetimepad.encrypt(KEY, message) for message in MSGS]
```
XOR the ciphertexts together, and consider what happens when a space is XORed with a character in [a-zA-Z]:
```
['#', '#', 'E', '#', 'A', '#', 'S', '#', '#', '#', 'T', '#', 'R', 'S', '#', '#', '#', 'A', '#', 'U', '#', '#', '#', '#', 'E', 'C', '#', '#', '#', '#', '#', '#', 'R', 'Q', '#', '#', '#', 'T', '#', '#', 'E', 'C', '#', '#', '#', 'U', '#', '#', '#', '#', '#', 'T', '#', '#', 'N', 'C', '#', '#', 'C', '#']
['#', '#', '#', '#', 'R', 'U', '#', '#', '#', '#', 'D', 'A', 'P', '#', '#', '#', '#', '#', '#', 'Y', 'C', '#', '#', '#', '#', '#', '#', 'T', '#', '#', '#', 'E', '#', 'O', '#', 'S', '#', 'I', '#', 'H', '#', 'H', '#', '#', '#', 'E', '#', 'O', '#', '#', 'C', '#', '#', '#', '#', '#', '#', 'N', '#', '#']
['#', '#', '#', 'N', 'N', '#', '#', '#', 'N', '#', 'H', '#', 'N', '#', 'T', '#', '#', '#', '#', 'T', 'C', '#', '#', '#', '#', '#', 'C', 'Q', 'N', '#', '#', 'E', '#', 'O', '#', 'S', '#', 'E', 'T', '#', '#', 'Y', '#', '#', '#', 'G', '#', '#', '#', '#', 'E', '#', '#', 'A', '#', 'A', '#', 'N', '#', '#']
['#', '#', '#', 'N', 'C', '#', '#', '#', '#', '#', 'T', '#', 'X', '#', 'T', '#', '#', '#', '#', 'U', '#', '#', '#', 'H', '#', '#', '#', 'A', 'N', '#', '#', '#', '#', '#', '#', '#', '#', 'R', '#', '#', '#', 'I', '#', '#', 'Y', 'A', '#', '#', '#', '#', 'I', '#', '#', '#', 'N', 'L', '#', '#', '#', '#']
['#', '#', '#', 'N', 'D', '#', '#', 'N', '#', 'G', 'W', '#', 'N', '#', 'T', '#', '#', 'A', '#', 'U', '#', 'I', '#', 'H', '#', '#', 'X', '#', '#', '#', 'V', '#', '#', 'R', 'U', '#', '#', 'Y', '#', 'H', '#', 'R', '#', '#', 'Y', 'A', 'M', '#', '#', '#', '#', '#', '#', '#', 'N', 'S', '#', '#', '#', '#']
['#', '#', '#', '#', 'E', 'U', '#', '#', '#', 'G', 'T', '#', 'O', 'S', '#', '#', '#', '#', '#', '#', '#', '#', 'P', '#', '#', '#', '#', 'T', '#', '#', '#', '#', '#', 'H', '#', 'S', 'H', '#', '#', '#', '#', 'T', 'K', '#', '#', 'I', '#', '#', 'R', '#', 'I', '#', '#', 'A', '#', 'E', '#', '#', 'C', '#']
['#', '#', '#', '#', 'E', 'U', '#', '#', '#', 'G', 'T', '#', 'O', 'S', '#', '#', '#', '#', '#', '#', '#', '#', 'P', '#', '#', '#', 'X', 'O', '#', '#', '#', '#', '#', 'Y', 'O', 'S', '#', 'N', '#', 'H', '#', 'H', '#', '#', 'Y', 'A', '#', '#', '#', '#', 'S', 'T', '#', '#', '#', '#', '#', '#', '#', '#']
['#', '#', 'E', '#', 'A', '#', 'S', '#', '#', '#', '#', '#', 'H', '#', 'T', '#', '#', '#', '#', 'T', 'C', '#', '#', '#', '#', '#', '#', 'T', '#', '#', 'V', '#', '#', 'I', '#', 'S', '#', 'S', 'T', '#', '#', 'H', '#', '#', '#', 'Y', 'M', '#', '#', 'E', 'A', 'T', '#', '#', '#', 'N', '#', 'N', '#', '#']
['#', 'H', 'M', '#', 'R', '#', '#', '#', '#', '#', '#', '#', 'E', '#', '#', 'R', 'E', '#', '#', 'C', '#', '#', '#', '#', '#', '#', 'B', '#', '#', '#', '#', '#', '#', 'E', 'U', '#', '#', 'A', '#', '#', '#', '#', 'X', 'E', '#', 'L', '#', '#', '#', '#', 'T', '#', '#', '#', 'B', '#', '#', '#', '#', '#']
['w', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#', '#', '#', '#', '#', '#', '#', '#', 'd', '#', '#', '#', '#', '#', '#', 'M', 'R', '#', 'E', '#', 'W', 'B', '#', 'C', 'Z', 'E', 'D', '#', 'ﭩ', '#', 'E', '#', 'E', '#', 'R', '#', '#', '#', '#', '#', '#', '#', 'A', '#', 'H', '#', 'N', '#', '#']
```
What do we get by doing so? If there is a space character in either side of the XOR operator and an alphabet character in the other one at the same position, after XOR operation the alphabet character will be flipped from lower to upper case or upper to lower case. As a result, we get a partial decryption of the target message:
```
When usnng a strea  ciphec, never use the key more t an  nc 
```
Now we can assume what was in this message. It's easy:
```
When using a stream cipher, never use the key more than once
```
When we have the ciphertext and plaintext, we can get the key and decrypt other messages:
```Python
key = onetimepad.strxor(crack, target)
for chipertext in chipertexts:
    plaintext = onetimepad.decrypt(key, chipertext)
    print(plaintext)
```
