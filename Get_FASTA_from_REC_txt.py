__author__ = 'kaihami'
"""
Take the REC_Final_by_domain and output a fasta file with a >Locus and the sequence \n\n
"""
import os
dir = "/home/kaihami/Desktop/RR_files/Final_NarL/"
dir2 = "/home/kaihami/Desktop/RR_files/Final_NarL/"
REC_file_lst = []

for File in os.listdir(dir):
    if File.endswith(".txt"):
        REC_file_lst.append(File)
x = 1
for ele in REC_file_lst:
    path = ele

    to_open = open(dir+path, "r").read().split("\n")
    total = []
    for line in to_open:
        lsplit = line.split(",")
        if len(lsplit) >2:
            total.append(lsplit)
    print x
    x+=1
    print dir+path
    save_path = (dir2+"Fasta_RR_NarL.txt")
    for ele2 in total:
        locus = ele2[7]
        fasta = ele2[-1]
        with open(save_path, "a") as f:
            f.write(">")
            f.write(str(locus))
            f.write("\n")
            f.write(str(fasta))
            f.write("\n")
            f.write("\n")
print "finish"

