from sklearn.cluster import KMeans
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
from PIL import Image
import plot 
from mpl_toolkits.mplot3d import Axes3D
import random

im = Image.open('img/unknown.png') # Can be many different formats.
pix = im.load()
data = []
size = im.size
for x in range(size[0]):
    for y in range(size[1]):
        r = (pix[x,y][0], pix[x,y][1],pix[x,y][2],255)
        data.append(list(pix[x,y]))


kmean = KMeans(n_clusters=16)
kmean.fit(data)
center = [cent for cent in kmean.cluster_centers_.astype(int)]

nr=0
for x in range(size[0]):
    for y in range(size[1]):
        d = center[kmean.labels_[nr]]
        d = d.tolist()
        d = tuple(d)
        pix[x,y] = d
        nr+=1
im.save('img/unknown_komp.png')  # Save the modified pixels as .png
