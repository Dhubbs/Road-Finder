
from classify import *
import time
import random 
from PIL import Image
#Dylan Hubble
#looks at satelitle images and tries to classify Roads and houses in the pictures


#creats an array of colors that are and are not colors of roads and roofs
colors = [[0,0,0,1],[100,100,100,1],[250,250,250,1]]
for i in range(40):
    a = random.randint(0,250)
    b = random.randint(0,250)
    c = random.randint(0,250)
    if a>160 and a<205:
        a = random.randint(0,180)
    if b>160 and b<205:
        b = random.randint(0,180)
    if c>160 and c<205:
        c = random.randint(0,180)
    colors.append([a,b,c,1])

for i in range(100):
    a = random.randint(140,190)
    b = random.randint(140,195)
    c = random.randint(140,195)
    colors.append([a,b,c,0])

#opens the image of the satelite image
img = Image.open('C:\Users\Dylan\Pictures\\1.jpg')

#creates a empty image array the same size as the one we opened
img2 = Image.new('RGB',(img.size[0],img.size[1]))
pixels = img2.load()

#loops through all of the pixels in the images
for i in range(3,img.size[0]-3):
    for j in range(3,img.size[1]-3):
        current = img.getpixel((i,j))
        
        #classifys whether this pixel color falls under the category of being a house or road or not
        if classify(colors,[current[0],current[1],current[2]]) == 0:
            pixels[i,j] = (250,0,0)
        else:
            pixels[i,j] = (current[0],current[1],current[2])
            
    #displays how long through processing the image we are
    print str(i) + " of " + str(img.size[0])

img2.show()

