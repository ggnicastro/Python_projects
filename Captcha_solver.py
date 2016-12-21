__author__ = 'kaihami'
import pytesseract
import cv2
import Image

from skimage.color import rgb2hed
from skimage.exposure import rescale_intensity
from skimage.filters import threshold_otsu
from skimage.feature import local_binary_pattern
from scipy.stats import itemfreq
import numpy as np
from matplotlib import pyplot as plt
from pytesser import *

#imagem
img = Image.open('/home/kaihami/Desktop/captcha2.png')

#convert to RGB
img = img.convert('RGBA')

pixdata = img.load()

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x,y] != (255,255,255,255):
            pixdata[x,y] = (0,0,1,255)

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x,y] == (255,255,255,255):
            pixdata[x,y] = (0,0,0,255)
        if pixdata[x,y] ==(0,0,1,255):
            pixdata[x,y] = (255,255,255,255)
img.save('black4.png','PNG')

#aumentar imagem
im = Image.open("/home/kaihami/Desktop/Python/black4.png")
nx, ny = im.size
im2 = im.resize((int(nx*4), int(ny*4)), Image.BICUBIC)
im2.save("final_pic_test.png")

img_g = cv2.imread("final_pic_test.png", 0)

global_thresh = threshold_otsu(img_g)
binary_global_dab = img_g > global_thresh
plt.imshow(binary_global_dab, 'gray')

my_array = binary_global_dab.astype('uint8')*255

im = Image.fromarray(my_array)
im.save("Binary_g_test2.tif")

#   Yeah! Fazemos OCR da imagem usando o Pytesser

####
img = cv2.medianBlur(img_g,9)
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(th2, 'gray')
cv2.imwrite('otsu.tif', th2)

image_cont2 = cv2.imread('/home/kaihami/Desktop/Python/otsu.tif', 0)
ret,thresh = cv2.threshold(image_cont2,127,255,0)

contours2, hierarchy2 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
plt.imshow(image_cont2)

cv2.drawContours(image_cont2, contours2, -1, (0,0,0), 3)
plt.imshow(image_cont2)
cv2.imwrite('try_try2.tif',image_cont2)

image = Image.open('/home/kaihami/Desktop/Python/try_try2.tif')
print image_to_string(image)
