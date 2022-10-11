import socket
import sys
import utils.socketHelper as socketHelper
import utils.utils as utils
import utils.mathsUtils as mathsUtils
import RSA.rsa as rsa
import threading

HOST = "127.0.0.1"
PORT = 4567

def clientThread(connexion, address, publicKeyServer):
    port = address[1]
    print(f"{port} >> Open connection with client {address}")
    # Envoie de la clef publique du serveur au client
    socketHelper.send(connexion, publicKeyServer[0])
    socketHelper.send(connexion, publicKeyServer[1])

    # Reception de la clef publique du client au serveur
    publicKeyClientE = int(socketHelper.receive(connexion))
    publicKeyClientN = int(socketHelper.receive(connexion))
    publicKeyClient = (publicKeyClientE, publicKeyClientN)

    socketHelper.sendCrypt(connexion, publicKeyClient, "What year were you born ?")

    while True:
        yearOfBrithString = socketHelper.receiveCrypt(connexion, privateKeyServer)

        if yearOfBrithString == "close":
            print(f"{port} >> Client exit his application.")
            break

        if mathsUtils.isInt(yearOfBrithString):
            guyAgeMessage = utils.getAgeMessage(int(yearOfBrithString))
            socketHelper.sendCrypt(connexion, publicKeyClient, guyAgeMessage)
        else:
            socketHelper.sendCrypt(connexion, publicKeyClient, f"The format of year is unknow.")

    connexion.close()
    print(f"{port} >> Connection has been closed.")
    sys.exit()

if __name__ == "__main__":
    # Génération de la clef privée et publique
    keys = rsa.generatePrivatePublicKeys()
    privateKeyServer = keys[0]
    publicKeyServer = keys[1]

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Tentative de connexion
    try:
        serverSocket.bind((HOST, PORT))
    except socket.error:
        print(f"Connection to host {HOST} and port {PORT} failed.")
        sys.exit()

    serverSocket.listen(5)

    while True:
        print("Waiting client...")
        # Reception d'un client
        connexion, address = serverSocket.accept()
        print(f"{address[1]} >> New Client !")

        thread = threading.Thread(None, clientThread, None, (connexion, address, publicKeyServer), {})
        thread.start()
