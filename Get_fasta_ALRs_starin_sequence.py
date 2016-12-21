__author__ = 'kaihami'
"""
Take the REC_Final_by_domain and output a fasta file with a >Locus and the sequence \n\n
"""
import os
dir = "/home/kaihami/Desktop/"
fi = open("/home/kaihami/Desktop/ALR_protein_strains.txt","r").read().split("\n")
ALR_lst = []
for ele in fi:
    if len(ele.split("\t"))>2:
        ALR_lst.append(ele.split("\t"))
save_path = dir+"FASTA_ALR.txt"
for seq in ALR_lst:
    ID = seq[0]
    sequence = seq[-1]

    with open(save_path, "a") as f:
        f.write(">")
        f.write(str(ID))
        f.write("\n")
        f.write(str(sequence))
        f.write("\n")
        f.write("\n")
print "finish"

