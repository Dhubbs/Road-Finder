
from PIL import Image
#from sklearn import svm
import random



from sklearn.neighbors import KNeighborsClassifier

#opens the image
img = Image.open("base.png") 



coord = [[505,290],[450,400],[333,604],[720,533],[1440,700],[1200,200],[1470,300],[950,910],[400,720],[990,117],[570,350],[500,415],[1250,700],[1200,780],[1160,850],[730,950],[90,877],[1745,608],[1355,70],[450,70]]

x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y = [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]

for i in range(len(coord)):
	print str(coord[i][0]) + "   " + str(coord[i][1])
	x[i] = img.getpixel((coord[i][0],coord[i][1]-5)) + img.getpixel((coord[i][0],coord[i][1]+5)) + img.getpixel((coord[i][0]-5,coord[i][1])) + img.getpixel((coord[i][0]+5,coord[i][1]))
	x[i] = list(x[i])
print x

imgout = Image.new( 'RGB', (img.size[0]+10,img.size[1]+10), "black") # create a new black image
pixels = imgout.load() # create the pixel map


clf = KNeighborsClassifier(n_neighbors=1)
clf.fit(x, y)

#for every pixel in the image
for i in range(img.size[0]-6):
	for j in range(img.size[1]-6):
		temp = [list(img.getpixel((i+6,j+6)) + img.getpixel((i+6,j+6)) + img.getpixel((i+6,j+6)) + img.getpixel((i+6,j+6)))]
		
		a = clf.predict(temp)

		if a == 1:
			pixels[i,j] = (255,0,0)
		else:
			pixels[i,j] = img.getpixel((i,j))
	print str(i) + " of " + str(img.size[0])
imgout.save("done.png")
#todo run test.py on this so that we can remove the outlying pixels