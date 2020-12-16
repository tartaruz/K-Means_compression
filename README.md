### Installation

Use  [pip](https://pip.pypa.io/en/stable/) to install needed libraries.

```bash
pip install numpy matplotlib Pillow
```
Python3+ is needed

### Usage

After running the file "k-compress.py", the porgram will need to know the name of the file and the k-value/number of colors needed.

```bash
Filename: king.png
K_value: 2
```
! PS: The imagen must be in the folder img/original AND be in the format PNG !

# **Compression with K-mean clustering**

>Imagenes contains building-block known as pixels. A pixel is an entity that has three values; **R**ed, **G**reen and **B**lue. Each value of **RGB** ranges from 0-255 going from not containing any of the colours or containing maximum(255). In other words, a green, a white and a magenta pixel has the values in respective order; 

- Green = rgb(0, 255, 0) 
- White = rgb(255, 255, 255)
- Magenta = rgb(255, 0, 255)

####*The method*
The main algorithms making all the magic happening is the k-means clustering [https://en.wikipedia.org/wiki/K-means_clustering]. 

As previously explained, the pixel contains three values. The three values can be used as axes creating a three-dimensional plane. Every pixel in the imagen is inserted in the plane, giving it a position using its RGB values. 
The usage of the algorithm is to find clusterings of a set of, in this case, points. The algorithm needs a K-values indicating how many clusters that are wanted. In this context, the founded points after running the algorithm, are also a pixel with RGB values. Therefore, the k value in this context will be the number of wanted colours for the output imagen. Now we have K-points for all the pixels of the imagen.

The imagen can now be recreated by assigning every pixel the same values as the pixel's belonging clustering value. 


####*Compression*
Initially, the idea was to use Huffman-code to create an image, but as I found out, the PNG format already has a form of compression[https://en.wikipedia.org/wiki/Portable_Network_Graphics#Compression].


####*Example*
As the example imagen called "king.png" in the folder "img/original" of the Norwegian King Harald V, the original imagen has the size of 1 001 305 bytes.
After converting it only to contain two colours, the size changed to 25 524 bytes and reduced in size by 97.46 %

| **K (colours)**  | 2  |  4 | 8  | 16  | 32  | 64  | 128  | 256  |
|---|---|---|---|---|---|---|---|---|
|  **Size(bytes)** | 25 524  | 52 090 | 148 847  | 209 680  |  360 498 | 509 475  |  701 327 |  900 328 |
|  **Reduction** | 97.46%  | 94.80%  | 85.13%  | 79.05%  |  64% | 49.12%  |  29.95% |  10.08% |


Here are the corresponding images. The K number increases to the power of 2, and correspond to the number of different colours.
![Kings](https://github.com/tartaruz/K_compress/blob/master/img/banner/output_2-4-8-16-32.png)
