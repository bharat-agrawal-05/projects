from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})


# install pillow using:
# pip3 install pillow
# if above does not work and you are on windows, try:-
# py -m pip3 install pillow

# importing Image and ImageOps from PIL
from PIL import Image, ImageOps

# creating image object:
imInp = Image.open('problem1cInput.jpg')

# converting imInp to grayscale:
imGrayscale = ImageOps.grayscale(imInp)

# converting image to numpy array
import numpy as np
pixels2D = np.array(imGrayscale,dtype='int')
print(pixels2D.shape)

# showing/saving image
# imGrayscale.show()
# imGrayscale.save('problem1cOutput.jpg')

# Write code for finding histogram here:

# Write code for finding histogram of difference of pixel's intensity
# with its left neighbour here:
pixelflat=pixels2D.flatten()
plt.hist(pixelflat)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.title('histogram of pixel intensity')
plt.savefig('problem1ci.png')
plt.show()

data=[]
for row in pixels2D:
    for i in range(len(row)):
        if i>0:
            data.append(row[i]-row[i-1])
        else:
            data.append(row[0])

x=[i for i in range(min(data),max(data)+1,16)]


plt.hist(data,bins=32)
plt.title('histogram of difference of pixel intensity with its left neighbour')
plt.xticks(x,fontsize=8,rotation=90)
plt.yticks(fontsize=10)
plt.savefig('problem1cii.png')
plt.show()




