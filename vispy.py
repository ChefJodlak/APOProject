#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Generates 3D Histogram of Wallaby image and renders to screen using vispy
Requires:
vispy
scipy
numpy
Related URLs:
http://vispy.org/installation.html
https://github.com/vispy/vispy/blob/master/examples/basics/scene/volume.py
http://api.vispy.org/en/latest/scene.html#vispy.scene.visuals.Volume
'''

from urllib.request import urlopen

import numpy as np
from imageio import imread


import vispy
from vispy.io import load_data_file, read_png

# Create the all zero 3D Histogram we will use to store the color information
tristogram = np.zeros((256,256,256), dtype=np.uint8)


url = "https://raw.githubusercontent.com/desertpy/presentations/master/exploring-numpy-godber/wallaby_746_600x450.jpg"
with urlopen(url) as file:
    img = imread(file, mode='RGB')

for h in range(600):
    for w in range(450):
        (r, g, b) = img[h, w, :]
        tristogram[r, g, b] += 1

canvas = vispy.scene.SceneCanvas(show=True)
view = canvas.central_widget.add_view()
volume = vispy.scene.visuals.Volume(tristogram, parent=view.scene, emulate_texture=False)
view.camera = vispy.scene.cameras.TurntableCamera(parent=view.scene)


if __name__ == '__main__':
    app.run()