__author__ = 'kaihami'
""" From a Fasta file separate in 50 sequences"""
import os
Fasta_file_lst = []
Dir = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/"
for File in os.listdir(Dir):
    if File.endswith(".txt"):
        Fasta_file_lst.append(File)

for path in Fasta_file_lst:
    OpenFile = open(Dir+path, "r").read().split("\n")
    x = 0
    w = 0
    Name = path.split(".")[0]
    Name2 = Name.replace("(","-").replace(")","")
    Output_Dir = "/home/kaihami/Desktop/RR_files/REC_Final_By_domain/REC_FASTA_2/FASTA_50_bucket/"
    for y in xrange(0, len(OpenFile)):
        head = OpenFile[y]
        if ">" in head:
            x +=1
            if x <= 100:
                with open(Output_Dir+ Name2 + "_" + str(w)+ ".txt", "a") as f:
                    f.write(OpenFile[y])
                    f.write("\n")
                    f.write(OpenFile[y+1])
                    f.write("\n\n")
            if x == 100:
                x =0
                w+=1
print "finish"
