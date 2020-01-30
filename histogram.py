# importing required libraries of opencv
import cv2
# importing library for plotting
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cv2
from tkinter import messagebox

class Histogram:
    def __init__(self, root):
        self.root = root

    def histogram2d(self, img):
        try:
            self.img_cv = img
            channels = cv2.split(self.img_cv)
            colors = ("b", "g", "r")

            # create the histogram plot, with three lines, one for
            # each color
            for (channel, c) in zip(channels, colors):
                histr = np.zeros(shape=(256))
                h = self.img_cv.shape[0]
                w = self.img_cv.shape[1]

                # loop over the image, pixel by pixel
                for y in range(0, h):
                    for x in range(0, w):
                        histr[channel[y, x]] += 1

                plt.bar(np.arange(256), histr, color=c, alpha=0.3)

            plt.xlim([0, 256])
            plt.xlabel("Color value")
            plt.ylabel("Pixels")
            plt.show()
        except:
            self.displayerror()


    def histogram3d(self, img, type):
        try:
            if type == 'color':
                self.histogram3dcolor(img)
            else:
                self.histogram3dmono(img)
        except:
            self.displayerror()

    def histogram3dcolor(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        fig = plt.figure()

        ax = fig.add_subplot(111, projection='3d')
        for x, c, z in zip([h, s, v], ['r', 'g', 'b'], [30, 20, 10]):
            xs = np.arange(256)
            ys = cv2.calcHist([x], [0], None, [256], [0, 256])
            cs = [c] * len(xs)
            cs[0] = 'c'

            ax.bar(xs, ys.ravel(), zs=z, zdir='y', color=cs, alpha=0.8)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    def histogram3dmono(self, img):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        xs = np.arange(256)
        ys = cv2.calcHist([img], [0], None, [256], [0, 256])
        cs = '#ff8080'

        ax.bar(xs, ys.ravel(), zs=5, zdir='y', color=cs, alpha=0.8)

        ax.set_xlabel('Pixels')
        ax.set_ylabel('')
        ax.set_zlabel('Color value')
        plt.show()

    def displayerror(self):
        messagebox.showerror("Error", "Please open image first")