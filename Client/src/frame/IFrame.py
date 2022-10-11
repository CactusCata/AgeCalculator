from tkinter import Label, Text, Scale, Canvas, Toplevel, CENTER, NW, Frame, ttk, Checkbutton, IntVar
from tkinter.ttk import Combobox
from frame.libs.tkinter_custom_button import TkinterCustomButton
from PIL import Image, ImageTk
import frame.utils.screenUtils as screenUtils

class IFrame:

    def __init__(self, master, title, dimX, dimY, binds={}):
        """
        master Fenêtre mère
        title Titre de l'interface
        dimX Largeur de la fenêtre en pixel
        dimY Hauteur de la fenêtre en pixem
        binds Events à detecter
        """
        self.master = master
        self.dimX = dimX
        self.dimY = dimY
        self.master.minsize(dimX, dimY)
        self.master.maxsize(dimX, dimY)
        xScreenPos = max(0, screenUtils.screenSize[0] // 2 - dimX // 2)
        yScreenPos = max(0, screenUtils.screenSize[1] // 2 - dimY // 2)
        self.master.geometry(f"{dimX}x{dimY}+{xScreenPos}+{yScreenPos}")
        self.master.iconbitmap('res/img/icon.ico')
        self.master.title(title)
        self.master.configure(background='#1E1E1E')
        self.master.protocol("WM_DELETE_WINDOW", self.closingCallbackEvent)
        self.closingCallback = None
        self.canvas = None
        for eventName, callback in binds.items():
            self.master.bind_all(eventName, callback)

    def setClosingCallback(self, callback):
        """
        Evenement à déclencher à la fermeture de
        la fenêtre
        """
        self.closingCallback = callback

    def closingCallbackEvent(self):
        """
        Destruction de la fenêtre
        """
        if self.closingCallback != None:
            self.closingCallback()
        self.master.destroy()

    def createLabel(self, relX, relY, text, fontSize=15, anchor=NW):
        """
        Créer un label
        """
        label = Label(self.master, text=text, bg='#1E1E1E', fg='#ABB2B9', font=("Arial", fontSize))
        label.place(relx=relX, rely=relY, anchor=anchor)
        return label

    def createTextBox(self, relX, relY, text="", width=1, height=1, fontSize=13, anchor=NW, binds={}):
        """
        Créer une boite de dialogue
        """
        textBox = Text(self.master, width=width, height=height, bg='#1E1E1E', fg='#ABB2B9', font=("Arial", fontSize))
        textBox.place(relx=relX, rely=relY, anchor=anchor)
        textBox.insert(1.0, text)
        for eventName, callback in binds.items():
            textBox.bind(eventName, callback)
        return textBox

    def createButton(self, relX, relY, text, width, height, callback, fontSize=13, anchor=NW):
        """
        Créer un boutton
        """
        button = TkinterCustomButton(master=self.master,
                                                bg_color="#1E1E1E",
                                                fg_color="#1E1E1E",
                                                border_color="#ABB2B9",
                                                hover_color="#566573",
                                                text_font=("Arial", fontSize),
                                                text=text,
                                                text_color="white",
                                                corner_radius=0,
                                                border_width=2,
                                                width=width,
                                                height=height,
                                                hover=True,
                                                command=callback)
        button.place(relx=relX, rely=relY, anchor=anchor)
        return button

    def createScalebar(self, relX, relY, text, orientation, from_, to, length, defaultValue=None, tickInterval=10, callback=None, resolution=1, fontSize=13, anchor=NW):
        """
        Créer une scale bar
        """
        if defaultValue == None:
            defaultValue = from_
        scalebar = Scale(self.master, orient=orientation, from_=from_, to=to, resolution=resolution, tickinterval=tickInterval, length=length, label=text, bg='#1E1E1E', fg='#ABB2B9', font=("Arial", fontSize))
        if callback != None:
            scalebar.bind("<ButtonRelease-1>", callback)
        scalebar.set(defaultValue)
        scalebar.place(relx=relX, rely=relY, anchor=anchor)
        return scalebar

    def createCheckBox(self, relX, relY, text, checked, fontSize=15, anchor=NW, callback=None):
        """
        Créer des check box
        """
        checkedValue = IntVar(value=int(checked))
        checkBox = Checkbutton(self.master, text=text, variable=checkedValue, command=callback, bg='#1E1E1E', fg='#ABB2B9', selectcolor="#1E1E1E", activebackground="#161616", activeforeground="#ABB2B9")
        checkBox.configure(font=("Arial", fontSize))
        checkBox.place(relx=relX, rely=relY, anchor=anchor)
        return checkedValue

    def createComboBox(self, relX, relY, list, fontSize=15, callback=None):
        """
        Créer une combo box
        """
        comboBox = Combobox(self.master, values=list)
        comboBox.configure(font=("Arial", fontSize))
        comboBox.place(relx=relX, rely=relY)

        if (callback != None):
            comboBox.bind("<<ComboboxSelected>>", callback)

        return comboBox

    def createFrame(self, relX, relY, width, height):
        """
        Créer une sous frame
        """
        frame = Frame(self.master, width=width, height=height, bg='#1E1E1E')
        frame.place(relx=relX, rely=relY)
        return frame

    def enableCanvas(self):
        """
        Active un canvas (nécéssaire pour le dessin ou
        pour mettre une image de fond)
        """
        self.canvas =  Canvas(self.master, width=self.dimX, height=self.dimY)
        self.canvas.pack()

    def setBackgroundImage(self, path, resize=None):
        """
        Met une image de fond
        """
        if self.canvas == None:
            print("Need to enable canvas")
            return

        image = Image.open(path)
        if resize != None:
            image = image.resize((resize[0], resize[1]), Image.ANTIALIAS)

        self.backgroundImage = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.backgroundImage)

    def drawCircle(self, x, y, r):
        """
        Dessine un cercle
        """
        if self.canvas == None:
            print("Need to enable canvas")
            return None
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='white')

    def deleteForm(self, form):
        """
        Détruit une form grâce à son ID
        """
        self.canvas.delete(form)

    def scheduleTask(self, time, task):
        """
        Permet d'executer une fonction après un délai
        """
        self.master.after(time, task)

    def loop(self):
        """
        Maintien en vie l'interface
        """
        self.master.mainloop()

    def close(self):
        """
        Ferme l'interface
        """
        self.closingCallbackEvent()

    def throwMessage(self, message, title="Message", afterReadCallback=None):
        """
        Envoie un message à l'utilisateur
        """
        from frame.errorFrame import ErrorFrame
        ErrorFrame(Toplevel(self.master), message, title=title, nextStep=afterReadCallback)
