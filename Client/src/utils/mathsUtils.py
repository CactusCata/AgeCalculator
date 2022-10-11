def euclide_e(a, n):
    """
    Soient a et n deux entiers, l'algorithme d'Euclide étendu permet de calculer u et v dans Z tels que au+vn=pgcd(a,n).
    """
    u_1 = n
    v_1 = 1
    w_1 = 0
    u_2 = a
    v_2 = 0
    w_2 = 1

    while u_1 % u_2 != 0:
        u_3 = u_1 % u_2
        v_3 = v_1 - (u_1 // u_2) * v_2
        w_3 = w_1 - (u_1 // u_2) * w_2

        u_1 = u_2
        v_1 = v_2
        w_1 = w_2

        u_2 = u_3
        v_2 = v_3
        w_2 = w_3

    return [v_2, w_2, u_2]

def expoRapide(x, n, mod):
    """
    Réalise l'exponentition rapide modulaire de x à la puissance n modulo mod
    """
    res = 1
    while n:
        if n & 1:
            res = (res * x) % mod
        x = (x * x) % mod
        n >>= 1
    return res

def pgcd(a, b):
    """
    Détermine le pgcd de a et de b récursivement
    """
    if b == 0:
        return a
    return pgcd(b, a % b)

def findCoPrimeOf(a):
    i = 3
    while pgcd(a, i) != 1:
        i += 2
    return i

def isInt(stringInt):
    """
    Détermine si une chaine de caractère peut être convertie en nombre entier
    """
    try:
        int(stringInt)
        return True
    except ValueError:
        return False
