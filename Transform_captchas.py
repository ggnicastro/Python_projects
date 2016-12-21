__author__ = 'kaihami'
"""
From a captcha.png file transform it in a binary image (black and white) almost 90% ok
Open .png in openCV2, inverted binary threshold, crop and save image

"""

#OK!
import os
import cv2


current_dir = '/home/kaihami/Desktop/Python/Captcha_images/Test_data/2000_2250/'
n_dir = "/home/kaihami/Desktop/Python/Captcha_images/Test_data/"
x = 0
for image in os.listdir(current_dir):
    if image.endswith(".png"):
        image_name = image

        img = cv2.imread(current_dir+image,0)
        img_original = cv2.imread(current_dir+image,0)
        ret,thresh = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
        save_image_path = n_dir+image
        mid = (len(thresh[0])/2)
        img_crop = thresh[:,28:mid+12]
        cv2.imwrite(save_image_path, img_crop)
        x+=1
        print "*"*50
        print save_image_path
        print "*"*50
        print "LEFT:", str(2000-x)
print "Finish"

