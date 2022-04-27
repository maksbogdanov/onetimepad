import onetimepad

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

# Let us see what goes wrong when a stream cipher key is used more than once
chipertexts = [onetimepad.encrypt(KEY, message) for message in MSGS]

# XOR the ciphertexts together, and consider what happens when a space is XORed with a character in [a-zA-Z]
target = chipertexts[0]
for chipertext in chipertexts[1:]:
    xored = onetimepad.strxor(target, chipertext)
    result = list(map(lambda c: c if c.isalpha() else '#', xored))
    print(result)

# Now we need to assume what is encrypted in the chipertext to hack  the key
crack = input("Enter the crack: ")
key = onetimepad.strxor(crack, target)

# Received decrypted messages
for chipertext in chipertexts:
    plaintext = onetimepad.decrypt(key, chipertext)
    print(plaintext)
