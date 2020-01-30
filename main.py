import tkinter
from tkinter import filedialog
from histogram import Histogram
import cv2
from PIL import ImageTk, Image

class APO:
    def __init__(self):
        self.root = tkinter.Tk()
        self.histogram = Histogram(self.root)
        self.img_cv = None
        self.image = None
        self.imageType = None
        self.initializeui()

    def initializeui(self):
        self.root.configure(background='grey')

        #Set GUI
        self.root.title("APO PROJEKT - RAFAŁ JODEŁKA")  # title of the GUI window
        self.root.maxsize(1200, 800)  # specify the max size the window can expand to
        self.left_frame = tkinter.Frame(self.root, width=100, height=400, bg='grey')
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.center = tkinter.Frame(self.root, width=800, height=400, bg='grey')
        self.center.grid(row=0, column=1, padx=10, pady=5)
        self.right_frame = tkinter.Frame(self.root, width=800, height=400, bg='grey')
        self.right_frame.grid(row=0, column=2, padx=10, pady=5)
        self.image = Image.open('bg.png')
        self.image = ImageTk.PhotoImage(self.image)
        self.showimage = tkinter.Label(self.center, image=self.image).grid(row=0, column=0, padx=5, pady=5)

        self.tool_bar = tkinter.Frame(self.left_frame, width=180, height=400, bg='grey')
        self.tool_bar.grid(row=0, column=0, padx=5, pady=5)
        tkinter.Button(self.tool_bar, text="Open Mono", command=self.load_mono, bg='grey', highlightbackground='#3E4149').pack()
        tkinter.Button(self.tool_bar, text="Open Color", command=self.load_color, bg='grey',highlightbackground='#3E4149').pack()

        hist = tkinter.Frame(self.right_frame, width=180, height=400)
        hist.grid(row=0, column=0, padx=5, pady=5)
        tkinter.Button(hist, text="Histogram 2D", command=lambda: self.histogram.histogram2d(self.img_cv),
                       highlightbackground='#3E4149').pack()
        tkinter.Button(hist, text="Histogram 3D", command=lambda: self.histogram.histogram3d(self.img_cv, self.imageType),
                       highlightbackground='#3E4149').pack()
        self.root.mainloop()

    def load_mono(self):
        """Load image as greyscale"""
        self.openimage()
        if self.root.filename is None:
            return

        self.img_cv = cv2.imread(self.root.filename, cv2.IMREAD_GRAYSCALE)
        self.setimage()
        self.imageType = 'mono'

    def load_color(self):
        """Load Color image"""
        self.openimage()
        if self.root.filename is None:
            return

        self.img_cv = cv2.imread(self.root.filename)
        self.setimage()
        self.imageType = 'color'

    def openimage(self):
        """Open image path"""
        self.root.filename = filedialog.askopenfilename(initialdir="./", title="Select file", filetypes=(
            ("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))

    def setimage(self):
        """Display image on UI"""
        image = cv2.cvtColor(self.img_cv, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image.thumbnail((800, 600))
        self.image = ImageTk.PhotoImage(image=image)
        self.showimage = tkinter.Label(self.center, image=self.image).grid(row=0, column=0, padx=5, pady=5)

apo = APO()