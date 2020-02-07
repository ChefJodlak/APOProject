import tkinter
from tkinter import filedialog
from histogram import Histogram
import cv2
from PIL import ImageTk, Image

class APO:
    """Main class"""
    def __init__(self):
        """
        Initialization
        @:param None
        """
        self.root = tkinter.Tk() # Inicjalizacja Tkinter
        self.histogram = Histogram(self, self.root) # nowa instancja klasy histogram
        self.img_cv = '' # ścieżka do obrazu openCV
        self.cleanimage = ''# ścieżka do nieedytowanego obrazu openCV
        self.image = None # ścieżka do obrazu
        self.imageType = None # typ obrazu
        self.initializeui() # Inicjalizacja GUI

    def initializeui(self):
        """
        Initialize UI using TKinter
        @:param None
        """
        self.root.configure(background='grey') # Ustawienie tła na kolor szary

        #Set GUI
        self.root.title("APO PROJEKT - RAFAŁ JODEŁKA")  # Tytuł okna
        self.root.maxsize(1200, 800)  # Maksymalna wielkość okna
        self.left_frame = tkinter.Frame(self.root, width=100, height=400, bg='grey') # UI
        self.left_frame.grid(row=0, column=0, padx=10, pady=5) # UI
        self.center = tkinter.Frame(self.root, width=800, height=400, bg='grey') # UI
        self.center.grid(row=0, column=1, padx=10, pady=5) # UI
        self.right_frame = tkinter.Frame(self.root, width=800, height=400, bg='grey') # UI
        self.right_frame.grid(row=0, column=2, padx=10, pady=5) # UI
        self.image = Image.open('bg.png') # Pierwszy obraz
        self.image = ImageTk.PhotoImage(self.image) # Pierwszy obraz
        self.showimage = tkinter.Label(self.center, image=self.image).grid(row=0, column=0, padx=5, pady=5) # Pierwszy obraz

        self.tool_bar = tkinter.Frame(self.left_frame, width=180, height=400, bg='grey') # Przyciski z lewej strony
        self.tool_bar.grid(row=0, column=0, padx=5, pady=5) # Przyciski z lewej strony
        tkinter.Button(self.tool_bar, text="Open Color", command=self.load_color, bg='grey',highlightbackground='#3E4149').pack() # Przyciski z lewej strony

        hist = tkinter.Frame(self.right_frame, width=180, height=400, bg='grey') # Przyciski z prawej strony
        hist.grid(row=0, column=0, padx=5, pady=5) # Przyciski z prawej strony
        tkinter.Button(hist, text="Histogram 2D(Clean)", command=lambda: self.histogram.histogram2d(self.cleanimage),
                       highlightbackground='#3E4149').pack() # Przyciski z prawej strony
        tkinter.Button(hist, text="Histogram 3D(Clean)", command=lambda: self.histogram.generatehistogram3d(self.cleanimage),
                       highlightbackground='#3E4149').pack() # Przyciski z prawej strony
        tkinter.Button(hist, text="Histogram 2D(After Operations)", command=lambda: self.histogram.display2doperations(self.img_cv),
                       highlightbackground='#3E4149').pack()  # Przyciski z prawej strony
        tkinter.Button(hist, text="Histogram 3D(After Operations)",
                       command=lambda: self.histogram.display3doperations(self.img_cv),
                       highlightbackground='#3E4149').pack()  # Przyciski z prawej strony

        self.root.mainloop() # Nie wyłączaj UI

    def load_color(self):
        """
        Load Color image
        @:param None
        """
        self.openimage() # Otwórz obraz
        if self.root.filename is None: # Jeśli ścieżka jest none wtedy nie rób nic
            return

        self.img_cv = cv2.imread(self.root.filename) # Odczytaj obraz
        self.cleanimage = self.img_cv # Przypisz wartość do cleanimage
        self.setimage() # Ustaw obraz

    def openimage(self):
        """
        Open image path
        @:param None
        """
        self.root.filename = filedialog.askopenfilename(initialdir="./", title="Select file", filetypes=(
            ("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*"))) # wybierz ścieżkę do obrazu

    def setimage(self):
        """
        Display image on UI
        @:param None
        """
        image = cv2.cvtColor(self.img_cv, cv2.COLOR_BGR2RGB) # Ustaw odpowiednie kolory
        image = Image.fromarray(image) # Pobierz obraz
        image.thumbnail((800, 600)) # Ustaw wielkość obrazu
        self.image = ImageTk.PhotoImage(image=image) # Wyświetlenie obrazu
        self.showimage = tkinter.Label(self.center, image=self.image).grid(row=0, column=0, padx=5, pady=5) # Wyświetlenie obrazu

    def setimgcv(self, img):
        """
        Set img_cv value
        @:param img opencv2 image array value
        """
        self.img_cv = img
apo = APO()