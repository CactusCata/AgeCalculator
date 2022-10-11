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

def getAgeMessage(bornYear):
    """
    Détermine la date de naissance
    """
    currentTime = date.today()
    currentYear = currentTime.year
    guyAge = currentYear - bornYear

    betterAge = ""
    dayAmountInMonth = 365 / 12
    dayProportion = 1 / 365
    percentageOfPassedDay = int(100 * (dayProportion * (currentTime.month * dayAmountInMonth + currentTime.day)))

    if currentTime.month < 6:
        betterAge = f"{guyAge - 1} ({100 - percentageOfPassedDay} %)"
    else:
        betterAge = f"{guyAge} ({percentageOfPassedDay} %)"

    if guyAge < 0:
        return "Roads? Where we're going, we don't need roads"
    elif guyAge == 0:
        return "Ohhh, he is soo cute, it's Vincent Porel's baby ?"
    else:
        return f"You are {betterAge} years old."

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
