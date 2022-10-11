from tkinter import CENTER
from frame.IFrame import IFrame

class ErrorFrame(IFrame):
    """
    Cette classe permet d'afficher une frame "basique", comme
    par exemple des messages d'erreur
    """

    def __init__(self, master, message, title="Message", nextStep=None):
        """
        master IFrame mère
        message Message à afficher
        title Titre de l'interface
        nextStep Fonction à executer à la fermeture de cette fenêtre
        """
        super().__init__(master, title, 600, 150)

        if (nextStep != None):
            super().setClosingCallback(nextStep)

        super().createLabel(0.5, 0.1, message, fontSize=20, anchor=CENTER)
        super().loop()
