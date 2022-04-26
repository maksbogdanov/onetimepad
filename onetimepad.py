def strxor(a, b):
    """Return the xor of two strings of different lengths."""
    if len(a) > len(b):
        return ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def encrypt(key, plaintext):
    """Encryption algorithm takes key and message. And return ciphertext."""
    ciphertext = strxor(key, plaintext)
    return ciphertext


def decrypt(key, ciphertext):
    """Decryption algorithm takes key and ciphertext. Then return message."""
    plaintext = strxor(key, ciphertext)
    return plaintext
