import socket
import utils.socketHelper as socketHelper
import RSA.rsa as rsa
from frame.mainFrame import MainFrame
import tkinter

HOST = "127.0.0.1"
PORT = 4567

if __name__ == "__main__":
    # Génère la clef privée et la clef publique du client
    keys = rsa.generatePrivatePublicKeys()
    privateKeyClient = keys[0]
    publicKeyClient = keys[1]

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connexion au serveur
    clientSocket.connect((HOST, PORT))

    # Recepetion de la clef publique du serveur par le client
    publicKeyServerE = int(socketHelper.receive(clientSocket))
    publicKeyServerN = int(socketHelper.receive(clientSocket))
    publicKeyServer = (publicKeyServerE, publicKeyServerN)

    # Emission de la clef publique du client au serveur
    socketHelper.send(clientSocket, publicKeyClient[0])
    socketHelper.send(clientSocket, publicKeyClient[1])

    message = socketHelper.receiveCrypt(clientSocket, privateKeyClient)

    root = tkinter.Tk("Age calculator")
    mainFrame = MainFrame(root, message, clientSocket, privateKeyClient, publicKeyServer)
