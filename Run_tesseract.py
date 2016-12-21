__author__ = 'kaihami'
import os

inp = "/home/kaihami/Desktop/Python/Captcha_images/Test_data/"
os.chdir(inp)
for png in os.listdir(inp):
    if png.endswith(".png"):
        os.system("tesseract " + png +" output -l captcha")
        output = open("output.txt", "r").read().replace("\n", "")
        with open("Test_trained.txt", "a") as f:
            f.write(png+"\t")
            f.write(output)
            f.write("\n")
print "Finish"
#tesseract input_file.tif output -l tla


