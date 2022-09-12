import PIL #install with "pip install pillow", verify with "python3 -m PIL"
from PIL import Image,ImageFilter #Image class used for all images
import os, sys
import numpy as np
import matplotlib.pyplot as plt


#image_name = input("Enter the name of the image file.")
image_name = "test.jpg"
filepath = os.path.join(os.getcwd(),image_name)
try:
    im = Image.open(filepath)
    print(f"Image - {filepath}")
    print(f"Format - {im.format}")
    print(f"Size - {im.size} - {im.width} x {im.height}")
    print(f"Mode - {im.mode}")
    print(f"Bands - {im.getbands()}")
    print(f"Bounds - {im.getbbox()}")
    print(im)
    print(np.asarray(im))
    print(Image.fromarray(np.asarray(im)))
except OSError:
    print(f"Unable to open image {filepath}.")
    im = Image.new(mode="RGB",size=(400,300),color=(120,233,122))

imlow = im.copy()
imlow.thumbnail((64,64))

fig,axs = plt.subplots(3,3)
for ax in axs.flat:
    ax.xaxis.tick_top()
    ax.invert_yaxis()



axs[0,0].imshow(im) #original image
axs[0,1].imshow(im.rotate(90)) #rotated image
axs[0,2].imshow(im.resize((128,128))) #resized image
axs[1,0].imshow(im.crop((100,100,300,300))) #cropped image
axs[1,1].imshow(im.convert("L")) #
axs[1,2].imshow(im.getchannel("B")) #extract blue channel
axs[2,0].imshow(im.transpose(Image.Transpose.FLIP_LEFT_RIGHT))
axs[2,1].imshow(imlow.resize((1024,1024),resample = Image.Resampling.BICUBIC))
axs[2,2].imshow(imlow.filter(ImageFilter.EDGE_ENHANCE_MORE))

plt.show()

im.save("result.png",optimize=True,quality=70)
im.rotate(45,fillcolor=(123,212,42)).save("rotato.tiff")
imsplit = im.split()
for i in range(len(imsplit)):
    imsplit[i].save(f"channel{i}.jpg")



