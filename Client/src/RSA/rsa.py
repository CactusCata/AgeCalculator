import RSA.rabinMiller as rabinMiller
import utils.mathsUtils as mathsUtils

def chiffrement(x, e, n):
    """
    Permet de chiffrer le message x
    """
    return mathsUtils.expoRapide(x, e, n)

def dechiffrement(x, v, n):
    """
    Permet de déchiffrer le message
    """
    return mathsUtils.expoRapide(x, v, n)

def generatePrivatePublicKeys():
    """
    Permet de générer une paire de clefs, la première est privée, l'autre publique
    """
    t = 256
    p = rabinMiller.generatePrimeNumber(t)
    q = rabinMiller.generatePrimeNumber(t)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = mathsUtils.findCoPrimeOf(phi)
    v = mathsUtils.euclide_e(phi, e)[0] % phi

    return ((v, n), (e, n))

if __name__ == "__main__":
    # Test unitaire pour le chiffrement et déchiffrement RSA
    t = 1024
    p = rabinMiller.generatePrimeNumber(t)
    q = rabinMiller.generatePrimeNumber(t)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = mathsUtils.findCoPrimeOf(phi)
    v = mathsUtils.euclide_e(phi, e)[0] % phi

    print(f"Clef publique: e: {e} n: {n}")
    print(f"Clef privée: v: {v} n: {n}")

    print(dechiffrement(chiffrement(1234, e, n), v, n))
