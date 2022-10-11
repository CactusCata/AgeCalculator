from datetime import date

def charSequenceToNumber(charSequence):
    """
    Convertie une séquence de caractère en nombre
    """
    number = 0
    for c in charSequence:
        number += ord(c)
        number <<= 7
    return number >> 7

def numberToCharSequence(x):
    """
    Convertie un nombre en séquence de caractère
    """
    charSequence = ""
    while x:
        charSequence += chr(x % (1 << 7))
        x >>= 7
    return charSequence[::-1]

if __name__ == "__main__":
    # Tests unitaires
    import string
    import random

    letters = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    for i in range(10):
        randomString = ''.join(random.choice(random.choice(letters)) for i in range(random.randint(5, 20)))
        if randomString != numberToCharSequence(charSequenceToNumber(randomString)):
            print(f"Test not passed for '{randomString}'")
        else:
            print(f"Test passed for '{randomString}'")
