import RSA.rsa as rsa
import utils.utils as utils
import sys

def send(connexion, message):
    """
    Permet d'envoyer à un écouteur un message en clair
    """
    try:
        connexion.send(str(message).encode("UTF-8"))
    except ConnectionResetError:
        connexion.close()
        sys.exit()

def receive(connexion):
    """
    Permet de récuperer un message en clair
    """
    try:
        return connexion.recv(4096).decode("UTF-8")
    except ConnectionResetError:
        connexion.close()
        sys.exit()

def sendCrypt(connexion, encryptionKey, message):
    """
    Permet d'envoyer un message chiffré
    """
    x = utils.charSequenceToNumber(message) # Conversion du message en nombre décimal
    encodedMessage = rsa.chiffrement(x, encryptionKey[0], encryptionKey[1]) # Chiffrement du nombre décimal
    send(connexion, encodedMessage) # Envoie du nombre décimal chiffré

def receiveCrypt(connexion, decryptionKey):
    """
    Permet de lire un message chiffré
    """
    encryptedMessage = int(receive(connexion)) # Reception du nombre chiffré
    decodedMessage = rsa.dechiffrement(encryptedMessage, decryptionKey[0], decryptionKey[1]) # Dechiffrement du nombre décimal
    return utils.numberToCharSequence(decodedMessage) # Conversion du nombre décimal déchiffré en message
