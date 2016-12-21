__author__ = 'kaihami'
"""
Generate .box file for tesseract training
use cropped images from Transform_captcha.py
TODO

"""

import os
import shutil
current_dir = '/home/kaihami/Desktop/Python/Captcha_images/Training_data/Black_White/'
not_dir = ["0_250","251_500","501_750",
           "751_1000","1001_1250","1251_1500",
           "1501_1750","1751_2000","No_size","Sub_train"]
list_dir = os.listdir(current_dir)
for dir_name in list_dir:
    if dir_name not in not_dir:
        local_dir = current_dir+dir_name+"/"
        for image in os.listdir(local_dir):
            if image.endswith(".png"):
                image_path = local_dir+image
                image_name = image.replace(".png","")
                image_to_save = local_dir+image_name
                os.system("tesseract "+image_path + " " + image_to_save + " batch.nochop makebox")
print "Finish"

current_dir = '/home/kaihami/Desktop/Python/Captcha_images/Training_data/Black_White/'
list_dir = os.listdir(current_dir)
for dir_name in list_dir:
    local_dir = current_dir+dir_name+"/"
    for box in os.listdir(local_dir):
        if box.endswith(".box"):
            box_path = local_dir+box
            file_size = os.path.getsize(box_path)
            if file_size == 0:
                move_to = '/home/kaihami/Desktop/Python/Captcha_images/Training_data/Black_White/No_size/'+box
                shutil.move(box_path, move_to)
                #also move png
                png = box.replace(".box",".png")
                png_path = local_dir+png
                move_png = '/home/kaihami/Desktop/Python/Captcha_images/Training_data/Black_White/No_size/'+png
                shutil.move(png_path, move_png)
                print "*"*50
                print move_to
                print move_png

print "Finish"


##### Train data

dir_a = '/home/kaihami/Desktop/Python/Captcha_images/Training_data/Sub_train/'
for fi in os.listdir(dir_a):
    if fi.endswith(".png"):
        rename = fi.replace(".png","")
        path_name = dir_a+fi
        path_name2= dir_a +rename
        os.system("tesseract "+path_name+ " "+ path_name2+" nobatch box.train")
        print path_name
print "Finish"

#unichar
os.chdir('/home/kaihami/Desktop/Python/Captcha_images/Training_data/Sub_train/')
os.system("unicharset_extractor captcha.training_font.exp*.box")
os.system('echo "training_font 0 0 0 0 0" > font_properties')
os.system('shapeclustering -F font_properties -U unicharset captcha.training_font.exp*.tr')
os.system('mftraining -F font_properties -U unicharset -O captcha.unicharset captcha.training_font.exp*.tr')
os.system('cntraining captcha.training_font.exp*.tr')

os.system('mv inttemp captcha.inttemp')
os.system('mv normproto captcha.normproto')
os.system('mv pffmtable captcha.pffmtable')
os.system('mv shapetable captcha.shapetable')
os.system('combine_tessdata captcha.')

#sudo cp eng2.traineddata /usr/local/share/tessdata/