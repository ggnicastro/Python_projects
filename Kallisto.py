__author__ = 'kaihami'
import os

dir = "/home/kaihami/kallisto/build/src/"
a = os.listdir(dir)
files = []

for File in a:
    if File.endswith(".fastq"):
        files.append(File)

files.sort()
def kalisto(r1, r2, o):
    os.system("./kallisto quant -i transcripts.idx -o " + o + " -b 100 " + r1 + " " + r2)

for x in xrange(0, len(files),2):
    type(files[x])
    b = files[x].split("_")
    sample_name = b[1]
    kalisto(files[x],files[x+1], sample_name)




