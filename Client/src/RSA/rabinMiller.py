import random
import utils.mathsUtils as mathsUtils

def step1(n):
    """
    Permet de décomposer un entier n - 1 = 2**k * m
    """
    res = n - 1
    count = 0

    while res & 1 == 0:
        res >>= 1
        count += 1
    return count, res

def isPrimeNumber(n):
    """
    Algorithme permettant de déterminer si un nombre est premier
    grâce à la méthode de Rubbin-Miller
    """
    s = step1(n)[0]
    res = mathsUtils.expoRapide(random.randint(2, n - 1), step1(n)[1], n)
    if res in {1, n - 1}:
        return True

    while s != 1:
        res = (res**2) % n
        if res == n - 1:
            return True
        s -= 1

    return False

def generatePrimeNumber(t):
    """
    Génère un nombre premier entre 2**t et 2**(t + 1) - 1
    grâce à la méthode de Rubbin-Miller
    """
    number = random.randint(1 << t, 1 << (t + 1))
    if number & 1 == 0:
        number += 1
    while not isPrimeNumber(number):
        number = random.randint(1 << t, 1 << (t + 1))
        if number & 1 == 0:
            number += 1
    return number
