# importing library for plotting
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cv2
from tkinter import messagebox

class Histogram:
    """Class for histogram"""
    def __init__(self, main, root):
        """
        Initialization
        @:param root root ui
        """
        self.main = main # Ustawienie głównej klasy
        self.root = root # Ustawienie głównej klasy

    def histogram2d(self, img):
        """
        Generate histogram 2d using cv2 function
        @:param img: CV2 image
        """
        try:
            plt.close("all")
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Ustawienie kolorów RGB
            hist = cv2.calcHist([rgb], [0, 1], None, [256, 256], [0, 256, 0, 256]) # Obliczenie histogramu

            p = plt.imshow(hist, interpolation='nearest') # Stworzenie histogramu, interpolacja ustawiona na najbliższe
            plt.colorbar(p) # Dodanie przedziału kolorów
            plt.show() # Wyświetl histogram
        except:
            self.displayerror() # Wyświetl błąd


    def histogram3d(self, h, e, fig=None):
        """
        Visualize a 3D histogram

        @:param h: histogram array of shape (M,N,O)
        @:param e: list of bin edge arrays (for R, G and B)
        """
        plt.close("all")
        M, N, O = h.shape # Kształty
        idxR = np.arange(M)
        idxG = np.arange(N)
        idxB = np.arange(O)

        #Generowanie okręgów dla każdego z kolorów R G B
        R, G, B = np.meshgrid(idxR, idxG, idxB)
        a = np.diff(e[0])[0]
        b = a / 2
        R = a * R + b

        a = np.diff(e[1])[0]
        b = a / 2
        G = a * G + b

        a = np.diff(e[2])[0]
        b = a / 2
        B = a * B + b

        colors = np.vstack((R.flatten(), G.flatten(), B.flatten())).T / 255 # Kolory
        h = h / np.sum(h)
        if fig is not None: # Stworzenie Figury
            f = plt.figure(fig)
        else:
            f = plt.gcf()
        ax = f.add_subplot(111, projection='3d') # Stworzenie 3D projekcji
        mxbins = np.array([M, N, O]).max() # Maksymalne wartości
        ax.scatter(R.flatten(), G.flatten(), B.flatten(), s=h.flatten() * (256 / mxbins) ** 3 / 2, c=colors) # Kolory

        ax.set_xlabel('Red') # Label dla Red
        ax.set_ylabel('Green') # Label dla Green
        ax.set_zlabel('Blue') # Label dla Blue

    def generatehistogram3d(self, img):
        """
        Generate histogram 3d using cv2 function
        @:param img: CV2 image
        """
        if img != '':
            h, e = np.histogramdd(img.reshape(-1, 3), bins=8) # Wartości dla histogramu
            self.histogram3d(h, e) # Wygeneruj Histogram 3D
            plt.show() # Wyświetl histogram 3D
        else:
            self.displayerror()  # Wyświetl błąd

    def display3doperations(self, img):
        """
        Display histogram 3d for Image where operations were used
        @:param img: CV2 image
        """
        if img != '':
            image = self.tweakimage3d(img) # Użyj Dylatacji i Laplacian na obrazie
            self.generatehistogram3d(image) # Wygeneruj histogram 3d
        else:
            self.displayerror()  # Wyświetl błąd

    def display2doperations(self, img):
        """
        Display histogram 2d for Image where operations were used
        @:param img: CV2 image
        """
        if img != '':
            image = self.tweakimage2d(img) # Użyj Dylatacji na obrazie
            self.histogram2d(image) # Wygeneruj histogram 2d
        else:
            self.displayerror()  # Wyświetl błąd
    def displayerror(self):
        """
        Display error message
        @:param None
        """
        messagebox.showerror("Error", "Please open image first") # Wyświetl błąd

    def dilate(self, img):
        """
        Use Dilate function on Image
        @:param img: CV2 image
        """
        tab = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3)) # Generowanie MORPH_CROSS
        img2 = cv2.dilate(img, tab, iterations=1) # Use Dilate function on image

        cv2.namedWindow(winname="Dilate", flags=cv2.WINDOW_NORMAL) # Set Window title
        cv2.imshow(winname="Dilate", mat=img2) # Display Dilate image
        return img2 # Return Dilate result

    def laplacian(self, img):
        """
        Use Laplacian function on Image
        @:param img: CV2 image
        """
        tab = np.array((
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]), dtype="int") # set tab
        imgl = cv2.filter2D(img, -1, tab) # Use Laplacian function with the provided tab
        self.main.setimgcv(imgl) # Set variable in main Class
        self.main.setimage() # Set image on UI

        return imgl # Return Laplacian result


    def tweakimage3d(self, img):
        """
        Use Dilate and then Laplacian function on Image
        @:param img: CV2 image
        @:return image: Image on which Dilate and Laplacian function were used
        """
        img2 = self.dilate(img) # Dilate
        image = self.laplacian(img2) # Laplacian
        return image # Return Dilate and Laplacian result

    def tweakimage2d(self, img):
        """
        Use Dilate function on Image
        @:param img: CV2 image
        @:return image: Image on which Dilate function were used
        """
        image = self.dilate(img) # Dilate
        return image # Return Dilate result