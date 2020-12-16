from sklearn.cluster import KMeans
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
import random
import huffman as hman
class K_compress:
    def __init__(self, filename=None):
        self.filename = filename
        self.img = None
        self.pix = None
        self.data = []
        self.size = None
        self.newData = []
        self.counter = {}
        self.compressed = None

    def changeImgen(self, filename):
        self.filename = filename

    def getImagen(self):
        try:
            if self.filename.split(".")[-1] == "png":
                self.img = Image.open("img/original/"+self.filename)
                self.pix = self.img.load()
            else:
                print("Not PNG")
        except:
            print("Error getting imagen")
        
    def setSize(self):
        self.size = self.img.size

    def extractData(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.data.append(list(self.pix[x,y]))

        
    def compress(self, cluster=16):  
        self.getImagen()
        self.setSize()
        self.extractData()  
        kmean = KMeans(n_clusters=cluster)
        kmean.fit(self.data)
        center, point = [cent for cent in kmean.cluster_centers_.astype(int)], 0
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                new_color = center[kmean.labels_[point]]
                new_color = tuple(new_color.tolist())
                self.pix[x,y] = new_color
                point+=1
                self.newData.append(new_color)
                key = str(list(new_color))
        newName = self.filename.split(".")[0]+"["+str(cluster)+"_colors]"
        self.img.save("img/compressed/"+newName+".png")
        print("Saved at img/compressed/"+newName+".png")

for i in range(117,128):
    print(i)
    r = K_compress(filename = "king.png")
    r.compress(cluster=i)