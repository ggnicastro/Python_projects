__author__ = 'kaihami'
import os

os.chdir('/home/kaihami/Desktop/Python/Captcha_images/Test_data/')

for x in xrange(2000,3250):
    with open("info.txt","a") as f:
        f.write("bw_captcha"+str(x)+".png.png")
        f.write("\n")
fi = open("info.txt","r").read().split("\n")

del fi[-1]

for f in fi:
    img = "/home/kaihami/Desktop/Python/Captcha_images/Test_data/BW/"+f
    img_name = str(f)
    os.system("tesseract "+img +" out")
    out_old = open("out.txt","r").readline().rstrip()
    os.system("tesseract "+img +" out2 -l captcha")
    out_new = open("out2.txt","r").readline().rstrip()
    with open("infos.txt","a") as f:
        l = [img_name, out_old, out_new]
        f.write("\t".join(l))
        f.write("\n")