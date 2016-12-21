__author__ = 'kaihami'
import os
dir_test = "/home/kaihami/Desktop/Python/Captcha_images/Test_data/"

for x in xrange(2000,3251):
    c = "captcha"+str(x)+".png"
    with open(dir_test+"Expected_results.txt", "a") as f:
        f.write(c+"\t")
        f.write("\n")
